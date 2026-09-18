# Program installation: core sprint implementation bundle

Source inspection, 2026-09-17. No builds, tests, live node requests, Git operations, or sibling repository edits were performed. Locations refer to the inspected working tree. Proposed files and checks below do not yet exist unless explicitly identified as existing.

## Recommendation

Put the new authoritative program-install/invoke path in **minidregg's canonical typed carrier**, and make reused breadstuffs shell, resource and hosting surfaces call that path. This follows accepted [D-0002](/Users/ember/dev/minidregg/docs/decisions/D-0002-canonical-hyperedge-kernel.md), rather than choosing a weaker route to avoid old proof work. The carrier lane independently reaches the same recommendation.

The kernel must consume actual authored program data on invocation. An integer called `programCode`, a stored blob, an uploaded descriptor, and a script that submits effects are each insufficient by themselves. The nearest existing semantic foundation is [CanonicalPolicyAdmission.PolicyRecord](/Users/ember/dev/minidregg/Compiler/CanonicalPolicyAdmission.lean:36): complete `Pred` source plus policy ID, version, domain, semantics and predecessor. Its compiler gate really invokes `PredCompile.lower`; its soundness theorem actually invokes the general lowering theorem. Complete this mechanism, its source codec, state projection, executable admission and durable receiver.

Preserve breadth by making this a common resource operation. Research workrooms, social objects, stories, games and public jobs can all install rules and invoke typed operations over the same carrier. Authored transition rules plus a programmable shell are already kernel programmability; an imperative kernel language that generates effects is a further semantic feature, not something to imply from the existing names. If we add parameterized action-producing entries, their argument substitution and derived patch must be in Lean too.

Breadstuffs needs targeted repairs wherever it remains a receiving authority. It should not acquire a second independently authoritative implementation of the new program model. In particular, adding its missing native wire arm and then advertising a verified install would make the wrong boundary look complete.

## What the existing breadstuffs path actually contains

### Program data and ordered application exist

`cell/src/program/types.rs:6–110` defines serializable `None`, `Predicate`, `Cases` and `Circuit` programs. Predicate/case composition is authored data; the rules validate proposed transitions. `turn/src/action.rs:1154` carries `Effect::SetProgram`; `authorize.rs:2647` uses program-identity `SetVerificationKey` authority. `apply.rs:1400–1457` checks cross-cell permission and live lifecycle, journals the old program, then assigns the new one. It does not require a host rebuild to compose existing rules.

The program is part of committed authority. `cell/src/commitment.rs:1118–1136` serializes its variant/payload into the authority residue; `compute_authority_digest_8` at 1007 hashes that residue. `turn/src/action.rs:2289` separately hashes postcard program bytes into the effect. These are real existing commitments, not a proof that all encodings or consumers coincide. The program byte format has no independent evaluator/schema version at this boundary. Both serializers also have error-swallowing branches (`unwrap_or_default` / `if let Ok`) that a total canonical encoding should eliminate rather than copy.

### Native Lean coverage is more than a missing enum arm

Lean already has the integer-valued operation:

- `metatheory/Dregg2/Exec/TurnExecutorFull/PerAsset.lean:1581`: `setProgramA actor cell prog`.
- `Exec/Handlers/StateSupply.lean:643`: `setProgramEffect` delegates to `stateWriteEffect`.
- `Exec/EffectsState.lean:206`: the write requires authority, account membership and a live cell.
- `Exec/FFI.lean:835`: JSON `setprogram` parsing already exists.

Rust lacks the corresponding `WireAction`, direct-FFI builder, effect projection and `StateOp` reconstruction. Exact edit owners if this compatibility path is retained:

1. `dregg-lean-ffi/src/marshal.rs`: `WireAction`, encoder, roundtrip fixtures.
2. `metatheory/Dregg2/Exec/FFIDirect.lean` plus `dregg-lean-ffi/src/lean_direct.rs`: direct constructor/export/import parity.
3. `exec-lean/src/lean_shadow.rs`: eligibility, referenced-cell collection, projection and pre-state source. Do not update only the public coverage list.
4. `exec-lean/src/lean_apply.rs`: exact committed post-image and whole-turn rollback, including program payload and caches.

**The more important receiving gap:** `ledger_to_wire_state` at `lean_shadow.rs:1910–2018` carries balance, nonce, ordinary fields, caps, lifecycle and delegation pointer, but no installed `CellProgram` or its policy semantics. `forest_is_root_agreeing` at 882 admits by turn shape/effect kind, without reading the program-bearing ledger. `produce_via_lean` at `lean_apply.rs:1770–1930` unconditionally installs a Lean COMMIT even when the Rust reference refuses. Thus the Rust program evaluator is not a safety backstop on this path. A wire arm plus turn-payload replay does not make installed rules authoritative.

