# Local-first participant nodes and resource hosting — sprint investigation

2026-09-17. Astra lane `/root/sprint_localfirst`. Source inspection only: no builds, tests, live probes, Git commands, node operation, deployments, or code edits. This report concerns the current local worktrees, which may contain unrelated uncommitted work. File/test references establish inspected implementation and executable scenarios, not newly observed passes.

## Recommended integration target

Make a participant's independently operated node a real durable resource host: it holds its own node identity and storage; receives owner-authorized resource placement; accepts locally authored programs/requests through the same canonical typed admission as the community host; retains exact pending and accepted history across restart; exchanges that history over an actual network; and publishes a valid merge through the same kernel and durable commit path. A second `World::fork()` inside one process is not this target.

Use minidregg's canonical typed cell/effect/hyperedge/history path as the semantic source selected by the carrier/history lanes. Reuse and repair breadstuffs' actual network, signed ingress, custody and recovery mechanisms around that source. Use leanuweave's existing delivery and history results where an explicit representation theorem connects them. Do not introduce a second authoritative document history, a parallel permissive executor, or an app-only sync service.

Three powers need distinct checked bindings:

1. An **author/principal** may request a particular resource transition.
2. A **host** may retain, serve or execute that resource under its placement and disclosure policy.
3. A **settlement participant** may order/attest a transition under the selected resource's finality regime.

Ordinary ownership/hosting is also distinct from volunteering as a bonded provider. Requiring every friend who runs a node to lock provider stake would be an additional product rule, not an implication of the user's request.

## Existing receiving paths

### Identity and signed mutation

Breadstuffs has an actual remote mutation contract, not merely an in-memory example:

```rust
// turn/src/signed_turn.rs:20
pub struct SignedTurn {
    pub turn: Turn,
    pub signature: Signature,
    pub signer: PublicKey,
    pub pq_signature: Vec<u8>,
    pub pq_signer: Vec<u8>,
}

// node/src/signed_turn_validation.rs:259
pub fn validate_signed_turn(
    signed: &SignedTurn,
    executor: &TurnExecutor,
    live_agent: Option<&dregg_cell::Cell>,
) -> Result<ValidatedSignedTurn, SignedTurnValidationError>

// same file:639
pub fn stage_signed_turn_admission(
    s: &mut NodeStateInner,
    signed: &SignedTurn,
) -> Result<StagedAdmission, AdmissionRefusal>
```

The validator checks the Ed25519 signature over `Turn::hash`, binds `turn.agent` to `CellId::derive_raw(signer, blake3("default"))`, and in required-PQ mode binds the carried ML-DSA public key to independently committed cell identity or the explicit legacy enrollment bridge. Staging verifies this agent's receipt head, runs `execute_via_producer`, and unconditionally rolls back the ledger restore point. Therefore the HTTP `accepted` response is admission, not the authoritative commit.

The bearer-gated signed route is `/turns/submit` / `/api/turns/submit-signed` (`node/src/api.rs:2589–2620,2753–2771,5572–5593`); the shared `submit_signed_turn` later gossips the bytes and submits them to blocklace (`:5729–5760`). Finalization rechecks the user envelope independently of block-producer authentication (`node/src/blocklace_sync.rs:9300–9370`). This is the natural receiving seam to adapt to the canonical typed carrier; duplicating a request decoder/gate for local-first work would create another policy path.

### Actual node replication and restart

`node/src/blocklace_sync.rs:4890–4945` creates a QUIC `PeerNode` and a signed `GossipNetwork`. Transport-certificate identity changes across boots and is explicitly not authority; the stable envelope sender is `blake3(federation_public_key)`, resolved through enrolled federation keys. Authenticated peer exchange advertises reachable addresses (`:4935–4955`). Blocklace, turns, revocations, intents, roots, checkpoints and budgets already have gossip routes (`:4985–5070`). This transports committee state, not a per-cell foreign-owner placement authorization.

