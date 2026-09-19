# Work records

> Generated from `graph.jsonld`. [Current board](../CURRENT.md).

## W-ANDROID-CONTRACT

**Define resource-host lifecycle ownership and its kernel contract**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T18:04:40.439Z

Unassigned cloud/resource-host lifecycle contract work. The earlier proposal to offer it to Wisper is superseded by his separate low-level networking assignment. This stable work ID retains the original Android example.

**Next:** Define the Mini resource-host lifecycle contract as part of the new platform; Wisper remains on separate networking work outside the critical path.

**Done when:** A contributor can scaffold a real product surface from a concrete brief and agreed contracts, with executable receiving interfaces or explicitly owned upstream delivery, test scenarios and no need to infer core architecture from chat.

**Evidence so far:** September 18 source-backed hosting proposal retained. September 19 clarification: Wisper is assigned elsewhere, outside our critical path. Exact runtime/export contract remains open; no implementation owner assigned.

[Task brief](../contributing/resource-host-lifecycle.md)

**Enables:**

- E-WORLD — Programmable social resource world
- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-CLOUD-HOST-REVIEW — Bounded cloud lifecycle source review, September 18](../research/cloud-host-2026-09-18.md)
- [S-MOBILE-REVIEW — Bounded Android/mobile source inventory, September 18](../research/mobile-2026-09-18.md)
- [S-HOST-CONTRIBUTOR-PROPOSAL — Proposed resource-host lifecycle ownership and receiving contract](../contributing/resource-host-lifecycle.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-DIRECTION-0919 — September 19 hosted Hermes direction, superseded Wisper plan and revised disconnect preference](../sprints/2026-09-19/direction.md)
- [S-REBUILD-MINI-0919 — Ember chooses rebuilding the New World in Mini](../sprints/2026-09-19/rebuild-in-mini.md)

**Write scope:** DreggNet/control provider/server/supervisor and gateway lifecycle; Selected native host extraction/export, jointly reserved with core; Selected packaging and integration harness

**Acceptance:**

- Fault-injected provision/settlement/publication crash intervals reconcile one backend and one charge.
- Actual native authorized operation and exact retained state/result survive restart and response-loss retry.
- Owner isolation, stop/wake, incompatible/corrupt storage refusal and acknowledged event resume are exercised.

## W-GRAPH-NAVIGATION

**Follow graph relationships in both directions**

Status: **done** · Owner: Astra: core_durable_receiver · Updated: 2026-09-19T11:21:30-04:00

Extend the existing graph browser so readers can move from work to purpose, dependencies and evidence, and discover what points back.

**Next:** Use and maintain the tested hub tools during handoffs; the unassigned hosting-contract proposal remains in W-ANDROID-CONTRACT, while hosted-Hermes design continues in W-M26-DESIGN.

**Done when:** Existing graph relationships are traversable deterministically and safely in both directions; broken links and cycles are handled explicitly; default short output remains usable.

**Evidence so far:** 12 focused tests pass, including real graph traversal and a standalone script-plus-graph checkout.

[Task brief](../internal/tooling-candidates-2026-09-18.md)

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-HUB-TOOLS-0145 — Graph navigation/source-impact tooling and captured tests](../sprints/2026-09-18/hub-tools-0145.md)
- [S-DIRECTION-0919 — September 19 hosted Hermes direction, superseded Wisper plan and revised disconnect preference](../sprints/2026-09-19/direction.md)

**Write scope:** dregg-assortia/browse_graph.py; dregg-assortia/tests/test_browse_graph.py

**Acceptance:**

- Python standard-library tests cover outward/inward traversal, depth2, a cycle and a dangling target.
- The checked-in W-RESOURCE-BIRTH record reaches its actual related work/evidence in the CLI.
- No graph record or sibling repository is changed; the tool runs from an assortia-only clone.

## W-HUB-LIVE

**Make assortia usable for ongoing work and new contributors**

Status: **done** · Owner: Astra: root · Updated: 2026-09-19T11:21:30-04:00

Graph-backed work ownership, concrete briefs, generated current views and an explicit update routine replace an orientation-only entry point.

