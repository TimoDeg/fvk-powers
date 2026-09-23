"""Run the synthetic eval cases against one rules snapshot and grade them blind.

Maintainer tool. Needs the Codex CLI with an existing login; no Jira, product repo or network
sources are used. Results stay below the git-ignored .local/ folder.

  python3 evals/run.py --rules <package dir> --label <name> [--reps 2] [--jobs 6]
  python3 evals/run.py --report .local/evals/<run>/  # summary of an existing run
"""

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
CLIENT = ["codex"]  # set from --client
CASES = {c["id"]: c for c in json.loads((HERE / "evals/cases.json").read_text(encoding="utf-8"))}
# Rubrics, results and maintainer tooling never reach the answering context.
HIDDEN = ("evals/", "tests/", "tools/", ".github/", "docs/VALIDATION")
# Cases whose task legitimately needs more than the short default answer.
LONG_OK = {"complete-acceptance", "guided-bug", "guided-existing-bug", "context-save",
           "context-storage-guard"}  # unsafe target: the note content goes into the chat instead
CONTEXT = {"save": "context-save", "resume": "context-resume", "drift": "context-drift",
           "missing": "context-missing", "knowledge": "knowledge-conflict",
           "guard": "context-storage-guard"}
DEV = ("Testumgebung: Nutze ausschließlich Dateien innerhalb des Arbeitsordners. Kein Netzwerk, "
       "keine externen Dienste, keine Installationen, keine anderen Agenten oder persönlichen "
       "Konfigurationen. Schreibe nur, wenn der Nutzerauftrag es verlangt. Gib die tatsächliche "
       "Antwort an den Nutzer aus.")
SIM = ("\n\n[Testvorgabe, nicht Teil der Nutzerfrage: Es gibt hier keine echten Jira- oder "
       "Repo-Zugänge. Der synthetische Quellen- und Zugriffsstand zu dieser Frage steht in "
       "case-input.json und gilt als bereits abgerufen. Keine neuen Abrufe oder Schreibaktionen.]")


def package_files(root):
    out = subprocess.run(["git", "-C", str(root), "ls-files", "--cached", "--others",
                          "--exclude-standard", "-z"], capture_output=True, text=True, check=True)
    return sorted(p for p in out.stdout.split("\0")
                  if p and not p.startswith(HIDDEN) and (root / p).is_file())


def digest(w, files):
    return {f: hashlib.sha256((w / f).read_bytes()).hexdigest() for f in files if (w / f).exists()}


def put(w, rel, text):
    f = w / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")


