# September 18 account handoff

This is a continuation of the autonomous September 26 programmable-nexus sprint, not a new orientation assignment. Ember reported 7% weekly usage remaining and another account available. The swarm converged its current checks and preserved unapplied work. Read CURRENT.md and intent.md, then resume the next receiving journey below. Preserve foreign working-tree changes.

## Decisions now settled

- Existing grants survive owner rule replacement and are checked under the new rules. Revocation remains separate. Current live installation still conflates source revision and grant generation; implementing the split is the next coordinated schema wave.
- Cloud/resource-host lifecycle is the area to offer Wisper. Exact kernel/host contract, runtime and assignment remain open. No agent contacted Wisper. The substantial [brief](../../contributing/resource-host-lifecycle.md) and [native-host export proposal](account-handoff/design/dregg-native-host-export-proposal.md) provide the starting point.
- Earlier retained direction still applies: Git primary; mostly Astra with selective Sol; wide coordinated work; real provider stake locked with penalties recorded only; no selected live custody/asset/cluster operation.

## Implemented and exercised

Mini **8056f9b** runs actual native signed resource birth through policy/capability admission, canonical Book fee transfer, initial immutable policy source, distinct owner/control grants and one durable publication. It reopens SQLite, invokes with the actually issued owner grant, reopens again, and replays original birth/invocation receipts without another charge. The final probe also replays birth after its original key/grant expiry, and refuses stolen-capability use, creator-coordinate substitution, altered payload and noncanonical ingress without changing bytes. Native test keys and ZMod65537/scalar15 are explicitly fixture parameters, not a production profile or on-chain payment.

The exact final log, commands, source/binary hashes and 24-theorem ordinary-axiom audit are [preserved here](account-handoff/native/dregg-resource-birth-receiver-checks.json), with a [receiving-path report](account-handoff/native/dregg-declared-resource-receiver-wip.md). Mini **a21633c** additionally checkpoints the physical policy installer: focused Lean check passes; its native probe is uncompiled/unrun, and its old-epoch grant invalidation remains to be replaced.

Earlier committed Bread **73136dd30** passes 24 targeted cell/turn/World tests, including intermediate history boundaries and tampered receipts. Lazy SDK registration at **3b9497753** lets its four candidate/publication tests complete in 0.026–0.047 seconds each. Actual js-agent Hermes admission passes but still takes 191.097 seconds at first verified use; the full-byte PQ KAT also passed. These results are captured in the preceding checkpoints and predate the new FFI/factory changes.

The real Hermes/node-brain/live-brain library, CLI and two integration targets compile; full Starbridge desktop/headless-render/live-brain library and binary, including Servo, also compile. These are **compile checks on the recorded pre-FFI/factory snapshot**, not runtime results for the latest changes. [Exact scope](account-handoff/runtime/dregg-consumer-compile-closure-20260918.md).

Assortia has a graph-owned board, bidirectional relationship navigation and portable source checking with retained historical hashes. Its 41 tests passed in the preceding checkpoint. A changed source remains a reinspection request; no old measurement has been refreshed into a new green.

## Runtime changes converging at this checkpoint

Bread has ordered persistent factory deployment across World/replay/history/forks and one native Lean initialization coordinator, including real narrow DelegAdmit initialization, thread/mode ownership and sticky failure. The changes are committed in **bf953115d** as a work-in-progress checkpoint. The first combined check failed on history mutability; that was fixed. The second failed before tests on three stale Mina test callers; their15-field arguments are now sourced from the actual Lean shape contract. The third attempt reached linking, then failed on the new optional profiler’s C++ clock symbol. No selected runtime test ran. Its source repair and final checkpoint are recorded below. Do not carry the earlier24-test pass across these new changes.

## Resume in this order

1. Finish the targeted FFI/factory runtime checks and failures recorded below, then real full-initialization fresh-process probes, unchanged full-byte PQ and exact Hermes first-use profiling. Keep one Cargo build on hbox, 32G/four jobs, native Lean required; inspect actual verdicts. Do not weaken the verified gate to reduce startup time.
2. Integrate **one** coordinated generation/revision, full-request codec and explicit delegation representation wave. Preserve exact generation equality; add explicit signed source revision; update every source/codec/profile/physical consumer coherently. Current scratch transport has 16 fields; the revision addition requires 17. Do not apply independently versioned patches blindly.
3. Exercise create → replace rules twice while grants survive → delegate a narrower right to another enrolled subject → recipient invocation → reopen/retry/refusal. Preserve the new born-owner fixture as a regression boundary. Implement actual generation revocation and its usable control path; do not auto-reissue grants to conceal epoch invalidation.
4. Bring that path through a real programmable shell/native host. The proposed compiled Lean host and BabyBear/29 profile are source-backed candidates, not accepted deployment choices. Complete source-owned signing/ingress/query/cursor/clock/export contracts and use this as the receiving interface for Wisper's hosting feature.
5. Keep the Clutch/Solana/provider operation linked to its own finality and custody facts. The known whole-system STARK statement problems remain work; none of these native/component results closes them.

