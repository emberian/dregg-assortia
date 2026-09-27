# Checkpoint 66 — user-requested wind-down

September 27, 2026. Ember requested winding down at 10% remaining usage.
Construction is paused; the complete [parallel journeys](parallel-journeys.md)
remain unfinished. Resume from this record and [checkpoint 65](checkpoint-65.md).
No lane is authorized to continue launching work during this pause.

## Safe stopping point

All implementation/review lanes acknowledged the wind-down. Their private
builds and diagnostic queries are terminal. The approved 2,400-second direct
birth retry **was not launched**: its hbox unit is not found, and no
`retry-0002` artifact was created. The integrated GitWeb r3 Store remains
genesis; the exact original birth lookup returned `absent`. Preserve
`/var/lib/minidregg/spk/fixtures/gitweb-v2-20260927-client-session-r3`, including
the original `base/workroom/birth-attempt`. Do not recreate keys/genesis or
blindly resubmit the request on resume. Recheck process state, exact artifact
pins, Store and original receipt before a continuation.

Mini **5a4ff3b** preserves the portable failed-birth/lookup evidence and the
corrected private replay profile. Root verified all 11 preflight checksums
and all 11 profile supporting-file checksums. The hot version-3 replay events
are grain births. Generic directory/authority reload is not the main latency
target. No optimization or real integrated-birth profiling was launched.

## Preserved unfinished source

Mini **8846d4e** contains
`docs/evidence/2026-09-27-wind-down-wip/{controller,resident}.patch`, based on
**1ec2fc0**, plus source hashes, reconstruction verdict and component evidence.
Root applied both patches in a separate plain scratch directory and verified
all **13 resulting source hashes**. They are portable source preservation,
not adopted implementation or native acceptance. The working-tree changes
remain present; **do not apply the patches over them**. Foreign WIP is untouched.

The controller cut passed 125/125 component tests and strict Clippy. Independent
read-only review found no concrete custody/crash-ordering bypass in the inspected
paths, but identified conservative held states that still need reconciliation
and native crash/restart testing. The resident cut passed eight focused Linux
tests and strict Clippy. Its op78/79 assembly and separate payer/app/grant
custody remain unconnected to a complete callable dispatch path.

The review and same-Store event22 continuation contract are retained in Mini
under `docs/evidence/2026-09-27-wind-down-wip-review/README.md` and
`docs/evidence/2026-09-27-spk-platform-base-preflight/SAME-STORE-EVENT22.md`.
The latter is an unexecuted recipe, not an installed ticket. All retained
public evidence excludes live credentials and private Store contents.

## Resume order and missing integration

1. Inspect current Git/WIP and exact source hashes before adopting the frozen
   controller/resident changes. Source-qualified Host **f450a57** already exists;
   its evidence is **477e2e6**, so do not rebuild merely because an older component
   note lists a qualified Host as a prerequisite. No same-Store upgrade is claimed.
2. Profile the retained 212,637-byte real workroom birth on an independent Store
   copy. Focus on grain-birth preparation/admission and source-equivalent changes.
   A single bounded exact direct retry may also continue integration after fresh
   absence/pin checks; it is an acceptance bridge, not a latency fix.
3. Complete resident fresh op76 installed-permit validation, durable mark-send
   ACK, one fd3 delivery, retained response, settlement ACK and definite http-v3
   reply, plus callable versioned listener/config. Then exercise the exact
   same-Store grant/reserve/paid-dispatch chain and uncertainty/restart behavior.
4. Implement the callable STOP supervisor. No new supervisor source was started.
   Existing **1ec2fc0** only supplies exact Fenced recovery. Coordinate a new
   `lifecycle_v3_stop_service.rs` with resident config/report adapters and minimal
   shared lib/main registration; join source BEGIN/claim, physical fence, stopped
   report and completion without turning historical receipts into new permits.
5. Continue actual GitWeb INSTALL/START and two human/agent subjects, direct
   resource commands, real-model Hermes, hard/soft disconnect and selected fn
   publication with independent receiving authority. These are still the full
   product goal; separate component greens are not its completion.

No further long run is waiting for observation. Private source/build caches
are preserved, not cleaned. Graph work remains unfinished; an `active` work
record is ownership of remaining work, not an assertion that its old agent is
still running during this user-requested pause.