This is a source-derived candidate violation requiring the narrow executable check below, not a claimed reproduced exploit. The current `monotonic_slot_poles_through_lean.rs` explicitly drives `TurnExecutor::execute` with the Lean constraint oracle; it does not test `produce_via_lean`. The distinction matters even when both tests are described as using Lean.

### Program upgrade ordering also needs a semantic check

`execute_tree.rs:1082` snapshots only `CellState`; 1109 partitions permission effects; 1203 applies `SetProgram` in the permission tail; 1332 then runs the program evaluator. That evaluator obtains `touched_cell.program` from the **post-effect** ledger at 665–710. Setting a weaker program last therefore does not, by itself, ensure other effects in the action were judged under the prior law. This contradicts the protection claimed by `apply_set_program`'s comment.

Recommendation for the canonical carrier: every incidence in a joint turn is admitted against the same pre-state policy; a program update takes effect on later committed requests. An explicit administrative upgrade operation can remain possible under current authority, but it must not retroactively authorize co-batched data effects. A newly installed rule need not be evaluated as though it had authorized its own installation. This is a proposed precise upgrade contract, not a claim that ember already selected every detail.

### Sovereign projection guard is correctly identifying missing machinery

`rotation_witness.rs:1208–1217` classifies SetProgram as `UnprojectedMover`; `sdk/src/cipherclerk.rs:5537–5554` refuses it before either sovereign cohort route. The shared `apply_effect_to_cell` has no SetProgram arm. The runtime VM effect type, selector and projection have no SetProgram row (`circuit/src/effect_vm/effect.rs`, `trace.rs:55`; `turn/src/executor/effect_vm_bridge.rs`, `sdk/src/cipherclerk.rs:6501`).

There is a Lean `setProgramV3` descriptor, but it is **not** a completed runtime route. `Emit/EffectVmEmitRotationV3.lean:5593–5620` wraps the setVK face with a single record-digest pin and explicitly leaves it at limb-0 strength. Its prose says runtime mapping exists; the inspected Rust projectors contradict that statement. The own-selector/dispatch/PI/witness/after-cell work is real.

More seriously, `Circuit/RotatedKernelRefinementProgram.lean:170–187`'s headline `setProgram_descriptorRefines_sat` returns its entire `SetProgramSpec` from readout fields: `guard`, `cellMapMove`, log and frames. It never consumes `hsat` or `hside`. The separate `setProgram_forced` theorem consumes the descriptor, but its readout assumes a singleton program-slot root and externally anchored program digest; that is not the actual serialized full authority residue. Connecting this headline theorem is not a proof repair. Replace the assumed transition with an extraction from the actual accepted statement and prove the program reference/source/state bindings.

The proof-integrity lane independently verified this statement finding. It also advises canonical injective source encoding before hashing; eight reduced u32 limbs are not an injective byte representation.

### Full-turn proving does not cure the omission

The full-turn node also calls `AgentCipherclerk::try_convert_effects_to_vm` (`node/src/turn_proving.rs:938`, 1261, 1607). The SDK projector drops unhandled effects, then injects `NoOp` when the result is empty (`cipherclerk.rs:7016–7030`). SetProgram is not one of its checked named refusals. The rotation builder declines a NoOp-only projection (`turn_proving.rs:698–724`), and the nonrotated branch builds/compares actor EffectVM commitments (`:970–1025`). Thus a narrow proof can describe a projected no-op while the runtime had a program installation. No fresh finalization run was performed, so this report does not assert a particular deployed node's resulting status.

This route is an additional obligation to close, not a release alternative. Both sovereign and full-turn consumers must bind every accepted effect and the actual installed program semantics; an effect that is neither represented nor separately proved cannot disappear behind another cohort.

## One shared install/invoke contract

The following is a proposal ready for implementation across the four lanes, consistent with D-0002:

