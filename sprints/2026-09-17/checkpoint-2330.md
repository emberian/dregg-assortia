# September 17, 23:30 — executable receiving and admission checkpoint

This follows [23:00](checkpoint-2300.md). Times are EDT. Source checkpoints are deliberately allowed to be incomplete while the shared interfaces converge; targeted component checks are not a whole-tree verdict.

## Published implementation

| Repository | Commit | Change and observed scope |
|---|---|---|
| breadstuffs | `97cb55e80` | Ordered setup/turn history, exact UI history cursors, live Hermes authority-type correction. Targeted runtime validation remains in progress. |
| breadstuffs | `3ff4970ae` | Embedded SDK/World candidate publication and rollback; executor-owned side-state and deferred observer notification. Rustfmt parsing passed; joined build pending. |
| minidregg | `ece0ec2` | Concrete complete authority-entry page codec and fixed projection; targeted Lean and executable page probe passed. Complete multi-page domain is subsequent work. |
| minidregg | `8840978` | Mandatory actual pre-state and complete source-request binding in the base accepted-effect token; concrete private, authority, publication and agent consumers migrated. All changed sources have targeted checks; integrated closure pending. |
| minidregg | `ee0b6cd` | Existing Lean durable executor joined to actual SQLite exact-byte CAS and journal readback. Three Lean modules, ten optimized native tests and the joined lifecycle probe passed. |
| minidregg | `9e65093` | Policy replacement evaluates the selected old source against prepared state. Expanded installation/refusal probe passed with an explicitly identified signature fixture. |
| minidregg | `daa9685` | Compact canonical Book encoding, source-bound ordered funded batches, shared sparse-map codec. Three core modules and executable resource probe passed; provider-consumer followups pending at this checkpoint. |

These changes use the current branches and named files. Unrelated pre-existing staged/unstaged work remains outside the checkpoints. The breadstuffs push still uses the hook's declared `DREGG_ALLOW_DEAD_DOC_REFS=1` exception for its existing dead-reference failure; the secrets scan ran. This is not a claim that the documentation gate passed.

## Captured runs

The [native receiving excerpt](evidence/native-receiver-2330.txt) records the actual release-mode SQLite checks and joined Lean/native probe. It exercised repeated two-cell commits, exact retries after later commits, payload conflicts, stale reads/writes, reused nullifiers, exhausted metering, process exit before and after commit, uncertain-reply reconciliation, concurrent guard movement and corruption refusal. The final valid fixture was 1,080 bytes with five commits.

This is an internal controller-bound `DataIntent` fixture, not yet the complete resource-birth authorization journey. SQLite/OS byte preservation and durability remain physical assumptions. No STARK security or public deployment conclusion follows from this test.

The receiving work also repaired a concrete optimized-build bug: an old `debug_assert_eq!(statement.step()?, SQLITE_DONE)` skipped the INSERT itself in release mode. The statement now executes unconditionally; the optimized lifecycle tests exercise the repair.

The [resource probe](evidence/resource-batch-2330.txt) executes the actual ordered Book operations and compact codec: payer 2, collector 4, newborn 2, issuer-inclusive total zero, canonical encoding 45→53 bytes, changed actual cSHAKE root. Overdraw and duplicate account inputs refuse. This supplements the general Lean laws; it is not itself a general conservation proof.

The second Hermes bridge attempt compiled successfully, then hit the default 180-second test limit. Its [captured verdict](evidence/hermes-timeout-2330.txt) is FAIL, zero passed/one timed out. Native initialization is a hypothesis being measured, not the recorded diagnosis. A binary-only bounded diagnostic is running on hbox; phase markers are committed for the next source build.

## Correction: rejected turns

The initial reading of the raw executor suggested that a charged-refusal journal was needed. Reading its actual node callers changes that conclusion: `node/src/blocklace_sync.rs` discards rejected candidates, and `node/src/mcp/mod.rs::settle_mcp_turn` rolls noncommits back. The raw executor's phase-one fee/nonce retention is a caller responsibility, not the selected durable rejection policy.

