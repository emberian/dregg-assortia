#!/usr/bin/env python3
"""Observe source freshness and graph impact; never verify or rewrite claims."""
import argparse
from collections import defaultdict, deque
import hashlib
import json
from pathlib import Path
import subprocess

from hub import RELATIONS, short

ROOT = Path(__file__).resolve().parent
SCOPE = "This checks source freshness, not correctness, test success, or deployment."


def repository_overrides(nodes, assignments):
    """Resolve repeatable NAME=PATH options without changing recorded locations."""
    aliases = defaultdict(set)
    for node in nodes:
        if node.get("@type") == "Repository":
            ident = node["@id"]
            for name in (ident, short(ident), short(ident).removeprefix("R-"), node.get("label")):
                if name:
                    aliases[name].add(ident)
    overrides = {}
    for assignment in assignments:
        name, separator, raw_path = assignment.partition("=")
        if not separator or not name or not raw_path:
            raise ValueError("Repository override must be NAME=PATH")
        matches = aliases.get(name, set())
        if len(matches) != 1:
            raise ValueError(f"Unknown or ambiguous repository name: {name}")
        ident = next(iter(matches))
        if ident in overrides:
            raise ValueError(f"Repository overridden more than once: {name}")
        overrides[ident] = Path(raw_path).expanduser().resolve()
    return overrides


def graph_index(nodes):
    index, errors = {}, []
    for node in nodes:
        if not isinstance(node, dict) or not isinstance(node.get("@id"), str):
            raise ValueError("Every graph record needs a string @id")
        ident = node["@id"]
        if ident in index:
            errors.append(f"Duplicate graph identity: {ident}")
        else:
            index[ident] = node
    reverse, broken = defaultdict(set), set()
    for ident, node in sorted(index.items()):
        for relation in RELATIONS:
            values = node.get(relation, [])
            if isinstance(values, str):
                values = [values]
            if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
                errors.append(f"Invalid {relation} references: {ident}")
                continue
            for target in values:
                if target not in index:
                    broken.add((ident, relation, target))
                else:
                    reverse[target].add((ident, relation, target))
    return index, reverse, sorted(set(errors)), [
        {"record": record, "relation": relation, "target": target}
        for record, relation, target in sorted(broken)
    ]


def impact(source, index, reverse):
    """Follow incoming recorded references; retain one shortest, stable path."""
    paths, queue = {source: []}, deque([source])
    while queue:
        target = queue.popleft()
        for record, relation, _ in sorted(reverse.get(target, ())):
            if record in paths:
                continue
            edge = {"record": record, "relation": relation, "target": target}
            paths[record] = [edge] + paths[target]
            queue.append(record)
    records = [
        {"id": ident, "type": index[ident].get("@type"),
         "label": index[ident].get("label", ident), "depth": len(paths[ident]), "path": paths[ident]}
        for ident in sorted(paths.keys() - {source})
    ]
    return {"directDependents": [r["id"] for r in records if r["depth"] == 1],
            "transitiveDependents": [r["id"] for r in records if r["depth"] > 1],
            "impactPaths": records}


def git_head(path):
    """Read-only observation. Failure is not evidence of HEAD movement."""
    try:
        result = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"],
                                capture_output=True, text=True, check=False, timeout=5)
    except subprocess.TimeoutExpired:
        return None, "head-observation-timeout"
    except OSError:
        return None, "git-unavailable"
    if result.returncode or not result.stdout.strip():
        return None, "head-observation-failed"
    return result.stdout.strip(), None


def directory_reason(path):
    if path is None:
        return "no-local-path"
    try:
        if not path.is_dir():
            return "repository-unavailable"
        path.stat()
    except OSError:
        return "repository-unreadable"
    return None


