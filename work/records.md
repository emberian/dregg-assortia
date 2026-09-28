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

Status: **done** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-20T00:00:01.955Z

Persist exact signing keys/epochs; accept actual configured native verification of the exact request and capability against the complete same-snapshot authority.

**Next:** Retain the source-matched native and Rust-client evidence as regression boundaries while building the persistent host and real agent lifecycle. This closure does not claim a deployed hosted platform.

**Done when:** Actual installed verification plus complete committed authority checks feed accepted source operations; stale/altered/revoked credentials cannot authorize them.

**Evidence so far:** Complete native receiving exercised actual detached signatures, exact observation roles, wrong-kind/internal/excess/missing/reordered read refusals, current-law direct-submit checks, per-capability revocation and stale-worker generation fencing. Refusals preserve the entire durable image. The separate Rust authority recipe also passed ordinary authored delegation/escalation/revocation/retry.

[Task brief](../sprints/2026-09-19/cycle-1-result.md)

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
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)

**Write scope:** minidregg/Kernel/CapabilityRevocation*.lean; minidregg/Kernel/NativeObservationController.lean; minidregg/Compiler/NativeObservationCodec.lean; minidregg/Assurance/CapabilityRevocationAudit.lean and NativeObservationAudit.lean

## W-AUTHORIZED-DELEGATION

**Give a friend a narrower usable right**

Status: **done** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-20T00:00:01.955Z

Add an explicit authorized subject-to-subject delegation edge without weakening strict holder-narrowing or inventing bearer custody.

**Next:** Retain the source-matched native and Rust-client evidence as regression boundaries while building the persistent host and real agent lifecycle. This closure does not claim a deployed hosted platform.

**Done when:** Owner delegates a bounded right; friend can use that right, cannot exceed it or replace policy, and revocation/current epochs remain enforced.

**Evidence so far:** Native and ordinary Rust-client journeys passed Alice-to-Bob narrower delegation, permitted use, prohibited policy escalation, explicit revocation and exact historical recovery. The complete joint task/content scenario also preserves the worker grants through a rule revision and fences a freshly signed old worker under the current generation rule.

[Task brief](../sprints/2026-09-19/cycle-1-result.md)

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
- [S-CLIENT-AUTHORITY-0919 — Completed Rust authority client journey on b119f86 host](../sprints/2026-09-19/cycle-1-evidence/final-client-authority/README.md)
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)

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

Status: **done** · Owner: Astra: cycle_authority; Sol: cycle_build; root integration/review · Updated: 2026-09-19T22:33:11.191Z

Preserve exact admitted charges and record bytes while removing repeated birth write/read-guard computation during historical serialization.

**Next:** Retain the exact proof/build/runtime evidence as a regression boundary. W-HOST-SESSION now has scoped native evidence in the September 26 checkpoints and continues integration; do not extrapolate the measured workload into a general speedup.

**Done when:** The actual receiving/replay path retains materialized charge data; a general proof preserves every charge lane, complete intent/record identity and canonical bytes without changed bounds or tariffs. Generated-code and matched native operation evidence show repeated serialization does not reconstruct birth writes/read guards, and semantic replay, receipts, charges and refusal behavior remain unchanged.

**Evidence so far:** Implemented at 66d74dd: finite charge values and general complete-charge/intent/record/byte equalities; actual receiving and replay retain the values. Full umbrella/native link passed with exact 581-file committed source match. Matched eight-event signed query accepted with identical view and unchanged entire logical image: immediate parent105.51s versus charge91.66s (one trial, 13.13% reduction). Latest host also returns the exact original stale-worker refusal with unchanged whole image. Earlier one-event query and birth comparisons showed no gain and used different baseline hosts. The completed representation change does not make the host interactive or eliminate full-history replay.

[Task brief](../sprints/2026-09-19/next-cycle-native-computation.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-NATIVE-COMPUTATION-0919 — Native query profile: repeated charge computation in reconstructed history](../sprints/2026-09-19/next-cycle-native-computation.md)
- [S-CHARGE-BUILD-0919 — Exact 66d74dd full umbrella and native charge-materialization build](../sprints/2026-09-19/cycle-1-evidence/charge-build/README.md)
- [S-CHARGE-HISTORY8-0919 — Matched charge-materialized query against eight-event history](../sprints/2026-09-19/cycle-1-evidence/charge-history8-benchmark/README.md)
- [S-CHARGE-REFUSAL-0919 — Charge host replays eight events and refuses the stale worker unchanged](../sprints/2026-09-19/cycle-1-evidence/charge-stale-worker/README.md)

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

## W-FN-INTEGRATION

**Operate actual Mini resources through fn correspondence and separate gateways**

Status: **active** · Owner: Sol: fn_contracts; Astra: root · Updated: 2026-09-27T05:18:14.567Z

Converge existing fn consumer lineage and improve its authority, fresh setup, general reply profiles and distributed hosted receiving path.

**Next:** Finish selected-release durable receiver and exact historical retry checks, integrate native Host/Replay/CLI route, then exercise authorized selected public bytes through actual fn without private-prefix disclosure. Receiver import/install remains separate authority.

**Done when:** Real Mini-resource operation and reply travel through independently configured fn nodes with separately pinned application authorities; durable Mini processing precedes fn ACK, direct forged consumer input is refused, exact retries and uncertain outcomes reconcile, and a documented user entrance uses this path.

**Evidence so far:** Native own-R accept/restart/repeat/ACK and equal-position no-op passed on fresh private Store. Exact owner-release codec and current-key signature component narrowly checked; receiving/replay remains construction. Selected-release Signature/Ingress/Admission have narrow source checks; new durable receiver is under construction. No native route or selected-release transport run is claimed. Mini b6373d7 now commits narrow-checked selected-release admission/receiver; dedicated native routing and replay are being integrated. Mini9a128b4 article framing, b9b9869 exact-attempt CLI, and e1bbf2d native submit/lookup/replay source are checked and committed. Separate source publication authority is being built; no end-to-end selected release run yet.

[Task brief](../sprints/2026-09-26/checkpoint-17.md)

**Enables:**

