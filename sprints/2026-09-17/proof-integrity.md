# Programmable nexus: load-bearing proof and compiler work

Source audit by Astra `/root/sprint_proof_integrity`, 2026-09-17. This is a proposed implementation sequence, not a claim that any implementation or new runtime check has run.

## Recommendation

Begin with the canonical flat transition contract selected by minidregg decision D-0002, and make program installation one instance of it. The first bundle should force the relationship between the requested authority, the complete write footprint, the actual balance changes, the installed program bytes, and the canonical before/after state. Derive the executable checker, circuit, witness interface, public statement and receipt from that same declaration. Shell entry points can develop against that contract while this core work proceeds.

Do not spend the first bundle making an existing `SetProgram` proof produce successfully: its current theorem and producer have different, substantive omissions. Likewise, the existing declared-action AIR is a bounded reflection theorem about a statement-specific descriptor, not yet a generic proof of an authenticated programmable state transition. These are implementation work to close, not permanent limitations to accept.

In parallel, integrate the strongest applicable IR2 proof-frontier patches and instantiate their exact descriptor/lookup/quotient and native-controller obligations. That is a different dependency chain from proving a particular cell rule. A correct proof system proves the statement it receives; it cannot repair an insufficient statement.

## Evidence scope

- Read breadstuffs continuity, August 11 handoff, memory index and relevant flagged records, overview, current claim/commitment sources; minidregg `CLAUDE.md`, `ATLAS.md`, accepted decisions and relevant source; zkml-research instructions, verdicts, proof-frontier sources and captured artifacts.
- No builds, prover runs, live-node probes, code edits, Git commands, deployment, key operations or shared-tree mutation in this lane. The only output written is this report.
- Root independently reports breadstuffs HEAD `3e51def6a5a95424e54fbe7432539b06088de5c3`, with `cell/src/commitment.rs`, `circuit/src/cap_root.rs`, and `Circuit/{CircuitSoundness,ApexFloorFree,EffectRefinement}.lean` clean. Root reports minidregg HEAD `6937394e1dc2c2aaff986c7d4b3a258aca5d16fd`, with `Theory/DeclaredActionLowering.lean` and `Kernel/DeclaredActionExecution.lean` clean. Other anchors are current source inspections; relevant hashes are recorded below.
- Independently checked that all three selected-column research source hashes match their retained `CHECKS.json`, and that the terminal-control result and command JSON hashes match its README. This verifies artifact identity, not a fresh execution.

## What must be repaired, and what each finding means

### 1. Authored action state changes are not yet covered by the advertised resource law

**Source-level semantic gap, independently confirmed with `sprint_kernel_carrier`; no reachable runtime exploit claimed.**

`minidregg/Theory/DeclaredActionLowering.lean:44–69` permits `create` and `write` on every `StateKey`, including `.accountBalance`. At `:104–111`, only `move` creates postings. At `:295–302`, all checked writes become field writes and the patch has no resource writes. `Declaration.postingSum_zero` therefore proves the sum of an independently derived posting list, not that the actual account-balance fields changed by that sum.

`Kernel/DeclaredActionExecution.lean:67–78` sets `ResourceLaw.delta` from those postings. Its typed aggregate balance proof then sums them. A declaration that writes `accountBalance(a,r)` from `b` to `b+1` has no move postings, but its state change is nonzero. This is a constructive counterexample recipe over the source definitions, not an executed Lean witness in this audit.

**Closure:** separate freely mutable fields from linear resource state in the authored language, or derive *every* resource delta from the resulting canonical patch and prove exact agreement with semantic before/after balances. Raw writes must not mint resources. Prove actual-state conservation with issuer/source accounting where applicable, over repeated writes, self-moves, multi-incidence composition and full-width amounts. The law cannot be merely a supplied `delta` function.

### 2. Authorization is not yet forced to cover the canonical state and every write

**Source-level missing relation, not a claim that all policies admit arbitrary writes.**

`Theory/DeclaredActionLowering.lean:395–414` derives one authorization target/verb from the declaration's type, while its action keys remain arbitrary. `ValidAt` at `:418–423` requires root equality and guard/post equality only; `Accepted`/`accept` at `:445–470` add authorization for that request without a key-to-target obligation.

