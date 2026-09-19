# Cycle 1 evidence — final native integration in progress

The full Mini umbrella and native builds are green. The legacy native scenario
and Rust mixed-resource client scenario have completed successfully. The New
World task/content scenario and an additional Rust authority recipe are still
running or being completed. Builds, source proofs, runtime cases and deployments
remain distinct claims.

| Evidence | Captured result | Scope |
|---|---|---|
| [Client API build](final-client-api-build/README.md) | All 581 compiled source files match `b119f86`; umbrella and native link pass. | Exactly one source delta from the preceding build: `Host/Json.lean` exposes policy address and editable predicate. New Rust authority recipe pending. |
| [Core committed-source build](final-build/README.md) | Umbrella passed in 177 seconds; native host and compiled runner linked. All 581 umbrella/Host files and 153 host-source files match `12e6608`. | Full-gate and runtime-tested executables have separate hashes/object namespaces, with matching source. |
| [Legacy native journey](final-legacy/README.md) | Complete exit-0 PASS in 1,066 seconds: six mutations, two grant-preserving rule changes, Alice-to-Bob delegation, hostile-history refusals and original receipt recovery without changing final bytes. | Complete scalar/authority regression; New World remains separately gated. |
| [Rust mixed-resource client](final-client/README.md) | Complete 444-second PASS on host `0da9f139…`; actual lost-reply recovery, mixed transaction, exact retries, final authorized queries; focused Rust tests 4/4. | Does not yet exercise policy installation, delegation and revocation through Rust JSON. |
| [Birth and order sharing](birth-and-order-sharing/README.md) | Matched birth 223.78 s → 49.43 s, identical signed-call/genesis inputs and identical receipt bytes. General equalities and generated-code evidence are retained. | About 4.53× for this matched pair, combining changes; not an isolated contribution or all-operation speedup. |
| [Task query](order-query-benchmark/README.md) | Formerly stalled exact signed query completes in 33.55 seconds after the proved direct-bit substitution. | Earlier attempt was interrupted; no exact speedup ratio is claimed. |
| [Theta computation](theta-sharing/README.md) | Matched primitive median 4.147 s → 2.059 s, with general equality and existing conformance checks. | Primitive measurement, not native-host latency. |
| [Earlier round-6 umbrella](full-gate-green-20260919T202556Z/README.md) | Full umbrella and Host.Main checks passed before subsequent performance fixes. | Historical snapshot includes preserved unrelated worktree imports; later committed-source builds identify the final source. |
| [Earlier birth](birth-benchmark-20260919T202801Z/README.md) | Complete 223.78-second installed birth, accepted count 1. | Baseline for the later matched 49.43-second result. |

The [integration checkpoint](../cycle-1-integration-checkpoint.md) is an immutable,
dated intermediate record. Component archives retain their original pending
language; the completed results above supersede that status at their stated
scope. Earlier failures and deliberate interruptions remain recorded as such.
No private keys, deployment configurations, raw signed calls, stores or full
process samples are archived. The initial `../cycle-1.md` and its graph Source
hash remain unchanged.

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

The archive now includes the completed native legacy and Rust mixed-resource journeys and both final source-matched builds. The New World and additional Rust authority results, concluding cycle narrative and graph completion links remain pending. No work item is closed by an archival update alone. `SHA256SUMS` was regenerated for these additions while preserving the bytes of every earlier evidence file except this index. Later additions require a new manifest or explicitly regenerated manifest.