- **Program source:** canonical, versioned bytes for a closed AST; content address binds the complete record, domain, evaluator semantics, schema, predecessor and entry definitions. Crypto binding is a named hash property, never literal injectivity of a compressing digest.
- **Install/update request:** resource identity, exact prior resource root/revision and prior program reference, new source address, typed installation args, actor/delegation evidence, idempotency/nullifier and resource budget. Authority and current policy are read from the same canonical pre-state. Missing source or unsupported semantics refuses before publication.
- **Invocation:** exact program reference and named operation/typed arguments. The evaluator selects that installed source, computes or validates the canonical patch, and produces accepted incidences. A caller cannot submit an unrelated patch under an agreeing opaque digest. Shell scripts may calculate proposals, but cannot substitute the program gate.
- **Atomic publication:** resource behavior reference, canonical registry entry and resource manifest move in the same typed hyperedge and durable transaction. The content/presentation lanes share that resource identity. A staged source blob is not an installed program.
- **Result:** either a precise refusal with unchanged state, or the selected program identity, actual pre/post roots, ordered receipt/history and durable acknowledgment. Retry returns the same committed identity. A renderer or agent reads this result rather than a separate local applet state.

The resource/history lane proposes a typed resource-component manifest with body, behavior and presentation references, and an event in the existing separate append-only log to avoid a post-root self-cycle. The shell lane proposes `program.read`, `program.install/update`, `program.invoke`, resource read/history and delegated share/fork; CLI and MCP compile to the same typed requests.

## Ownership and implementation order

### A. Semantic/source codec lane — can begin immediately

Own minidregg `Pred/Core.lean`, a new `Compiler/PolicyRecordCodec.lean`, and the codec consumer in `Compiler/CredentialAuthorityPolicyRegistry.lean`. Coordinate any shared type edits with carrier ownership. Replace `Encodable.ofCountable` at line 77 with an executable structural codec using the project's lawful streaming codec conventions. Preserve exact decode/encode laws and reject unknown versions, trailing junk and malformed constructor payloads. Version the format; do not reinterpret previous bytes.

The declared-action codec separately emits a unary list of length `declaration.code + 1` (`Theory/DeclaredActionLowering.lean:271`); that must be replaced by a practical codec in the carrier lane before real source roundtrips. Do not keep program source as a giant integer or paper over it with a second Rust codec.

### B. Installed rules and upgrade authority — core kernel lane

Own `Compiler/CanonicalPolicyAdmission.lean`, `Kernel/CanonicalPolicyRegistry.lean`, and a new typed installation/invocation family adjacent to them. Carrier lane owns shared `Theory/CellState`, `AcceptedCellEffect`, credential-authority projection, hyperedge and durable admission APIs; coordinate those changes rather than editing their hot files.

Implement an executable admission function over materialized canonical state and explicit evidence, deriving `Authorized` and the validated patch. Existing `admit` takes already-constructed `Evidence` and an epoch equality proof; connecting an HTTP endpoint requires executable evidence verification, not asking Rust to manufacture those proofs. Existing registry read guards cover invocation under a stable registry; installation itself needs a registry write with the matching prior-root guard and canonical patch.

The `Pred` fragment has actual reference semantics and actual lowering. `le` and `monotone` are currently rejected by `PredCompile.supported` (373–380); add the required finite/full-width ordered arithmetic lowering and forcing theorem in `Compiler/PredCompile.lean` and its arithmetic compiler dependencies. The deployed value representation and cast-injectivity condition must be established, not assumed by a Boolean host flag. Existing `witnessed` is first-party fail-closed under `Pred.eval`; external proof discharge is a separate explicit family if needed.

### C. Native receiver and durable publication — carrier/history lanes

Own a real service entry point consuming emitted/compiled Lean admission and typed durable intents, with physical persistence and recovery. Reuse existing native transport/storage packages only where they implement this exact carrier. Do not place the authoritative program map alongside canonical state or publish the resource manifest before installation commits. The carrier and history reports own the precise new service files and physical refinement boundary.

### D. Proof statement/descriptor lane — required for the selected proof path

Own the Lean statement from decoded request/program source through authorized patch to canonical post-state; compiler emission; verifier request/program/source/root binding; and adversarial statement tests. If breadstuffs remains a proof receiver, coordinate these concrete files:

- `metatheory/Dregg2/Circuit/Spec/cellstateprogram.lean`, `RotatedKernelRefinementProgram.lean`, and `Emit/EffectVmEmitRotationV3.lean` — replace assumed readout completion with real forcing/derivation, then emit.
- `circuit/src/effect_vm/effect.rs`, `columns.rs`, `helpers.rs`, `trace.rs`, `trace_rotated.rs` — data projection/witness generation/descriptor dispatch only; **no Rust-authored AIR**.
- `turn/src/executor/effect_vm_bridge.rs`, `rotation_witness.rs`, `proof_verify.rs`; `sdk/src/cipherclerk.rs`, `full_turn_proof.rs`; `node/src/turn_proving.rs` — exact one-statement producer/verifier contract, all full-turn/sovereign paths, mixed and nested effects.
- Generated descriptor registries/VK identities and affected downstream recursion pins — generated, not manually transcribed.

