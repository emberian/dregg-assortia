# Proposed next native computation work

Read-only investigation, September 19, 2026. **No implementation, build, measured
optimization gain or completed-journey claim accompanies this note.** It
supplements [the verified-session proposal](next-cycle-host-session.md), whose
registered source bytes are unchanged. Finish the current native journey
before another implementation iteration.

## Measured: historical charge computation survives serialization

One two-second `/usr/bin/sample` observation targeted verified child PID **3765**
of native acceptance runner **50198**. The child launched at
**2026-09-19 17:55:54.721 -0400**; sampling began at
**17:56:19.938 -0400**. A preceding read-only process check reported approximately
98% CPU. The observed public operation was a query.

All **1,363 active sampled stacks** were inside
`NativeHost.query → openExisting → NativeHostReplay.verifyLoaded`.

| Selected frame | Inclusive sampled count |
|---|---:|
| `Sp800185Cshake256.cshake256Bytes` | 1,332 |
| `DurableReceiverCodec.chargeTuple` | 828 |
| `NativeHostCodec.imageBoundary` | 639 |
| `ResourceBirthReceiver.charge` | 892 |
| `ResourceBirthReceiver.readGuards` | 447 |
| `CanonicalPolicyAdmission.admit` | 0 |
| `canonicalWitness` | 0 |
| `instDecidableSystemAccepts` | 0 |

These are overlapping inclusive call-graph counts, not exclusive percentages
or an operation-wide breakdown. Extraction excludes the sample's aggregate
summary and strips embedded `___at___` specialization-site suffixes before
matching symbols. This short observation cannot establish fresh-admission
latency or its dominant cost.

The source explains the observed work:

- `Kernel/ResourceBirthReceiver.lean:252–279` stores `charge accepted` as a
  function. Its memory/storage lanes recompute prepared writes and read guards;
  obtaining their lengths still constructs values whose roots require hashing.
- `Kernel/DurableReceiver.lean:64–77` retains that function in `IntentRecord`.
  `Compiler/DurableReceiverCodec.lean:25–28` evaluates all ten lanes whenever
  the record is encoded.
- `Kernel/NativeHostReplay.lean:112–138` compares exact encoded records and
  appends the freshly derived intent. Its `walk` at `149–168` also hashes each
  reconstructed prefix through `NativeHostCodec.imageBoundary`
  (`Compiler/NativeHostCodec.lean:26–29`).

Thus the measured next fix is **materializing source-derived charges once**,
with shared computed writes/read guards where appropriate. The existing
`DurableReceiverCodec.chargeOfTuple_tuple` theorem at `42–44` proves
`chargeOfTuple (chargeTuple charge) = charge` for every charge. A receiving
implementation can exploit this equality without changing charges, wire
bytes, commitments or authorization. Put any common helper below the codec
if needed to avoid an import cycle. Prove exact intent/record equality, then
inspect generated code to ensure later charge calls project stored naturals.
The performance improvement remains to be measured.

**Caching `verified.opened` alone retains the expensive closures.**
`NativeHostReplay.verifyLoaded:197–202` returns the reconstructed `final`,
rather than the already decoded target representation. Its old records
therefore retain source computations; subsequent prefix encoding can force
them again even if semantic admission is cached. Materialization should
accompany a persistent session. Another possible receiving implementation
would retain the decoded record only after transporting the exact equality
proved by `recordMatches_iff:116–119`; it must preserve the actual admitted
record and introduce no trust in unchecked stored posts.

## Source-justified, unmeasured: canonical-only native admission

`Compiler/CanonicalPolicyAdmission.lean:547–581` already proves
`canonical_verifies_iff_eval`: after every resolution, content, request,
step, profile, support, range and cast-injectivity condition holds, checking
the emitted canonical witness is equivalent to `Pred.eval`. The theorem's
existing axiom pin at `886–887` is `[propext, Classical.choice, Quot.sound]`.
Its foundation is the general `PredCompile.lower_sound` and `lower_complete`
theorems (`Compiler/PredCompile.lean:957,974`).

A proposed `admitCanonical` should preserve **all** existing checks and
construct the same `Authorized` value, including the same canonical witness,
using that theorem after source evaluation. Prove exact `Option` equality
with `admit ... (canonicalWitness ...)`; agreement only on positive examples
or `isSome` is insufficient. Keep arbitrary-witness admission unchanged.
This can preserve the existing compiler/profile assurance semantics: it
requires no caller-selected evaluator, omitted bound or new trusted axiom.

First receiving consumers would be
`Kernel/ResourceObservationAdmission.lean:187–197` and
`Kernel/DeclaredResourceController.lean:221–244`. Preserve the latter's
distinct range/cast refusal behavior. `canonicalWitness:536–542` initially
allocates an auxiliary function; the avoidable work is **forcing that
function while building/evaluating the compiled constraint system**, not
merely allocating its record. The current sample did not observe this cost,
so it does not rank this proposal above measured charge materialization.

Before promising interactive latency, measure unchanged-image refresh,
fresh admission, durable preparation/commit and confirmation separately.
Keep complete native operations as the final check. Session reuse, charge
sharing and canonical-only admission address different work; none yet has
a measured gain in this note.

## Exact source and evidence identities

SHA-256 values captured from `/Users/ember/dev/minidregg` during this
investigation; line references above apply to these bytes:

```text
04a3f1036d5fe4a6baa93d9afdb5391d3cea82613fbd19899d57188255638e5f  Compiler/CanonicalPolicyAdmission.lean
873cb99baeea907ff0614cd5163a336fb95195e09b6ac3479950ae90c07593f5  Compiler/PredCompile.lean
70db2bd1160d036771ec6c13fbee2a1f662355af0ed0004d03208d55fc27660c  Compiler/DurableReceiverCodec.lean
a3f2c8256d6f2b9eb5f944c34a466462bb819952fad4905c2a4cc381fea0d7e4  Compiler/NativeHostCodec.lean
ecda43944f736cde8f25ffd3143bd9413847a74e93a5063d19ae96562ad0d862  Kernel/ResourceBirthReceiver.lean
95db8fe1c0ffa86e07e5cefd6f5ce311aa7625c9607cb60b22c1a6ed186cc5b5  Kernel/NativeHostReplay.lean
f4eade83c8792c0c4b631174485ead84451d680c91cf22aa6415ce3bfe1ebee7  Kernel/DurableReceiver.lean
9b048a882b8eae3bb0fd2cc3e946f708f4556e4c73d1e435d19e920ecf78b360  Kernel/DeclaredResourceController.lean
70770123966e2e46271404961c31ac103358a805ecb22d70792192ef15150a17  Kernel/ResourceObservationAdmission.lean
```

The private temporary sample is identified by SHA-256
`31f02dabf2a007962792b7ac6a5f8dd75a2087fd9470b9c8e7e0ed99302691c6`.
Its raw contents, command line, environment and runtime inputs are not
archived here. No graph, evidence index, shared hash manifest or existing
proposal was edited by this archival task.
