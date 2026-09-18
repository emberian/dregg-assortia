# Work records

> Generated from `graph.jsonld`. [Current board](../CURRENT.md).

## W-ANDROID-CONTRACT

**Define resource-host lifecycle ownership and its kernel contract**

Status: **active** · Owner: Astra: root with ember; contributor assignment pending · Updated: 2026-09-18T02:12:02-04:00

Cloud/resource-host lifecycle is the selected area to offer Wisper. This stable work ID retains the original Android example; exact runtime/export contract is still open.

**Next:** Agree the first runtime/export and executable shell consumer with ember and Wisper, then freeze owned core delivery and crash/restart acceptance.

**Done when:** A contributor can scaffold a real product surface from a concrete brief and agreed contracts, with executable receiving interfaces or explicitly owned upstream delivery, test scenarios and no need to infer core architecture from chat.

**Evidence so far:** Ember selected cloud/resource-host lifecycle. Source-backed brief and concrete native-host export proposal are preserved; exact first runtime/profile and owned upstream exports remain open. No contributor contact or assignment.

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

**Write scope:** DreggNet/control provider/server/supervisor and gateway lifecycle; Selected native host extraction/export, jointly reserved with core; Selected packaging and integration harness

**Acceptance:**

- Fault-injected provision/settlement/publication crash intervals reconcile one backend and one charge.
- Actual native authorized operation and exact retained state/result survive restart and response-loss retry.
- Owner isolation, stop/wake, incompatible/corrupt storage refusal and acknowledged event resume are exercised.

## W-GRAPH-NAVIGATION

**Follow graph relationships in both directions**

Status: **done** · Owner: Astra: core_durable_receiver · Updated: 2026-09-18T01:45:00-04:00

Extend the existing graph browser so readers can move from work to purpose, dependencies and evidence, and discover what points back.

**Next:** Use and maintain the tested hub tools during project handoffs; contributor/runtime selection continues in W-ANDROID-CONTRACT.

**Done when:** Existing graph relationships are traversable deterministically and safely in both directions; broken links and cycles are handled explicitly; default short output remains usable.

**Evidence so far:** 12 focused tests pass, including real graph traversal and a standalone script-plus-graph checkout.

[Task brief](../internal/tooling-candidates-2026-09-18.md)

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-HUB-TOOLS-0145 — Graph navigation/source-impact tooling and captured tests](../sprints/2026-09-18/hub-tools-0145.md)

**Write scope:** dregg-assortia/browse_graph.py; dregg-assortia/tests/test_browse_graph.py

**Acceptance:**

- Python standard-library tests cover outward/inward traversal, depth2, a cycle and a dangling target.
- The checked-in W-RESOURCE-BIRTH record reaches its actual related work/evidence in the CLI.
- No graph record or sibling repository is changed; the tool runs from an assortia-only clone.

## W-HUB-LIVE

**Make assortia usable for ongoing work and new contributors**

Status: **done** · Owner: Astra: root · Updated: 2026-09-18T01:45:00-04:00

Graph-backed work ownership, concrete briefs, generated current views and an explicit update routine replace an orientation-only entry point.

**Next:** Use and maintain the tested hub tools during project handoffs; contributor/runtime selection continues in W-ANDROID-CONTRACT.

**Done when:** A clean assortia clone exposes current work, ownership and a concrete feature-handoff investigation without sibling repositories; graph/status checks and generated-view checks pass.

**Evidence so far:** Graph-backed ownership/board, portable tools and substantial source-backed contributor proposal are present. Runtime/feature selection remains explicitly active.

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-HUB-TOOLS-0145 — Graph navigation/source-impact tooling and captured tests](../sprints/2026-09-18/hub-tools-0145.md)

## W-AUTHORITY-NATIVE

**Bind native use to committed keys and complete authority**

Status: **active** · Owner: Astra: resume_authority + resume_signatures · Updated: 2026-09-18T03:14:26-04:00

Persist exact signing keys/epochs; accept actual configured native verification of the exact request and capability against the complete same-snapshot authority.

**Next:** Finish joined delegation/receiving checks and refresh generated Rust consumers and the root integration gate.

**Done when:** Actual installed verification plus complete committed authority checks feed accepted source operations; stale/altered/revoked credentials cannot authorize them.

**Evidence so far:** Real Ed25519/SQLite signature probe passes the17-field revision migration, legacy and tamper refusals. Physical authority and source admission modules pass.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

## W-AUTHORIZED-DELEGATION

**Give a friend a narrower usable right**

Status: **active** · Owner: Astra: resume_journey · Updated: 2026-09-18T03:14:26-04:00

Add an explicit authorized subject-to-subject delegation edge without weakening strict holder-narrowing or inventing bearer custody.

**Next:** Run actual born-resource Alice-to-Bob delegation and recipient invocation with hostile scope/identity cases.

**Done when:** Owner delegates a bounded right; friend can use that right, cannot exceed it or replace policy, and revocation/current epochs remain enforced.

