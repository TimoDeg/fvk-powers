"""Offline package checks; no model grading, Jira access or automatic installation."""

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit


ENTRYPOINTS = (
    "AGENTS.md", "README.md", "SETUP.md", "CONTEXT.md", "profiles/pm.md",
    "docs/DEPENDENCIES.md", "evals/README.md", "examples/pm.md",
)
PRODUCT_PATHS = (
    "docs/specs/README.md", "docs/specs/features/README.md", "docs/domains",
    "docs/decisions", "docs/decisions/testing-layers-decision.md",
    "docs/decisions/product-entry-deployable.md", "docs/jenkins/ci-cd-documentation.md",
    "deployables/frontend-journey", "deployables/frontend-product-entry",
    "deployables/frontend-pim", "deployables/frontend-sim", "deployables/frontend-crm",
    "deployables/frontend-customer-area", "deployables/monolith/src/Backend/Domains",
    "deployables/monolith/src/Backend/Orchestrators",
    "deployables/monolith/src/BackendForFrontend/Comparison",
    "deployables/monolith/src/BackendForFrontend/Checkout",
)


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args], capture_output=True, text=True, check=True,
    ).stdout.strip()


def check(root, product=None):
    root = root.resolve()
    checks = []

    def record(name, problems):
        checks.append({"name": name, "passed": not problems, "problems": problems})

    # Include untracked additions, exclude ignored local evidence, and inspect tracked leaks.
    names = git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z")
    paths = sorted(set(names.rstrip("\0").split("\0")) - {""})
    record("entrypoints", [p for p in ENTRYPOINTS if p not in paths or not (root / p).is_file()])
    private = [p for p in paths if Path(p).parts[0] in {".local", "runs", "indexes"}
               or Path(p).name == ".env" or Path(p).name.startswith(".env.")]
    record("private_files_excluded", private)
    docs = [p for p in paths if p.endswith(".md")]
    links, private_text = [], []
    for name in docs:
        path = root / name
        if not path.is_file():
            links.append(name + ": missing file")
            continue
        if not path.resolve().is_relative_to(root):
            links.append(name + ": symlink outside package")
            continue
        content = path.read_text(encoding="utf-8")
        if re.search(r"/(?:Users|home)/[^\s/]+/|(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----", content):
            private_text.append(name)
        # ponytail: inline Markdown file links only; use a parser if reference links are introduced.
        for target in re.findall(r"\[[^\]\n]*\]\(([^)\s]+)\)", content):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                links.append(f"{name}: {target}")
    record("local_markdown_links", links)
    record("portable_documentation", private_text)
    cases, errors = [], []
    try:
        cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
        if not isinstance(cases, list) or not cases:
            raise ValueError("Expected nonempty case list")
        seen = set()
        for row in cases:
            if not isinstance(row, dict):
                raise ValueError("Each case must be an object")
            key = row.get("id")
            if not isinstance(key, str) or not key or key in seen:
                raise ValueError("Case IDs must be unique nonempty strings")
            seen.add(key)
            if not isinstance(row.get("prompt"), str) or not row["prompt"].strip():
                raise ValueError(f"{key}: missing prompt")
            sources = row.get("sources")
            if not isinstance(sources, dict) or not sources or not all(isinstance(v, str) and v.strip() for v in sources.values()):
                raise ValueError(f"{key}: missing source text")
            for field in ("must_include", "must_not"):
                values = row.get(field)
                if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                    raise ValueError(f"{key}: missing {field}")
    except (OSError, ValueError) as exc:
        errors.append(str(exc))
    record("evaluation_cases", errors)
    source = None
    if product is not None:
        product = product.resolve()
        missing = [p for p in PRODUCT_PATHS if not (product / p).exists()]
        for name in PRODUCT_PATHS[:2]:
            try:
                if not (product / name).read_text(encoding="utf-8").strip():
                    missing.append(name + ": empty")
            except OSError:
                if name not in missing:
                    missing.append(name + ": unreadable")
        try:
            source = {"head": git(product, "rev-parse", "HEAD"),
                      "dirty": bool(git(product, "status", "--porcelain")),
                      "checked_paths": len(PRODUCT_PATHS), "jira": "NOT_CHECKED"}
        except subprocess.CalledProcessError:
            missing.append("Product Git state unavailable")
        record("product_context_paths", missing)
    return {
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "scope": "package_structure_only",
        "passed": all(c["passed"] for c in checks),
        "checks": checks,
        "inventory": {"markdown_files": len(docs), "eval_cases": len(cases) if isinstance(cases, list) else 0},
        "product_source": source,
        "model_quality": "NOT_MEASURED",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product-repo", type=Path)
    args = parser.parse_args()
    try:
        report = check(Path(__file__).resolve().parents[1], args.product_repo)
    except (OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Package check could not run: {exc}\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
