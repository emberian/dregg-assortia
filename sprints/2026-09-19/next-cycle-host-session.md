# Proposed next core step: a persistent verified host session

Source investigation at Mini `12e6608`, September 19. **Proposal, not an implemented interface or a newly assigned implementation cycle.** The current native client works through fresh processes; the complete kernel scenarios remain independently gated by cycle 1's evidence.

## The measured problem and existing path

The matched two-resource birth takes 49.43 seconds, and the first task query takes 33.55 seconds after the proved computation fixes. `Host/Main.lean:213-215` opens the store before entering `stdio`, then discards that result. Sequential frames at `:107-125,144-158` call APIs that reopen it. `Kernel/NativeHost.lean:29-35` loads/restores the durable image and asks `NativeHostReplay.verifyLoaded` to replay every retained original signed ingress. Confirmation at `:255-262` reopens again after the receiver's physical readback. This is actual executed verification work, not a missing index alone.

## Proposed receiving contract

Thread an internal `Session config` through the sequential `stdio` loop. Its cached tip must be minted by the semantic replay verifier and retain the checked `Opened`, exact canonical image bytes and a verified-prefix invariant. `Opened` or structural storage validity alone is insufficient evidence of historical authorization.

Every request still reads the physical image. Identical bytes may reuse the verified tip. A changed image must be strictly decoded, have the same pinned seed and exact accepted-record prefix, and pass replay of the new suffix at each original logical height. Reconstructed final bytes must equal the physical readback before replacing the tip. Absence, read errors, malformed encoding, rollback or a rewritten prefix invalidate the live session. Startup and restart still perform full verification. Do not use a height, digest, timestamp or disk-side assertion as byte equality.

Fresh preparation, observation and mutation still check the current challenge, authority, rules and signatures against the refreshed tip. Cache no grant decision or signing plan. The receiver still performs one CAS against the exact preimage bytes; contention does not rebase an old admission. Confirmation requires verified physical readback and exact original ingress identity, returning the receipt's original prefix boundary even if another writer has appended. Failed readback remains uncertainty.

This removes repeated semantic verification, but whole-image SQLite reads and decoding remain proportional to history. It does not establish a constant-cost storage design or an authenticated persistent checkpoint scheme.

## Verifier stability is an explicit obligation

`Compiler/CredentialSignatureIO.lean:21-22` stores only the native verifier pathname; `:43-76` launches it for each check. A fixed `Config` does not make that executable immutable or its answers deterministic. `CredentialSignatureAdmission.NativeIORefinement` at `Compiler/CredentialSignatureAdmission.lean:250-263` leaves the physical verifier/transport refinement as an explicit assumption.

Cached historical verdicts therefore need a fixed verifier semantics and deployment boundary. Pin the executable and relevant launch/runtime context, tie execution to that pinned artifact, and invalidate on a change or unverifiable identity. A pathname or modification time is insufficient; hashing a path and later executing it also has a replacement race. The proof must state the stable-verifier assumption. Equivalence of accepted state is distinct from exact IO-result equivalence: a cached past success can remain mathematically valid when a fresh helper invocation would be unavailable. The service contract must specify that availability behavior instead of quietly assuming equivalence.

## Completion evidence required

Prove that extending a verified prefix with checked suffix steps produces the same semantic image as full replay under the stated verifier assumptions. `Kernel/DurableReceiver.lean:267-288` supplies append/replay facts; the actual semantic verifier is `Kernel/NativeHostReplay.lean:149-204`.

Exercise unchanged-image reads; external valid append and revocation; stale challenges; rewritten/reordered/rolled-back history; same-height or same-root substitutions; CAS contention; lost replies and later appends before readback; restart and changed configuration. Include same-path verifier replacement, symlink swaps, unavailable helpers and changing verdicts. Check both outcomes and physical-read/replay counts. The public frame grammar can remain unchanged; physical process supervision and disconnect interruption are further host work.
