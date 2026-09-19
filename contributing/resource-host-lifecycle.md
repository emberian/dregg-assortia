# Proposed ownership: persistent DREGG resource hosting

Draft from September 18, retained as **unassigned design work**. On September 19, ember reported assigning Wisper a separate low-level networking task outside our critical path. This supersedes the proposal to offer him this package. Runtime/export decisions below remain open; source and former lane ownership references describe the September 18 checkpoint, not current assignments. This platform package serves the intended community shellserver and participant-operated hosting. Android embedding remains a separate possible future feature.

The [native-host export investigation](../sprints/2026-09-18/account-handoff/design/dregg-native-host-export-proposal.md) is the earlier proposal. The BabyBear/29 profile is now implemented and passes its focused source checks; the receiving process and authenticated read/preparation interface are under construction. The [current checkpoint](../sprints/2026-09-18/resumed-0311.md) distinguishes source checks, actual receiving tests and the still-pending linked host. The public deployment and contributor-facing contract are not frozen.

The user-visible result: a friend obtains a programmable DREGG resource host, operates a resource through the real kernel, disconnects, and returns to the same identity, committed state and history. Its operator can restart, stop and wake the host without silently duplicating machines, losing state, double charging, or treating an uncertain command as a failed command safe to repeat.

A future host owner would own the lifecycle and its operational interfaces, with room to change inadequate existing designs. Core owners deliver and maintain the canonical operation/authority/receipt semantics. That boundary permits work in both areas concurrently once assignments resume.

## Why this is real work

Source inspection at DreggNet `7f5159126c09cdb829347a56ef9d52fa29b3db30` found useful machinery and concrete missing connections. These are source findings, not new deployment measurements.

