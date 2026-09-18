#!/usr/bin/env python3
"""Check source identity and graph references. This does not verify project claims."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
graph = json.loads((ROOT / "graph.jsonld").read_text())["@graph"]
by_id = {item["@id"]: item for item in graph}
if len(by_id) != len(graph):
    raise SystemExit("Duplicate graph identities")
errors = []
links = ("subject", "object", "sources", "dependsOn", "motivatedBy", "related", "repository")
for item in graph:
    for key in links:
        values = item.get(key, [])
        if isinstance(values, str):
            values = [values]
        for value in values:
            if value not in by_id:
                errors.append(f"Broken {key}: {item['@id']} -> {value}")
changed = []
checked = 0
head_moved = set()
for item in graph:
    if item.get("@type") != "Source" or "path" not in item:
        continue
    repo = by_id[item["repository"]]
    path = Path(repo["localPath"]) / item["path"]
    if not path.is_file():
        changed.append(f"MISSING {path}")
        continue
    checked += 1
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != item["sha256"]:
        changed.append(f"CHANGED {path}")
    if repo["@id"] not in head_moved and item.get("gitHead"):
        result = subprocess.run(
            ["git", "-C", repo["localPath"], "rev-parse", "HEAD"],
            capture_output=True, text=True, check=False)
        if result.returncode or result.stdout.strip() != item["gitHead"]:
            head_moved.add(repo["@id"])
for message in errors + changed:
    print(message)
for ident in sorted(head_moved):
    print("HEAD MOVED (inspect dependency scope):", by_id[ident]["label"])
print(f"{checked} file sources checked; {len(changed)} missing/changed; "
      f"{len(errors)} broken graph references; {len(head_moved)} moved repository heads.")
print("This checks source freshness, not correctness, test success, or deployment.")
# A repository can advance without changing any inspected file. Preserve the
# recorded HEAD as provenance and report movement for context; content hashes
# decide whether this source snapshot needs reinspection.
raise SystemExit(1 if errors or changed else 0)