## Preserved next-wave work

[Inventory](account-handoff/inventory.json) maps original temporary paths to retained files and hashes. [Scratch overview](account-handoff/next-wave/README.md) distinguishes checked Family/State/Effects, mixed-lineage checker/witness and universal byte-compatible codecs from the unchecked registry draft and unapplied wire changes. 32 delegation declarations and 21 checker declarations passed ordinary-axiom audits. No live representation cutover occurred. Rebuild isolated artifacts; no symlink olean tree or generated binary was copied.

Remaining exact proof gaps include source-admission success preserving returned evidence/parent identity, receiver construction and native Alice→Bob use. Revision separation, its request/profile versioning and management/revocation usability require real implementation despite the checked scratch.

## Coordination and foreign work

Both Mini compiler seats are released. Keep at most two narrow Lean compiler processes, two threads each, and serialize shared representation edits. No Hbox build remains active. The previous root lease was agent:astra-sprint; release completed with zero holders remaining. Reacquire a live lease when resuming. Persvati was unreachable on its LAN path during this sprint; do not read that as absent toolchains.

Do not sweep unrelated Bread staged/unstaged circuit-prove/fhegg benchmarks, untracked research/images; Mini Compiler.lean/README/licensing/Uwueave/prover/Cargo changes; or DreggNet control/src/node_api.rs WIP. Mini scripts/probe-authority-domain.lean is an earlier source-only scratch probe left outside these commits. Root commits named files on main; no branches/worktrees/stash. The Bread push hook still requires the already-used DREGG_ALLOW_DEAD_DOC_REFS=1 override for historical dead references; that is not a passed documentation gate.

## Swarm assessment

Astra produced the difficult source-policy/authority/physical-state joins and adversarial reviews. Sol supplied useful bounded participant-node and cloud/mobile inventories. Initial Terra orientation remains historical input. This was not a controlled model comparison, and no per-agent quota ledger was captured. Commit volume and isolated theorem counts are not measures of a usable product.

The main process improvement is to keep the wide swarm tied to one executable user journey and stage shared representation changes, while using lighter bounded work for inventories, tooling and routine verification. Too much dependent work accumulated before integration. The current paid-birth/owner-invocation journey is substantive progress; a friends-ready shellserver, delegation, cloud orchestration and public economic experience remain ahead.

## Final runtime checkpoint

Bread **bf953115d** contains the 16 frozen implementation/config/test files plus HORIZONLOG. Actual attempt3 verdict was **FAIL / 101 at link, before all nine selected tests**: the new profiling clock referenced a libstdc++ chrono symbol while the Lean link supplies libc++. The narrow repair now uses `clock_gettime(CLOCK_MONOTONIC)` and reports unavailable timings on clock failure. Pinned Lean-header syntax passes; **post-repair linking and runtime execution remain unrun**. The previous two failures and exact source snapshots remain preserved.

Resume the targeted command from repository root after acquiring a live lease:

```sh
scripts/lane-lease.sh acquire --host hbox --root /tank/dregg-build --lane hcargo --owner agent:astra-sprint --pid <live-session-pid>
SWARM_MEM_MAX=32G DREGG_REQUIRE_LEAN=1 DREGG_LEANC_JOBS=4 LEAN_NUM_THREADS=2 scripts/hbuild hcargo env DREGG_LEAN_INIT_PROFILE=1 timeout --signal=TERM --kill-after=15s 900s cargo nextest run --profile full --build-jobs 4 --test-threads=1 --no-fail-fast --no-tests fail --no-capture -p dregg-lean-ffi -p starbridge-v2 --features dregg-lean-ffi/lean-lib,starbridge-v2/agent-js --lib --test lean_init_lifecycle -E 'test(~init_lifecycle_failed_module) or test(~init_lifecycle_unwind) or test(~init_lifecycle_mode_refusal) or test(~delegated_admission_initializes_only_its_real_lean_module) or test(/factory_chronology_/)'
```

Use a new captured log/source manifest and read `pbuild: VERDICT`. Later full/ST lifecycle and PQ/Hermes tests remain necessary. The new factory tests and preceding history suite also need their actual current-source results. No Cargo or Lean process from this swarm remains active; Hbox lease release returned `holders_remaining=0`.

Implementation checkpoints are on main: Mini 8056f9b and a21633c; Bread bf953115d. Assortia's own commit contains this handoff, graph updates and preserved next-wave evidence. The older source-only Mini authority probe and unrelated user changes remain outside these checkpoints.
