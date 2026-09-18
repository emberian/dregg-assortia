# Mixed delegation checker — frozen scratch handoff

Status: scratch-only. No live source or live `.lake` artifact was changed by this wave. The root stopped representation cutover for the remaining account budget. User chose **keep grants, check the new rules**, with explicit revocation separate from policy revision. That decision is not implemented by these drafts.

## Exact checked sources

`Theory/CredentialLineageAdmission.lean` in this directory is GREEN in an isolated overlay, empty log, SHA256 `da0a6cdd306a4fef71960475816fb0612824c15c8254bc1d6931e996a34f14cb`.

It replaces the old strict-only recursion with one reflected mixed-origin checker. A strict origin requires unchanged `StrictAttenuates`; a delegated origin requires the source Family's `DelegationShape`. `storedLineageCheck_iff` retains its public API and now proves both generalized `LineageValid` and exact canonical parent/remaining-suffix anchoring. It does not interpret serialized origin data as historical authorization.

New general laws include origin shape reflection, no missing delegate permission or bearer transfer, `LineageAnchored.cons`, `.parent_exact`, and `.of_present_reads_preserved`. The latter supports actual joint-post anchoring without requiring equality of the whole authority state. `storedLineageCheck_refuses_parent_substitution` covers changed parent data and changed suffix. Capability-read congruence proves the checker does not reauthenticate historical grantor keys. Global three-kind capability-ID freshness is unchanged and still reflected.

`Assurance/CredentialDelegationLineageWitness.lean` is GREEN, empty log, SHA256 `0f1f93be1729bb3f522f3de273af245520a6197d8e9bc81f0f0e7fe503c3d970`.

It constructs a narrower Alice-to-Bob lineage and a same-holder strict lineage, accepted by the actual shared checker in cells parameterized by any materializer. It rejects unmarked transfer, missing delegation permission, bearer transfer, orphaned lineage, and a well-shaped substituted parent that disagrees with canonical storage. It proves grantor-key-plane rotation preserves historical lineage and gives the counterexample to unrestricted same-request root admission after holder transfer. These are semantic/checker witnesses, not native signed issuance or durable accepted-delegation witnesses.

`DelegationLineageAxiomAudit.lean` and its log are GREEN. All 21 named core/checker/witness statements use only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`, compiled-decision axiom, or cryptographic injectivity premise. Complete attempt records, latest exact source hashes, commands, logs and output paths are in `manifest.json` and `checks.jsonl`.

## Source-only registry draft

`Compiler/CredentialAuthorityPolicyRegistry.lean` is frozen **unchecked**, SHA256 `86b42ea32276a27534c6f8dfe9f6a37729f2dd19717dbc942f3c66bf87edc54c`.

It preserves existing portal/helper signatures and mandatory native current-recipient request authentication. It bumps the full stored-capability commitment customization to `DREGG.AUTHORITY.CAPABILITY/v2` because stored bytes now include explicit origins and complete historical requests. New drafted laws expose data-check invariance under equal capability reads/domain and exact current recipient/subject-key epoch. No helper gate is weakened and no historical signature is rechecked against a new grantor key.

Do not count this entire registry as checked merely because the old live registry passed or the isolated helper passes. Its changed State/Entry/Domain/native dependencies must be emitted coherently. The current affected ancestry is listed in `registry-affected-order.json`; native request forwarding to the low codec should remove the incidental Artifact/ResourceBirth request-encoding dependency.

Two requested proofs remain **unimplemented**, not just uncompiled:

1. `capabilityEvidence_success` / `sourceCapabilityOnlyEvidence_names_parent`: successful helper result must expose the exact stored record at the helper's input identifier and return `evidence.capabilityValue = some (stored.head, storedCapabilityDigest snapshot stored)`. Localfirst needs this for mandatory delegation `parentNamed` without unfolding all checks.
2. `CanonicalPolicyAdmission.admit_preserves_evidence`: success retains the exact supplied evidence. Shell owner reserved the source location, then stopped under the root budget instruction.

## Other owners and scratch dependencies

- Durable callers owns `/tmp/dregg-authorized-delegation-draft/Theory/{CredentialAuthorityFamily,CredentialAuthorityState,CredentialAuthorityEffects}.lean`. Family and State checked successfully before comment-only cleanup; checked source hashes are in `/tmp/dregg-delegation-foundation-checks.json`. Effects subsequently GREEN with this helper, its own exact-parent capability-mode gate, actual-post anchoring, global freshness and 32-law ordinary-axiom audit. Obtain its final manifest directly from that owner.
- Authority owns `/tmp/dregg-authorized-delegation-draft/Compiler/{TypedAuthorizationRequestCodec,CredentialAuthorityEntryCodec}.lean`. Both are isolated GREEN; full Request/ParentLink codec and source compatibility manifests are `/tmp/dregg-parentlink-codec-isolated-checks.json` and the authority handoff. No live representation changed.
- Localfirst owns the future actual native delegation receiver, exact parent capability authorization, physical target/policy observations and Alice-to-Bob invocation. There is no live callable delegation endpoint from this draft.

The request codec still has the current 16 fields. The chosen policy-revision/generation separation changes this contract and its native frame, containing carrier identities and runtime pins in the next coordinated wave. Do not invent a missing-revision default or silently reinterpret these scratch bytes as that future format.

## Resuming safely

`migration.patch` contains this lane's three source deltas against the frozen live baselines. The live helper and registry hashes still exactly match `baselines.json`; the new Assurance witness remains absent from live source. Reconcile the patch with the next revision/generation changes before applying it.

`check-isolated.py` emits only beneath `/tmp/dregg-delegation-core-effect/olean` and rejects output/sidecar symlinks. The overlay uses symlinks for unchanged artifact files, with all planned outputs excluded. A partial `Theory` overlay shadows unchanged imports, so retain the complete safe mirror. Never write through a symlink into live `.lake`. The runner takes a scratch source root and module-relative path, uses the actual lake-selected compiler, and sets two threads. Compiler seats still require explicit coordinator handoff.

All compiler work in this lane has ended. Seat 2 is released; no further checks or live edits are pending in the current account window.
