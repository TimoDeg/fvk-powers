"""Build a throw-away workspace to run the fvk-powers setup as a new user would.

Layout follows SETUP.md: <dest>/fvk-powers next to <dest>/fvk. fvk-powers is a fresh clone of
the current commit plus uncommitted changes to tracked files; nothing from .local/ is copied.
The product repo is a small synthetic Rewrite fixture, or with --product a local shared clone
(read-only for the source repo, no network). Jira is the offline stub from tools/jira_stub.py.

  python3 tools/fresh_env.py [--dest DIR] [--product ../fvk]

Prints the commands to start Claude Code or Codex without personal settings, skills or memory.
"""

import argparse
import json
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = {
    "docs/specs/README.md": "# Specs\n\nFeature-Specs liegen unter `features/`. Status und Zuständigkeit pflegt der Spec-Bot.\n",
    "docs/specs/features/README.md": "# Feature-Specs\n\n- [Favoriten](favorites.md)\n",
    "docs/specs/features/favorites.md": (
        "# Favoriten im Vergleich\n\n## Verhalten\n\nKunden markieren bis zu drei Angebote als Favoriten. "
        "Beim vierten Versuch erscheint ein Hinweis; die bisherigen drei bleiben ausgewählt.\n\n"
        "## Speicherung\n\nMit Konto bleibt die Auswahl nach Neuladen erhalten. Ohne Anmeldung endet sie mit der Sitzung.\n\n"
        "## Begriffe\n\n- **Favorit:** ein im Vergleich gemerktes Angebot, höchstens drei gleichzeitig.\n"),
    "docs/domains/README.md": "# Domains\n\n- **Vergleich:** Ergebnisliste der Tarife nach der Eingabe.\n",
    "deployables/monolith/README.md": "# Monolith\n",
    "deployables/frontend-journey/README.md": "# Journey\n",
}
GIT_ID = ["-c", "user.name=Fresh Env", "-c", "user.email=fresh@example.invalid", "-c", "commit.gpgsign=false"]


def run(*cmd, cwd=None):
    subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)


def build(dest, product=None):
    dest = Path(dest).resolve()
    dest.mkdir(parents=True, exist_ok=True)
    powers = dest / "fvk-powers"
    run("git", "clone", "-q", "--no-hardlinks", str(ROOT), str(powers))
    # Carry uncommitted edits to tracked files so a rule change can be tried before committing.
    diff = subprocess.run(["git", "-C", str(ROOT), "diff", "HEAD", "--binary"], capture_output=True, check=True).stdout
    if diff:
        subprocess.run(["git", "-C", str(powers), "apply", "-"], input=diff, check=True)
    for extra in subprocess.run(["git", "-C", str(ROOT), "ls-files", "--others", "--exclude-standard"],
                                capture_output=True, text=True, check=True).stdout.splitlines():
        (powers / extra).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / extra, powers / extra)
    run("git", "-C", str(powers), "add", "-A")
    if subprocess.run(["git", "-C", str(powers), "diff", "--cached", "--quiet"]).returncode:
        run("git", "-C", str(powers), *GIT_ID, "commit", "-qm", "Work in progress under test")
    fvk = dest / "fvk"
    if product:
        run("git", "clone", "-q", "--shared", str(Path(product).resolve()), str(fvk))
    else:
        for rel, text in FIXTURE.items():
            (fvk / rel).parent.mkdir(parents=True, exist_ok=True)
            (fvk / rel).write_text(text, encoding="utf-8")
        run("git", "init", "-q", str(fvk))
        run("git", "-C", str(fvk), "add", "-A")
        run("git", "-C", str(fvk), *GIT_ID, "commit", "-qm", "Synthetic Rewrite fixture")
    stub = dest / "jira-stub"
    stub.mkdir(exist_ok=True)
    shutil.copyfile(ROOT / "evals/fixtures/tickets.json", stub / "tickets.json")
    mcp = {"mcpServers": {"atlassian": {"command": sys.executable, "args": [
        str(powers / "tools/jira_stub.py"), "--tickets", str(stub / "tickets.json"), "--log", str(stub / "calls.jsonl")]}}}
    (stub / "mcp.json").write_text(json.dumps(mcp, indent=2))
    # Codex lists personal skills (~/.codex/skills, ~/.agents/skills) even when disabled; an empty HOME
    # with only the login linked in is the only reliable way to hide them.
    home = dest / "home"
    (home / ".codex").mkdir(parents=True, exist_ok=True)
    auth = Path.home() / ".codex/auth.json"
    if auth.is_file() and not (home / ".codex/auth.json").exists():
        (home / ".codex/auth.json").symlink_to(auth)
    return {"dest": dest, "powers": powers, "product": fvk, "mcp": stub / "mcp.json", "calls": stub / "calls.jsonl",
            "home": home}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dest", type=Path)
    ap.add_argument("--product", type=Path, help="local Rewrite checkout to clone instead of the fixture")
    a = ap.parse_args()
    env = build(a.dest or tempfile.mkdtemp(prefix="fvk-fresh-"), a.product)
    stub = json.loads(env["mcp"].read_text())["mcpServers"]["atlassian"]
    # -c instead of `codex mcp add`: that would write the stub into the personal ~/.codex/config.toml.
    codex_mcp = " -c ".join(shlex.quote(f"mcp_servers.atlassian.{k}={json.dumps(stub[k])}") for k in ("command", "args"))
    print(f"""Arbeitsordner: {env['dest']}
  fvk-powers: {env['powers']}
  fvk:        {env['product']} ({'Klon von ' + str(a.product) if a.product else 'synthetische Specs'})
  Jira-Stub:  Tickets TEST-42, TEST-43 unter https://example.atlassian.net/browse/<KEY>

Claude Code, ohne persönliche Einstellungen, nur mit dem Jira-Stub:
  cd {env['powers']} && claude --setting-sources project --strict-mcp-config --mcp-config {env['mcp']}

Codex, ohne persönliche Konfiguration und Skills, nur mit dem Jira-Stub:
  cd {env['powers']} && HOME={env['home']} CODEX_HOME={env['home']}/.codex codex --ignore-user-config --disable plugins --disable apps --disable memories -c {codex_mcp}

Dann: „Richte fvk-powers für mich ein. Mein Ticket: https://example.atlassian.net/browse/TEST-42“
Aufgerufene Jira-Tools stehen danach in {env['calls']}. Aufräumen: rm -rf {env['dest']}""")


if __name__ == "__main__":
    main()
