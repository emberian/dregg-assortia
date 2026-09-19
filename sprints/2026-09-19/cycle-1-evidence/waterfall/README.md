# Waterfall adoption study, 2026-09-19

This is scratch proof discovery. It does not change Mini's toolchain, Lake
dependencies, source closure, or assurance claims.

## Pinned input

- Official documentation: https://samth.github.io/waterfall/
- Upstream: https://github.com/samth/waterfall
- Commit: `4acadf6e12c06caac50b4e99e0753711b7426354`
- Package version: 0.1.0; Apache-2.0; no external package dependencies.
- Upstream toolchain: Lean 4.33.1. The official site also reports testing 4.30.0.
- Locally tested toolchain: existing Mini Lean 4.30.0, unchanged.

## Compatibility result

`bash build-430.sh` compiled all eight modules in the public tactic import
closure with the existing 4.30.0 executable, serially, `LEAN_NUM_THREADS=1`.
All eight returned success; individual output is under `logs/build-*.log`.
No upstream source patch was necessary. This is not an upstream full-test-suite
claim and does not test its optional observation modules.

## Why use it only during proof discovery initially

`waterfall?` records accepted search steps, renders ordinary Lean commands, then
reparses and elaborates their literal text from the original checkpoint with
error recovery disabled. Its root checks reject unassigned roots, unresolved
metavariables, and direct sorry terms. See upstream
`waterfall/Suggestions.lean:159` and `waterfall/Core.lean:643`.

This does not replace Mini's transitive axiom accounting. The desired workflow
is to copy the checked ordinary script into a separate file without importing
Waterfall, compile it again, and pin `#print axioms` output. This leaves no new
tactic dependency in deployed Mini's closure or the Theory layer.

## Experiments prepared

`TagSearch.lean` imports only `Theory.AuthorizationDeclaration` and Waterfall.
It attempts the actual inverse verb-tag fact currently used by
`Compiler.TypedAuthorizationRequestCodec`. It deliberately does not import that
Compiler file or its already-proved private target theorem.

`RecursiveSearch.lean` uses the actual live
`Compiler.ResourceAuthorityProjection.bytesSlots` definition. It attempts two
general laws: output length equals input byte count, and splitting a byte list
commutes with serialization when the suffix offset advances by prefix length.
The latter exercises induction with a changing index. Neither target theorem
already exists in its imported module.

Run a selected search using `bash run-study.sh TagSearch` or
`bash run-study.sh RecursiveSearch`. The script claims fleet seat2 atomically,
releases it on exit, prepends only the scratch Waterfall library to Mini's
existing `LEAN_PATH`, and limits Lean to one thread. Search explicitly sets
`cpus := 1`, low effort, and bounded heartbeat slices. Integration work has
priority over these optional experiments.

The initial search was queued behind native integration. The subsequently
released bounded window completed all three searches and independent replays.

## Final results

- Tag inverse: success, 92 attempts, 34,133,737 raw heartbeats.
- Byte-slot length: success, 32 attempts, 1,623,879 raw heartbeats.
- Byte-slot append: success, 47 attempts, 3,519,159 raw heartbeats.
- `TagReplayExact.lean`, `TagReplay.lean`, and `RecursiveReplay.lean` all compiled
  successfully without importing Waterfall. Exact axiom guards passed: length
  uses `[propext]`; tag and append use the standard three axioms.
- The normalized inverse-tag script was integrated with root authorization in
  `Compiler/TypedAuthorizationRequestCodec.lean`; the actual canonical module
  compiled to olean/ilean/C. Its consumer axiom footprints remain clean.
- Byte-slot lemmas remain scratch study artifacts, not unused production API.
- Durable concise record: `/Users/ember/dev/minidregg/docs/WATERFALL.md`.
- Final canonical codec SHA256:
  `5a2b60f996d4a5c85628bce8d70070e91cb3441802167b3fc52b67e818201e14`.

## Canonical input source hashes

SHA256:

```
1599d2af4fabbb666c846ae44a2adc70c0ff78e85b3f5c68c5820ca315253745  Theory/AuthorizationDeclaration.lean
08b6c99a76d21401b30775a4ef5904b41c0e2f35e2e438bae870ad8636f464a8  Compiler/ResourceAuthorityProjection.lean
fc6735aac9247901bf4419140478862d89169eb2c984a9a8550021391f8e8e54  Compiler/TypedAuthorizationRequestCodec.lean
```
