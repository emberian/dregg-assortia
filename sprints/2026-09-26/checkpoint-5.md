# Overnight construction checkpoint — September 26, 10:00 UTC

The overnight goal remains active. This advances [checkpoint 4](checkpoint-4.md) with an actual upstream Hermes publication, signed hard-disconnect recovery, measured interactive improvements, and a durable fn consumer worker. The hosted service is still converging; the passes below belong to their named artifacts.

## Actual Hermes publication

Unmodified Nous Hermes ACP ran in the Linux grain sandbox against a deterministic local OpenAI-compatible endpoint. It read object 7003 through the keyless Mini MCP tool, used that observed root in `mini_publish`, and obtained a confirmed native joint transaction. The signed result had accepted count 10; an independent signed resource query showed field 0 becoming 1 and the root changing. The final journal had no pending operation, child, hold, or unresolved external effect.

The [r5 evidence](https://github.com/emberian/minidregg/tree/main/native/hermes-test-provider/evidence/2026-09-26) pins controller/MCP binary `708f2617…`, source `b4a2449…`, and exact accepted call `08039ed4…`. The earlier r4 failure exposed an actual joint-observation bug: the controller supplied duplicate grants in the wrong order. Mini correctly refused it. The repaired controller supplies one observation grant for each command target in order; [6e1128a](https://github.com/emberian/minidregg/commit/6e1128a) records that repair and further source work.

This is a real Hermes/tool/kernel integration test, with deterministic model responses and no paid provider request. It establishes the initial conversation only. The frozen runtime looked for Hermes's database in the wrong workspace; the actual scoped database contains the retained session and its six messages. A narrowly repaired controller is now testing `session/load` and a second publication without silently creating a new conversation.

The accepted call also exports a 139,470-byte portable Mini package, SHA prefix `9be53614`, independently re-admitted by the Linux and Mac hosts. A Lean renderer checked its grain settlement, parent witness and publication leg, then produced a strict 191,283-byte fn R source (`8b2da29b…`). Actual fn signing, transport and B admission of this new grain-produced source are next; do not substitute the earlier small synthetic exchange for that result.

## Interruption and latency

Both Mac and Linux runs of immutable controller source `55045ec6…` reached signed parent generation 2, status 5, remaining 96 and reserved 3 after hard disconnect. The controller detached while retaining the held allowance; Linux also showed the exact worker unit inactive and its launch gate fenced. Stale tool retry was refused, and signed administrative reconciliation completed. This closes the earlier completion/cancel and duplicate-disconnect failures at those gates. The full recipe remains incomplete: Linux's later ACP wait expired shortly after the slow native reserve finished, before a worker launch was observed. The timeout is being corrected and the later publication phase uses a newer grant-order fix.

[Matched measurements](https://github.com/emberian/minidregg/tree/322334c/docs/evidence/2026-09-26-grain-performance) on the same copied Store and signed input reduced warm challenges from about 8 to 2.4 seconds and signed resource queries from about 18 to 5.5 seconds. Outputs were byte-identical. Cold replay still took about two minutes. A real SQLite rollback and same-height fork still permanently poisoned the faster session. These timings exclude the subsequent exact-CAS-readback optimization.

A new Mac catalog host, SHA `9a42dca4e181ad67c3de469fdb1f14d5649fb9cddc80fc6e88b4dd386cbb9dbe`, has linked from the exact `229c3a3` source overlay: 165 Host sources and four linked-artifact checks pass. It adds prepared outboxes, fn inbox presentation and the CAS-readback optimization to the measured session code. Its full umbrella gate and native catalog/performance probes are separate work. Later plural worker policy and ACK diagnostics are excluded from this binary.

## Sustainable fn coordination

The [fresh neutral-page exchange](https://github.com/emberian/minidregg/tree/9dc8abd/docs/evidence/2026-09-26-fresh-fn/public-b-skip-bbf) passed 111 steps: two signed progress-only records advanced 0→16→21, the first survived a Mini service restart before ACK, and the subsequent R/Q exchange completed on both distinct nodes. Read-only native replay recognized both exact signed tag9 records. Since fn ACK itself appends a journal event, draining until idle would process its own acknowledgments indefinitely.

[f74125f](https://github.com/emberian/minidregg/commit/f74125f) adds `consumer-drain-once` to the existing Rust client. It durably prepares the exact signed call before sending, retains uncertain operations, and stops after a publication, short neutral page, idle result or page bound. A fresh native run has now processed both neutral pages through this worker and archived their confirmed transactions. An unattended worker is being added using authenticated NNTP article counts as wake hints; the Mini poll remains authoritative. ACK-only events leave those counts unchanged.

Separate post-run ACK retries exposed unexpected child-output framing, despite successful direct re-projection of the exact retained bytes. Diagnostics and actual socket reproductions are underway. An older cursor can also legitimately be behind fn's current acknowledged position. Recovery must distinguish an exact ACK from a fresh, scope-matched durable frontier that already covers the position; it must not invent evidence that the original ACK reply was received.

[229c3a3](https://github.com/emberian/minidregg/commit/229c3a3) adds a Mini-admitted prepared-R outbox and dynamic Q parent selection. Preparation requires native fn signature verification and byte equality with the live origin Mini's exact export. It is not a claim that fn posting occurred. The origin and outbox deployments are distinct, preventing recursive inclusion of retained carriers in their own origin history. Maximum-size codec/content-page checks pass; two successive real publications and lifetime executable custody are being integrated.

## Next receiving gates

- Finish actual Hermes conversation reload and carry its accepted publication through fn into a signed, readable B inbox.
- Exercise two successive prepared origins and replies through the catalog, and unattended consumer wake/restart without self-ACK charges.
- Finish native hosted-provider admission and interruption/recovery. The Rust gateway already has local fake-upstream checks; controller wiring, separate provider-task budget and audited ambiguous-outcome recovery are under review. Lean policy authoring now supports bounded distinct workers under one grain generation while preserving singleton bytes. No real provider spend or TLSNotary claim has been made.
- Exercise SSH's forced-command entry against a real persistent grain and current native host, then leave a reproducible provisioning path. Existing SSH control-only probes are not that acceptance.
- Add an actual content-resource workroom note/create/edit/read fixture using the existing Mini content semantics and MCP path. The scalar publication proves the joint path; the workroom should use the same system, not a separate application store.

Root continues scoped commits/pushes and handoff maintenance with Sol lanes. Claude's active fn tree and protected live hbox service remain untouched. No asset or stake transaction has been made.
