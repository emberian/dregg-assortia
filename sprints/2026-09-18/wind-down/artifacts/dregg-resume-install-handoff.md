# Resume installer lane — native recurring-owner journey verified

Status: completed focused implementation and checks; all four owned files frozen. Main loop owns Git. Seat 2 released; no running compiler or runtime process. Exact sources/checks are `/tmp/dregg-resume-install-checkpoint.json`.

Owned files:
- `Kernel/PolicyInstallController.lean`
- `Kernel/PolicyInstallReceiver.lean`
- `scripts/probe-policy-install-receiver.lean`
- `scripts/probe-credential-capability-use.lean`

## What now works

The controller separates exact grant generation from signed source revision. The original selected source authorizes its own replacement. The grouped authority update advances revision/address and retains generation; the mandatory semantic-family postcondition also retains generation under composition. `Installed.generation_preserved` and `Installed.capability_preserved` are checked general theorems. The latter proves that every capability field (all kinds and IDs) is unchanged by the actual source update, so continued use is not manufactured by reissue. Both standard-axiom pins pass.

The physical receiver derives both coordinates from one loaded authority snapshot and selects the old immutable source by revision. Its physical authority post carries the exact generation/capability preservation laws. `receiveLoaded profile deployment native transport durable federation height bytes` invokes root's pinned-image CAS, with no silent rebase onto a newer journal. Existing `receive` loads once and delegates. Original-byte historical receipt replay precedes fresh admission.

Ember explicitly selected deliberate self-governing management, including potential permanent lockout. The probe labels this intended behavior; there is no owner repair bypass.

## Actual checks

Controller and physical receiver emitted GREEN, empty logs. Expanded native probe compiled GREEN and **actual Ed25519 + SQLite run exited 0**. It checks occupied/retired source IDs, missing old source, code-only capability, copied capability without key, and the old policy denying replacement. The successful journey discards the native success reply and recovers by exact readback, checks immutable old/new source bytes and one exact charge, and exercises two successive replacements with the same original control grant. The same original object grant performs actual mutations under source revisions 2 and 3. A request denied by revision 2 becomes allowed under changed revision 3; no grant payload changes. Final journal is exactly four entries (two installs plus two owner mutations). Self-governing management lockout rejects through the actual policy while grants remain current. Both original installation receipts replay at height 20000 (past key and grant expiry) with a missing verifier and unchanged physical image/accounting.

All **26 public PolicyInstallReceiver theorem axioms** audit to subsets of propext/Classical.choice/Quot.sound; no sorryAx/native-decide/hash-injectivity axiom appears. The controller's installed generation/capability pins are inline.

The older capability-use probe is migrated to current grouped Entry.policy, current snapshot generation/revision/subject epoch, and explicit strict ParentLink origin. It compiles and its **actual native matrix exits 0**: exact policy-control succeeds, code-only, changed nonce, copied key, altered/wrong-kind capability, wrong root/role opening, self-revocation, stale issuer/generation, and malformed ancestry refuse. This remains an accepted semantic token fixture, not a claim of durable commit.

## Scope and exact evidence caveat

This install fixture bootstraps its owner/control grants and object. The joined born-resource → update → delegation provenance witness is owned by journey; this lane does not claim it. F=ZMod65537 and order-width15 remain probe parameters, not a production field selection or STARK statement claim.

The repeated-install run captured a 128-file local import closure. 127 stayed byte-identical; `Kernel/DeclaredResourceController.lean` changed concurrently for the strict signed-ingress codec factor requested by semantic history. The actual run consumed the previous emitted controller SHA `ca22fd70077620c6bc16990ca2eb7537d9eb12c3c217b921adc75636b3a26918`, preserved exactly at `/tmp/dregg-declared-before-history-codec.lean`. Birth-review reports no admission/receive edits and owns `signedBytes_wire_unchanged`; its eventual check is separate from this runtime evidence. Do not silently relabel this native result as having executed the later refactor. All 124 local source hashes of the legacy native matrix remained identical.

Attempt 1 of the new native probe correctly refused its second install because my fixture used global wire verb ordinal10, while the actual runtime predicate slot uses kind-local EntryCodec verbTag4 for installPolicy. I replaced the fixture's raw verb literals with the actual typed encoder; no production gate changed. Both failed attempt source/log and passing rerun are preserved.

## Evidence

- `/tmp/dregg-resume-install-checkpoint.json`: exact four owned hashes and all check results.
- `/tmp/dregg-resume-policy-install-controller.log`, `/tmp/dregg-resume-policy-install-receiver.log`: module greens.
- `/tmp/dregg-resume-policy-install-probe-check.log`: expanded probe source green.
- `/tmp/dregg-resume-policy-install-native.log`, `...-native-sources.json`, `...-native-source-stability.json`: actual recurring-owner result and exact attribution.
- `/tmp/dregg-resume-policy-install-axioms.lean`, `...-axioms.log`: all26 public receiver theorem audit.
- `/tmp/dregg-resume-capability-use-check.log`, `...-native.log`, `...-native-sources.json`, `...-source-stability.json`: legacy migrated negative matrix.
- `/tmp/dregg-resume-policy-install-native-attempt1.log`, `...-attempt1-sources.json`: truthful initial fixture failure.

No further checks are queued in this lane. Explicit grant-generation rotation receiving work remains separate ownership.