`3ff4970ae` aligns SDK and World with unchanged-on-rejection: retain one candidate checkpoint, restore ledger and executor side tables on refusal, defer external observer notification until publication, and refuse reentry into an unresolved candidate. A successful durable write may be uncertain to its caller; RAM rollback still requires authoritative reopen before another attempt. Paid late-refusal, next-success/replay/reopen, observer and side-state checks are the next runtime gates. The earlier charged-refusal suggestion is superseded, including its mention in the previous commit description.

## Next actual joins

- **Resource birth:** exact descriptor-bound fresh allocation, initial content, owner authority, account registration/funding and real fee in one accepted transaction. User-created payloads must not introduce prefunded Books or arbitrary authority. Internal shard allocations are derived from the complete used-id set, bound in the authorized descriptor and checked exactly at admission.
- **Authority domain:** a pinned complete catalogue, every shard at the same pre-snapshot, deterministic routing and full revocation/epoch coverage. A four-entry page does not impose a four-entry product limit.
- **One computable production cell registry:** reuse existing concrete partial registries and materializers. Fixed kinds and initial-state laws prevent shared schemas from becoming type-relabeling or alternative-money paths. The old noncomputable length-root registry is a logical exhibit.
- **Joint admission:** implemented touched-field preservation and actual-joint resource accounting reject minted overlap and dropped fees. Review has also identified cross-field policy stability as the next mandatory obligation: individually valid disjoint edits need not satisfy a rule on the combined state. A constructive witness and source-derived joint-policy admission are in progress; universal composition safety is not claimed.
- **Product receiving path:** the real source-authorized birth/install/invoke journey must consume the same complete authority, registry and native receiver. Shell/Hermes, durable resource editing, history import and contributed computation remain receiving consumers to finish, not replacements for missing core work.

Final affected-closure/umbrella verification is coordinated after shared interfaces settle. Per-file checks can otherwise retain stale structure-projection artifacts. The graph's older source observations remain dated; their changed hashes call for review rather than automatic refresh.

## Subsequent receiving result and composition checkpoint

Minidregg `091e2e3` checkpoints the actual joint resource/outcome repair and its checked concrete overlap/whole-Book regressions. The [additional source-policy counterexample](evidence/joint-post-policy-counterexample.lean.txt) was checked against that contract: disjoint flag changes each preserve `left = 0 OR right = 0` locally, then jointly falsify it. It uses an explicit permissive witness portal to isolate semantic composition; it is not a deployed-signature attack. Mandatory source-family postconditions and preauthorization joint-policy context are now being implemented.

The existing Hermes binary subsequently passed twice in 191.90–192.99 seconds; the [bounded diagnosis](evidence/hermes-runtime-diagnosis.md) records its exact hash and timings. The marker-enabled current candidate snapshot then [compiled and passed through nextest](evidence/hermes-joined-pass.txt), with `pbuild: VERDICT outcome=PASS`, one test passed/two skipped in 190.590 seconds. `AgentRuntime::new` accounts for 190.514 seconds; JS initialization finishes by 190.520 seconds, followed by successful actual fires, receipt retention through a later script exception, readback and socket shutdown. This replaces the unresolved runtime diagnosis above. It validates the captured SDK/World snapshot, not later batch-history changes or all candidate rollback tests.

The specific cold-runtime bridge test is being routed to the heavy set with a measured named 480-second ceiling. This changes its testing budget; initialization cost remains work. The next checks target paid rejection, storage failure, observer timing, complete rollback, exact history and published boundaries.

The [focused persistence run](evidence/persist-tail-pass.txt) then passed all three selected tests: atomic config batch rollback/reopen, unpublished-tail cursor/receipt/publication-head comparison, and durable tail truncation across reopen. This is a package-scoped receiving check (305 skipped), not whole World recovery validation. Breadstuffs `6fa265937` checkpoints the named Hermes test budget; the config/name gate passes after removing one nonexistent budget-only selector.