- E-WORLD — Programmable social resource world
- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-OVERNIGHT-0926 — September 26 overnight actual fn/Mini construction authorization and lane plan](../sprints/2026-09-26/overnight.md)
- [S-CHECKPOINT1-0926 — Overnight published core checkpoints and fresh integration failures](../sprints/2026-09-26/checkpoint-1.md)
- [S-CHECKPOINT2-0926 — Native persistent receiving and distributed integration checkpoint](../sprints/2026-09-26/checkpoint-2.md)
- [S-CHECKPOINT3-0926 — Linked Mini hosts, native prefix evidence and active hosted receiving](../sprints/2026-09-26/checkpoint-3.md)
- [S-CHECKPOINT4-0926 — Fresh complete fn exchange, physical interruption repairs and ongoing hosted integration](../sprints/2026-09-26/checkpoint-4.md)
- [S-CHECKPOINT5-0926 — Actual Hermes publication, native hard fence, faster observations and durable fn worker](../sprints/2026-09-26/checkpoint-5.md)
- [S-CHECKPOINT6-0926 — Real Hermes reconnect, committed missing reply, signed grain fn transport and reader-profile gap](../sprints/2026-09-26/checkpoint-6.md)
- [S-CHECKPOINT7-0926 — Actual SSH grain, provider custody, late-effect reporting and core hash repair](../sprints/2026-09-26/checkpoint-7.md)
- [S-CHECKPOINT8-0926 — Complete real grain fn exchange, hosted provider and crash recovery; resumed construction](../sprints/2026-09-26/checkpoint-8.md)
- [S-CHECKPOINT9-0926 — Delivered same-session workroom receipt, first durable fn POST, interrupt source and large-call pair](../sprints/2026-09-26/checkpoint-9.md)
- [S-CHECKPOINT10-0926 — Combined Mini builds, corrected native members, scoped recovery, workroom R2 fn publication and provider continuity](../sprints/2026-09-26/checkpoint-10.md)
- [S-CHECKPOINT11-0926 — Proved native hash speedup, exact-readback integration, hosted peer publications and recovered fn receive](../sprints/2026-09-26/checkpoint-11.md)
- [S-CHECKPOINT12-0926 — Combined native speed and adversaries, fresh law recovery, scoped hosted peer and receipt progress](../sprints/2026-09-26/checkpoint-12.md)
- [S-CHECKPOINT13-0926 — Exact hosted Hermes receipt, held fn B ACK/read completion and scoped next-source construction](../sprints/2026-09-26/checkpoint-13.md)
- [S-CHECKPOINT14-0926 — Signed cross-UID resources, fresh stale-root cleanup and operator-assisted workroom fn reply](../sprints/2026-09-26/checkpoint-14.md)
- [S-CHECKPOINT15-0926 — Dedicated-account Hermes shared workroom, read-only provider quote and linked typed A view](../sprints/2026-09-26/checkpoint-15.md)
- [S-FN-DISCLOSURE-0927 — Semi-untrusted fn principle and source-grounded publication disclosure investigation](../sprints/2026-09-26/fn-publication-disclosure-contract.md)
- [S-CHECKPOINT16-0926 — Native provider settlement, own-R restart failure and continued kernel/hosting construction](../sprints/2026-09-26/checkpoint-16.md)
- [S-CHECKPOINT17-0926 — Native restart, terminal, sequential metering and resource birth progress](../sprints/2026-09-26/checkpoint-17.md)
- [S-PARALLEL-JOURNEYS-0927 — Parallel platform journeys and independent app-issued authority requirement](../sprints/2026-09-26/parallel-journeys.md)
- [S-SPK-CHECKPOINT20-0927 — Parallel journeys and checked receiving core checkpoint](../sprints/2026-09-26/checkpoint-20.md)
- [S-SPK-CHECKPOINT21-0927 — Real GitWeb work and connected receiving paths](../sprints/2026-09-26/checkpoint-21.md)

**Write scope:** minidregg/Kernel/Fn*.lean; minidregg/Host/Json.lean; minidregg/scripts/fn-e1e2/; minidregg/Compiler/FnEvidenceCodec.lean; minidregg/Host/Main.lean; minidregg/Host/GrainOriginSource.lean; minidregg/native/resource-client/; minidregg/Host/GrainOriginPreparation.lean; minidregg/docs/FN-PUBLICATION-DISCLOSURE.md

## W-GRAIN-BROKER

**Custody and meter scoped provider requests**

Status: **active** · Owner: Sol: runtime_review, build_native; Astra: root · Updated: 2026-09-27T23:59:51.217Z

Execute bounded streaming requests after canonical reservation, retain exact evidence, fence old epochs, reconcile uncertain work and demonstrate secret isolation.

**Next:** Qualify local Ternary Bonsai 2 27B on hbox and run actual hosted Hermes through current Mini provider custody; integrate DREGG-paid provider access as an additional route after its API and accounting contract are established.

**Done when:** Execute bounded streaming requests after canonical reservation, retain exact evidence, fence old epochs, reconcile uncertain work and demonstrate secret isolation.

**Evidence so far:** Three sequential Hermes requests separately quoted/settled at counts11/15/23; provider reserve zero. Missing usage and HTTP422 retain held uncertain responses.

[Task brief](../sprints/2026-09-26/checkpoint-17.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-CHECKPOINT4-0926 — Fresh complete fn exchange, physical interruption repairs and ongoing hosted integration](../sprints/2026-09-26/checkpoint-4.md)
- [S-CHECKPOINT5-0926 — Actual Hermes publication, native hard fence, faster observations and durable fn worker](../sprints/2026-09-26/checkpoint-5.md)
- [S-CHECKPOINT6-0926 — Real Hermes reconnect, committed missing reply, signed grain fn transport and reader-profile gap](../sprints/2026-09-26/checkpoint-6.md)
- [S-CHECKPOINT7-0926 — Actual SSH grain, provider custody, late-effect reporting and core hash repair](../sprints/2026-09-26/checkpoint-7.md)
- [S-CHECKPOINT8-0926 — Complete real grain fn exchange, hosted provider and crash recovery; resumed construction](../sprints/2026-09-26/checkpoint-8.md)
- [S-CHECKPOINT9-0926 — Delivered same-session workroom receipt, first durable fn POST, interrupt source and large-call pair](../sprints/2026-09-26/checkpoint-9.md)
- [S-CHECKPOINT10-0926 — Combined Mini builds, corrected native members, scoped recovery, workroom R2 fn publication and provider continuity](../sprints/2026-09-26/checkpoint-10.md)
- [S-CHECKPOINT12-0926 — Combined native speed and adversaries, fresh law recovery, scoped hosted peer and receipt progress](../sprints/2026-09-26/checkpoint-12.md)
- [S-CHECKPOINT13-0926 — Exact hosted Hermes receipt, held fn B ACK/read completion and scoped next-source construction](../sprints/2026-09-26/checkpoint-13.md)
- [S-CHECKPOINT14-0926 — Signed cross-UID resources, fresh stale-root cleanup and operator-assisted workroom fn reply](../sprints/2026-09-26/checkpoint-14.md)
- [S-CHECKPOINT15-0926 — Dedicated-account Hermes shared workroom, read-only provider quote and linked typed A view](../sprints/2026-09-26/checkpoint-15.md)
- [S-CHECKPOINT16-0926 — Native provider settlement, own-R restart failure and continued kernel/hosting construction](../sprints/2026-09-26/checkpoint-16.md)
- [S-CHECKPOINT17-0926 — Native restart, terminal, sequential metering and resource birth progress](../sprints/2026-09-26/checkpoint-17.md)
- [S-PAYMENT-INFERENCE-0927 — DREGG-only inference direction and payment/provider source audit](../research/payment-inference-2026-09-27.md)

**Write scope:** minidregg/native/grain-runtime/src/provider.rs; minidregg/native/grain-runtime/src/main.rs; minidregg/deploy/grain-host/

