"""The board must refuse misleading project states, independently of source builds."""
import unittest
from hub import validate, render


def fixture():
    return [
        {"@id": "urn:test:source", "@type": "Source", "label": "Captured result"},
        {"@id": "urn:test:cap", "@type": "Capability", "label": "Useful operation"},
        {"@id": "urn:test:task", "@type": "WorkItem", "label": "Deliver operation",
         "status": "active", "owner": "Maintainer", "sources": ["urn:test:source"],
         "advances": ["urn:test:cap"], "closure": "Actual receiving path works",
         "nextAction": "Run the receiving scenario", "updatedAt": "2026-09-18T00:00:00-04:00"},
    ]


class ProjectStateTests(unittest.TestCase):
    def test_ready_cannot_hide_an_unfinished_prerequisite(self):
        nodes = fixture()
        nodes[-1].update(status="ready", brief="brief.md", writeScope=["owned.py"],
                         acceptance=["receiver works"], blockedBy=["urn:test:cap"])
        self.assertTrue(any("blocking dependencies" in e for e in validate(nodes)))

    def test_done_needs_completion_evidence_not_just_a_source(self):
        nodes = fixture()
        nodes[-1]["status"] = "done"
        self.assertTrue(any("completion evidence" in e for e in validate(nodes)))

    def test_dependency_cycle_does_not_become_a_runnable_plan(self):
        nodes = fixture()
        nodes[-1]["blockedBy"] = ["urn:test:task"]
        self.assertTrue(any("cycle" in e for e in validate(nodes)))

    def test_active_owner_and_all_new_edges_are_validated(self):
        nodes = fixture()
        nodes[-1].update(owner=None, advances=["urn:test:missing"])
        errors = validate(nodes)
        self.assertTrue(any("no owner" in e for e in errors))
        self.assertTrue(any("broken advances" in e for e in errors))

    def test_render_is_portable_and_retains_result_scope(self):
        nodes = fixture()
        nodes[-1]["progress"] = "Component passed; receiving path unrun."
        self.assertEqual(validate(nodes), [])
        output = render(nodes)
        self.assertIn("Component passed; receiving path unrun.", output["work/records.md"])
        self.assertIn("Maintainer", output["CURRENT.md"])
        self.assertEqual(output, render(nodes))

    def test_dangling_completion_evidence_is_rejected(self):
        nodes = fixture()
        nodes[-1].update(status="done", completionEvidence=["urn:test:missing"])
        self.assertTrue(any("broken completionEvidence" in e for e in validate(nodes)))


if __name__ == "__main__":
    unittest.main()