A correct host recomputation protects a full node but does not prove the source/program relation to a ledgerless verifier. Both consumer classes must have their actual acceptance conditions specified and checked. Remove the UnprojectedMover refusal only in the commit that gives its consumers the full replacement binding.

### E. Compatibility/native authority repairs — bounded breadstuffs lane

Own `exec-lean` plus FFI bridge files listed above and the narrow producer tests. First reproduce the missing installed-policy check through the actual authoritative producer. Then route the corrected canonical semantic evaluator or complete its native program projection; neither restoring Rust as authority nor disabling the policy is closure. If the new runtime cuts this surface over entirely, implement an explicit adapter/rejection boundary and remove the old authoritative endpoint rather than maintaining two divergent program stores.

## Synchronized format and release changes

Do not declare every edit a re-genesis:

1. Adding an otherwise unused FFI constructor is not itself a persisted cell/schema change or a new AIR.
2. New program source format/evaluator semantics requires a source-format version and dispatch identity. Changed accepted semantics needs replay compatibility to be explicitly versioned or refused.
3. Changing canonical cell/program commitment bytes changes stored roots and receipt expectations. Breadstuffs' persistence guard is `persist/src/lib.rs:923`, current `CANONICAL_STATE_SCHEMA_EPOCH = 27`; the corresponding schema-history and refusal tests must move together if that recipe changes.
4. Changed statement/selector/columns/PI shape or emitted constraints changes descriptor/VK identities and any consuming recursive pins. Witness generators, SDK, verifier, fixtures and genesis/deployment manifest must agree on the same identities. Old proofs/old schemas must refuse rather than decode under the new meaning.
5. Fixing an omitted after-cell write changes honest AFTER commitments for that effect. This is a witness compatibility change even when the cell serialization shape is unchanged; measure the actual affected contract rather than copying a stale “epoch required” docblock.

The handoff records standing authorization for devnet VK rotation/re-genesis, and reserves `PROVENANCE.json` stamping to ember. No such rotation, stamping or deployment was performed by this lane.

## Smallest meaningful red/green checks

These are proposed checks, not executed results. Use the unchanged intended production configuration, require the Lean archive, and run targeted release tests in leased remote lanes. Mutating a guard/descriptor for an ablation happens **only on scratch/copies**.

1. **Existing program survives the native producer.** Seed a real cell with a monotone or bounded-field rule, then call `produce_via_lean` on a violating ordinary `SetField`, with oracle installed. Require the precise rule refusal, unchanged cell/root/receipt head, and a subsequent allowed turn. Compare the same request through the normal executor only to locate divergence, not as the acceptance criterion. The existing monotonic oracle test is a fixture source, not this test. Suggested new target: `exec-lean/tests/program_policy_through_producer.rs`.
2. **No same-transaction rule laundering.** Under a prior monotone rule, co-batch a decrement with an authorized replacement to `None`. Require refusal under the explicit prior-rule contract; a standalone authorized upgrade followed by a later request has the separately specified outcome. Exercise owner and delegated permissions, cross-cell target, nested/mixed topology where retained, and rollback of the program itself. Suggested target: `turn/tests/program_install_semantics.rs`.
3. **Actual codec/evaluator consumer.** Encode a realistic PolicyRecord, decode and install it through the same function the native entry calls; invoke an allowed and a forbidden patch. A differing AST, version, domain, prior program, root or args must change the selected result or refuse. Prove codec roundtrip generally, not only by fixture. Run one realistic payload to detect unary/noncomputable traps.
4. **Descriptor binds the claimed program operation.** A valid install proof accepts. Keeping the witness but changing one source byte, the prior program, AFTER program reference, permissions, caller or data write must fail for the relevant check. A mixed `[ordinary effect, SetProgram]` and a program-only request must each be represented. Replacing the source/after-state binding on a scratch descriptor must make the negative test fail. The refinement theorem's premises may not include the entire desired post-state update.
5. **One shell-to-restart journey.** External shell/MCP authors source, installs via canonical authority, invokes an operation, obtains the selected durable receipt; independent readback and process restart recover the same program/source/root/history; a violating invoke leaves all of them unchanged; repeated submission is idempotent. This is the integration bar, not a standalone codec or solver success.

The first two checks can start now to expose the old receiving gaps while the other lanes build the canonical replacement. None is satisfied by changing the test mode to a weaker executor, checking only a scalar digest, or acknowledging a source upload before the kernel installation commits.
