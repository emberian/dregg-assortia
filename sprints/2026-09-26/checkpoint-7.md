# Overnight construction checkpoint — September 26, 10:57 UTC

The goal remains active. This follows [checkpoint 6](checkpoint-6.md). The swarm is still building the shared service through the actual Mini kernel and fn. This is an integration checkpoint, not a public launch.

## Actual SSH entry and the missing-result problem

A private loopback SSH daemon on persvati now exercised the forced-command entrance into a persistent Mini grain controller. Soft EOF let a bounded worker finish and settle. Hard EOF killed the exact worker unit and its captured cgroup processes, fenced the gate, and produced the signed Mini generation fence with its allowance held. Audited reconciliation then settled the retained allowance. The SSH fixture was stopped after the run; no shared authorized_keys or fn deployment was changed. [Exact source identities, signed views and observations](https://github.com/emberian/minidregg/blob/1995529/deploy/grain-host/SSH-LIVE-2026-09-26.md).

The first SSH Hermes prompt successfully read and published object 7003 through the Mini MCP tools. Unmodified upstream Hermes ACP 0.21.3 ran in the gated Linux worker against the deterministic local model fixture. Its publication response reached Hermes, the worker stopped, and both parent and tool charges settled. A second SSH attachment loaded the same conversation and committed field 2 = 2, but Hermes received a tool timeout first. That second prompt is a failed user interaction with a real committed effect, not a refused mutation.

The cause is now specific: Mini's inner broker still waited only 300 seconds even when the operator selected a 1500-second worker lifetime and a longer upstream MCP timeout. The older Mac synthetic ACP recipe independently reproduced it; its full assertion remains red despite a confirmed native publication. [Retained failure evidence](https://github.com/emberian/minidregg/tree/552ae3a/docs/evidence/2026-09-26-grain-mcp-deadline). [1b478d9](https://github.com/emberian/minidregg/commit/1b478d9) aligns the bounded broker deadline and journals exact confirmed publication receipts for read-only lookup and presentation on a later prompt. It must cover completed ACP prompts whose tools reported failure, as well as interrupted prompts. Those new receiving checks are still pending.

## Provider custody and retry behavior

The separate native provider fixture passes signed reserve, over-budget refusal, unchanged-state refusal and stale-parent-witness refusal after a hard fence. It uses a distinct provider subject and purse; this gate makes no network claim. [Recipe and selected receipts](https://github.com/emberian/minidregg/tree/552ae3a/docs/evidence/2026-09-26-grain-provider-direct).

[e475072](https://github.com/emberian/minidregg/commit/e475072) repairs a concrete duplicate-send path: recording an upstream response after the waiting HTTP side timed out could otherwise clear the hold and permit an SDK retry to forward again. Exact same-prompt responses now have a durable replay entry before settlement clears the hold; ambiguous delivery retains the attempt. Focused socket-failure tests and integrated Rust checks pass. This is not cross-prompt deduplication or proof of a provider invoice.

A fresh task 7201 is now exercising that gateway with actual Hermes and a dummy key. At this checkpoint, two local model requests have each passed signed provider reservation, retained HTTP response and signed settlement, and the joint Mini publication has confirmed. The final MCP response, final signed readback and complete prompt settlement are still being observed. No paid provider request or TLSNotary assurance is claimed.

## fn correspondence and durable publishing

The coherent reader profile and native builds now handle the real 391,022-byte fn report that the earlier reader refused. The actual grain-R run has passed fn signing, A acceptance, peering, B restart/verdict verification, and B's typed opcode-12 decision. The subsequent signed 717 KiB B Mini call also confirmed after about nine minutes of CPU-heavy admission. B ACK and Q return are still in progress.

The selected-profile maximal synthetic frame also passes: the complete JSON plus opcode is 11,568,847 bytes, below the 12,102,760-byte cap, with strict inner/outer roundtrips. [Mac/Linux build scope and frame evidence](https://github.com/emberian/minidregg/tree/fb1a104/docs/evidence/2026-09-26-mini-bbf). This synthetic result is distinct from authenticated fn evidence. The Mac and Linux build manifests have different grain worker-authoring baselines; they must not be called identical source images.

Native equal-current skip ACK retry returns byte-identical acceptance. The client retains one bounded exact ACK retry and can recover its archive after an ACK-before-archive interruption; coverage remains distinct from exact ACK success. [Client change](https://github.com/emberian/minidregg/commit/ac30b1b), [recovery evidence](https://github.com/emberian/minidregg/commit/b634048).

[a3d99fb](https://github.com/emberian/minidregg/commit/a3d99fb) adds read-only historical outbox export and reservation-continuity endpoints. Their coherent narrow compilation passes; a linked host is being built. A Rust origin publisher is being integrated around exact carrier custody, signed Mini outbox acceptance, historical readback and protected fn POST. It distinguishes duplicate acceptance, conflicts, explicit do-not-repost uncertainty and one bounded exact transport retry. Its local crash/race tests pass; the native publisher journey remains pending. A reusable Lean grain-origin renderer is also under construction. Neither prepared outbox custody nor source compilation means an article was delivered.

## Core performance and useful resources

Matched measurements on the same quiet accepted-22 Store show warm signed queries falling from 24.8–33.7 seconds to 7.1–8.4 seconds with the earlier combined host. All compared responses are byte-identical. Cold replay remains about 170 seconds. [Paired evidence](https://github.com/emberian/minidregg/blob/fb1a104/docs/evidence/2026-09-26-grain-performance/linux-paired-accepted22.md).

The large report probe exposed quadratic list traversal in the cSHAKE absorber: every block rescanned the input prefix. [7941bcd](https://github.com/emberian/minidregg/commit/7941bcd) replaces it with forward suffix traversal and proves equality with the indexed definition for every input, plus equality of complete cSHAKE outputs. Narrow conformance/vector compilation passes; the native performance improvement is not yet measured. A second optimization uses the loaded image's proven canonical bytes and is being extended to share one boundary digest across grant checks. These are semantic-preserving core changes, not a relaxation of authorization.

Direct signed create/edit/read of a content workroom has passed. A fresh task 7301/7302 will now exercise those actions through actual Hermes, separately from the active provider task and the retained older 7101 fixture. The intended content lives in Mini's resource page. No successful Hermes content-workroom journey is claimed yet.

Claude's fn checkout and protected hbox node remain outside this swarm's write scope. No asset operation or public onboarding occurred. Root continues reviewed commits/pushes and graph updates; Sol lanes continue the native receiving, recovery, hosting and content work until ember returns to choose release scope.