Important correction to stale memory: live membership joins now carry `MembershipAction::Join { node_id, ml_dsa_pubkey }`; startup scans retained blocks to restore the joined members' PQ keys (`:4835–4877`). The older memory that every live Join lacks that key and necessarily halts after projection must not be repeated as current state. This source reading does not establish a fresh successful multi-node join run.

Finalized execution constructs a `CommitRecord` from the complete actual touched-cell overlay and explicit removals (`:11655–11692`), then commits receipt/root/nullifiers/executor state through the store at an expected durable ordinal (`:11705–11835`). Only after this commit does it install the candidate overlay into authoritative RAM (`:11839–11860`). Duplicate durable completion suppresses duplicate RAM/event publication. These are reusable receiving obligations for canonical data intents, not a reason to layer a second file store beside the node.

`node/src/lib.rs:3685+` contains the shared boot-recovery weld: reconstruct the genesis baseline plus retained overlay/removals, check recovery convergence, and pin a full height-zero baseline where authorized. It also explicitly names a still-distinct `run_mcp`/`run_node` boot-baseline construction issue. The durable consumer must be common to shell, HTTP and node startup; preserving separate baseline builders would make one data directory depend on which interface opened it.

### Remote shell/client joins that need repair

There is already an HTTP `deos_js::WorldSink` in `dregg-sdk-net/src/node_world_sink.rs`, under feature `world-sink`:

```rust
// :121
pub async fn submit_turn(
    &self, signer: &AgentCipherclerk, agent: CellId,
    method: &str, effects: Vec<Effect>, federation_id: &[u8; 32],
) -> Result<[u8; 32], SdkError>
```

It fetches a fresh nonce, but still fetches the **node-wide** `/api/receipts` head (`:132,247–264`), while the admission predicate requires the **acting agent's** committed head. Its HTTP construction shown at `:148–159` carries no bearer. After admission it performs one immediate receipt lookup (`:272+`), so finalization lag becomes an error; it has no durable submission/retry state machine. Its ledger crawl intentionally omits programs and sovereign commitments and skips cells it cannot reconstruct (`:79–103`), so it is an inspector projection, not an authoritative replica image.

The newer `dregg-sdk-net/src/remote.rs` already has `RemoteRuntime::agent_receipt_chain_head` (`:255`) and action signing bound to the live nonce. However `RemoteAuthorizedTurn::submit` (`:538–555`) returns `RemoteReceipt { turn_hash }` immediately on HTTP `accepted`. Despite the docstring, that method does not wait for committed receipt/finality. Consolidate the good signing/head handling and add one explicit admitted → finalized/rejected lifecycle, with persisted retry identity and actual receiver verification. The shell lane has been notified of both source findings.

The existing SSE channel also need not be reinvented: `node/src/events.rs:150–191` reads the canonical receipt chain; `events_stream` (`:233`) treats broadcasts as wake-ups and supports `Last-Event-ID`. The cockpit `ReceiptFeed` (`starbridge-v2/src/live_node.rs:372–450`) is only a bounded in-memory tail; `client.rs:823–884` reconnects within that reader's lifetime. An SSE notification/read cache is not a durable replica or a finality verifier.

## Placement/custody exists in pieces; close the receiving protocol

### Content placement and operator obligations

`storage/src/placement.rs:217` has:

```rust
pub fn select_operators(
    candidates: &[OperatorCandidate], grain_id: &[u8], count: usize,
) -> Result<Vec<Placement>, PlacementError>
```

Candidates bind operator ID, bond, bond minimum and dispute count (`:83–96`). Selection is deterministic owner-supplied candidate ranking, not an open registration service and not verification that the supplied bond is actually locked. `storage/src/durability_deal.rs:223` creates a metadata deal plus erasure shards; `reconstruct` (`:298`), `verify_challenge` (`:313`) and `verify_challenge_authenticated` (`:362`) reuse existing erasure/membership checks. These are useful storage-service components. The sole located node-side composition, `node/src/market_loop.rs`, is entirely inside `#[cfg(test)] mod tests` from line 23. It does not currently implement provider transport, durable placement acceptance or a running market. Economic lane is reviewing the challenge/stake part.

