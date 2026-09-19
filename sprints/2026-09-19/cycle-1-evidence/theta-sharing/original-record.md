# Exact theta sharing: bounded evidence

Source: `/Users/ember/dev/minidregg/Compiler/Sp800185Cshake256Core.lean`.

- Baseline source SHA256: `38dee253180ecf9fb9f19db741dff830102085a05364381d16fa0693023d6123`.
- Frozen optimized source SHA256: `dfad9ce72142d7f9d47fcb35253777eaf37256e2b5593347017ab986650497e6`.
- Fixture SHA256: `b50fb178e865d200146bab183152f4d7385c123c2dc77f8758e47c8712acf16d` (`cshake-primitive-bench.lean` alongside this file).
- Baseline source retained as `Sp800185Cshake256Core-before-theta.lean`.

The exact general theorem `theta_eq_thetaCached : theta = thetaCached` is registered with `@[csimp]`. It covers every input array, including short arrays under the existing default-lane convention. Its measured/pinned axioms are `[propext, Classical.choice, Quot.sound]`. No FFI, profile, framing, suffix, round constants, codec, or replay behavior changed. The runtime computes five column parities and five deltas once per round instead of recomputing fifty column sums and twenty-five rotations.

Direct narrow proof/C check (exit 0, empty `theta-proof-final.log`):

```sh
LEAN_NUM_THREADS=2 lake env lean \
  -o /tmp/minidregg-cycle-20260919/theta-overlay/Compiler/Sp800185Cshake256Core.olean \
  -c /tmp/minidregg-cycle-20260919/theta-overlay/Compiler/Sp800185Cshake256Core.c \
  Compiler/Sp800185Cshake256Core.lean
```

Generated C for `round` calls `thetaCached` (line 1515 in that emitted file). The isolated optimized overlay was used for execution; the shared baseline `.olean` was not overwritten.

Matched **Lean `--run` primitive measurements**, not native-host latency: twenty varied cSHAKE256 requests each comprising a one-byte varying prefix followed by a 4096-byte deterministic payload, same customization, all 32 output bytes consumed. Compilation/startup excluded by `IO.monoNanosNow` inside `main`.

| Trial | Baseline ns | Optimized ns | Checksum, both |
| --- | ---: | ---: | ---: |
| 1 | 4146953416 | 2019640542 | 80425 |
| 2 | 4532298208 | 2059449042 | 80425 |
| 3 | 4044253334 | 2133853750 | 80425 |

Median elapsed: 4.147 s → 2.059 s (approximately 2.01× faster). Checksum equality is a fixture observation; the general Lean theorem supplies the equivalence argument.

Baseline command:

```sh
LEAN_NUM_THREADS=2 lake env lean --run /tmp/minidregg-cycle-20260919/cshake-primitive-bench.lean 20 4096
```

Optimized command:

```sh
lake env sh -c 'LEAN_NUM_THREADS=2 LEAN_PATH=/tmp/minidregg-cycle-20260919/theta-overlay:$LEAN_PATH lean --run /tmp/minidregg-cycle-20260919/cshake-primitive-bench.lean 20 4096'
```

All six raw output logs are alongside this record: `cshake-theta-baseline.log`, `cshake-theta-optimized.log`, and the corresponding `-2.log` / `-3.log` files.

Existing NIST SP800-185 and FIPS202 SHAKE256 fixtures also passed against the optimized overlay (exit 0, empty `theta-conformance.log`):

```sh
lake env sh -c 'LEAN_NUM_THREADS=2 LEAN_PATH=/tmp/minidregg-cycle-20260919/theta-overlay:$LEAN_PATH lean Compiler/Sp800185Cshake256Conformance.lean'
```

No integrated host timing or operation acceptance claim follows from these primitive measurements. Build owner is rebuilding the native closure and full umbrella independently. All checks used one claimed compiler seat and `LEAN_NUM_THREADS=2`; the seat is released.
