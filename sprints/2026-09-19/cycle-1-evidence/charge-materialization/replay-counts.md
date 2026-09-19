# Replay consumption and structural call counts

Read-only follow-up to Mini **`66d74dd`**, September 19, 2026. These are
source/generated-code deductions, **not measured CPU counts, timings or a
performance model validated across workloads**. No implementation, benchmark
or existing evidence file was changed for this note.

## The rebuilt replay path retains the finite charge

The inspected C belongs to the charge candidate built under
`/tmp/minidregg-cycle-20260919/native-charge-20260919T220000Z`.
`Kernel/NativeHostReplay.c:24339` calls the specialized
`ResourceBirthReceiver_materializedIntent` on successful birth admission.
That function calls `Charge_materialize` at `18953`, then captures only the
returned record in the `Values_toCharge` closure at `18954–18955`.
The `derive` function body contains one materialized-intent callsite and
zero original birth-intent callsites.

Within each successful `walk` iteration, the emitted callsites are:

| Operation | Calls per successful iteration | C line |
|---|---:|---:|
| `derive` | 1 | 26530 |
| `recordMatches` | 1 | 26617 |
| `advance` | 1 | 26661 |
| `validateLoaded` | 1 | 26702 |
| `imageBoundary` | 1 | 26821 |

`advance`'s C body (`26122–26303`) calls durable `prepare`, `Image.append` and
image `encode` once each; it has no `derive` call. `recordMatches`
(`26098–26112`) encodes the stored record and the derived record separately.
Counts inspect function bodies, not declarations or specialization names
embedded in another function's name.

The source retention path is equally important:

- `Kernel/NativeHostReplay.lean:112–138,149–169` derives the next intent once,
  checks its exact record, appends it and creates a receipt for that prefix.
- `Kernel/DurableReceiver.lean:74–77,174–176` copies the intent's existing
  charge value into its record and appends that record. Older record values
  remain in the list; append does not rerun their receiving constructors.
- `Compiler/DurableReceiverIO.lean:102–107` and
  `Compiler/CredentialAuthorityDomainReceiver.lean:152–171` reconstruct the
  typed directory from the existing loaded snapshot. This path does not
  restart semantic history admission.
- `Kernel/NativeHostReplay.lean:197–202` returns the reconstructed final
  image, including the same materialized charges.

No path was found that recreates the original birth charge closure inside
one `verifyLoaded` traversal after materialization. A separate host operation
still starts a new traversal and materializes it again; this patch does not
implement persistent-session reuse.

## Lower-bound sites for the first birth

Consider a successful full replay of **n** accepted records with a birth at
index 1. Count only these complete charge serializations:

1. One encoding of that freshly derived birth in `recordMatches`.
2. Its presence in each of the **n** growing-prefix encodings in `advance`.
3. Its presence in each of the **n** prefix encodings for `imageBoundary`.

The latter commitment encodes the whole image
(`Compiler/NativeHostCodec.lean:26–29`). Each record encoding invokes all
ten charge lanes (`Compiler/DurableReceiverCodec.lean:25–28`). Therefore
these identified sites alone request **10 × (1 + 2n)** birth-charge lane
values. At depth 8, that is **170** lane requests.

Before materialization those requests invoke the retained source charge
computation. Afterwards `Charge.materialize` evaluates its ten lanes once
(`Theory/ResourceCost.lean:91–101`), and those same serialization requests
project stored naturals. This is a structural lower bound on eliminated
source evaluations at the listed sites after allowing for the ten one-time
evaluations: **160 fewer at depth 8** from this accounting alone. It is not
a count of all host work.
The already decoded stored-record side of `recordMatches` is deliberately
excluded: its charge was decoded into finite values already.

Budget evaluation supplies further reuse, without changing the conclusion:
`Kernel/DurableCommitProtocol.lean:159` retains each prior charge in the
remaining-budget function; `:295` checks funding across all lanes. These
references now reach the same finite birth charge. They are not included
in the 170 count. Other operation families' source charge functions were
not changed.

## Why the wall-time gain can remain modest

This fixture has one birth, so the removed birth-charge recomputation grows
linearly with history depth. Whole-image serialization and cSHAKE over each
growing prefix remain; for similarly sized appended records their total
input volume can grow quadratically. Every historical event also retains
native admission and structural validation. `NativeHostContext.validateLoaded`
at `79–112` still checks genesis identity, directory, authority and committed
policy sources. This patch is not a bound on total replay complexity.

Root reports the matched depth-8 comparison as **105.51 s → 91.66 s**
(approximately **13.13%** less wall time, **1.151×**), with the same accepted
view and unchanged complete image. The build lane owns the captured timing
and state-equivalence artifacts; this note did not run or independently
retime that benchmark. Earlier one-event query and birth comparisons showed
no gain. The structural counts explain the intended work removal; they do
not replace those measured results or establish broader speedup.

No further benchmark depths or performance expansion are proposed here.
Future phase timing should separate replay, fresh admission, durable
construction/commit and confirmation before choosing another change.

## Exact identities

Generated C:

```text
5583d4c542f12102a5708fc49491f214a13a5e39db8dbe4c048052668511576c  native-charge-20260919T220000Z/.lake/build/ir/Kernel/NativeHostReplay.c
```

Source files read from `/Users/ember/dev/minidregg`; source hashes for the
two changed files are also retained in this directory's `source.sha256`:

```text
92102c05812416385f0dfc22941158dee7c3f0fdc205f1d461d296e8831075f7  Theory/ResourceCost.lean
675bc737295d6a0d7db121a93f035c994cb452528e9d0622ada812ab903d0917  Kernel/ResourceBirthReceiver.lean
95db8fe1c0ffa86e07e5cefd6f5ce311aa7625c9607cb60b22c1a6ed186cc5b5  Kernel/NativeHostReplay.lean
f4eade83c8792c0c4b631174485ead84451d680c91cf22aa6415ce3bfe1ebee7  Kernel/DurableReceiver.lean
c7e2c80cb235be701e3a69208956eb6599ef8b01a5881c67388e1cf5f70ee891  Kernel/DurableCommitProtocol.lean
5ab6e9903186fa64201f3861bf72b977adcbe51bfbe149de9087c0cc6dc01686  Kernel/NativeHostContext.lean
70db2bd1160d036771ec6c13fbee2a1f662355af0ed0004d03208d55fc27660c  Compiler/DurableReceiverCodec.lean
af1a3cf40cbfdaf09bcb7cbbd8fbe22d6962ebb4bd49a7dfc91943ad9bd16df0  Compiler/DurableReceiverIO.lean
0181dafd83f16bb67f9c9c9aacf536ffd4f2d8fff9830e9f0928ad4470d457c9  Compiler/CredentialAuthorityDomainReceiver.lean
a3f2c8256d6f2b9eb5f944c34a466462bb819952fad4905c2a4cc381fea0d7e4  Compiler/NativeHostCodec.lean
```
