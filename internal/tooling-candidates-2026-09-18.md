> Reclassified after ember's correction on September18: these are internal agent tooling tasks, not an offered Wisper contribution. The original bounded tool specifications below remain useful internally.

# Internal hub-tooling candidates

Prepared 2026-09-18 as selection input. These are proposals, not assignments or
accepted priorities. They deliberately avoid `README.md`, the contributor
landing page, `graph.jsonld`, and current sprint state, which the root lane is
editing. Each candidate consumes the current graph read-only and can begin
without a DREGG build or a decision about Fossil.

## Recommended: make graph relationships navigable

### User value

`browse_graph.py --id` currently shows a record's prose and sources, but it does
not show the graph edges that answer the useful project-management questions:
what motivates this task, what it depends on, what it is related to, and what
points back to it. A contributor or ember should be able to start at
`W-M26-DESIGN` or `W-RESOURCE-BIRTH` and follow the existing knowledge graph
without reading raw JSON-LD or several long narrative files.

### Receiving consumer and files

- Human consumer: a contributor or maintainer orienting from the terminal.
- Program consumer: the existing `browse_graph.py` command.
- Write scope: `browse_graph.py` and a new
  `tests/test_browse_graph.py`. A tiny reusable module under this repository is
  acceptable if it makes traversal testable.
- Read-only inputs: `graph.jsonld` and repository/source paths already recorded
  there.

### Current evidence

- `browse_graph.py:10-21` accepts only `--id` and a small `--type` enum.
- `browse_graph.py:25-38` expands scalar metadata and `sources`, but omits
  `subject`, `object`, `dependsOn`, `motivatedBy`, and `related` even though
  `check_sources.py:14` already names those relationship fields.
- The current graph has 141 nodes, including 12 capabilities, 12 work items,
  26 claims, and 64 source records. For example, `W-M26-DESIGN` has ten
  `motivatedBy` edges and several `related` edges that the browser hides.
- The milestone says the next useful traversal is “release milestone → user
  journey → operations → design decisions and contracts → receiving
  implementations → acceptance evidence”
  (`milestones/2026-09-26.md:148-152`). Showing the relationships that already
  exist is a concrete first step; the task must not invent missing stages.

### Bounded deliverables

1. Add `--relations` plus `--direction outbound|inbound|both` and
   `--depth 1|2` to `browse_graph.py`. Defaults must preserve today's short
   output.
2. Resolve each edge to short ID, type, label, and relationship name. For
   sources, retain the current absolute path and starting line.
3. Make traversal deterministic, cycle-safe, and explicit about a broken
   target instead of raising an incidental `KeyError`.
4. Include every relationship field validated by `check_sources.py`:
   `subject`, `object`, `sources`, `dependsOn`, `motivatedBy`, `related`, and
   `repository`.
5. Add focused tests for outbound, inbound, two-hop, cycle, broken-link, and
   unchanged default output behavior. Tests may use a small temporary graph;
   they must also include one integration assertion against the checked-in
   graph.

### Dependencies and active-owner conflicts

There is no prerequisite beyond Python 3's standard library. Do not edit the
graph vocabulary or project records to make the display prettier. The root
lane owns `README.md`, contributor landing material, and project-state updates;
this task needs none of those files. It does not overlap the active
breadstuffs/minidregg core owners.

### Reproducible acceptance

```sh
cd ~/dev/dregg-assortia
python3 -m unittest tests.test_browse_graph
python3 browse_graph.py --id W-RESOURCE-BIRTH --relations --direction both --depth 1 > /tmp/assortia-relations.txt
python3 - <<'PY'
from pathlib import Path
s = Path('/tmp/assortia-relations.txt').read_text()
assert 'W-RESOURCE-BIRTH | WorkItem' in s
assert 'W-NATIVE-DATA-RECEIVER' in s
assert 'W-JOINT-POST' in s
assert 'related' in s
PY
python3 browse_graph.py --id DOES-NOT-EXIST >/tmp/assortia-missing.out 2>&1; test $? -ne 0
```

Closure is a reader reaching the existing work item, capability, claim, and
source records in both directions with stable, tested output. It does not
include changing any claim or declaring a work item complete.

## Candidate: explain which records a stale source affects

### User value

`check_sources.py` currently reports changed paths. During this sprint it
reports eight changed sources and two moved repository heads, but a reader must
manually search `graph.jsonld` to learn which claims and work items need review.
An impact report turns source freshness from a warning list into an actionable
maintenance queue while preserving the rule that changed bytes mean “recheck,”
not “false.”

### Receiving consumer and files

- Human consumer: the maintainer refreshing claims after an implementation
  checkpoint.
- Program consumer: scripts or a later dashboard consuming a stable JSON
  report.
- Write scope: `check_sources.py` and a new
  `tests/test_check_sources.py`.
- Read-only inputs: `graph.jsonld`, recorded source files, and Git HEADs.

### Current evidence

- `check_sources.py:23-47` stores changed sources as display strings, losing
  their source IDs and graph relationships before output.
- Its current run names changed World, Hermes, and minidregg files but does not
  identify dependent claims/work items such as `C-DOC-DURABLE` or the active
  implementation records.
- `README.md:28` says changed-source warnings identify observations to revisit
  and are not proof failures. The new report must keep that meaning.

