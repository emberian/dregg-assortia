# Dregg kernel/compiler/proof frontier — read-only orientation

**Inspection:** 2026-09-17.  No builds, edits to repositories, Git writes, or
remote operations.  MiniDregg committed revision is
`6937394e1dc2c2aaff986c7d4b3a258aca5d16fd` (2026-09-06).  The retained IR2
package is explicitly based on that revision.  No additional `AGENTS.md` or
correction file was found under the inspected `minidregg`/`zkml-research`
roots; the parent workspace instructions were observed.

## Current usable pieces

### 1. Social/local-first semantic substrate: modelled, with one genuine narrow adapter

`Theory/TypedAuthorization`, `Theory/EffectDeclaration`, canonical transitions,
typed cell effects, and `Kernel/DurableDataIntent` give useful *semantic*
objects for friend-resource turns: typed authority requests, canonical writes,
read guards, replay-nullifiers, root-bound bytes, conflict refusal, and an
explicit physical-refinement contract.  The Hyperdocument/reactive witnesses
exercise a logical terminal/outbox transaction.  This is meaningful for a
DREGG resource graph: it says what a signed/attested transition must bind and
what a local store must preserve.

It does **not** make a Fossil/Git store, Hermes endpoint, SQLite process,
network replication, finality service, or outbox delivery a refinement.
`Kernel/DurableDataIntent.lean:400-434` makes that dependency explicit as
`ImplementationRefinement`; `HyperdocumentReactiveCarrierWitness.lean:603-613`
lists commitment-opening soundness, authenticated finality, durable refinement,
fairness, and eventual delivery as externally supplied deployment conditions.

### 2. There is a real compiler/runtime seam, but it is a small proof-carrying candidate path

The best committed vertical slice is Stage 0 EVM addition:

`Theory/EvmFragment`/`EvmResidual`
→ `Compiler/EvmAddAir.evmAddDescriptor` (16-limb BabyBear descriptor semantics)
→ `DescriptorEval` and `NativeKernelPlan.descriptorHoldsCheck`
→ `EvmStage0NativeDeployment` (registered work 9103 and exact codec pins)
→ Lean-emitted `prover/generated/evm_stage0_add_aux.rs`
→ `native_dispatch::evm_stage0_add_aux_bytes`
→ `prover/tests/evm_stage0_dispatch.rs` (five Lean-authored, 4,131-word vectors).

`CommittedTerminal*` and `Assurance/ReleaseGateRouting` additionally show a
non-interactive receipt binds the full public word and descriptor under their
named ideal-commitment/ROM assumptions.  This is a good pattern for Hermes:
native code supplies bounded candidate bytes; Lean selects continuation and
acceptance.  It is not a general refinement of Rust arithmetic, serializer,
prover, or I/O, and the five-vector agreement is evidence rather than a
universal native-correctness proof.

### 3. The IR2 proof package is available, inspected, and unlanded

`zkml-research/research/proof_frontier/2026-09-08/ir2_verifier_bridge/` retains
an additive 13-module patch (`ir2-verifier-bridge.patch`, SHA-256
`57e47c…f6c8`) for exactly MiniDregg `6937394`.  `CHECKS.json` records 128
axiom pins, per-module source hashes/checks, import-boundary success, and patch
replay in an isolated temporary directory.  It is therefore better represented
as an **available, reproducible candidate integration**, not a vague research
claim and not a landed MiniDregg dependency.

Its strongest theorem is conditional but specific:
`Ir2Fri.native_fresh_38` proves the modeled actual-row native interpolation /
query event for a fixed alpha-reduced word outside radius 2/5 of degree<16384
RS code on the observed BabyBearExt4 profile.  At 38 queries it records
approximately `3.713192974e-9`, with actual schedule 17→14→11→8→5→3 and five
fresh Ext4 challenges.  `native_eq_foldStep` and `native_query_iff_counted`
remove a *symbolic native-row-to-fold-event* premise inside Lean.  The package
also has satisfying and rejecting witnesses.

This is neither a global proof acceptance theorem nor a runtime refinement.
Its own README names the blockers precisely: arbitrary canonical packed-MMCS
extraction to a prefix-fixed word; false PCS claims → farness (including
hiding columns/coset substitution); Poseidon2/PoW challenge generation →
FS/QROM game; Rust field/serialization/MMCS/malformed-proof/admission
refinement.  A saved proof is canonically admitted and replay-projected, but
that confirms one artifact, not arbitrary native proofs.  Its handoff says
no additional tuning, rounds, witness expansion, or replay is needed before
those bridges; that changes the next proof choice toward extraction/PCS/FS,
not parameter polishing.

### 4. IR2 is already a receiving *identity* contract, not a receiving verifier

Committed `Selvage/ZkmlSuiteRegistry.lean` contains the exact
`dregg.ir2.babybear-ext4.poseidon2-w16.fri.v1` suite identity, source commit,
payload hash, protocol/checker identity, and fail-closed lookup.  Its own
`claimCeiling` is “checked source-export and exact suite identity; no deployed
verifier refinement,” and it names Rust-checker refinement, Plonky3 soundness,
registry authentication/upgrades, BaseFold/Poseidon2 commitment and FS
instantiation as residuals.  Thus it is a useful Hermes admission metadata
contract, but proof bytes cannot yet become a product truth claim through it.

## High-impact integration blockers at HEAD

