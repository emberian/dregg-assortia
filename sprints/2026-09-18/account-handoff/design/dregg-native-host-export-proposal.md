# Mini native host and shell export proposal

Source/design review, 2026-09-18; no source changes or builds. Ember selected cloud/resource-host lifecycle as Wisper's area; its first runtime/export contract remains open. Recommendation for review: one compiled Lean Mini host with canonical birth, policy-install, invocation and delegation routes. No deployment profile is selected by this document. Bread remains a separately identified runtime. The shell authors policies and typed actions; installing `Pred` is rule programming, not installation of an imperative VM.

## Executable profile and trust boundary

The concrete candidate is a source-owned `NativeHostProfile` over the existing executable `Compiler.BabyBear = ZMod 2013265921` (`EmitSerialize.lean:72–83`), with scalar order width **29**. Its `NoWrap` requirement is inhabited by `PredOrder.noWrap_zmod` and `2^30 ≤ 2013265921`; this proposed instantiation has not been compiled. Width 30 does not satisfy the current construction. This would be a new native deployment profile, not promotion of the `ZMod65537` probe. Retain the **same** `PredCompile.lower`, canonical witness, full-view `castInjOn`, and every-branch actual-input range checks (`CanonicalPolicyAdmission.lean:316`). Present comparisons require `-2^29 ≤ right-left < 2^29`; this is a difference bound, not a blanket operand bound. Report range/cast refusal distinctly. Never truncate integers, rescale token units, disable order or fall back to `Pred.eval`.

The choice has a source-backed reason: BabyBear already has the prime proof, executable field, descriptor serialization and native candidate-compute path. Accepted decision D-0004 permits heterogeneous dialects and rejects a universal execution field. Scalar order cannot use characteristic-two Tower256 unchanged: 0 and 2 alias. Ext6's current proof-side deployment uses noncomputable codecs and is not a substitute executable host (`Ext6GateProofDeployment.lean:1–15`).

Pin the field descriptor, compiler version, width, all receiver projections/codecs, delegation version and factory template into one shared semantics identity. This selects native checked execution; it does not certify a succinct proof backend. Portable policy proofs still need the exact derived descriptor/public-input binding and a checked proof controller, with explicit cross-dialect common-opening relations. For full-width balances/counters, extend the sole compiler with source-bound limbs and carry/order proofs; do not make width 29 an economic workaround.

`HostConfig` is operator-owned, loaded once: deployment/domain, federation, factory pins/template, bootstrap identity, store path, pinned storage/verifier executable identities, custody handle and resource budgets. No request supplies a profile, verifier callback, authority store, field, height or proposed post-state. An explicit admin genesis builder creates the initial keys, factory, policies and conserved Book; ordinary `open` only validates/replays an existing image and checks its profile/domain. The seed is not public mutation ingress.

Use local logical height `genesisHeight + loaded.image.accepted.length`, derived **inside each receiver from the same restored image used for admission**. Pin this clock convention in the runtime epoch; successful new commits advance it, retries/failures do not. Lifetimes then count commits, not seconds or Solana slots. Exact historical replay precedes current expiry checks. Existing receivers accept ambient height parameters, so this requires a coordinated source refactor, not an outer read followed by an independently reloaded admission.

## Public Mini call shapes

Proposed Lean-owned, strictly versioned codecs; these are new APIs, not existing exports:

```text
open(HostConfig) -> Ready(Description) | OpenRefused
prepare(OperationDraft) -> SigningPlan | Refused
submit(SignedMiniCall) -> OperationResult
lookup(original: SignedMiniCall) -> Recorded(Receipt) | Absent | Conflict | Unavailable
read(SignedRead) -> SnapshotView | Refused | Unavailable
events(SignedRead, Cursor, limit) -> EventPage | Gap | Refused
```

`OperationDraft` and `SignedMiniCall` are closed Mini variants `birth | policyInstall | invoke | delegate`, each carrying its own canonical command/ingress. There is no Bread receipt coercion or raw `DataIntent` variant. `Description` reports runtime/profile/domain/codec identities and local durable acceptance boundary, without implying network finality.

`SigningPlan` contains finalized canonical unsigned command bytes, operation identity, exact expected roots, logical height and ordered `(role, selected key/epoch, canonical header bytes)` slots. Clients retain and sign those bytes using real custody; the fixture seed signer is not a product signer. Submission re-derives every request and checks native signatures against committed keys. A prepared plan is not authority or success.

