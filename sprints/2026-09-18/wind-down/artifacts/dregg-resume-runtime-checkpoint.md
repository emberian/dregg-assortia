# Resumed runtime closure, 2026-09-18

The first post-handoff run failed at link, before nine tests: the host C++ `std::thread` harness expected libstdc++ while the Lean link selected libc++. The optional profiler's `clock_gettime` repair was already present and no longer failed. Replaced only the test harness's host thread creation/join with the pthread ABI; the native init/reentry/kernel-call/thread-exit assertions are unchanged. Failed pthread creation refuses; failed join aborts rather than letting a worker retain a stack pointer past return. Local C++ syntax under Wall/Wextra/Werror passes.

The resumed attempt2 has actual `pbuild: VERDICT outcome=PASS status=0`. Nine tests passed in 1.213s, with zero skips among selected tests: three sticky lifecycle/mode unit tests; actual strict Lean DelegAdmit/thread/malformed-wire probe; five factory chronology durable/replay/refusal tests. The native narrow initializer took 1.230ms, runtime prefix 0.247ms; full initialization remains unattempted in that probe. Main factory constructor→child mutation→checkpoint→later deployments→reopen→historical World/History/reversible branches passed in 0.737s. These measurements do not carry into the still-pending full lifecycle/PQ/Hermes scenarios.

Artifacts:
- /tmp/dregg-resume-ffi-factory-fast-20260918.log (first resumed FAIL)
- /tmp/dregg-resume-ffi-factory-fast-source-20260918.json
- /tmp/dregg-resume-ffi-factory-fast-attempt2-20260918.log (9 PASS)
- /tmp/dregg-resume-ffi-factory-fast-attempt2-source-20260918.json (16 source hashes)
- /tmp/dregg-resume-ffi-factory-fast-attempt2-remote-source-20260918.json (all 16 exactly matched the actual receiving lane)

Current source edit: dregg-lean-ffi/tests/native_init_thread.cpp. Root owns commits. Foreign reversible.rs formatting/index changes were preserved. The sole Hbox Cargo lane is hcargo at /tank/dregg-build, lease owner agent:resume-runtime anchored to live Codex process 37986. 32 GiB / four jobs / native Lean required.

The initial three-process full/ST lifecycle baseline subsequently completed; see below.

## Full lifecycle baseline complete

Actual pbuild PASS: three selected fresh-process scenarios passed in 564.570s total, each approximately 187–189 s. Native foreign-thread full-first, narrow followed by racing full/native callers, and ST owner/mode refusal all ran actual kernel KATs. Source snapshot: /tmp/dregg-resume-ffi-full-lifecycle-source-20260918.json; log: /tmp/dregg-resume-ffi-full-lifecycle-20260918.log. Inclusive timing table: /tmp/dregg-resume-baseline-init-profile-20260918.json. Dominant first default calls: NetworkJudge 53.512 s and NightWatchCampaignWire 116.696 s; FFI 36.575 ms and FFIDirect 0.002 ms. These are baseline timings, not attribution to individual imported terms.

Approved executor-family changes are now applied locally (five files), joined with hotspot lane’s four source-owned fixture moves. Exact 21-file snapshot /tmp/dregg-resume-executor-family-source-20260918.json. Coherent Lean build of NetworkJudgeFixtures, DeckDescentFixtures and Dregg2.FFI completed with actual pbuild PASS. The regenerated C audit removed every moved definition from the two runtime C files while retaining the assurance modules.


## Executor-family checkpoint

The single Rust lifecycle coordinator now initializes the actual FFIDirect dependency family independently. It retains the initialization lock through owned native work and object teardown while registration remains open; after full default initialization it permits the existing parallel path. Default-only execution, sticky failure, ST refusal and full-readiness truth are preserved. The direct wrappers return owned Rust values, not Lean objects.

Actual fast native result: 11 selected tests PASS in 1.289 s, including the direct corpus/host-thread lifecycle probe and the five factory chronology regressions. FFIDirect initialization took 41.285 ms; its complete direct corpus/thread probe took 0.058 s. The main factory historical journey passed in 0.755 s. Log: /tmp/dregg-resume-executor-family-fast-20260918.log. Frozen nine-file manifest: /tmp/dregg-resume-executor-nine-file-checkpoint-20260918.json. Root owns commits.

Scope correction: every input in the standing conformance corpus carries prev=0xDEADBEEF, whereas its hosts store head 0 or 4. Those cases cannot commit a body; parity there establishes marshalling/refusal consistency, not accepted-credential behavior. Escrows/queues/swiss are deliberately retired wire ballast erased by BOTH FFI paths, so their omission is not a newly established direct parity fault.

## Final running capture at user wind-down

