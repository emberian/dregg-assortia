# Policy revision / grant generation: independent review

Source review, 2026-09-18. No shared source edits or builds. Reviewed `/tmp/dregg-policy-revision-separation.md` against the current typed authorization, canonical policy gate, installer, complete authority projection, signature admission and replay carrier. Ember's desired default remains unanswered; current implementation behavior is evidence, not accepted intent.

## Conclusion

Separate source revision from grant generation. They answer different questions and the split can represent either user preference: replacing source while preserving generation retains grants; replacing source and rotating generation in one authorized, ordered update invalidates them. Keep exact equality for both coordinates, current-source membership, native invocation proof and old-policy authorization of the change. Do not weaken any existing check.

The proposed split is sound for **grants bounded by immutable capability data and governed by the resource owner's current mutable policy**. It does not preserve the complete allowed-operation set from grant issuance. A revision can make previously denied operations possible inside the same capability scope. That is legitimate only if this is the grant's documented meaning. The current type has no immutable `Pred` caveat or pinned source-revision consent to preserve.

Two independent questions remain: whether grants should follow current rules, and whether changing those rules may intentionally disable further administration. Splitting the counters answers neither implicitly.

## What the current source actually enforces

* `Theory/TypedAuthorization.lean:91,168,207,228,416`: `Request.policyEpoch`, `Capability.policyEpoch` and `AuthState.policyEpoch` are tied by exact equality. Capability admission additionally fixes holder, typed target/verb/cost scope, validity interval, issuer epoch, self/ancestor/channel revocation. Attenuation retains the policy ID and epoch. Every evidence mode passes the common current-policy gate.
* `Compiler/CanonicalPolicyAdmission.lean:316`: `(policyId, policyEpoch)` selects the source, and `record.version = request.policyEpoch` is checked separately alongside domain, semantics, exact canonical record address, actual candidate view and compiled predicate acceptance.
* `Compiler/CredentialAuthorityPolicyRegistry.lean:88,109`: loading uses the complete current snapshot, exact current epoch, grouped entry membership, canonical source bytes and recomputed address. It must migrate to current **revision**, not discard these gates.
* `Compiler/CredentialAuthorityDomain.lean:313,621`: the single `.policy id epoch address` entry simultaneously installs generation and source head. Replacement removes the prior entry's fields. This is the concrete conflation.
* `Theory/PolicyInstall.lean:39` requires source version `old.version + 1` and exact predecessor address. `Kernel/PolicyInstallController.lean:143,356` requires a stored capability with `.installPolicy`, a request-bound native signature and the old selected predicate. Thus the current successful update stales both data-use and controlling grants of that policy.
* `Theory/CredentialAuthorityEffects.lean:461` already specifies exact `nextEpoch = expectedEpoch + 1` with root and unused-marker checks. However the current Compiler/Kernel caller inventory has no production receiver for this rotation; its existing concrete use is the assurance lifecycle exhibit. Reusing the semantics still requires a real grouped physical update and native/durable receiving consumer.

## Required semantic choice: current law, pinned freshness, or immutable grant restrictions

The simplest coherent interpretation of the proposed split is:

`usable = current generation ∧ original cap bounds/lineage/revocation ∧ fresh invocation proof ∧ current resource law(actual pre, actual final post)`.

Example: a delegated `.mutateObject` capability can cover a broad target and verb while revision 0 restricts the actual transition. If revision 1 removes that restriction, the same cap may perform the newly allowed transition after its holder signs a fresh exact request. Scope attenuation remains monotone **under the same current state and request**; no theorem may promote this into temporal non-amplification across arbitrary policy replacement.

The current retained restrictions are finite target/verb sets, `maxCost`, time bounds, lineage and revocation channels. They are not a general caveat language. In ordinary invocation `request.cost` is encoded command length; it is not a conserved monetary allowance. The older `Kernel/Gate.lean` caveat vocabulary is a separate carrier and cannot establish that the typed receiving path preserves immutable predicate caveats.

If the intent instead requires old-rule consent, there are two principled representations:

