# Overnight fn / Mini construction

Ember authorized autonomous overnight work on September 26, using mostly Sol agents, toward distributed shellservers or other shared programmable infrastructure built from the actual Mini/Bread components and coordinated through fn. This is substantial core and integration work. Do not replace it with a disconnected greenfield interface or prematurely reduce scope for an assumed morning deadline. Ember will decide release compromises when awake. An explicit goal is active for this work.

## Recovered starting point

Mini's local main was `dd1360d`, while `implement/fn-evidence` at `183cd37` already contained 54 additional commits implementing portable Mini evidence, fn poll/consumer transactions, durable reply staging and A-side reply consumption. The 44 incoming paths did not overlap the 18 preexisting dirty/untracked paths. Root fast-forwarded main to that lineage, then merged the independent upstream CI-action pin commit `ba884ab`. The older perf/fn-e2-materialized-cache branch is separate experimental work, not silently included.

Fn's [two-store evidence](../../../fn/planning/evidence/two-store-join-1a9dd747-2026-09-24.md) records five completed A→B→A exchanges using Mini `183cd37` and qualified fn `1a9dd747`, including a lost ACK response settled from fn's durable position. Mini's older two-store note predates these results. These are synthetic exchanges on one machine, using a retained report and reused Mini identity. They do not establish a hosted service or separate user identities. The matching Mini binary remains in the existing fn-evidence worktree; historical private `/tmp` setup inputs are gone, so fresh setup is necessary.

Fn is being developed by Claude. Its [coordination note](../../../fn/planning/for-codex-2026-09-26.md) is authoritative for shared-checkout/host coordination: use fn as a dependency; do not edit its shared checkout or run its owner/images on the laptop; protect the live hbox node. Existing qualified isolated scratch harnesses can supply integration evidence. Requests for fn changes go in Mini-owned `docs/FN-UPSTREAM-REQUESTS.md` for coordination. BP is not assumed deployed.

## Actual integration being built

The user-facing path should join a durable shell/agent session to Mini's real `AgentGrain` authority, reservation and generation transitions; authored resource operations and fn correspondence go through the real Lean receiver. Fn carries durable authored correspondence across nodes. Mini decides application meaning and current authority; fn acknowledgement follows durable Mini processing. An accepted operation, completed external effect, recorded fn authorship and transported article are distinct facts.

Current lanes (all Sol, root integration/review):

| Lane | Write scope and receiving obligation |
| --- | --- |
| mini_receiver | `Host/Main.lean`, `Kernel/NativeHost.lean`, new session module: retain verified state in the served process, current admission and exact CAS/readback |
| replay_session | `Kernel/NativeHostReplay.lean`: verify exact retained prefix and new suffix, preserve original receipts, prove semantic composition |
| client_session | Rust resource-client: actual persistent stdio/Unix-socket service, retained exact requests, uncertainty and reusable entrance |
| hermes_path | New Rust grain-runtime within Mini: actual AgentGrain commands, durable supervision, physical hard interruption, soft continuation and upstream Hermes connection |
| fn_reply_profile | `FnReplySource`, `FnReplyPublication`, `Host/Json`: durable operator-selected reply context and grain-intent/publication authoring |
| fn_mini_review | `FnConsumerOperation`, its proofs, `FnReplyConsumption`: dedicated pinned gateway authority, recognized consumer admission/provenance, remove arbitrary history ceilings |
| fn_contracts | Mini-owned fn setup/recipe: fresh custody/genesis inputs, real isolated exchange, then separate A/B gateway identities |
| build_native | Warm independent snapshots, narrow compiler seats, source/binary manifests, final receiving-path checks |

The initial review identified a real gap: a producer-observed poll Boolean inside an otherwise ordinary authorized content command is not unforgeable Store provenance. The chosen repair uses a dedicated gateway identity and its resource law/current capability, independently pinned by the consumer service. Ordinary user authority must not manufacture a recognized gateway record. This explicitly trusts the local poll gateway; it invents no fn-issued portable Store certificate. Its enforcement and negative direct-submit tests remain work until captured.

Hard disconnection must signal owned worker processes immediately, not wait for a slow kernel write. The controller remains to fence the generation, retain uncertain outcomes and reconcile before relaunch. Never kill a recycled PID merely because an old journal mentions it. Hermes's built-in tools remain an execution path to supervise; adding MCP tools does not make them exclusive.

Session reuse needs stable verifier semantics. The initial design uses a service-owned private executable snapshot throughout the session, with an explicit OS/same-UID non-tampering and runtime-library assumption. Checking the original pathname's hash then executing that mutable pathname is insufficient. Current authority is refreshed per operation; no cached authorization decisions.

## Convergence evidence

Run focused checks during development; converge exact source at a native build. Exercise real client→host→fn→peer→Mini reply paths, separate identities, restart/uncertain reply, revoked/stale authority, hard/soft disconnect, physical process death and original receipt recovery. Record timings for interactive behavior and evidence for every remaining failure. Existing passes remain scoped to their original bytes. No result from tonight is claimed merely by this brief.

Graph work records own status. Root commits reviewed scoped files and pushes regularly, preserving other sessions' WIP; unsigned per-commit fallback is authorized. Existing Python test harnesses may orchestrate the real systems; the platform implementation remains Lean/Rust with fn's own ACL2 semantics.
