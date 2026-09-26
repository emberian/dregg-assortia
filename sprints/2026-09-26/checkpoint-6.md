# Overnight construction checkpoint — September 26, 10:15 UTC

The goal remains active. This follows [checkpoint 5](checkpoint-5.md). Mini source through `0329a85` is checkpointed; the shared service is still being assembled and exercised.

## Reconnect and a committed operation with a missing reply

The actual upstream Hermes session reload succeeded using its retained database and the same session ID. Its six existing messages were loaded before the second prompt. That prompt eventually committed a second joint Mini publication: attempt 48 returned confirmed/installed, accepted count 20. Independent signed readback of object 7003 showed field 0 = 1 and field 2 = 2, at root `113165090123915682967404063493066207533634109815478468793224753513096677075760`.

This was **not a successful second Hermes tool response**. Hermes's 300-second MCP timeout expired while the native reserve was still running; the scoped worker later reached its 600-second lifetime. Mini subsequently confirmed the settlement. The controller retained the operation and the stranded prompt/worker state. Physical recovery, exact receipt reconciliation and a useful explanation to the next conversation are necessary before another prompt. Increasing a timeout alone does not close this case.

The private run is `/tmp/mini-hermes-provider-codec/evidence-real-r5` on persvati; the resumed runtime/MCP binary is `023be6b4…`. Its Mini host was the older Linux B image `faf1f837…`, not the faster combined image. Retained attempt timings show repeated signed queries and preparation dominating the delay. Paired measurements on isolated Store copies and a proof-preserving reduction of repeated image hashing are underway.

Mini [516c178](https://github.com/emberian/minidregg/commit/516c178) adds a fixed per-command worker lifetime of 1–1800 seconds and places the generated hosted-provider MCP deadline 60 seconds below it. It preserves the previous 600-second default and old configuration serialization. Focused Rust checks and the actual systemd launcher probe pass. These are bounds, not a guarantee that a later MCP call finishes before the whole worker deadline.

## Real grain correspondence and ACK correction

The original r5 publication's 191,283-byte R source has now been signed with fn's existing v2 carrier route, accepted and durably stored at A, peered to B and natively verified there. Both article counts are one. Fn's older `hybrid-author` control encoder refused this source because its input limit is 65,535 bytes; the qualified image already supports the larger signed carrier through protected NNTP POST. No fn source or live-node configuration was changed. The second Mini publication is being exported separately, retaining its timed-out Hermes-response qualification.

B Mini admission then exposed a concrete profile mismatch: fn's real poll report is 391,022 bytes, above Mini's older 196,608-byte Store-event bound. Mini refused before authoring an intent. The carrier itself is 198,883 bytes. The codec lane is deriving consistent event, inbox, report and host-frame bounds from the qualified fn source/carrier profile; the fix requires a new source-matched host and actual receiving run. B admission and Q return are not yet green.

The earlier manual ACK framing failures were traced to a **missing `FN_B3_IMAGE` environment variable in the restarted probe service**. They were not evidence of a production framing defect. With the environment restored, native host `d3fef24a…` returned exact `durable-accepted` for the current article cursor (position 23), preserving fn Store sequence/transaction 22/22. An older skip cursor returned distinct `covered-by-durable-frontier`. [29f6e17](https://github.com/emberian/minidregg/commit/29f6e17) retains the correction and fixes bridge cleanup so it cannot hide the original failure. Equal-current skip retry and automatic ACK recovery remain separate gates.

[4d0fdee](https://github.com/emberian/minidregg/commit/4d0fdee) implements the unattended B consumer worker. A fresh native run advanced neutral pages, woke for one actual R, admitted it, acknowledged it, stopped its ACK self-tail, and remained quiet after restart with unchanged article hints. Wake hints come from authenticated, certificate-pinned NNTP; Mini's native poll decides the work. A second distinct R after that restart is not yet tested. [5e1fde4](https://github.com/emberian/minidregg/commit/5e1fde4) exposes bounded, path-free prepared-origin opcode 16 and preserves historical coverage as distinct from exact ACK success.

## Build and custody convergence

- The [combined Linux host](https://github.com/emberian/minidregg/tree/b2e52e4/docs/evidence/2026-09-26-mini-linux-combined), SHA `31a00492594a9abbde4541fef687f4d6a2fd2cac06c1645e604178a3e7f18179`, passes all 165 transitive source checks and four artifact checks. It includes catalog/outbox, ACK handling, plural workers and faster session observations. Fresh native provider and SSH lifecycle fixtures use it.
- The [catalog umbrella](https://github.com/emberian/minidregg/tree/0329a85/docs/evidence/2026-09-26-mini-catalog) passes literal `lake build Minidregg`, with 594 source hashes verified. Its exact frozen scope excludes later ACK, plural-worker and pinning edits; a green umbrella is not inherited by newer code.
- [e240e53](https://github.com/emberian/minidregg/commit/e240e53) pins private copies of local fn helpers, verification PEMs and origin storage helpers for a host lifetime, while retaining stable logical identities in accepted records. Origin/outbox alias rejection checks resolved paths and device/inode identity. Isolated path-swap and old-JSON compatibility probes pass. The Mac pinning image `180f81c3…` has linked; full native receiving with these copies remains a separate check. A remote image behind the local bridge still requires operator custody.
- [16b9bed](https://github.com/emberian/minidregg/commit/16b9bed) presents carried content create/edit payloads, including exact untrusted text, in the native fn inbox view. This is presentation of admitted provenance, not automatic application of another node's resource mutation.

Matched next-call measurements on identical copied Stores found exact byte-equivalent accepted outcomes, but **no measured submit speedup** from the later durable readback change: 16.810 versus 17.090 seconds. The earlier 3.3× warm-query improvement remains valid at its own measured source. [Performance evidence](https://github.com/emberian/minidregg/tree/b2e52e4/docs/evidence/2026-09-26-grain-performance) preserves both findings.

## Current receiving work

The immediate paths are real SSH entry into a persistent native grain; hosted-provider reservation, refusal and interruption; real content-resource create/edit/read through Hermes; grain-origin fn admission and reply; and safe recovery when an operation commits after the agent times out. A proposed native reservation-continuity query binds the complete original receipt and call to verified history and refuses later provider writes. Its evolving proof/implementation does not yet replace the conservative provider send fence, and it cannot alone establish current parent authority or atomicity with external HTTP.

No paid provider request, TLSNotary assurance, public onboarding or asset operation is claimed. Sol lanes continue implementation and native acceptance; root owns integration, scoped commits/pushes and this record. Claude's active fn tree and protected hbox node remain untouched.
