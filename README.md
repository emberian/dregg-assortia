# dregg-assortia

A working place to recover the DREGG suite's intentions, evidence, decisions, and ongoing work.

**First orientation: 2026-09-17.** This is a source-linked research snapshot and a small graph specimen, not a new authority over the code or a settled project-management system. Git remains the primary VCS. Fossil is being considered for issues, discussion, and project memory.

Start with [the orientation](orientation/2026-09-17.md), then [ember's stated intentions](intent.md). The [graph specimen](graph.jsonld) carries a few concrete findings, candidate work items, and their sources. [Repository revisions](repositories.json) distinguish committed heads from worktrees. The [research index](research/README.md) links the bounded investigations and their corrective follow-ups.

The practical questions this should eventually answer:

- What are we trying to make possible, and for whom?
- Which implementations and research results bear on that capability?
- What actually connects, at which revision and in which configuration?
- What is proved, what was exercised, what was deployed, and what is only proposed?
- What decision or missing connection is preventing the next useful experience?
- What changed since the last time ember or an agent understood this part?

## Reading the evidence

No project build, proof replay, test run, or live-service probe was performed in this orientation. A test file is evidence of an executable scenario, not a newly observed pass. Historical deployment records retain their historical dates.

Source records contain the inspected file's SHA-256, Git HEAD and blob identity where available. An unchanged hash means the source observation is still about the same bytes; it does not prove its claim. A changed hash means recheck the observation, not declare the claim false.

Run `python3 check_sources.py` to check source freshness and graph references. This reads files and Git metadata only; it runs no project checks. Run `python3 browse_graph.py` for a short text view of the graph's findings and proposed work; `--id C-DOC-DURABLE` expands one record.

## Deliberately unresolved

- Whether Fossil becomes the shared issue/discussion service.
- The long-term graph vocabulary, query engine, and editing interface.
- Which existing application surface should carry the first community experience.
- The exact relation between future minidregg semantics and existing breadstuffs consumers.
- Whether a particular old component is retained, adapted, replaced, or archived.

This directory has no deployed service and changes no sibling repository. The Loore profile was read as personal context and is not copied or indexed here.