**Acceptance:**

- Execute bounded streaming requests after canonical reservation, retain exact evidence, fence old epochs, reconcile uncertain work and demonstrate secret isolation.

## W-GRAIN-CONTROL

**Durable hosted grain control and authenticated entrance**

Status: **active** · Owner: Sol: client_session, hermes_path, fn_reply_profile; Astra: root · Updated: 2026-09-27T02:10:00Z

Execute authenticated provisioning, hard/soft attachment, retained operation lookup and recovery through actual kernel/runtime adapters.

**Next:** Complete short spawn/cancel critical section and custody ownership without blocking immediate worker stop; preserve uncertainty and exact-call recovery.

**Done when:** Execute authenticated provisioning, hard/soft attachment, retained operation lookup and recovery through actual kernel/runtime adapters.

**Evidence so far:** Dedicated operator stack installed and explicitly restarted with stable signed root; terminal source and actual worker controls exercised on fresh fixture.

[Task brief](../sprints/2026-09-26/checkpoint-17.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-OVERNIGHT-0926 — September 26 overnight actual fn/Mini construction authorization and lane plan](../sprints/2026-09-26/overnight.md)
- [S-CHECKPOINT4-0926 — Fresh complete fn exchange, physical interruption repairs and ongoing hosted integration](../sprints/2026-09-26/checkpoint-4.md)
- [S-CHECKPOINT5-0926 — Actual Hermes publication, native hard fence, faster observations and durable fn worker](../sprints/2026-09-26/checkpoint-5.md)
- [S-CHECKPOINT6-0926 — Real Hermes reconnect, committed missing reply, signed grain fn transport and reader-profile gap](../sprints/2026-09-26/checkpoint-6.md)
- [S-CHECKPOINT7-0926 — Actual SSH grain, provider custody, late-effect reporting and core hash repair](../sprints/2026-09-26/checkpoint-7.md)
- [S-CHECKPOINT8-0926 — Complete real grain fn exchange, hosted provider and crash recovery; resumed construction](../sprints/2026-09-26/checkpoint-8.md)
- [S-CHECKPOINT9-0926 — Delivered same-session workroom receipt, first durable fn POST, interrupt source and large-call pair](../sprints/2026-09-26/checkpoint-9.md)
- [S-CHECKPOINT10-0926 — Combined Mini builds, corrected native members, scoped recovery, workroom R2 fn publication and provider continuity](../sprints/2026-09-26/checkpoint-10.md)
- [S-CHECKPOINT11-0926 — Proved native hash speedup, exact-readback integration, hosted peer publications and recovered fn receive](../sprints/2026-09-26/checkpoint-11.md)
- [S-CHECKPOINT12-0926 — Combined native speed and adversaries, fresh law recovery, scoped hosted peer and receipt progress](../sprints/2026-09-26/checkpoint-12.md)
- [S-CHECKPOINT13-0926 — Exact hosted Hermes receipt, held fn B ACK/read completion and scoped next-source construction](../sprints/2026-09-26/checkpoint-13.md)
- [S-CHECKPOINT14-0926 — Signed cross-UID resources, fresh stale-root cleanup and operator-assisted workroom fn reply](../sprints/2026-09-26/checkpoint-14.md)
- [S-CHECKPOINT15-0926 — Dedicated-account Hermes shared workroom, read-only provider quote and linked typed A view](../sprints/2026-09-26/checkpoint-15.md)
- [S-CHECKPOINT16-0926 — Native provider settlement, own-R restart failure and continued kernel/hosting construction](../sprints/2026-09-26/checkpoint-16.md)
- [S-CHECKPOINT17-0926 — Native restart, terminal, sequential metering and resource birth progress](../sprints/2026-09-26/checkpoint-17.md)

**Write scope:** minidregg/native/resource-client/; minidregg/native/grain-runtime/; minidregg/Host/Json.lean

**Acceptance:**

- Execute authenticated provisioning, hard/soft attachment, retained operation lookup and recovery through actual kernel/runtime adapters.

## W-GRAIN-RUNTIME

**Host upstream Hermes with persistent confined execution**

Status: **active** · Owner: Sol: hermes_path, replay_session, linux_hosting; review runtime_review; Astra: root · Updated: 2026-09-27T02:10:00Z

Run real upstream Hermes in a confined Linux scope, preserve conversation/output, kill descendants on hard disconnect and retain exact scope on soft reconnect.

**Next:** Finish birth charge crash recovery and dispatch cancellation; exercise soft EOF and usable hard-stop reconnect/recovery.

**Done when:** Run real upstream Hermes in a confined Linux scope, preserve conversation/output, kill descendants on hard disconnect and retain exact scope on soft reconnect.

**Evidence so far:** Installed runtime e213b4f passed 50 tests/clippy. Terminal publication and hard EOF physically exercised. Old same-UID B44 recovered through explicit audit and native zero settlement.

[Task brief](../sprints/2026-09-26/checkpoint-17.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-OVERNIGHT-0926 — September 26 overnight actual fn/Mini construction authorization and lane plan](../sprints/2026-09-26/overnight.md)
- [S-CHECKPOINT1-0926 — Overnight published core checkpoints and fresh integration failures](../sprints/2026-09-26/checkpoint-1.md)
- [S-CHECKPOINT2-0926 — Native persistent receiving and distributed integration checkpoint](../sprints/2026-09-26/checkpoint-2.md)
- [S-CHECKPOINT3-0926 — Linked Mini hosts, native prefix evidence and active hosted receiving](../sprints/2026-09-26/checkpoint-3.md)
- [S-CHECKPOINT4-0926 — Fresh complete fn exchange, physical interruption repairs and ongoing hosted integration](../sprints/2026-09-26/checkpoint-4.md)
- [S-CHECKPOINT5-0926 — Actual Hermes publication, native hard fence, faster observations and durable fn worker](../sprints/2026-09-26/checkpoint-5.md)
- [S-CHECKPOINT6-0926 — Real Hermes reconnect, committed missing reply, signed grain fn transport and reader-profile gap](../sprints/2026-09-26/checkpoint-6.md)
- [S-CHECKPOINT7-0926 — Actual SSH grain, provider custody, late-effect reporting and core hash repair](../sprints/2026-09-26/checkpoint-7.md)
- [S-CHECKPOINT8-0926 — Complete real grain fn exchange, hosted provider and crash recovery; resumed construction](../sprints/2026-09-26/checkpoint-8.md)
- [S-CHECKPOINT9-0926 — Delivered same-session workroom receipt, first durable fn POST, interrupt source and large-call pair](../sprints/2026-09-26/checkpoint-9.md)
- [S-CHECKPOINT10-0926 — Combined Mini builds, corrected native members, scoped recovery, workroom R2 fn publication and provider continuity](../sprints/2026-09-26/checkpoint-10.md)
- [S-CHECKPOINT11-0926 — Proved native hash speedup, exact-readback integration, hosted peer publications and recovered fn receive](../sprints/2026-09-26/checkpoint-11.md)
- [S-CHECKPOINT12-0926 — Combined native speed and adversaries, fresh law recovery, scoped hosted peer and receipt progress](../sprints/2026-09-26/checkpoint-12.md)
- [S-CHECKPOINT13-0926 — Exact hosted Hermes receipt, held fn B ACK/read completion and scoped next-source construction](../sprints/2026-09-26/checkpoint-13.md)
- [S-CHECKPOINT14-0926 — Signed cross-UID resources, fresh stale-root cleanup and operator-assisted workroom fn reply](../sprints/2026-09-26/checkpoint-14.md)
- [S-CHECKPOINT15-0926 — Dedicated-account Hermes shared workroom, read-only provider quote and linked typed A view](../sprints/2026-09-26/checkpoint-15.md)
- [S-CHECKPOINT16-0926 — Native provider settlement, own-R restart failure and continued kernel/hosting construction](../sprints/2026-09-26/checkpoint-16.md)
- [S-CHECKPOINT17-0926 — Native restart, terminal, sequential metering and resource birth progress](../sprints/2026-09-26/checkpoint-17.md)

