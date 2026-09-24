import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("jira_stub", ROOT / "tools/jira_stub.py")
stub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stub)
TICKETS = json.loads((ROOT / "evals/fixtures/tickets.json").read_text(encoding="utf-8"))


def call(name, **args):
    with tempfile.NamedTemporaryFile(suffix=".jsonl") as log:
        res = stub.handle({"method": "tools/call", "params": {"name": name, "arguments": args}},
                          TICKETS, "https://example.atlassian.net", log.name)
    return json.loads(res["content"][0]["text"])


class JiraStub(unittest.TestCase):
    def test_default_fields_hide_acceptance_criteria_like_the_real_server(self):
        self.assertNotIn("customfield_10100", call("getJiraIssue", cloudId="x", issueIdOrKey="TEST-42")["fields"])

    def test_field_lookup_finds_acceptance_criteria(self):
        meta = call("getJiraIssueTypeMetaWithFields", cloudId="x", projectIdOrKey="TEST", issueTypeId="10001",
                    requiredFieldsOnly=False)
        field = next(f["fieldId"] for f in meta["fields"] if f["name"] == "Akzeptanzkriterien")
        issue = call("getJiraIssue", cloudId="x", issueIdOrKey="TEST-42", fields=[field], expand="names")
        self.assertIn("Neuladen", issue["fields"][field])
        self.assertEqual(issue["names"][field], "Akzeptanzkriterien")

    def test_required_only_metadata_does_not_show_optional_fields(self):
        meta = call("getJiraIssueTypeMetaWithFields", cloudId="x", projectIdOrKey="TEST", issueTypeId="10001")
        self.assertNotIn("customfield_10100", [f["fieldId"] for f in meta["fields"]])


if __name__ == "__main__":
    unittest.main()