### Cell mobility primitives

`cell/src/ledger.rs` exposes actual operations:

```rust
pub fn migrate_prepare(
    &mut self, id: &CellId, from: FederationId, to: FederationId,
    target_mode: CellMode, prepared_at: u64,
) -> Result<MigrationVoucher, MigrationError> // :1676

pub fn migrate_accept(
    &mut self, voucher: &MigrationVoucher, cell: Cell,
    this_federation: FederationId, accepted_at: u64,
) -> Result<MigrationReceipt, MigrationError> // :1716

pub fn migrate_commit(
    &mut self, id: &CellId, receipt: &MigrationReceipt,
) -> Result<(), MigrationError> // :1786
```

Prepare retains a migration lock. Accept checks destination, cell identity, exact state commitment and occupied destination tables; it installs hosted state or a sovereign commitment. Commit tombstones the source and clears the lock. Cell identity survives a location change because it is derived from public key and token identity, not host address.

But `MigrationVoucher` / `MigrationReceipt` (`cell/src/migration.rs:64–129`) contain data and hashes, **no authenticated source/destination certificate**. The cell-level commit checks its cell/voucher binding, not a cryptographic origin. A bounded Rust reference search found the ledger handoff exercised in cell/integration and honesty tests; no live node route calling these ledger methods was located. The separate `TurnExecutor::cell_migrations` manager (`turn/src/executor/migration.rs:88+`) is an in-memory state machine; its `confirm_receipt(cell_id, height)` receives no receipt bytes. Do not treat either primitive alone as a secure distributed handoff.

`dregg-genesis-snapshot/src/lib.rs:47–79` explicitly confirms this distinction: its reused vouchers provide self-consistency, not source-chain authentication; a wholly self-consistent forged entry can pass. Its own operator deployment connection is also named separately.

The sprint repair should make placement a checked resource transition: exact owner/principal, resource and revision/root, destination node identity/key epoch, read/serve/execute rights, disclosure policy, duration/exit and required data availability. Host acceptance and its recoverable custody acknowledgement must bind that exact assignment. Full mutable-cell relocation must durably prepare/freeze before export, authenticate source finality and destination acceptance, persist recovery state on both hosts, and complete through the canonical transition. A timeout cannot independently revive a source after an accepted destination may already be live. Reconcile/delete the two partial migration state machines as the canonical path replaces them.

## Local-first histories: existing material to connect

### Breadstuffs behavior and its exact scope

`dregg-doc/tests/two_device_sync.rs` is an executable behavior fixture for divergent histories and settlement-tip revocation. Its `SettlementGate` is defined in the **test** (`:78–161`); its revocation check is Rust over fixture data, not a running remote admission service. Reuse the scenarios, not this fixture as new authority semantics.

`BranchStitchSession::fork` (`starbridge-v2/src/branch_stitch_session.rs:156`) deep-clones a `World`; `Branch::drive` (`:252`) executes against that local branch. `stitch(&self, a: &Branch, b: &Branch) -> StitchVerdict` (`:181`) computes the state pushout and current-tip authority verdict. Its immutable `&self` method returns the proposed root/conflicts/admitted/dropped authority; it does not install that verdict into a durable remote base. These are good behavior and UI inputs, but two branches still share one process/library environment and are not independent hosts.

The remote mirror has a real frame abstraction, but do not infer more transport than implemented. `captp/src/netlayer.rs:31–54` supplies in-process and in-memory relay adapters; the silo TCP mapping is documented as a further instance. `starbridge-v2/src/netlayer_image.rs:226` fetches snapshot frames, while `remote_mirror.rs:410`'s `propose_edit` returns only the cell that a subsequent turn would target. Actual QUIC and HTTP node transports above are the stronger existing network integration surfaces.