**Next:** Use and maintain the tested hub tools during handoffs; the unassigned hosting-contract proposal remains in W-ANDROID-CONTRACT, while hosted-Hermes design continues in W-M26-DESIGN.

**Done when:** A clean assortia clone exposes current work, ownership and a concrete feature-handoff investigation without sibling repositories; graph/status checks and generated-view checks pass.

**Evidence so far:** Graph-backed ownership/board, portable tools and substantial source-backed contributor proposal are present. Runtime/feature selection remains explicitly active.

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-HUB-TOOLS-0145 — Graph navigation/source-impact tooling and captured tests](../sprints/2026-09-18/hub-tools-0145.md)
- [S-DIRECTION-0919 — September 19 hosted Hermes direction, superseded Wisper plan and revised disconnect preference](../sprints/2026-09-19/direction.md)

## W-AUTHORITY-NATIVE

**Bind native use to committed keys and complete authority**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-19T21:07:36.798Z

Persist exact signing keys/epochs; accept actual configured native verification of the exact request and capability against the complete same-snapshot authority.

**Next:** Finish the complete signed missing/excess/stale/revoked/wrong-kind read and mutation checks on the combined candidate.

**Done when:** Actual installed verification plus complete committed authority checks feed accepted source operations; stale/altered/revoked credentials cannot authorize them.

**Evidence so far:** Native signed current-state observation, exact preparation footprint and explicit per-capability revocation are implemented. Earlier native checks refused wrong-kind/internal-role reads; final complete authority journey is running.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/Kernel/CapabilityRevocation*.lean; minidregg/Kernel/NativeObservationController.lean; minidregg/Compiler/NativeObservationCodec.lean; minidregg/Assurance/CapabilityRevocationAudit.lean and NativeObservationAudit.lean

## W-AUTHORIZED-DELEGATION

**Give a friend a narrower usable right**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-19T21:07:36.798Z

Add an explicit authorized subject-to-subject delegation edge without weakening strict holder-narrowing or inventing bearer custody.

**Next:** Finish the full combined delegation/replay journey and explicit revocation refusal before closing this item.

**Done when:** Owner delegates a bounded right; friend can use that right, cannot exceed it or replace policy, and revocation/current epochs remain enforced.

**Evidence so far:** The earlier native candidate admitted Alice-to-Bob delegation and Bob invocation with exact narrow lineage, including historical verification after expiry. Its final replay loop was interrupted to move to the combined candidate.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/Kernel/CapabilityRevocationController.lean; minidregg/Kernel/CapabilityRevocationReceiver.lean; minidregg public native acceptance harness

## W-CANONICAL-CONSUMER

**Trace one canonical typed event through its real compiler and consumer**

Status: **done** · Owner: Astra: kernel_carrier · Updated: 2026-09-18T01:30:00-04:00

Connect the canonical source request and accepted joint state to actual artifact and native consumers. Keep mandatory request/capability-use and policy-change verb tags consistent.

**Next:** Use the captured receiving evidence as a regression boundary while completing the linked resource journey.

**Done when:** One explicit event/schema/codec/acceptance/storage path, with each existing join or missing obligation sourced. No broad rewrite before the path is understood.

**Evidence so far:** Regenerated authorization artifacts, actual page execution reflection, and one source-authorized native invocation/physical publication path are captured at minidregg278ed6a. This bounded trace does not close every compiler or proof consumer.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-COMPILER — Compiler's joint-turn artifact projection

**Context dependencies:**

- C-KERNEL-COMPILER — The joint-turn artifact projection still consumes DeclaredHyperedge

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)

## W-CHARGE-MATERIALIZATION

**Materialize admitted charges instead of recomputing their source**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T22:02:08.714Z

Preserve exact admitted charges and record bytes while removing repeated birth write/read-guard computation during historical serialization.

**Next:** Materialize source-derived finite charges once at receiving construction, prove exact intent/record equality, inspect compiled sharing, then measure unchanged signed operations. Measure fresh admission separately before assigning the canonical-only admission proposal.

**Done when:** The actual receiving/replay path retains materialized charge data; a general proof preserves every charge lane, complete intent/record identity and canonical bytes without changed bounds or tariffs. Generated-code and matched native operation evidence show repeated serialization does not reconstruct birth writes/read guards, and semantic replay, receipts, charges and refusal behavior remain unchanged.

