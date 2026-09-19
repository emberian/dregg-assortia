# Cycle 1 evidence — umbrella green, native integration pending

Archived September 19, 2026 by the content lane from `/tmp/minidregg-cycle-20260919`, with a later update for the completed 20:25–20:31 UTC gates. **The full `Minidregg` umbrella is green; complete native integration remains pending and slow.** A separately identified native host accepted one matched-input birth in 223.78 seconds. That result does not establish the complete multi-resource journey or a speedup. Earlier failed/interrupted evidence is preserved below.

## September 19, 21:03 UTC component update: birth and order computation

[Birth and order sharing](birth-and-order-sharing/README.md) preserves general
equality proofs, standard axiom pins, exact source hashes, lane-reported
successful empty compiler logs and bounded generated-C/profile facts. A later
matched birth with theta plus birth sharing completed in **49.43 seconds**,
versus the archived **223.78 seconds**, using identical signed-call/genesis
inputs and returning identical 132-byte outcome files. This pair measures
about 4.53× improvement; it does not isolate the component contributions.

An independent authorized-query stall was traced to recursive bit extraction
inside actual canonical policy-witness generation. The exact direct-bit
compiler substitution passes its bounded source check and appears in the
freshly generated `PredCompile` caller. **Its native query retry and the full
journey remain pending in this component record.** No configuration, raw
signed call, genesis/store contents or full process sample was archived.

## September 19 update: completed gates

Later component/runtime progress is recorded in the [integration checkpoint](../cycle-1-integration-checkpoint.md), including the [33.55-second task query](order-query-benchmark/README.md). The final combined umbrella and full native journeys remain separate pending integration checks at that checkpoint.

| Evidence | Captured result | Limit |
|---|---|---|
| [Final legacy native journey](final-legacy/README.md) | Complete exit-0 PASS in 1,066 seconds: six mutations, two grant-preserving rule changes, delegation, hostile-history refusals and every original receipt recovered after restart without changing final bytes. | Scalar/authority regression coverage; the New World task/content scenario remains separate. |
| [Final committed-source build](final-build/README.md) | Final `lake build Minidregg` passed in 177 seconds; native link and runner build passed. All 581 compiled Lean files and all 153 native host source files match Git commit `12e6608`. | The full-gate and runtime-tested executables have separate hashes and object namespaces, with matching source. Complete New World and legacy acceptance remains separate. |
| [Final Rust-client journey](final-client/README.md) | Complete 444-second PASS against combined host `0da9f139…`: actual lost-reply recovery, mixed resource transaction, exact retries and authorized post-state queries. Focused Rust tests 4/4 pass. | This completes the client scenario, not hosted Hermes or the broader New World/legacy kernel scenarios. Earlier fixture failures are not relabeled as passes. |
| [Round 6 full gate](full-gate-green-20260919T202556Z/README.md) | `lake build Minidregg` completed successfully (9107 jobs); wrapper reports 59 seconds. `Host.Main:leanArts` also passed. Root's captured source recheck reports all 584 listed source files matching. | A successful compile and link do not prove native acceptance. The recorded snapshot Git head precedes its source overlays; use the exact source manifest. |
| [Matched birth benchmark](birth-benchmark-20260919T202801Z/README.md) | Exit 0, public outcome `confirmed`/`installed`, accepted count 1, wall time 223.78 seconds. | Same signed birth and genesis as the preceding native run, using independent fresh storage. The benchmark binary differs from the full-gate binary. No comparable uninterrupted old timing is retained, so there is no measured speedup claim. |

No private signing keys, runtime deployment configuration, raw state/artifact stores, or full process samples are included. Paths retained in manifests identify source trees, public executable locations and evidence directories. Copied source inventories contain file names and hashes, not their contents. The initial `../cycle-1.md` and its graph Source/hash are unchanged.

## Contents and interpretation

