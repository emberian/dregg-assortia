# dregg-assortia

The living knowledge index and project hub for DREGG: what we are building, how the pieces connect, who owns current work, and what evidence supports each claim.

**[Start here / handoff](HANDOFF.md) · [Current work](CURRENT.md) · [Project map](MAP.md) · [Contributor entry](contributing/README.md)**

The intended offering is a complete hosted Nous Hermes experience within the September 26 programmable nexus: friends and agents author, govern, share and run DREGG-native resources. Hosted OpenRouter-key custody is acceptable initially; external unforked Hermes access is also desirable. **Build the New World in Mini:** ember settled the construction direction after the [Bread/Mini microswarm](sprints/2026-09-19/core-orientation.md) and has now authorized a substantial [Mini implementation cycle](sprints/2026-09-19/cycle-1.md). The [first core cycle passed](sprints/2026-09-19/cycle-1-result.md): joint resources, typed content, scoped authority, current-law grants, revocation, exact recovery, the native host and Rust client. Native latency and the real hosted Hermes lifecycle are the next implementation work. Bread is reference material, and reuse is optional rather than a prerequisite. Read the [decision](sprints/2026-09-19/rebuild-in-mini.md) and [ember's intentions](intent.md). The rejected earlier Python [implementation wave](sprints/2026-09-19/implementation.md) is not resumed.

An outside contributor should be able to own a substantial product feature from this hub. [Resource-host lifecycle](contributing/resource-host-lifecycle.md) remains an unassigned platform proposal. Ember has assigned Wisper a separate low-level networking task outside our critical path; the earlier plan to offer him hosting work is superseded.

## Where information lives

| Question | Start here |
|---|---|
| What is happening now, and who owns it? | [Current board](CURRENT.md), generated from graph work records |
| How do repositories and capabilities relate? | [Project map](MAP.md), then [source investigations](research/README.md) |
| What can I build, against which interface? | [Contributor entry](contributing/README.md), linked feature briefs and contracts |
| What does done mean? | [Work records](work/records.md): closure, dependencies, owner and evidence |
| What was actually checked? | [Completed cycle result](sprints/2026-09-19/cycle-1-result.md) and [captured build/runtime evidence](sprints/2026-09-19/cycle-1-evidence/INDEX.md); earlier handoffs retain their dated scope |
| What did the hosted-Hermes review find? | [September 19 protocol review](sprints/2026-09-19/protocol-review.md), three source investigations and their inventory; no new execution |
| What is the current implementation cycle? | [Mini construction cycle 1](sprints/2026-09-19/cycle-1.md): authorization and owned deliveries; [completed result](sprints/2026-09-19/cycle-1-result.md): measured build/runtime evidence and the remaining construction |
| What did the deeper orientation establish? | [Bread/Mini orientation](sprints/2026-09-19/core-orientation.md): source investigation preceding the settled Mini direction and implementation cycle |
| What should disconnect do? | [Circuit-breaker follow-up](sprints/2026-09-19/connection-breaker.md): immediate interruption by default; explicit soft mode keeps working under existing authority and budget |
| Why are we doing this? | [Intent](intent.md), [current hosted-Hermes direction](sprints/2026-09-19/direction.md) and [earlier September 26 design draft](milestones/2026-09-26.md) |
| What did the first investigation find? | [September 17 orientation](orientation/2026-09-17.md), a historical snapshot |

## Use the hub

These commands require only Python 3.10+ and this repository. No sibling checkout, server or database is needed.

```sh
python3 hub.py board
python3 hub.py show W-RESOURCE-BIRTH
python3 hub.py check
python3 hub.py render --check
python3 browse_graph.py --id C-DOC-DURABLE
python3 browse_graph.py --id W-RESOURCE-BIRTH --relations --direction both --depth 1
```

`graph.jsonld` owns source assertions and current work records. `CURRENT.md`, `MAP.md` and `work/records.md` are generated views. Update the graph, then run `python3 hub.py render`. [The update routine](WORKFLOW.md) explains ownership, evidence and handoffs. A current board is maintained information, not a live view of running agents.

`python3 check_sources.py` additionally inspects recorded file sources. Use repeatable `--repo NAME=PATH` options to locate your checkouts and `--explain` to follow affected records; `--format json` provides structured observations. [Source-checking documentation](internal/source-checking.md) defines the results and exit codes. Unavailable repositories remain unknown. Changed bytes call for reinspection, not a claim that the old observation is false. Historical hashes remain unchanged.

Git remains primary. The Git-tracked work records are usable now; Fossil's issue/discussion features remain an undecided option. No tracker service is required to read or contribute to this hub.

## Read claims at their actual scope

User intent, design decisions, source inspection, theorem checks, captured runtime tests and deployments are distinct evidence. A passing component does not establish its integration, and a checkpoint commit may contain work still converging. The work records keep the remaining receiving path explicit.

This graph is incomplete. Missing evidence means unknown; an absent relationship is not proof of absence. Older observations remain dated even as current tasks advance. Credentials, private profiles and unrelated transcripts do not belong here.
