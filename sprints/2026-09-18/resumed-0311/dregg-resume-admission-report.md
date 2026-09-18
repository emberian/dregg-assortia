# Current-source admission migration — September 18 resumed sprint

All eight owned files compiled and emitted successfully against the coordinated live generation/revision and explicit-delegation representation. Exact source hashes, commands, exits, timings and archived log hashes are in `/tmp/dregg-resume-admission-source.json`. Full attempt ledger is `/tmp/dregg-resume-admission-checks.json`. No Git operation performed; root owns checkpointing. Compiler seat1 was released directly to resume_host after the final audit.

## Behavior and proof boundary

Canonical policy compilation and source selection now resolve `(policyId, policyRevision)`. `admit` retains exact `policyEpoch` generation equality and additionally requires exact `policyRevision` equality. The selected record's revision, content address, membership, domain, semantics and actual source-derived pre/post predicate evaluation remain mandatory. Its final arguments are `... membershipWitness generationExact revisionExact`.

The mixed-origin checker is the preserved semantic implementation: strict links retain holder narrowing; delegated links require the explicit parent-holder delegation shape. Every parent and remaining suffix is anchored in canonical storage. Historical origin data is not treated as a certificate, and historical grantor keys are not rechecked during descendant invocation. The actual source portal still requires the current recipient's native checked signature, exact complete request and expected marker.

Two missing shared laws are complete:

- `CanonicalPolicyAdmission.admit_preserves_evidence` exposes exact identity of the evidence retained by a successful admission.
- `CredentialAuthorityPolicyRegistry.sourceCapabilityOnlyEvidence_names_parent` exposes the exact lookup at the helper's input identifier and the returned evidence's exact stored head/full lineage commitment. It derives from the generic `capabilityEvidence_success` law.

The latter is implemented by one private checked constructor executing the original semantic/native/membership/issuer/revocation gates and carrying an erased proof of the lookup/evidence relation at the success construction site. Public `capabilityEvidence` keeps its existing signature and projects the same evidence. There is no second gate, duplicated authorization semantics, unchecked endpoint cast, higher heartbeat limit or additional axiom. This replaced an unsuccessful proof that repeatedly unfolded the large proof-dependent gate expression.

The native registry's loaded policy uses current revision and membership of the SAME grouped `(policyId, current generation, revision, address)` entry. Its bounded-page example uses the shared demo's deliberately different generation5/revision11, so the source gate no longer depends on their accidental numerical equality.

## Actual checks

- `Theory/CredentialLineageAdmission.lean`: GREEN, 4.079s.
- `Assurance/CredentialDelegationLineageWitness.lean`: GREEN, 4.240s. Constructive Alice→Bob and same-holder strict lineages; missing permission, bearer transfer, orphaned lineage and parent substitution refuse.
- `Assurance/CredentialDelegationLineageAudit.lean`: GREEN, 3.902s;21 exact axiom pins.
- `Compiler/CanonicalPolicyAdmission.lean`: GREEN, 4.477s, including shared evidence retention and source-generation independence.
- `Compiler/BoundedQuantifiedPolicyAdmission.lean`: GREEN, 3.896s.
- `Kernel/CanonicalPolicyRegistry.lean`: GREEN, 4.096s.
- `Compiler/CredentialAuthorityPolicyRegistry.lean`: GREEN, 4.438s, including exact parent helper and actual native recipient gates.
- `Assurance/CredentialSourceAdmissionAudit.lean`: GREEN, 3.771s;7 exact ordinary-three-axiom pins.

Unchanged `Theory/PolicyInstall`, `Kernel/MultiCellHyperedge`, and `Compiler/PolicyRecordCodec` were also re-emitted for the changed dependency ABI. Existing MultiCellHyperedge linter warnings remain; all eight owned final logs are empty/exit0. No `sorry`, compiled-decide axiom, hash injectivity premise, stale-generation relaxation, or copied historical signature is introduced.

This is a source/compiler/semantic closure. The actual newly issued delegated capability, durable create→replace rules→delegate→recipient invocation journey is owned by resume_journey and receiving lanes and was not run here. Neither native component closure nor these theorem pins resolve the known whole-system STARK statement obligations.

## Files for the root's named commit

- Theory/CredentialLineageAdmission.lean
- Assurance/CredentialDelegationLineageWitness.lean
- Assurance/CredentialDelegationLineageAudit.lean
- Assurance/CredentialSourceAdmissionAudit.lean
- Compiler/CanonicalPolicyAdmission.lean
- Compiler/CredentialAuthorityPolicyRegistry.lean
- Kernel/CanonicalPolicyRegistry.lean
- Compiler/BoundedQuantifiedPolicyAdmission.lean

Earlier failed check outputs were initially overwritten by the runner's reused log path. Their original exit/source/timing records are retained and now explicitly marked with no archived log rather than pointing misleadingly at a later green. Final passing outputs have unique source-qualified paths and hashes. The final source manifest contains only the eight actual current-source successful measurements.
