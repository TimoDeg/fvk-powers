import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools/remember.py"


class Remember(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        (self.root / "tools").mkdir()
        shutil.copy(SCRIPT, self.root / "tools/remember.py")
        (self.root / ".gitignore").write_text(".local/\n")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)

    def write(self, rel, text="neu\n"):
        return subprocess.run(["python3", "tools/remember.py", rel], cwd=self.root, input=text,
                              capture_output=True, text=True)

    def test_writes_ignored_untracked_file(self):
        done = self.write(".local/tickets/TEST-42.md")
        self.assertEqual(done.returncode, 0, done.stdout)
        self.assertEqual((self.root / ".local/tickets/TEST-42.md").read_text(), "neu\n")

    def test_refuses_tracked_file(self):
        note = self.root / ".local/tickets/TEST-42.md"
        note.parent.mkdir(parents=True)
        note.write_text("alt\n")
        subprocess.run(["git", "-C", str(self.root), "add", "-f", str(note)], check=True)
        done = self.write(".local/tickets/TEST-42.md")
        self.assertEqual(done.returncode, 1)
        self.assertIn("verfolgt", done.stdout)
        self.assertEqual(note.read_text(), "alt\n")

    def test_refuses_outside_local_and_unignored(self):
        self.assertEqual(self.write("README.md").returncode, 1)
        (self.root / ".gitignore").write_text("")
        self.assertEqual(self.write(".local/profile.md").returncode, 1)
        self.assertFalse((self.root / ".local/profile.md").exists())


if __name__ == "__main__":
    unittest.main()