`OperationResult` is `Confirmed(confirmation, Receipt) | Refused(phase, reason) | Contention | Unavailable | Uncertain`. Preserve existing confirmation distinctions: installed, recovered-after-uncertain-response, replayed. A receipt contains original transaction/event identity and historical commit boundary, derived from the retained canonical journal. Keep any later observed boundary separate. Invocation currently exposes an internal recorded intent/snapshot; the export must project a sealed receipt instead.

`lookup` matches the exact original signed ingress through each receiver's replay logic; an occupied ID alone is conflict. After a lost response, resend/lookup those exact bytes. Do not generate a fresh nonce, resign against current roots or translate uncertainty into failure. Preserve refusals without publishing a success record.

`SnapshotView` identifies a canonical image boundary plus resource/schema/root, installed policy address/version and authorized content. Define boundary/cursor as domain/profile, chronological accepted-record index and a domain-separated digest of the actual canonical image prefix. Reads/history need source-owned observe authorization and projection from one `Loaded` snapshot; these query guards and codecs are work to implement. Cursor resume validates that exact prefix; acknowledgement persists a client resume position without inventing a kernel mutation.

## Reuse the actual builders and receivers

- **Birth:** `ResourceBirthController.Concrete.sourceIdentity` and `prepareDraft` derive identity/auxiliary creates; `ResourceBirthPolicyController.Concrete.branchRequest` derives every branch. `CredentialSignatureAdmission.signingHeader` supplies the exact selected-key header. Encode the existing ordered `CredentialBundle`/strict ingress; mutate only through `ResourceBirthReceiver.receive` (`:577`).
- **Policy install:** `PolicyInstallController.declarationCodec`, `request`, `requestDigest` and same-snapshot context derive the successor source/head and signing frame. Submit the existing strict `PolicyInstallReceiver.Ingress` through `receive` (`:625`). The physical source allocation, authority pages and marker are one accepted transaction.
- **Invoke:** `DeclaredResourceController.prepare`/`prepareTuple` derive target and authority requests from command actions and the installed policy. Add a strict codec for the existing `SignedCommand` triple; call the existing `receive` (`:948`). No host effect evaluator.
- **Delegate:** not yet a live callable receiver. Localfirst owns its compact command and receiving adapter; effect/proof owners own exact-parent capability evidence. Proposed command coordinates are kind, subject, parent, target, expected authority/target roots, nonce and child capability. Receiver derives marker/context/requests and validates actual parent possession, attenuation, lineage and installed policy. Enable the route only with this real durable receiver.

`DurableReceiverIO.load/confirm` already canonical-decode, replay and confirm exact journaled intents by physical readback. Reuse its SQLite transport and native signature adapter; Rust only moves bytes or returns opaque native observations.

## Executable, ownership and acceptance

Add a Lake `lean_exe` target `minidregg-host`, rooted at new `Host/Main.lean`; the current lakefile has libraries only. Compile the actual Lean receiver closure and offer length-framed stdio plus a CLI. SSH, Hermes/MCP and Wisper's supervisor transport those calls. Defer in-process C/JNI embedding until lifecycle ownership is implemented; process supervision already fits the proposed Linux host.

Proposed export ownership: this lane—new `Compiler/NativeHostProfile.lean`, `Kernel/NativeHost.lean`, `Compiler/NativeHostCodec.lean`, `Host/Main.lean`; coordinate shared profile/lakefile changes with root. Program/proof owners retain birth/install builders; localfirst retains invocation/delegation; authority owners retain signing and lineage; durable receiver owner retains storage/replay/query-boundary review. No shared file is claimed or edited by this proposal.

Acceptance: initialize real stored keys and a funded internal Book; Alice creates a resource with an authored monotonic policy, invokes it, installs a successor rule and delegates a bounded edit to Bob. Bob's permitted edit commits; decrease, wrong signer, excess delegation and stale-root attempts refuse unchanged. Kill the host after publication before replying, reopen, and recover each original receipt by exact-ingress lookup; changed payload under the same identity conflicts. Read the same state/policy/history and resume the acknowledged cursor. Run through the compiled CLI and actual SQLite/signature adapters. This completes the host brief's first kernel journey; provider reconciliation, external $DREGG lockup and succinct proof deployment retain their own acceptance gates.

## Decisions retained for continuation

Choose the actual native profile and promised integer domain before implementation; BabyBear/29 is the source-backed candidate, while full-width or characteristic-two representations require compiler work. Freeze the Mini-first export with Wisper, including process packaging versus later library embedding, custody/bootstrap ownership, query visibility and logical-clock semantics. Delegation is still pending a real receiver; invocation still needs its complete signed-ingress codec; observe authorization, stable query/cursor codecs and public receipt projection are unimplemented. Current controller/probe results do not discharge these host obligations. No shell/backend deployment, source mutation or new compile was performed during this review.
