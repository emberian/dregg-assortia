# Checking recorded sources on any machine

`check_sources.py` reads `graph.jsonld`, hashes locally available file sources,
and reports which recorded assertions and work refer to changed evidence. The
graph remains the owner of every historical hash, observation and relationship.
The checker never updates it or marks a claim false or a work item blocked.

```sh
python3 check_sources.py
python3 check_sources.py --explain
python3 check_sources.py --format json > /tmp/assortia-freshness.json
```

The default remains a concise text report with `CHANGED`, `MISSING` and
informational `HEAD MOVED` lines, counts and a scope reminder. `--explain` adds
source IDs, directly and transitively referencing records, and the path of
recorded links for each result. JSON always includes those paths.

## Checkout locations

Recorded absolute paths describe the machine where an observation was made.
Override them without editing the graph:

```sh
python3 check_sources.py --explain \
  --repo minidregg="$HOME/dev/minidregg" \
  --repo breadstuffs="$HOME/dev/breadstuffs" \
  --repo dregg-assortia="$HOME/dev/dregg-assortia"
```

Repeat `--repo NAME=PATH` for each checkout to relocate. `NAME` can be its unique
repository label, short ID (`R-minidregg`), short ID without `R-`
(`minidregg`), or full graph ID. Unknown, ambiguous and repeated repository
assignments are usage errors; two aliases cannot silently override the same
repository twice. Paths may contain spaces or `=`. Quote the whole assignment
when necessary. `~` is expanded; relative override paths use the current working
directory. Relative paths recorded in the graph use the graph's directory.

Unspecified repositories retain their recorded paths. A checkout absent from
this machine is **unavailable**, not a collection of missing source files.
No checkout is cloned or fetched. `--graph PATH` selects another read-only
graph, including temporary fixtures.

## What each status means

| File-source status | Observation | Result |
| --- | --- | --- |
| `unchanged` | Available file matches its recorded SHA-256. | No freshness finding. |
| `changed` | Available file has different bytes. | Reinspect the observation and linked records. |
| `missing` | The repository directory is available, but the source file is absent or is a directory. | Reinspect the recorded source location and linked records. |
| `unavailable` | Repository has no local path, is absent or unreadable, or a source cannot be read. | Unknown on this machine; no change or impact finding is inferred. |
| `invalid` | Source metadata cannot identify a valid repository, relative file path or SHA-256. | Repair the metadata after inspecting its intended meaning; this is not a content-change observation. |

Sources without a `path`, such as a recorded conversation, do not create a local
file check. A source's hash covers the **whole file**; recorded line ranges are
context, not a partial-file hashing rule. Neither matching bytes nor a successful
check proves correctness, passing tests, deployment or current design intent.

For available repositories with historical source `gitHead` values, the tool
observes `git rev-parse HEAD` once per repository, with a five-second timeout.
A changed HEAD is informational even when all source hashes match. A failed
HEAD observation is reported separately as `HEAD UNAVAILABLE`; it does not
establish movement. HEAD movement alone generates no source impact list.

Exit codes are:

- **0:** no observed freshness or graph-metadata finding. The result may still
  be incomplete because repositories, files or HEAD observations are unavailable.
- **1:** at least one changed/missing source, invalid source record, broken
  graph reference, duplicate graph ID or malformed reference field.
- **2:** invalid command arguments, unreadable/unparseable graph, or a graph
  that lacks the basic list-of-identified-records structure.

The JSON report's `status` is `findings` for exit 1, `incomplete` for exit 0 with
unavailable observations, and `current` otherwise. When there are both findings
and unknowns, the status is `findings`; the unavailable arrays and counts still
retain every unknown observation. `current` concerns the checked sources and
graph references; moved HEADs remain independently visible. No finding arises
solely from an absent checkout.

## Reading impact paths