Only the already-running five-test full/PQ/Hermes capture is allowed to finish. Log: /tmp/dregg-resume-executor-full-pq-hermes-20260918.log; session 61744. Exact snapshot contains the executor-family changes and NetworkJudge/DeckDescent fixture cuts, but no wide auth repair, no JSON/string repair, and no NightWatch fixture move. The latter is local source-only work owned by root, not part of the linked runtime being measured here.

So far: exact Hermes js-agent bridge PASS 0.073 s (10 requests, successful mutations, partial effects before runtime failure, post-error readback). First connected admission/fire returned at +0.030 s; actual DelegAdmit init 0.587 ms. This test reaches the narrow admission family, not FFIDirect. The unchanged full-byte PQ route/KAT probe PASS 191.471 s. Three full/ST lifecycle scenarios remain in progress at this note's initial write; final verdict will be appended after completion.

NetworkJudge still took 53.959 s in the PQ capture. The two fixture cuts have NOT demonstrated an inclusive startup speedup. Read-only linked audit /tmp/dregg-resume-postcut-linked-members-20260918.json confirms current archives have SHA256 0b272abf86e6bab2ee04bbe846f745747429ff1a77f21cda119c7254faeb3e24; the exact NetworkJudge and DeckDescent archive members equal their fresh cached objects. NetworkJudge has no moved check symbols and DeckDescent has no moved blind-search symbols. Remaining imported startup work is still a named residual.

## Staged repairs and unrun work

- /tmp/dregg-direct-auth-width-20260918: hotspot-owned seven full-width credential builders and test encoder, Lean equalities/axiom pins and Rust owned-region replacements. Unapplied, unbuilt. Production currently still truncates nine 256-bit digest coordinates through the narrow auth ABI.
- /tmp/dregg-wide-auth-test-draft/: this lane's supplemental accepted cases, high-192-bit mutations, selected OneOf cases and exact native AuthW serialization comparison. Unapplied, uncompiled, unrun; hashes and missing integration in /tmp/dregg-wide-auth-test-draft-manifest-20260918.json. Production build.rs must pin all seven wide builders plus dregg_d_auth_encode_w before applying this test wave.
- Eight credential digest coordinates participate in the existing Crypto.Reference echo portal and should refuse a high-bit mutation; stealth ephemeralPk is ignored by current semantics, so its mutation must preserve exact transport/parity without an invented refusal assertion. These are transport/reference-executor checks, not evidence of real cryptographic verification.
- Exact UTF-8/NUL direct transport is approved but unimplemented: use lean_mk_string_from_bytes plus a byte-size shim/readback, not CString's current empty fallback. The separate wire_strings lane owns staged strict JSON decoding and both Lean/Rust control-character escaping. No next-wave rebuild or test was launched.
- Root's NightWatchCampaignWire/Fixtures/CanonicalCodecHealthWire source move is not runtime-tested. Next coherent wave needs all four affected assurance roots and Dregg2.FFI rebuilt before native archive retiming.
- The wider 24-case durable ledger/replay/time-travel/reversible regression filter has NOT been rerun after the factory changes in this resumed lane; only the five new focused factory regressions above have current evidence. No whole-workspace gauntlet was attempted.

No Git operation, branch, worktree, stash, semantic fallback, disabled gate, or foreign WIP restoration was performed by this lane. The lease remains live until the already-running capture finishes, then will be released and recorded.


## Final verdict and stopped state

The allowed existing capture is COMPLETE: `pbuild: VERDICT outcome=PASS status=0`, five selected tests passed in 802.039 s total (four slow; four other tests excluded by the requested filter). Individual times: exact Hermes bridge 0.073 s; unchanged full-byte PQ 191.471 s; native foreign-thread full-first 204.100 s; narrow-first followed by racing full/default/native callers 203.382 s; ST owner/mode exclusion 203.013 s. No selected check was skipped. Actual module timings and log hash are in /tmp/dregg-resume-final-runtime-results-20260918.json. Receiving-lane extra source identities are in /tmp/dregg-resume-final-capture-extra-source-20260918.json.

The full-runtime cost remains approximately 191–204 s; executor narrowing solves entry into the exact family, not initialization of every unrelated family. The prior fixture moves remain assurance-preserving source separation, not a demonstrated full-init performance fix.

Final staged patch handoffs: /tmp/dregg-direct-auth-width-20260918/staged-manifest.json and /tmp/resume_wire_strings/HANDOFF.md. The string agent completed only the strict decoder draft; both producers' control escaping, Lean pins, and length-aware direct string transport remain incomplete. Do not read the earlier requested scope as work that was implemented.

No next wave was launched after wind-down. This lane is stopping after final artifact preservation and release of its own hcargo lease.

Lease release completed: `state=released lane=hcargo owner=agent:resume-runtime holders_remaining=0`. Session 61744 exited; no process from this lane remains running.
