# Explicit authorized delegation — source design, 2026-09-18

Status: design and source review only. No shared source edited and no build run for this task. The names below are proposed interfaces for owner coordination, not declarations already present or proven. Read against the current sources while the signature, policy-source and authority-key lanes are changing them.

## Decision

Keep `Holder.Narrows`, `Capability.StrictAttenuates`, and `strict_attenuation_admits_subset` exactly as they are. Add an explicit subject-to-subject delegation transition. It consumes an **actual capability-mode authorization using the exact parent**, under the indexed delegate verb, and produces a narrower child whose holder is the recipient. Alice remains the grantor; the child retains the parent's original issuer, issuer epoch, policy, root, ancestors, and channels. This is authorized production of authority, not holder inclusion.

Use one canonical stored lineage with explicit edge provenance and one shared executable checker. Do not reinterpret every holder change as an ordinary attenuation. Do not fix the demonstration with a bearer capability, an unrelated signer, an admin signature-only `Authorized`, or a weakened holder predicate.

The concrete receiver should implement the exact shape localfirst confirmed: request target is the parent/child resource, request pre-root is the complete canonical authority cell root, request verb is the resource-kind-indexed delegate verb, and the child target set is exactly that singleton. The actual unchanged target cell and selected policy source are also physically observed/guarded. One request for X cannot mint a child over Y.

## What the source says today

- `Theory/CredentialAuthorityFamily.lean:101`: holder narrowing is universal subject inclusion. Thus `.subject Bob` narrows `.subject Alice` iff Bob=Alice; subject→bearer is also correctly rejected.
- `Theory/TypedAuthorization.lean:228`: `Capability.Attenuates` already expresses all required payload bounds except holder. It preserves parent/root/issuer/policy identity and epochs, narrows target/verb/cost/time, exactly adds the parent to ancestors, and only adds revocation channels.
- `Theory/CredentialAuthorityFamily.lean:145`: `StrictAttenuates` adds holder inclusion. Its same-request subset theorem is correct and must survive unchanged.
- `Theory/CredentialAuthorityFamily.lean:164` and `Theory/CredentialAuthorityState.lean:157`: both proof lineage and stored-lineage validity currently admit only roots and strict edges. Their unconditional `root_admissible` theorems are false for Alice→Bob mixed lineage. A valid Bob invocation is deliberately not a valid Alice-root invocation by Bob.
- `Theory/CredentialAuthorityState.lean:51`: stored ancestry is currently just a list of parent capability values. There is no explicit distinction between strict and holder-transfer edges.
- `Theory/CredentialAuthorityEffects.lean:220`: attenuation mode opens the exact current parent and validates strict lineage, freshness, epochs and revocations. `acceptAttenuation` at line271 accepts an independently supplied outer `Authorized`; it does **not** require that this authorization be capability-mode evidence naming this parent. It is an administrative strict-narrowing operation, not an authenticated Alice→Bob delegation gate.
- `Compiler/CredentialAuthorityPolicyRegistry.lean:170`: current capability binding opens the exact typed stored head and commits complete stored ancestry. At the inspected source checkpoint it did not yet validate ancestry semantics. Core-effect is now assigned the shared reflection/checker and mandatory registry use.
- `Compiler/CredentialAuthorityPolicyRegistry.lean:296`: native capability use requires a current exact-request signature by the subject holder; bearer use correctly refuses. `sourceCapabilityEvidence` uses this source portal. Preserve that behavior for both Alice's delegation and Bob's subsequent invocation.
- `Compiler/CredentialAuthorityEntryCodec.lean:186`: stored-capability encoding currently serializes head plus the old parent list. Changing stored lineage requires a real codec/wire migration; an out-of-band host annotation is insufficient.

## Minimal semantic and stored representation

Put the first-order relation/edge types in `CredentialAuthorityFamily` or a foundation module importing it, before `CredentialAuthorityState`; do not create an Effects→State→Effects cycle.

Proposed data shape:

```text
LineageOrigin kind
  = strict
  | delegated (request : Request kind)

ParentLink kind = { parent : Capability kind, origin : LineageOrigin kind }
StoredCapability kind = { head : Capability kind, ancestry : List (ParentLink kind) }
```

Roots still have an empty ancestry list. Strict derivation prepends `{parent.head, strict}`. Delegation prepends `{parent.head, delegated exactDelegationRequest}`. The remaining ancestry is copied exactly from the canonical parent. This replaces the old parent-list representation; there is no parallel accepted lineage format or separate authoritative host side table. The full existing `Request` codec is reusable for the new origin payload.

The complete request in a delegated link records the actual operation that produced that edge. Its presence is **not** a self-authenticating certificate. A pure lineage checker verifies structural/semantic consistency; source-owned accepted state transitions and durable history establish that the operation was authorized. This distinction already exists for root capabilities: a syntactically valid root record is not proof somebody legitimately issued it. Do not name an unchecked `authorized : Bool` or turn a consumed nullifier into such a certificate.

Define a candidate-independent `DelegationShape request child parent` proposition with mandatory fields:

1. `child.Attenuates parent` (reuse the existing relation, including exact issuer/policy epochs and full ancestor/channel constraints).
2. `parent.holder = .subject request.subject` and `child.holder = .subject recipient` for an explicit recipient. Rebinding does not change `child.issuer` to the grantor or recipient.
3. `request.verb = delegateVerb kind`, using one source-owned indexed dispatch.
4. `child.scope.targets = {request.target}`, and the parent scope covers this delegation request, including its delegate verb and cost.
5. The recorded grant time is inside the parent's time window, and request policy ID/epoch agree with the parent. Current epoch/revocation/key checks belong to actual admission at creation; they cannot be fabricated from this historical record.

The strict edge branch still requires `StrictAttenuates`; the delegated branch requires the distinct shape. Same-holder explicit delegation is allowed if it actually went through this operation, but neither branch silently classifies an unmarked holder change.

The exact argument/effect binding is established by the accepted delegation constructor from a full first-order declaration. Do not recursively hash a stored origin containing its own digest: derive argument/effect addresses from the declaration (child head, parent ID, target, old authority root, nonce), derive the complete request, then construct the stored origin from that request. The origin is a deterministic result of this source shape. The complete old root binds the exact parent record and suffix used as the family outcome.

## One lineage checker, with source anchoring

Generalize the existing proof lineage and stored `LineageValid` to explicit strict/delegated edges. Preserve the existing root and strict constructors where practical; add the delegated constructor rather than weakening the strict one.

Add a strict-only predicate (`Lineage.IsStrict` and its stored counterpart), and restrict the old same-request root theorem to it, e.g. `root_admissible_of_strict`. Keep the one-edge `strict_attenuation_admits_subset` unchanged. For mixed lineage prove the honest general laws: root scope/budget bounds, inherited issuer/policy identity and epochs, time narrowing, retained full ancestors, and inherited revocation channels. Do not claim the root holder authorizes the recipient's same request.

The shared source checker should additionally anchor every retained parent/suffix to the actual canonical capability lookup. Proposed specification:

```text
LineageAnchored pre stored:
  for each retained ParentLink(parent, origin) and remaining suffix,
  readCapability pre kind parent.id = some {head := parent, ancestry := suffix}

storedLineageCheck pre stored = true
  iff LineageValid stored ∧ LineageAnchored pre stored
```

This checks the whole chain, including its terminal root, against the complete authority snapshot. It prevents a well-shaped but substituted parent copy, orphaned ancestry, or self/duplicate-ID chain from being accepted merely because its bytes were hashed. At creation, `parentExact` and the checked parent chain give this property for the newly stored child; capability records remain immutable and fresh-only while revocation lives in its own plane.

Core-effect owns `Theory/CredentialLineageAdmission.lean`, already drafted with reflected `Scope.Narrows`, `Holder.Narrows`, `Attenuates`, and `StrictAttenuates` helpers. Extend that one module with the approved origin relation and recursive stored checker. Localfirst reuses its returned proof in delegation mode; the registry reuses it in `capabilityCheck`/`CapabilityBound`, and consequently in `sourceCapabilityEvidence`. There must not be an endpoint-local second checker or a weaker invocation checker than creation uses.