1. **Pinned freshness:** a cap commits an allowed source revision/address, and use requires the current source to match. Any replacement makes that cap unusable until explicitly renewed. This represents revoke-on-update per grant without confusing source revision with global generation. It must never allow the holder to select an obsolete owner law.
2. **Immutable grant restriction:** capability content commits its own first-order restriction source (including its interpretation/view semantics). Invocation evaluates that restriction **and the owner's current resource law** on the same actual transition. Attenuation retains all inherited restrictions and can add stricter ones; the one `Pred` compiler remains the evaluator. Using only the old source after the owner updates would bypass current law and is not an acceptable pinned design.

Do not automatically copy the entire old resource policy into a caveat: it may include management/version conditions that are meaningless for later operations. An explicit grant restriction is clearer. If immutable caveats are promised, their payload, source availability, interpretation, lineage retention and actual-joint evaluation must be implemented; the generation/revision split alone cannot deliver them.

## Concrete split and exact obligations

The proposed API is coherent:

* Keep capability/request/state `policyEpoch` as grant generation, or rename it consistently to `policyGeneration` during this breaking migration. Keep exact generation checks; never use `≤`.
* Add request/state `policyRevision`, mandatory `Authorized.policyRevisionExact`, and select `policyAddress policyId request.policyRevision`. `PolicyRecord.version` and `PolicyInstall.Head.version` are source revisions. Distinct wrapper types for revision and generation would prevent accidental cross-wiring; their conceptual distinction must hold even if the initial implementation uses `Nat` aliases.
* Expand the one canonical physical policy entry to `(id, generation, revision, address)`. All four coordinates route to one group and project from the same complete old snapshot. An absent/partial head is not a default revision-zero grant. Birth supplies the complete zero/zero/source-zero record explicitly.
* Source installation derives both request coordinates from that snapshot. The old source authorizes the exact candidate update. The new source never approves its own installation. Source version increments once, predecessor matches, generation is framed, the old active address is retired, the marker is consumed, and actual final grouped bytes agree with this one source update.
* Generation rotation retains source revision/address and increments generation exactly once. It is a distinct authorized effect, using the existing rotation semantics. If an operation changes both, execute one ordered batch producing one final policy entry; do not join conflicting same-pre physical writes.
* The actual joint postcondition must retain generation framing as well as final revision/address and marker. Existing generic outcome preservation is useful, but do not make the new invariant a comment beside a head-only postcondition.

A precise grant-preservation theorem should compare capability-relevant projections, not claim all authorizations survive. Freeze or re-prove holder, target, verb, cost and height conditions; preserve issuer and grant generations plus revocation state; retain the exact stored capability and lineage. `Admissible` then transports when only source revision/root coordinates change. Actual re-preparation can change cost or cross expiry, so those premises matter. Complete `Authorized` evidence does **not** transport automatically: new snapshot membership, invocation proof and new-predicate acceptance must be obtained.

The common revision gate must apply to signature and proof modes too, even though those modes have no capability generation to compare. Do not implement revision checking only inside `Capability.Admissible`.

## Administration and explicit revocation

Preserving generation keeps the control cap semantically live, but a newly installed predicate may reject every later `.installPolicy` request. Conversely, rotating the policy generation deliberately kills control caps sharing it as well as ordinary caps. Both outcomes can be intentional, but neither should be sold as a guarantee of recoverability.

A separate management authority is a principled alternative when recoverable ownership is required: canonical state identifies the management policy/control generation that governs changes to this resource's operational policy. The receiver derives that relationship; the caller cannot nominate an unrelated permissive policy. The control cap must explicitly cover `.installPolicy` on this exact target, the old management law must admit the exact source update, and reassignment of management authority must itself be an authorized transition. This can live in the same canonical authority domain and source machinery; it requires no secondary registry or host bypass.

This is orthogonal to the revision split. Giving only control caps a special epoch while leaving ordinary source selection conflated would address self-lockout without resolving the general grant semantics. A native signature alone, a permissive fallback portal, or automatic cap reissue is not management authority.