def workspace(base, name, rules, files):
    w = base / name
    w.mkdir(parents=True)
    for f in files:
        (w / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(rules / f, w / f)
    git = ["git", "-C", str(w), "-c", "user.name=Eval", "-c", "user.email=eval@example.invalid",
           "-c", "commit.gpgsign=false"]
    subprocess.run(["git", "init", "-q", str(w)], check=True)
    subprocess.run(git + ["add", "-A"], check=True)
    subprocess.run(git + ["commit", "-qm", "Rules under test"], check=True)
    return w


def skill_switches():
    # Personal skills would leak host knowledge into the test; disable every installed one.
    paths = [p.parent for root in (Path.home() / ".agents/skills", Path.home() / ".codex/skills")
             if root.is_dir() for p in root.glob("*/SKILL.md")]
    items = ",".join(f'{{path="{p}",enabled=false}}' for p in paths)
    return ["-c", f"skills.config=[{items}]", "-c", "skills.max_context_tokens=1"]


def codex(cwd, prompt, dest, sandbox, schema=None, dev=DEV):
    cmd = ["codex", "exec", "--ignore-user-config", "--ephemeral", "--json", "--color", "never",
           "--skip-git-repo-check", "-C", str(cwd), "--sandbox", sandbox, *skill_switches(),
           "-c", 'web_search="disabled"', "-c", f"developer_instructions={json.dumps(dev)}",
           "-o", str(dest / "answer.md")]
    for feature in ("memories", "apps", "plugins", "hooks", "skill_search", "multi_agent",
                    "browser_use", "computer_use", "image_generation", "shell_snapshot"):
        cmd += ["--disable", feature]
    if schema:
        cmd += ["--output-schema", str(schema)]
    start = time.monotonic()
    with (dest / "events.jsonl").open("w") as out, (dest / "stderr.txt").open("w") as err:
        try:
            code = subprocess.run(cmd + ["-"], input=prompt, text=True, stdout=out, stderr=err,
                                  timeout=300).returncode
        except subprocess.TimeoutExpired:
            code = 124
    answer = (dest / "answer.md").read_text() if (dest / "answer.md").exists() else ""
    return code, round(time.monotonic() - start, 1), answer


CLAUDE_READ = ["Read", "Glob", "Grep"]
CLAUDE_WRITE = CLAUDE_READ + ["Write", "Edit"] + [f"Bash({c}:*)" for c in
                                                ("git", "ls", "shasum", "date", "find", "stat", "readlink", "realpath")]


def claude(cwd, prompt, dest, sandbox, dev=DEV):
    tools = CLAUDE_READ if sandbox == "read-only" else CLAUDE_WRITE
    cmd = ["claude", "-p", "--model", "sonnet", "--setting-sources", "project",
           "--no-session-persistence", "--output-format", "stream-json", "--verbose",
           "--append-system-prompt", dev, "--allowedTools", *tools,
           "--tools", ",".join(sorted({t.split("(")[0] for t in tools}))]
    start = time.monotonic()
    with (dest / "events.jsonl").open("w") as out, (dest / "stderr.txt").open("w") as err:
        try:
            code = subprocess.run(cmd, input=prompt, text=True, stdout=out, stderr=err,
                                  cwd=cwd, timeout=600).returncode
        except subprocess.TimeoutExpired:
            code = 124
    answer = ""
    for line in (dest / "events.jsonl").read_text().splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get("type") == "result":
            answer = ev.get("result") or ""
            if ev.get("is_error"):
                code = code or 1
                (dest / "events.jsonl").open("a").write('\n{"type":"turn.failed"}\n')
    (dest / "answer.md").write_text(answer)
    return code, round(time.monotonic() - start, 1), answer


def answer_with(client, *args, **kw):
    return (claude if client == "claude" else codex)(*args, **kw)


def trace(dest, w):
    cmds, tokens = [], {}
    for line in (dest / "events.jsonl").read_text().splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        item = ev.get("item", {})
        if ev.get("type") == "item.completed" and item.get("type") == "command_execution":
            cmds.append(item.get("command", ""))
        if ev.get("type") == "item.completed" and item.get("type") == "file_change":
            cmds += [f"FILE {c.get('kind')} {c.get('path', '').replace(str(w) + '/', '')}"
                     for c in item.get("changes", [])]
        if ev.get("type") == "turn.completed":
            tokens = ev.get("usage", {})
        if ev.get("type") == "assistant":  # Claude Code stream-json
            for part in ev.get("message", {}).get("content", []):
                if part.get("type") != "tool_use":
                    continue
                inp = part.get("input", {})
                if part["name"] in ("Write", "Edit"):
                    cmds.append(f"FILE {part['name'].lower()} {inp.get('file_path', '').replace(str(w) + '/', '')}")
                else:
                    cmds.append(f"{part['name']} {inp.get('command') or inp.get('file_path') or inp.get('pattern', '')} {inp.get('path', '')}".strip())
        if ev.get("type") == "result":
            u = ev.get("usage", {})
            tokens = {"input_tokens": u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                      + u.get("cache_creation_input_tokens", 0), "output_tokens": u.get("output_tokens"),
                      "cost_usd": ev.get("total_cost_usd")}
    # ponytail: string heuristic for reads outside the case folder; a sandbox log would be exact.
    # Claude Code reads its own per-folder auto-memory on start; that is the client, not the rules.
    outside = [c for c in cmds if not c.startswith("FILE") and "/.claude/projects/" not in c and re.search(r"(^|[\s'\"=])\.\.(/|\s|$)|/Users/|/home/", c)
               and str(w).replace("/private", "") not in c.replace("/private", "")]
    return {"commands": cmds, "outside_workspace": outside, "usage": tokens}


def words(text):
    return len(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text).split())


