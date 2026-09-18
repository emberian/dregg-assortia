#!/usr/bin/env python3
"""Current project work from graph.jsonld; Python 3.10+, standard library only.

This validates project bookkeeping, not program correctness or deployment.
It needs no sibling repositories, network, or local absolute paths.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATES = ("ready", "active", "blocked", "backlog", "done")
RELATIONS = ("subject", "object", "sources", "dependsOn", "motivatedBy",
             "related", "repository", "blockedBy", "advances", "milestone", "workItems", "completionEvidence")


def short(ident):
    return ident.rsplit(":", 1)[-1]


def refs(record, key):
    value = record.get(key, [])
    return [value] if isinstance(value, str) else value


def validate(nodes):
    errors = []
    index = {n["@id"]: n for n in nodes}
    if len(index) != len(nodes):
        errors.append("Duplicate graph identities")
    for node in nodes:
        ident = short(node["@id"])
        for key in RELATIONS:
            for target in refs(node, key):
                if target not in index:
                    errors.append(f"{ident}: broken {key} -> {target}")
        if node.get("@type") != "WorkItem":
            continue
        if node.get("status") not in STATES:
            errors.append(f"{ident}: invalid work status")
        for key in ("closure", "nextAction", "updatedAt", "advances", "sources"):
            if not node.get(key):
                errors.append(f"{ident}: missing {key}")
        if node.get("status") == "active" and not node.get("owner"):
            errors.append(f"{ident}: active work has no owner")
        if node.get("status") == "ready":
            if node.get("blockedBy"):
                errors.append(f"{ident}: ready work still has blocking dependencies")
            for key in ("brief", "writeScope", "acceptance"):
                if not node.get(key):
                    errors.append(f"{ident}: ready work has no {key}")
        if node.get("status") == "blocked" and not node.get("blockedBy"):
            errors.append(f"{ident}: blocked work needs a named blocking record")
        if node.get("status") == "done" and not node.get("completionEvidence"):
            errors.append(f"{ident}: done work needs explicit completion evidence")
        for target in node.get("blockedBy", []):
            if index.get(target, {}).get("status") == "done":
                errors.append(f"{ident}: completed blocker {short(target)} needs reassessment")
    # A dependency cycle is not a runnable plan. Report it without recursion loops.
    visiting, visited = set(), set()

    def visit(ident):
        if ident in visiting:
            errors.append(f"Blocking dependency cycle at {short(ident)}")
            return
        if ident in visited or ident not in index:
            return
        visiting.add(ident)
        for target in index[ident].get("blockedBy", []):
            visit(target)
        visiting.remove(ident)
        visited.add(ident)

    for ident in sorted(index):
        visit(ident)
    return errors


def work(nodes, status=None):
    return sorted((n for n in nodes if n.get("@type") == "WorkItem"
                   and (status is None or n["status"] == status)),
                  key=lambda n: (n.get("priority", 9), short(n["@id"])))


def clean(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(nodes):
    index = {n["@id"]: n for n in nodes}
    items = work(nodes)
    updated = max(n["updatedAt"] for n in items)
    lines = ["# Current work", "", "> Generated from `graph.jsonld` by `python3 hub.py render`. Edit the graph, not this file.",
             "", f"Latest work-record update: **{updated}**. This is recorded project state, not a live process monitor.",
             "", "[New contributor](contributing/README.md) · [Project map](MAP.md) · [Detailed work records](work/records.md)",
             "", "`ready` means a scoped task can be picked up; `active` names its current owner; `blocked` names a prerequisite; `backlog` is unassigned future work. A component pass does not close an integration task."]
    for state in STATES:
        group = work(nodes, state)
        if not group:
            continue
        lines += ["", f"## {state.capitalize()}", "", "| Work | Owner / reviewer | Next action |", "|---|---|---|"]
        for n in group:
            ident = short(n["@id"])
            link = n.get("brief", f"work/records.md#{ident.lower()}")
            owner = n.get("owner") or "Unassigned"
            if n.get("reviewer"):
                owner += " / " + n["reviewer"]
            lines.append(f"| [{clean(n['label'])}]({link}) | {clean(owner)} | {clean(n['nextAction'])} |")
    lines += ["", "Sources and prerequisites live in the detailed records. Dated orientations and test captures are evidence at their stated revision; they are not silently promoted to today's result.", ""]

    details = ["# Work records", "", "> Generated from `graph.jsonld`. [Current board](../CURRENT.md).", ""]
    for n in items:
        ident = short(n["@id"])
        details += [f"## {ident}", "", f"**{n['label']}**", "",
                    f"Status: **{n['status']}** · Owner: {n.get('owner') or 'Unassigned'} · Updated: {n['updatedAt']}", "",
                    n.get("description", ""), "", "**Next:** " + n["nextAction"], "",
                    "**Done when:** " + n["closure"], ""]
        if n.get("progress"):
            details += ["**Evidence so far:** " + n["progress"], ""]
        if n.get("brief"):
            details += [f"[Task brief](../{n['brief']})", ""]
        for key, label in (("advances", "Enables"), ("blockedBy", "Waiting for"),
                           ("dependsOn", "Context dependencies"), ("sources", "Evidence / provenance")):
            targets = refs(n, key)
            if targets:
                details += [f"**{label}:**", ""]
                for target in targets:
                    other = index[target]
                    text = short(target) + " — " + other.get("label", other.get("path", ""))
                    if other.get("repository", "").endswith(":R-assortia") and other.get("path"):
                        text = f"[{text}](../{other['path']})"
                    details.append("- " + text)
                details.append("")
        if n.get("writeScope"):
            details += ["**Write scope:** " + "; ".join(n["writeScope"]), ""]
        if n.get("acceptance"):
            details += ["**Acceptance:**", ""] + ["- " + a for a in n["acceptance"]] + [""]

    mapping = ["# Project map", "", "> Generated from `graph.jsonld`. [Current board](CURRENT.md).", "",
               "DREGG is being developed as a programmable resource world: people and agents create, govern, share and run resources under explicit authority, with durable, inspectable results. The September 26 milestone is a mixed programmable nexus for friends; the exact public offering is still being selected.", "",
               "The repositories below have different roles. Presence of code, a proof, a successful component test and a deployed capability are separate facts.", "",
               "| Repository | Role in the suite |", "|---|---|"]
    for repo in nodes:
        if repo.get("@type") == "Repository":
            mapping.append(f"| {clean(repo['label'])} | {clean(repo.get('role', 'See the dated orientation.'))} |")
    mapping += ["", "## Capabilities and current work", "", "| Capability | Work records |", "|---|---|"]
    for cap in nodes:
        if cap.get("@type") == "Capability":
            linked = [f"[{short(n['@id'])}](work/records.md#{short(n['@id']).lower()})" for n in items if cap["@id"] in n["advances"]]
            mapping.append(f"| {clean(cap['label'])} | {', '.join(linked) or 'No current scoped work item'} |")
    mapping += ["", "[Design intent](intent.md) · [September 26 milestone](milestones/2026-09-26.md) · [Source investigations](research/README.md).", "",
                "The graph is deliberately incomplete. An absent edge means it has not been recorded, not that the capability does not exist.", ""]
    return {"CURRENT.md": "\n".join(lines), "work/records.md": "\n".join(details), "MAP.md": "\n".join(mapping)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "board", "show", "render"))
    parser.add_argument("id", nargs="?")
    parser.add_argument("--status", choices=STATES)
    parser.add_argument("--check", action="store_true", help="For render: refuse stale views without writing")
    args = parser.parse_args()
    nodes = json.loads((ROOT / "graph.jsonld").read_text())["@graph"]
    errors = validate(nodes)
    if errors:
        raise SystemExit("\n".join(errors))
    if args.command == "check":
        print(f"{len(work(nodes))} work records: bookkeeping and graph references valid. Program correctness was not checked.")
    elif args.command == "board":
        for n in work(nodes, args.status):
            print(f"{short(n['@id'])} | {n['status']} | {n.get('owner') or 'Unassigned'} | {n['label']}")
    elif args.command == "show":
        selected = [n for n in nodes if args.id in (n["@id"], short(n["@id"]))]
        if not selected:
            raise SystemExit("No such record: " + str(args.id))
        print(json.dumps(selected[0], indent=2, ensure_ascii=False))
    else:
        stale = []
        for name, content in render(nodes).items():
            path = ROOT / name
            if args.check:
                if not path.exists() or path.read_text() != content:
                    stale.append(name)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
        if stale:
            raise SystemExit("Stale generated views: " + ", ".join(stale))
        print("Generated views current." if args.check else "Updated CURRENT.md, MAP.md and work/records.md.")


if __name__ == "__main__":
    main()
