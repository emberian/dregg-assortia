# Policy source revision and capability generation — proposed coherent repair

Status: source-backed design only, no shared representation edits. Current native/controller checkpoint comes first. Intended user behavior still pending ember's answer.

The present `PolicyRecord.version = Request.policyEpoch = AuthState.policyEpoch` both selects source and invalidates capabilities. A successful source update therefore leaves all prior owner and control caps stale. The current strict checks are correctly detecting the consequences of a conflated coordinate; none should be relaxed.

## Exact split

Keep `Capability.policyEpoch`, `Request.policyEpoch`, `AuthState.policyEpoch`, and existing `Capability.Admissible` generation checks unchanged. These identify authority generation, not source revision.

Add `Request.policyRevision : Nat` and `AuthState.policyRevision : PolicyId → Nat`. The complete canonical signed request gains a seventeenth coordinate. Add mandatory `Authorized.policyRevisionExact : request.policyRevision = state.policyRevision request.policyId`. Select `state.policyAddress policyId request.policyRevision`; `PolicyRecord.version = request.policyRevision` remains mandatory. `CanonicalPolicyAdmission.verifies`, registry resolution, witnesses and source availability all use revision. There is no erased wrong-version gate.

Add canonical `AuthorityField.policyRevision policy`. `policyEpoch policy` remains the independently rotatable generation. Existing `policyAddress policy revision` retains versioned content addresses. Use one existing physical policy entry expanded to `(policyId, generation, revision, address)`, so pages and complete-state projection bind both coordinates atomically under one routing group. Current-head APIs read revision/address. A source update preserves generation and changes revision/address exactly; explicit generation rotation preserves source revision/address. No second authority registry/cache.

Birth initializes both coordinates to zero and sources version zero. Owner/control caps remain generation zero. Source revision one then continues to admit their old scopes/time/holder/issuer under the newly selected revision-one predicate. An explicit generation bump makes all prior caps fail the EXISTING exact cap/request/current-generation checks.

The explicit bump semantic operation already exists: `CredentialAuthorityEffects.RotateEpochDeclaration` with `EpochTarget.policy`; `EpochTarget.write` targets `.policyEpoch`. Reuse this operation and extend its concrete page lowering to preserve revision/address. Do not add an alternate revocation engine.

## Source-scope map

* Effect admission owner: `Theory/TypedAuthorization.lean` Request/AuthState/Authorized required fields and universal teeth; `Theory/AuthorizationDeclaration.lean` full wire/field lists/semantic admission vocabulary; associated witness/family lemmas.
* Carrier/emitter owner: `DeclaredHyperedgeArtifact.requestWords`, semantic generated artifact schema/field count/order, every generated output. Old request frames must refuse; no omitted revision→0 fallback.
* Authority owner: canonical AuthorityField, state codec and projection, expanded Entry/entry codec, page framing/root epoch, exact routing, complete Domain/currentHead, grouped source update and explicit generation rotation consumers.
* Policy compiler/registry owners: resolve `(policyId, revision)`, SelectedPolicy/LoadedPolicy current revision proofs, policy membership role revision, compiled `record.version` check, mandatory `Authorized.policyRevisionExact`, Bounded consumer migration. Capability issuer/lineage/possession checks remain unchanged.
* Native signature owner: request frame version and complete request bytes (now seventeen coordinates), actual native signature probes/replay identity; outer snapshot binding preserved.
* Installer owner: Ready successor on revision; derived request reads current generation and revision from the SAME snapshot, old source controls actual final grouped update; source update preserves generation; profile/projection source pins updated.
* Birth/invocation/delegation owners: derive both request coordinates from complete old snapshot; source-zero + generation-zero birth; delegated rights inherit generation; no snapshot host defaults or unrelated content source.
* Runtime profile owner: commit changed request frame/vocabulary, authority page/state schemas and source-selection/projection contract. This is a coherent runtime epoch change, not compatibility mode.

## General statements / teeth

1. Revision replacement preservation: if a capability is admitted under old state/request and only the selected source revision/address changes, updating only the request's revision/root/source binding preserves the capability's semantic authorization obligations (holder/scope/time/issuer/generation/revocations). Actual acceptance additionally requires the NEW selected predicate and actual signature over the NEW request; old signatures/witnesses never transfer automatically.
2. No revision substitution: any `Authorized` request has `request.policyRevision = state.policyRevision policyId`; its selected committed record has that exact revision and canonical content address. If either differs, no accepted token exists. Prove this generically, then current actual receiver refusal for replaying an old signed envelope against the new source snapshot.
3. Explicit generation bump revocation: for old cap generation g and canonical current generation g+1, no admissible request exists using that cap, even if source revision/address is unchanged or predicate is permissive. The existing `stale_policy_epoch_rejected` supplies the essence; exhibit the actual grouped rotation post.
4. Installed source generation frame: successful `preparePolicyAndNullifier` preserves `.policyEpoch id`, increments revision by exactly one, erases retired address and consumes exactly the signed marker.
5. Distinct first-person lifecycle: birth → owner edit under revision0 → authorized install revision1 (generation unchanged) → same owner cap edits under revision1; recipient's previously narrowed cap retains its scope under revision1. Then explicit generation bump makes both old caps fail. Wrong revision, stale signature, unrelated holder, expansion and code-edit-only policy replacement remain red.

No hash injectivity axiom, ≤ generation rule, automatic cap mutation, silent cap reissue, or permission inferred from the new policy is needed.

## Adversarial review additions

Carrier review confirms this is preservation of dynamically governed grants. The capability type does not currently contain an immutable copy of its original `Pred` caveat. A source update may therefore change the current policy that a retained grant must satisfy; this proposal must not be described as retaining the recipient's original-rule consent. If pinned-rule delegation is desired, that needs an explicit first-class caveat/source pin and its existing predicate consumer, not an implied guarantee.

The installer family's mandatory postcondition must retain the unchanged generation alongside new revision/address and consumed marker, so a joint composition cannot silently rotate authority while passing a local source-update proof. Old source authorization remains mandatory. Preserving the generation also does not promise that the replacement policy continues to allow `.installPolicy`; management liveness is a policy property, not automatic authority preservation.

The existing epoch-rotation semantic family is the source vocabulary for explicit revocation, but its actual durable receiving path still needs work. In particular, refreshing control after a generation bump cannot reuse old `IssueEvidence`: that evidence checks the issued capability against the OLD generation. Any simultaneous bump-plus-successor-grant batch needs source-owned preparation and an explicit post-generation issuance law authorized under the old control policy; no signature or issuer cache bypass.