### Minidregg's canonical event source

`Theory/CausalVersionDag.lean:57–116` gives the exact event preimage: history domain, stream, schema/version, semantic object root, pre/post roots, canonical parent frontier, author, principal, request and effect identities. Parent digests are already strictly ordered. `AddressedEvent` binds ID to the lawful codec and digest; collision/binding remains an explicit assumption. `SemanticFamily` (`:135+`) separately retains `Evidence`, `ParentCompatible` and the actual `Step` relation. Therefore event-set union alone must not be promoted into accepted resource effects.

`Theory/LaceMerge.lean:69–96` uses those addressed events for replica views and union-like merge, with convergence conditional on the chosen binding premise. This is an existing canonical replication algebra; no reason to invent another ID universe.

Hyperdocument's event log is a separate append-only sparse cell (`Kernel/HyperdocumentEventLog.lean:30–93`). Publication/merge publication use typed multi-cell commits to join resource content and event append; `Assurance/HyperdocumentGuardedDurable.lean:234–264` rejects a moved authority root at durable preflight. History lane owns the detailed declaration and physical-publication design.

### Leanuweave's receiving and recovery mechanisms

The inspected repository is `~/dev/leanuweave` (its project/crate is called lean-uwueave/uwueave). It contains more than the uncommitted static Projection V2 experiment in minidregg:

```lean
-- Uwueave/HistoryRuntime.lean:394,486,582
structure Event (Id Payload : Type) where
  id : Id
  parents : List Id
  payload : Payload
structure DeliveryState (Id Payload : Type) where
  materialized : EventState Id Payload
  pending : List (Event Id Payload)
  capacity : Nat
def receive ... (state : DeliveryState Id Payload)
  (event : Event Id Payload) : ReceiveDecision Id Payload
```

The Lean receive function distinguishes delivered, buffered, exact retry, ID collision, capacity refusal, self-parent and duplicate-parent. `PersistentHistoryRuntime` supplies the corresponding pure durable-record schema. `FiniteHistoryProtocol.RecordImage` (`:200`) is the crucial representation obligation: equal materialized event sets representing two semantic histories imply `SameRecord`; `SemanticReplica` (`:212`) then combines settled delivery with that representation. Convergence additionally requires `HistoryConvergent` / `RecordDetermined`; authentication and availability do not follow from equality of IDs.

The real Rust `HistoryArrivalJournal` (`rust/src/persistence/history.rs:761`) durably writes accepted arrivals before changing materialized/pending state. `open(path, options, capacity)` replays the arrival journal and verifies recorded checkpoints; `receive`/`receive_at` deduplicate exact bytes and reject collisions/capacity changes. This is distinct from `BufferedHistoryJournal` (`:460`), whose pending buffer is explicitly volatile. Neither is a proved refinement of the Lean delivery schema; the source calls out that exact debt (`:458,754–758`). Its IDs are caller-supplied equality keys, not authentication. There is no networking dependency in `rust/Cargo.toml`; these are host components to attach to transport.

`rust/src/auth_runtime.rs:589+` also provides real `AuthenticatedRuntime<V,C,R,A,M,T>` orchestration over **move operations**, with fixed document/genesis/context/execution binding. `admit(maximum_bytes, raw_request)` (`:753`) runs Lean projection, exact-byte verification, retry/collision classification, context/authority/membership, Lean preflight, trace validation, durable append then in-memory commit. `recover` (`:651`) rechecks stored certificates and each historical context before replay. Its available keyed-BLAKE3 verifier is a symmetric MAC profile (`auth_verifier.rs:1–15`), not DREGG public-key authority or a generic typed resource executor. Reuse this discipline and any faithfully mapped component; do not silently substitute it for minidregg admission.

