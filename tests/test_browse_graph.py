import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import browse_graph

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "urn:test:"
RELATIONS = ("subject", "object", "sources", "dependsOn", "motivatedBy", "related",
             "repository", "blockedBy", "advances", "milestone", "workItems", "completionEvidence")


def node(ident, kind="WorkItem", **fields):
    return {"@id": PREFIX + ident, "@type": kind, "label": ident + " label", **fields}


def document(nodes):
    return {"@context": {key: {"@type": "@id"} for key in RELATIONS}, "@graph": nodes}


def fixture():
    return document([
        node("A", description="Start here.", status="active", closure="Reach B.",
             sources=[PREFIX + "S"], dependsOn=[PREFIX + "B"]),
        node("B", related=[PREFIX + "C"]),
        node("C", related=[PREFIX + "D"]),
        node("D"),
        node("CLAIM", "Claim", subject=PREFIX + "A", object=PREFIX + "CAP"),
        node("CAP", "Capability"),
        node("S", "Source", path="proof.lean", lineStart=17, repository=PREFIX + "REPO"),
        node("REPO", "Repository", localPath="/absent/sibling"),
    ])


def view(graph, ident="A", **options):
    return browse_graph.render(graph, graph.select(ident), detailed=True, **options)


class BrowseGraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = browse_graph.Graph(fixture())

    def test_default_detailed_output_unchanged(self):
        self.assertEqual(view(self.graph),
                         "A | WorkItem | A label\n"
                         "  Start here.\n"
                         "  status: active\n"
                         "  closure: Reach B.\n"
                         "  source: /absent/sibling/proof.lean:17\n\n")
        self.assertNotIn("relations", view(self.graph))

    def test_default_listing_and_type_filter_preserve_order(self):
        self.assertEqual([browse_graph.short(n["@id"]) for n in self.graph.select()],
                         ["A", "B", "C", "D", "CLAIM"])
        self.assertEqual(browse_graph.render(self.graph, self.graph.select(record_type="Claim")),
                         "CLAIM | Claim | CLAIM label\n  \n\n")
        self.assertEqual(self.graph.select(PREFIX + "A"), self.graph.select("A"))

    def test_outbound_resolves_type_label_relation_and_source_location(self):
        text = view(self.graph, relations=True)
        self.assertIn("--dependsOn--> B | WorkItem | B label", text)
        self.assertIn("--sources--> S | Source | S label | /absent/sibling/proof.lean:17", text)
        self.assertNotIn("CLAIM | Claim", text)
        self.assertNotIn("C | WorkItem", text)

    def test_inbound_preserves_original_relation_orientation(self):
        text = view(self.graph, relations=True, direction="inbound")
        self.assertIn("<--subject-- CLAIM | Claim | CLAIM label", text)
        self.assertNotIn("--dependsOn-->", text)
        visits = self.graph.walk(PREFIX + "A", "inbound")
        self.assertEqual([(v.edge.source, v.edge.target) for v in visits],
                         [(PREFIX + "CLAIM", PREFIX + "A")])

    def test_two_hops_stop_at_requested_depth_in_both_directions(self):
        text = view(self.graph, relations=True, direction="both", depth=2)
        self.assertIn("depth 2 from B:", text)
        self.assertIn("--related--> C | WorkItem | C label", text)
        self.assertIn("--object--> CAP | Capability | CAP label", text)
        self.assertIn("--repository--> REPO | Repository | REPO label", text)
        self.assertNotIn("D | WorkItem", text)
        incoming = browse_graph.Graph(document([
            node("A"), node("B", related=[PREFIX + "A"]),
            node("C", dependsOn=[PREFIX + "B"]), node("D", related=[PREFIX + "C"]),
        ]))
        self.assertEqual({v.edge.source for v in incoming.walk(PREFIX + "A", "inbound", 2)},
                         {PREFIX + "B", PREFIX + "C"})

    def test_cycles_self_links_and_duplicate_edges_are_bounded(self):
        graph = browse_graph.Graph(document([
            node("A", related=[PREFIX + "B", PREFIX + "B", PREFIX + "A"]),
            node("B", related=[PREFIX + "A", PREFIX + "C"]),
            node("C", related=[PREFIX + "A"]),
        ]))
        visits = graph.walk(PREFIX + "A", "both", 2)
        self.assertEqual(len(visits), 5)
        self.assertEqual(len({visit.edge for visit in visits}), 5)
        self.assertTrue(all(visit.depth in (1, 2) for visit in visits))

    def test_dangling_target_and_missing_provenance_are_explicit(self):
        graph = browse_graph.Graph(document([
            node("A", sources=[PREFIX + "LOST", PREFIX + "S"], related=[PREFIX + "GONE"]),
            node("S", "Source", path="proof.lean", lineStart=3, repository=PREFIX + "NO-REPO"),
        ]))
        text = view(graph, relations=True, depth=2)
        self.assertIn("LOST [missing record]", text)
        self.assertIn("GONE | MISSING | unresolved graph record", text)
        self.assertIn("proof.lean:3 [missing repository: NO-REPO]", text)
        self.assertIn("NO-REPO | MISSING | unresolved graph record", text)
        self.assertIn("LOST [missing record]", view(graph))

    def test_relationships_follow_schema_including_new_work_fields(self):
        graph = browse_graph.Graph(document([
            node("A", **{key: PREFIX + key for key in RELATIONS},
                 description=PREFIX + "NOT-AN-EDGE"),
            *[node(key) for key in RELATIONS],
        ]))
        visits = graph.walk(PREFIX + "A")
        self.assertEqual({v.edge.relation for v in visits}, set(RELATIONS))
        self.assertNotIn(PREFIX + "NOT-AN-EDGE", {v.edge.target for v in visits})

    def test_relation_output_ignores_graph_and_set_order(self):
        original = fixture()
        original["@graph"][0]["sources"].append(PREFIX + "CAP")
        shuffled = copy.deepcopy(original)
        shuffled["@graph"].reverse()
        shuffled["@context"] = dict(reversed(list(shuffled["@context"].items())))
        for record in shuffled["@graph"]:
            for key in RELATIONS:
                if isinstance(record.get(key), list):
                    record[key].reverse()
        self.assertEqual(view(browse_graph.Graph(original), relations=True, direction="both", depth=2),
                         view(browse_graph.Graph(shuffled), relations=True, direction="both", depth=2))

    def test_unknown_record_and_invalid_traversal_fail_clearly(self):
        with self.assertRaisesRegex(ValueError, "No such record: UNKNOWN"):
            self.graph.select("UNKNOWN")
        for direction, depth in (("sideways", 1), ("both", 0), ("both", 3)):
            with self.subTest(direction=direction, depth=depth):
                with self.assertRaises(ValueError):
                    self.graph.walk(PREFIX + "A", direction, depth)

    def test_cli_works_with_only_script_and_graph(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            shutil.copyfile(ROOT / "browse_graph.py", directory / "browse_graph.py")
            (directory / "graph.jsonld").write_text(json.dumps(fixture()))
            command = [sys.executable, str(directory / "browse_graph.py")]
            result = subprocess.run(command + ["--id", "A", "--relations", "--direction", "both",
                                                "--depth", "2"],
                                    cwd=directory, capture_output=True, text=True, check=True)
            self.assertIn("<--subject-- CLAIM | Claim", result.stdout)
            self.assertIn("/absent/sibling/proof.lean:17", result.stdout)
            self.assertEqual(result.stderr, "")
            for options in (["--id", "UNKNOWN"], ["--relations", "--depth", "3"],
                            ["--direction", "inbound"]):
                with self.subTest(options=options):
                    result = subprocess.run(command + options, cwd=directory,
                                            capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertNotIn("Traceback", result.stderr)

    def test_checked_in_resource_birth_relationships(self):
        graph = browse_graph.Graph(json.loads((ROOT / "graph.jsonld").read_text()))
        text = view(graph, "W-RESOURCE-BIRTH", relations=True, direction="both")
        self.assertIn("W-RESOURCE-BIRTH | WorkItem", text)
        self.assertIn("W-NATIVE-DATA-RECEIVER | WorkItem", text)
        self.assertIn("W-JOINT-POST | WorkItem", text)
        self.assertIn("related", text)


if __name__ == "__main__":
    unittest.main()
