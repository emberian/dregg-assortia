# Theta sharing — component evidence only

Archived September 19, 2026 from the completed `orient_mini_semantics` lane. Root identifies minidregg commit `722a8bb` as containing the optimized source. [Source identities](source-identities.txt) retain its exact hash, the baseline source hash and the unchanged timing fixture hash.

The general theorem `theta_eq_thetaCached : theta = thetaCached` proves equality for every input array and supplies the `@[csimp]` compiler substitution. Its pinned axioms are `[propext, Classical.choice, Quot.sound]`; see the [source excerpt](Sp800185Cshake256Core.source-excerpt.txt). Five column parities and five deltas are computed once per round. Hash framing, constants, FFI, profile and replay semantics are unchanged.

Three matched **Lean `--run` primitive** trials gave median elapsed times of **4.147 s → 2.059 s**, approximately **2.01× faster**. Each trial hashes twenty varying 4097-byte messages and consumes every output byte. All six checksums are `80425`. This is neither a native-host latency measurement nor evidence that a complete agent-grain operation succeeds.

The [original lane record](original-record.md), [fixture](cshake-primitive-bench.lean) and six tiny timing logs are copied byte-for-byte. The record retains its original temporary paths and historical build status; its baseline-source reference points to the original temporary evidence directory, not to a file included here. Full baseline source, native binaries, credentials and process samples are excluded.

The lane observed exit 0 for the direct proof/C check and the existing NIST SP800-185/FIPS202 SHAKE256 conformance checks. Their captured logs, `theta-proof-final.log` and `theta-conformance.log`, are empty. **The exit statuses are lane-reported tool results; empty logs alone do not establish successful exits.** Commands and measurement boundaries are retained in the original record. Nothing was rebuilt or reexecuted for this archival step.
