# Checkpoint 58 — successor build and concrete app Store running

September 27, 2026. Continues [checkpoint 57](checkpoint-57.md). The full platform objective remains active; these jobs do not establish a deployed service.

Two independent jobs were directly checked active by root:

| Job | Authoritative handle | Exact scope |
| --- | --- | --- |
| Persvati successor Host | User unit `minidregg-f461f39-host-r1.service`, invocation `ceb69857d4ee443e85a932cf9cf404ae`, PID1996002 | Exact f461f39 archive, SHA `86dd1cecb72c361584c66f22fc506b6011d9b5b624da75c9468d56ed368d35e6`; independent snapshot `/home/ember/build/minidregg-f461f39-next-20260927`. Guarded incremental suffix from Replay, with 258 unchanged prefix modules, nine later changes and five inserted modules declared. Expected suffix85; completion is not yet observed. Log `/home/ember/build/minidregg-f461f39-next-evidence/run-r1.log`. |
| Hbox concrete GitWeb base Store | User unit `mini-spk-platform-runbase-r1-client-session.service`, invocation `3f37cb04cfe34833b7ffdd179072ce5b`, PID3876902 | Fresh protected root `/var/lib/minidregg/spk/fixtures/gitweb-v2-20260927-client-session-r1`; exact f8bc6bf run-base script, v2 Host4fba5329, physical helper2819d365, Mini007b513 and9746 helpers. Base app/package/snapshot and sessions only; no INSTALL/START. Logs `/tank/dregg-build/minidregg-spk-platform-client-session-runbase-r1/`. |

The jobs run on different machines at CPUQuota200% each; the build has MemoryMax32G and the base Store job8G. Poll these handles before treating either as stopped. Quiet logs are not a terminal verdict. The old event22r2 Store remains untouched.

Mini **fa6f4dd** adds a distinct STOP-only signing plan carrying the verifier-selected prior running event25 receipt, invocation, cgroup, image and custody. General codec round-trip and two direct Lean checks pass. This source is outside the fixed f461f39 build and still needs the current-Verified postclaim inspection and Rust physical consumer. INSTALL/create retain their prior plan codec.

Root review found an INSTALL restart gap during interrupted report/plan authoring. Agent-api-host is repairing safe resumption before op38 while keeping a possibly submitted completion on exact read-only recovery. Authoring operations70/71 alone are not physical effects or Store acceptance and should not permanently strand an attempt. Uncertain BEGIN/claim recovery remains a separate obligation. The concrete base's older Host will need an explicit qualified successor upgrade with matching settings/profile and Store validation before INSTALL; do not remove the existing artifact identity check as a workaround.

Event27 owner custody is being implemented by fn-contracts. Its issue/recovery operations72/73 are operator-private in the committed broker, as are74/75; the client must use that private socket. Event26 reserve submission remains a different ordinary-call path. Main/Json/event26 routing belongs to fn-mini-review, physical lifecycle to agent-api-host and mini-app-contract, runtime integration to runtime-review, native fixtures to client-session, builds to build-native, and review/Git to root.

Next: certify the successor, inspect the retained event22 plan with that linked executable before the expensive fresh run, finish concrete base creation, then perform actual signed app INSTALL/create on that Store. Continue physical STOP/restart, controller lifetime dispatch and grant custody. All two-user web/API/CLI, actual-model Hermes, bounded authority, hard/soft disconnect, selective fn publication/receive and latency requirements remain open until integrated evidence exists.
