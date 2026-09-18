# Book support lane wind-down

No compiler process or compiler seat remains held by resume_admission.

## Checked

`Theory/CanonicalResourceBookInvariant.lean` emitted GREEN, first attempt,
exit 0 in 3.991 seconds with LEAN_NUM_THREADS=2.
SHA256: `21bc2c3ef99964a10a832bc9b0ae699dff012f73f122dddf7a9f7d5ad2baf96d`.
Log: `/tmp/dregg-book-Theory-CanonicalResourceBookInvariant-21bc2c3ef999-1789716121205426000.log`.
Command/attempt manifest: `/tmp/dregg-book-checks.json`.

The source defines finite decidable `Book.AccountSupported` (every nonzero
balance coordinate belongs to a registered account). It proves zero balances
outside the account namespace; preservation under empty/zero Books, account
registration, postings between registered endpoints, all admitted transfer,
mint, burn, fee, lease operations, ordered operation and registration batches,
Batch.run, and actual Accepted/AcceptedBatch patch results. Registration
admission is equivalent to public account freshness, and Books with equal
accounts have equal registration outcomes regardless of private balances and
lease data. An explicit hidden-balance Book violates support.

## Source-only, never compiled

- `Kernel/NativeHostBookInvariant.lean`: actual source genesis fund/initialBook
  preservation, actual PreparedBirth loaded/post Book support, registration
  accounts-only corollary. It depends on the proposed Registry extraction API.
- `Kernel/NativeHostBookAdmission.lean`: actual NativeHost.validateLoaded
  success implies listed-cell CellLaw; universal hidden-balance image refusal
  and concrete witnessHiddenBook refusal. It imports final NativeHostContext,
  whose extraction was in progress. Proof scripts may require repair.
- `Assurance/CanonicalResourceBookInvariantAudit.lean`: declaration list for
  25 `#print axioms` outputs; not run, not converted into exact guard_msgs pins.
  No claim of completed axiom accounting for the new support wave.

## Registry race at wind-down

After authority explicitly granted Registry edits (both old native probes had
finished PASS), I applied the narrowly approved Registry source patch. The
wind-down messages arrived immediately afterward, before any emit/check.
The source contains the import, stronger loaded/final Book law, extraction and
generic hidden-book refusal theorem. The old Registry olean remains unchanged.
Root was notified immediately. Exact own patch is archived at
`/tmp/dregg-book-registry-proposed.patch`; no foreign edits were touched.
No semantic/profile/schema pin update was made. Root explicitly chose to preserve this stronger Registry source as a WIP
checkpoint; no revert is needed. The next session must finish the coordinated
semantic pin + Registry/downstream re-emit before treating it as the active
contract.

The last checked loaded/final law still requires only the configured Book
physical ID and a present Book. The pure codec intentionally roundtrips
unregistered hidden balances. Therefore hidden support remains a real gap in
the CHECKED host; the source-only Registry patch is not checked enforcement.

## Resume order

1. Keep the preserved Registry patch and add explicit runtime semantic law pin
   with host/profile owner (representation/root codec is unchanged).
2. Emit strengthened CanonicalCellRegistry and necessary downstream imports
   under authority's two-seat limit; do not reuse old native probe evidence.
3. Emit current actual Genesis and final NativeHostContext after their owners
   finish their changes.
4. Check Kernel/NativeHostBookInvariant, then NativeHostBookAdmission; repair
   proof scripts at ordinary axiom strength without raising heartbeat limits.
5. Run audit, replace print-only output with exact axiom guard_msgs pins, and
   recheck audit. Add new modules to appropriate root import closure as needed.
6. Repeat targeted native loaded-image rejection and ordinary genesis/birth
   probes under the new exact profile and source identities.

No Git/branches/worktrees/stash used by this lane. No new agents or remote jobs.
Full preparation-read audit: `/tmp/dregg-native-prepare-read-footprint.md`.

Exact source snapshot: `/tmp/dregg-book-winddown-source/`.
Source status/hash manifest: `/tmp/dregg-book-winddown-source.json`.
