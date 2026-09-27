# Checkpoint 42 — shared-app recovery and fresh deployment preparation

September 27, 2026. Continues [checkpoint 41](checkpoint-41.md). The integrated platform goal remains active. No joined two-human/two-agent deployment or real-model hosted session is established by this checkpoint.

## Qualified client and pending native Host

Mini **dc3b231**, pushed, records a fresh Linux **007b513** sharing client build: SHA-256 `a339b384f9a6c15d9c3f64e5df243b230da7e5a50d0b252cafbbcd94ad8e47ee`, 83/83 tests. Root independently checked the remote executable and compile/test evidence. The earlier cached-target result remains explicitly rejected. The same commit records the **9746c47** SQLite and signature helper builds; those are build results, not native journey results. Portable manifests and logs are in Mini's `docs/evidence/2026-09-27-native-007b513-client/` and `2026-09-27-native-9746c47-helpers/`.

The full **9746c47** Host build remains live on hbox. Root observed user unit `minidregg-9746c47-host-r2.service`, MainPID `2549629`, active/running with approximately 3.1 GB memory and module 94/292 underway. The source archive and monitoring commands remain in checkpoint 41. No replacement build was launched. Its eventual executable and closure manifest must be verified before the event22 fee fixture or fresh deployment uses it.

## Recovery integration under review

The resident is being extended to up to eight distinct agent routes alongside separate human entrances, all using one shared application process and RPC driver. Each controller retains separate authority, custody, session and attempt records.

Review found two global locks after an interrupted app request. The implementation now supplies a non-cloneable, exact-dispatch fence only when no RPC was queued or the worker has acknowledged release. With that fence, hostd can retain the operation's durable uncertain tombstone while freeing the shared slot. A two-second cancellation-acknowledgement timeout remains fail-closed. A successful RPC followed by response formatting or retention failure also needs this fence; the staged caller handles that case.

An initial review incorrectly inferred that the separate native-submit marker blocked other agents. Following its actual directory construction and the resident's distinct per-route directories corrected this: the marker is per agent route. Its removal on uncertain worker release is therefore being withdrawn; the interrupted agent retains its hold pending reconciliation. Other participants proceed through the released hostd shared slot and their own native markers. Exact inode/byte checks remain appropriate for normal definite marker removal. Worker release does not establish that the application's effect was absent or rolled back, and never authorizes replay of the interrupted operation.

Exact retained HTTP reply recovery, historical read-only inspection, and reverse reserve inspection are also being joined. A mere `definite.json` filename cannot establish a verified retained result: digest/binding failures must remain terminal without a recovered result. The controller and resident must agree on this distinction.

The combined hbox Rust check r6 reached compilation but failed on a pointer type inference error in `agent_api_native.rs`; no tests ran. The owner is correcting that error and an unused-mut warning. Earlier component greens do not qualify this combined cut. A real A/B application-loop test still needs source-qualified op46 fixtures.

The subsequent r7 snapshot compiled and ran 102 library tests: 100 passed and two failed (agent saved-binding recovery and the preexisting spawn-gate handshake test). The owner reported the hostd/RPC component cancellation and invalid-response-to-second-participant cases passing. This is not a green combined suite or a native two-agent journey. The per-route marker correction above follows that snapshot and requires its own check.

## Next deployment and transport gates

Fresh GitWeb preparation scripts under Mini `scripts/spk-platform/` reuse the existing birth sources and actual signed SPK. An isolated preparation check generated custody and composed the config overlay without creating a Store. Root review requested consistent canonical-path, dangling-symlink and protected-ancestor checks before committing that preparation cut. Actual INSTALL, START, installed-version sharing and participant enrollment remain unrun.

The payer helper and hosted controller are joining source-authored reserve and paid-dispatch plans. Full HTTP bytes must match the original retained authorized request; the compact selector carrier intentionally contains empty HTTP and is not interchangeable with that request. The payer helper independently reauthors the current op48 plan before signing. This path still needs combined qualification and actual paid application delivery.

Fn receiving routes **60–65** were reserved in pushed Mini **5ab5a70**. Their implementation remains WIP: event17 selected-page coverage, event19 empty-page coverage, typed source-owned poll planning, detached assembly and joined receipt checks before ACK. Selected ACK must require the original event13 receipt plus exact event17 coverage; empty ACK requires event19. Endpoint/scope/control come from the configured service. The intended node2 `selected-mini-gateway` namespace was last verified at ACK 0/frontier 2; the different node1 consumer is not evidence about it. No namespace reset or new publication was performed by this checkpoint.

The next convergence is the qualified Host, fresh INSTALL/START Store, version-1 tickets, two people and two controllers sharing that app, then delegation/revocation, restart/disconnection, selected fn exchange and an authorized real-model session. Separately green fixtures remain separately scoped evidence.