**Evidence so far:** A live query sample found all active stacks in history replay and repeated source charge computation during encoding. Existing chargeOfTuple_tuple proves the representation equality; no receiving implementation or measured gain exists yet.

[Task brief](../sprints/2026-09-19/next-cycle-native-computation.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-NATIVE-COMPUTATION-0919 — Native query profile: repeated charge computation in reconstructed history](../sprints/2026-09-19/next-cycle-native-computation.md)

**Write scope:** minidregg admitted charge and intent/record construction; minidregg/Kernel/ResourceBirthReceiver.lean; minidregg lower-layer finite-charge helper and serialization equality proofs

## W-COORD-CONTRACT

**Compare the three existing local-first contracts**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-18T00:45:00-04:00

Compare breadstuffs History/World forks, minidregg hyperdocuments and lean-uwueave at identity, authority, offline operation, conflict, settlement and persistence boundaries.

**Next:** Select and exercise the cross-participant operation after the first authorized create/invoke/delegate/reopen journey.

**Done when:** A compatibility map identifying shared meaning, incompatible assumptions, and absent adapters. No inferred equivalence from similar names.

**Enables:**

- E-COORD — Coordination and replicated computation
- E-WORLD — Programmable social resource world

**Context dependencies:**

- C-SYNC-SCENARIO — Two-device document synchronization exists as a local replica test model
- C-UWUEAVE — lean-uwueave is a separate relevant coordination library

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-DECLARED-INVOKE

**Invoke a declared resource through the real kernel**

Status: **done** · Owner: Astra: localfirst · Updated: 2026-09-18T02:12:02-04:00

Compact commands use actual page execution, complete old authority, stored policy and accepted final-state evidence.

**Next:** Retain the actual native born-owner journey as a regression boundary during generation/revision and delegation migration.

**Done when:** An owner can invoke an authored operation, invalid requests refuse unchanged, and accepted data/receipt survive reopen.

**Evidence so far:** Mini 8056f9b actual native signed paid birth, initial source/owner/control creation, SQLite reopen and issued-owner invocation pass. Historical retry after expiry returns original receipt unchanged; forged signer/identity, changed payload and noncanonical bytes refuse. Fixture parameters; no deployment or delegation claim.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)

## W-DOC-PERSIST

**Establish the chosen document storage/turn contract**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T18:04:40.439Z

Implement durable refusal propagation and exact ordered physical history in breadstuffs, while joining resource birth, owner authority and charge in the canonical shared core. Repeated body updates still require the selected accepted operation and receiving cutover.

**Next:** Retain the unfinished Bread work and evidence as historical maintenance/reference; it is not a prerequisite for the New World implementation in Mini.

**Done when:** Repeated authorized saves, rejection without committed mutation, crash/reopen at each ordered boundary, and matching body/receipt history through the actual selected consumer. Physical setup journaling alone does not close kernel authorization.

**Evidence so far:** Earlier 24-test history repair passed; new targeted ordered-factory chronology tests pass. Kernel-authorized document saves remain a distinct receiving task. Work frozen at ember’s request; no agent is currently assigned.

**Enables:**

- E-DOC — Desktop document authoring
- E-COORD — Coordination and replicated computation

**Context dependencies:**

- C-DOC-DURABLE — Current desktop heap persistence refuses after a durable cell has participated in a turn

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-REBUILD-MINI-0919 — Ember chooses rebuilding the New World in Mini](../sprints/2026-09-19/rebuild-in-mini.md)

## W-EFFECT-ADMISSION

**Make full request and actual-pre binding mandatory for generic effects**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-18T03:34:10-04:00

Replace optional binding adapters with a source-derived family request and exact pre requirement in AcceptedCellEffect, migrating concrete families and consumers.

**Next:** Finish pending consumer modules and full-root checks without weakening the mandatory exact-parent/request/source contract.

**Done when:** All receiving constructors use the strengthened base token; target/verb/args/nonce/pre relabeling refuses, honest effects remain inhabited, and the integrated tree checks.