| Existing entry | What is there | What the feature must resolve |
|---|---|---|
| [`VmProvider`](https://github.com/emberian/DreggNet/blob/7f5159126c09cdb829347a56ef9d52fa29b3db30/control/src/provider.rs#L173) | Provision, terminate, list, status and leased workload dispatch | Stable host identity, idempotent creation/adoption and actual workload readiness; a rented machine alone is insufficient |
| [`ServerFleet::reload`](https://github.com/emberian/DreggNet/blob/7f5159126c09cdb829347a56ef9d52fa29b3db30/control/src/server.rs#L645) | Durable server records and a metering cursor | It provisions again for each running record and reconstructs `ComputeCell` empty. Reconcile the existing backend and restore the actual resource image before serving |
| [`ServerFleet::bring_up`](https://github.com/emberian/DreggNet/blob/7f5159126c09cdb829347a56ef9d52fa29b3db30/control/src/server.rs#L1030) | Prepayment, provider provisioning and durable running status | Durable reconciliation across every external action/record boundary, including a lost response or failed final record write |
| [`VatsHandler`](https://github.com/emberian/DreggNet/blob/7f5159126c09cdb829347a56ef9d52fa29b3db30/gateway/src/vats.rs#L261) | Subject-scoped create/list/get | Owner-scoped lifecycle commands, durable operation status and resumable observation; stop/wake are not current HTTP operations |
| [`env_vat_plane`](https://github.com/emberian/DreggNet/blob/7f5159126c09cdb829347a56ef9d52fa29b3db30/gateway/src/main.rs#L544) | Local provider with a mirrored rent rail | Select and supervise the actual host; the current gateway main does not run `tick_uptime` or `reap_idle` |
| Bread [`complete_boot_recovery`](https://github.com/emberian/dregg/blob/73136dd30/node/src/lib.rs#L3747) | Actual reconstruction and convergence checks | Library construction is not full readiness: completion currently lives in private CLI startup, alongside process-level ownership |
| Mini [declared-resource receiver](https://github.com/emberian/minidregg/blob/278ed6a/Kernel/DeclaredResourceController.lean) | Actual signed capability/policy admission and durable invocation | A stable hosted native export, query/status/event contract and joined creation/replacement/delegation journey are being built |

The DreggCloud review is also relevant: its archive-first recovery and service contracts supply experience to carry forward. An operational control-plane row must not become an alternative authority over DREGG resource state.

The bounded [cloud review](../research/cloud-host-2026-09-18.md), [source identities](../research/cloud-host-sources-2026-09-18.json) and [mobile inventory](../research/mobile-2026-09-18.md) retain the underlying investigation. Android has Rust core/renderer experiments; a Kotlin/Gradle/JNI product host and a demonstrated native Lean port were not found in that inspection.

## Feature boundary

Own a **durable resource-host lifecycle**, spanning provider reconciliation, native process/library supervision, persistent storage and identity, owner commands, command status, events and packaging. The existing gateway/fleet is a concrete starting consumer, not a mandate to preserve every abstraction.

The intended host itself must become a programmable DREGG resource: ownership and desired lifecycle operations belong to its kernel-governed contract. Provider handles and reconciliation journals record the physical implementation of that intent. Ember selected self-governing management: resource rules may deliberately deny even their owner a subsequent policy change. Restart/recovery must preserve that decision, not provide an implicit repair privilege. Core and the host owner must define this source schema and the meaning of provider observations together; the existing `ServerRecord` is not automatically that canonical contract. Keep a request to start a host distinct from evidence that the external host actually started.

Proposed responsibilities:

- Define an idempotent provider contract around a stable logical host ID. Discover/adopt an already-created backend after uncertainty; correlate inventory with the requesting deployment and owner. Termination must also be recoverable.
- Make initialize, open, readiness, quiesce, stop and reopen explicit. Supervise child tasks/processes and preserve uncertain operations for reconciliation. A library caller must not exit its enclosing process or claim readiness before recovery succeeds.
- Restore the actual kernel-owned state and identity. Keep tenant stores, key custody and runtime/profile identities distinct; never replace a missing image with an empty cell under the same ID.
- Supervise lease charging and idle policy, using the actual settlement interface and stable charge identity. Reconcile external settlement with the recorded period; advance the cursor only with retained evidence.
- Expose owner-scoped lifecycle operations and acknowledged event resume. Service authentication identifies a caller; the kernel still decides that caller's resource authority.
- Package one Linux/homelab host with bounded resource use, truthful readiness, useful diagnostics and an integration harness. Define the adapter boundary so an Android host can later use the same canonical semantics.

Module/process organization, adapter language, supervision, diagnostics and packaging are part of the contributor's design ownership. Changes crossing authority, persistence or settlement semantics need joint review and executable evidence, not a prohibition against touching core code.

## Contract to freeze together

These are required meanings, **not existing stable method names**. The exact wire/C/JNI/API schema must be agreed against the selected implementation before an external client depends on it.

| Interface | Required meaning | Delivery owner |
|---|---|---|
| Initialize / open / stop | Explicit store and custody handle; incompatible or corrupt state refuses; readiness follows full recovery; stop reports pending/uncertain operations | Host owner with core recovery reviewer |
| Describe | Exact runtime, deployment, profile, supported codecs, durable boundary and actual network/finality state | Host owner; core supplies authoritative identifiers |
| Prepare / submit | Preparation discloses private state only after actual per-resource read authority; source-owned canonical signing frames; exact signed operation bytes and retry identity; blind signed writes remain possible with uniform public refusal | Core exports; host transports and supervises |
| Operation lookup | Original retained result and its boundary after response loss/restart; current state is separately identified | Core journal semantics; host API |
| Resource/history read | A projection from one identified committed boundary with applicable read authority; imported history rechecks original semantic authorization, not only physical roots | Core projection/export; host caching/API |
| Subscribe / acknowledge / resume | Store/deployment-bound cursor over retained records, explicit retention gaps and refresh; application acknowledgement controls its durable resume position | Joint contract; host implementation |
| Provider ensure / observe / terminate | Stable logical identity and durable reconciliation of uncertain external outcomes | Host owner |
| Charge / lookup charge | Canonical charge identity and external settlement evidence; unknown outcome is reconciled | Host owner with economic/core reviewer |

Resource writes enter the actual semantic receiver. Raw `DataIntent`, mutable `Ledger` access, database images and setup/genesis writes are internal interfaces. A host acknowledgement or heartbeat does not by itself prove correct remote computation. Admission, durable local acceptance and network finalization must keep their actual runtime-specific meanings.

The first runtime remains a decision to freeze. The September kernel work is minidregg's canonical birth/install/invoke/delegate path. Bread supplies existing node, World and Hermes consumers with different receipts and recovery semantics. A Bread lifecycle extraction can be useful immediately, but does not complete the Mini consumer cutover; a Mini host export does not become a federated Bread node by sharing an HTTP envelope. Preserve these identities in the contract and select one real end-to-end acceptance target.

## Receiving owners and initial files

| Area | Initial source scope / coordination |
|---|---|
| Host/fleet/gateway | DreggNet `control/src/provider.rs`, `server.rs`, relevant provider implementation; `gateway/src/vats.rs`, `main.rs` and owner/status/event routes |
| Native Bread lifecycle if selected | `breadstuffs/node/src/lib.rs`, `state.rs`, a proposed reusable host module, task startup and SDK network consumers; reserve shared files before editing |
| Canonical Mini exports | `minidregg/Kernel/{ResourceBirthReceiver,PolicyInstallReceiver,DeclaredResourceController}.lean` and native storage/signature adapters; current core owners are resume_host, resume_journey, resume_install and resume_birth_review; observation is owned by resume_foundations |
| Recovery/initialization | Bread runtime history and FFI lanes currently own factory-history and narrow/full Lean initialization changes; coordinate their checkpoints |
| Packaging/deployment | Selected DreggNet deployment directories and `dregg-infra`; first acceptance uses an explicitly configured local/homelab target |

Core must deliver a runnable source-pinned receiver/export harness, exact command and result codecs, stable identity/retry rules, and one accepted create → invoke → reopen witness. Existing [captured invocation evidence](../sprints/2026-09-18/checkpoint-0130.md) is a foundation, not that whole deliverable. Host work can start with provider reconciliation and lifecycle extraction while those exports converge; use the real current consumer in tests and record which runtime it exercises.

## Acceptance journey

1. An authenticated funded subject requests one host. The endpoint becomes ready only after the selected runtime has recovered the correct store, identity and profile.
2. Create or open a programmable resource, perform a permitted operation, and read its actual retained receipt/state through the host. Insufficient authority and stale state refuse without publishing success.
3. Drop the reply after acceptance. Restart gateway and worker independently. Lookup/retry returns the original operation result, and provider inventory shows one adopted backend. No second charge or resource mutation appears.
4. Crash before and after provider creation, settlement and durable status recording. Reconcile each uncertain interval. Restart a charge period without paying it twice or serving indefinitely after funds lapse.
5. Stop and wake the host. Restore the same resource/history and resume an acknowledged event cursor. A different tenant, wrong store/profile, corrupted published record or missing image produces an explicit refusal without destroying evidence.
6. Exercise two tenants, repeated in-process open/stop where supported, resource exhaustion and a failed backend. No stale endpoint, unowned task, shared key/store or unexplained replacement machine survives.

Keep an exact build/run recipe and source identities beside these witnesses. Unit/provider fakes support fault injection, while the final acceptance uses an actual native runtime and physical storage. Cloud, Android, provider bonding and proof-system completion have separate acceptance claims.

## Decisions before assignment

Ember and the eventual implementation owners should choose the first consumer: an operated Linux/homelab resource host is the proposal. Freeze its runtime/export and owner identity together with core. Android remains separate future work; this package is not Wisper's current assignment.

Real $DREGG lockup and devnet recorded-only penalties remain accepted product intent, with asset, custody and exit terms unresolved. They require their own canonical economic contract; this host package should expose the necessary provider identity/evidence seam without inventing those terms.