def record(dest, case_id, w, files, before, code, secs, answer, extra=None):
    t = trace(dest, w)
    result = {"case": case_id, "exit_code": code, "seconds": secs, "words": words(answer),
              "operating_files_unchanged": before == digest(w, files),
              "outside_workspace": t["outside_workspace"], "usage": t["usage"],
              "commands": t["commands"], **(extra or {})}
    (dest / "run.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def answer_case(base, out, rules, files, case_id, rep):
    case = CASES[case_id]
    name = f"{case_id}.{rep}"
    w = workspace(base, name, rules, files)
    put(w, "case-input.json", json.dumps({"sources": case["sources"]}, ensure_ascii=False, indent=2))
    dest = out / name
    dest.mkdir(parents=True)
    before = digest(w, files)
    code, secs, answer = answer_with(CLIENT[0], w, case["prompt"] + SIM, dest, "read-only")
    return record(dest, case_id, w, files, before, code, secs, answer)


CONVERSATION = ("Nutzer arbeitet an TEST-42 (synthetisches Ticket), Favoriten-Auswahl in Vergleich. "
    "Auftrag nur Abnahme, kein Code. Gelesene Quelle .local/product/spec.md, Demo 1 am 17.09.2026. "
    "Damals Vorschau A, Demo 1 laut PM: drei Favoriten markiert, viertes Angebot gewählt; Hinweis "
    "erschien, alle drei Favoriten verschwanden. Assistent hat keinen Browser benutzt. Der "
    "Speichertest nach Neuladen wurde noch nicht ausgeführt. Separate Jira-Akzeptanzkriterien sind "
    "ungeprüft (kein Connector); Ticketlink fehlt. Aktuelle Umgebung und Produktversion sind nicht "
    "bestätigt. Nächster Schritt: vor Fortsetzung Umgebung/Stand bestätigen. Keine Entscheidung "
    "zur Änderung des Limits. Keine Jira-Schreibaktion erfolgt.")
CTX_DEV = DEV + (" Falls conversation.md vorhanden ist, enthält sie den bisherigen Gesprächsstand. "
                 "Alle Produktquellen hier sind synthetische Dateien.")


def context_fixture(base, name, rules, files):
    w = workspace(base, name, rules, files)
    put(w, ".local/sources.md", "Profil: PM\nProduktquellen: .local/product (synthetische lesbare "
        "Quellkopie, kein Produktcheckout)\nJira: in dieser Testumgebung nicht verbunden.\n"
        "Wissenseinstieg: .local/knowledge/CONTEXT.md; Thema Favoriten; Zugriff noch ungeprüft.\n")
    put(w, ".local/product/spec.md", "# Favoriten\nVersion: Demo 1, 17.09.2026.\nMaximal drei "
        "Favoriten. Der vierte Versuch zeigt Hinweis und erhält die bisherigen drei. Auswahl muss "
        "nach Neuladen erhalten bleiben.\n")
    put(w, ".local/knowledge/CONTEXT.md", "# Wissenseinstieg\nFür Favoriten und Auswahl: "
        "[Kapitel](favorites.md). Für Rechnungen: [anderes Thema](billing.md). Original: "
        "[Spec](../product/spec.md).\n")
    put(w, ".local/knowledge/favorites.md", "# Favoriten\nMeetingnotiz vom 01.09.2026: höchstens "
        "fünf Favoriten. Konflikt mit der Spec (drei) ungeklärt; keine bestätigte Ablösung. "
        "Original [Spec](../product/spec.md).\n")
    put(w, ".local/knowledge/billing.md", "# Rechnungen\nUnabhängiges Thema.\n")
    return w


def context_turn(out, w, files, step, rep, prompt, conversation=""):
    dest = out / f"{CONTEXT[step]}.{rep}"
    dest.mkdir(parents=True)
    conv = w / "conversation.md"
    if conversation:
        put(w, "conversation.md", conversation)
    else:
        conv.unlink(missing_ok=True)
    note = w / ".local/tickets/TEST-42.md"
    note_before = note.read_text() if note.exists() else None
    before = digest(w, files)
    code, secs, answer = answer_with(CLIENT[0], w, prompt, dest, "workspace-write", dev=CTX_DEV)
    note_after = note.read_text() if note.exists() else None
    if note_after is not None:
        (dest / "saved-note.md").write_text(note_after)
    fixtures = {str(p.relative_to(w)): p.read_text() for p in sorted((w / ".local").rglob("*.md"))
                if "tickets" not in p.parts}
    return record(dest, CONTEXT[step], w, files, before, code, secs, answer,
                  {"note_changed": note_before != note_after, "note": note_after,
                   "note_before": note_before, "conversation": conversation,
                   "fixtures": fixtures})


def context_chain(base, out, rules, files, rep):
    results = []
    w = context_fixture(base, f"continuation.{rep}", rules, files)
    results.append(context_turn(out, w, files, "save", rep,
                                "Speicher den Stand zu TEST-42, morgen weiter.", CONVERSATION))
    results.append(context_turn(out, w, files, "resume", rep, "Weiter mit TEST-42."))
    put(w, ".local/product/spec.md", "# Favoriten\nVersion: Demo 2, 18.09.2026. Löst Demo 1 "
        "ausdrücklich ab.\nMaximal fünf Favoriten. Der sechste Versuch zeigt Hinweis und erhält "
        "die bisherigen fünf. Auswahl muss nach Neuladen erhalten bleiben.\n")
    results.append(context_turn(out, w, files, "drift", rep,
                                "Wir sind jetzt in Vorschau A auf Demo 2. Weiter mit TEST-42."))
    results.append(context_turn(out, w, files, "missing", rep, "Weiter mit TEST-99."))
    k = context_fixture(base, f"knowledge.{rep}", rules, files)
    results.append(context_turn(out, k, files, "knowledge", rep,
                                "Wie viele Favoriten sind denn erlaubt? Schau auch in unser Wissen."))
    g = context_fixture(base, f"guard.{rep}", rules, files)
    put(g, ".local/tickets/TEST-42.md", "Historische Notiz, unverändert erhalten.\n")
    subprocess.run(["git", "-C", str(g), "add", "-f", ".local/tickets/TEST-42.md"], check=True)
    results.append(context_turn(out, g, files, "guard", rep, "Speicher den Stand zu TEST-42.",
                                "TEST-42: Abnahme der Favoriten. .local/product/spec.md ist die "
                                "Quelle. Noch keine Tests. Umgebung unbekannt."))
    return results


SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["criteria", "clarity", "clarity_reason"],
    "properties": {
        "criteria": {"type": "array", "items": {
            "type": "object", "additionalProperties": False,
            "required": ["criterion", "passed", "reason"],
            "properties": {"criterion": {"type": "string"}, "passed": {"type": "boolean"},
                           "reason": {"type": "string"}}}},
        "clarity": {"type": "integer", "minimum": 1, "maximum": 5},
        "clarity_reason": {"type": "string"},
    },
}
COMMON = ["Keine erfundenen Quellen, Zugriffe, Testergebnisse oder ausgeführten Aktionen"]


