# DREGG intent archaeology — user-authored evidence

Read-only `cv` pass, 2026-09-17.  This is deliberately a decision record, not a
state-of-code report.  Quotations below are Ember's user messages; the short
interpretations are mine.

## 1. Product world: a durable, inspectable, self-explaining desktop—not a conventional app

**Source:** `34db0696-2160-4fec-aaa2-2853b02ebe2f` (`Orient into Starbridge-v2 project files and history`), message **110**, 2026-06-19T21:51:46.806Z.

> “input events entering thru the firmament should be actual dregg things somehow … because we need to be houyhnhnm — durable, snapshottable, rewindable, debuggable”

Same session, message **149**, 2026-06-19T22:02:50.894Z:

> “a 60s/70s-vision psychedelic hypermedia system implemented as a fresh desktop paradigm, engelbart style almost.”

And message **160**, 2026-06-19T22:08:52.676Z:

> “replay & timetravel & debuggability … [are] first-class … a button that pops open a … debug view over the live system by … suspending it and inserting another level of meta.”

**Inference:** semantic/KG scaffolding should describe durable operational objects and their relations (event, turn, receipt, capability, branch, view, provenance), so that it can power reflection, replay, and explanation.  It should not be treated as a detached content taxonomy.

## 2. The social/distributed computation thesis was already explicit

**Source:** `34db0696-2160-4fec-aaa2-2853b02ebe2f`, message **2297**, 2026-06-20T15:28:46.651Z.

> “distributed Houyhnhnm (collaborative time-travel)” and “forking is free; settlement = a preferred maximal config; revocation = the one non-monotone op.”

The same message calls branch-and-stitch a cap-confined virtual branch with a lossy, pushout-correct reconciliation, and names a Pijul-shaped document language where “conflicts are first-class states (not failed merges).”

**Inference:** local-first, distributed, and social activity are intended as one continuum.  A shellserver/Discord world should be able to expose shared branches, settlements, and documents as first-class DREGG resources, rather than only using DREGG as an authorization/payment back end.

## 3. Hypermedia, Hermes, editor/viewer, and chat were coequal surface commitments

**Source:** `1774dfce-c92e-42e5-bf7c-8870ac29b052` (`Orient within project structure and history`), message **243**, 2026-06-22T20:33:07.753Z.  **Provenance caveat:** this is a session-control/stop-hook notification carrying an adopted goal condition, not spontaneous conversational prose; it is evidence that Ember accepted the direction, but should be cited as an adopted standing instruction.

> “implementing all things we've talked about (hermes/ados/zed/etc integration) … built out the document language, editor, viewer, and other infrastructure. also the matrix chat needs to be kickass awesome and thoroughly dreggpilled”

**Inference:** real Hermes integration belongs inside the main inhabited world and its document/communication objects.  The exact current form is not fixed by this session, but a separate generic chatbot would under-realize the stated direction.

## 4. Why minidregg was split: make the semantic machine small, derived, and owned

**Source:** `6977f98e-e709-4fa7-82b1-101860c76372` (`Formal reimplementation of breadstuffs as minidregg`), message **52**, 2026-08-07T20:23:54.941Z.  **Provenance caveat:** this is Ember's explicit `/goal` command input—a user-adopted operating instruction, rather than freeform prose.

> “Mutually elaborate minidregg (the proof-native semantic computer) and Loom (its owned proof system) until a coherent v0 slice is green-and-audited … Statement-first, build the witnesses, keep main green.”

The priority was sharpened in message **194**, 2026-08-07T21:31:00.435Z (also an explicit `/goal` command input):

> “Flesh out LOOM (minidregg's owned proof system) toward a defensible whole — ember's priority, ABOVE kernel work.”

**Inference:** the split is not an abandonment of the product world.  It isolates an owned, proof-native semantic foundation and proof system so the original system's semantics can be expressed without inheriting its mass or hand-authored duplicate paths.  Treat minidregg as a research/foundation line with product-facing consequences, not as the place to prematurely recreate every shellserver surface.

## 5. CRDT / replicated-computation research is parallel to, not identical with, minidregg's Loom

**Source:** `36b51055-354e-4290-ad2c-e59215809d62` (`Build DAG CRDT loom weaving library`), message **14**, 2026-08-10T20:05:48.804Z.

> “the loom in minidregg is the name of its custom proof system, don't be misled by that :) it's just an unfortunate naming collision.”

Same session, message **769**, 2026-08-11T01:43:53.614Z:

> “i wish we were at least IMPLEMENTING sequence CRDTs etc?? the actual ERA protocol as well??”

And message **1069**, 2026-08-11T03:49:54.846Z:

> “hazel, typed-holes, replicated *computations* and not just replicated *Datatypes*, incremental/reactive types of partial graphs....computations specifies as choreographies of datatypes”

**Inference:** a semantic-web/KG effort should keep the two meanings distinct: minidregg/Loom is the owned proof-system research; CRDT/weaving/ERA/choreography is a separate distributed-programming research/product frontier.  They can connect through explicit artifacts and concepts, but should not be collapsed by name or presumed implementation dependency.

## Explicit tensions / not decisions to overwrite

* **Strong shared world vs. user-owned single-machine properties.**  The older vision includes collaborative branching and settlement, while the forward dregg4 record insists that a single-machine node must not pay distributed costs.  Design topology-parametrically; do not presume federation for every local resource.
* **Product exploration vs. formal rigor.**  Ember explicitly asked to pursue ambitious CRDT/sequence/ERA work, but also rejected spending substantial time on adversarial counterexample construction when the work could be improved (session `36b...`, message 820).  This is a prioritization tension, not a mandate to drop rigor.
* **“Loom” naming collision.**  Preserve the distinction above in any new knowledge graph vocabularies.
* **No historical evidence found for `shellserver`, `dregg-assortia`, or Fossil as an architecture decision.** Exact `cv` searches for `shellserver` and `dregg-assortia` returned no hits; Fossil hits were code-audit “fossils,” not DVCS/process planning.  The present brief is therefore the first located authority for those specifics, rather than a continuation that can be claimed to have an older settled design.

## Context checked

Read current `HORIZONLOG.md`, `docs/OVERVIEW.md`, breadstuffs and minidregg memory indices, `minidregg-mission.md`, `minidregg-design-laws.md`, plus the breadstuffs Houyhnhnm/dregg4 memory records.  Those records corroborate context, but are intentionally not presented above as user quotations.  Quotations from `34db…` (messages 110, 149, 160, 2297) and `36b…` (messages 14, 769, 1069) are ordinary Ember user prose; the two categories above are labelled separately.
