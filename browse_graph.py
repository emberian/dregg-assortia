#!/usr/bin/env python3
"""Read the orientation graph without a database or network connection."""
import argparse
import json
from pathlib import Path

root = Path(__file__).resolve().parent
nodes = json.loads((root / "graph.jsonld").read_text())["@graph"]
by_id = {item["@id"]: item for item in nodes}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--id", help="Record ID, for example C-DOC-DURABLE")
parser.add_argument("--type", choices=["Claim", "WorkItem", "Question", "Intent", "Hypothesis"])
args = parser.parse_args()
if args.id:
    selected = [item for item in nodes if item["@id"].rsplit(":", 1)[-1] == args.id]
    if not selected:
        raise SystemExit("No such record: " + args.id)
else:
    selected = [item for item in nodes
                if item.get("@type") == args.type] if args.type else [
        item for item in nodes if item.get("@type") in ("Claim", "WorkItem", "Question")]
for item in selected:
    print(item["@id"].rsplit(":", 1)[-1] + " | " + item["@type"] + " | " + item["label"])
    print("  " + item.get("description", ""))
    if args.id:
        for key in ("evidenceKind", "scope", "limitations", "status", "closure"):
            if item.get(key):
                print("  " + key + ": " + str(item[key]))
        for ident in item.get("sources", []):
            source = by_id[ident]
            if "path" in source:
                repo = by_id[source["repository"]]
                location = str(Path(repo["localPath"]) / source["path"])
                if source.get("lineStart"):
                    location += ":" + str(source["lineStart"])
                print("  source: " + location)
            else:
                print("  source: " + source.get("label", ident))
    print()