Do not re-run the historical grantor signature against the *current* grantor key or require its historical nullifier to be fresh during descendant use. An Alice key rotation after a valid delegation should not silently revoke Bob. Current Bob invocation authenticates Bob's current selected key; explicit parent/ancestor revocation and issuer/policy epoch changes still invalidate the child under existing admission semantics. Historical signature provenance is retained by the committed operation/history, not recreated from current-key admission.

## Mandatory accepted delegation gate

Add `DelegateDeclaration kind` and `delegateFamily` alongside the semantically distinct strict attenuation family. Reuse common freshness, canonical-parent, nullifier and inherited-revocation checks rather than cloning them without a common specification. The declaration contains the child head, exact parent ID, target, expected complete authority root and operation nullifier. Ambient domain/semantics/federation are deployment-owned; the request is computed by the source receiver, not accepted as a free callback or reconstructed from untrusted request fields to obtain `rfl`.

The mandatory delegation mode must contain:

- Exact canonical parent lookup and full shared lineage check.
- Actual `Authorized` for the source-derived complete delegate request, under the same complete authority state and same portal.
- A proof that **that authorization's evidence is capability mode naming this exact parent and its exact source commitment**. A signature-only token, proof-only token, or another capability is insufficient even if its unrelated request passes policy.
- `DelegationShape`, child freshness, nullifier freshness, current issuer/policy epochs, and all registered/live self, ancestor and channel checks.
- The exact source-derived stored child/origin and a validated atomic patch which installs that child and consumes the same operation nullifier.

This constraint must be in the family mode/accepted type. Merely adding a check to a convenience `acceptDelegation` function leaves a public `AcceptedCellEffect` constructor bypass. A practical minimal arrangement is to parameterize the delegation family by its portal and put the exact parent `Authorized` and evidence-name proof in `DelegationEvidence`; the receiving constructor uses the same authorization value for that mode and the outer accepted token. Having an unrelated outer token then cannot replace the required inner parent grant. There is still only the existing `Authorized` judgment and canonical policy gate.

The child slot must be fresh **across all resource kinds**. Storage uses `(kind, CapabilityId)` while revocation uses `CapabilityId` alone. The inspected `AttenuateEvidence.childSlotFresh` only checks its own kind. Use one shared global capability-ID freshness predicate/checker for new authority production; do not add another local interpretation. Coordinate the root-issuance batch consumer too: per-descriptor `GrantIdsDistinct` only settles duplicates within that descriptor, not a preexisting other-kind capability.

At the physical join, the resulting authority-domain update, nullifier, target observation, policy-source observation, and every changed/unchanged authority dependency belong to one source-derived tuple. Existing Domain lowering computes internal shards and exact read guards. No early in-memory grant, sequential side install, or policy-free raw authority write is a valid implementation.

## General acceptance obligations and witnesses

Every item below should be a named general theorem with ordinary axiom accounting; closed native probes supplement these statements and do not replace them.

1. **No parent substitution:** accepted delegation retains exact canonical parent membership and the exact parent capability-mode authorization for the full source-derived request.
2. **No unearned delegate permission:** if the parent lacks `delegateVerb kind`, or its holder does not cover the authenticated grantor, no accepted delegation exists.
3. **No payload amplification:** accepted child targets/verbs/budget/time narrow parent; issuer/policy/epochs/root remain equal; complete ancestors and channels remain inherited.
4. **No subject-to-bearer laundering:** the new native delegation operation produces only an explicitly named subject holder. Existing strict holder rejection remains a theorem.
5. **Exact post and frame:** success installs the exact child+origin and consumes exactly its nullifier; all unrelated fields remain unchanged. Failed admission exposes no child or consumed marker.
6. **Lineage preservation:** success produces valid, canonically anchored mixed lineage. Root issuance supplies the base; strict and delegated steps preserve it. Use existing accepted-effect/history machinery for reachable-state provenance rather than inventing a second ledger.
7. **Transitive withdrawal:** any inherited ancestor/channel revocation or stale issuer/policy epoch rejects descendant use, including across subject transfers.
8. **Recipient authentication:** public child/parent bytes do not produce Bob invocation evidence. Bob must supply the exact native signature under Bob's current canonical signing key; Alice's or a substituted signature refuses.
9. **Strict theorem retained:** a strict-only lineage still implies root admission for the same request. Provide the Alice/Bob counterexample to the unrestricted mixed-lineage claim so that it cannot be accidentally restored.
10. **Exact replay:** the fresh path rejects consumed nullifiers; a lost-reply retry can only return the exact previously committed request/commit identity or be reconstructed against its retained old snapshot. An arbitrary spent marker is never success.