`Kernel/DeclaredActionExecution.lean:37–39` supplies `AuthorizationProjection.project := fun _ => authState`. The projection does not inspect the canonical pre-state. Generic higher-level policy can constrain more, but the carrier by itself does not establish the D-0002 invariant that authorization comes from the same canonical state and covers the complete effect.

**Closure:** make the concrete authority/policy registry part of canonical materialized state; derive the request's authorities and resource scope from each incidence's actual footprint. Prove authorization for another object, stale policy epoch, replaced program, wrong effects digest and wrong pre-root cannot construct an accepted effect. Keep policy data and actual code identity bound; a true admission bit is not the policy.

### 3. The existing action AIR is a real but narrower theorem than the required proof

**Compiler-to-consumer obligation.**

`Compiler/DeclaredActionAir.lean:10–21` explicitly scopes itself to a statement-specific descriptor and excludes policy verification. `publicBytes` at `:109–111` consists of declaration bytes, policy id/epoch and the claimed pre-root. `pinSystem` at `:292–315` pins all values to a canonical assignment computed from `context`, `declaration`, and the externally supplied `fields`; `descriptor` at `:380–386` is specialized to those values. `descriptor_accepts_iff_run` at `:412–418` reflects the guarded write fold under `CodesBounded` (`:122–127`).

This theorem does not derive that its supplied field store is the one committed by that pre-root, nor that a policy was satisfied. Pinning a descriptor to an untrusted candidate's observation trace cannot supply that missing trust. The semantic `Int` model also exceeds the single-field encoding's proved range.

**Closure:** compile a program's actual predicate/effect semantics with authenticated pre-state reads, canonical field/byte encodings, explicit range/limb constraints, complete post-state writes and frame conditions. Make descriptor identity selected by authenticated program state. Close the selected source-to-descriptor theorem over adversarial witness assignments, rather than requiring the truthful private assignment as input to descriptor construction. If an admission checker reads full state directly, its trusted Lean check and its circuit relation must agree; it is not a substitute for the promised succinct proof.

### 4. Breadstuffs program installation is not a complete alternate path

**Missing native/witness wiring plus a theorem that assumes its semantic conclusion.**

The executable Rust `SetProgram` path exists. `turn/src/rotation_witness.rs:1208–1216` explicitly classifies it as `UnprojectedMover`: no VM row and no AFTER-cell program projection. `sdk/src/cipherclerk.rs:5536–5547` consumes that classification before cohort dispatch and refuses. Retain that guard until the repaired path replaces it.

`metatheory/Dregg2/Circuit/RotatedKernelRefinementProgram.lean:73–118` carries `cellMapMove`, guard, log advance and all frames in its readout. Its `setProgram_descriptorRefines_sat` at `:171–182` constructs `SetProgramSpec` exclusively from those readout fields; neither `hsat` nor `hside` is consumed. The separate `setProgram_forced` theorem at `:130–157` uses a record pin, but its decoding/PI premises identify the residue with a singleton integer program-slot digest. The real source value is a structured `CellProgram` folded with other authority data. Its header's claim that the runtime maps `SetProgram` onto a set-VK row conflicts with the actual producer coverage.

**Closure:** a program identity must commit to canonical complete code/predicate data, semantics/schema version and relevant parameters. The install transition must authorize under the correct existing authority/policy, force the new program field and all untouched authority/state fields, then make subsequent invocation load exactly that committed program. Replace the readout's supplied transition with extraction from constraints. Implement the native wire/reconstitution, source lowering, emitter, witness, verifier selection/anchors and durable consumer as one compatible change.

**Important distinction:** a succinct verifier taking `NEW_COMMIT` from the claimant is normal. `turn/src/executor/proof_verify.rs:857,926–936` is not itself an exploit because it does that. The AIR and public anchors must bind that claim to the actual permitted transition. The repair is constrained canonical preimage/transition binding, not mandatory full re-execution by a light client.

