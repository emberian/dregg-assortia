# Birth / revision / delegation join review — 2026-09-18

Source inspection while the coordinated migration is in progress; not a compiled or runtime verdict. Owned birth source changes have not yet been emitted.

## Reviewed obligations

- `ResourceBirth.factoryRequest` now names the exact current grant generation and current source revision separately. `FactoryAuthorization.policyPinned` selects the address by revision. The root grant payload remains generation zero; it is not silently rewritten to track policy revisions.
- `ResourceBirthAuthority.BatchEvidence` requires absence of generation, revision and initial source address. Its patch and mandatory postcondition install all three; `installs_policy` proves generation0/revision0/address0. Root issues inherit across-kind `CapabilityIdFresh` from actual `IssueEvidence`, because revocation identifiers are not kind-indexed. The new explicit refusal theorem covers existing grants of any kind.
- `ResourceBirthPolicyController.Pending.admitBranch` checks generation and revision independently, resolves immutable source by revision, and forwards both exactness proofs into `CanonicalPolicyAdmission.admit`. Portal lifting retains both. Policy dispatch uses the full canonical request equality, not only target or a digest.
- `CredentialAuthorityPolicyRegistry.loadPolicy` checks current revision, exact grouped policy membership including generation, exact source ID/revision/domain, canonical bytes and derived address. An absent-to-zero sparse state is not enough to select a source.
- `CredentialAuthorityEffects.DelegationEvidence` makes actual exact-parent capability authorization part of mandatory family mode evidence, with `parentNamed` binding its actual capability value. Stored `ParentLink.origin` is first-order history; it is not treated as a signature certificate. New invocation independently uses current recipient key. `LineageValid`/`LineageAnchored` check exact retained parent contents and full suffix. Strict holder narrowing was not weakened to authorize subject transfer.
- Initial resource allocation and source allocation retain exact typed bytes and permanent directory freshness; no root equality is converted into absence by a collision-free-hash premise. Complete authority post pages and catalogue remain covered by the existing installed-byte theorems.
- `PolicyInstallController` preparation targets the resource-derived policy ID, requires the actual current head and successor, and its mandatory postcondition preserves grant generation. Updated source is still authorized under the old source, through the existing control capability and native signature.

## Receiving change

Birth `receiveLoaded` accepts one already-loaded snapshot and calls the new exact-image CAS entrypoint. A concurrent change returns contention instead of reloading under an already-admitted birth. Historical replay still requires identical canonical signed ingress, event and shared nullifier before returning the original receipt.

## Remaining validation

Compile the owned six-module closure after foundational/interface emits; regenerate axiom accounting; rerun actual signed birth-to-invocation after migration, then integrate update/share/recipient journey. This review has not established production profile suitability, whole-system proof soundness, external cloud deployment or the completeness of generic low-level APIs.

## Installer witness inspection

The migrated `scripts/probe-policy-install-receiver.lean` uses a separately bootstrapped resource with generation1/revision1, installs revision2 using its exact original control grant, refuses one owner invocation under the newly selected nonce rule, accepts the permitted owner invocation, then installs revision3 with the same control grant. It checks exact stored owner/control capability payloads after each reopen. Revision3 admits a second actual object mutation and deliberately denies another installPolicy request; the refusal is asserted as policyRejected rather than stale generation. The final physical object value2 and four accepted journal entries are checked, then both old installation requests replay with the original receipts and unchanged image. This is substantive source scope for preserved-grant/current-law behavior, not yet a runtime verdict or a birth-joined witness.

## Actual delegation receiving review

Read both new `Kernel/CapabilityDelegationController.lean` and `Kernel/CapabilityDelegationReceiver.lean`, including all preparation, authorization, family joining, physical lowering, identity and replay branches. No executable bypass identified in the reviewed source. Parent selection is the exact canonical slot; the native helper constructs capability-only evidence for that ID; `parentNamed` is retained inside actual family mode. Across-kind child freshness, source-derived marker, exact current generation and source revision, parent validity/anchoring and holder/delegate scope are mandatory. The complete canonical authority post is compared via injective source encoding to the semantic delegation patch before policy evaluation; the same source tuple feeds acceptance and physical lowering. The target and immutable policy are actual directory observations retained as guards, while whole authority writes and auxiliary shard allocations are checked globally for uniqueness, expected pre-roots and lawful payloads.

A material assurance gap remained: `accepted_authority_post` stopped at the lowering's semantic post and did not prove bytes in the actual `DataSnapshot.install`. Root assigned the frozen receiver proof section to this lane. Added exact installed-write, whole authority-page/catalogue, unchanged target/source, and auxiliary-allocation disjointness laws; these are pending compilation. This is a proof-closure change; the inspected receiving algorithm already had the required freshness/guard checks.

Also strengthened the generic birth batch mode to retain its already enforced global grant-ID distinctness. The new concrete cross-kind witness has distinct typed addresses but a shared revocation ID; its family evidence is now uninhabitable. Existing physical receiving already rejected the collision before this source-contract improvement.

## Final scoped verdict

All eight owned/current receiving closure files were narrowly compiled successfully, with exact source hashes verified after the final build. Birth audit34 and joined delegation controller/receiver audit14 both completed with only `propext`, `Classical.choice`, `Quot.sound`. No native-evaluation or sorry axioms appeared. The new final installed-byte and frame laws are now compiled, not pending. Current-source native birth/update/share/recipient runtime verification belongs to `resume_journey`; it has been unblocked, but this report does not borrow the old pre-migration8056f9b runtime PASS. No full-tree/umbrella or production cryptographic-soundness verdict is claimed.
