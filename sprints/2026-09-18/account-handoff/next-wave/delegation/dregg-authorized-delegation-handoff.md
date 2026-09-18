# Authorized delegation — concrete scratch handoff

Status: SCRATCH ONLY. No repository source or live build artifact was changed by this lane. Root has not released the shared representation wave. The patch contains only this lane's three foundation/producer files; it is not the whole coordinated codec/checker/consumer migration.

- Patch: `/tmp/dregg-authorized-delegation.patch`
- Scratch root: `/tmp/dregg-authorized-delegation-draft`
- Exact baseline/source hashes: `manifest.json` under that root.
- Family + State definition checks: `/tmp/dregg-delegation-foundation-checks.json` — green; comment-only corrections followed those recorded hashes.
- Full typed request + ParentLink Entry codec: `/tmp/dregg-parentlink-codec-isolated-checks.json` — authority-owned, green against the isolated new Family/State.
- Shared checker/witness: core-effect isolated green. Effects exact current source: isolated green, SHA `fc5676a9e39733a20856d00e163cda8acf98248c608e4ffcc59b1b089103a152`, empty log.
- Final owned manifest: `/tmp/dregg-authorized-delegation-checks.json`. Standalone axiom audit of 32 declarations is green, using only `propext`, `Quot.sound`, and optional `Classical.choice`. This is not a green whole closure or a working native delegation claim.
- Budget freeze: no new shared representation wave. Ember chose **keep grants and check new rules**; the generation/revision split is decided for the next combined revision+delegation wave. It is not implemented by this scratch patch.

## Implemented semantic carrier

`CredentialAuthorityFamily` adds `delegateVerb`, `LineageOrigin` (`strict` or `delegated (Request kind)`), `ParentLink`, and `DelegationShape`. The shape reuses the original `Capability.Attenuates` payload relation, demands a subject grantor matching the request subject, a subject recipient, the indexed delegate verb, exact singleton child target, parent request scope/cost, grant-time validity, and matching policy ID/epoch.

`Holder.Narrows`, `Capability.StrictAttenuates`, and `strict_attenuation_admits_subset` are unchanged. Proof lineage gains a distinct delegated constructor. `Lineage.IsStrict` and `StoredCapability.IsStrict` make the old same-request root theorem's actual premise explicit through `root_admissible_of_strict`. `Capability.LineageBounds` projects the honest transitive invariants (scope/budget, time, issuer/policy/epochs/root, retained ancestors/channels); it is not another execution relation.

`CredentialAuthorityState.StoredCapability.ancestry` is now `List (ParentLink kind)`. Its `DecidableEq` lives at the definition, replacing downstream duplicate deriving. `LineageValid.root` and `.attenuate` remain; `.delegate child parent tail request parentValid shape` retains the precise origin. Stored validity is structural provenance, not proof that arbitrary bytes were legitimately issued.

## Implemented producer API

`IssueEvidence.slotFresh` keeps its name but now requires shared `CapabilityIdFresh pre cap.id` across all three resource kinds.

`DescentEvidence` factors the canonical parent lookup, exact parent ID, `LineageValid` and `LineageAnchored` for the parent, global child ID freshness, nullifier freshness, exact pre-root, and current/registered/live issuer-policy-revocation requirements. `AttenuateEvidence` extends it and retains the original `strict` field. Existing `acceptAttenuation` parameters are unchanged. Its family postcondition now also requires the exact child's parent chain to remain anchored in the actual post-state, closing the joint-update read invariant.

New source declaration and ambient context:

```lean
DelegateDeclaration kind
  child : Capability kind
  parentId : CapabilityId
  target : ResourceId kind
  expectedPreRoot : Digest
  operationNullifier : Nat

DelegationContext
  domain semantics : Digest
  federation : FederationId
  subject : SubjectId
  subjectKeyEpoch : Epoch
  height : Height
  cost : Nat
  argsDigestBytes : List UInt8 → Digest
```