The cross-repo contract (`minidregg/CROSS_REPO_CONTRACTS.md:13–46`) selects rich Projection V3 as planning data and RuntimeAuth V4 as a narrower context-auth sidecar. Neither grants DREGG authorization. Do not merge the static V2 projection merely to claim integration.

### Exact history bridge agreed with the history lane

Candidate mapping: delivery event ID = `StoredVersionEvent.key.digest`; parents = the canonical record's parent digests; payload = full canonical record **plus** the exact accepted declaration/patch and state/proof references needed to derive non-merge states. A post-root by itself cannot satisfy the representation relation. Preserve canonical parent ordering before hashing; do not sort a signed payload after admission.

`RecordImage.faithful` must establish same DAG/root/origin shape, non-merge states and genesis. Its `SameRecord` relation intentionally forgets merge bases/states; it **cannot replace** minidregg's exact accepted merge post-root and current-authority checks. Incoming network data can enter a durable bounded pending inbox without becoming canonical accepted history. Only the Lean-valid accepted append/publication advances the one authoritative published event log. This is a delivery queue in front of the kernel, not a parallel history beside it.

## Coherent cross-stack work bundle

1. **Canonical carrier and bytes.** Finish the typed joint commit/data-intent carrier and practical codec work identified by the carrier lane: bound `AcceptedCellEffect` → `TypedCellHyperedge` / `MultiCellHyperedge` → exact `DataIntent`. Peer receiving must retain the complete versioned family/arguments/subject/policy epoch/pre-root/nonce bytes and exact stable replay envelope, then invoke the Lean controller; arbitrary host reconstruction of state is not an accepted substitute. The canonical authority cell remains a read-only root dependency in atomic preflight and retry identity (`HyperdocumentGuardedDurable.PublicationPlan`, `CanonicalPolicyRegistry.guardPolicyRegistry`). Bind resource/event/request/authority/root identities once. Add the exact delivery representation to existing canonical event types. Every ingress and restart path must consume this artifact, not separately reauthor its fields. This generic typed action endpoint remains work to implement; the current native artifact is not already that endpoint.
2. **One durable participant runtime.** Implement the selected physical CAS/root/nullifier/history/outbox installation and cold recovery. Use actual independent data directories and node keys. Repair the node/shell baseline discrepancy and receipt acknowledgement lifecycle; make durable pending delivery and canonical accepted publication distinct states in the API and UI.
3. **Owner-authorized hosting and mobility.** Derive the assignment/acceptance/withdrawal transitions through the same typed kernel. Bind transport node identity to the selected assignment; a bearer or certificate alone confers no resource rights. Complete persistent handoff/recovery where mutable authority changes host. Reuse storage challenge/erasure components with their real custody and availability obligations closed.
4. **Real transport/reconnect.** Carry bounded canonical candidates/accepted publication data through existing node HTTP/QUIC or the existing authenticated relay service. Retain durable inbox/outbox IDs and exact attempts/acknowledgements (`Kernel/OutboxDelivery.lean:31–70,114–161,199+` already states these obligations). Add authenticated manifest/frontier exchange and missing-parent fetch under the resource's disclosure policy. Keep committee joins distinct from permission to serve a resource.
5. **Offline merge and settlement.** Permit local branch authoring inside the actual semantic substrate. On reconnect, verify exact provenance/parents and select the resource's declared merge/coordination regime; submit the resulting declaration through current-root authority admission and atomic publication. Use leanuweave's classifications/record-determined selection where the chosen algebra matches. Conflicting linear resource updates need real settlement; no local UI grant can bypass it.
6. **Finality receiving closure.** `Kernel/ReplicatedSettlementFinality.Candidate` (`:50`) carries exact prior log and intent; `AuthenticatedSettlementFinality` pins authority root, signer/key epoch, policy and exact candidate bytes. Its signature origin/key directory/issuance discipline still need concrete realization. `FinalityGate` currently exports a closed `Fin 3` trusted-vote-book example and explicitly names signed-vote and receipt-seam work. Connect/generalize this to the real carrier, retaining the existing network implementation as a donor rather than calling its old proof interface equivalent by assertion. Resource causal tiers require their actual confluence conditions; monetary/authority state does not become coordination-free because history exchange converges.