1. **Canonical semantic kernel is not compiler input.**  The tracked
   `docs/KERNEL-TWIN-AUDIT.md` (Sep 4) finds `KernelState`/Gate (A) and typed
   canonical cell/hyperedge layer (B) are twins, not a refinement.  Worse, the
   compiler consumes legacy `Kernel/DeclaredHyperedge` through
   `Compiler/DeclaredHyperedgeArtifact`, although that carrier labels itself a
   migration surface; intended `TypedCellHyperedge`/`MultiCellHyperedge` have
   no Compiler/Effects consumer.  `Kernel/Gate.lean` has no importer beyond
   umbrella and no native caller.  For product work, defining a stable
   resource/turn ABI and repointing compiler output to one canonical B carrier
   is higher leverage than proving more A-side gate lemmas.

2. **Security-statement validity is distinct from deployment.**  Sept 5
   refutations/replacements are valuable: old heterogeneous `KnowledgeSound`
   at a succinct system was refuted; old `ComposeErrorBound` was proved inert
   and `ComposeErrorBoundStrict` added; unlinked shifted BCS knowledge was
   retired; inverse-fold extraction was refuted.  But the planned R2/R3/R4
   deletion/repoint did not land: old objects remain beside corrected ones;
   `HeteroCompositionErrorBound` says it did not edit `HeteroComposition` or
   docs; linked knowledge packaging remains an obligation; the old table
   extractor remains beside the all-query identity route.  Querying the graph
   must distinguish `refuted`, `replacement-proved`, `replacement-consumed`,
   and `legacy-deleted`.

3. **Artifact availability is distinct from runtime receipt.**  The IR2 patch
   is a retained, source-hashed integration proposal with individual checks;
   it is absent from MiniDregg imports at HEAD.  The uncommitted Projection V2
   addition is also only Lean-rendered static coordination data and explicit
   Rust data tests; it has no verifier/policy/admission/dispatch authority and
   no clean integration build.  Neither should be used as a product capability
   until an exact consumer contract accepts it.

4. **A bound is distinct from cost and from an end-to-end security parameter.**
   IR2's `3.713e-9` is an honest conditional mathematical probability over the
   stated fresh experiment.  It earns no FS/QROM, hash/PCS, proof-of-work, or
   runtime bit-security credit.  Stage 0's FS price is likewise scoped to its
   word/descriptor/ROM model.  Neither record supplies proof size, proving
   time, verification time, memory, local storage, sync latency, or availability
   cost for a friends/local-first DREGG service.  Those must be separate
   benchmark/operational claims, tied to the same admitted ABI.

## Relations that should determine next work

1. `canonical_resource_turn --compiled_to--> descriptor/artifact
   --accepted_by--> Lean controller --carried_by--> native/store adapter`.
   It is broken at the first arrow by legacy `DeclaredHyperedge`; repair this
   before treating proof receipts as application turns.

2. `canonical_admission --requires--> packed-MMCS extraction
   --requires--> PCS false-claim→farness
   --requires--> FS/QROM challenge transport`.
   The IR2 actual-row theorem is downstream of an extracted far word, so the
   next security bridge is packed extraction/PCS, not more FRI schedule work.

3. `artifact identity --authorizes routing only--> checker selection`, while
   `runtime accepted receipt --requires--> verifier refinement + security
   premises + exact statement binding`.  This keeps Hermes routing metadata
   useful without laundering it into proof validity.

4. `logical durable intent --requires--> physical refinement + availability
   policy`.  This is the direct path for local-first social data: monotone
   local receipts/replay can land before global finality, provided the graph
   records the chosen replication/finality semantics instead of inferring them
   from the model.

5. `claim --qualified_by--> source revision/workspace state/build evidence/
   parameter profile`.  In particular, retained patch, committed head, and
   dirty Projection V2 are three distinct revisions.  This relation is needed
   for a Fossil/Git-independent discussion graph as much as for code.

## Workspace distinction and unknowns

MiniDregg HEAD is `6937394`; the worktree is dirty: modified `Compiler.lean`,
`README.md`, three Cargo manifests and `prover/src/lib.rs`; untracked Projection
V2 Lean/generated Rust/tests, licensing files, and untracked formal-status doc.
No build was run.  The formal-status document is an untracked Aug 18 snapshot
and is stale relative to the Sep 5 proof repairs.  I did not audit actual
Fossil, Hermes, or production DREGG consumers, nor validate retained logs by
re-running them; those are unknowns, not negative findings.

## Suggested graph vocabulary

Reify `Claim` with scope, assumptions, parameter profile, revision and status.
Link it to `Definition/Carrier`, `Proof`, `Refutation`, `Witness`, `Obligation`,
`CompilerPass`, `Artifact/Codec`, `RuntimeAdapter`, `Consumer`, `Test`,
`BuildEvidence`, and `OperationalMeasurement`.  Essential relation labels:
`proves`, `refutes`, `satisfies`, `falsifies`, `depends_on`, `assumes`,
`compiles_to`, `emits`, `serializes_as`, `registers`, `routes_to`, `consumes`,
`checks`, `refines`, `binds`, `supersedes`, `repoints_to`, `deleted_by`,
`coexists_with`, `verified_at`, `claimed_in`, and `stale_against`.

That vocabulary preserves the useful content here without declaring either
the proof project or the social runtime “done” or “unusable.”
