"""Write the local memory safely: stdin becomes the file, but only below .local/ and only if Git
ignores the path and does not track it. Otherwise nothing is written and the exit code is 1.

  python3 tools/remember.py .local/tickets/TEST-42.md <<'EOF'
  <complete new file content>
  EOF
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(rel):
    """Reason why rel must not be written, or None."""
    target = (ROOT / rel).resolve()
    if (ROOT / ".local").resolve() not in target.parents:
        return f"{rel} liegt nicht unter .local/"
    if subprocess.run(["git", "-C", str(ROOT), "ls-files", "--error-unmatch", rel], capture_output=True).returncode == 0:
        return f"{rel} wird bereits von Git verfolgt"
    if subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", rel]).returncode != 0:
        return f"{rel} ist nicht von Git ausgeschlossen"
    return None


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    reason = check(argv[1])
    if reason:
        print(f"NICHT GESPEICHERT: {reason}. Nichts geändert.")
        return 1
    target = ROOT / argv[1]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(sys.stdin.read(), encoding="utf-8")
    print(f"GESPEICHERT: {argv[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
