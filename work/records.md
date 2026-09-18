# Work records

> Generated from `graph.jsonld`. [Current board](../CURRENT.md).

## W-ANDROID-CONTRACT

**Define a substantial Android product work package**

Status: **active** · Owner: Astra: root + mobile inventory + runtime review · Updated: 2026-09-18T00:51:00-04:00

Trace existing mobile work and actual node/receiver APIs, then specify app responsibilities, embedded runtime contract, system/UI integrations and acceptance scenarios for an outside contributor. Android is the concrete example supplied by ember, not yet a settled release commitment. Ember also suggested DreggNet/cloud for the experienced platform contributor; compare the shared native-host boundary rather than presuming Android is selected.

**Next:** Compare Android embedding and cloud lifecycle ownership against the actual node/receiver source; publish a substantial feature proposal.

**Done when:** A contributor can scaffold a real product surface from a concrete brief and agreed contracts, with executable receiving interfaces or explicitly owned upstream delivery, test scenarios and no need to infer core architecture from chat.

**Enables:**

- E-WORLD — Programmable social resource world
- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-GRAPH-NAVIGATION

**Follow graph relationships in both directions**

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-18T00:51:00-04:00

Extend the existing graph browser so readers can move from work to purpose, dependencies and evidence, and discover what points back.

**Next:** Astra handles this internal tooling work; it is not an external contributor assignment.

**Done when:** Existing graph relationships are traversable deterministically and safely in both directions; broken links and cycles are handled explicitly; default short output remains usable.

[Task brief](../internal/tooling-candidates-2026-09-18.md)

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

**Write scope:** dregg-assortia/browse_graph.py; dregg-assortia/tests/test_browse_graph.py

**Acceptance:**

- Python standard-library tests cover outward/inward traversal, depth2, a cycle and a dangling target.
- The checked-in W-RESOURCE-BIRTH record reaches its actual related work/evidence in the CLI.
- No graph record or sibling repository is changed; the tool runs from an assortia-only clone.

## W-HUB-LIVE

**Make assortia usable for ongoing work and new contributors**

Status: **active** · Owner: Astra: root · Updated: 2026-09-18T00:45:00-04:00

Graph-backed work ownership, concrete briefs, generated current views and an explicit update routine replace an orientation-only entry point.

**Next:** Publish the current graph-backed board and substantive contributor feature investigation.

**Done when:** A clean assortia clone exposes current work, ownership and a concrete feature-handoff investigation without sibling repositories; graph/status checks and generated-view checks pass.

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-AUTHORITY-NATIVE

**Bind native use to committed keys and complete authority**

Status: **active** · Owner: Astra: authority_pages + durable_receiver + effect_admission · Updated: 2026-09-18T00:45:00-04:00

Persist exact signing keys/epochs; accept actual configured native verification of the exact request and capability against the complete same-snapshot authority.

**Next:** Refresh affected authority consumers, then exercise real signed acceptance and wrong-key/request/epoch refusals.

**Done when:** Actual installed verification plus complete committed authority checks feed accepted source operations; stale/altered/revoked credentials cannot authorize them.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-AUTHORIZED-DELEGATION

**Give a friend a narrower usable right**

Status: **active** · Owner: Astra: durable_callers + effect_admission · Updated: 2026-09-18T00:45:00-04:00

Add an explicit authorized subject-to-subject delegation edge without weakening strict holder-narrowing or inventing bearer custody.

**Next:** Complete the source-owned delegation/lineage contract, then implement its receiver and real two-subject probe.

**Done when:** Owner delegates a bounded right; friend can use that right, cannot exceed it or replace policy, and revocation/current epochs remain enforced.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-CANONICAL-CONSUMER

**Trace one canonical typed event through its real compiler and consumer**

Status: **active** · Owner: Astra: kernel_carrier · Updated: 2026-09-18T00:45:00-04:00

Connect the canonical source request and accepted joint state to actual artifact and native consumers. Keep mandatory request/capability-use and policy-change verb tags consistent.

**Next:** Finish regenerated authorization artifacts, then prove actual page-write reflection used by invocation.

**Done when:** One explicit event/schema/codec/acceptance/storage path, with each existing join or missing obligation sourced. No broad rewrite before the path is understood.