Starting from a changed or missing source, the checker follows **incoming**
references from other records through the relation names exported by
`hub.RELATIONS`. These currently include `sources`, `dependsOn`, `related`,
`motivatedBy`, `subject`, `object`, `repository`, `blockedBy`, `advances`,
`milestone`, `workItems` and `completionEvidence`.

For example, `work --dependsOn--> claim --sources--> source` makes the claim a
direct reference and the work item a transitive reference. The checker does not
follow the source's outgoing `repository` link and infer that every record in
that repository changed. It also does not invent missing links.

Contextual links such as `related` are included and named in each path. Thus
“impact” means **a linked candidate for review**, not a demonstrated dependency,
false assertion or failed task. A record with no recorded route to a source
cannot appear in that source's impact report. This is a limit of the graph's
coverage, not evidence that the record is unaffected.

Traversal is cycle-safe and keeps one shortest path per affected record. Stable
edge ordering breaks ties. Lists of records and references are sorted, and
shuffling graph records or relationship arrays does not alter the report.
Direct references have depth 1; transitive references have depth greater than
1. These sets are disjoint, and a source is never reported as its own impact.

## Structured output

`--format json` emits one JSON object, including on exit 1. Version 1 has these
top-level fields:

| Field | Contents |
| --- | --- |
| `schemaVersion`, `status`, `exitCode`, `scope` | Report version, overall observation status, corresponding exit code and scope reminder. |
| `counts` | File-source totals, successful hash reads, changed/missing/unavailable/invalid source counts, broken-reference and graph-error counts, moved/unavailable HEAD counts and distinct impacted-record count. |
| `repositoryPaths` | Full repository ID to resolved local path, or `null` when none is recorded. |
| `sources` | Every file-source observation, sorted by source ID. |
| `changedSources` | **Both changed and missing** sources, distinguished by each entry's `status`, with impact paths. |
| `unavailableSources`, `invalidSources` | Separate unknown observations and invalid source metadata. |
| `unavailableRepositories` | Used repositories whose directories cannot be observed. |
| `brokenReferences` | `{record, relation, target}` edges with missing targets. |
| `graphErrors` | Duplicate identities or invalid reference fields. |
| `movedRepositories` | Observed HEAD, recorded heads and source IDs recorded at other heads. |
| `unavailableHeads` | Failed HEAD observations and their reason codes. |
| `impactedRecords` | Distinct sorted IDs reached from changed/missing sources. |
| `impactedClaims`, `impactedWorkItems` | Type-filtered subsets of `impactedRecords`. |

`counts.changedSources` counts only the `changed` status, while
`counts.missingSources` counts `missing`; their sum is the length of the
`changedSources` array. `counts.checkedSources` counts successful hash reads
(`unchanged` plus `changed`), not unavailable, invalid or missing files.

Every changed/missing source includes `id`, `repository`, resolved `path`,
`recordedPath`, `expectedSha256`, `actualSha256` (`null` for missing files),
`directDependents`, `transitiveDependents` and `impactPaths`. Each path record
contains `id`, `type`, `label`, `depth` and a `path` list of
`{record, relation, target}` edges, ordered from the referencing record down
to the source. Expected hashes are copied from the graph unchanged; the checker
does not update them to silence a finding. Unavailable observations have no
impact paths inferred from their absence.

The report is a local observation. It does not read source contents into its
output, run project builds, access the network, or mutate Git state. Its only
subprocess is the existing read-only HEAD observation.

## Focused checks

```sh
python3 -m unittest tests.test_check_sources
python3 -m unittest discover -s tests
```

The fixtures use temporary checkout directories and a substituted HEAD reader;
they do not need Git repositories or run Git. They cover changed and missing
files, unavailable evidence, portable repeated overrides, immutable historical
hashes, broken metadata, informational/unknown HEADs, deterministic transitive
impact and cycles. A checked-in-graph test relocates all repositories to absent
fixture locations and checks that absence creates no source-change findings.
