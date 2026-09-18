# Shared Lean initialization lifecycle — implementation handoff

2026-09-18. Eight owned files are source-complete. Actual Cargo/link/runtime validation is queued through root; no performance or full correctness claim yet. A bounded independent Astra source audit found no source-level blocker; actual linked execution remains pending. Exact source hashes: [manifest](/tmp/dregg-ffi-init-lifecycle-source-20260918.json).

The existing `dregg_ffi_init` and `dregg_ffi_init_st` native ABI names now enter the same Rust coordinator as library calls. The five existing standalone native-init consumers need no call-site migration. C/C++ runtime prefixes, module lists, and the end-initialization marker are factored into private phases. All original 42 default and 21 ST module calls and their order are preserved, checked against pre-edit source. The runtime's actual default/ST selection cannot change after startup.

`deleg_admit` still invokes the identical generated Lean predicate and strict codec. Its linked export and exact Init-only module initializer are required as a pair. The coordinator initializes that family and holds its lock through each narrow call while full initialization remains deferred. It does not mark Lean initialization complete until the existing full module family succeeds. Module errors remain sticky: generated guards are set before import initialization, so no failed module is retried. Mutex poisoning also requires process restart. Mode/thread refusals do not poison a previously healthy runtime.

Secondary native host threads are attached once through `lean_initialize_thread`; their owned Rust TLS guard calls `lean_finalize_thread` at exit. The runtime-starting thread is marked separately and is neither reattached nor finalized by this wrapper. ST calls must use the selecting host thread. Native callers must enter the init ABI before Lean use and must not independently initialize/finalize the same runtime or duplicate its thread attachment.

`lean_runtime_init_status` retains default-full status; `lean_initialization_status` distinguishes the runtime mode, narrow family, default/ST full results and sticky failure. A narrow admission cannot report full initialization success. No-link/missing-pair requests refuse.

Set `DREGG_LEAN_INIT_PROFILE=1` in the actual remote command to emit runtime-prefix and per-module times. Each module time includes its not-yet-initialized import closure. Default output stays quiet. The diagnostic wrapper calls every required initializer unchanged; it does not stub, trim or replace any initializer.

Owned files:

- `dregg-lean-ffi/src/lib.rs`
- `dregg-lean-ffi/src/lean_init.c`
- `dregg-lean-ffi/src/lean_init_st.cpp`
- `dregg-lean-ffi/src/lean_init_internal.h` (new)
- `dregg-lean-ffi/build.rs`
- `dregg-lean-ffi/tests/lean_init_lifecycle.rs` (new)
- `dregg-lean-ffi/tests/native_init_thread.cpp` (new, compiled only with the existing `lean-lib` harness feature)
- `.config/nextest.toml`

Source checks completed: rustfmt parsing, C and C++ syntax against the pinned Lean headers, preserved full initializer sequences, TOML parse and exact new selector inventory. These do not establish a linked or executed green.

## Requested narrow validation

First run the three test-owned coordinator failure/unwind/mode tests and the isolated real narrow-family probe. A suggested nextest selector is:

```
cargo nextest run --profile full --build-jobs 4 --test-threads=1 --no-fail-fast --no-tests fail --no-capture -p dregg-lean-ffi --features lean-lib --lib --test lean_init_lifecycle -E 'test(~init_lifecycle_failed_module) or test(~init_lifecycle_unwind) or test(~init_lifecycle_mode_refusal) or test(~delegated_admission_initializes_only_its_real_lean_module)'
```

The three fresh-process full lifecycle probes have prefix `lean_init_lifecycle_heavy`. They are excluded from default/ci and included in heavy, with an eight-minute per-test ceiling inherited by full. They exercise narrow-first with racing full/native and narrow calls, foreign-thread full-first followed by Rust admission, and ST mode/host-thread exclusion. Every full native probe executes an actual Lean kernel known-answer call. Subprocess isolation is explicit even if invoked under ordinary libtest. The real narrow probe checks all refused conjuncts, integer extremes, multiple host threads, malformed codec output, and that full initialization remains unattempted.

Then retain the existing `lazy_pq_registration` real KAT and rerun exact Hermes with `js-agent` and profiling enabled. The new code does not touch the six lazy PQ registration callbacks.

Accepted Hermes latency remains an explicit obligation: after the small admission predicate it executes a covered accountability turn through the default-on Lean producer, whose `direct_available` requests full initialization. Narrow admission alone does not close the previously measured 191-second accepted-call latency. Use the new per-module timings to select the next source-owned dependency repair; do not turn off producer mode or Lean requirements.

Independent audit confirmed that the foreign native probe allocates Lean closures and constructors, rather than only calling a scalar function. Error injection currently exercises the test-owned initializer backend. Native thread exit exercises owned TLS cleanup, without a direct finalizer-call counter. A poisoned diagnostic preserves the observed runtime mode and readiness alongside its failure.
