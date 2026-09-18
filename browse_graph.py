#!/usr/bin/env python3
"""Read the orientation graph without a database or network connection."""
import argparse
from collections import defaultdict, deque
from dataclasses import dataclass
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIRECTIONS = ("outbound", "inbound", "both")


def short(ident):
    return ident.rsplit(":", 1)[-1]


def references(record, key):
    value = record.get(key, [])
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(ref, str) for ref in value):
        return value
    raise ValueError(f"Invalid relationship value: {short(record['@id'])}.{key}")


@dataclass(frozen=True, order=True)
class Edge:
    source: str
    relation: str
    target: str


@dataclass(frozen=True)
class Visit:
    depth: int
    via: str
    edge: Edge


class Graph:
    """Index ID relationships declared in this graph's existing local context.

    This consumes the repository's JSON-LD shape, not general JSON-LD.
    Source paths are displayed without opening them.
    """

    def __init__(self, document):
        self.nodes = document["@graph"]
        self.by_id = {record["@id"]: record for record in self.nodes}
        if len(self.by_id) != len(self.nodes):
            raise ValueError("Duplicate graph identities")
        self.relations = tuple(sorted(
            key for key, definition in document["@context"].items()
            if isinstance(definition, dict) and definition.get("@type") == "@id"
        ))
        self.outbound = defaultdict(set)
        self.inbound = defaultdict(set)
        for record in self.nodes:
            for relation in self.relations:
                for target in references(record, relation):
                    edge = Edge(record["@id"], relation, target)
                    self.outbound[edge.source].add(edge)
                    self.inbound[edge.target].add(edge)

    def select(self, ident=None, record_type=None):
        if ident:
            # Full IDs also disambiguate records with the same short ID.
            if ident in self.by_id:
                return [self.by_id[ident]]
            selected = [n for n in self.nodes if short(n["@id"]) == ident]
            if not selected:
                raise ValueError("No such record: " + ident)
            return selected
        return [n for n in self.nodes if n.get("@type") == record_type] if record_type else [
            n for n in self.nodes if n.get("@type") in ("Claim", "WorkItem", "Question")
        ]

    def walk(self, ident, direction="outbound", depth=1):
        """Expand each node and display each edge once, within one or two hops.

        Incoming edges retain their actual relation and orientation; no inverse
        claim is invented. Missing targets remain visible but are not expanded.
        """
        if direction not in DIRECTIONS or depth not in (1, 2):
            raise ValueError("Traversal requires outbound|inbound|both and depth 1|2")
        if ident not in self.by_id:
            raise ValueError("No such record: " + ident)
        queue = deque([(ident, 0)])
        visited = {ident}
        shown = set()
        result = []
        while queue:
            current, distance = queue.popleft()
            if distance == depth:
                continue
            edges = set()
            if direction in ("outbound", "both"):
                edges.update(self.outbound[current])
            if direction in ("inbound", "both"):
                edges.update(self.inbound[current])
            for edge in sorted(edges):
                if edge not in shown:
                    result.append(Visit(distance + 1, current, edge))
                    shown.add(edge)
                other = edge.target if edge.source == current else edge.source
                if other in self.by_id and other not in visited:
                    visited.add(other)
                    queue.append((other, distance + 1))
        return sorted(result, key=lambda visit: (
            visit.depth, visit.via, visit.edge.relation, visit.edge.source, visit.edge.target))

    def source_location(self, source):
        """Render recorded provenance only; absent sibling checkouts are fine."""
        if "path" not in source:
            return source.get("label", source["@id"])
        repo_id = source.get("repository", "")
        repo = self.by_id.get(repo_id)
        location = source["path"]
        warning = ""
        if repo is None:
            warning = f" [missing repository: {short(repo_id) or '(unspecified)'}]"
        elif not repo.get("localPath"):
            warning = f" [repository has no local path: {short(repo_id)}]"
        else:
            location = str(Path(repo["localPath"]) / location)
        if source.get("lineStart"):
            location += ":" + str(source["lineStart"])
        return location + warning

    def describe(self, ident):
        record = self.by_id.get(ident)
        if record is None:
            return short(ident) + " | MISSING | unresolved graph record"
        description = f"{short(ident)} | {record['@type']} | {record['label']}"
        if record.get("@type") == "Source" and "path" in record:
            description += " | " + self.source_location(record)
        return description


def render(graph, selected, detailed=False, relations=False, direction="outbound", depth=1):
    lines = []
    # Keep the original short listing order; relation views sort graph sets.
    if relations:
        selected = sorted(selected, key=lambda record: record["@id"])
    for item in selected:
        ident = item["@id"]
        lines.append(short(ident) + " | " + item["@type"] + " | " + item["label"])
        lines.append("  " + item.get("description", ""))
        if detailed:
            for key in ("evidenceKind", "scope", "limitations", "status", "closure"):
                if item.get(key):
                    lines.append("  " + key + ": " + str(item[key]))
            sources = references(item, "sources")
            for source_id in sorted(sources) if relations else sources:
                source = graph.by_id.get(source_id)
                location = graph.source_location(source) if source else (
                    short(source_id) + " [missing record]")
                lines.append("  source: " + location)
        if relations:
            if item.get("@type") == "Source" and "path" in item:
                lines.append("  location: " + graph.source_location(item))
            lines.append(f"  relations ({direction}, depth {depth}):")
            visits = graph.walk(ident, direction, depth)
            previous = None
            for visit in visits:
                group = (visit.depth, visit.via)
                if group != previous:
                    lines.append(f"    depth {visit.depth} from {short(visit.via)}:")
                    previous = group
                edge = visit.edge
                if edge.source == visit.via:
                    arrow, other = f"--{edge.relation}-->", edge.target
                else:
                    arrow, other = f"<--{edge.relation}--", edge.source
                lines.append(f"      {arrow} {graph.describe(other)}")
            if not visits:
                lines.append("    (none)")
        lines.append("")
    return "\n".join(lines) + ("\n" if lines else "")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", help="Record ID, for example C-DOC-DURABLE")
    parser.add_argument("--type", choices=["Claim", "WorkItem", "Question", "Intent", "Hypothesis"])
    parser.add_argument("--relations", action="store_true", help="Show existing graph relationships")
    parser.add_argument("--direction", choices=DIRECTIONS,
                        help="With --relations: traversal direction (default: outbound)")
    parser.add_argument("--depth", type=int, choices=(1, 2),
                        help="With --relations: maximum hops (default: 1)")
    args = parser.parse_args(argv)
    if not args.relations and (args.direction is not None or args.depth is not None):
        parser.error("--direction and --depth require --relations")
    try:
        graph = Graph(json.loads((ROOT / "graph.jsonld").read_text()))
        selected = graph.select(args.id, args.type)
        print(render(graph, selected, detailed=bool(args.id), relations=args.relations,
                     direction=args.direction or "outbound", depth=args.depth or 1), end="")
    except ValueError as error:
        raise SystemExit(str(error)) from None


if __name__ == "__main__":
    main()