**Write scope:** minidregg/native/grain-runtime/; minidregg/Kernel/AgentGrain.lean; minidregg/Host/Json.lean; minidregg/deploy/grain-host/

**Acceptance:**

- Run real upstream Hermes in a confined Linux scope, preserve conversation/output, kill descendants on hard disconnect and retain exact scope on soft reconnect.

## W-GRAIN-TOOLS

**Expose canonical resource programming to Hermes**

Status: **active** · Owner: Sol: hermes_path, replay_session, codec_stack, shared_resource_tools; Astra: root · Updated: 2026-09-27T02:10:00Z

Drive real signed resource create/read/program/invoke/delegate/history operations through the source-owned host; reject stale generation authority without refreshing it.

**Next:** Fix durable pre-reserve birth intent and refusal zero-phase recovery, final dispatch cancellation, then exercise created-resource tools through Hermes and exact restart.

**Done when:** Drive real signed resource create/read/program/invoke/delegate/history operations through the source-owned host; reject stale generation authority without refreshing it.

**Evidence so far:** Native composite created8301/count11 and owner bare8303/count12. Worker bare refused uniformly; runner expected wrong private reason. Controller birth lifecycle review found crash/charge windows.

[Task brief](../sprints/2026-09-26/checkpoint-17.md)

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-GRAIN-IMPLEMENTATION-0919 — Historical, subsequently paused agent-grain implementation wave](../sprints/2026-09-19/implementation.md)
- [S-CORE-ORIENTATION-0919 — Bread/Mini microswarm after implementation pause](../sprints/2026-09-19/core-orientation.md)
- [S-CHECKPOINT1-0926 — Overnight published core checkpoints and fresh integration failures](../sprints/2026-09-26/checkpoint-1.md)
- [S-CHECKPOINT2-0926 — Native persistent receiving and distributed integration checkpoint](../sprints/2026-09-26/checkpoint-2.md)
- [S-CHECKPOINT3-0926 — Linked Mini hosts, native prefix evidence and active hosted receiving](../sprints/2026-09-26/checkpoint-3.md)
- [S-CHECKPOINT4-0926 — Fresh complete fn exchange, physical interruption repairs and ongoing hosted integration](../sprints/2026-09-26/checkpoint-4.md)
- [S-CHECKPOINT5-0926 — Actual Hermes publication, native hard fence, faster observations and durable fn worker](../sprints/2026-09-26/checkpoint-5.md)
- [S-CHECKPOINT6-0926 — Real Hermes reconnect, committed missing reply, signed grain fn transport and reader-profile gap](../sprints/2026-09-26/checkpoint-6.md)
- [S-CHECKPOINT7-0926 — Actual SSH grain, provider custody, late-effect reporting and core hash repair](../sprints/2026-09-26/checkpoint-7.md)
- [S-CHECKPOINT8-0926 — Complete real grain fn exchange, hosted provider and crash recovery; resumed construction](../sprints/2026-09-26/checkpoint-8.md)
- [S-CHECKPOINT9-0926 — Delivered same-session workroom receipt, first durable fn POST, interrupt source and large-call pair](../sprints/2026-09-26/checkpoint-9.md)
- [S-CHECKPOINT10-0926 — Combined Mini builds, corrected native members, scoped recovery, workroom R2 fn publication and provider continuity](../sprints/2026-09-26/checkpoint-10.md)
- [S-CHECKPOINT11-0926 — Proved native hash speedup, exact-readback integration, hosted peer publications and recovered fn receive](../sprints/2026-09-26/checkpoint-11.md)
- [S-CHECKPOINT12-0926 — Combined native speed and adversaries, fresh law recovery, scoped hosted peer and receipt progress](../sprints/2026-09-26/checkpoint-12.md)
- [S-CHECKPOINT13-0926 — Exact hosted Hermes receipt, held fn B ACK/read completion and scoped next-source construction](../sprints/2026-09-26/checkpoint-13.md)
- [S-CHECKPOINT14-0926 — Signed cross-UID resources, fresh stale-root cleanup and operator-assisted workroom fn reply](../sprints/2026-09-26/checkpoint-14.md)
- [S-CHECKPOINT15-0926 — Dedicated-account Hermes shared workroom, read-only provider quote and linked typed A view](../sprints/2026-09-26/checkpoint-15.md)
- [S-CHECKPOINT16-0926 — Native provider settlement, own-R restart failure and continued kernel/hosting construction](../sprints/2026-09-26/checkpoint-16.md)
- [S-CHECKPOINT17-0926 — Native restart, terminal, sequential metering and resource birth progress](../sprints/2026-09-26/checkpoint-17.md)

**Write scope:** minidregg/native/grain-runtime/; minidregg/Kernel/AgentGrain.lean; minidregg/Host/Json.lean; minidregg/scripts/workroom/; minidregg/Compiler/GrainResourceBirthController.lean

**Acceptance:**

- Drive real signed resource create/read/program/invoke/delegate/history operations through the source-owned host; reject stale generation authority without refreshing it.

## W-GRANT-REVISION

**Keep grants valid across policy source revisions**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-20T00:00:01.955Z

Separate immutable policy-source revision from grant revocation generation across the exact signed request, authority representation, compiled/source policies and every receiving consumer.

**Next:** Implement and exercise generation-wide native revocation and the delegated-grant two-replacement case against the same source-owned receiving path; preserve the completed per-capability/current-law regressions.

**Done when:** After two admitted rule replacements, previously issued owner/control and delegated grants remain usable exactly when their scope and new rules authorize the new request; stale revisions refuse, explicit generation revocation invalidates prior grants, and restart/retry preserves exact state and receipts. Resource policy can deliberately refuse further management, with no implicit owner bypass.

**Evidence so far:** Revision/generation separation and per-capability revocation passed full native integration. Original owner/control grants survive two policy replacements in the legacy scenario; delegated worker grants survive one replacement in the New World scenario, with current-law enforcement and deliberate owner management lockout. Explicit generation-wide native revocation and a delegated grant surviving two replacements remain uncompleted closure obligations.

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
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)

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