### Bounded deliverables

1. Preserve the existing text mode and exit semantics.
2. Add `--explain` text output that prints each missing/changed `Source` ID,
   path, directly referencing records, and transitive dependents reached only
   through the declared relationship fields. Label direct versus transitive
   impact.
3. Add `--format json` with a documented top-level shape containing counts,
   broken references, changed/missing sources, moved repositories, and impacted
   record IDs. Sort every collection deterministically.
4. Report expected and actual SHA-256 for changed files in JSON. Never rewrite
   the recorded hash, status, or graph.
5. Add fixture-based tests for unchanged, changed, missing, broken-reference,
   head-moved, and cyclic dependency cases. Tests must use temporary
   repositories/graphs and must not depend on today's changing count.

### Dependencies and active-owner conflicts

This is standard-library-only and independent of the relationship browser.
It must not refresh `graph.jsonld`; root owns the decision to reinterpret and
update project state. Avoid shelling out except for the existing read-only Git
HEAD observation.

### Reproducible acceptance

```sh
cd ~/dev/dregg-assortia
python3 -m unittest tests.test_check_sources
set +e
python3 check_sources.py --format json > /tmp/assortia-freshness.json
status=$?
set -e
python3 - <<'PY'
import json
r = json.load(open('/tmp/assortia-freshness.json'))
assert {'counts', 'brokenReferences', 'changedSources', 'movedRepositories'} <= r.keys()
for source in r['changedSources']:
    assert {'id', 'path', 'expectedSha256', 'actualSha256', 'directDependents', 'transitiveDependents'} <= source.keys()
PY
test "$status" -eq 0 -o "$status" -eq 1
```

Closure is a deterministic report that tells a maintainer exactly which graph
records require reinspection for each stale source, without asserting those
records are wrong and without mutating project state.

## Candidate: render a local, static work index

### User value

The graph and sprint records are useful but terminal and Markdown navigation is
still manual. A single generated HTML file would make the current capabilities,
work items, statuses, closures, relationships, and source locations searchable
for ember and external contributors. This is a local view over the graph, not a
new authority, tracker, or deployed service.

### Receiving consumer and files

- Human consumer: anyone opening the generated file in a browser.
- Write scope: new `render_hub.py` and `tests/test_render_hub.py`. Keep CSS and
  JavaScript inline so the output is one portable file.
- Read-only input: `graph.jsonld`.
- Generated output: a caller-selected path such as
  `/tmp/dregg-assortia-hub.html`; do not commit generated HTML in this task.

### Current evidence

- `README.md` describes practical project questions and explicitly says the
  directory has no deployed service.
- The checked-in graph already has user-facing labels, descriptions, statuses,
  closures, relations, and source locations, but `browse_graph.py` exposes only
  a subset in a sequential text view.
- Long-term editing/query UI and Fossil remain undecided. A deterministic local
  rendering does not decide either question.

### Bounded deliverables

1. Add `render_hub.py --output PATH`, using only Python's standard library.
2. Render counts and filterable sections for capabilities, work items, claims,
   questions, and sources. Work-item cards must show status and closure; linked
   IDs must navigate to in-page anchors.
3. Render recorded local source paths and line starts as text that can be
   copied. Do not read or embed source bodies, credentials, Git diffs, or
   unrecorded workspace state.
4. Escape all graph strings before placing them in HTML. The small client-side
   filter must work with JavaScript disabled as a complete unfiltered page.
5. Produce byte-identical output for identical graph bytes and include tests
   for escaping, broken references, anchors, status/closure visibility, and
   deterministic generation.

### Dependencies and active-owner conflicts

No dependency on the other two candidates is required, and no server or
frontend framework is introduced. Do not edit `README.md`, `graph.jsonld`, or
the root-owned contributor landing. If root later chooses to link or publish
the output, that is a separate decision.

### Reproducible acceptance

```sh
cd ~/dev/dregg-assortia
python3 -m unittest tests.test_render_hub
python3 render_hub.py --output /tmp/assortia-hub-a.html
python3 render_hub.py --output /tmp/assortia-hub-b.html
cmp /tmp/assortia-hub-a.html /tmp/assortia-hub-b.html
python3 - <<'PY'
from pathlib import Path
s = Path('/tmp/assortia-hub-a.html').read_text()
for text in ('Programmable social resource world',
             'Implement one accepted resource birth with owner authority and charge',
             'active-design-and-implementation'):
    assert text in s
assert 'id="W-RESOURCE-BIRTH"' in s
PY
```

Closure is a deterministic, safe, locally openable index over every current
graph record. Editing graph state, issue tracking, comments, authentication,
and deployment are outside this task.

## Why no sibling DREGG code task is recommended yet

The obvious source-backed seams are presently owned: World persistence and
Hermes receiving are changing in breadstuffs, while canonical admission,
composition, resource birth, authority, and compiler consumers are changing in
minidregg. The apparently small `dregg-doc` receipt-to-patch correspondence is
also only a named seam (`dregg-doc/src/atom.rs:21,93`) without a selected
identity contract. Assigning any of those as a first external task now would
either race an active owner or ask the contributor to make an unresolved design
decision. The three tasks above improve the living knowledge/PM hub against
stable read-only inputs and make the next code task easier to specify from
current evidence.