| Directory | Evidence | Scope |
|---|---|---|
| `waterfall/` | Original study record, search/replay source, bounded search logs, canonical codec log and command scripts | Three successful proof searches and independently compiled scripts with no Waterfall imports, as recorded by the completed lane. Canonical codec log retains transitive axiom reports. The optional tactic is not a new production dependency. |
| `cast-injectivity/` | Empty original compiler log, exact source hash, theorem/axiom-pin excerpt, native source-overlay ledger and completed component-build lines | Root reports receiving the lane's successful direct tool exit. The empty log alone does not encode an exit status. The later native build explicitly records `Compiler.PredCompile PASS 32s`; this is one completed module, not the entire native build. |
| [`theta-sharing/`](theta-sharing/README.md) | Original lane record, unchanged primitive fixture, six timing logs, source hashes and equality/axiom-pin excerpt; empty proof/conformance logs with lane-reported exit 0 | Proved theta compiler substitution; matched Lean `--run` primitive median 4.147 s → 2.059 s (about 2.01×). Component evidence only: no native-host speedup or complete operation-acceptance claim. Optimized source is identified by hash and root-reported commit `722a8bb`. |
| [`birth-and-order-sharing/`](birth-and-order-sharing/README.md) | Selector/identity and bit-function equalities, standard pins, source hashes, bounded compiler/C/profile evidence and matched birth manifests/timings/outcome hashes | Matched birth 223.78 s → 49.43 s with identical receipts. Direct order-bit implementation is present in generated consumer C; no completed native query or complete-journey claim. |
| `import-boundary/` | `final.log` | Captured Theory and Selvage import-boundary checks report `OK`. |
| `source-snapshots/umbrella/` | Initial snapshot manifest, complete source-hash inventories, exact overlay ledgers 1–4 | Identifies source snapshots and subsequent source-only overlays. Round 4 is split between content and remaining consumers. These ledgers are not acceptance results. |
| `source-snapshots/native-baseline/` | Baseline snapshot manifest and source-hash inventories | Identifies the separately built initial native host source. |
| `full-gates/initial/` | Command, wrapper result, bounded failure lines, final summary and original full-log hash | Full `Minidregg` gate starting 19:03:53 UTC failed. Missing policy-revision fields and resulting axiom failures required consumer migration; the pins were not waived. |
| `full-gates/warm-optimized/` | Same bounded evidence format | Warm full gate starting 19:41:19 UTC also failed, exposing further consumer migration. Neither failure is relabeled as a pass by later component checks. |
| `native-baseline/` | Build manifest/log, acceptance manifest/log/verdict, bounded hot-path counts | A linked native host was built, but its first new-world acceptance run was intentionally interrupted during initial birth preparation. This was a performance investigation, not an admission rejection or successful journey. |

## Native baseline ceiling

The baseline binary hash is `688d277f7c1364ad5cdcca113d068cde884618b148b2b4e992d7f7a664a9987c`. Its build explicitly reports `umbrella=0`: 153 source modules compiled for the host, without establishing the complete library gate. Acceptance ran from 19:32:53 to 19:37:13 UTC; the manifest records exit 1 and 258 elapsed seconds. The child host exited 143 after root terminated it. Only setup, key and signature checks completed before interruption.

The full process sample is deliberately omitted. `native-baseline/hot-path-counts.tsv` retains selected inclusive stack counts, and `original-sample.sha256` identifies the original sample. Counts along a stack overlap and must not be added or interpreted as timing percentages. The sample places repeated cast-injectivity work beneath policy admission during observation preparation; it does not measure a before/after speedup.

## Source identities and archival limits

The cast optimization source hash is `873cb99baeea907ff0614cd5163a336fb95195e09b6ac3479950ae90c07593f5`; the integrated canonical codec hash is `5a2b60f996d4a5c85628bce8d70070e91cb3441802167b3fc52b67e818201e14`. Root identifies commit `6cff3aa` as the durable source for the optimization's theorem statements and axiom pins. `PredCompile.source-excerpt.txt` is a review excerpt, not a standalone Lean module.

Waterfall's original README distinguishes lane-reported completion from exact preserved compiler output and pins its upstream/toolchain inputs. Its scripts retain original temporary paths; they document the commands and need path adjustment before any rerun. Nothing was rebuilt or reexecuted to create this archive.

Failure excerpts are line-numbered selections from the complete logs, whose SHA-256 values are retained. They omit repetitive proof states and compilation warnings. Snapshot manifests and overlay ledgers are copied without editing. The content round-4 before hashes were recovered from the initial snapshot manifest and independently confirmed by removing exactly the five added revision-witness lines in a read-only stream; the ledger was written after that overlay's direct check began.

The archive now includes the completed round-6 full gate, single-birth benchmark and bounded theta-sharing component evidence. It has not received a completed full native journey, concluding cycle narrative, or graph completion links. Root owns those updates; no graph work was closed by this archival task. `SHA256SUMS` was regenerated for these additions while preserving the bytes of every earlier evidence file except this index. Later additions require a new manifest or explicitly regenerated manifest.
