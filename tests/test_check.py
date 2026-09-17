import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location("package_check", Path(__file__).resolve().parents[1] / "tools/check.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)
        for name in checker.ENTRYPOINTS:
            self.write(name, "# Example\n")
        self.write(".gitignore", ".local/\n.env\nruns/\nindexes/\n")
        self.cases = [{"id": "a", "prompt": "Explain", "sources": {"ticket": "Example"},
                       "must_include": ["condition"], "must_not": ["fabrication"]}]
        self.write_cases()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_cases(self):
        self.write("evals/cases.json", json.dumps(self.cases))

    def passes(self, name):
        return next(c["passed"] for c in checker.check(self.root)["checks"] if c["name"] == name)

    def test_clean_package(self):
        self.assertTrue(checker.check(self.root)["passed"])

    def test_broken_link_fails(self):
        self.write("README.md", "[Missing](missing.md)")
        self.assertFalse(self.passes("local_markdown_links"))

    def test_parent_escape_fails_even_when_file_exists(self):
        self.write("README.md", "[Outside](../)")
        self.assertFalse(self.passes("local_markdown_links"))

    def test_encoded_space_link_passes(self):
        self.write("examples/some file.md", "Example")
        self.write("README.md", "[Example](examples/some%20file.md)")
        self.assertTrue(self.passes("local_markdown_links"))

    def test_missing_entrypoint_fails(self):
        (self.root / "SETUP.md").unlink()
        self.assertFalse(self.passes("entrypoints"))

    def test_ignored_local_evidence_is_not_published(self):
        self.write(".local/note.md", "[Private broken link](missing.md)")
        self.assertTrue(checker.check(self.root)["passed"])

    def test_force_tracked_private_file_fails(self):
        self.write(".local/sources.md", "Private")
        subprocess.run(["git", "-C", str(self.root), "add", "-f", ".local/sources.md"], check=True)
        self.assertFalse(self.passes("private_files_excluded"))

    def test_personal_path_fails(self):
        self.write("README.md", "Read /Users/example/private/file.md")
        self.assertFalse(self.passes("portable_documentation"))

    def test_duplicate_eval_id_fails(self):
        self.cases.append(self.cases[0].copy())
        self.write_cases()
        self.assertFalse(self.passes("evaluation_cases"))

    def test_missing_eval_expectations_fail(self):
        del self.cases[0]["must_not"]
        self.write_cases()
        self.assertFalse(self.passes("evaluation_cases"))

    def test_invalid_eval_json_fails(self):
        self.write("evals/cases.json", "{")
        self.assertFalse(self.passes("evaluation_cases"))

    def test_nonexistent_product_is_not_ready(self):
        report = checker.check(self.root, self.root / "missing-product")
        self.assertFalse(report["passed"])
        self.assertEqual(report["model_quality"], "NOT_MEASURED")


if __name__ == "__main__":
    unittest.main()
