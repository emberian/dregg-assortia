# Checkpoint 31 — package-bound lifecycle and physical delivery custody

September 27, 2026. Continues [checkpoint 30](checkpoint-30.md).
The platform goal remains active across the five parallel journeys.

Mini `00e5a87` preserves the exact `9aec865` Linux native build evidence:
212 source modules, source/archive comparison, native link, and independent
artifact/checkpoint readbacks. Its binary is `47e09c55…`. It remains the
sharing/publication fixture input and does not contain the later routes below.

Mini `916bcdd` defines the full signed SPK identity descriptor and the explicit
versioned bridge mapping. Raw package and signed member SHA-256 bytes, signer
AppID, upstream app version, API path and ordered interface/schema mapping are
committed together. Mini installation revision is separate from upstream app
version. Physical identity inputs from one verified Bread parse were retained
in `0ad3605`; the source/physical comparison still needs to be exercised at
installation.

Mini `0424eca` adds descriptor-bound lifecycle BEGIN and claim v2. Historical
v1 replay remains intact. A claim selects the exact previously admitted v2
BEGIN, checks current authority and uses exact CAS readback before emitting a
descriptor-bearing reservation. Install/upgrade bind the prospective manifest;
start/stop check the currently installed manifest. The eleven source hashes
and bounded Lean closure verify in the
[evidence](https://github.com/emberian/minidregg/tree/0424eca/docs/evidence/2026-09-27-application-lifecycle-spk-v2).
Fresh Host routing, native signed acceptance, physical execution and checked
completion are outstanding.

Mini `0ea9cb5` authors dispatch signing plans from a single verified current
image and its admitted sharing history. The fixed custodian request cannot
choose subject, principal, permission bits or current roots. This first profile
is human-only; agents need an explicit parent task/generation and budget/fence
path. Mini `69fa859` provides bounded source-owned inspection of the strict
committed frame, including exact input bytes. Inspection does not confer
delivery authority. Private op36/37 and their request/plan adapters are the
next Host cut.

Mini `7043168` records physical delivery custody before fd3 RPC under the same
lock used for app lifecycle. It retains exact permit bytes, an active marker,
and a one-shot tombstone. The key includes app/generation/session/operation,
so two participants issuing identical HTTP bytes do not collide. The lock is
released while waiting for the app; a concurrent fence keeps the result
uncertain and forbids automatic resend. Focused Linux tests and strict Clippy
pass, with optional systemd probes explicitly excluded from physical claims.
The browser entrance still returns 503 until the actual delivery join exists.

## Live integration and next work

The hosted unforked Hermes fixture has reported confirmed native app creation
at accepted count 15 and session creation at count 31, across a reconnect to
the same verified Hermes session. Those are in-flight lane observations:
independent signed readback, final settlement and portable evidence are still
being collected. The model provider is synthetic. A real-model run still
requires the requested credential location, model and spending bound.

Fresh native app/session creation and exact receipt recovery passed with
Host `47e09c55…`. The first share plan then refused ticket birth preparation;
the owner is diagnosing the actual factory/funding/capability condition.
No sharing success is inferred from the passing base.

The fn ACK-tail finding and required joint empty/selected progress ordering
are recorded in [the continuity contract](fn-consumer-progress-continuity.md).
The new distinct gateway fixture separates release owner 7 from gateway 8.
Selected publication remains held pending the qualified coverage path.

A bounded read-only latency probe on a copied completed Store observed first
authorized reads of 60.74 and 76.46 seconds in fresh Host processes, warm reads
of 1.60/1.50 seconds, and warm exact receipt lookup of 1.70 seconds. These are
few samples under concurrent load, not a throughput benchmark. Full cold
replay and per-request storage transport are being investigated; unchanged
bytes must still be compared exactly, and changed histories must retain
checked replay.

Several agent turns failed during an account/access transition. They were
resumed after inspecting surviving sources and processes, without restarting
in-flight submissions. Only explicitly released build caches were removed.
The next finite native cut joins dispatch authoring and lifecycle v2 routes;
new fn frontier work and agent dispatch remain separately tracked obligations,
not prerequisites for indefinitely delaying that build.
