# September 18 — usable graph navigation and source impact

Two internal agent tasks now provide everyday navigation and evidence maintenance for the living hub. These are not external contributor assignments.

`browse_graph.py` retains its short output and adds deterministic incoming/outgoing/both traversal at depth one or two. It displays relation labels, record identity/type/label and source locations, stops cyclic/repeated expansion, and labels dangling targets. Relation names come from the actual JSON-LD context. Twelve tests cover the current graph, deterministic ordering, cycles, missing targets, unchanged short output and an isolated script-plus-graph checkout.

`check_sources.py` retains the text CLI and adds repeatable repository overrides, JSON, and explanatory reference paths. Changed/missing evidence is distinct from an unavailable checkout or unreadable source. It never updates a historical hash, treats contextual references as proof of dependency/falsity, or treats failed HEAD observation as movement. Twenty-three focused tests and actual subprocess CLI fixtures passed; the full hub suite contains 41 passing tests. See [the source-checking contract](../../internal/source-checking.md) for statuses and exit codes; exit zero can report incomplete observation.

Captured [navigation manifest](evidence/hub-tools-0145/navigation.sha256), [checker manifest](evidence/hub-tools-0145/source-checker-manifest.json), [focused check](evidence/hub-tools-0145/source-checker-focused.txt), [whole hub check](evidence/hub-tools-0145/all-tests.txt) and [CLI fixtures](evidence/hub-tools-0145/cli.txt) retain the observed scope. Root also ran the earlier 18 navigation/hub checks before the source checker joined. These validate bookkeeping/tools, not DREGG runtime correctness.

Try:

```sh
python3 hub.py board
python3 browse_graph.py --id W-RESOURCE-BIRTH --relations --direction both --depth 1
python3 check_sources.py --repo dregg-assortia=. --repo minidregg=../minidregg --explain
```

The substantial contributor proposal is [persistent resource hosting](../../contributing/resource-host-lifecycle.md). It names source-backed cloud/native-host gaps, existing and proposed interfaces, upstream owners and acceptance scenarios. Runtime/consumer selection and assignment remain active work with ember.