Concrete positive witness: issue Alice an object owner cap over X with `{mutateObject, delegateObject}` and cost/time bounds; install Alice and Bob's current canonical signing keys; Alice signs the exact delegation under her parent; source policy admits it; one durable transition records Bob's child with `{mutateObject}`, narrower budget/time, parent/root/full ancestors; reopen; Bob signs and invokes the child; verify the actual target change and provenance. A second positive mixed chain may let Bob further delegate only when Alice retained the delegate verb in Bob's child.

Negative witness matrix: Alice→Bob through strict branch; parent without delegate; wrong signer or signature-only mode; wrong parent ID/commitment; edited recipient/child payload after signing; target X request with Y child; widened budget/time/verbs or changed issuer/policy/epoch; removed ancestor/channel; missing/substituted parent record; duplicate ID in another kind; replayed nullifier; stale Alice key at *creation*; revoked parent before/after creation; Bob invocation signed by Alice; unsupported bearer; expired child. A post-creation Alice key rotation with Bob's current key should remain a positive case unless an explicit separate issuer/policy/revocation change withdraws authority.

## File ownership and dependency order

| Area | Minimal source change | Owner coordination |
| --- | --- | --- |
| `Theory/TypedAuthorization.lean` | Shared indexed delegate-verb helper if not already defined; preserve `Attenuates`, holder semantics and mandatory capability-use verifier. | Core-effect |
| `Theory/CredentialAuthorityFamily.lean` | First-order origin/shape, generalized proof lineage, strict-only theorem, honest mixed payload bounds. | Root assigns semantic owner before edits |
| `Theory/CredentialAuthorityState.lean` | Replace ancestry element with ParentLink; generalized stored validity and canonical parent anchoring. No separate authority plane needed. | Coordinate authority-key owner |
| `Theory/CredentialAuthorityEffects.lean` | Explicit delegate declaration/family/mandatory mode; shared checks; source-derived stored origin; post/frame/lineage laws. Preserve strict path. | Root assigns semantic owner |
| `Theory/CredentialLineageAdmission.lean` | One executable checker and exact iff proofs, including mixed edges and canonical lookup. | Core-effect, already reserved |
| `Compiler/CredentialAuthorityEntryCodec.lean` and page/full-state/version pins | Canonical edge-tag+existing Request encoding, exact roundtrip/separation; explicit version update; reject unsupported old bytes. Capability digests commit all new bytes. | Authority owner |
| `Compiler/CredentialAuthorityPolicyRegistry.lean` | Mandatory shared chain proof in `CapabilityBound` and source capability use. No optional lineage mode. | Core-effect |
| `Theory/Hyperdocument.lean`, credential wrappers and strict fixture consumers | Use generalized checked lineage for actual principals; retain strict-only premises where same-request monotonicity is claimed. | Route exact fallout after source freezes |
| New concrete delegation receiver and native witness | Full compact descriptor, selected parent source evidence, complete policy tuple, one physical update, durable reopen and Bob invocation. | Localfirst |

Freeze the data/relation/codec choice before shared checker and consumer edits. Then check targeted dependency order with two threads: semantic foundation → stored state/effects → shared reflected checker → codecs/domain → registry → concrete delegation → native two-user witness. Root owns the full closure, checkpoint and push. This design task performed no builds or source edits.