Status: **active** · Owner: Astra: root; Sol: fn_mini_review · Updated: 2026-09-28T00:05:41.042Z

Replace repeated whole-history semantic replay with a source-owned verified session, preserving exact history identity, current authorization and durable CAS/recovery behavior.

**Next:** Recover app bootstrap with separately authorized tool attach, fresh read/reserve and retained refused attempt; finish actual app admission then INSTALL/START, shared human/agent use and fn receiving.

**Done when:** Prove verified-prefix plus suffix replay agrees with full semantic replay under explicit verifier assumptions; run unchanged-image, external append/revocation, rewritten/rolled-back history, stale challenge, exact CAS, lost reply, restart and verifier-change cases through the real host. Preserve fresh authorization, exact original receipt boundaries and uncertainty. Measure physical reads, replay counts and latency; do not substitute height/hash/mtime for exact image identity.

**Evidence so far:** Retained workroom recovery passed eight signed views and six parent delegations; next app reserve explicitly refused with tool7902 detached, Store unchanged. Mixed-route config committed/tested; accepted-grant inspector passed narrow Lean; real local model qualification and source integration ongoing.

[Task brief](../sprints/2026-09-26/checkpoint-17.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-HOST-SESSION-PROPOSAL-0919 — Proposed persistent verified host session, grounded in measured native replay cost](../sprints/2026-09-19/next-cycle-host-session.md)
- [S-NATIVE-COMPUTATION-0919 — Native query profile: repeated charge computation in reconstructed history](../sprints/2026-09-19/next-cycle-native-computation.md)
- [S-OVERNIGHT-0926 — September 26 overnight actual fn/Mini construction authorization and lane plan](../sprints/2026-09-26/overnight.md)
- [S-CHECKPOINT1-0926 — Overnight published core checkpoints and fresh integration failures](../sprints/2026-09-26/checkpoint-1.md)
- [S-CHECKPOINT2-0926 — Native persistent receiving and distributed integration checkpoint](../sprints/2026-09-26/checkpoint-2.md)
- [S-CHECKPOINT3-0926 — Linked Mini hosts, native prefix evidence and active hosted receiving](../sprints/2026-09-26/checkpoint-3.md)
- [S-CHECKPOINT4-0926 — Fresh complete fn exchange, physical interruption repairs and ongoing hosted integration](../sprints/2026-09-26/checkpoint-4.md)
- [S-CHECKPOINT5-0926 — Actual Hermes publication, native hard fence, faster observations and durable fn worker](../sprints/2026-09-26/checkpoint-5.md)
- [S-CHECKPOINT6-0926 — Real Hermes reconnect, committed missing reply, signed grain fn transport and reader-profile gap](../sprints/2026-09-26/checkpoint-6.md)
- [S-CHECKPOINT7-0926 — Actual SSH grain, provider custody, late-effect reporting and core hash repair](../sprints/2026-09-26/checkpoint-7.md)
- [S-CHECKPOINT8-0926 — Complete real grain fn exchange, hosted provider and crash recovery; resumed construction](../sprints/2026-09-26/checkpoint-8.md)
- [S-CHECKPOINT9-0926 — Delivered same-session workroom receipt, first durable fn POST, interrupt source and large-call pair](../sprints/2026-09-26/checkpoint-9.md)
- [S-CHECKPOINT10-0926 — Combined Mini builds, corrected native members, scoped recovery, workroom R2 fn publication and provider continuity](../sprints/2026-09-26/checkpoint-10.md)
- [S-CHECKPOINT11-0926 — Proved native hash speedup, exact-readback integration, hosted peer publications and recovered fn receive](../sprints/2026-09-26/checkpoint-11.md)
- [S-CHECKPOINT12-0926 — Combined native speed and adversaries, fresh law recovery, scoped hosted peer and receipt progress](../sprints/2026-09-26/checkpoint-12.md)
- [S-CHECKPOINT13-0926 — Exact hosted Hermes receipt, held fn B ACK/read completion and scoped next-source construction](../sprints/2026-09-26/checkpoint-13.md)
- [S-CHECKPOINT14-0926 — Signed cross-UID resources, fresh stale-root cleanup and operator-assisted workroom fn reply](../sprints/2026-09-26/checkpoint-14.md)
- [S-CHECKPOINT15-0926 — Dedicated-account Hermes shared workroom, read-only provider quote and linked typed A view](../sprints/2026-09-26/checkpoint-15.md)
- [S-CHECKPOINT16-0926 — Native provider settlement, own-R restart failure and continued kernel/hosting construction](../sprints/2026-09-26/checkpoint-16.md)
- [S-CHECKPOINT17-0926 — Native restart, terminal, sequential metering and resource birth progress](../sprints/2026-09-26/checkpoint-17.md)
- [S-SPK-CHECKPOINT65-0927 — Preserved native results and creation deadline failure](../sprints/2026-09-26/checkpoint-65.md)
- [S-SPK-CHECKPOINT66-0927 — User-requested wind-down and portable unfinished source](../sprints/2026-09-26/checkpoint-66.md)
- [S-DEMO-CONVERGENCE-RESUME — Resumed construction around complete demo journeys](../sprints/2026-09-26/demo-convergence.md)
- [S-SPK-CHECKPOINT67-0927 — Resident/controller batch adopted; ordinary birth bottleneck isolated](../sprints/2026-09-26/checkpoint-67.md)
- [S-SPK-CHECKPOINT67-0927 — Resident/controller batch adopted; ordinary birth bottleneck isolated](../sprints/2026-09-26/checkpoint-67.md)
- [S-SPK-CHECKPOINT68-0927 — Exact retained birth and cold reopen pass on repaired native Host](../sprints/2026-09-26/checkpoint-68.md)
- [S-SPK-CHECKPOINT68-0927 — Exact retained birth and cold reopen pass on repaired native Host](../sprints/2026-09-26/checkpoint-68.md)
- [S-SPK-CHECKPOINT69-0927 — Live retained birth and qualified coherent Host; base socket recovery pending](../sprints/2026-09-26/checkpoint-69.md)
- [S-SPK-CHECKPOINT70-0927 — Workroom recovered; detached app tool reserve refused; source integrations progressing](../sprints/2026-09-26/checkpoint-70.md)

**Write scope:** minidregg/Kernel/NativeHost*.lean; minidregg/Host/Main.lean; minidregg/native/resource-client/; minidregg/Compiler/Sp800185Cshake256Core.lean; minidregg/Kernel/NativeObservationController.lean; minidregg/scripts/build-native-host.sh

## W-JOINT-POST

**Check composition against the actual joint post-state**

Status: **done** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-20T00:00:01.954Z

Implement the general Mini transaction receiver over scalar and typed-content resources, with one exact joint post and current-policy admission for every incidence. Singleton mutations use the same receiver.