**Evidence so far:** Controller and receiver compile; mandatory exact parent authorization, actual whole post, stored lineage and final authority-byte/frame laws pass their scoped checks.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

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

Status: **active** · Owner: Astra: root + kernel_carrier + localfirst · Updated: 2026-09-18T01:30:00-04:00

Implement durable refusal propagation and exact ordered physical history in breadstuffs, while joining resource birth, owner authority and charge in the canonical shared core. Repeated body updates still require the selected accepted operation and receiving cutover.

**Next:** Complete ordered factory/history repair and connect document edits to accepted kernel operations instead of setup writes.

**Done when:** Repeated authorized saves, rejection without committed mutation, crash/reopen at each ordered boundary, and matching body/receipt history through the actual selected consumer. Physical setup journaling alone does not close kernel authorization.

**Evidence so far:** The earlier intermediate-root failures are fixed: cell/turn/World24/24 pass. Kernel-authorized document saves remain a distinct receiving task.

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

## W-EFFECT-ADMISSION

**Make full request and actual-pre binding mandatory for generic effects**

Status: **active** · Owner: Astra: resume_journey + resume_authority · Updated: 2026-09-18T03:14:26-04:00

Replace optional binding adapters with a source-derived family request and exact pre requirement in AcceptedCellEffect, migrating concrete families and consumers.

**Next:** Use the current exact-parent/source-admission laws in the joined native receiving path and root integration.

**Done when:** All receiving constructors use the strengthened base token; target/verb/args/nonce/pre relabeling refuses, honest effects remain inhabited, and the integrated tree checks.

**Evidence so far:** Eight source modules and28 exact axiom pins pass. The shared capability helper now proves the exact input-parent identity.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

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

Status: **active** · Owner: Astra: resume_runtime · Updated: 2026-09-18T02:51:31-04:00

World deployment currently mutates volatile registries; historical paths either omit factories or preload the present registry into the past. Persist ordered descriptor/VK evidence and replay the actual executor deployment at that boundary.

**Next:** Run the affected history regression set against the exact recorded current source and preserve completion evidence.

**Done when:** Actual factory deployment, birth/mutation and recovery use the same ordered descriptor/VK evidence; no historical prefix sees a later factory; conflicting deployment and persistence failures leave committed state unchanged; unsupported old images refuse without changing evidence.

**Evidence so far:** All five targeted factory chronology tests now ran and passed with actual native Lean in the combined9-test suite. Current-source affected history regressions remain queued.

**Enables:**

- E-DOC — Desktop document authoring
- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)

## W-GRANT-REVISION

**Keep grants valid across policy source revisions**

Status: **active** · Owner: Astra: resume_install + resume_authority; root integration · Updated: 2026-09-18T03:14:26-04:00

Separate immutable policy-source revision from grant revocation generation across the exact signed request, authority representation, compiled/source policies and every receiving consumer.

**Next:** Run repeated native installs and retained-grant use, then expose explicitly authorized generation revocation through the same core. Preserve deliberate management lockout.

**Done when:** After two admitted rule replacements, previously issued owner/control and delegated grants remain usable exactly when their scope and new rules authorize the new request; stale revisions refuse, explicit generation revocation invalidates prior grants, and restart/retry preserves exact state and receipts. Resource policy can deliberately refuse further management, with no implicit owner bypass.

**Evidence so far:** Foundation, physical codecs, signature, source registry and installer source checks pass at the new schema. Native integration is now running. No owner repair bypass.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

## W-HERMES-STARTUP

**Make actual Hermes/SDK startup avoid unused Lean initialization**

Status: **active** · Owner: Astra: resume_runtime + resume_init_hotspot · Updated: 2026-09-18T03:14:26-04:00

SDK route discovery is lazy while actual cryptographic calls retain real Lean initialization.

**Next:** Complete fresh runtime/PQ/Hermes checks and wide-credential ABI repair with actual accepted cases.

**Done when:** The same operations and refusal/publication checks pass through actual receiving code without eager unused-core initialization; real PQ first-use remains checked.

**Evidence so far:** Original full lifecycle passes at~187–189s; game fixture separation retains both proof suites. Narrow executor actual initialization~41ms. Existing differential corpus covers refusal paths; accepted cases and width repair are in progress.

**Enables:**

- E-HERMES — External Hermes integration

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

## W-JOINT-POST

**Check composition against the actual joint post-state**

Status: **active** · Owner: Astra: kernel_carrier + program_install · Updated: 2026-09-18T00:45:00-04:00

Actual-joint resource accounting and accepted field preservation now reject minted overlap and lost fees in targeted Lean witnesses. Source-policy validity on the joint post, including cross-field dependencies, is the next compulsory composition closure.

**Next:** Exercise concrete factory/invocation policies against the same actual final tuple.

**Done when:** Generic accepted composition preserves incidence outcomes, enforces resource laws and source-owned policy/postconditions on the actual joint result; hostile overlap/cross-field examples refuse, legitimate composition remains inhabited, and receiving constructors use the contract.

