import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location("eval_run", Path(__file__).resolve().parents[1] / "evals/run.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class EvalRunner(unittest.TestCase):
    def test_link_targets_do_not_count_as_words(self):
        self.assertEqual(runner.words("Laut [der Spec](docs/a%20b.md#x) gilt drei."), 5)

    def test_rubrics_and_results_stay_hidden_from_answering_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            for name in ("AGENTS.md", "evals/cases.json", "docs/VALIDATION.md",
                         "docs/VALIDATION-HISTORY.md", "docs/DEPENDENCIES.md", "tools/check.py"):
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_text("x")
            self.assertEqual(runner.package_files(root), ["AGENTS.md", "docs/DEPENDENCIES.md"])


if __name__ == "__main__":
    unittest.main()
