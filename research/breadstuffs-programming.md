# Breadstuffs programmable kernel routes — source-only audit

Read-only investigation, 2026-09-17. No builds, tests, live probes, Git operations, or repository edits. Source references describe the inspected working tree, not an executed result.

## Finding

There is genuine program-as-data machinery. The clearest first route is serializable cell laws plus tools that propose ordinary kernel effects. New combinations of existing laws and effects need no host rebuild. This is transition-policy programmability, not an imperative script that computes effects. Shell exposure of installation remains unestablished.

## Route 1: cell law data → installation → ordinary executor

- `cell/src/program/types.rs:6`: serializable `CellProgram::Predicate` and `Cases`; `TransitionCase` at 62 and `TransitionGuard` at 84 provide method/effect/slot guards and boolean composition. Constraints describe admissible transitions.
- `sdk/src/program.rs:136,163`: existing factory and `CellProgramBuilder` authoring sugar.
- `turn/src/action.rs:1154`: ordered `Effect::SetProgram { cell, program }`.
- `turn/src/executor/authorize.rs:2647`: self-targeted SetProgram requires SetVerificationKey permission. `apply.rs:1400` checks the same authority for cross-cell updates, checks liveness, journals old data and installs the new program.
- `cell/src/program/eval.rs:64`: evaluates matching cases, ANDs their constraints, denies unknown operation dispatch. `turn/src/executor/execute_tree.rs:640` collects touched cells, constructs context/witnesses and invokes the evaluator; refusal becomes ProgramViolation.
- `node/src/signed_turn_validation.rs:632` stages ordinary signed turns through the shared executor; `node/src/blocklace_sync.rs:9247,10376,11680` shows finalized-turn processing, shared producer invocation and commit-record construction.
- Rich effects require typed signed-envelope ingress, not the thin operator JSON projection (`node/src/api.rs:749`).

### Installation eligibility is mode-dependent — do not assume finalization

The ordinary Rust executor implements SetProgram. It is **not covered by the native Lean producer projection**: `exec-lean/src/lean_shadow.rs:748` lists SetProgram among the kinds with no wire arm. `producer_uncovered_effects` is the complement of coverage. The node's existing producer dispatcher logs a named Rust fallback for outside-coverage turns (`node/src/executor_setup.rs:571`). This is evidence of an existing receiving implementation, not a recommendation to change mode or disable a gate, and not proof that every configured node finalizes the turn.

The rotated sovereign proof producer explicitly refuses SetProgram. `turn/src/rotation_witness.rs:1212` classifies it as `UnprojectedMover("SetProgram rewrites cell.program (authority digest limbs 12..=18, 24)")`. `sdk/src/cipherclerk.rs:5537` consumes that classification and returns InvalidWitness before cohort dispatch: the shared `apply_effect_to_cell` weld does not project the write, so its after-state commitment would attest a transition that did not happen. `rotation_witness.rs:1107` also identifies the missing VM row: a lone SetProgram has no descriptor cohort, while a mixed turn could otherwise hide it behind another row.

Required missing work is therefore not merely a shell command: SetProgram needs its native producer wire/reconstitution coverage and, for the sovereign proof route, VM effect projection plus descriptor/witness and after-cell program-authority update binding. The latter changes the attested after-state and requires coordinated witness migration. A specific full-turn node route was not exhaustively traced; success there is unestablished.

Lean oracle scope must also remain explicit: `cell/src/program/eval.rs:353` fails closed for undecided constraints within its Lean subset; other named constraints have other evaluation paths. Do not describe every CellProgram as Lean-executed.

## Route 2: circuit descriptor data → local deployment → generic verifier

- `circuit/src/dsl/circuit.rs:93`: serializable CircuitDescriptor defines columns, polynomials, transitions, boundaries and public inputs. Its separate DSL CellProgram (`:1206`) has a content-derived VK.
- `node/src/api.rs:8887`: POST /programs/deploy accepts hex postcard descriptor data plus version, validates a candidate registry, durably saves it and then exposes it. Route middleware is at `:2729`. This is authenticated node-admin deployment, **node-local**, explicitly not consensus-ordered federation deployment.
- `node/src/executor_setup.rs:348` copies the registry into the executor.
- `turn/src/executor/atomic.rs:1203`: sovereign atomic verification resolves the cell VK in that registry, lowers with `cellprogram_to_descriptor2`, then verifies with `verify_vm_descriptor2`; unknown programs refuse. `circuit/src/custom_leaf_lowering.rs:20` handles a defined vocabulary and refuses unsupported forms.

Descriptor upload and supported new compositions need no host rebuild. A valid witness/trace is still required. I did not establish the complete path from a new descriptor through VK installation, proof production and canonical finalized node ingress. The atomic consumer alone does not establish that chain.

Do not conflate this with Effect::Custom: `cell/src/custom_effect.rs:183` defines host Rust verifier callbacks; `turn/src/executor/apply.rs:542` rejects Custom on the classical path; `proof_verify.rs:304` refuses proofs without a configured custom-effect registry. No node/src composition of set_custom_effect_registry was found in this pass. Arbitrary user callback deployment is unestablished.

## Recommended next single executable check — not run

Attempt one authorized serialized SetProgram through the **intended existing shell sink and its unchanged receiving/proving configuration**, recording the exact first verdict and stage. Do not presume an installation receipt. If refused, preserve the exact diagnostic and classify it against the native wire gap, missing VM row/descriptor cohort, and UnprojectedMover after-cell binding above; identify which projection/witness work the selected route actually needs. Do not disable proving, switch off the oracle, or accept a private embedded ledger as evidence for the chosen node.

Only if installation is finalized should that same check proceed to a permitted transition and a law-violating transition, requiring a finalized receipt versus ProgramViolation with unchanged state. This tests both data-defined laws and the shell-to-kernel boundary without inventing a new shell or committing to one application.