**Evidence so far:** Authorization base3/3 and artifact closure27/27 passed; regenerated outputs byte-compared and pushed in c41d77e. Page reflection and actual native consumers continue.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-COMPILER — Compiler's joint-turn artifact projection

**Context dependencies:**

- C-KERNEL-COMPILER — The joint-turn artifact projection still consumes DeclaredHyperedge

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

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

Status: **active** · Owner: Astra: localfirst · Updated: 2026-09-18T00:45:00-04:00

Compact commands use actual page execution, complete old authority, stored policy and accepted final-state evidence.

**Next:** Finish page-write reflection, native per-incidence admission and durable acknowledgment.

**Done when:** An owner can invoke an authored operation, invalid requests refuse unchanged, and accepted data/receipt survive reopen.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Waiting for:**

- W-POLICY-SOURCE — Store initial policies and use one runtime profile
- W-AUTHORITY-NATIVE — Bind native use to committed keys and complete authority

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-DOC-PERSIST

**Establish the chosen document storage/turn contract**

Status: **active** · Owner: Astra: resource_history · Updated: 2026-09-18T00:45:00-04:00

Implement durable refusal propagation and exact ordered physical history in breadstuffs, while joining resource birth, owner authority and charge in the canonical shared core. Repeated body updates still require the selected accepted operation and receiving cutover.

**Next:** Repair intermediate-root disagreement across reopen, then rerun the exact failed World/history checks.

**Done when:** Repeated authorized saves, rejection without committed mutation, crash/reopen at each ordered boundary, and matching body/receipt history through the actual selected consumer. Physical setup journaling alone does not close kernel authorization.

**Evidence so far:** World/history attempt2:14 passed,2 failed,2 not run. Final-state equality does not close every-boundary recovery.

**Enables:**

- E-DOC — Desktop document authoring
- E-COORD — Coordination and replicated computation

**Context dependencies:**

- C-DOC-DURABLE — Current desktop heap persistence refuses after a durable cell has participated in a turn

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-EFFECT-ADMISSION

**Make full request and actual-pre binding mandatory for generic effects**

Status: **active** · Owner: Astra: core_effect_admission · Updated: 2026-09-18T00:45:00-04:00

Replace optional binding adapters with a source-derived family request and exact pre requirement in AcceptedCellEffect, migrating concrete families and consumers.

**Next:** Finish native registry capability-use/lineage integration after the fresh authority closure.

**Done when:** All receiving constructors use the strengthened base token; target/verb/args/nonce/pre relabeling refuses, honest effects remain inhabited, and the integrated tree checks.

**Evidence so far:** Mandatory full request, pre-state and joint postconditions are published; current capability-use and installPolicy base checks passed.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-EMBEDDED-CANDIDATE

**Keep embedded candidates atomic through durable publication**

Status: **active** · Owner: Astra: root + resource_history · Updated: 2026-09-18T00:45:00-04:00

SDK/World align with the current node rejection policy: no retained fee, nonce, executor side-state or observer notification from a refused candidate. A possibly committed storage failure still requires authoritative reopen.

**Next:** Finish current World batch validation and remeasure the SDK/Hermes path after lazy initialization.

**Done when:** Paid late refusal leaves exact prior state; storage refusal restores executor side-state; pending/unwound candidates cannot reenter; observer runs once only after acceptance; next success replays and reopens correctly.

**Evidence so far:** Four actual SDK candidate rollback/publication tests passed; World intermediate-history failures remain separate.

**Enables:**

- E-HERMES — External Hermes integration
- E-DOC — Desktop document authoring

**Evidence / provenance:**

- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-HERMES-STARTUP

**Make actual Hermes/SDK startup avoid unused Lean initialization**

Status: **active** · Owner: Astra: resource_history + root · Updated: 2026-09-18T00:45:00-04:00

SDK route discovery is lazy while actual cryptographic calls retain real Lean initialization.

**Next:** Repair first-use archive initialization at the actual Lean gate without changing its semantics.

**Done when:** The same operations and refusal/publication checks pass through actual receiving code without eager unused-core initialization; real PQ first-use remains checked.

**Evidence so far:** SDK4/4 passed in0.026–0.047s; exact js-agent Hermes1/1 passed in191.097s. Construction is<10ms; first verified admission still initializes the archive.

**Enables:**

- E-HERMES — External Hermes integration

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

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