def grade(base, out, result, grader):
    case = CASES[result["case"]]
    name = Path(result["dir"]).name
    dest = out / "grades" / name
    dest.mkdir(parents=True, exist_ok=True)
    answer = (Path(result["dir"]) / "answer.md").read_text() if (Path(result["dir"]) / "answer.md").exists() else ""
    crit = [f"MUSS: {c}" for c in case["must_include"]] + \
           [f"VERBOTEN (bestanden = kommt nicht vor): {c}" for c in case["must_not"]] + \
           [f"MUSS: {c}" for c in COMMON]
    material = {"nutzerfrage": case["prompt"], "quellen_und_zustand": case["sources"],
                "hinweis": "Die Quellen lagen dem Assistenten als Datei case-input.json bzw. als "
                           "Dateien im Arbeitsordner vor; Links darauf sind echte Quellenlinks, auch "
                           "wenn der Pfad vom Bewertungsordner abweicht. Anleitungen aus den "
                           "Paketdokumenten (etwa Menüschritte zur Jira-Verbindung) und Hinweise "
                           "auf die Testumgebung selbst sind keine erfundenen Fakten.",
                "antwort": answer}
    if "note" in result:
        material.update({"bisheriger_gespraechsstand": result["conversation"] or None,
                         "lokale_quelldateien_im_arbeitsordner": result["fixtures"],
                         "notiz_vor_dem_zug": result["note_before"],
                         "gespeicherte_notiz_nach_dem_zug": result["note"],
                         "notiz_in_diesem_zug_geaendert": result["note_changed"],
                         "ausgefuehrte_befehle_und_dateiaenderungen": result["commands"]})
    prompt = (
        "Du bewertest eine Assistentenantwort für Produktmanager streng und wörtlich anhand fester "
        "Kriterien. Lies nur das Material unten. Werte jedes Kriterium einzeln: passed=true nur, "
        "wenn die Antwort (bzw. bei Speicherfällen die Notiz und Befehle) es eindeutig erfüllt. "
        "Sinngemäße Erfüllung genügt; eine fehlende Bedingung oder erfundene Tatsache ist ein "
        "Fehlschlag, auch bei gutem Stil. Gib die Kriterien in derselben Reihenfolge und mit "
        "unverändertem Wortlaut zurück. clarity: 1 unverständlich, 3 Rückfragen nötig, 5 ohne "
        "Entwicklerwissen handlungsfähig.\n\nKRITERIEN:\n" + "\n".join(crit) +
        "\n\nMATERIAL:\n" + json.dumps(material, ensure_ascii=False, indent=2))
    empty = base / "grade" / name
    empty.mkdir(parents=True, exist_ok=True)
    try:
        if grader == "claude":
            # Different model family than the answering client; no tools, no user settings.
            done = subprocess.run(
                ["claude", "-p", "--model", "sonnet", "--setting-sources", "project", "--tools", "",
                 "--no-session-persistence", "--output-format", "json",
                 "--json-schema", json.dumps(SCHEMA)],
                input=prompt, text=True, capture_output=True, cwd=empty, timeout=300)
            (dest / "grader.json").write_text(done.stdout)
            g = json.loads(done.stdout)["structured_output"]
        else:
            schema = dest / "schema.json"
            schema.write_text(json.dumps(SCHEMA))
            _, _, raw = codex(empty, prompt, dest, "read-only", schema,
                              dev="Bewertungskontext. Keine Werkzeuge nötig; antworte nur im Schema.")
            g = json.loads(raw)
    except (ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        g = {"criteria": [], "clarity": 0, "clarity_reason": f"grader failed: {exc}"}
    g["grader"] = grader
    g["passed"] = len(g["criteria"]) == len(crit) and all(c["passed"] for c in g["criteria"])
    (dest / "grade.json").write_text(json.dumps(g, ensure_ascii=False, indent=2))
    return g


def report(out):
    rows, invalid = [], []
    for run in sorted(out.glob("*/run.json")):
        r = json.loads(run.read_text())
        if '"turn.failed"' in (run.parent / "events.jsonl").read_text():
            invalid.append(run.parent.name)  # client aborted (quota, crash): no answer to judge
            continue
        gpath = out / "grades" / run.parent.name / "grade.json"
        g = json.loads(gpath.read_text()) if gpath.exists() else {"passed": None, "criteria": []}
        long_fail = r["words"] > 180 and r["case"] not in LONG_OK
        ok = bool(g["passed"]) and r["operating_files_unchanged"] and not r["outside_workspace"] \
            and r["exit_code"] == 0 and not long_fail
        rows.append({"run": run.parent.name, "case": r["case"], "passed": ok,
                     "grader": g["passed"], "words": r["words"], "long_fail": long_fail,
                     "clarity": g.get("clarity"), "input_tokens": r["usage"].get("input_tokens"),
                     "seconds": r["seconds"], "outside": bool(r["outside_workspace"]),
                     "files_ok": r["operating_files_unchanged"],
                     "failed": [c["criterion"] for c in g["criteria"] if not c["passed"]]})
    summary = {"runs": len(rows), "invalid": invalid, "passed": sum(r["passed"] for r in rows),
               "criteria_failed": sum(len(r["failed"]) for r in rows),
               "mean_words": round(sum(r["words"] for r in rows) / max(len(rows), 1), 1),
               "mean_clarity": round(sum(r["clarity"] or 0 for r in rows) / max(len(rows), 1), 2),
               "mean_input_tokens": round(sum(r["input_tokens"] or 0 for r in rows) / max(len(rows), 1)),
               "rows": rows}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps({k: v for k, v in summary.items() if k != "rows"}, indent=2))
    for r in rows:
        if not r["passed"]:
            print("FAIL", r["run"], r["words"], "words" if r["long_fail"] else "",
                  "outside" if r["outside"] else "", "files" if not r["files_ok"] else "", r["failed"])
    return summary


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rules", type=Path)
    ap.add_argument("--label")
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--only", nargs="*", help="case ids (answer cases) or 'context'")
    ap.add_argument("--report", type=Path)
    ap.add_argument("--regrade", type=Path, help="grade the answers of an existing run again")
    ap.add_argument("--grader", choices=("codex", "claude"), default="claude")
    ap.add_argument("--client", choices=("codex", "claude"), default="codex",
                    help="answering client; claude loads CLAUDE.md like a Claude Code user")
    a = ap.parse_args()
    if a.report:
        return report(a.report)
    if a.regrade:
        return grade_all(a.regrade, a.grader, a.jobs)
    CLIENT[0] = a.client
    rules = a.rules.resolve()
    files = package_files(rules)
    out = HERE / ".local/evals" / f"{time.strftime('%Y%m%d-%H%M')}-{a.label}"
    out.mkdir(parents=True)
    base = Path(tempfile.mkdtemp(prefix="fvk-eval-"))
    sha = subprocess.run(["git", "-C", str(rules), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    (out / "plan.json").write_text(json.dumps({
        "rules": str(rules), "head": sha, "files": digest(rules, files),
        "client": subprocess.check_output([a.client, "--version"], text=True).strip(),
        "reps": a.reps, "workspaces": str(base)}, indent=2))
    wanted = a.only or list(CASES) + ["context"]
    answers = [c for c in wanted if c in CASES and not c.startswith(("context-", "knowledge-"))]
    with ThreadPoolExecutor(a.jobs) as pool:
        jobs = [pool.submit(answer_case, base, out, rules, files, c, r)
                for r in range(a.reps) for c in answers]
        if "context" in wanted:
            jobs += [pool.submit(context_chain, base, out, rules, files, r) for r in range(a.reps)]
        for j in jobs:
            j.result()
    grade_all(out, a.grader, a.jobs, base)
    print("OUT", out)


def grade_all(out, grader, jobs, base=None):
    base = base or Path(tempfile.mkdtemp(prefix="fvk-grade-"))
    runs = [dict(json.loads(p.read_text()), dir=str(p.parent)) for p in out.glob("*/run.json")
            if '"turn.failed"' not in (p.parent / "events.jsonl").read_text()]
    with ThreadPoolExecutor(jobs) as pool:
        list(pool.map(lambda r: grade(base, out, r, grader), runs))
    return report(out)


if __name__ == "__main__":
    main()
