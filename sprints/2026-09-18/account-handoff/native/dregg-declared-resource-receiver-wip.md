# Declared resource receiver checkpoint — 2026-09-18

Owner: /root/sprint_localfirst. Root owns Git and compiler scheduling. This lane has used only its authorized narrow two-thread Lean seat and existing native binaries; no Git, full builds, or SSH.

## Current state

- Kernel/DeclaredResourceController.lean and scripts/probe-declared-resource.lean compiled cleanly and the actual native bootstrap invocation probe passed. Both sources remain frozen for root checkpoint.
- Thirteen codec/page/joint-post/native-ingress/read-guard theorems were axiom-audited: only propext, Classical.choice and Quot.sound.
- The shared identity-pin dependency chain Replay → RuntimeProfile → lower birth → upper native admission → physical Receiver is now GREEN/fresh. This lane re-emitted the unchanged ordinary controller against that complete chain: exit 0, empty /tmp/dregg-declared-resource-current.log.
- New scripts/probe-born-resource-invocation.lean compiled and actually ran successfully through the native verifier/signer/SQLite binaries: first run exit 0 and PASS, preserved in /tmp/dregg-born-resource-invocation-native-first.log. This is actual accepted paid birth → physical reopen → issued-owner invocation → physical reopen, not a bootstrapped owner substitute.
- The final focused rerun also PASSED: session 73791 exited 0 and /tmp/dregg-born-resource-invocation-native-final.log contains PASS. Exact original birth replay at trusted height 20000, beyond the original key and issued-owner expiry, returned the original receipt and preserved byte-identical stored state. Alice-to-Bob delegation remains outside these results and awaits the approved stored authorized-edge semantics.

## Receiving contract implemented

1. Compact strict framed Command directly transports existing DeclaredActionLowering.Action constructors. It never evaluates the old unary Action.code/Declaration.code codec. Canonical whole-frame re-encoding rejects aliases; full target and authority roots remain intact.
2. The actual target is selected from the complete loaded directory by CanonicalCellRegistry.selectDeclared. The same image supplies the fixed complete authority catalogue/shards and deterministic immutable PolicySource cell. Policy ID comes from the actual target; no host policy map, authority projection or proposed post is accepted.
3. Existing Page.applyWrites computes the candidate. Carrier-owned general Page.applyWrites_checked proves correspondence to the same ordered checked-write semantics, including sparse presence and sequential guards. Physical page roots are not confused with functional effect roots. Object/program edits are supported; account money is explicitly routed out to the canonical Book family, never shadow metadata balances.
4. The source operation marker hashes domain, common runtime semantics, resource kind/target, subject and nonce. Actions, roots and cap ID cannot manufacture a new marker for the same coordinates. Domain.nullifierEdit plus the shared physical lower groups changed shards and allocates only source-derived auxiliary pages.
5. Raw two-incidence PreparedTuple precedes portals. Policies observe the exact final target page and complete authority candidate. Native signatures bind each incidence’s exact root and the same full command/marker; the signing client generates the pair.
6. Capability ownership is required in the actual evidence type: sourceCapabilityPortal/sourceCapabilityOnlyEvidence have empty signature-only/proof-only alternatives. CheckedLeg retains actual private native receipt, equality to input envelope bytes, and literal source authorize result. AcceptedInvocation has a private constructor.
7. Exact accepted-post proofs connect semantic page/authority results to the computed physical write plan. Its DataIntent requires the private accepted token and actual unique-ID, pre-root, permanent-law and complete read-guard checks. There is no fake handler/Unit commitment theorem.
8. Shared CredentialAuthorityReplay.nullifier uses one domain/semantic-marker namespace across operation kinds. Journal lookup checks exact transaction identity, full original signed ingress and marker before fresh root/nullifier admission. Matching returns only the prior receipt; changed same-coordinate ingress conflicts.
9. Publication uses existing DurableReceiverIO.receive and actual physical readback. Admission refusal performs reads but no write/publication.

The elaboration hotspot was portal expansion into the common cSHAKE semantics while constructing CheckedLeg. A local irreducible annotation on the already-defined portal fixed it at default heartbeats. No executor, policy, theorem premise or receipt check changed; no sorry or new axiom was introduced.

## Measured evidence