**Additional high-priority candidate, independently source-checked after `sprint_program_install` found it:** `exec-lean/src/lean_shadow.rs:1898–2016` projects state fields, cap edges, lifecycle and delegate pointers into `WireState`, but does not carry the installed structured `CellProgram` or slot caveats. Producer eligibility at `:882–895` is a predicate on `Turn`, not on the program-bearing ledger. `exec-lean/src/lean_apply.rs:1796–1914` calls the native Lean producer, runs Rust as a reference, and at `:1904–1913` installs a Lean COMMIT even when Rust refused; `node/src/executor_setup.rs:529` consumes this path. Therefore a direct `TurnExecutor::execute` program-rule test does not establish that the node-shaped producer enforces the rule. The immediate diagnostic should install a monotonic/forbidding program and submit a violating covered self-target write through `produce_via_lean`, requiring the native archive and classifying the resulting producer outcome. No such execution occurred here; host/reconstitution details could still cause refusal. If reproduced, close it by carrying and evaluating the actual installed rule in the authoritative kernel/controller. Simply reverting authority to the Rust reference would not complete the intended design.

### 5. Capability target commitments still lose source identity

**Exhibited encoding collision; full credential/valid-cell exploit preconditions were not established in this audit.**

`cell/src/commitment.rs:556–588` builds the legacy seven-field `CapLeaf`, folding target bytes at `:566`. `circuit/src/cap_root.rs:216–254` confirms the committed target is a single felt. Its `fold_bytes32` at `:283–284` hashes eight *reduced* u32 chunks; byte siblings that differ by the field modulus can reach identical hash input. This is distinct from the linear `effect_vm::fold_bytes32_to_bb` function; do not assign the latter's O(1) target-solve argument to every hash-derived target in the system.

`metatheory/Dregg2/Circuit/CapLeafTargetLanes9.lean:220–224` proves the explicit old leaf alias for any downstream hash, while `:233–245` uses the injective nine-lane source encoding. Its proposed leaf is padded/domain-separated to an admitted arity16 shape; `circuit/tests/cap_leaf_target_lanes9_pins.rs` retains old/new poles. **The cutover has not occurred in the inspected committed producer.**

Do not directly install `circuit/src/exact_cap_root.rs` as the solution: `cap_root.rs:281–282` records that its Rust-authored sixty-felt preimage has no Lean authority and is not an admitted chip arity. Also, target-only widening does not by itself repair breadstuff/custom-authority/provenance fields. Audit the entire authority leaf required by the chosen programmable-resource path and derive its canonical source binding in Lean.

**Closure:** complete authority leaf encoding + semantic membership/update constraints + producer/consumer cutover, one descriptor/VK/state-root epoch, old-shape refusal, canonical genesis/replay. If the selected new kernel replaces this tree, retire its old consumer rather than retaining two authoritative leaf schemes.

`node/src/turn_proving.rs:1168–1169` separately still folds NoteSpend nullifiers, with `:1172–1184` identifying the freshness set consumer. That is a real known repair track, but the ordinary programmable nexus has not yet been shown to consume NoteSpend. Do not conflate it with the generic joint-turn nonce/nullifier boundary or silently treat it as fixed by cap widening.

### 6. The old global apex is not a release certificate

**Residual theorem assumptions and wrong-model boundaries; not a proof that every deployed statement is forgeable.**

Current `CircuitSoundness.CommitSurface` retains `restFrame : RestHashIffFrameFin RH` (`:157–181`). The finite-support commitment theorem at `:284–311` also requires explicit representability and no actual collision. The source notes the deployed-width problem and the still-needed per-effect representability preservation. Read these fields, not the older overview's unconditional prose.

The useful successor is `ApexFloorFree.lightclient_unfoolable_free` (`:250–273`). It properly carries three distinct obligations: `StarkSound`, witness-to-canonical-state existence, and `descriptorRefinesFree` for the actual published effect. It composes those obligations; it does not independently discharge them for every installed application. Its existence conclusion is not unconditional injectivity of a finite cryptographic digest.

**Closure:** use an explicit finite canonical state model and a computational collision/extraction failure boundary. Discharge the actual selected program's refinement and witness extraction. Do not introduce impossible global hash-injectivity floors, or replace a missing semantic implication by a named assumption holding the same conclusion.

