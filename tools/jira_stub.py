"""Read-only stand-in for the Atlassian MCP server, for offline setup tests.

Speaks MCP over stdio (newline-delimited JSON-RPC) and serves synthetic tickets from a JSON
file. Every call is appended to --log so a test can check which tickets and fields were read.
No network, no writes to any tracker.

  python3 tools/jira_stub.py --tickets evals/fixtures/tickets.json --log calls.jsonl
"""

import argparse
import json
import sys
from pathlib import Path

# Mirrors the Atlassian MCP defaults: without `fields` only standard fields come back, custom fields
# such as acceptance criteria only by id, via "*all", or after a field lookup.
DEFAULT_FIELDS = ("summary", "description", "status", "issuetype", "priority", "labels", "components",
                  "assignee", "reporter", "created", "updated", "resolution", "project")
TOOLS = [
    {"name": "getJiraIssue",
     "description": "Get issue details",
     "inputSchema": {"type": "object", "required": ["cloudId", "issueIdOrKey"], "properties": {
         "cloudId": {"type": "string", "description": "Cloud ID (UUID or site URL)"},
         "issueIdOrKey": {"type": "string"},
         "fields": {"type": "array", "items": {"type": "string"},
                    "description": "Issue fields to return. When omitted or empty, defaults to: "
                                   + ", ".join(DEFAULT_FIELDS) + '. Pass "*all" to return every field '
                                   "(including custom fields)."},
         "expand": {"type": "string", "description": "Additional issue details to expand in the "
                                                     "response (for example, renderedFields or names)."}}}},
    {"name": "getJiraIssueTypeMetaWithFields",
     "description": "Get field metadata",
     "inputSchema": {"type": "object", "required": ["cloudId", "projectIdOrKey", "issueTypeId"], "properties": {
         "cloudId": {"type": "string"}, "projectIdOrKey": {"type": "string"}, "issueTypeId": {"type": "string"},
         "requiredFieldsOnly": {"type": "boolean", "description": "When true (default), returns only the "
                                "fields that are required to create an issue of this type."}}}},
    {"name": "getAccessibleAtlassianResources",
     "description": "List the Atlassian sites this login can read.",
     "inputSchema": {"type": "object", "properties": {}}},
]
FIELD_NAMES = {"summary": "Summary", "description": "Description", "status": "Status", "issuetype": "Issue Type",
               "project": "Project", "updated": "Updated", "assignee": "Assignee",
               "customfield_10100": "Akzeptanzkriterien"}
REQUIRED = {"summary", "issuetype", "project"}


def handle(msg, tickets, site, log):
    method, params = msg.get("method"), msg.get("params") or {}
    if method == "initialize":
        return {"protocolVersion": params.get("protocolVersion", "2025-06-18"),
                "capabilities": {"tools": {}}, "serverInfo": {"name": "jira-stub", "version": "1"}}
    if method == "tools/list":
        return {"tools": TOOLS}
    if method == "tools/call":
        name, args = params.get("name"), params.get("arguments") or {}
        with open(log, "a", encoding="utf-8") as f:
            f.write(json.dumps({"tool": name, "arguments": args}) + "\n")
        if name == "getAccessibleAtlassianResources":
            text = json.dumps([{"id": "stub-cloud", "url": site, "name": "Testsite"}])
            return {"content": [{"type": "text", "text": text}]}
        if name == "getJiraIssueTypeMetaWithFields":
            only_required = args.get("requiredFieldsOnly", True)
            fields = [{"fieldId": f, "name": n, "required": f in REQUIRED}
                      for f, n in FIELD_NAMES.items() if f in REQUIRED or not only_required]
            return {"content": [{"type": "text", "text": json.dumps({"fields": fields}, ensure_ascii=False)}]}
        key = str(args.get("issueIdOrKey", "")).rsplit("/", 1)[-1].upper()
        issue = tickets.get(key)
        if issue is None:
            return {"content": [{"type": "text", "text": f"Issue {key} does not exist or you lack permission."}],
                    "isError": True}
        wanted = args.get("fields") or DEFAULT_FIELDS
        if "*all" in wanted:
            wanted = list(issue)
        fields = {f: issue[f] for f in wanted if f in issue}
        body = {"key": key, "fields": fields}
        if "names" in str(args.get("expand", "")):
            body["names"] = {f: FIELD_NAMES.get(f, f) for f in fields}
        return {"content": [{"type": "text", "text": json.dumps(body, ensure_ascii=False)}]}
    if method == "ping":
        return {}
    raise LookupError(method)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tickets", type=Path, required=True)
    ap.add_argument("--log", type=Path, required=True)
    ap.add_argument("--site", default="https://example.atlassian.net")
    a = ap.parse_args()
    tickets = {k.upper(): v for k, v in json.loads(a.tickets.read_text(encoding="utf-8")).items()}
    for line in sys.stdin:
        if not line.strip():
            continue
        msg = json.loads(line)
        if "id" not in msg:  # notification, e.g. notifications/initialized
            continue
        try:
            reply = {"jsonrpc": "2.0", "id": msg["id"], "result": handle(msg, tickets, a.site, a.log)}
        except LookupError as exc:
            reply = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32601, "message": f"unknown method {exc}"}}
        sys.stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