- Shared replay helper: exit 0, empty /tmp/dregg-authority-replay-helper.log; source owner authorized the isolated prerequisite emission.
- Original receiver: exit 0, empty /tmp/dregg-declared-resource-controller.log.
- Original probe source: exit 0, empty /tmp/dregg-declared-resource-probe-check.log.
- Thirteen-theorem axiom audit: exit 0, /tmp/dregg-declared-resource-axioms.log.
- Actual native invocation: exit 0 and PASS, /tmp/dregg-declared-resource-probe-native.log. Real enrolled Ed25519 keys, stored Alice cap and physical installed policy source; target field mutation and authority marker persisted in one publication and survived native reopen; exact retry replayed; changed same-nonce ingress conflicted. Request tamper, valid Bob signature using Alice’s cap, stale target root, out-of-target write and object-to-program write refused while preserving byte-exact physical image. This fixture bootstraps the object/cap/policy and does NOT claim accepted birth or delegation.

Native paths: /tmp/minidregg-credential-signature-verifier-target/release/minidregg-credential-signature-verifier; sibling examples/sign-probe; /Users/ember/dev/minidregg/native/hyperdocument-link-sqlite-store/target/release/minidregg-link-sqlite-store. Probe field is proven ZMod 65537 with scalar width 15, explicitly a probe parameter, not a production field selection.

Frozen SHA256: receiver 38d062e33f55295179ebdd1b208ba42c06decc343f1cf4aaff2c989f372cffeb; original probe ebea6582fe071180cd7d448fb2345eefcedc51d5f5028364b16c6fb7eaffb7a5.

## Joined born-resource probe — final actual native run passed

Uses actual ResourceBirthReceiver.receive through the complete source-derived per-incidence signed bundle. Bootstrap includes deployment/factory/Book and Alice’s existing fee capability and their governing policy sources; it explicitly checks newborn, owner/control grants and newborn policy source absent. Actual birth must publish all of them. The test then opens that image and uses its actual issued owner cap and selected source to invoke the actual born object.

Passed checks: fee7 moves payer100→93 and collector0→7 through the real Book, conserving total; feeDebit admission lane agrees; exact birth retry does not alter any stored bytes/charges; Bob cannot use the actually issued Alice cap; owner invocation survives reopen; original birth and invocation receipts both replay after later state changes without charging again. Identity uses Concrete.sourceIdentity over domain/runtime/factory/creator/nonce. An enrolled Bob exact native factory signature cannot reuse Alice’s coordinates: receiving rejects specifically preparation.identity. Changed payload with unchanged creator/nonce coordinates conflicts with the prior full ingress. Noncanonical trailing bytes also refuse; all refusals preserve byte-exact physical state.

First-run source SHA256: 6fc257c6d6488c7ba204c235a13bef145349403b9d2d2718c679273f2a0ad257. That artifact predates only the final expired-credential replay assertion. Final checked source SHA256: bd4c812c7cd2d3997adf378fbf4c2fceefd5b1d45a1a4453a95c0fd40abcd6ab. The first runtime was confirmed executing main (read-only sample in /tmp/dregg-born-resource-invocation-sample.txt), initially roughly 530 MB resident footprint and one busy core; a later sample of the final run was roughly 3.1 GB. No claims about compiled native Lean executable performance follow from this interpreted `lean --run` probe.

Exact final command, cwd /Users/ember/dev/minidregg:

```sh
LEAN_NUM_THREADS=2 lake env lean --run scripts/probe-born-resource-invocation.lean /tmp/minidregg-credential-signature-verifier-target/release/minidregg-credential-signature-verifier /tmp/minidregg-credential-signature-verifier-target/release/examples/sign-probe /Users/ember/dev/minidregg/native/hyperdocument-link-sqlite-store/target/release/minidregg-link-sqlite-store > /tmp/dregg-born-resource-invocation-native-final.log 2>&1
```

Exact native executable SHA256 values used:

- Verifier: 3cac3584c9bcf46bf54d19d298cadd568b24df57e19fecd9dfca19dbaee700ad.
- Public-test-key signer: 3a2ee794ed7abd35a75baf2394bb84b1bb8382a86348a0a14bc4ae66204f17c1.
- SQLite store: 6c716da59969563cb9ddbe71a25370bbe9db8de13670fabaac5abe8a2ed42a03.

This is a native signed fixture with a temporary actual SQLite store and test keys. The fee is the canonical Book accounting exercised by the source receiver; this probe neither transfers on-chain tokens nor establishes a production field/profile or participant-node service.

All three owned source files are frozen. Seat 1 was explicitly released to core_authority_pages, who handed it to the policy installer receiver queue. No process remains from this lane. Root owns checkpoint/push; next work is approved mixed-lineage foundation and its actual delegation receiver. Do not weaken StrictAttenuates or use bearer/synthetic-cap workarounds for holder transfer.