`context.request codec effectDigest pre.root declaration` builds the complete request. Target, indexed delegate verb, argument digest of the whole declaration, effect digest, nonce, actual authority root, and inherited child policy are derived. Ambient identity is fixed by the receiving source; no host request-to-request callback is accepted. The lawfulness/digest parameters are the existing family boundary, not a hash-injectivity assumption.

`DelegationEvidence domain pre portal context codec effectDigest declaration parent` extends the common descent requirements and adds:

- `parentCommitment : Digest`;
- actual `parentAuthorization : Authorized portal (authState domain pre) exactDerivedRequest`;
- `parentNamed : parentAuthorization.evidence.capabilityValue = some (parent.head, parentCommitment)`;
- `shape : DelegationShape exactDerivedRequest declaration.child parent.head`.

These are mandatory `delegateFamily.ModeEvidence`, including when an accepted token is constructed directly. `acceptDelegation domain pre portal context codec parentCodec effectDigest declaration parent mode` receives no freely substitutable request or outer authorization; it reuses the mandatory parent authorization.

The generated atomic patch writes only the exact child with `delegated exactRequest` followed by the complete canonical parent's suffix, plus the same true operation nullifier. The family postcondition is exact `Patch.ResultAt` and canonical ancestry anchoring in the actual post. This detects a joint post that substitutes or removes a retained parent even when the child write itself remains correct.

## Named theorem surface

Family and State definitions have passed their first isolated proof check:

- `DelegationShape.recipient_is_subject`, `.requires_delegate_verb`, `.no_other_target`;
- `Capability.LineageBounds.refl`, `.trans`, `Capability.Attenuates.lineageBounds`;
- `Capability.Lineage.root_bounds`, `.root_admissible_of_strict`;
- `LineageValid.root_bounds`, `.root_admissible_of_strict`, `.nonempty_lineage`.

Effects proof terms have passed the final isolated check:

- `IssueEvidence.reject_existing_id`;
- `DescentEvidence.reject_existing_child`, `.reject_spent_nullifier`;
- `capabilityProduction_preserves_present` (one general frame theorem for all fresh capability creation);
- `AttenuateEvidence.childLineageValid`, `.childLineageAnchored`;
- `DelegationEvidence.childLineageValid`, `.childLineageAnchored`, `.parent_use_verified`, `.parent_exact`, `.child_bounds`;
- `DelegationEvidence.reject_missing_delegate`, `.reject_non_capability_mode`, `.reject_wrong_parent`, `.reject_wrong_grantor`, `.reject_bearer_child`;
- `delegation_post_capability_exact`, `delegation_post_nullifier_exact`, `delegation_post_lineage_valid`;
- `issue_post_lineage_valid`, `attenuation_post_lineage_anchored` plus the preserved existing strict lineage theorem.

No new axiom or placeholder is introduced. The checked standalone axiom audit retains actual output for all 32 selected declarations. New permanent in-source pins were not installed after the budget freeze; add them from that output during the next coordinated wave.

## Exact consumer migration list