def source_observation(source, path, repo_path):
    expected = source.get("sha256")
    observed = {"id": source["@id"], "repository": source.get("repository"),
                "path": str(path) if path is not None else None, "recordedPath": source["path"],
                "expectedSha256": expected, "actualSha256": None}
    if reason := directory_reason(repo_path):
        return {**observed, "status": "unavailable", "reason": reason}
    if not isinstance(expected, str) or len(expected) != 64 or any(
            c not in "0123456789abcdefABCDEF" for c in expected):
        return {**observed, "status": "invalid", "reason": "invalid-recorded-sha256"}
    try:
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
    except (FileNotFoundError, NotADirectoryError, IsADirectoryError):
        reason = directory_reason(repo_path)
        return {**observed, "status": "unavailable" if reason else "missing",
                "reason": reason or "source-file-missing"}
    except OSError:
        return {**observed, "status": "unavailable", "reason": "source-unreadable"}
    actual = digest.hexdigest()
    return {**observed, "actualSha256": actual,
            "status": "unchanged" if actual == expected.lower() else "changed"}


def inspect_sources(nodes, overrides=None, graph_dir=ROOT, head_reader=None):
    index, reverse, graph_errors, broken = graph_index(nodes)
    overrides, head_reader = overrides or {}, head_reader or git_head
    repos = {i: n for i, n in index.items() if n.get("@type") == "Repository"}
    paths = {}
    for ident, repo in sorted(repos.items()):
        raw = overrides.get(ident, repo.get("localPath"))
        path = Path(raw).expanduser() if raw else None
        paths[ident] = ((path if path.is_absolute() else Path(graph_dir) / path).resolve()
                        if path is not None else None)
    observations, head_sources, used_repos = [], defaultdict(list), set()
    for ident, source in sorted(index.items()):
        if source.get("@type") != "Source" or "path" not in source:
            continue
        repo_id, relative = source.get("repository"), source["path"]
        reason = None
        if not isinstance(repo_id, str) or repo_id not in repos:
            reason = "invalid-source-repository"
        elif not isinstance(relative, str) or not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
            reason = "source-path-not-relative"
        if reason:
            observations.append({"id": ident, "repository": repo_id, "recordedPath": relative,
                                 "path": None, "status": "invalid", "reason": reason})
            continue
        used_repos.add(repo_id)
        repo_path = paths[repo_id]
        path = repo_path / relative if repo_path is not None else None
        observed = source_observation(source, path, repo_path)
        if observed["status"] in ("changed", "missing"):
            observed.update(impact(ident, index, reverse))
        observations.append(observed)
        if source.get("gitHead"):
            head_sources[repo_id].append(source)
    changed = [o for o in observations if o["status"] in ("changed", "missing")]
    unavailable = [o for o in observations if o["status"] == "unavailable"]
    invalid = [o for o in observations if o["status"] == "invalid"]
    unavailable_repos = []
    for ident in sorted(used_repos):
        if reason := directory_reason(paths[ident]):
            unavailable_repos.append({"id": ident, "label": repos[ident].get("label", ident),
                                      "path": str(paths[ident]) if paths[ident] is not None else None,
                                      "reason": reason})
    moved, unavailable_heads = [], []
    for ident, sources in sorted(head_sources.items()):
        if directory_reason(paths[ident]):
            continue
        actual, reason = head_reader(paths[ident])
        info = {"id": ident, "label": repos[ident].get("label", ident), "path": str(paths[ident]),
                "expectedHeads": sorted({s["gitHead"] for s in sources}), "actualHead": actual}
        if actual is None:
            unavailable_heads.append({**info, "reason": reason or "head-observation-failed"})
        elif differing := sorted(s["@id"] for s in sources if s["gitHead"] != actual):
            moved.append({**info, "sourcesAtOtherHeads": differing})
    affected = sorted({ident for source in changed for ident in
                       source["directDependents"] + source["transitiveDependents"]})
    findings = bool(changed or broken or graph_errors or invalid)
    incomplete = bool(unavailable or unavailable_heads)
    counts = {"fileSources": len(observations),
              "checkedSources": sum(o["status"] in ("unchanged", "changed") for o in observations),
              "changedSources": sum(o["status"] == "changed" for o in observations),
              "missingSources": sum(o["status"] == "missing" for o in observations),
              "unavailableSources": len(unavailable), "invalidSources": len(invalid),
              "brokenReferences": len(broken), "graphErrors": len(graph_errors),
              "movedRepositories": len(moved), "unavailableHeads": len(unavailable_heads),
              "impactedRecords": len(affected)}
    return {
        "schemaVersion": 1, "status": "findings" if findings else "incomplete" if incomplete else "current",
        "exitCode": int(findings), "scope": SCOPE, "counts": counts,
        "repositoryPaths": {i: str(p) if p is not None else None for i, p in paths.items()},
        "sources": observations, "changedSources": changed, "unavailableSources": unavailable,
        "invalidSources": invalid, "unavailableRepositories": unavailable_repos,
        "brokenReferences": broken, "graphErrors": graph_errors,
        "movedRepositories": moved, "unavailableHeads": unavailable_heads,
        "impactedRecords": affected,
        "impactedClaims": [i for i in affected if index[i].get("@type") == "Claim"],
        "impactedWorkItems": [i for i in affected if index[i].get("@type") == "WorkItem"],
    }