**Evidence so far:** Eight source modules and 28 exact axiom pins pass; actual joined native receiving journey also passed. Remaining consumer/root integration is unfinished. Work frozen at ember’s request; no agent is currently assigned.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)

## W-EMBEDDED-CANDIDATE

**Keep embedded candidates atomic through durable publication**

Status: **done** · Owner: Astra: root + resource_history · Updated: 2026-09-18T01:30:00-04:00

SDK/World align with the current node rejection policy: no retained fee, nonce, executor side-state or observer notification from a refused candidate. A possibly committed storage failure still requires authoritative reopen.

**Next:** Use the captured receiving evidence as a regression boundary while completing the linked resource journey.

**Done when:** Paid late refusal leaves exact prior state; storage refusal restores executor side-state; pending/unwound candidates cannot reenter; observer runs once only after acceptance; next success replays and reopens correctly.

**Evidence so far:** SDK 4/4 candidate/publication tests pass after lazy registration; World/cell/history24/24 pass at breadstuffs73136dd30 including paid refusal, storage failure, subsequent acceptance and reopen.

**Enables:**

- E-HERMES — External Hermes integration
- E-DOC — Desktop document authoring

**Evidence / provenance:**

- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)

## W-FACTORY-HISTORY

**Retain factory deployment at its actual history boundary**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T18:04:40.439Z

World deployment currently mutates volatile registries; historical paths either omit factories or preload the present registry into the past. Persist ordered descriptor/VK evidence and replay the actual executor deployment at that boundary.

**Next:** Retain the unfinished Bread work and evidence as historical maintenance/reference; it is not a prerequisite for the New World implementation in Mini.

**Done when:** Actual factory deployment, birth/mutation and recovery use the same ordered descriptor/VK evidence; no historical prefix sees a later factory; conflicting deployment and persistence failures leave committed state unchanged; unsupported old images refuse without changing evidence.

**Evidence so far:** All five targeted factory chronology tests passed twice in current native suites. Wider 24-case history/replay regression filter remains unrun after this repair. Work frozen at ember’s request; no agent is currently assigned.

**Enables:**

- E-DOC — Desktop document authoring
- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-REBUILD-MINI-0919 — Ember chooses rebuilding the New World in Mini](../sprints/2026-09-19/rebuild-in-mini.md)

## W-GRAIN-BROKER

**Custody and meter scoped provider requests**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T17:59:03.858Z

Execute bounded streaming requests after canonical reservation, retain exact evidence, fence old epochs, reconcile uncertain work and demonstrate secret isolation.

**Next:** After the core/resource contract is agreed, review preserved WIP against it and reassign a concrete receiving path before resuming this implementation.

**Done when:** Execute bounded streaming requests after canonical reservation, retain exact evidence, fence old epochs, reconcile uncertain work and demonstrate secret isolation.

**Evidence so far:** Paused after ember rejected the Python platform direction and requested deeper orientation. Existing WIP and earlier component evidence are preserved; no integrated acceptance is established. Previous assignment: Astra: grain_broker + root.

[Task brief](../sprints/2026-09-19/core-orientation.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)

**Acceptance:**

- Execute bounded streaming requests after canonical reservation, retain exact evidence, fence old epochs, reconcile uncertain work and demonstrate secret isolation.

## W-GRAIN-CONTROL

**Durable hosted grain control and authenticated entrance**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T17:59:03.858Z

Execute authenticated provisioning, hard/soft attachment, retained operation lookup and recovery through actual kernel/runtime adapters.

**Next:** After the core/resource contract is agreed, review preserved WIP against it and reassign a concrete receiving path before resuming this implementation.

**Done when:** Execute authenticated provisioning, hard/soft attachment, retained operation lookup and recovery through actual kernel/runtime adapters.

**Evidence so far:** Paused after ember rejected the Python platform direction and requested deeper orientation. Existing WIP and earlier component evidence are preserved; no integrated acceptance is established. Previous assignment: Astra: grain_control + root.

[Task brief](../sprints/2026-09-19/core-orientation.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)

**Acceptance:**

- Execute authenticated provisioning, hard/soft attachment, retained operation lookup and recovery through actual kernel/runtime adapters.

## W-GRAIN-RUNTIME