## September IR2 frontier: what is actually reusable

All paths in this section are under `zkml-research/research/proof_frontier/2026-09-08/ir2_verifier_bridge/` unless otherwise stated. Parent README and NEXT files are stale relative to some completed successors; read the successor theorem and checks.

1. `src/Selvage/Ir2FriSoundness.lean` / parent README: native barycentric folds, actual BabyBearExt4 roots, bit-reversed row transport and a shared-query event are connected to a conditional fresh-randomness proximity theorem. The recorded canonical profile uses domain heights `17→14→11→8→5→3`, width-eight folds then width-four, and q38. Its stated conditional numerical term is about `3.71319e-9`, **not a deployed cryptographic-security estimate**.
2. `packed_extraction/src/Selvage/Ir2PackedSoundness.lean:29–42`: `supplied_fresh_38` constructs the relevant words from commitment-time packed logs and retains an explicit observed extraction failure term. The extraction is not merely an assumed global-word witness. Salt shapes, flattening order, path direction, fixed-height concatenation and cap shape matter.
3. `packed_extraction/pcs_batching/Selvage/Ir2PcsBatching.lean:155–208`: the native ordered reduction has 5,271 quotients, a single alpha power sequence and the actual coset31 substitution. `actual_bad_alpha_probability` closes the fresh-alpha batching argument under off-domain and no-common-nearby-explanation premises. This successor is complete despite its parent's "active construction" wording.
4. `air_pcs_join/selected_columns/proposal/Compiler/Ir2SelectedAirPcs.lean:28–42,44–87`: the strongest inspected head is `selected_air_pcs_soundness`. It selects nearby polynomials from pre-zeta commitment words; it no longer assumes every committed column is exactly a low-degree codeword. It still requires the actual constraint polynomial family, residual/equation identity, source rows and checkpoint logging. It retains shaped hash/on-domain failure and fresh-challenge assumptions. The module's exact axiom pin is at `:93–95`.
5. **Actual old-statement exploit artifact:** `air_pcs_join/native_terminal_control/results/control001/artifacts/result.json` records a malformed last row accepted by the old BFV query template and by an actual serialized/deserialized native proof verifier. Row8191 column43 changed11→10 with the matching public tuple; exactly one witness cell changed. The repaired compiler-generated template rejects the row in the main-gate evaluator, and the old proof rejects under the repaired statement. The retained proof hash is `3497e4a37522cc9d188d0d11bcecc86cb194af0580f336d2b8860205e24714c8`. This is a bounded executed statement exploit for that research profile, not an observed attack on every breadstuffs cell.
6. `air_pcs_join/whole_domain/whole-domain-query.patch` is the compiler-owned selector repair. It makes source assertions cover every relevant physical row, including the terminal row, while preserving arithmetic bodies. It belongs with the source compiler and its consuming template, not as a handwritten Rust AIR patch.

Current minidregg main has none of `Compiler/Ir2SelectedAirPcs.lean`, `Compiler/Ir2NearbyColumns.lean`, `Selvage/Ir2PackedSoundness.lean`, or `Selvage/Ir2PcsBatching.lean` at their proposed paths (exact existence checks, not a whole-tree absence claim). The patches are reusable work, not already integrated security.

**Remaining constructive proof-system work:** instantiate the native main/range/LogUp equations and quotient expression; derive selected-polynomial base-domain source rows and required field descent; connect arbitrary accepted byte proofs to the typed theorem; price or explicitly bound actual shaped Poseidon extraction failures and Fiat–Shamir/PoW challenge generation. Fresh uniform challenges cannot silently replace the actual duplex transcript, and dependent beta/beta²/beta⁴ subfolds cannot be charged as independent rounds. These are distinct proof tasks; increasing query count alone does not close any of the semantic bindings above.

## First implementation bundle and dependency order

**Bundle A: canonical authored-program transition.** Start immediately in the minidregg carrier/program lanes, with one jointly reviewed contract before modifying shared types:

1. Define the authored program/rule record and practical lawful bytes, including exact schema and semantics version. Replace the existing declaration unary codec (`DeclaredActionLowering.lean:271`) for operational use; do not run realistic nested codes through it as a benchmark.
2. Repair the action/key/authority/resource relations described above. Derive authority from canonical pre-state and prove actual-state balance delta from the same patch. A program install must not grant itself new authorization by replacing policy in the same incidence.
3. State the accepted-install/invoke theorem before building its proof: exact requested program installed; future invocation uses that program; all reads authenticated; every affected resource authorized; actual resource conservation; exact changed footprint; untouched state framed; stale roots/epochs/nonces refused.
4. Make positive and negative inhabitants constructive: legal install and call, unauthorized foreign write, balance mint through raw write, altered program bytes under the same requested identity, wrong old-state opening, same-turn weakening, stale replay, and last-row violation. No readout may supply the intended post-state equation as its proof.
5. Derive the executable Lean decider and compiler reflection from that declaration. Extend missing source vocabulary, including full-width range/ordering or authenticated state access where the first rules require it. Unsupported cases are work to implement, not permanent feature exclusions.

**Bundle B: the same statement across the real consumer.** Bind generated source identity, compiler version, descriptor, witness layout, public input order, native work/ABI and verifier profile. Wire shell/agent bytes to the Lean-owned request decoder and acceptance; candidate Rust compute returns bytes/errors only. Durable commit must consume that exact accepted effect, atomically performing pre-root CAS, nullifier insertion, cost accounting and receipt append. Reopen must replay the exact program/code identity and intermediate state roots. This is where shell integration becomes a real path through the kernel.

**Bundle C: commitment/circuit flag day.** Change every legacy producer/consumer still on the selected path, including program AFTER binding and authority-leaf encoding. Derive emitter artifacts; move all descriptor/VK/registry pins and genesis roots together; reject the old shape. Do not connect a new producer to an old statement and call the resulting refusal a feature limitation. Do not waive the sovereign after-cell gate while the bundle is incomplete.

**Bundle D: proof-frontier consumer.** Integrate the inspected patch dependency closure into an isolated source copy for review, then replace the chosen source/compiler consumer in the authoritative tree. Instantiate the actual native equation/lookup/profile join for the nexus statement; avoid independently maintaining a BFV-only theorem island. Preserve standard cryptographic assumptions where necessary, but make reductions and concrete transcript/profile obligations explicit and executable as part of the same selected verifier path.

These bundles can overlap across owned files. They should converge on one accepted transition and one proof relation. A permanent old/new executor split would recreate the problem minidregg was founded to remove.

## Design coordination with the other sprint lanes

- **With `sprint_kernel_carrier`:** honor accepted D-0002's flat canonical hyperedge; do not make legacy call-forest coverage a prerequisite. Its source investigation found the balance/authority mismatch, independently confirmed here. Agree on `delta = actual canonical post-minus-pre` and exact footprint authority before dispatching an effect compiler lane.
- **With `sprint_program_install`:** existing `SetProgram` spec treats `prog : Int`, while the user-facing source is structured program/rule data. Agree on the actual code record, content commitment, versioning and upgrade timing. The existing refinement theorem's `cellMapMove` is a premise to eliminate, not a reusable completion certificate. Its shared source field should be the same one the canonical controller later loads.
- **Native boundary:** minidregg's accepted `docs/decisions/2026-08-09-rust-native-authority.md` makes Lean authoritative for statements, scheduling, challenges and acceptance. Rust returns fallible candidate bytes, not a semantic verdict or receipt. Adopting the IR2 research's source-inspected Rust verifier as semantic authority without a Lean controller/refinement would be a design change, not a routine port.
- **Commitment format:** do not choose the old seven-felt cap target, reduced-u32 octet encoding, and exact-sixty-felt Rust leaf in different lanes. Source identity is injectively encoded first, then cryptographically committed with the required domain/shape. If a leaf/VM interface must grow, grow it in the authoritative source compiler and cut every consumer over together.

## Bounded verification recipes after implementation

No command in this section ran in this audit. These are recipes for the implementation owner; root should serialize heavy work on each box and select/lease actual warm lanes. hbox storage must be under `/tank`.

