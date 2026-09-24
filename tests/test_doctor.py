import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location("doctor", Path(__file__).resolve().parents[1] / "tools/doctor.py")
doctor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(doctor)


def repo(path, files):
    path.mkdir(parents=True)
    subprocess.run(["git", "init", "-q", str(path)], check=True)
    for name, text in files.items():
        (path / name).parent.mkdir(parents=True, exist_ok=True)
        (path / name).write_text(text)
    subprocess.run(["git", "-C", str(path), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(path), "-c", "user.name=T", "-c", "user.email=t@example.invalid",
                    "-c", "commit.gpgsign=false", "commit", "-qm", "init"], check=True)


class Doctor(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.work = Path(tmp.name)
        self.powers = self.work / "fvk-powers"
        repo(self.powers, {".gitignore": ".local/\n", "AGENTS.md": "x"})
        product = {m + "/.keep": "" for m in doctor.REWRITE_MARKERS}
        product.update({e: "# Specs" for e in doctor.SPEC_ENTRIES})
        repo(self.work / "fvk", product)

    def status(self, report, area):
        return next(r["status"] for r in report["checks"] if r["area"] == area)

    def test_sibling_layout_passes_without_sources(self):
        report = doctor.check(self.powers)
        self.assertTrue(report["passed"])
        self.assertEqual(self.status(report, "Quellenangaben"), "OFFEN")

    def test_sources_path_with_note_is_used(self):
        (self.work / "fvk").rename(self.work / "rewrite")
        (self.powers / ".local").mkdir()
        (self.powers / ".local/sources.md").write_text("Produktrepo: ../rewrite (bestätigt am 23.09.)\n")
        self.assertEqual(self.status(doctor.check(self.powers), "Produktrepo"), "OK")

    def test_empty_value_does_not_swallow_next_key(self):
        (self.powers / ".local").mkdir()
        (self.powers / ".local/sources.md").write_text("Infrastruktur:\nJira-Site: https://example.atlassian.net\n")
        self.assertEqual(self.status(doctor.check(self.powers), "Jira"), "OK")

    def test_wrong_repo_fails(self):
        (self.powers / ".local").mkdir()
        (self.powers / ".local/sources.md").write_text("Produktrepo: .\n")
        self.assertFalse(doctor.check(self.powers)["passed"])

    def test_tracked_private_file_fails(self):
        (self.powers / ".local").mkdir()
        (self.powers / ".local/sources.md").write_text("Profil: PM\n")
        subprocess.run(["git", "-C", str(self.powers), "add", "-f", ".local/sources.md"], check=True)
        self.assertEqual(self.status(doctor.check(self.powers), "Lokaler Speicher"), "FEHLT")


if __name__ == "__main__":
    unittest.main()