Status: **active** · Owner: Astra: core_durable_receiver + proof_integrity · Updated: 2026-09-18T00:45:00-04:00

The existing Lean executor now crosses exact-byte SQLite CAS with crash/retry/concurrency checks; full source-authorized resource birth and product receiving joins remain active.

**Next:** Join source-authorized operations and reconcile exact signed retries from retained journal entries.

**Done when:** A controller-bound multi-cell operation crosses real Lean decoding/admission/execute and physical CAS; stale/conflicting/malformed requests refuse, exact retry replays, and reopen preserves exact bytes and history.

**Evidence so far:** SQLite CAS/reopen/concurrency component checks passed; strict native Ed25519 helper exercised. Complete signed journey remains active.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-POLICY-SOURCE

**Store initial policies and use one runtime profile**

Status: **active** · Owner: Astra: resource_pages + shell_hermes + program_install · Updated: 2026-09-18T00:45:00-04:00

Immutable internal policy-source cells and a common field/compiler/request profile make resource creation, invocation and policy replacement agree.

**Next:** Finish source-cell/profile closure and install/birth/invoke consumers.

**Done when:** Policy source is created atomically and selected from the same durable directory; kind/domain/address mismatches refuse, and all consuming verbs share compatible source semantics.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

## W-PROGRAMMABLE-PATH

**Implement and exercise the canonical authored-program-to-resource path**

Status: **active** · Owner: Astra: program_install + localfirst · Updated: 2026-09-18T00:45:00-04:00

Select the canonical rule/program representation and actual authority projection, then implement needed compiler/native/proof/durable support and shell/Hermes consumers. Existing guards are retired only by replacing their missing guarantees. Active source investigation is recorded in sprints/2026-09-17.md.

**Next:** Join birth, distinct policy-control installation and declared invocation under the same source runtime profile.

**Done when:** Author and install a rule under actual resource authority, invoke a permitted operation through the chosen shell/agent path, refuse a violating operation with correct state/outcome evidence, and recover accepted behavior/history through the chosen durable runtime. Complete all necessary core obligations, not merely a private demo.

**Enables:**

- E-WORLD — Programmable social resource world
- E-KERNEL — Canonical typed semantic kernel

**Evidence / provenance:**

- [S-PROGRAMMING-REVIEW — Parent-reviewed programming and shell investigation](../research/programming.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

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

Status: **active** · Owner: Astra: proof_integrity + program_install · Updated: 2026-09-18T00:45:00-04:00

Reuse canonical CellRegistry, authority pages, ordered resource Book batches, MultiCellHyperedge and DataIntent; one final write per physical cell.

**Next:** Commit initial policy/source bytes, owner and policy-control grants, funding and fees through accepted native receiving.

**Done when:** Actual source-authorized birth commits identity, initial content, owner grant and selected fee together; refusals and crash/retry cannot expose a partial accepted result.

**Evidence so far:** Complete authority and funded birth preparation exercised; real source authorization, initial policy and native publication are still joining.

**Enables:**

- E-KERNEL — Canonical typed semantic kernel
- E-WORLD — Programmable social resource world

**Waiting for:**

- W-AUTHORITY-NATIVE — Bind native use to committed keys and complete authority
- W-POLICY-SOURCE — Store initial policies and use one runtime profile

**Evidence / provenance:**

- [S-IMPLEMENTATION-2300 — Late-evening source checkpoints, captured run, and shared-core assignments](../sprints/2026-09-17/checkpoint-2300.md)
- [S-IMPLEMENTATION-2330 — Executable receiving/admission checkpoint and rejected-turn correction](../sprints/2026-09-17/checkpoint-2330.md)
- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)

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

Status: **backlog** · Owner: Unassigned · Updated: 2026-09-18T00:45:00-04:00

Report which claims/work items need reinspection when source bytes change, with repository paths configurable on a contributor machine.

**Next:** Agree the portable path override and structured impact report contract before assignment.

**Done when:** The checker identifies unavailable repositories separately from changed files, explains affected records without rewriting their historical hashes, and runs against temporary fixture repositories.

**Enables:**

- E-KNOWLEDGE-HUB — Living project knowledge and contributor coordination

**Evidence / provenance:**

- [S-IMPLEMENTATION-0045 — September 18 implementation and contributor checkpoint](../sprints/2026-09-18/checkpoint-0045.md)
