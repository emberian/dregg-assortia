# Physical policy installation checkpoint — 2026-09-18

The actual receiving module `Kernel/PolicyInstallReceiver.lean` is focused-Lean GREEN: final emission exited 0 with an empty log. Its source SHA256 is `55b386ac06479c7133af7ae561f282ad2fbb05c0e74c22c3a5014b71eb3edfc7`. No native/SQLite execution of this new receiver is claimed. The coordinator stopped this window after the narrow module check to preserve the remaining account quota.

The exact frozen source/check manifest is `/tmp/dregg-policy-install-receiver-checkpoint.json`. Root owns Git and umbrella imports; this lane performed neither. The module needs a deliberate import in the appropriate root-owned kernel umbrella. The prior actual birth upper `Kernel/ResourceBirthPolicyController.lean` remains GREEN/frozen and has now been consumed by localfirst's passing joined native birth-to-invocation probe.

## What is implemented and proved

The receiver accepts a strict original signed ingress containing subject, policy-control capability ID, canonical installer declaration and original native envelope bytes. It loads the complete authority and lifecycle directory from the actual durable snapshot, derives the request context, invokes the existing semantic `PolicyInstallController.prepare`, and supplies its policy store only from immutable source cells in that same directory. The old selected source is retained as an actual physical read guard.

The new source cell and any required authority shards are deterministic internal representation creates for the same semantic declaration. The source-derived physical ID is reserved before shard placement. The existing permanent lifecycle allocator checks the complete directory, so existing and retired IDs refuse. The final writes are exact internal creates plus the existing grouped authority-head/nullifier shard and catalogue writes. No caller supplies an auxiliary blob, policy store, raw durable intent, native-verification Boolean or alternate portal.

Actual authorization consumes `CredentialSignatureAdmission.verifyNative` and the existing capability-only installer. A private `AcceptedInstall` retains the exact original native envelope, capability admission result and semantic accepted family. General checked laws bind source-owned creates, permanent fresh pre-state, exact allocated payloads, reserved IDs, actual physical roots/read guards, the accepted authority post, new head and consumed marker. `installed_source_bytes`, `installed_head_and_source`, `installed_authority_pages` and `installed_authority_catalogue` identify exact installed bytes rather than assuming cryptographic root injectivity. `source_loader_of_present` joins those source bytes to the existing canonical loader. Existing no-partial-commit semantics are reused.

The source-owned accounting vector charges actual ingress/envelope/storage/touch counts and the one semantic installation. It invents no monetary transfer: such a transfer needs a conserved Book leg. The public `receive` path uses the existing exact-byte durable journal/CAS loop. Historical replay compares the complete original event/ingress and shared semantic marker before any new key, root, height, policy or nullifier admission, and returns only the original transaction/event IDs. It never automatically resigns a stale request.

## Current known limitation and selected next semantics

The current authority schema couples policy source revision with the capability epoch. One accepted replacement invalidates the prior owner/control capabilities. This is explicitly documented in the receiving module and probe. Ember has now selected **KEEP grants; check the new rules; revoke separately**. That decision is not implemented in this checkpoint: no epoch equality was relaxed or bypassed. The next coordinated cutover is the design in `/tmp/dregg-policy-revision-separation.md`, with carrier's independent review in `/tmp/dregg-policy-revision-review.md`. Preserve exact generation matching, separately sign/bind source revision, and carry generation framing through the actual final post.

## Preserved native probe — source only

`scripts/probe-policy-install-receiver.lean` is frozen at SHA256 `751215a341b63cc9bb160d34d5490db5d50a9b705d0936750695a2a31b9d1c67`. It has **not been compiled or run**. Compile it before trusting syntax or any listed expected outcome.

It is designed to exercise real Ed25519 public test keys, the private actual native receipt, capability-only admission and SQLite bootstrap/reopen. Intended teeth: occupied/retired successor source ID, missing old source, ordinary `installProgram` cap trying `installPolicy`, stolen public control cap without holder key, and an old policy rejecting replacement. The positive path discards only the native success response, recovers by exact readback, reopens complete authority/source state, checks the new head and exact source bytes, and verifies the exact charge vector once. It then resubmits the unchanged original ingress at an expired height with an intentionally absent verifier binary, checks receipt-only replay, and rejects changed payload at the same source-derived transaction identity without changing storage.

The field `ZMod 65537` and scalar order width 15 are explicitly probe parameters, not a production field choice. Complete projected source/header values still pass the canonical injectivity and actual operand range checks.

## Exact next commands

Run only after the coordinator releases a focused two-thread seat. Existing binaries are already built; do not launch a new Rust build to run this probe.

```sh
env LEAN_NUM_THREADS=2 lake env lean scripts/probe-policy-install-receiver.lean
env LEAN_NUM_THREADS=2 lake env lean --run scripts/probe-policy-install-receiver.lean \
  /tmp/minidregg-credential-signature-verifier-target/release/minidregg-credential-signature-verifier \
  /tmp/minidregg-credential-signature-verifier-target/release/examples/sign-probe \
  /Users/ember/dev/minidregg/native/hyperdocument-link-sqlite-store/target/release/minidregg-link-sqlite-store
```

Then audit the new general theorem axiom sets and add enforced `#guard_msgs ... #print axioms` gates, following the existing installer convention. The current checked proofs contain no `sorry` or `native_decide`; the full axiom enumeration for this new module is not yet recorded. Root should run the appropriate integration closure after its deliberate umbrella imports. No broad build or native probe was launched after the explicit stop boundary.

## Check logs

- `/tmp/dregg-policy-install-controller-refresh.log`: exit 0, empty, current shared runtime profile.
- `/tmp/dregg-policy-install-receiver-check.log`: exit 0, empty, final frozen source and complete proofs.
- `/tmp/dregg-birth-native-upper.log`: prior joined upper exit 0, empty; the separate joined birth-to-invocation native verdict belongs to localfirst.

The first receiver check required only namespace and projection-proof elaboration corrections. The final code uses ordinary explicit projection lemmas instead of raising heartbeat limits. Local opacity of `CanonicalRuntimeProfile.Profile.compilerProfile` prevents the elaborator from trying to invert the source cSHAKE computation; it does not change kernel equations, runtime values, codec bytes or semantic checks.
