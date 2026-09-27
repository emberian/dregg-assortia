# Checkpoint 67 — resident/controller batch adopted

September 27, 2026. Continuation of [checkpoint 66](checkpoint-66.md) under
[demo convergence](demo-convergence.md). Ember requests precise closeout with
severely limited remaining usage. No new workstreams. The platform goal remains
active and incomplete.

## Closed source batch

Mini **b988513**, pushed to main, adopts the callable resident v3 route and
read-only settlement recovery. The controller is **d4d18d0** (129/129 focused
tests and strict Clippy); resident evidence records **27/27** focused Linux
tests and strict all-target Clippy. Root verified all 14 resident source/log
hashes and reviewed the final recovery changes. Exact uncertain A recovery and
repeat inspection preserve participant B's active slot. Lost settlement ACK
recovery does not resend fd3. See Mini
`docs/evidence/2026-09-27-spk-lifetime-resident-v3/README.md` and
`docs/evidence/2026-09-27-lifetime-controller-recovery/README.md`.

This closes the reviewed source batch, not deployed acceptance. Updated Host
inspection fields in **3d10f81** passed a scoped Lean check but still need a
source-matched native image. Current qualified SPK and Host images do not include
this complete source batch. Physical STOP supervisor integration remains open.

Mini **c9ba45f** contains the resumable same-Store journey driver, with checked
shell gates and retained-source pins. It has not positively continued the live
journey. Its original Host pin needs an explicit reviewed compatibility transition
before using an optimized successor; do not rewrite the original attempt identity.

## Exact integrated blocker

The r3 Store still has no accepted app/ticket/grant lineage. The first 212,637-byte
request is an **ordinary ResourceBirthPolicyController birth**, not composite
GrainResourceBirth. Earlier hot grain-birth replay profiles describe a different
workload. Private exact-call diagnostics measured outer decode at 23.468 ms,
Store open at 247.444 ms, ordinary ingress decode at 0.122 s and historical replay
at approximately 2 microseconds. The remaining long stage is
`ResourceBirthPolicyController.admitDecodedNative`.

Redundant private runs were stopped, with no outcome and unchanged copied
SQLite; cancellation is not a native refusal. No live r3 retry was launched.
At this checkpoint the sole diagnostic job is Persvati session **54535**, private
tree `/home/ember/build/minidregg-2649-ordinary-birth-deep-profile-20260927`,
timeout 1200 seconds, two Lean threads/two C jobs. Direct Lean passed; suffix
build was at module 166/351 when reported. Owner `fn_mini_review` will finish
this build and one copied-genesis run, retain the dominant stage and concrete next
edit, and avoid another build ladder. Recheck this handle before launching anything.

## Next integration boundary

Finish the measured admission repair with appropriate equivalence evidence;
qualify source-matched binaries in a single batch; resume the retained Store
through accepted birth, install/start and actual browser/agent use. No combined
service or real-model Hermes result is established. The model, test-spend cap
and approved credential location remain unanswered prerequisites for paid calls.
Selected Git content-to-Mini publication and independently authorized fn receiving
also remain open. Preserve unrelated WIP in all repositories.
