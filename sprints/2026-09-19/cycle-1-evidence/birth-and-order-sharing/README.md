# Birth sharing and direct order witnesses — September 19, 2026

This is component evidence from the authority lane. It records exact semantic
equalities, successful bounded compiler invocations, generated-C inspection,
two bounded profiles, and one matched native birth benchmark. It does **not**
claim a completed native authorized query or full new-world journey.

## What changed and what was proved

- `PolicyStepContext.ofPreparedTupleExact` accepts direct pre/post selectors
  only with pointwise equality to the actual prepared tuple. The general
  `ofPreparedTupleExact_eq` theorem retains its complete original context.
- Birth's `policyPreCell` and `policyPostState` select actual prepared payloads
  without constructing unused signed requests and descriptor commitments.
  `Pending.branchStep_prepared_exact` equates the result with the original
  tuple constructor. Admission shares one computed step and compiler profile.
- `mapped_policyBranches_nodup_iff` proves that a duplicate-free list of the
  exhaustively enumerated, precomputed request identities is exactly the old
  injectivity condition, for **every** identity function. Collision refusal
  and private prepared-state admission remain intact.
- `binaryDigits_eq_direct_value` proves every original bit equals
  `(n / 2 ^ i.val) % 2`, for every width, natural and valid index. The
  `binaryDigits_eq_binaryDigitsDirect` compiler substitution uses this
  equality. The original order gadget and soundness/completeness statements
  are unchanged. Its axiom pin is `[propext, Quot.sound]`; the selector and
  identity equalities use `[propext, Classical.choice, Quot.sound]`.

The source excerpts include the named equalities and checked axiom pins.
`source.sha256` identifies exact canonical files when archived. These are
review excerpts, not independently compilable modules.

## Checks and emitted code

The four original logs under `logs/` are empty. The lane observed exit 0 for
each actual Lean source-to-olean/C invocation; **an empty log by itself does
not encode exit status**. `commands.txt` records the command forms, absolute
source/output paths and private dependency-overlay arrangement. The helper,
controller and receiving `ResourceBirthReceiver` were checked sequentially.
The order-gadget check was independent. There was no rerun to manufacture
archival output.

`generated-c-facts.tsv` counts specific callsites in exact emitted functions,
and `generated-c.sha256` identifies the inspected C artifacts. Most
significantly, the newly compiled `PredCompile.orderAux` calls the direct
implementation: the compiler substitution reaches the actual witness
consumer. These are code-shape facts, not runtime measurements.
The `rawLeg` checks count calls, excluding a shared closed registry constant
whose generated name still includes `rawLeg`.

## Measured scope

The original fullgate birth profile placed 1351 of 1354 sampled main-task
stacks under post-install confirmation's full semantic replay. Repeated
request/descriptor hashing appeared inside birth policy preparation. The
sharing changes retain that replay; no persisted state is trusted without
the existing verification.

The later authorized-query profile placed all 1502 sampled active stacks
under policy admission and canonical order-witness construction. The deployed
order width is 29, hence 30 witness bits. Lean 4.30's `Fin.cases` is defined
through `Fin.induction`: executable induction evaluates predecessor results
even though the case handler ignores them. Combined with recursive digit
generation, this caused repeated branching work. The old query was
interrupted after roughly eight minutes; this is neither an admission
rejection nor a completed benchmark. The direct implementation has no such
recursion. Its native query retry was **pending at archival time**.

`hot-path-counts.tsv` contains selected inclusive frame counts; descendant
and recursive counts overlap and must not be added or treated as exclusive
CPU percentages. The originals are identified by hash. Full process samples
are deliberately omitted.
Counts use only the call-graph section, remove embedded specialization-site
suffixes before matching symbols, and exclude `binaryDigits___boxed` from
the `PredOrder_binaryDigits` row. The other selected fragments include their
listed recursive/adapter frames.

The completed matched birth takes **49.43 s** with theta sharing plus birth
selectors/identity sharing, versus **223.78 s** with the preceding guard-cache
candidate (about **4.53×** in this pair of runs). Both use the same signed
birth and genesis with fresh independent storage. Both return installed,
accepted count 1, and the **132-byte outcome files are byte-identical**.
`matched-birth/` preserves original time/outcome/manifest text and the exact
receipt hashes; `cmp` was independently rerun during archival and returned
0. This comparison does not isolate theta from birth sharing, does not
measure the new bit implementation, and is not a general performance claim.

No configuration files, signed calls, genesis contents, state stores, private
keys or full process samples are included. Root owns completed journey and
project-status claims.