**Evidence so far:** Mandatory general postcondition API and constructive cross-field refusal witnesses passed; concrete new consumers still need their joined checks.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-M26-DESIGN

**Define the September 26 programmable nexus and its shared contracts**

Status: **active** · Owner: ember + Astra · Updated: 2026-09-18T00:45:00-04:00

Active design and implementation planning for the September 26 mixed programmable nexus: canonical resource/authority/history, user-authored rules and shell/Hermes invocation, participant hosting and meaningful economic operations. Close required core/compiler/proof/runtime gaps instead of routing around them.

**Next:** Review the running create/install/invoke/share/reopen journey; decide the public economic operation and release promises.

**Done when:** Accepted nexus operations and consequential design decisions; selected semantic and receiving-runtime paths; an explicit owned-node participation path and selected Solana/resource outcome; linked implementation obligations and evidence. Selecting a contract does not close implementation or deployment.

**Enables:**

- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

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

Status: **active** · Owner: Astra: resume_host + resume_foundations + resume_genesis + resume_admission + resume_birth_review · Updated: 2026-09-18T03:14:26-04:00

Compile the source-owned Mini birth, rule installation, invocation and delegation path into an executable shell/stdio interface with exact signed calls, committed-history clock and replay receipts.

**Next:** Implement per-resource authenticated observation/preparation, Book support enforcement and semantic journal verification; link host and run public CLI acceptance.

**Done when:** A real compiled host with operator-owned configuration accepts only source-authorized signed calls, preserves committed resources/receipts across restart and lost replies, and drives the same grant-preserving shared-resource journey through the programmable shell.

**Evidence so far:** Concrete native profile compiles. Independent review found unsigned preparation balance oracle and missing historical semantic revalidation; fixes are assigned, public prepare closed. Host binary and CLI journey remain unverified.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

## W-POLICY-SOURCE

**Store initial policies and use one runtime profile**

Status: **active** · Owner: Astra: resume_install + resume_journey · Updated: 2026-09-18T03:14:26-04:00

Immutable internal policy-source cells and a common field/compiler/request profile make resource creation, invocation and policy replacement agree.

**Next:** Run current native repeated installation and the joined born-resource journey.

**Done when:** Policy source is created atomically and selected from the same durable directory; kind/domain/address mismatches refuse, and all consuming verbs share compatible source semantics.

**Evidence so far:** Current source revision is independent of exact grant generation; native installer and birth source closure compile.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

## W-PROGRAMMABLE-PATH

**Implement and exercise the canonical authored-program-to-resource path**

Status: **active** · Owner: Astra: resume_journey + resume_host + resume_genesis · Updated: 2026-09-18T03:14:26-04:00

Select the canonical rule/program representation and actual authority projection, then implement needed compiler/native/proof/durable support and shell/Hermes consumers. Existing guards are retired only by replacing their missing guarantees. Active source investigation is recorded in sprints/2026-09-17.md.

**Next:** Complete the native joined journey, then drive it through authenticated preparation and the public compiled host.

**Done when:** Author and install a rule under actual resource authority, invoke a permitted operation through the chosen shell/agent path, refuse a violating operation with correct state/outcome evidence, and recover accepted behavior/history through the chosen durable runtime. Complete all necessary core obligations, not merely a private demo.

**Evidence so far:** Birth, invocation, installer and delegation receiving modules compile against current semantics; actual joined probe is next.

**Enables:**

- E-WORLD — Programmable social resource world
- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-PROGRAMMING-REVIEW — Parent-reviewed programming and shell investigation](../research/programming.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-ACCOUNT-HANDOFF-0918 — September18 account handoff: native born-owner journey and next integration wave](../sprints/2026-09-18/account-handoff.md)
- [S-RESUMED-0250 — Resumed native runtime and pinned publication checks, September18](../sprints/2026-09-18/resumed-0250.md)
- [S-RESUMED-0311 — Revision migration checks and host review, September18 03:11](../sprints/2026-09-18/resumed-0311.md)

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

Status: **done** · Owner: Astra: core_resource_pages · Updated: 2026-09-18T01:45:00-04:00

Report which claims/work items need reinspection when source bytes change, with repository paths configurable on a contributor machine.

**Next:** Use and maintain the tested hub tools during project handoffs; contributor/runtime selection continues in W-ANDROID-CONTRACT.

**Done when:** The checker identifies unavailable repositories separately from changed files, explains affected records without rewriting their historical hashes, and runs against temporary fixture repositories.

**Evidence so far:** 23 focused tests,41 total hub tests and actual CLI fixtures pass; unavailable evidence is unknown, old hashes remain unchanged, and contextual reference paths are explicit.

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
- [S-IMPLEMENTATION-0130 — Durable native invocation and repaired runtime history, September 18 01:30](../sprints/2026-09-18/checkpoint-0130.md)
- [S-HUB-TOOLS-0145 — Graph navigation/source-impact tooling and captured tests](../sprints/2026-09-18/hub-tools-0145.md)