These are substantive kernel, compiler, protocol and runtime changes. They should be assigned as connected sprint work, not converted into product limitations or used to justify a shell facade over disconnected mutable state.

## Acceptance evidence to produce

Run the integrated journey on independently keyed node processes, including two machines (hbox `/tank`, persvati, or the local machine as available). Use isolated data roots/build lanes and the repository's build-memory policies. This report did not run them.

- Two participants independently boot/reopen the same authorized resource; both can serve it from their own persistent storage according to the placement policy.
- A shell-authored rule/program is installed and invoked locally; one permitted and one forbidden transition use the real canonical checker.
- Partition nodes; create two legitimate offline branches; reconnect with reversed delivery and duplicate retry. Missing-parent data remains durable pending across an actual process restart. Both retain exactly the accepted event set and materialize the declared result after settlement.
- Revoke/rotate authority after branch creation. The merge checks the current settlement authority snapshot and refuses or removes only the authority the selected semantics says is no longer admitted; it cannot reuse a branch-time authorization verdict.
- Deliver same-ID/different-payload, wrong resource domain, wrong parent order, wrong author/key epoch, forged placement, stale expected root and wrong destination acknowledgement. Refusals preserve the previous canonical root and never acknowledge unpublished state.
- Crash before/after each durable linearization and between network send/ack. Recovery produces the same exact accepted history and roots at every committed step; retry neither loses an accepted edit nor executes it twice. Check every recorded root, not only the final reopened root.
- Host withdrawal/relocation survives an interrupted handoff without two live mutation authorities or a permanently forgotten resource. An independent participant receives actual bytes, not just a snapshot summary.
- Normal friends' nodes do not acquire validator authority or bonded-provider obligations implicitly. Public and restricted resources enforce the selected disclosure policy on the serving side.

Useful existing regression source to reuse: `dregg-doc/tests/two_device_sync.rs`; `cell/tests/integration_migration.rs`; `node/src/first_turn_e2e.rs`; `node/src/lib.rs` recovery tests from `:4345`; `dregg-sdk-net/src/remote.rs:626` agent-head test; `leanuweave/rust/tests/runtime_auth_arrival.rs:93`; `leanuweave/rust/tests/authenticated_runtime.rs:798,973,1090,1141,1176,1248`. Their current passes were not measured. The actual chosen typed runtime requires its own cross-process tests; these local fixtures alone cannot establish the release journey.

## Consequential choices for the main loop

- Which **resource finality/placement domain** is first: one community committee with ordinary nonvalidator participant hosts, participant-owned resource domains, or both? A single-host resource domain can exist without pretending to provide quorum finality; it still needs canonical authority and durable history.
- Does a participant replica receive plaintext, encrypted content, or an attenuated view for each resource class? Current public explorer endpoints cannot by themselves enforce private resource disclosure. This must be represented in resource/hosting policy before payload transport.
- Which mutable resources may merge automatically under a proved declared algebra, which retain first-class conflict, and which require ordered settlement? Application genre does not decide this; each resource's laws do.
- Is host acceptance a revocable best-effort replica permission or a priced availability obligation? Provider bonding is the latter's separate economic protocol, not the default meaning of self-hosting.
- Does September 26 include complete mutable-cell relocation, or independent participant hosting plus local branch/merge publication with explicit ongoing placement? The primitives exist for both, but a functioning network and a signed migration record are not substitutes for the two-sided commit/recovery closure.

The user's latest instruction supports doing the necessary core work, including closing these protocol gaps. These choices select the intended semantics; they are not requests to accept the gaps indefinitely.
