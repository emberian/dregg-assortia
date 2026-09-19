# Cycle 1 component evidence — integration pending

Archived September 19, 2026 by the content lane from `/tmp/minidregg-cycle-20260919`. This archive is a bounded collection of completed component phases and failed/interrupted integration attempts. **No final full-umbrella or native acceptance PASS is recorded here.** The later integration result must be added separately by root.

No private signing keys, runtime deployment configuration, raw state/artifact stores, or full process samples are included. Paths retained in manifests identify source trees, public executable locations and evidence directories. Copied source inventories contain file names and hashes, not their contents. The initial `../cycle-1.md` and its graph Source/hash are unchanged.

## Contents and interpretation

| Directory | Evidence | Scope |
|---|---|---|
| `waterfall/` | Original study record, search/replay source, bounded search logs, canonical codec log and command scripts | Three successful proof searches and independently compiled scripts with no Waterfall imports, as recorded by the completed lane. Canonical codec log retains transitive axiom reports. The optional tactic is not a new production dependency. |
| `cast-injectivity/` | Empty original compiler log, exact source hash, theorem/axiom-pin excerpt, native source-overlay ledger and completed component-build lines | Root reports receiving the lane's successful direct tool exit. The empty log alone does not encode an exit status. The later native build explicitly records `Compiler.PredCompile PASS 32s`; this is one completed module, not the entire native build. |
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

The archive has not yet received final native/full-gate evidence, a concluding cycle narrative, or graph completion links. Root owns those updates. Check `SHA256SUMS` to verify the files present at this handoff; later additions require a new manifest or explicitly regenerated manifest.