**Next:** Retain the source-matched native and Rust-client evidence as regression boundaries while building the persistent host and real agent lifecycle. This closure does not claim a deployed hosted platform.

**Done when:** Generic accepted composition preserves incidence outcomes, enforces resource laws and source-owned policy/postconditions on the actual joint result; hostile overlap/cross-field examples refuse, legitimate composition remains inhabited, and receiving constructors use the contract.

**Evidence so far:** General mixed scalar/content receiving and joint final-post policy enforcement are implemented and compiled. The complete native journey exercised an accepted atomic reservation/content change, accepted settlement/result publication, and an invalid second task leg that left the entire durable image unchanged. Current read authority was rechecked on direct submission.

[Task brief](../sprints/2026-09-19/cycle-1-result.md)

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-WIND-DOWN-0918 — User-requested wind-down, exact native passes and unfinished host, September 18](../sprints/2026-09-18/wind-down.md)
- [S-CYCLE-1-0919 — Authorized Mini construction cycle 1: initial convergence record](../sprints/2026-09-19/cycle-1.md)
- [S-CYCLE-1-INTEGRATION-0919 — Mini cycle 1 integration checkpoint: builds, native bottlenecks and pending final journeys](../sprints/2026-09-19/cycle-1-integration-checkpoint.md)
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)

**Write scope:** minidregg/Kernel/ResourceTransaction*.lean; minidregg/Kernel/DeclaredResourceController.lean and shared scalar projection

## W-M26-DESIGN

**Define the September 26 programmable nexus and its shared contracts**

Status: **active** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-27T02:38:13.221Z

Specify the coherent Mini resource/program and hosting contracts for the New World and complete hosted Nous Hermes experience. The construction home is settled; exact shared activity and economic operation remain open.

**Next:** Converge the SPK platform cycle: packaged apps provide shared human views and agent APIs under Mini authority; retain separate contributed-hosting and Solana obligations.

**Done when:** Accepted nexus operations and consequential design decisions; selected semantic and receiving-runtime paths; an explicit owned-node participation path and selected Solana/resource outcome; linked implementation obligations and evidence. Selecting a contract does not close implementation or deployment.

**Evidence so far:** Mini cycle1 completed the native programmable resource core and Rust client, with eleven-event task/content/authority acceptance and complete legacy/client recipes. Interactive latency, hosted Hermes and actual interruption, contributed-node hosting and a selected Solana operation remain unfinished.

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
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)
- [S-SPK-CYCLE-0927 — SPK application platform goal and grounded integration contract](../sprints/2026-09-26/spk-platform-cycle.md)

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

Status: **done** · Owner: Astra: root; Sol: cycle_build + cycle_client · Updated: 2026-09-20T00:00:01.955Z

Compile and exercise the source-owned Mini birth, joint transaction, policy, delegation, scoped observation and explicit revocation path through the public host and Rust client, with semantic replay and exact retry receipts.

**Next:** Retain the source-matched native and Rust-client evidence as regression boundaries while building the persistent host and real agent lifecycle. This closure does not claim a deployed hosted platform.

**Done when:** A real compiled host with operator-owned configuration accepts only source-authorized signed calls, preserves committed resources/receipts across restart and lost replies, and drives the same grant-preserving shared-resource journey through the programmable shell.

**Evidence so far:** The source-owned compiled host and Rust client passed complete native New World and legacy journeys plus mixed-resource and authority-client recipes. Exact retries recover original receipts across fresh processes and a real lost reply, preserving durable state and charges. Latest66d74dd has full581-source build closure plus focused exact-byte birth, eight-event replay/query/refusal and eleven-event accepted-policy-query/owner-lockout evidence. Whole-history latency and actual hosted agent process lifecycle remain separate implementation work.

[Task brief](../sprints/2026-09-19/cycle-1-result.md)

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
- [S-CLIENT-AUTHORITY-0919 — Completed Rust authority client journey on b119f86 host](../sprints/2026-09-19/cycle-1-evidence/final-client-authority/README.md)
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)
- [S-CHARGE-BUILD-0919 — Exact 66d74dd full umbrella and native charge-materialization build](../sprints/2026-09-19/cycle-1-evidence/charge-build/README.md)
- [S-CHARGE-FINAL-LOCKOUT-0919 — Latest host replays eleven events and enforces owner management lockout](../sprints/2026-09-19/cycle-1-evidence/charge-final-lockout/README.md)

**Write scope:** minidregg/Compiler/NativeHostCodec.lean; minidregg/Kernel/NativeHost*.lean; minidregg/Host/Main.lean and Host/Json.lean; minidregg/native/resource-client/; minidregg isolated native build and public journey harness

## W-POLICY-SOURCE

**Store initial policies and use one runtime profile**

Status: **done** · Owner: Astra: root; component implementation/review lanes completed · Updated: 2026-09-20T00:00:01.955Z

Immutable internal policy-source cells and a common field/compiler/request profile make resource creation, invocation and policy replacement agree.

**Next:** Retain the source-matched native and Rust-client evidence as regression boundaries while building the persistent host and real agent lifecycle. This closure does not claim a deployed hosted platform.

**Done when:** Policy source is created atomically and selected from the same durable directory; kind/domain/address mismatches refuse, and all consuming verbs share compatible source semantics.

**Evidence so far:** Shared source/runtime semantics for birth, joint invocation, typed content, source policy replacement, observation and per-capability revocation passed full source closure and native integration. The actual receiving path checks source kind/domain/address and current rules. Complete native acceptance confirms grant-preserving revision, current-law observation denial and deliberate management lockout.

[Task brief](../sprints/2026-09-19/cycle-1-result.md)

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
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)

**Write scope:** minidregg/Compiler/CanonicalRuntimeProfile.lean and coordinated policy/control source; minidregg/Compiler/NativeHostCodec.lean; minidregg shared umbrella imports

## W-PROGRAMMABLE-PATH

**Implement and exercise the canonical authored-program-to-resource path**

Status: **done** · Owner: Astra: root; Sol: cycle_build + cycle_client · Updated: 2026-09-20T00:00:01.955Z

Build and exercise the canonical Mini resource-programming path with installed laws, typed content, joint mutations and scoped observation, exposed through the source-owned host and Rust client.

**Next:** Retain the source-matched native and Rust-client evidence as regression boundaries while building the persistent host and real agent lifecycle. This closure does not claim a deployed hosted platform.

**Done when:** Author and install a rule under actual resource authority, invoke a permitted operation through the chosen shell/agent path, refuse a violating operation with correct state/outcome evidence, and recover accepted behavior/history through the chosen durable runtime. Complete all necessary core obligations, not merely a private demo.

**Evidence so far:** Source-owned JSON authoring, installed rules, scalar/typed-content resources, mixed transactions, scoped queries and retained signed calls are exercised through the real native host and Rust mini. The authority recipe roundtrips initial/installed policy JSON to exact canonical bytes, performs a permitted Bob operation, refuses violations, and recovers the historical receipt after revocation.