**Host upstream Hermes with persistent confined execution**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T17:59:03.858Z

Run real upstream Hermes in a confined Linux scope, preserve conversation/output, kill descendants on hard disconnect and retain exact scope on soft reconnect.

**Next:** After the core/resource contract is agreed, review preserved WIP against it and reassign a concrete receiving path before resuming this implementation.

**Done when:** Run real upstream Hermes in a confined Linux scope, preserve conversation/output, kill descendants on hard disconnect and retain exact scope on soft reconnect.

**Evidence so far:** Paused after ember rejected the Python platform direction and requested deeper orientation. Existing WIP and earlier component evidence are preserved; no integrated acceptance is established. Previous assignment: Astra: grain_runtime.

[Task brief](../sprints/2026-09-19/core-orientation.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)

**Acceptance:**

- Run real upstream Hermes in a confined Linux scope, preserve conversation/output, kill descendants on hard disconnect and retain exact scope on soft reconnect.

## W-GRAIN-TOOLS

**Expose canonical resource programming to Hermes**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T17:59:03.858Z

Drive real signed resource create/read/program/invoke/delegate/history operations through the source-owned host; reject stale generation authority without refreshing it.

**Next:** After the core/resource contract is agreed, review preserved WIP against it and reassign a concrete receiving path before resuming this implementation.

**Done when:** Drive real signed resource create/read/program/invoke/delegate/history operations through the source-owned host; reject stale generation authority without refreshing it.

**Evidence so far:** Paused after ember rejected the Python platform direction and requested deeper orientation. Existing WIP and earlier component evidence are preserved; no integrated acceptance is established. Previous assignment: Sol: grain_tools + host_json; Astra: grain_kernel.

[Task brief](../sprints/2026-09-19/core-orientation.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)

**Acceptance:**

- Drive real signed resource create/read/program/invoke/delegate/history operations through the source-owned host; reject stale generation authority without refreshing it.

## W-GRANT-REVISION

**Keep grants valid across policy source revisions**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-19T21:07:36.798Z

Separate immutable policy-source revision from grant revocation generation across the exact signed request, authority representation, compiled/source policies and every receiving consumer.

**Next:** Finish current combined acceptance, then implement and exercise explicit generation-wide revocation and the delegated-grant two-replacement case.

**Done when:** After two admitted rule replacements, previously issued owner/control and delegated grants remain usable exactly when their scope and new rules authorize the new request; stale revisions refuse, explicit generation revocation invalidates prior grants, and restart/retry preserves exact state and receipts. Resource policy can deliberately refuse further management, with no implicit owner bypass.

**Evidence so far:** Revision/generation separation is implemented. The earlier native candidate preserved original owner/control grants through two updates and enforced the new rule. Full combined runs remain pending; generation-wide native revocation and a delegated grant surviving two replacements remain separate closure obligations.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/Kernel/CapabilityRevocation*.lean; minidregg/Kernel/PolicyInstallController.lean and coordinated authority/control source; minidregg public native acceptance harness

## W-HERMES-STARTUP

**Make actual Hermes/SDK startup avoid unused Lean initialization**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T18:04:40.439Z

SDK route discovery is lazy while actual cryptographic calls retain real Lean initialization.

**Next:** Retain the unfinished Bread work and evidence as historical maintenance/reference; it is not a prerequisite for the New World implementation in Mini.

**Done when:** The same operations and refusal/publication checks pass through actual receiving code without eager unused-core initialization; real PQ first-use remains checked.

**Evidence so far:** Executor-family native initialization 41.285ms; focused 11-test suite PASS. Actual JS-agent Hermes test PASS 0.073s; full-byte PQ PASS. Final full/PQ/Hermes capture 5/5 PASS in 802.039s; lease released; width/string repairs staged only. No NetworkJudge inclusive startup gain established. Work frozen at ember’s request; no agent is currently assigned.

**Enables:**

- E-HERMES — External Hermes integration

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-REBUILD-MINI-0919 — Ember chooses rebuilding the New World in Mini](../sprints/2026-09-19/rebuild-in-mini.md)

## W-HOST-SESSION

**Retain verified history across native host requests**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-19T22:02:08.713Z

