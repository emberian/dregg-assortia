# Resource-composition orientation (source-only, 2026-09-17)

## Evidence status

This report is a read-only source review. No build or test was run in this pass.
Statements called “tested” identify test source and assertions, not a newly observed passing execution. No captured current execution log was found for the document author → fork → resolve flow.

## Existing resource journey, accurately scoped

1. `starbridge-v2/tests/deos_desktop_conflict_is_a_state.rs:51-160` is an executable test scenario: a headless desktop over `demo_world()` opens a document, writes base text, forks a draft, makes main and draft diverge, holds a stitch conflict without advancing world height, then resolves it and asserts height advancement and heap read-back.
2. The underlying world is an embedded executor/ledger in the same process, not a remote node: `starbridge-v2/src/world/mod.rs:1-18`. `demo_world()` is constructed from `World::with_costs_and_timestamp`, hence is ephemeral (`world/mod.rs:2003-2008`, `2037-2040`; the `persist` field documentation says `None` for `new`/`fork` demo paths at `215-224`).
3. A normal editor edit first changes `dregg_doc` patch history, then writes/reseals the heap out of band, persists the JSON layout sidecar, and only then attempts a `SetField` revision turn: `starbridge-v2/src/deos_desktop/mod.rs:2983-3014`. The heap itself is not an executor effect.
4. `World::set_cell_heap` expressly mutates `heap_map` and reseals `heap_root` without running a turn (`starbridge-v2/src/world/genesis.rs:207-228`, `247-283`). The successful out-of-band write emits `HeapWritten`; it does not itself produce a `TurnReceipt`.
5. The following `SetField` revision is a real `World::commit_turn` / `TurnExecutor` route (`deos_desktop/mod.rs:2594-2611`; `world/mod.rs:1048-1056`). Since edit uses `prose_ok && commit_set_field`, a failed heap write suppresses the revision turn (`deos_desktop/mod.rs:3004-3008`). Thus the test’s post-resolution height proves the revision turn occurred in its ephemeral world; it does not make the heap write an ordered turn effect.

## Durable-image qualification

1. Durable `commit_turn` dual-writes an accepted turn and its exact write set, fail-closing on durable-record failure (`starbridge-v2/src/world/mod.rs:1148-1266`). That protection does not cover the document heap path, which bypasses `commit_turn`.
2. `genesis_mutation_would_break_reopen` returns true exactly when a durable image has a prior committed turn touching that cell (`world/mod.rs:986-1003`). `set_cell_heap` returns false before any mutation when that guard fires (`world/genesis.rs:224-235`).
3. The source explicitly documents the concrete result: the shipping document editor’s `set_cell_heap` path refuses from save #2 onward on a durable image; the `&&` suppresses its revision turn, and the layout JSON sidecar becomes the only prose copy (`world/genesis.rs:25-31`). The stated remedy is an ordered `Effect::SetHeap`.
4. There is durable guard test source, not a passing durable document-edit/reopen artifact: `world/mod.rs:3602-3641` opens a redb image, commits a turn, and asserts `set_cell_heap` refusal and no event. The document heap test (`starbridge-v2/tests/deos_doc_persists_to_cell_heap.rs:42`) uses `demo_world`, so its “reopen from ledger” is in-memory reopening rather than durable image recovery.

## Composition and sharing boundaries

1. Verified transclusion first resolves a live source through finalized-read/membrane machinery and then creates a host-document patch plus revision turn (`deos_desktop/mod.rs:2633-2649`). Its source-level test refuses a forged absent cell without text or height change and accepts a live source with `dregg://` plus cited receipt (`starbridge-v2/tests/deos_desktop_transclude_is_verified.rs:128-207`). This is a verified citation/reference; this review found no proof that it persistently materializes source content/version inside the host document.
2. `dregg-doc/tests/two_device_sync.rs:1-40` models two independently held `History` replicas, offline edits, a later pushout stitch, and settlement-tip authority checking. It is a strong semantic/test fixture, but this file does not provide deployed device transport/discovery/synchronization evidence.
3. `World::fork` is explicitly a throwaway deep-cloned what-if world; it does not mutate the live world and starts without live provenance/dynamics/replay tape (`world/mod.rs:772-795`). Do not conflate this with a durable distributed replica.
4. Hermes is one interface rail, not the document resource substrate. External `hermes-acp` remains a subprocess with base tools in addition to MCP (`deos-hermes/src/mcp_server.rs:1-34`); the internal Rust `HermesAgentPeer<B: LlmBrain>` uses the same ACP/gateway seam (`deos-hermes/src/agent_peer.rs:48-90`).
5. DreggCloud is documented as a separate service alongside rather than woven into the node/federation path (`docs/deos/DEVNET-DEPLOYMENT-REALITY.md:133-142`).

## Questions the product graph should make explicit

1. Is a social-resource share a live attenuated view, an independently durable replica, or a choice between them?
2. Is a transclusion a live verified citation, a version-pinned embedded copy, or both?
3. When can an authoring claim be shown as durable? For current Deos document editing: only the ephemeral/in-memory journey is evidenced; the durable second-save path is source-documented as refused.