[Task brief](../sprints/2026-09-19/cycle-1-result.md)

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
- [S-CLIENT-AUTHORITY-0919 — Completed Rust authority client journey on b119f86 host](../sprints/2026-09-19/cycle-1-evidence/final-client-authority/README.md)
- [S-NEW-WORLD-0919 — Completed eleven-event native task/content/authority journey](../sprints/2026-09-19/cycle-1-evidence/final-new-world/README.md)
- [S-CYCLE-1-RESULT-0919 — Mini cycle 1 completed core result and exact remaining construction](../sprints/2026-09-19/cycle-1-result.md)

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

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-28T00:01:07.304Z

Compare provider bonds, resource payments and Clutch claim/settlement operations. Holder admission is useful existing material but does not alone perform an on-chain mutation. Specify the real asset/cluster and the DREGG receiver of the external result.

**Next:** Pin OpenRouter models, prices and operator custody; connect transactional DREGG service credits to existing Mini provider custody and a shared inference operation before adding the Discord client.

**Done when:** A selected user-visible economic function with exact mint/program/cluster, custody and release policy where applicable, external evidence acceptance and resource-result binding; required source/consumer changes and acceptance checks identified, then exercised at an explicitly authorized deployment scope.

**Evidence so far:** Ember selected an additional DREGG-only inference offering through existing payment infrastructure and a Discord interface. Source audit finds a selected DREGG signature watcher and reusable provider code, but bot SQLite credit/dedup writes are not transactional. No paid request or transaction performed; provider bonds remain a separate obligation.

**Enables:**

- E-SOLANA — Solana-facing asset and resource participation
- E-CLUTCH — Clutch claim, market and settlement resources
- E-PROVIDERS — Contributed hosting and optimistic provider accountability

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-PAYMENT-INFERENCE-0927 — DREGG-only inference direction and payment/provider source audit](../research/payment-inference-2026-09-27.md)

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

## W-SPK-PLATFORM

**Run shared SPK applications through Mini, browsers, agents and fn**

Status: **active** · Owner: Astra: root; Sol: client_session, agent_api_host, runtime_review, fn_mini_review, fn_contracts · Updated: 2026-09-28T00:05:41.041Z

Integrate real third-party packaged app execution and persistent state with Mini lifecycle/current grants, hosted Hermes, direct commands, and selected version publication over semi-untrusted fn.

**Next:** Recover app bootstrap with separately authorized tool attach, fresh read/reserve and retained refused attempt; finish actual app admission then INSTALL/START, shared human/agent use and fn receiving.

**Done when:** A coherent deployed and tinkerable platform satisfies all listed acceptance journeys at pinned source, with core latency measured/addressed, persistent hosting, scoped adversarial/recovery evidence, and portable operator/contributor handoff. A substitute notes body, parser-only compatibility, or independent fixture greens do not close this item.

**Evidence so far:** Retained workroom recovery passed eight signed views and six parent delegations; next app reserve explicitly refused with tool7902 detached, Store unchanged. Mixed-route config committed/tested; accepted-grant inspector passed narrow Lean; real local model qualification and source integration ongoing.

[Task brief](../sprints/2026-09-26/spk-platform-cycle.md)

**Enables:**