Replace repeated whole-history semantic replay with a source-owned verified session, preserving exact history identity, current authorization and durable CAS/recovery behavior.

**Next:** Agree and implement the verified-session and pinned-verifier contract, then exercise unchanged-image reuse and exact-prefix suffix replay through persistent stdio.

**Done when:** Prove verified-prefix plus suffix replay agrees with full semantic replay under explicit verifier assumptions; run unchanged-image, external append/revocation, rewritten/rolled-back history, stale challenge, exact CAS, lost reply, restart and verifier-change cases through the real host. Preserve fresh authorization, exact original receipt boundaries and uncertainty. Measure physical reads, replay counts and latency; do not substitute height/hash/mtime for exact image identity.

**Evidence so far:** Current native operations repeatedly verify retained original signed ingress. Matched birth and query measurements identify a concrete latency obstacle; a receiving contract and adversarial matrix are proposed, with no cache implementation claimed. A later bounded profile shows reconstructed history retains expensive charge functions; a cache alone would retain that recomputation. Charge materialization is tracked separately.

[Task brief](../sprints/2026-09-19/next-cycle-host-session.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-HOST-SESSION-PROPOSAL-0919 — Proposed persistent verified host session, grounded in measured native replay cost](../sprints/2026-09-19/next-cycle-host-session.md)
- [S-NATIVE-COMPUTATION-0919 — Native query profile: repeated charge computation in reconstructed history](../sprints/2026-09-19/next-cycle-native-computation.md)

**Write scope:** minidregg/Kernel/NativeHost.lean and NativeHostReplay.lean; minidregg/Host/Main.lean persistent stdio loop; minidregg native public acceptance and measured replay counts

## W-JOINT-POST

**Check composition against the actual joint post-state**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-19T21:07:36.798Z

Implement the general Mini transaction receiver over scalar and typed-content resources, with one exact joint post and current-policy admission for every incidence. Singleton mutations use the same receiver.

**Next:** Finish the combined native joint transaction and atomic-refusal checks; retain exact whole-image evidence.

**Done when:** Generic accepted composition preserves incidence outcomes, enforces resource laws and source-owned policy/postconditions on the actual joint result; hostile overlap/cross-field examples refuse, legitimate composition remains inhabited, and receiving constructors use the contract.

**Evidence so far:** General mixed scalar/content receiver and exact joint policy projections are implemented and compiled. The final signed task/content journey and invalid-second-leg rollback check are running.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/Kernel/ResourceTransaction*.lean; minidregg/Kernel/DeclaredResourceController.lean and shared scalar projection

## W-M26-DESIGN

**Define the September 26 programmable nexus and its shared contracts**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-19T21:07:36.798Z

Specify the coherent Mini resource/program and hosting contracts for the New World and complete hosted Nous Hermes experience. The construction home is settled; exact shared activity and economic operation remain open.

**Next:** Complete cycle acceptance and record the resulting core contracts and measured costs before assigning the next hosted experience cycle.

**Done when:** Accepted nexus operations and consequential design decisions; selected semantic and receiving-runtime paths; an explicit owned-node participation path and selected Solana/resource outcome; linked implementation obligations and evidence. Selecting a contract does not close implementation or deployment.

