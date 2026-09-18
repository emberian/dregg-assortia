# September 18, 01:30 — durable invocation and runtime history

This follows [00:45](checkpoint-0045.md); its failed and slow measurements remain historical evidence. Breadstuffs `73136dd30` and minidregg `278ed6a` are committed and pushed. No deployment or asset operation is part of this checkpoint.

## Runtime history repair

The [24 targeted cell/turn/World tests](evidence/world-cache-closure-0130.txt) all passed on hbox with native Lean required. The [source capture](evidence/world-cache-closure-source-0130.json) identifies the tested files. Root compared the eight changed runtime files against that capture before committing. The capture was made immediately after launch because the first manifest script failed; the owned files remained frozen throughout the run.

Replacing a cell through `*ledger.get_mut(id) = changed_clone` invalidated the outgoing cell's hash cache, then installed the clone's stale incoming cache. A reopened image drops caches, so its roots could disagree with the live history. `Ledger::replace_cell` now validates immutable identity, invalidates the incoming cache, journals the old image and preserves auxiliary indexes. World, replay and reversible history use it. Checks cover changed warm clones, cache-free reconstruction, auxiliary state, rollback, every retained history boundary, refusal/publication failure, batches and corrupted receipt/root evidence. The reversible mirror now also checks the original receipt clock and embedded root.

This closes the earlier two observed intermediate-history failures. It does not complete authorized document editing: physical setup journaling is still distinct from a kernel-authorized save. A subsequent source inspection found that factory deployments are not ordered persistent events, and historical forks preload present-day factories. That repair is assigned to the runtime history lane.

The four SDK candidate/publication tests already passed after lazy registration in 0.026–0.047 seconds each and return to the default test set. The exact Hermes bridge still takes 191.097 seconds at its first verified admission. Its ongoing repair concerns actual Lean module initialization; the accepted worker accountability turn also invokes the full producer. Construction speed alone does not close that path.

## Canonical native receiving

The [frozen source/check manifest](evidence/native-wave-source-0130.json) covers 53 files: 47 with scoped checks, two documentary caveats and four unchecked compatibility/label changes. Forty-four files changed in the commit; others were already committed dependencies. [Captured check logs](evidence/native-wave-0130/index.json) retain their individual scopes and reported exit evidence. The checkpoint collector verified hashes and read logs; it did not rerun those checks or perform a whole-tree build.

The actual declared-resource probe crosses real Ed25519 verification, stored capability/lineage admission, same-snapshot physical policy-source selection, compiled policy and actual page/authority effects into SQLite publication. Reopening recovers the changed resource and marker. Exact signed ingress replays its original retained result; changed ingress under the same operation identity conflicts. Tampered signatures, an enrolled different signer borrowing the capability, stale roots, out-of-scope actions and object-to-program actions refuse without changing physical bytes. See [the invocation result](evidence/native-wave-0130/localfirst-native-invocation.txt).

That fixture starts with explicit bootstrap authority and policy. Accepted resource birth and authorized delegation are separate pending joins. The lower birth controller is checked; the upper native birth controller and physical receiver are still being elaborated. Review also identified caller-chosen birth transaction IDs and authority markers; the birth lane is replacing these with a canonical identity scoped to the authenticated creator, factory, domain, runtime semantics and nonce before claiming the joined birth path.

Other captured results include ten strict native Ed25519 CLI checks; 33 policy-source storage/codec/read-guard checks; actual capability-only policy-install admission; general page-write reflection; full key/schema and runtime profile checks; and standard-axiom audits. Policy-install admission is not yet a durable policy replacement. Fixture fields and scalar widths are not deployment parameter selections. No new whole-system STARK claim follows from these results.

## Next receiving work and ownership

- Birth: native source authorization, conserved funding/fee, initial source/grants, exact physical refinement and retry identity. Owners: proof_integrity and program_install.
- Joined invocation: create through the actual birth receiver, reopen, then invoke using the created owner's capability. Owner: localfirst.
- Policy replacement: actual immutable source creation and grouped authority update in one accepted durable operation. Owner: program_install.
- Delegation: explicit authenticated parent-to-recipient production, immutable scope narrowing, current lineage and global capability-ID freshness. Owners: durable_callers and effect_admission; shared representation migration waits for the current receiving checkpoint.
- Runtime: ordered factory deployment/history, actual consumer compilation, and safe narrow/full Lean initialization. Owners: kernel_carrier, shell_hermes and resource_history respectively.

Separating source revision from grant generation is under design. Preserving a grant means it remains bounded by its immutable scope and follows the current resource law; the current typed capability does not yet carry an arbitrary immutable predicate caveat. Preserved grants also do not guarantee that a newly installed policy permits future administration. These questions stay explicit in the design record.

## Contributor work and the hub

Wisper is an experienced backend/platform engineer whom ember trusts with broad systems work. Android was an example of substantial product ownership; DreggNet/cloud is another candidate. The current investigation proposes ownership of the real resource-host lifecycle and its cloud integration, including recovery, supervision, custody, command status, resumable events and packaging. This is a proposal to discuss with ember and Wisper, not an assignment or a claim that stable exports already exist.

Assortia's graph traversal and portable source-impact tools are internal agent tasks. Current work, owners, next actions and captured evidence live in the graph and generated board; historical observations are not silently rewritten as current facts.
