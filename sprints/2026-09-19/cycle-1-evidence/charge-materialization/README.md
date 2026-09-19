# Admitted charge materialization — September 19, 2026

Root reports Mini commit **`66d74dd`** for this two-file change. The authority
lane independently rechecked the exact source hashes in `source.sha256`.
This archive contains **general proofs, successful bounded compiler checks
and generated-C inspection**. Native benchmark results and complete source
closure results are not claimed here; root will append them separately.

## Exact semantic result

`Theory/ResourceCost.lean` adds a first-order `Charge.Values` record holding
the ten semantic natural values, `Charge.materialize`, and its `toCharge`
projection. `Charge.materialize_eq` proves equality with every original
charge function, for all lanes. Its checked axiom pin is `[Quot.sound]`.

`Kernel/ResourceBirthReceiver.lean` retains the original `intent` definition
as its specification. The optimized `materializedIntent` differs only in
retaining the evaluated finite charge. The receiving compiler substitution
`intent_eq_materializedIntent` proves equality of the complete functions.
`materializedIntent_eq`, `materializedIntent_record_exact` and
`materializedIntent_record_bytes_exact` establish whole-intent, whole-record
and exact canonical encoded-byte equality. The compiler-substitution and
byte-equality axiom pins are `[propext, Classical.choice, Quot.sound]`.

No fee, lane, root, guard, ingress, nullifier, receipt encoding, authorization
condition or replay condition changes. This does not implement persistent
sessions or canonical-only policy admission. The source excerpts preserve
the definitions, general equalities and pins; they are review excerpts,
not standalone Lean modules.

## Actual generated receiving behavior

Inspection of the successful private overlay's emitted C establishes:

| Function or receiving site | Observed code shape |
|---|---|
| `Charge_materialize` | Ten source-charge applications, followed by one record with ten captured natural fields; no lane argument. |
| `Charge_Values_toCharge` | Switch on the requested lane and project one stored field; no source-charge call. |
| `ResourceBirthReceiver_materializedIntent___redArg` | Call `Charge_materialize` once, then capture only the resulting record in the retained `toCharge` closure. The original source closure is consumed during materialization. |
| `ResourceBirthReceiver_receiveLoaded___redArg` | Calls `materializedIntent___redArg` before the existing durable receiving operation. |

The code excerpts and `generated-c.sha256` identify these observations.
Initial intent construction still performs the source-defined calculations;
this change avoids retaining and repeating them during subsequent charge
queries and record encodings. No speedup magnitude is inferred from C.

Previously compiled callers of the original exported `intent` do not
retroactively acquire a compiler substitution. The native reverse closure,
including `NativeHostReplay`, must be rebuilt. The build lane owns that work
and the full umbrella check. This archive's direct receiving check is not a
substitute for those gates.

## Check provenance and rejected first approach

`commands.txt` records the exact final Lean arguments, dependency root and
private overlay. The authority lane observed **exit 0** for both final
source-to-olean/C checks. Their original logs, copied into `logs/`, are empty;
**empty bytes alone do not encode an exit status**. No checks were rerun to
create this archive.

The first attempted helper returned `Charge` directly, with ten `let`
bindings followed by a lane lambda. Although its generic equality proof
checked, the compiler eta-expanded it into a function taking both the
original charge and a lane. Its output recomputed charge values on every
lane query. `rejected-eta-expanded-c-excerpt.txt` preserves that bounded
diagnosis. It is **not** an optimization result or the final source.
The first receiver check also rejected an incorrectly counted proof binder
and inaccurate expected axiom text; both were corrected, with final standard
axiom pins checked. No failed guard was waived.

The successful implementation forces a first-order record before creating
the projecting closure, which survives compiler arity transformations in
the inspected C. An independent read-only review confirmed exactness and
the same receiving shape, as reported to root.

No private process sample, environment, configuration, signed call, genesis
or state store is included. This archival task changes only this directory;
root owns the evidence index, shared hash manifest, graph status and runtime
measurements.