**Evidence so far:** Mini construction is committed through 12e6608. A real birth and task query execute; full combined native journeys remain pending. Hosted Hermes, physical interruption, contributed-node hosting and a selected Solana operation remain unfinished.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-DIRECTION-0919 — September 19 hosted Hermes direction, superseded Wisper plan and revised disconnect preference](../sprints/2026-09-19/direction.md)
- [S-PROTOCOL-REVIEW-0919 — Astra review of three Sol source investigations and proposed protocol boundaries](../sprints/2026-09-19/protocol-review.md)
- [S-CONNECTION-BREAKER-0919 — Disconnect as circuit breaker, explicit soft continuation and enforcement investigation](../sprints/2026-09-19/connection-breaker.md)
- [S-HERMES-BREAKER-0919 — Sol review of actual Hermes cancellation, descendants and continuation](../sprints/2026-09-19/reports/hermes-circuit-breaker.md)
- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-REBUILD-MINI-0919 — Ember chooses rebuilding the New World in Mini](../sprints/2026-09-19/rebuild-in-mini.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/docs/CYCLE-2026-09-19.md; dregg-assortia/sprints/2026-09-19/cycle-1.md and graph work records

## W-NATIVE-DATA-RECEIVER

**Connect canonical DataIntent execution to a real durable receiver**

Status: **done** · Owner: Astra: core_durable_receiver + proof_integrity · Updated: 2026-09-18T01:30:00-04:00

The existing Lean executor now crosses exact-byte SQLite CAS with crash/retry/concurrency checks; full source-authorized resource birth and product receiving joins remain active.

**Next:** Use the captured receiving evidence as a regression boundary while completing the linked resource journey.

**Done when:** A controller-bound multi-cell operation crosses real Lean decoding/admission/execute and physical CAS; stale/conflicting/malformed requests refuse, exact retry replays, and reopen preserves exact bytes and history.

**Evidence so far:** Actual controller-bound page and authority-marker writes pass native admission, SQLite publication, reopen, exact-ingress replay and conflicting/hostile input refusal. Probe authority is explicitly bootstrapped; accepted birth/delegation have their own active work.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)

## W-NATIVE-HOST

**Operate real resources through a compiled programmable host**

Status: **active** · Owner: Astra: root; Sol: cycle_build + cycle_client · Updated: 2026-09-19T21:07:36.798Z

Compile and exercise the source-owned Mini birth, joint transaction, policy, delegation, scoped observation and explicit revocation path through the public host and Rust client, with semantic replay and exact retry receipts.

**Next:** Capture complete results on immutable host 0da9f139 and its matching runner; verify final committed-source umbrella, then record performance and hosting work still required.

**Done when:** A real compiled host with operator-owned configuration accepts only source-authorized signed calls, preserves committed resources/receipts across restart and lost replies, and drives the same grant-preserving shared-resource journey through the programmable shell.

**Evidence so far:** Compiled host and Rust client exist. Matched birth fell from 223.78s to 49.43s with identical receipt bytes; a formerly stalled task query now completes in 33.55s. Full combined umbrella and fresh New World, legacy and client journeys are running.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/Compiler/NativeHostCodec.lean; minidregg/Kernel/NativeHost*.lean; minidregg/Host/Main.lean and Host/Json.lean; minidregg/native/resource-client/; minidregg isolated native build and public journey harness

## W-POLICY-SOURCE

**Store initial policies and use one runtime profile**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-19T21:07:36.798Z

Immutable internal policy-source cells and a common field/compiler/request profile make resource creation, invocation and policy replacement agree.

**Next:** Record final umbrella and actual native policy-source/current-rule checks together.

**Done when:** Policy source is created atomically and selected from the same durable directory; kind/domain/address mismatches refuse, and all consuming verbs share compatible source semantics.

**Evidence so far:** One source/runtime profile now covers birth, content, joint invocation, policy replacement, observation and revocation. Consumer migration passed broad gates; final proved performance changes are undergoing the committed-source gate.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/Compiler/CanonicalRuntimeProfile.lean and coordinated policy/control source; minidregg/Compiler/NativeHostCodec.lean; minidregg shared umbrella imports

## W-PROGRAMMABLE-PATH

**Implement and exercise the canonical authored-program-to-resource path**

Status: **active** · Owner: Astra: root; Sol: cycle_build + cycle_client · Updated: 2026-09-19T21:07:36.798Z

Build and exercise the canonical Mini resource-programming path with installed laws, typed content, joint mutations and scoped observation, exposed through the source-owned host and Rust client.

**Next:** Complete corrected Rust-client and native resource journeys on the same source-matched executable.

**Done when:** Author and install a rule under actual resource authority, invoke a permitted operation through the chosen shell/agent path, refuse a violating operation with correct state/outcome evidence, and recover accepted behavior/history through the chosen durable runtime. Complete all necessary core obligations, not merely a private demo.

**Evidence so far:** Source-owned authoring, typed birth/content and mixed transactions are implemented. The client exercised real lost-response recovery; its neutral scalar fixture expectation was corrected. Fresh full client and kernel journeys are running.

