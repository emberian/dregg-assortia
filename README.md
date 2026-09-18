# dregg-assortia

The living knowledge index and project hub for DREGG: what we are building, how the pieces connect, who owns current work, and what evidence supports each claim.

**[Current work](CURRENT.md) · [Project map](MAP.md) · [Contributor entry](contributing/README.md)**

The current effort is the September 26 programmable nexus: friends and agents author, govern, share and run DREGG-native resources through a programmable shell and related interfaces. The core and its real receiving applications are being developed together. The exact public release offering and economic operation remain under design. [Ember's intentions](intent.md) distinguish accepted direction from proposals.

An outside contributor should be able to own a substantial product feature from this hub—for example, an Android application with an embedded DREGG node and defined system/UI responsibilities. That requires concrete runtime contracts, upstream ownership and acceptance scenarios. The [Android work-package investigation](work/records.md#w-android-contract) is making that boundary explicit. It is not yet a claim that an Android runtime or release commitment exists.

## Where information lives

| Question | Start here |
|---|---|
| What is happening now, and who owns it? | [Current board](CURRENT.md), generated from graph work records |
| How do repositories and capabilities relate? | [Project map](MAP.md), then [source investigations](research/README.md) |
| What can I build, against which interface? | [Contributor entry](contributing/README.md), linked feature briefs and contracts |
| What does done mean? | [Work records](work/records.md): closure, dependencies, owner and evidence |
| What was actually checked? | [Latest checkpoint](sprints/2026-09-18/checkpoint-0045.md) and dated test/source artifacts |
| Why are we doing this? | [Intent](intent.md) and [September 26 design discussion](milestones/2026-09-26.md) |
| What did the first investigation find? | [September 17 orientation](orientation/2026-09-17.md), a historical snapshot |

## Use the hub

These commands require only Python 3.10+ and this repository. No sibling checkout, server or database is needed.

```sh
python3 hub.py board
python3 hub.py show W-RESOURCE-BIRTH
python3 hub.py check
python3 hub.py render --check
python3 browse_graph.py --id C-DOC-DURABLE
```

`graph.jsonld` owns source assertions and current work records. `CURRENT.md`, `MAP.md` and `work/records.md` are generated views. Update the graph, then run `python3 hub.py render`. [The update routine](WORKFLOW.md) explains ownership, evidence and handoffs. A current board is maintained information, not a live view of running agents.

`python3 check_sources.py` additionally inspects the sibling file paths recorded during the original investigation. Those paths currently refer to ember's machine; portability and source-impact reporting are internal tooling work. Missing local repositories on another machine do not disprove claims. Changed source bytes mean the old observation needs reinspection, not that its claim is false. Never silently refresh an old hash to suppress a warning.

Git remains primary. The Git-tracked work records are usable now; Fossil's issue/discussion features remain an undecided option. No tracker service is required to read or contribute to this hub.

## Read claims at their actual scope

User intent, design decisions, source inspection, theorem checks, captured runtime tests and deployments are distinct evidence. A passing component does not establish its integration, and a checkpoint commit may contain work still converging. The work records keep the remaining receiving path explicit.

This graph is incomplete. Missing evidence means unknown; an absent relationship is not proof of absence. Older observations remain dated even as current tasks advance. Credentials, private profiles and unrelated transcripts do not belong here.