| File | Required migration | Owner/status |
| --- | --- | --- |
| `Theory/CredentialAuthorityFamily.lean` | New explicit origin/shape; mixed proof lineage; strict-only root theorem | This patch; isolated definitions green |
| `Theory/CredentialAuthorityState.lean` | Replace ancestry element; mixed validity; definition-owned `DecidableEq` | This patch; isolated definitions green |
| `Theory/CredentialAuthorityEffects.lean` | Global freshness; common anchored descent; mandatory authorized delegation; actual-post ancestry | This patch; exact current source isolated green |
| `Theory/CredentialLineageAdmission.lean` | One mixed edge decider, full recursive validity+canonical suffix reflection, present-read transport | Core-effect scratch green, separate patch |
| `Compiler/CredentialAuthorityPolicyRegistry.lean` | Reuse mandatory shared stored checker; preserve native current-recipient key use | Core-effect; same public checker interface |
| `Compiler/TypedAuthorizationRequestCodec.lean` | Sole full typed request codec; indexed view retains and checks kind | Authority scratch green |
| `Compiler/CredentialAuthorityEntryCodec.lean` | Encode actual ParentLink/origin/request; remove duplicate StoredCapability deriving | Authority scratch green |
| `Theory/CanonicalAuthorityProjection.lean:24` | Remove duplicate `deriving instance DecidableEq for StoredCapability` | Recorded to authority; not edited |
| `Theory/DeployedMaterializerWitness.lean:45` | Derive Countable Request, LineageOrigin, ParentLink before StoredCapability; qualify/open Family names | Required existence-witness update; not a production codec |
| `Compiler/CredentialAuthorityDomainReceiver.lean:477` | GrantReady uses shared all-kind freshness; existing batchEvidence slotFresh field consumes it | Authority; per-grant type obligation forces change |
| `Assurance/DeployedCredentialLifecycle.lean:284,365` | All-kind root/child freshness proofs; strict parentLineageAnchored; preserve fixture signature-only strict administration | Required fixture update; native portal edits already owned by core-effect |
| `Compiler/CredentialAuthorityPageMaterializer.lean` | New stored layout, page wire 3→4 and old-frame refusal | Authority |
| `Compiler/CredentialAuthorityStateCodec.lean` | Full state wire 2→3 and old-frame refusal | Authority |
| `Compiler/BoundedPageExtensionCatalog.lean` + `Compiler/CanonicalCellRegistry.lean` | Actual authority shard schema 91003/v3→v4 and coherent derived pins | Authority |
| `scripts/probe-authority-domain.lean` | Old negative raw ancestry literal needs ParentLink; already stale for earlier initial-policy/profile ABI | Preserved prior checkpoint; active native fixture supersedes it |
| New concrete delegation receiver + `scripts/probe-born-resource-invocation.lean` | Actual native exact-parent grant, full physical tuple/guards, commit/reopen and Bob invoke | Localfirst; no source edit by this lane |

Definition-dependent refreshes expected without source edits: `Theory/ResourceBirthAuthority` (inherits IssueEvidence), `Theory/ResourceBirth`, `Kernel/ResourceBirthPolicyController`, `Theory/AcceptedCellEffectRequestBinding` (existing strict wrapper remains the same type interface), `Theory/Hyperdocument`, `Theory/HyperdocumentCausalFamily`, `Compiler/CredentialAuthorityPageProbe`, credential wrappers, and the downstream root-owned closure. Text search found no external call to the renamed unconditional root theorem. Root-capability constructors with empty ancestry retain their shape.

The low full request extraction additionally requires authority-coordinated forwarding in `Compiler/DeclaredHyperedgeArtifact.lean` and native-owned `Compiler/CredentialSignatureAdmission.lean`; its byte preservation is a separate checked component. The old object-only compact transport is not used for new origin encoding.

## Honest scope and release order

Core-effect's new witness proves real mixed `LineageValid`/`LineageAnchored`/checker behavior and child semantic admission, including refusal of unmarked holder transfer, orphaned/substituted parents, and a counterexample to unrestricted root admission. It deliberately does not fabricate historical authorization or a native signature. The accepted exact-parent mode's production inhabitation belongs to localfirst's native two-user receiver.

The receiving join must still bind actual unchanged target and selected PolicySource guards, use the complete anchored authority domain, commit child/nullifier atomically, and replay only an exact historical ingress identity before applying fresh current-root/nullifier checks. The theory patch does not itself claim durable commit or a cryptographic deployment.

Release after root's current birth checkpoint: foundation → shared checker → Effects and structural witness consumers → actual codec/version closure → Domain/global freshness → registry → concrete delegated receiver → native Alice→Bob/reopen/use witness. Root owns full closure and commits. Shared source must still match recorded baselines when applying this patch.
