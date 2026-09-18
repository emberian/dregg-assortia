# Current consumer supplement: typed kernel, Compiler, and Projection V2

**Read-only check, 2026-09-17.**  MiniDregg HEAD is
`6937394e1dc2c2aaff986c7d4b3a258aca5d16fd`; the worktree is dirty.  This note
uses live source, not the Sep 4 audit alone.  No builds or repository changes
were made.

## Exact current kernel → Compiler picture

### What Compiler directly consumes

`Compiler/DeclaredHyperedgeArtifact.lean` directly imports
`Kernel.DeclaredHyperedge`, opens its namespace, and defines
`ofDeclaration : DeclaredHyperedge.Declaration → Header`.  The emitted header
contains the legacy declaration's pre-root, apex, ordered legs, encoded typed
requests, and `DeclaredEffectArtifact` effects.  This is a real semantic-to-
artifact projection, not merely a comment or manifest edge.

Two other Compiler files import `Kernel.DeclaredHyperedgeWitness`:
`DeclaredEffectPageMaterializer.lean` and `FiniteSparseMaterializerAudit.lean`.
The former's live principal types are also `Theory.CanonicalTransition`,
`CellState`, `DeclaredActionLowering`, `EffectDeclaration`, and
`TypedAuthorization`; it is a concrete page/materialization adapter.  The
witness import means there are some shared examples/migration material, but it
does not make Compiler a direct consumer of `TypedCellHyperedge.Commit` or
`MultiCellHyperedge.Commit`.

Compiler has **no direct import or code-level reference** to
`Kernel.TypedCellHyperedge` or `Kernel.MultiCellHyperedge`.  The only
`MultiCellHyperedge` occurrence under `Compiler/` is a doc-comment in
`Compiler/DistributiveLaw.lean`.  Its other live typed inputs include
`Theory.TypedAuthorization` (`CanonicalPolicyAdmission`,
`TypedAuthorizationRequestCodec`) and `Theory.EffectDeclaration`
(`DeclaredEffectArtifact`).

### What this disproves and what it does not

It would be inaccurate to call all canonical typed semantics “unwired.”
The compiler does carry typed authorization, effects, cell/materializer and
canonical-transition structures through several real artifacts/adapters.
`MultiCellHyperedge` also has real non-Compiler consumers: canonical resource
effects; Hyperdocument publication/merge publication; and Assurance modules
for guarded durability, agent operations, link publication/recovery, and
durable installation.  `TypedCellHyperedge` is used by canonical resource
effects and by Grain-fork/reactive-lifecycle Assurance work.  Thus the typed
joint kernel is active in the semantic/Assurance Hyperdocument path.

The narrower, still material conclusion is:

> The **joint-turn compiler artifact** at HEAD is projected from
> `DeclaredHyperedge.Declaration`; no live Compiler producer or consumer
> accepts `TypedCellHyperedge.Declaration/Commit` or
> `MultiCellHyperedge.Declaration/Commit` as its joint-turn source or output.

`DeclaredHyperedge` is not an arbitrary untyped object—it itself uses typed
Theory-level request/effect/cell structures.  But `TypedCellHyperedge` retains
a `LegacyAdapter.Certificate` and witnesses a migration relationship to that
legacy carrier.  Consequently, the missing work is a precise re-point/
faithfulness decision at the joint-commit/artifact boundary, not a wholesale
replacement of every Compiler input type.

`Kernel/DeclaredActionExecution.lean` is a useful caution: it constructs
typed-cell commits and imports Compiler action bytes, but it has no importer
outside its umbrella according to the current source census.  It is evidence
of a potential bridge, not the live artifact route.

## Dirty Projection V2 lane: exact role and live consumers

The Projection V2 lane is uncommitted.  Its visible paths are:

* dirty `Compiler.lean` adds `import Compiler.UwueavePreoProjectionV2`;
* untracked `Compiler/UwueavePreoProjectionV2.lean` takes the upstream
  `Uwueave.Preo.ProjectionV2.Examples.fullExport`, validates it, proves exact
  IDs/reference/profile/budget facts, renders deterministic Rust source, and
  has `#eval writeGenerated` for
  `prover/generated/uwueave_preo_projection_v2.rs`;
* dirty `prover/src/lib.rs` `include!`s that generated file; and
* untracked `prover/tests/uwueave_preo_projection_v2.rs` reads its static
  values and explicitly checks that the generated surface has no `pub fn`,
  `impl`, `unsafe`, `extern`, `Verified`, or `Accepted` token.

The only live Rust uses found are that inclusion and the static-data tests.
The generated data module itself has constants/types/static values, no runtime
function.  No native dispatch, Lean controller, policy/admission check,
receipt, scheduling permit, or DREGG-resource consumer calls it.  Its source
docstrings make the same limitation explicit.

`CROSS_REPO_CONTRACTS.md` is stronger still: V2 is not the default new
crossing and should not merge merely because generated data is well formed;
first choose whether the actual receiver needs rich V3 planning data or the
narrower V4 context-auth sidecar.  Even a chosen planning artifact must remain
neutral until MiniDregg independently binds request kind, subject/target,
verb, arguments/effects, pre-root, policy, nonce and cost.

## HEAD versus dirty qualification

At HEAD there is no Projection V2 module/import/Rust inclusion.  In the dirty
workspace, the V2-specific path reaches the Compiler umbrella and Rust crate
namespace, but only as compile-time/rendered coordination data.  `Compiler.lean`
also has other dirty hunks, so this note does not attribute the entire file
diff to the V2 lane.  No build evidence was produced for this workspace state.

## Practical conclusion

For a DREGG resource/Hermes vertical slice, use the typed Theory-level request,
effect, root, policy and durable-intent contracts now; do not claim that a
typed/multicell Hyperdocument commit is what the existing Compiler header
emits.  The next integration choice is either:

1. establish a faithful typed/multicell joint-commit → artifact projection and
   re-point its receiving compiler/adapter consumer; or
2. intentionally retain `DeclaredHyperedge` as the joint artifact source and
   make its typed relationship, scope, and migration status explicit.

Projection V2 should remain planning metadata until a selected receiver maps
it into that independently checked request path.
