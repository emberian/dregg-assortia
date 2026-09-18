# September 17, late-evening implementation checkpoint

This is a checkpoint during an active shared-tree sprint. Commits are publication boundaries, not release or integration verdicts. No service was deployed and no token custody operation was performed.

## Published source

| Repository | Commit | Change and remaining boundary |
|---|---|---|
| breadstuffs | `c037d64ee` | Retain committed resource receipts when later attached JavaScript throws; propagate script failure and receipts through Hermes/MCP. Real bridge execution is being checked separately. |
| breadstuffs | `55ad7a19a` | Latch durable write failures, batch related storage writes, and propagate refusal through runtime creation, sessions and desktop startup. Ordered-history refinement and caller integration remain active. |
| minidregg | `698c10a` | First declared-action target/admission and actual-balance repair checkpoint. |
| minidregg | `3c65ebd` | Executable canonical policy-source codec v2, source-derived policy-step context, and dynamic policy selection from actual authority-page bytes and content storage. Installation controller remains active. |
| minidregg | `0c92e7b` | Complete the scoped declared-action repair through compiled/typed/page consumers, with admitted source-solvency and actual-post balance laws. Generic effect binding and composition are separate active repairs below. |
| dregg-assortia | `3a54a57` | Retain the mixed programmable-nexus intent, source corrections, opening investigations and autonomous sprint assignments. |

All listed commits reached their normal GitHub `origin/main`. Commit signing through 1Password failed, so these are unsigned checkpoints without a change to Git configuration. Breadstuffs' secret scan passed. Its existing dead-document-reference push gate refused publication; the retry used that hook's declared `DREGG_ALLOW_DEAD_DOC_REFS=1` override. This exception does not mark those references repaired.

## Evidence actually obtained

- **Captured remote execution:** `dregg-persist::tests::config_batch_rollback_and_reopen_keep_related_keys_atomic` passed on hbox, one selected test, 306 skipped, with `pbuild: VERDICT outcome=PASS`. The retained excerpt is [persist-config-batch.txt](evidence/persist-config-batch.txt). This run used the earlier WIP snapshot, not a full test of `55ad7a19a` or later history changes.
- **Reported targeted Lean checks, with root inspection of sources and saved logs:** five declared-action modules plus their unchanged page-registry consumer checked successfully. Import-boundary and scoped proof-hygiene checks passed. The compiler rejects inadmissible declarations; the arithmetic theorem is about actual post balances. These checks do not establish complete STARK security or a native consumer cutover.
- **Reported targeted Lean checks and executable probe:** the policy-source bundle checked successfully, including compact source encoding, canonical/malformed decoding, cSHAKE, dynamic source resolution and wrong-domain/changed-payload refusal. The production registry constructor fixes canonical step binding; the abstract digest adapter is explicitly an example. The policy installation journey is still being implemented.
- **Checked counterexample:** an isolated Lean program constructs a then-valid generic canonical-overlap commit whose two individually balanced transfers create seven units in the actual joint post. Root read that construction. The generic repair is assigned; the artifact is a discriminator for that repair, not permission to mutate the shared guard.
- **In progress:** the actual Hermes `world_bridge_e2e` test build on the single leased hbox Rust lane. No pass is claimed yet. Runtime callers have source/format checks and prepared failure/recovery tests, not a joined runtime verdict.

## Shared-core work now assigned

The common operation being built is a resource birth that joins its permanent identity, owner authority, initial content and any charge in one accepted multi-cell transaction. It must be usable by the shell and resource applications; a sequence of separately committed setup calls does not close it.

- **Exact generic effect admission:** require the accepted token's actual pre-cell and complete request to equal the family's source-derived pre/request. This replaces optional request-binding wrappers as the generic authority boundary. Concrete family constructors and their receiving consumers must migrate together.
- **Actual joint composition:** preserve each accepted leg's result in the actual combined state and check the resource law on that state. An independently admitted whole-Book write must not overwrite another fee or funding operation. Differing sequential writes belong inside an admitted ordered batch; overlap with agreeing outcomes can remain composable.
- **Concrete authority and resource pages:** executable compact codecs for capabilities, lineage, epochs, nullifiers and finite Books; explicit digest version changes; checked account registration and sequential resource batches. Account registration is bound to the exact authorized birth, not invented from a payer's transfer permission.
- **Resource birth/controller:** reuse `CellRegistry.create`, existing authority and resource semantics, `MultiCellHyperedge` and `DataIntent`. One incidence per physical cell and one final accepted write bundle. Source freshness, retired identities and duplicate births have explicit refusal obligations.
- **Native durable receiver:** implement a computable representation and actual storage consumer of the existing multi-cell `DataIntent`. The current single-record forward-link transports do not supply that general receiving path. Lean retains admission semantics; native code supplies fallible physical I/O.
- **Ordered World recovery:** record setup births/updates and turns in their actual sequence; verify every recorded boundary and receipt, and bind checkpoints/UI cursors to the full ordered position. Tail salvage may remove only unpublished records after validating all published evidence. This physical-history repair does not itself authorize raw setup mutations at the kernel.

Existing failures and research obligations remain work to close. Source pins in the opening graph deliberately remain dated observations while files change; a stale hash calls for review, not automatic refresh or a declaration that the old claim is false.

## First joined build result

The first Hermes bridge build returned `pbuild: VERDICT outcome=FAIL`: `deos-hermes/src/live_js.rs:272` still passed held `AuthRequired` where the revised API requires a `Requirement`. The test did not run. Its owner is migrating that actual receiver and checking other callers before a narrow rerun. This is a source integration failure, not an environment failure or a reason to disable the authority distinction.

At this record's source-freshness check, 62 file sources were checked: six had changed, no graph references were broken, and two repository heads had moved. The changed observations concern active World/UI/Hermes and generic accepted-effect/hyperedge edits. Their older pins were retained for review.