- E-WORLD — Programmable social resource world
- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-SPK-CYCLE-0927 — SPK application platform goal and grounded integration contract](../sprints/2026-09-26/spk-platform-cycle.md)
- [S-SPK-GROUNDING1-0927 — Actual Simple Todos package inspection and official-schema manifest repair](../sprints/2026-09-26/spk-grounding-01.md)
- [S-SPK-CHECKPOINT18-0927 — SPK package, RPC, Mini lifecycle and hosted birth checkpoint](../sprints/2026-09-26/checkpoint-18.md)
- [S-SPK-CHECKPOINT19-0927 — Real Simple Todos create/wake and Mini application-contract checkpoint](../sprints/2026-09-26/checkpoint-19.md)
- [S-PARALLEL-JOURNEYS-0927 — Parallel platform journeys and independent app-issued authority requirement](../sprints/2026-09-26/parallel-journeys.md)
- [S-SPK-CHECKPOINT20-0927 — Parallel journeys and checked receiving core checkpoint](../sprints/2026-09-26/checkpoint-20.md)
- [S-SPK-CHECKPOINT21-0927 — Real GitWeb work and connected receiving paths](../sprints/2026-09-26/checkpoint-21.md)
- [S-SPK-CHECKPOINT22-0927 — Native shared application and session foundation](../sprints/2026-09-26/checkpoint-22.md)
- [S-SPK-CHECKPOINT23-0927 — Native routes and connected journey integration boundaries](../sprints/2026-09-26/checkpoint-23.md)
- [S-SPK-CHECKPOINT24-0927 — Hosted recovery, publication custody and current integration frontier](../sprints/2026-09-26/checkpoint-24.md)
- [S-SPK-CHECKPOINT25-0927 — Current authoring, exact native build and verified-history integration](../sprints/2026-09-26/checkpoint-25.md)
- [S-SPK-CHECKPOINT26-0927 — Native selected receiving and parallel shared application integration](../sprints/2026-09-26/checkpoint-26.md)
- [S-SPK-CHECKPOINT27-0927 — Executable admitted-history selection and private participant entry](../sprints/2026-09-26/checkpoint-27.md)
- [S-SPK-CHECKPOINT28-0927 — Physical root repairs and complete sharing approval](../sprints/2026-09-26/checkpoint-28.md)
- [S-SPK-CHECKPOINT29-0927 — Native current births, private browser entry and operator share custody](../sprints/2026-09-26/checkpoint-29.md)
- [S-SPK-CHECKPOINT30-0927 — Dispatch and lifecycle source integration, provider interruption and native convergence](../sprints/2026-09-26/checkpoint-30.md)
- [S-FN-CONSUMER-CONTINUITY-0927 — Unified empty and selected fn consumer progress requirement](../sprints/2026-09-26/fn-consumer-progress-continuity.md)
- [S-SPK-CHECKPOINT31-0927 — Package-bound lifecycle and one-shot physical dispatch custody](../sprints/2026-09-26/checkpoint-31.md)
- [S-SPK-CHECKPOINT32-0927 — Hosted creation evidence, ticket repair and measured hashing hotspot](../sprints/2026-09-26/checkpoint-32.md)
- [S-SPK-CHECKPOINT33-0927 — Atomic sharing source and fixed native cutoff](../sprints/2026-09-26/checkpoint-33.md)
- [S-SPK-CHECKPOINT34-0927 — Native compile gate and recovery findings](../sprints/2026-09-26/checkpoint-34.md)
- [S-SPK-CHECKPOINT35-0927 — Qualified native host and dispatch recovery](../sprints/2026-09-26/checkpoint-35.md)
- [S-SPK-CHECKPOINT36-0927 — Receiving closure and physical integration gaps](../sprints/2026-09-26/checkpoint-36.md)
- [S-SPK-CHECKPOINT37-0927 — Qualified completion Host and private authoring routes](../sprints/2026-09-26/checkpoint-37.md)
- [S-SPK-CHECKPOINT38-0927 — Operator Host qualified and sharing reaches admission](../sprints/2026-09-26/checkpoint-38.md)
- [S-SPK-CHECKPOINT39-0927 — Lifecycle native build and grain-backed sharing diagnosis](../sprints/2026-09-26/checkpoint-39.md)
- [S-SPK-CHECKPOINT40-0927 — Hosted recovery and core integration findings](../sprints/2026-09-26/checkpoint-40.md)
- [S-SPK-CHECKPOINT41-0927 — Coherent native integration build selected](../sprints/2026-09-26/checkpoint-41.md)
- [S-SPK-CHECKPOINT42-0927 — Shared-app recovery and first-launch findings](../sprints/2026-09-26/checkpoint-42.md)
- [S-SPK-CHECKPOINT43-0927 — Committed resident/controller custody and native proof repair](../sprints/2026-09-26/checkpoint-43.md)
- [S-SPK-CHECKPOINT44-0927 — Prequeue recovery, participant separation and persistent grant contract](../sprints/2026-09-26/checkpoint-44.md)
- [S-SPK-CHECKPOINT45-0927 — Offline signed-package launch qualification and integration continuation](../sprints/2026-09-26/checkpoint-45.md)
- [S-SPK-CHECKPOINT46-0927 — Compiled source contracts and launch authorization review](../sprints/2026-09-26/checkpoint-46.md)
- [S-SPK-CHECKPOINT47-0927 — Persistent volume custody and grant admission components](../sprints/2026-09-26/checkpoint-47.md)
- [S-SPK-CHECKPOINT48-0927 — Receiving routes and guarded native build recovery](../sprints/2026-09-26/checkpoint-48.md)
- [S-SPK-CHECKPOINT49-0927 — Launch lifecycle lower source and fresh participant bootstrap](../sprints/2026-09-26/checkpoint-49.md)
- [S-SPK-CHECKPOINT50-0927 — Qualified native Host and reviewed launch/reconnect admission](../sprints/2026-09-26/checkpoint-50.md)
- [S-SPK-CHECKPOINT51-0927 — Foreground shell source and reviewed lifecycle/payer binding gaps](../sprints/2026-09-26/checkpoint-51.md)
- [S-SPK-CHECKPOINT52-0927 — Typed lifecycle history, exact receivers and physical BEGIN consumer](../sprints/2026-09-26/checkpoint-52.md)
- [S-SPK-CHECKPOINT53-0927 — Native descriptor Host and physical claim handoff review](../sprints/2026-09-26/checkpoint-53.md)
- [S-SPK-CHECKPOINT54-0927 — Native package qualification and CAS-winner lifecycle routing](../sprints/2026-09-26/checkpoint-54.md)
- [S-SPK-CHECKPOINT55-0927 — Lifecycle completion routes and cross-layer integration defects](../sprints/2026-09-26/checkpoint-55.md)
- [S-SPK-CHECKPOINT56-0927 — Lifetime client convergence and pinned Persvati build](../sprints/2026-09-26/checkpoint-56.md)
- [S-SPK-CHECKPOINT57-0927 — Completed combined Host build and native integration repair](../sprints/2026-09-26/checkpoint-57.md)
- [S-SPK-CHECKPOINT58-0927 — Live exact successor build and concrete GitWeb base Store](../sprints/2026-09-26/checkpoint-58.md)
- [S-SPK-CHECKPOINT59-0927 — Callable source-bound INSTALL and repaired concrete app fixture](../sprints/2026-09-26/checkpoint-59.md)
- [S-SPK-CHECKPOINT60-0927 — Deployed birth profile repair and native dispatch convergence](../sprints/2026-09-26/checkpoint-60.md)
- [S-SPK-CHECKPOINT61-0927 — Measured warm reads and same-Store integration work](../sprints/2026-09-26/checkpoint-61.md)
- [S-SPK-CHECKPOINT62-0927 — Callable START, fresh STOP custody and integration repairs](../sprints/2026-09-26/checkpoint-62.md)
- [S-SPK-CHECKPOINT63-0927 — Native binaries and source-derived delegation](../sprints/2026-09-26/checkpoint-63.md)
- [S-SPK-CHECKPOINT64-0927 — Native sharing accepted and paid-inspection successor](../sprints/2026-09-26/checkpoint-64.md)
- [S-SPK-CHECKPOINT65-0927 — Preserved native results and creation deadline failure](../sprints/2026-09-26/checkpoint-65.md)
- [S-SPK-CHECKPOINT66-0927 — User-requested wind-down and portable unfinished source](../sprints/2026-09-26/checkpoint-66.md)
- [S-DEMO-CONVERGENCE-RESUME — Resumed construction around complete demo journeys](../sprints/2026-09-26/demo-convergence.md)
- [S-SPK-CHECKPOINT67-0927 — Resident/controller batch adopted; ordinary birth bottleneck isolated](../sprints/2026-09-26/checkpoint-67.md)
- [S-SPK-CHECKPOINT68-0927 — Exact retained birth and cold reopen pass on repaired native Host](../sprints/2026-09-26/checkpoint-68.md)
- [S-SPK-CHECKPOINT69-0927 — Live retained birth and qualified coherent Host; base socket recovery pending](../sprints/2026-09-26/checkpoint-69.md)
- [S-SPK-CHECKPOINT70-0927 — Workroom recovered; detached app tool reserve refused; source integrations progressing](../sprints/2026-09-26/checkpoint-70.md)

**Write scope:** minidregg/Kernel/ApplicationLifecycle* and ApplicationSpkLaunchDescriptor.lean (mini_app_contract); minidregg/native/spk-host resident/RPC and dedicated physical evidence (agent_api_host); minidregg/native/spk-host agent custody/server (agent_api_host); minidregg/native/grain-runtime and dedicated controller evidence (runtime_review); isolated source-matched native Host builds and explicit proof repairs (build_native); minidregg/Kernel/Fn* receiving and Host/FnConsumerFrontierPlan.lean (fn_mini_review); persistent agent-route authorization design (runtime_review); coordinated Host/Main.lean and NativeHostReplay.lean hooks; root owns integration order and Git; minidregg/scripts/spk-platform source-authored fixture enrollment/birth continuations (spk_compatibility); minidregg/Host/ApplicationLifecycleLaunchAuthoring*.lean and coordinated Main ops66–71 after lower API freeze (fn_mini_review); minidregg/Kernel/NativeHostContext.lean canonical image-boundary byte reuse and general equivalence proof (client_session); actual Replay consumers coordinated with mini_app_contract

**Acceptance:**

- Two distinct participants use the same real third-party SPK app through browser and hosted real-model Hermes API access under Mini grants.
- Direct commands discover and operate the same resources; delegation/revocation and session fences are enforced without stopping another user’s shared app.
- Actual durable app state survives restart; uncertain requests are reconciled without blind repeat.
- Selected app or data versions travel through fn with explicit publication and separate receiver install/import authority, without private-prefix disclosure.
