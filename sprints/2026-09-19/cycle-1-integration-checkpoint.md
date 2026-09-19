# Mini cycle 1 integration checkpoint

Recorded September 19, 2026, approximately 20:50 UTC. **Integration remains in progress.** This records measured intermediate state, not a completed platform or a completed native journey. The original [cycle contract](cycle-1.md) remains unchanged.

Mini source is committed and pushed through `7c4b525`. The cycle added the general joint resource path, typed content, current-rule observation checks, explicit capability revocation, grant-preserving policy replacement, source-owned JSON authoring and the Rust client. The compiled acceptance fixture exercises these through signed native calls; its complete result is still pending.

The [round-6 full umbrella](cycle-1-evidence/full-gate-green-20260919T202556Z/README.md) passed before the latest performance changes. Its source manifest covers 584 Lean modules; it includes explicitly preserved unrelated working-tree imports. An independently identified native executable installed the exact two-resource birth in [223.78 seconds](cycle-1-evidence/birth-benchmark-20260919T202801Z/README.md). Later CLI operations reopen and semantically verify history, making that cost recur. This is a practical obstacle to the intended shell experience.

Three measured paths led to proved implementation changes:

- The earlier cast-injectivity check repeatedly cast the full source-slot list. Its replacement preserves the original proposition while deduplicating source integers and sharing their casts.
- Keccak theta recomputed column sums inside every output lane. `722a8bb` adds a general equality theorem and compiler substitution; the [matched primitive measurements](cycle-1-evidence/theta-sharing/README.md) show about twice the speed, with existing NIST/SHAKE fixtures passing. This is not yet a host-speed measurement.
- Birth admission constructed complete hashed requests merely to project pre-state, repeated its policy step, and recomputed request identities during pairwise comparison. `7c4b525` supplies exact pre/post selectors, shares the step, and checks the same full-wire injectivity condition over materialized identities. Helper, controller and receiver component checks passed; independent generated-C review confirmed the sharing survives compilation. Complete rebuild and native measurement are pending.

The Rust client passed birth and actual lost-response recovery before encountering a fixture assertion that expected an empty scalar page. The canonical page contains a neutral `object601.field1=0` entry. `a47c727` corrects that assertion without changing the host. A fresh full client run is required; the failed fixture run is not a pass.

The current native journeys and broad proof rebuild continue against immutable, separately hashed executables. A combined performance candidate is being built in a separate native snapshot. Build scripts now preserve existing executables and compile the acceptance runner against the host's exact object namespace. Final integration must record the actual tested binary, matching source manifest, complete journey results and remaining constraints before closing work records.

Nothing here establishes hosted Hermes, physical tool interruption, provider dispatch, OpenRouter custody, TLSNotary, Solana staking, or deployed STARK assurance. The task-resource generation fence is a kernel rule; stopping a real process remains host work. No graph work item is closed by this checkpoint.

## Addendum, approximately 21:05 UTC

The matched birth now completes in **49.43 seconds**, versus 223.78 seconds on the previous candidate, with identical original signed bytes, genesis and returned receipt bytes. The [birth and order evidence](cycle-1-evidence/birth-and-order-sharing/README.md) preserves the source proofs and measurements.

The first task query exposed a separate exponential computation in `PredOrder.binaryDigits`: executable `Fin.cases` evaluates ignored predecessor results. `12e6608` proves an equivalent direct bit selector, with `[propext, Quot.sound]`, and generated native witness code uses it. The previously interrupted query completes in **33.55 seconds** on host `0da9f1392fad3913356e3a495f0d3ab4f1a247aec8988a9f90312666e9ccadc1`, returning generation 0, paused status, remaining 100 and reserved 0. Its [captured result](cycle-1-evidence/order-query-benchmark/README.md) is a completed query, not the entire journey.

The theta-only broad umbrella subsequently passed in 1,532 seconds. The final umbrella is now rebuilding the birth and order changes against committed `Compiler.lean`, excluding unrelated shared-tree imports in this isolated build only. The combined native host has all 153 host-source files checked against the canonical tree. Fresh New World, legacy and corrected Rust-client journeys are running on this same immutable host; complete results remain pending. The earlier legacy candidate had passed six mutations, current-rule enforcement and hostile-history checks before root interrupted its final replay loop to test the combined candidate.
