"""Check the local fvk-powers workspace: folder layout, repositories, private files.

Read-only: no Jira call, no fetch, no install. The assistant runs it during setup and translates
the result for the user.

  python3 tools/doctor.py [--json]
"""

import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULTS = {"Produktrepo": "../fvk", "Infrastruktur": "../fvk-infrastructure"}
SPEC_ENTRIES = ("docs/specs/README.md", "docs/specs/features/README.md")
REWRITE_MARKERS = ("docs/specs/features", "deployables/monolith", "deployables/frontend-journey")
ENGINE = "deployables/frontend-journey/e2e-scenario-engine"


def git(path, *args):
    done = subprocess.run(["git", "-C", str(path), *args], capture_output=True, text=True)
    return done.stdout.strip() if done.returncode == 0 else None


def read_sources(root):
    """`Schlüssel: Wert` lines from .local/sources.md; everything else is free text."""
    path = root / ".local/sources.md"
    if not path.is_file():
        return {}
    pairs = re.findall(r"^[-*]?[ \t]*([A-Za-zÄÖÜäöü-]+):[ \t]*(\S.*?)[ \t]*$", path.read_text(encoding="utf-8"), re.M)
    # Tolerate an explanatory note after the value: "Produktrepo: ../fvk (bestätigt am …)".
    return {k: re.sub(r"\s+\(.*\)\.?$", "", v) for k, v in pairs}


def resolve(root, value):
    return (root / value).resolve() if not Path(value).is_absolute() else Path(value)


def repo_state(path):
    top = git(path, "rev-parse", "--show-toplevel")
    if top is None:
        return None
    return {"toplevel": top, "head": git(path, "rev-parse", "--short", "HEAD"),
            "branch": git(path, "branch", "--show-current") or "(detached)",
            "changes": len((git(path, "status", "--porcelain") or "").splitlines())}


def check(root=ROOT):
    rows = []

    def row(area, status, detail, required=False):
        rows.append({"area": area, "status": status, "detail": detail, "required": required})

    own = repo_state(root)
    row("fvk-powers", "OK" if own else "FEHLT", f"{own['branch']} @ {own['head']}" if own
        else "kein Git-Checkout", required=True)
    ignored = git(root, "check-ignore", "-q", ".local/probe") is not None
    tracked = (git(root, "ls-files", ".local") or "").splitlines()
    row("Lokaler Speicher", "OK" if ignored and not tracked else "FEHLT",
        ".local/ ignoriert, nichts getrackt" if ignored and not tracked
        else f"ignoriert={ignored}, getrackt={tracked[:3]}", required=True)

    sources = read_sources(root)
    row("Quellenangaben", "OK" if sources else "OFFEN",
        ".local/sources.md gelesen" if sources else ".local/sources.md fehlt, Standardpfade geprüft")

    product = resolve(root, sources.get("Produktrepo", DEFAULTS["Produktrepo"]))
    state = repo_state(product) if product.is_dir() else None
    if state is None:
        row("Produktrepo", "FEHLT", f"{product} ist kein Git-Checkout; erwartet als Ordner fvk direkt neben fvk-powers",
            required=True)
    else:
        missing = [m for m in REWRITE_MARKERS if not (product / m).exists()]
        unreadable = [e for e in SPEC_ENTRIES
                      if not (product / e).is_file() or not (product / e).read_text(encoding="utf-8").strip()]
        ok = not missing and not unreadable and Path(state["toplevel"]).resolve() == product
        row("Produktrepo", "OK" if ok else "FEHLT",
            f"{product.name}: {state['branch']} @ {state['head']}, {state['changes']} lokale Änderungen"
            + (f"; fehlt: {', '.join(missing + unreadable)}" if not ok else ""), required=True)
        engine = product / ENGINE
        if engine.is_dir():
            installed = (engine / "node_modules").is_dir()
            row("Scenario-Engine", "OK" if installed else "OFFEN",
                "installiert" if installed else "vorhanden, nicht installiert (nur für Browser-Abnahme nötig)")

    infra = resolve(root, sources.get("Infrastruktur", DEFAULTS["Infrastruktur"]))
    infra_state = repo_state(infra) if infra.is_dir() else None
    row("Infrastruktur", "OK" if infra_state else "OFFEN",
        f"{infra.name}: {infra_state['branch']} @ {infra_state['head']}" if infra_state
        else "optional; nötig für „Ist es live?“")

    row("Jira", "OK" if "Jira-Site" in sources else "OFFEN",
        f"{sources['Jira-Site']} gespeichert; Zugriff prüft nur ein Ticketabruf" if "Jira-Site" in sources
        else "Site unbekannt; Zugriff prüft nur ein echter Ticketabruf")
    for name, label in ((".local/profile.md", "Profil"), (".local/glossary.md", "Glossar")):
        row(label, "OK" if (root / name).is_file() else "OFFEN",
            name if (root / name).is_file() else f"{name} noch nicht angelegt")

    return {"passed": all(r["status"] == "OK" for r in rows if r["required"]), "checks": rows}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--root", type=Path, default=ROOT, help="fvk-powers checkout to inspect")
    a = ap.parse_args()
    report = check(a.root.resolve())
    if a.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for r in report["checks"]:
            print(f"{r['status']:6} {r['area']:18} {r['detail']}")
    raise SystemExit(0 if report["passed"] else 1)