- For a changed minidregg proof, run `LEAN_NUM_THREADS=4 lake env lean <changed-file>` inside the copied lane and `bash scripts/check-import-boundary.sh`. On hbox wrap all builds with `swarm-build`; after a coordinated interface wave, root runs the required `lake build Minidregg` integration gate once. Exact `#guard_msgs` axiom pins, positive/negative witnesses and premise inhabitation are part of the changed proof check.
- For breadstuffs proof changes, a warm hbox lane can use `SWARM_MEM_MAX=64G LEAN_NUM_THREADS=4 scripts/hbuild <leased-lane> bash -c 'cd metatheory && lake env lean Dregg2/Circuit/<changed-module>.lean'`. Confirm warm Dregg2 artifacts and archive freshness first; do not accept a missing native Lean archive as a failed semantic test or set `DREGG_REQUIRE_LEAN=0`.
- Validate Rust test names before running. Existing focused targets include `cargo nextest list -p dregg-turn --test sovereign_after_cell_weld_ledger` and `cargo nextest list -p dregg-circuit --test cap_leaf_target_lanes9_pins`. Use the same target with `cargo nextest run --release` through the leased `scripts/pbuild`/`scripts/hbuild` lane. Existing alias tests intentionally demonstrate the old wound; change their expectations only alongside the actual consumer replacement and new positive coverage.
- The emitter entry point is `scripts/emit-descriptors.sh`, with the declared VK epoch acknowledgment after review of what moves. Run its idempotent pass after the generated flag day, then the descriptor/pin closure checks for the changed dependency cone. Root has reported standing development rekey authority; a public/mainnet or provenance stamp is a different action.
- `scripts/check-no-degraded-felt.sh --rev HEAD` is the existing committed-source gate; it is currently expected to find known live folds. A green after the repair must come from changing the authoritative commitment/consumer, not an allowlist. A remaining unrelated NoteSpend red does not validate or invalidate the cap repair by itself.
- The decisive system check is one newly authored resource rule installed from shell bytes, successfully invoked, rejected when violated by an adversarial witness, then observed at the same canonical root and receipt after restart. Include a proof generated from a forged candidate directly, bypassing the honest witness generator. Also drive the rule violation through the real native producer entry point, not just the Rust executor. That demonstrates the statement and consumer, not merely the generator's behavior.
- All destructive red-proof mutations run on scratch copies/remote lanes. Retain exact commands, source/descriptor/profile pins, actual assertion counts and full verdict. `pbuild: VERDICT outcome=REFUSED` or `outcome=ENVFAULT` is not a code verdict. No whole workspace/heavy proof gauntlet per edit.

## Selected source identities

```text
b8a12ef4d5a93ac915ef2134bdf1da0273e9c4f54d59cd398705f98c5ee36576  breadstuffs/cell/src/commitment.rs
b9d3cffde3605088dd9e5ba5d445793604302e0b0d23c7d63e38a1d6d43e5353  breadstuffs/circuit/src/cap_root.rs
9f685a818446fa401f90918921adebc8cf58c0ebf02ca4b3221e510394ead08a  breadstuffs/metatheory/Dregg2/Circuit/RotatedKernelRefinementProgram.lean
b180e86e449be5c6f0c33cbdf4fde07aef16801202b06a85798417482bda6eee  breadstuffs/turn/src/rotation_witness.rs
a16058ae663c3c44c9d6dd7540568deabf063412983d7999b22b4b98e15f4c5f  minidregg/Theory/DeclaredActionLowering.lean
7fd4ed71d9b1fc1ae8f94bede1e9f00c42388512c6b35b1c329232d02ccb3d53  minidregg/Kernel/DeclaredActionExecution.lean
ba5df6c78dd067e8cb25fe492bda4bdb2ff9aa222a7b4ce4826a47713e3299d3  minidregg/Compiler/DeclaredActionAir.lean
0af8ed5fb9f942331d1f2902a6b44039077ec0e0e4fa4153b3ffd2fe9be6af6f  selected_columns/proposal/Compiler/Ir2SelectedAirPcs.lean
8afc17f7d3820f5cd514508b24fc0d225340a4ed1eebb46d9c17854adf7493fe  native_terminal_control/results/control001/artifacts/result.json
```