[Task brief](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Enables:**

- E-WORLD — Programmable social resource world
- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-PROGRAMMING-REVIEW — Parent-reviewed programming and shell investigation](../research/programming.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)

**Write scope:** minidregg/Kernel/ResourceTransaction*.lean; minidregg/Kernel/ContentResource*.lean and canonical content materializers; minidregg/Host/Json.lean; minidregg/native/resource-client/; minidregg public native acceptance harness

## W-PROVIDER-PATH

**Inventory existing provider job and penalty machinery**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-18T00:45:00-04:00

Trace eligible jobs, registration/stake, result commitments, challenges, adjudication and penalty effects, including the difference between wrong results and availability failures.

**Next:** Choose the eligible public job and its exact result checker, provider obligation and penalty-record consumer.

**Done when:** Current source/evidence inventory; explicit job class, custody and verdict-to-effect boundaries. No transfers, stake locking or deployment.

**Evidence so far:** Source inventory exists; connected provider eligibility/job/result/adjudication/penalty path is unfinished.

**Enables:**

- E-PROVIDERS — Contributed hosting and optimistic provider accountability

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-RESOURCE-BIRTH

**Implement one accepted resource birth with owner authority and charge**

Status: **done** · Owner: Astra: proof_integrity + program_install · Updated: 2026-09-18T02:12:02-04:00

Reuse canonical CellRegistry, authority pages, ordered resource Book batches, MultiCellHyperedge and DataIntent; one final write per physical cell.

**Next:** Retain the actual native born-owner journey as a regression boundary during generation/revision and delegation migration.

**Done when:** Actual source-authorized birth commits identity, initial content, owner grant and selected fee together; refusals and crash/retry cannot expose a partial accepted result.

**Evidence so far:** Mini 8056f9b actual native signed paid birth, initial source/owner/control creation, SQLite reopen and issued-owner invocation pass. Historical retry after expiry returns original receipt unchanged; forged signer/identity, changed payload and noncanonical bytes refuse. Fixture parameters; no deployment or delegation claim.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)

## W-SOLANA-UTILITY

**Choose and close one economic operation consumed by a nexus resource**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-18T00:45:00-04:00

Compare provider bonds, resource payments and Clutch claim/settlement operations. Holder admission is useful existing material but does not alone perform an on-chain mutation. Specify the real asset/cluster and the DREGG receiver of the external result.

**Next:** Choose exact economic operation, real asset/cluster, custody and exit terms before a live transaction.

**Done when:** A selected user-visible economic function with exact mint/program/cluster, custody and release policy where applicable, external evidence acceptance and resource-result binding; required source/consumer changes and acceptance checks identified, then exercised at an explicitly authorized deployment scope.

**Evidence so far:** Accepted intent: real stake locked, penalties recorded only. Token-2022/legacy-token compatibility and nexus result consumption are unresolved.

**Enables:**

- E-SOLANA — Solana-facing asset and resource participation
- E-CLUTCH — Clutch claim, market and settlement resources
- E-PROVIDERS — Contributed hosting and optimistic provider accountability

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-SOURCE-IMPACT

**Make source freshness portable and actionable**

Status: **done** · Owner: Astra: core_resource_pages · Updated: 2026-09-19T11:21:30-04:00

Report which claims/work items need reinspection when source bytes change, with repository paths configurable on a contributor machine.

**Next:** Use and maintain the tested hub tools during handoffs; the unassigned hosting-contract proposal remains in W-ANDROID-CONTRACT, while hosted-Hermes design continues in W-M26-DESIGN.

**Done when:** The checker identifies unavailable repositories separately from changed files, explains affected records without rewriting their historical hashes, and runs against temporary fixture repositories.

**Evidence so far:** 23 focused tests,41 total hub tests and actual CLI fixtures pass; unavailable evidence is unknown, old hashes remain unchanged, and contextual reference paths are explicit.

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-HUB-TOOLS-0145 — Graph navigation/source-impact tooling and captured tests](../sprints/2026-09-18/hub-tools-0145.md)
- [S-DIRECTION-0919 — September 19 hosted Hermes direction, superseded Wisper plan and revised disconnect preference](../sprints/2026-09-19/direction.md)
