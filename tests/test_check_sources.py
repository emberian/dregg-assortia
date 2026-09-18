"""Freshness is an observation, and unavailable evidence is not a finding."""
from contextlib import redirect_stderr, redirect_stdout
import copy
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import check_sources as checker


def ident(name):
    return "urn:test:" + name


def sha(data):
    return hashlib.sha256(data).hexdigest()


class SourceCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.repo = self.root / "alpha"
        self.repo.mkdir()
        self.file = self.repo / "source.txt"
        self.file.write_bytes(b"recorded source\n")
        self.nodes = [
            {"@id": ident("R-alpha"), "@type": "Repository", "label": "alpha",
             "localPath": str(self.repo)},
            {"@id": ident("S-source"), "@type": "Source", "label": "Source observation",
             "repository": ident("R-alpha"), "path": "source.txt",
             "sha256": sha(self.file.read_bytes()), "gitHead": "old-head"},
            {"@id": ident("C-claim"), "@type": "Claim", "label": "Recorded claim",
             "sources": [ident("S-source")]},
            {"@id": ident("W-work"), "@type": "WorkItem", "label": "Review receiving path",
             "dependsOn": [ident("C-claim")]},
        ]
        self.head = Mock(return_value=("old-head", None))

    def inspect(self, nodes=None, **kwargs):
        return checker.inspect_sources(self.nodes if nodes is None else nodes,
                                       head_reader=self.head, **kwargs)

    def run_cli(self, *args):
        graph_path = self.root / "graph.jsonld"
        graph_path.write_text(json.dumps({"@graph": self.nodes}))
        stdout = io.StringIO()
        with patch.object(checker, "git_head", self.head), redirect_stdout(stdout):
            status = checker.main(["--graph", str(graph_path), *args])
        return status, stdout.getvalue(), graph_path

    def test_unchanged_source_is_current_and_read_only(self):
        before = copy.deepcopy(self.nodes)
        report = self.inspect()
        self.assertEqual((report["status"], report["exitCode"]), ("current", 0))
        self.assertEqual(report["counts"]["checkedSources"], 1)
        self.assertEqual(report["sources"][0]["status"], "unchanged")
        self.assertEqual(report["changedSources"], [])
        self.assertEqual(report["impactedRecords"], [])
        self.assertEqual(self.nodes, before)
        self.assertEqual(self.file.read_bytes(), b"recorded source\n")

    def test_changed_bytes_keep_historical_hash_and_explain_claim_and_work(self):
        before = copy.deepcopy(self.nodes)
        self.file.write_bytes(b"new implementation\n")
        report = self.inspect()
        self.assertEqual((report["status"], report["exitCode"]), ("findings", 1))
        source, = report["changedSources"]
        self.assertEqual(source["expectedSha256"], sha(b"recorded source\n"))
        self.assertEqual(source["actualSha256"], sha(b"new implementation\n"))
        self.assertEqual(source["directDependents"], [ident("C-claim")])
        self.assertEqual(source["transitiveDependents"], [ident("W-work")])
        self.assertEqual(report["impactedClaims"], [ident("C-claim")])
        self.assertEqual(report["impactedWorkItems"], [ident("W-work")])
        work = next(r for r in source["impactPaths"] if r["id"] == ident("W-work"))
        self.assertEqual(work["path"], [
            {"record": ident("W-work"), "relation": "dependsOn", "target": ident("C-claim")},
            {"record": ident("C-claim"), "relation": "sources", "target": ident("S-source")},
        ])
        self.assertEqual(self.nodes, before)

    def test_missing_source_in_available_repository_is_a_finding(self):
        self.file.unlink()
        report = self.inspect()
        self.assertEqual(report["exitCode"], 1)
        self.assertEqual(report["counts"]["missingSources"], 1)
        self.assertEqual(report["counts"]["changedSources"], 0)
        source, = report["changedSources"]
        self.assertEqual(source["status"], "missing")
        self.assertIsNone(source["actualSha256"])
        self.assertEqual(report["impactedClaims"], [ident("C-claim")])

    def test_absent_repository_is_unknown_without_change_or_impact(self):
        self.nodes[0]["localPath"] = str(self.root / "not-cloned")
        report = self.inspect()
        self.assertEqual((report["status"], report["exitCode"]), ("incomplete", 0))
        self.assertEqual(report["counts"]["missingSources"], 0)
        self.assertEqual(report["counts"]["checkedSources"], 0)
        self.assertEqual(report["changedSources"], [])
        self.assertEqual(report["impactedRecords"], [])
        self.assertEqual(report["unavailableSources"][0]["status"], "unavailable")
        self.assertEqual(report["unavailableRepositories"][0]["id"], ident("R-alpha"))
        self.assertEqual(report["movedRepositories"], [])
        self.head.assert_not_called()

    def test_no_recorded_checkout_path_is_unknown(self):
        del self.nodes[0]["localPath"]
        report = self.inspect()
        self.assertEqual(report["exitCode"], 0)
        self.assertEqual(report["unavailableSources"][0]["reason"], "no-local-path")
        self.assertIsNone(report["unavailableSources"][0]["path"])
        self.head.assert_not_called()

    def test_unavailable_checkout_does_not_hide_an_observed_change_elsewhere(self):
        self.file.write_bytes(b"changed")
        self.nodes.extend([
            {"@id": ident("R-absent"), "@type": "Repository", "label": "absent",
             "localPath": str(self.root / "not-cloned")},
            {"@id": ident("S-unknown"), "@type": "Source", "repository": ident("R-absent"),
             "path": "unknown.txt", "sha256": sha(b"unknown source")},
            {"@id": ident("C-unknown"), "@type": "Claim", "sources": [ident("S-unknown")]},
        ])
        report = self.inspect()
        self.assertEqual((report["status"], report["exitCode"]), ("findings", 1))
        self.assertEqual(report["counts"]["changedSources"], 1)
        self.assertEqual(report["counts"]["unavailableSources"], 1)
        self.assertEqual(report["impactedClaims"], [ident("C-claim")])
        self.assertNotIn("impactPaths", report["unavailableSources"][0])

    def test_unreadable_source_is_unknown_not_changed_or_missing(self):
        # Permission bits are not reliable when the runner owns elevated privileges.
        with patch.object(Path, "open", side_effect=PermissionError("fixture refusal")):
            report = self.inspect()
        self.assertEqual((report["status"], report["exitCode"]), ("incomplete", 0))
        self.assertEqual(report["unavailableSources"][0]["reason"], "source-unreadable")
        self.assertEqual(report["changedSources"], [])
        self.assertEqual(report["impactedRecords"], [])

    def test_repeatable_overrides_relocate_two_repositories_without_changing_graph(self):
        beta = self.root / "beta checkout=second"
        beta.mkdir()
        (beta / "other.txt").write_bytes(b"second source")
        self.nodes[0]["localPath"] = "/not/available/alpha"
        self.nodes.extend([
            {"@id": ident("R-beta"), "@type": "Repository", "label": "beta-label",
             "localPath": "/not/available/beta"},
            {"@id": ident("S-other"), "@type": "Source", "repository": ident("R-beta"),
             "path": "other.txt", "sha256": sha(b"second source")},
        ])
        before = copy.deepcopy(self.nodes)
        status, output, graph_path = self.run_cli(
            "--repo", f"alpha={self.repo}", "--repo", f"beta-label={beta}", "--format", "json")
        report = json.loads(output)
        self.assertEqual(status, 0)
        self.assertEqual(report["counts"]["checkedSources"], 2)
        self.assertEqual(report["unavailableSources"], [])
        self.assertEqual(report["repositoryPaths"][ident("R-beta")], str(beta))
        self.assertEqual(self.nodes, before)
        self.assertEqual(json.loads(graph_path.read_text())["@graph"], before)

    def test_override_aliases_and_relative_paths_resolve_without_ambiguity(self):
        for alias in ("alpha", "R-alpha", ident("R-alpha")):
            with self.subTest(alias=alias):
                overrides = checker.repository_overrides(self.nodes, [f"{alias}=."])
                self.assertEqual(overrides, {ident("R-alpha"): Path.cwd().resolve()})
        for assignments in (["alpha"], ["alpha="], ["=somewhere"], ["unknown=somewhere"],
                            ["alpha=one", "R-alpha=two"]):
            with self.subTest(assignments=assignments), self.assertRaises(ValueError):
                checker.repository_overrides(self.nodes, assignments)
        ambiguous = self.nodes + [{"@id": ident("R-other"), "@type": "Repository", "label": "alpha"}]
        with self.assertRaises(ValueError):
            checker.repository_overrides(ambiguous, ["alpha=somewhere"])

    def test_recorded_relative_checkout_is_relative_to_graph_not_process(self):
        self.nodes[0]["localPath"] = "alpha"
        report = self.inspect(graph_dir=self.root)
        self.assertEqual(report["status"], "current")
        self.assertEqual(report["repositoryPaths"][ident("R-alpha")], str(self.repo))

    def test_cycle_and_multiple_paths_are_stable_and_use_shortest_recorded_path(self):
        self.file.write_bytes(b"changed")
        self.nodes[1]["related"] = [ident("W-loop")]
        self.nodes[2]["related"] = [ident("W-loop")]
        self.nodes[3]["dependsOn"] = [ident("C-other"), ident("C-claim")]
        self.nodes.extend([
            {"@id": ident("C-other"), "@type": "Claim", "sources": ident("S-source")},
            {"@id": ident("W-loop"), "@type": "WorkItem", "related": [ident("W-work")]},
            {"@id": ident("W-direct"), "@type": "WorkItem",
             "related": [ident("W-loop")], "sources": [ident("S-source")]},
        ])
        report = self.inspect()
        shuffled = copy.deepcopy(list(reversed(self.nodes)))
        for node in shuffled:
            for key in checker.RELATIONS:
                if isinstance(node.get(key), list):
                    node[key].reverse()
        self.assertEqual(report, self.inspect(shuffled))
        source, = report["changedSources"]
        paths = {r["id"]: r for r in source["impactPaths"]}
        self.assertNotIn(ident("S-source"), paths)
        self.assertNotIn(ident("R-alpha"), paths)  # Never traverse a source's outbound repo link.
        self.assertEqual(paths[ident("W-loop")]["depth"], 3)
        self.assertEqual(paths[ident("W-direct")]["depth"], 1)
        self.assertEqual(paths[ident("W-work")]["path"][0]["target"], ident("C-claim"))
        self.assertEqual(len(paths), 5)

    def test_impact_uses_every_declared_relation_without_inventing_new_ones(self):
        self.file.write_bytes(b"changed")
        for relation in checker.RELATIONS:
            self.nodes.append({"@id": ident("linked-" + relation), "@type": "Claim",
                               relation: ident("S-source")})
        self.nodes.append({"@id": ident("unlinked"), "@type": "Claim",
                           "unrecordedRelation": ident("S-source")})
        source, = self.inspect()["changedSources"]
        self.assertTrue(all(ident("linked-" + r) in source["directDependents"] for r in checker.RELATIONS))
        self.assertNotIn(ident("unlinked"), source["directDependents"])

    def test_broken_references_are_findings_but_do_not_invent_source_changes(self):
        self.nodes[3]["completionEvidence"] = [ident("missing"), ident("missing")]
        report = self.inspect()
        self.assertEqual(report["exitCode"], 1)
        self.assertEqual(report["brokenReferences"], [{"record": ident("W-work"),
                         "relation": "completionEvidence", "target": ident("missing")}])
        self.assertEqual(report["changedSources"], [])
        self.assertEqual(report["impactedRecords"], [])

    def test_duplicate_identity_and_invalid_relation_are_reported(self):
        self.nodes.append(copy.deepcopy(self.nodes[2]))
        self.nodes[3]["dependsOn"] = {"not": "a reference list"}
        report = self.inspect()
        self.assertEqual(report["exitCode"], 1)
        self.assertEqual(report["graphErrors"], [
            "Duplicate graph identity: " + ident("C-claim"),
            "Invalid dependsOn references: " + ident("W-work"),
        ])

    def test_invalid_source_metadata_is_not_a_content_change(self):
        for field, value, reason in (("sha256", "not a hash", "invalid-recorded-sha256"),
                                     ("path", "../outside", "source-path-not-relative"),
                                     ("repository", ident("C-claim"), "invalid-source-repository")):
            with self.subTest(field=field):
                nodes = copy.deepcopy(self.nodes)
                nodes[1][field] = value
                report = self.inspect(nodes)
                self.assertEqual(report["exitCode"], 1)
                self.assertEqual(report["invalidSources"][0]["reason"], reason)
                self.assertEqual(report["changedSources"], [])

    def test_head_movement_is_informational_and_observed_once_per_repository(self):
        other = copy.deepcopy(self.nodes[1])
        other.update({"@id": ident("S-second-observation"), "gitHead": "new-head"})
        self.nodes.append(other)
        self.head.return_value = ("new-head", None)
        report = self.inspect()
        self.assertEqual((report["status"], report["exitCode"]), ("current", 0))
        moved, = report["movedRepositories"]
        self.assertEqual(moved["expectedHeads"], ["new-head", "old-head"])
        self.assertEqual(moved["sourcesAtOtherHeads"], [ident("S-source")])
        self.assertEqual(report["impactedRecords"], [])
        self.head.assert_called_once_with(self.repo)

    def test_failed_head_observation_is_unknown_not_movement(self):
        self.head.return_value = (None, "head-observation-failed")
        report = self.inspect()
        self.assertEqual((report["status"], report["exitCode"]), ("incomplete", 0))
        self.assertEqual(report["counts"]["checkedSources"], 1)
        self.assertEqual(report["movedRepositories"], [])
        self.assertEqual(report["unavailableHeads"][0]["reason"], "head-observation-failed")
        self.assertEqual(report["changedSources"], [])

    def test_non_file_sources_do_not_create_local_checks(self):
        self.nodes.append({"@id": ident("S-conversation"), "@type": "Source",
                           "label": "Historical design discussion"})
        report = self.inspect()
        self.assertEqual(report["counts"]["fileSources"], 1)

    def test_default_text_is_compatible_and_explanation_is_opt_in(self):
        self.file.write_bytes(b"changed")
        status, output, _ = self.run_cli()
        self.assertEqual(status, 1)
        self.assertIn(f"CHANGED {self.file}\n", output)
        self.assertIn("1 file sources checked; 1 missing/changed; 0 broken graph references;", output)
        self.assertIn(checker.SCOPE, output)
        self.assertNotIn("direct:", output)
        status, output, _ = self.run_cli("--explain")
        self.assertEqual(status, 1)
        self.assertIn("direct: " + ident("C-claim"), output)
        self.assertIn("transitive: " + ident("W-work"), output)
        self.assertIn("W-work --dependsOn--> C-claim", output)
        self.assertIn("does not mean a claim is false", output)

    def test_no_argument_cli_reads_default_graph_and_keeps_success_exit(self):
        (self.root / "graph.jsonld").write_text(json.dumps({"@graph": self.nodes}))
        stdout = io.StringIO()
        with patch.object(checker, "ROOT", self.root), patch.object(checker, "git_head", self.head), redirect_stdout(stdout):
            status = checker.main([])
        self.assertEqual(status, 0)
        self.assertIn("1 file sources checked; 0 missing/changed;", stdout.getvalue())
        self.assertIn(checker.SCOPE, stdout.getvalue())

    def test_json_cli_is_deterministic_read_only_and_contains_paths_without_explain(self):
        self.file.write_bytes(b"changed")
        status, output, graph_path = self.run_cli("--format", "json")
        before = graph_path.read_bytes()
        repeated_status, repeated, _ = self.run_cli("--format", "json", "--explain")
        self.assertEqual((status, repeated_status), (1, 1))
        self.assertEqual(output, repeated)
        self.assertEqual(graph_path.read_bytes(), before)
        report = json.loads(output)
        self.assertTrue({"counts", "brokenReferences", "changedSources", "movedRepositories"} <= report.keys())
        self.assertTrue(report["changedSources"][0]["impactPaths"])

    def test_invalid_override_is_a_clear_cli_error(self):
        with redirect_stderr(io.StringIO()) as stderr, self.assertRaises(SystemExit) as error:
            self.run_cli("--repo", "unknown=/tmp/does-not-matter")
        self.assertEqual(error.exception.code, 2)
        self.assertIn("Unknown or ambiguous repository name: unknown", stderr.getvalue())

    def test_checked_in_graph_on_machine_without_checkouts_has_no_source_findings(self):
        nodes = json.loads((checker.ROOT / "graph.jsonld").read_text())["@graph"]
        overrides = {n["@id"]: self.root / "absent" / str(i) for i, n in enumerate(nodes)
                     if n.get("@type") == "Repository"}
        report = self.inspect(nodes, overrides=overrides)
        self.assertGreater(report["counts"]["fileSources"], 0)
        self.assertEqual(report["status"], "incomplete")
        self.assertEqual(report["exitCode"], 0)
        self.assertEqual(report["changedSources"], [])
        self.assertEqual(report["impactedRecords"], [])
        self.assertEqual(report["brokenReferences"], [])
        self.head.assert_not_called()


if __name__ == "__main__":
    unittest.main()
