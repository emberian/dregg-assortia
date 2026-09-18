# Existing Hermes world-bridge artifact: bounded runtime diagnosis

Measured on hbox `hcargo`, 2026-09-17 23:32–23:40 EDT. No rsync, Cargo,
nextest, source/config/profile edit, or rebuild occurred. Every test-binary
execution ran inside `SWARM_MEM_MAX=32G swarm-build` with a remote GNU
`timeout` no greater than 720 seconds.

## Artifact identity

```
path=/tank/dregg-build/hcargo/target/debug/deps/world_bridge_e2e-1502cea5aad1e55d
size=666409352
mtime=2026-09-17 23:13:36.589649582 -0400
sha256=aaf5238252368496893417abbfb7325648be43b4a9ef1af8a70c575b3a07bd0f
ELF BuildID=7f269e1649f1ab7f9983bd31f12e21ba92dbb79d
```

The lane's synced `deos-hermes/tests/world_bridge_e2e.rs` hashes to
`6e5f391eab2c6e65d986aeb30cb9a6eecb94f2bdbaa71349f1b02de0ab42f732`.
The attempt-2 source manifest is `/tmp/dregg-hermes-attempt2-source.json`; it
does not list this unchanged test file. This artifact is runtime evidence for
that attempt-2 snapshot only. It does not validate the current marker-enabled
SDK/World source.

## Exact execution and outcome

Listing the existing binary under a 32G swarm scope took 0.057 seconds and
found the expected three tests. It did not initialize the expensive runtime.

The untraced exact run was:

```sh
SWARM_MEM_MAX=32G swarm-build \
  timeout --signal=TERM --kill-after=15s 720s \
  /tank/dregg-build/hcargo/target/debug/deps/world_bridge_e2e-1502cea5aad1e55d \
  js_agent_weld::run_js_over_the_world_bridge_lands_on_the_served_world \
  --exact --nocapture
```

The diagnostic harness used `stdbuf` around that exact command and sampled
only its PID/threads. Outcome: **PASS**, libtest 192.99 seconds, outer wall
193.893 seconds, exit 0. At 1, 5, 15, 30, 60, 120, and 180 seconds one test
thread consumed about 100% of one CPU; the harness threads waited on futex,
and the bridge socket did not exist. Sampled RSS rose from 110,728 KiB to
221,332 KiB with zero swap.

One final sparse timestamp run used the same exact test and limits, with
`strace -ff -ttt -T -e trace=%process,%network` as its parent. It also
**PASSED**: libtest 191.90 seconds, outer wall 191.993 seconds, exit 0.

## Measured phases

Times below are relative to the traced binary's `execve` at
`1789702594.526682`. These are syscall timestamps, not log guesses.

| event | elapsed | implication |
|---|---:|---|
| libtest creates the named test thread | 0.020792s | ordinary process/test startup is tiny |
| test creates its explicit 64 MiB `run_js_bridge_body` thread | 0.023330s | test body entered |
| long CPU phase ends; the next helper-thread group begins | 191.844128s | 191.820798s passed with no process/network syscall from the body thread |
| first world-bridge `connect`, intentionally absent, returns `ENOENT` | 191.852449s | host/runtime initialization is complete; fail-closed check reached |
| served-world thread is created | 191.860285s | only now can `DreggEngine::new` and serving begin |
| server binds/listens | 191.861667s | server construction plus already-once Lean-core install took at most 1.382ms |
| client connects successfully | 191.870516s | no accept/connect stall; 8.849ms after bind |
| first protocol frame is sent | 191.881416s | JS evaluation/crawl reached the wire 10.900ms later |
| test-body thread exits successfully | 191.919733s | full connected bridge/assertion phase was 49.217ms from connect, 58.066ms from bind |
| process exits 0 | 191.927343s | complete traced execution |

The first-network marker accounts for essentially the whole runtime:
191.852449 of 191.927343 seconds (99.961%). There is no socket stall. The
long interval precedes even the expected absent-socket connect and precedes
creation of the served-world thread.

Source order explains what is inside that interval:

1. `run_js_bridge_body` constructs `AgentRuntime::new` before
   `McpToolHost::with_run_js`.
2. `AgentRuntime::new` calls `install_verified_pq_cores`.
3. Its first real-core availability probe calls `lean_init_once`, so native
   Lean runtime/module initialization happens here.
4. Only afterward does `with_run_js` call `JsRuntime::new`, followed by the
   fail-closed bridge call.

The trace cannot put a source-level marker inside that CPU-only interval, but
it bounds the Lean-bearing pre-network initialization phase at 191.821 seconds.
The helper-thread group appears at its end, then the JS/fail-closed path reaches
the first `connect` 8.321ms later. A marker-enabled rebuild can split the final
few milliseconds precisely; it will not turn the 180-second nextest timeout
into a code failure. The default timeout terminated the green artifact about
11.85 seconds before its first network call and about 12.99 seconds before the
untraced pass.

## Inspection limits

`/proc/<pid>/stack` was permission-denied. A brief gdb attach to only the exact
child was refused by hbox's Yama `ptrace_scope=1`; perf was refused by
`perf_event_paranoid=4`. No privilege escalation or host-policy change was
attempted. Thread CPU/wchan, file descriptors, socket presence, and the sparse
parent strace supplied the phase evidence instead.

## Logs

Local copies:

- `/tmp/dregg-hermes-direct-exact-aaf52382.log`
- `/tmp/dregg-hermes-direct-exact-aaf52382.diag`
- `/tmp/dregg-hermes-strace-exact-aaf52382.log`
- `/tmp/hbox-hermes-aaf52382-traces/` (per-thread raw strace files)

The same run/diagnostic/trace files remain under `/tmp` on hbox.
