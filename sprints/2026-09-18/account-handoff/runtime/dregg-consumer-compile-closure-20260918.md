# Breadstuffs authored-program consumer compile closure

2026-09-18. Owner: sprint_shell_hermes. Read/build-only pass; no breadstuffs source edits. This report distinguishes compile coverage from runtime tests and identifies the exact recorded source snapshot.

## Hermes and NodeJsHands

PASS: `scripts/hbuild hcargo timeout --signal=TERM --kill-after=15s 1800s cargo check --jobs 4 -p deos-hermes --features node-brain,live-brain --lib --bin deos-hermes --test node_backed_hands --test node_backed_round_trip`.

Environment: `SWARM_MEM_MAX=32G`, `DREGG_REQUIRE_LEAN=1`, `DREGG_LEANC_JOBS=4`, `LEAN_NUM_THREADS=2`. The remote build used the existing persistent root lane lease. The recorded wrapper elapsed time was 308.892 seconds; Cargo reported 4m59s. The actual wrapper verdict was `pbuild: VERDICT outcome=PASS status=0 lane=hcargo host=hbox`. This command compiled the library, real CLI and the two named NodeJsHands integration test targets; it did not run tests.

Artifacts:

- `/tmp/dregg-hermes-node-consumer-check-20260918.log`
- `/tmp/dregg-hermes-node-consumer-source-20260918.json` (exact command, environment and 31 directly relevant source hashes)
- `/tmp/dregg-hermes-node-consumer-remote-sha256-20260918.json` (remote hashes agree with all 31 captured local files; mismatches empty)

The command exercised the actual `node-brain` and `live-brain` consumers of the `Requirement` API and retained script-error/operation-receipt shape. It predates the next FFI lifecycle and factory chronology work.

## Desktop and live-brain

PASS: `/usr/local/bin/swarm-build timeout --signal=TERM --kill-after=15s 1800s cargo check --jobs 4 --keep-going -p starbridge-v2 --features desktop,headless-render,live-brain --lib --bin starbridge-v2` in `/tank/dregg-build/hcargo` over SSH, under the same 32G/4-job/Lean-required environment. The actual foreground subprocess exited 0 after 528.063 seconds. Cargo reported `Finished dev profile [unoptimized + debuginfo] target(s) in 8m 47s`; the log has no compiler errors. This is library and binary compile coverage, not a runtime or test result.

The parent authorized direct use of the existing remote snapshot after review of the actual wrappers: `hbuild` forwards to `pbuild`, which always rsyncs, while `/usr/local/bin/swarm-build` directly establishes the bounded systemd scope. No invented skip-sync option was used. The persistent root lease `agent:astra-sprint` / PID 66314 was verified alive; no lease was replaced or reacquired.

There was no rsync for this command. All original hashes plus the complete Starbridge source tree were rechecked just before execution: 201 recorded source hashes. The new local FFI lifecycle and factory chronology edits are explicitly outside this result. Servo remains enabled through the actual `desktop` feature; no feature was removed to bypass a failure. `headless-render` additionally compiles the real named rendering path in the binary.

Artifacts:

- `/tmp/dregg-desktop-live-consumer-check-20260918.log`
- `/tmp/dregg-desktop-live-consumer-source-20260918.json`
- `/tmp/dregg-desktop-live-consumer-remote-sha256-20260918.json` (all 201 source hashes rechecked after completion; mismatches empty)

This directly leased command has no `pbuild: VERDICT` line. The successful outcome comes from the actual foreground subprocess status together with Cargo's final success line and completed source recheck. The remaining warnings are ordinary unused imports/dead code plus Cargo's pre-existing future-incompatibility notice for `proc-macro-error2`; no warning cleanup was performed in this read/build-only pass.

## Result and next check

Both explicitly selected consumer resolves compile. This pass found no consumer compilation breakage to repair. The next remote sync/check should include the coherently frozen FFI lifecycle and factory chronology changes, which were deliberately absent from these two commands. The Cargo slot is released to the parent; the parent's persistent lane lease is unchanged. No local Cargo, whole-workspace build, fallback verifier, Git operation or source mutation was used.
