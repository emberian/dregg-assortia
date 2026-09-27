# Checkpoint 61 — measured warm reads and same-Store integration work

September 27, 2026. Continues [checkpoint 60](checkpoint-60.md). The full
[parallel journeys](parallel-journeys.md) remain open.

The unmodified f461 Host now has a measured persistent-session comparison on
an independent copy of the retained post-reserve Store. Socket readiness took
0.314 seconds, but the first successful signed query took 86.62 seconds while
verifying history. Repeating the exact same signed observation through the
same Host child took 0.73 and 0.96 seconds. All three returned the same 101-byte
view as the cold benchmark and left the copied Store unchanged. This does not
measure challenge/signing overhead, changed-image extension, or every query.
The bounded service finished inactive/success. Keyless timings, CPU snapshots
and identity hashes live in Mini's
`docs/evidence/2026-09-27-f461-warm-signed-query/`.

Source tracing explains much of the fixture's earlier delay: `mini query`
without a socket launches separate cold challenge and query processes. Mini
**9ccdea4** moves routine share-fixture reads and reserve submission onto the
existing persistent public service, then uses the existing operator service
for later reads. Public op56 refusal and explicit public/operator service
restart gates remain. Syntax, ShellCheck and diff checks pass; this changed
script has not run native acceptance. The live event22 r3 continues from its
immutable older archive. Its tool reserve was accepted at count 17, followed
by current tool/parent reads and source request authoring; no sharing-ticket
acceptance is claimed yet. Client-session owns that Store.

The exact 2649f49 successor Host build had two environment failures: r1 lacked
Git metadata; r2 lost Mathlib artifacts when Lake re-cloned package directories.
The builder checked package sources, revisions and manifest against f461,
restored only matching independent build artifacts, and started full r3.
It has passed the previously failing module and advanced into project modules.
Poll Persvati user unit `minidregg-2649f49-host-r3.service`, invocation
`b16899141d5f43b696d9c8ff51aa89a4`; log
`/home/ember/build/minidregg-2649f49-evidence/run-r3.log`. No finished successor
ELF is claimed. A separate private instrumented f461 replay build is assigned
to fn-mini-review to measure derive/advance/validation/boundary phases before
attempting a core semantic optimization; at most two Lean compiler processes
across the independent builds.

Mini **e8c3bca** separates stable lifetime Hello lineage/incarnation from
per-dispatch current claims. **06fe2c3** adds an exact durable STOP attempt
marker; **8b9cd9e** records the unrun one-Store physical STOP/continue acceptance
recipe. Physical START is still guarded while its source-bound launch,
completion-reply recovery and incarnation reconciliation are reviewed. The
controller/resident v3 wire is being connected: the initial forward request
retains stable binding and exact HTTP; the reverse reserve reply supplies
current claims derived from Mini op80 and binds them to that operation.
No reserve or historical receipt alone authorizes fd3 delivery.

The final GitWeb service cannot be assembled by renaming the synthetic sharing
fixture's paths. Its integrated allocation uses separate controller/tool
subjects and tasks, installed package version 1 and a completion custodian.
Client-session found a concrete missing authority edge: the agent needs its
own app-observe delegation; app owner capability 141 belongs to subject 8.
It is preparing source-authorized observe delegations and same-Store sharing
continuation from current signed state. Mini-app-contract owns a new protected
resident-config preparation script, coordinated with the physical host owner.
Neither task may recreate the integrated Store or invent accepted receipts.

The next useful result is actual INSTALL/create START and sharing in that same
GitWeb Store, followed by agent/API/browser access. Two users, bounded
delegation and revocation, actual-model Hermes, disconnect/restart behavior,
selected fn publication/receiving and direct programmable commands remain
required. Source components and independent fixtures do not replace those
integrated journeys.
