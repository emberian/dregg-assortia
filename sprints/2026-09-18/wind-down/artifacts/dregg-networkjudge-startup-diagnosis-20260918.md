# NetworkJudge native initialization: source diagnosis, 2026-09-18

## Evidence boundaries

Runtime lane `resume_runtime` measured the real native initialization coordinator in `/tmp/dregg-resume-ffi-full-lifecycle-20260918.log`. First two fresh-process tests report NetworkJudge inclusive initialization at 53,511.558 ms and 53,860.763 ms. NightWatchCampaignWire follows at 116,696.140 ms and 117,968.131 ms. Each timer wraps the generated initializer and includes imports not already initialized; no term-level time attribution is available.

The inspected local generated C for NetworkJudge, NetworkJudgeWire, Emit and DeckDescent is byte-identical to the receiving hbox lane's generated C, per `/tmp/dregg-resume-initializer-generated-c-20260918.json`. No new builds or native probes were launched by this diagnostic lane. Those hashes identify the pre-change baseline; the coherent post-change build and fresh-C audit are recorded below.

## Mechanism proven by generated C

`metatheory/.lake/build/ir/Dregg2/Games/PathOfAngels/NetworkJudge.c:3447` initializes NetworkJudgeWire at line3457, then eagerly assigns 42 closed declarations. All26 `check_*` Bool definitions are among them; these are actual calls, not eliminated proofs. At line3460 it calls `_init_...check__fixture__processSignalWire__success`; line1140's closed thunk calls the real `processSignalWire(fixtureInputBytes)`, and line1170 forces the thunk. Refusal fixtures likewise encode modified inputs and invoke the real judge at startup.

NetworkJudgeWire.c:31910 initializes Emit. Emit.c:23543–23549 initializes DeckDescentEmit, ArtificerLogicEmit and VentCrawlEmit. Emit itself eagerly computes `signalRulesTable` (line23581), `signalDescriptorJson` (line23586), relay/salvage/black-box descriptors and26 check Bools. These are unnecessary to initialize the judge's function entry points, although the descriptor computations have legitimate emission consumers and must remain available.

The existing local generated-C import inventory `/tmp/dregg-networkjudge-init-source-inventory.json` reaches35 Dregg2 modules,500 direct eager assignments,185 of them `check_*` values. This is a source inventory, not500 expensive calls or185 independent costs. Some imports are already initialized before the NetworkJudge timer starts.

The August fixture split moved `native_decide` proof evaluation but left closed `Bool` computations in production modules. Its docblocks accurately described def elaboration but incorrectly implied that this avoided runtime evaluation: generated initializers compute those values eagerly.

## Completed bounded source cut

The first bounded cut changed `metatheory/Dregg2/Games/PathOfAngels/NetworkJudge.lean` and `NetworkJudgeFixtures.lean`. The42 fixture/check definitions moved into the existing assurance module in the same namespace with the same open directives. Their entire source block is byte-identical. All26 existing theorem/native_decide/assert_compiled pins form a byte-identical suffix. All14 runtime axiom assertions remain (12 at the bottom,2 earlier), as do the exported judge and all runtime definitions/general theorems. Both headers now distinguish elaboration from native initialization.

A complete Lean-source text consumer scan found none of these42 definition names outside NetworkJudge and NetworkJudgeFixtures before the move. PathOfAngelsGuards still roots NetworkJudgeFixtures via lakefile.toml. Audit hashes, before-copies and non-Git diffs are in `/tmp/dregg-networkjudge-fixture-cut-20260918/`.

Status: source-preservation audits and the subsequent coherent Lean/fixture build pass. Post-change native timing is owned by the runtime lane; do not attribute the full53-second interval to this cut without that measurement.

## Second approved source cut: completed and compiled

DeckDescent.lean:1504–1542 contains6 definitions solely for assurance: blindBanked, blindAlive, blindStep, bestBlindFrom, bestBlind and check_no_blind_line_banks_every_board. `bestBlindFrom` traverses the actual nine-action alphabet to depth AIR=9, pruning families with no live boards. `bestBlind` executes that exhaustive search as a closed Nat.