Before exposing a broad “revoke all grants” action, choose whether it also retires management. If management shares that generation, continued administration needs an explicitly authorized atomic successor control grant or an intentionally separate management generation. The existing `IssueEvidence.policyCurrent` checks the issued cap against the old pre-state generation; a future-generation successor grant is therefore not obtained by simply appending the old issue primitive. It needs an explicit ordered batch whose source judgment ties that grant to the generation actually installed, while retaining old management authorization for the batch. Never reset a generation or delete its head and read absence as zero: that could resurrect old grants. Individual and channel revocation remain unchanged and should never be cleared by policy replacement.

## Signed requests, replay and migration

`Compiler/CredentialSignatureAdmission.lean:44–85,129–170` currently signs exact canonical request bytes in a header containing the old complete authority root, key-registry commitment, key epoch, domain and marker. A preserved cap is not a preserved signature: an old signed envelope must fail after the snapshot/revision changes; an old signature must not be silently reinterpreted against the new rule. The new revision coordinate makes this source choice explicit in all evidence modes, independent of native header details.

There are currently 15 typed request fields plus resource kind = 16 emitted coordinates. The added revision makes 17 emitted coordinates. The migration must update `AuthorizationDeclaration` wire encode/decode/order/check plans and generated schema; `DeclaredHyperedgeArtifact.requestWords`; both compact typed/packed request codecs and receipt encodings; canonical source policy loading/membership; complete authority entry/state/page codecs and routing; runtime `requestSlots` and its semantic pin; signature request frame/domain; every request constructor and generated artifact consumer. Preserve existing stable tags where feasible and append new vocabulary. Regenerate outputs through Lean, not by editing JSON/Rust payloads. Refuse old frames rather than invent omitted revision = 0.

Audit two replay identities separately. `DeclaredResourceController.operationMarker` is stable across changed authority roots/revisions for a given domain/semantics/kind/target/subject/nonce. `PolicyInstallController.requestDigest` currently includes the whole request and is also its nullifier. Adding revision changes that marker. This is not an immediate old-signature replay bypass, but it means “same nonce” does not universally identify one intent across controllers. Preserve and test the intended idempotency contract instead of relying on the shared stable-envelope codec to normalize distinct marker formulas. Journaled event identity must retain the full signed request/source identity. Do not include a new revision in a previously revision-independent marker merely as part of the wire migration.

This is a runtime schema/semantics migration. Existing immutable policy sources commit `semantics`, so a new runtime profile cannot silently reinterpret old sources. Either explicitly migrate a devnet snapshot/source history with provenance, or start a clearly new devnet state. Existing committed decisions and replay receipts remain facts of their original schema. A compatibility decoder that fabricates revision zero or treats the old epoch ambiguously would undermine the separation.

## Required teeth for the next implementation wave

1. Revision update preserves the exact old capability bytes and generation, but a fresh request under the new predicate can either pass or fail. Include a source-permitted loosening example so the dynamic grant semantics is visible, not accidental.
2. A narrowed delegated cap stays narrowed after revision change; expired, over-cost, wrong-holder and revoked caps remain refused. No claim of retained arbitrary Pred caveats until represented.
3. Wrong/current-stale revision fails in every evidence mode; a supplied source with mismatched version/address/domain/semantics fails independently. New-source self-approval of its installation fails.
4. Generation +1 with unchanged source refuses every old-generation cap, including old control grants under the shared-generation design. Reset/absent-head resurrection fails.
5. Old signed envelope, changed revision, changed generation, changed authority root and changed effect each refuse; a newly signed authorized operation succeeds. Reusing its consumed marker returns the existing durable outcome or refuses without another mutation.
6. Birth → ordinary invoke → delegated invoke → install revision 1 preserving generation → same grants re-evaluated under revision 1 → explicit generation rotation → old grants refused, through the actual native/durable receivers.
7. If recoverable management is selected, demonstrate recovery after an operational predicate denies everything; if self-governance is selected, exhibit the intentional management lockout instead of claiming survival from generation preservation alone.

Recommendation: approve the architectural split and these invariants independently of the pending UX default. Record the grant interpretation and management/recovery choice explicitly before asserting what survives an update. The current source provides the necessary atomic preparation, canonical predicate gate and rotation semantics, but the physical rotation consumer and any immutable grant caveats remain concrete implementation work.