def render_text(report, explain=False):
    lines = list(report["graphErrors"])
    for ref in report["brokenReferences"]:
        lines.append(f"Broken {ref['relation']}: {ref['record']} -> {ref['target']}")
    for source in report["sources"]:
        status = source["status"]
        if status == "unchanged":
            continue
        location = source["path"] or source["recordedPath"]
        if status in ("changed", "missing"):
            lines.append(f"{status.upper()} {location}")
            if explain:
                lines.append(f"  Source {source['id']}: recorded observation needs reinspection.")
                for record in source["impactPaths"]:
                    distance = "direct" if record["depth"] == 1 else "transitive"
                    label = str(record["label"]).replace("\n", " ")
                    lines.append(f"  {distance}: {record['id']} [{record['type']}] {label}")
                    chain = "; ".join(f"{short(e['record'])} --{e['relation']}--> {short(e['target'])}"
                                      for e in record["path"])
                    lines.append(f"    via {chain}")
                if not source["impactPaths"]:
                    lines.append("  No referencing records are recorded in this graph.")
        else:
            lines.append(f"{status.upper()} {location} [{source['id']}]: {source['reason']}")
    for repo in report["movedRepositories"]:
        lines.append("HEAD MOVED (inspect dependency scope): " + repo["label"])
    for repo in report["unavailableHeads"]:
        lines.append(f"HEAD UNAVAILABLE: {repo['label']} ({repo['reason']})")
    c = report["counts"]
    lines.append(f"{c['checkedSources']} file sources checked; "
                 f"{c['changedSources'] + c['missingSources']} missing/changed; "
                 f"{c['brokenReferences']} broken graph references; "
                 f"{c['movedRepositories']} moved repository heads; "
                 f"{c['unavailableSources']} unavailable sources; {c['invalidSources']} invalid sources.")
    if report["unavailableSources"] or report["unavailableHeads"]:
        lines.append("Unavailable means unknown on this machine; no source-change finding is inferred from it.")
    if explain:
        lines.append("Impact follows incoming recorded references, including contextual relations; it does not mean a claim is false.")
    lines.append(SCOPE)
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", action="append", default=[], metavar="NAME=PATH",
                        help="Override a repository location; repeat for each checkout")
    parser.add_argument("--graph", type=Path, default=ROOT / "graph.jsonld", help="Graph to inspect (read only)")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--explain", action="store_true", help="Show direct and transitive references in text output")
    args = parser.parse_args(argv)
    try:
        nodes = json.loads(args.graph.read_text())["@graph"]
        if not isinstance(nodes, list):
            raise ValueError("@graph must be a list")
        graph_index(nodes)
        overrides = repository_overrides(nodes, args.repo)
        report = inspect_sources(nodes, overrides, args.graph.resolve().parent)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        print(render_text(report, args.explain))
    return report["exitCode"]


if __name__ == "__main__":
    raise SystemExit(main())