The exact compiled path is DeckDescent.c:14645 (module initializer calls `_init_...bestBlind`) → line10345 (forces its closed thunk) → line10335–10341 (invokes actual `bestBlindFrom` with9). The source is DeckDescent.lean:1524–1533. Text references to the first5 names occur only in that block; the check's only external consumer is the existing `no_blind_line_banks_every_board` theorem in DeckDescentFixtures.lean:37, with its compiled axiom assertion at line100. Root approved the cut, and that entire6-definition block has now moved into DeckDescentFixtures before the existing theorems. The moved block and entire21-theorem/compiled-assertion suffix are byte-identical; all83 runtime axiom pins remain. Audit/before-copies/diffs: `/tmp/dregg-deckdescent-fixture-cut-20260918/`. Do not replace the search with a constant4, weaken the assertion, or change gameplay.

This removes the source-proven exhaustive startup search without changing production algorithms. Its individual elapsed contribution is not measured.

## Further work requires coordinated consumer movement

NetworkJudgeWire.lean:1806 onward carries its own fixture data,13 checks and a native fixture target proof. This can move to assurance, but RecordsRuntime and FinalizedRunEventAggregate currently consume its fixture bytes in their own closed fixture blocks. Those fixture consumers must move too; importing assurance back into runtime would restore the problem.

For actual descriptor emission, split the reusable emitted mission/config constructors from the all-game descriptor rendering module, retaining existing namespaces and one implementation. NetworkJudge requires signalConfigWith and ventConfigWith; NetworkJudgeWire uses additional Emit APIs. An exact dependency/consumer inventory is necessary before that wider move. Rendering tables are legitimate work when emission is requested, not during judge registration. Merely deleting module initialization or adding a dummy Unit argument is not the proposed repair.

Keep the current shared initializer coordination and semantic functions. After coherent C/olean generation, re-run the existing same-path native lifecycle probes and compare timings, while retaining the existing assurance proofs. A Rust-only archive splice cannot certify the new Lean source.

## Verification coordination update

The runtime owner completed all3 pre-change native full/ST lifecycle probes,564.570s total, then accepted the combined executor patch and these4 Lean sources for the next hcargo sync. Its agreed bounded command is the hbuild equivalent of `cd metatheory && lake build Dregg2.Games.PathOfAngels.NetworkJudgeFixtures Dregg2.Games.PathOfAngels.DeckDescentFixtures Dregg2.FFI`, under SWARM_MEM_MAX=32G, LEAN_NUM_THREADS=2 and DREGG_LEANC_JOBS=4. The runtime owner alone owns that build and ensuing strict native archive splice/tests.

`/tmp/dregg-networkjudge-deck-coherent-source-20260918.json` captures371 in-tree source/config hashes for the actual FFI import closure plus the2 assurance roots. Both assurance modules are absent from FFI's import closure and remain explicitly rooted in lakefile.toml.

`/tmp/dregg-check-fresh-fixture-initializers-20260918.py <repo>` is a read-only generated-C audit for after the remote build. Its check intentionally fails against unchanged local baseline C, finding all48 moved symbols still present. A post-build pass must demonstrate their absence from runtime C and records the new hashes/eager assignment counts. No new build or compiler was started by this diagnostic lane.

## Coherent remote check completed

Runtime reported actual hbuild PASS in `/tmp/dregg-resume-fixture-closure-build-20260918.log`: both fixture roots plus Dregg2.FFI completed3340 jobs under the agreed budget. DeckDescentFixtures took96s and NetworkJudgeFixtures7.7s. This confirms the preserved compiled assurance assertions remain checked.

Fresh generated-C audit PASS is captured in `/tmp/dregg-resume-fresh-fixture-initializers-20260918.json`: all42 moved NetworkJudge symbols are absent from runtime C and its direct eager assignments are0; all6 moved DeckDescent symbols are absent and29 direct eager assignments remain. These are measured generated-artifact facts, not elapsed-time attribution. A later native capture on the same receiving path measures combined initialization changes.
