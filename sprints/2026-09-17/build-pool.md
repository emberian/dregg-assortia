# Dregg sprint build-pool readiness

Measured on 2026-09-17 22:05–22:20 EDT from
`/Users/ember/dev/breadstuffs`. One authorized lane lease was acquired
(`hcargo`, owner `agent:astra-sprint`). No build or WIP sync was started, no
process was killed, and no cleanup was applied. One nominally read-only
minidregg toolchain probe unexpectedly triggered Lake dependency fetching; it
was interrupted and its partial cache is disclosed below.

## Routing verdict

- `persvati`: unavailable. Two BatchMode SSH attempts timed out during TCP
  connection, before authentication. This is a transport failure, not a key or
  authorization failure. The resolved SSH target is the direct LAN address
  `192.168.50.120:22` on `en0` with no ProxyJump/ProxyCommand; a second
  transport diagnostic got 0/2 ICMP replies and an incomplete ARP neighbor.
  The connection never reached an SSH handshake, so no vsauth/credential test
  occurred. Do not schedule a persvati lane until the host answers at layer 2.
- laptop: 12 cores, 96 GiB RAM, 329 GiB free on the data volume. Load was
  25–34 with no cargo/Lean process and no local Cargo profile lock; memory
  pressure reported 93% free and swap was 0.90/2 GiB. It is the only warm
  minidregg host and the deepest breadstuffs Lean host (2,344 Dregg2 oleans),
  but the current non-build load makes it a one-narrow-Lean-job host.
- `hbox`: 24 cores, CPU-idle (load about 2), no exact
  cargo/rustc/lake/lean/leanc/nextest process. It is the only usable remote
  build host tonight. Its health verdict is ALARM: 11–13 GiB MemAvailable,
  5.3/8 GiB swap used, stale sessions, and a drifted installed sweep script.
  The low MemAvailable is primarily a 56–63 GB ZFS ARC (`need=0`, still allowed
  to grow); user build cgroup usage was only 1.32 GB under a 96 GiB cap. The
  stale sessions account for only about 140 MiB and are hygiene, not the memory
  remedy. Earlyoom 1.8.2 acts only when **both** available RAM and free swap fall
  below their 10% floors; swap remained about 35% free. A single four-job Rust
  lane under a 32G cgroup cap has adequate reclaimable headroom, and the repo's
  measured surviving builds stay below roughly 14G.

Hbox storage is correctly routed through `/tank`:

```
/home/hbox/dregg-build -> /tank/dregg-build
/tank/dregg-build: 1.54 / 1.88 TiB used, 331.7 GiB free
/:                 367 / 455 GiB used, 66 GiB free
```

The build root now has roughly 600 directories, largely a newer dclutch fleet.
Use named warm breadstuffs lanes only. Do not seed another breadstuffs lane.

## Warm hbox breadstuffs lanes

All toolchain checks below resolve the repository pins: Rust
`nightly-2026-06-21` (`rustc 1.98.0-nightly`) and Lean/Lake 4.30.0. `cargo deps`
is the number of files in debug/release deps; `Dregg2` is the actual project
olean count, not a PATH probe.

| lane | disk | cargo deps | Dregg2 oleans | native Lean archive | authoritative lease | use |
|---|---:|---:|---:|---|---|---|
| `certify-transcript` | 27G | 1,763 | **2,222** | present; provenance absent, so pbuild must validate/adopt | absent | primary Lean |
| `poa-release-cd5533c` | 12G | 1,775 | 2,112 | present, adopted | absent | spare Lean |
| `eth-lc-air` | 12G | 2,187 | 2,031 | present, release-keyed, exports checked | absent | mixed Lean/Rust or executor gate |
| `green-rust` | 20G | 1,511 | 2,027 | present, adopted | expired, not held | spare mixed lane after reap |
| `games-deploy` | 34G | 2,447 | 1,896 | present, adopted | corpse, not held | integration Rust after reap |
| `privnode` | 14G | 6,132 | 1,063 | present, donor provenance | corpse, not held | spare Rust after reap |
| `hcargo` | 43G | **6,675** | 706 | present, release-keyed, exports checked | **held by `agent:astra-sprint`** | primary Rust |

At 22:18 EDT, the authorized claim succeeded for `hcargo`. It is the only live
holder. The physical lane is `/tank/dregg-build/hcargo`; its mirror is
`/home/hbox/dregg-build/hcargo/.pbuild-lease`, and the authoritative holder set
is `/home/hbox/dregg-build/.leases/hcargo.lease`. The lease anchor is local PID
66314, the long-lived Codex toolserver (`/opt/homebrew/.../bin/codex`, started
15:52 EDT, parent PID 66313 `node /opt/homebrew/bin/codex`), not a transient
probe shell. At 22:23 it was still `live=alive`, `state=held`, one holder, with
the live anchor present in both records. Do not pass
`PBUILD_LEASE_OWNER=agent:astra-sprint` to `hbuild`: its short-lived pbuild PID
must remain a separate holder rather than replacing this durable agent anchor.

## Exact first build recipes

Use one lane first to establish that ARC reclaim and earlyoom behave. If the
health check remains stable, run one Rust lane and one Lean lane concurrently;
keep the combined requested caps at the 96 GiB parent ceiling.

`hcargo` is already claimed. Claim a Lean lane only when Lean work is selected:

```sh
scripts/lane-lease.sh acquire --host hbox --lane certify-transcript --owner agent:<lean-owner>
```

First narrow Lean check, against the touched file only:

```sh
logdir=$(mktemp -d)
SWARM_MEM_MAX=64G LEAN_NUM_THREADS=2 \
  scripts/hbuild certify-transcript \
  'cd metatheory && lake env lean Dregg2/<TouchedModule>.lean' \
  2>&1 | tee "$logdir/lean.log"
grep 'pbuild: VERDICT' "$logdir/lean.log"
```

First narrow Rust check, one crate and one test pattern, with compilation and
test concurrency bounded independently:

```sh
logdir=$(mktemp -d)
SWARM_MEM_MAX=32G DREGG_REQUIRE_LEAN=1 \
  scripts/hbuild hcargo env CARGO_BUILD_JOBS=4 \
  cargo nextest run --test-threads=2 -p <crate> -E 'test(/<name>/)' \
  2>&1 | tee "$logdir/rust.log"
grep 'pbuild: VERDICT' "$logdir/rust.log"
```

The current WIP needs three package-scoped checks. Run them serially on the one
leased lane; every command has an explicit `-p`, target kind, required feature,
and `--no-tests fail` so a stale name cannot silently report green. Four build
jobs bound compilation. One test process at a time avoids overlapping
SpiderMonkey heaps while hbox is reclaiming ARC.

First, the Hermes cross-process bridge weld. The named test is inside the
`world_bridge_e2e` integration target and is compiled only with `js-agent`:

```sh
logdir=$(mktemp -d)
SWARM_MEM_MAX=32G DREGG_REQUIRE_LEAN=1 \
  scripts/hbuild hcargo cargo nextest run \
  --build-jobs 4 --test-threads=1 --no-tests fail \
  -p deos-hermes --features js-agent --test world_bridge_e2e \
  -E 'test(~run_js_over_the_world_bridge_lands_on_the_served_world)' \
  2>&1 | tee "$logdir/hermes-world-bridge.log"
grep 'pbuild: VERDICT' "$logdir/hermes-world-bridge.log"
```

Second, the starbridge library weld plus every currently changed durable-write
failure tooth. `agent-js` is load-bearing: `agent_attach` is absent under the
default `embedded-executor` feature, and one durable failure test is itself
`#[cfg(feature = "agent-js")]`.

```sh
logdir=$(mktemp -d)
SWARM_MEM_MAX=32G DREGG_REQUIRE_LEAN=1 \
  scripts/hbuild hcargo cargo nextest run \
  --build-jobs 4 --test-threads=1 --no-tests fail \
  -p starbridge-v2 --features agent-js --lib \
  -E 'test(~agent_run_js_drives_the_live_cockpit_world) \
      or test(~durable_write_failure_fully_unwinds_the_commit) \
      or test(~durable_write_failure_after_commit_requires_reopen_to_discover_the_result) \
      or test(~durable_write_failure_is_refused_through_the_attached_world_sink) \
      or test(~durable_write_failure_unwinds_a_cell_creation) \
      or test(~durable_write_failure_unwinds_a_cell_removal)' \
  2>&1 | tee "$logdir/starbridge-agent-durable.log"
grep 'pbuild: VERDICT' "$logdir/starbridge-agent-durable.log"
```

Third, the persist transaction/reopen tooth:

```sh
logdir=$(mktemp -d)
SWARM_MEM_MAX=32G DREGG_REQUIRE_LEAN=1 \
  scripts/hbuild hcargo cargo nextest run \
  --build-jobs 4 --test-threads=1 --no-tests fail \
  -p dregg-persist --lib \
  -E 'test(~config_batch_rollback_and_reopen_keep_related_keys_atomic)' \
  2>&1 | tee "$logdir/persist-config-batch.log"
grep 'pbuild: VERDICT' "$logdir/persist-config-batch.log"
```

The GUI signature migration needs the real cockpit feature cone. A default
starbridge build does not compile gpui, the dock, or the cockpit surfaces. Its
first package-scoped compile gate, when that migration is ready, is:

```sh
logdir=$(mktemp -d)
SWARM_MEM_MAX=32G DREGG_REQUIRE_LEAN=1 \
  scripts/hbuild hcargo env CARGO_BUILD_JOBS=4 \
  cargo check -p starbridge-v2 --features desktop --bin starbridge-v2 \
  2>&1 | tee "$logdir/starbridge-desktop-check.log"
grep 'pbuild: VERDICT' "$logdir/starbridge-desktop-check.log"
```

For the later installer-grade compile-only gate, use the same named feature and
package while compiling every starbridge target:

```sh
SWARM_MEM_MAX=32G DREGG_REQUIRE_LEAN=1 \
  scripts/hbuild hcargo cargo nextest run --no-run \
  --build-jobs 4 -p starbridge-v2 --features desktop --all-targets
```

None of these commands has been run or synced. `hcargo` already holds dep-info
for the selected starbridge/deos targets, debug and release mozjs caches, and
the broad root dependency cache; final test executables were swept, so a
bounded relink/rebuild is expected.

The pipe is outside the remote command, so pbuild grades the build rather than
`tee`. `PASS`/`FAIL` are results. `REFUSED`, `ENVFAULT`, and current pbuild's
`INCOMPLETE` are not results. Do not use `DREGG_REQUIRE_LEAN=0` or
`DREGG_ALLOW_UNAUDITED_PQ=1` to make a verified-core test run.

For an on-demand heavy suite, use release and a package filterset; do not pass
`-p` through `test-gauntlet.sh`, because the nextest profiles validate names
outside that package:

```sh
SWARM_MEM_MAX=64G DREGG_REQUIRE_LEAN=1 \
  scripts/hbuild hcargo env CARGO_BUILD_JOBS=8 \
  scripts/test-gauntlet.sh heavy-release -E 'package(<crate>)'
```

Release each claim when its owner is done:

```sh
scripts/lane-lease.sh release --host hbox --lane certify-transcript --owner agent:<lean-owner>
scripts/lane-lease.sh release --host hbox --lane hcargo --owner agent:astra-sprint
```

## Minidregg

The warm installation is local at `/Users/ember/dev/minidregg`:

- Lean 4.30.0; 600 project oleans across `Theory`, `Kernel`, `Pred`, `Effects`,
  `Compiler`, `Selvage`, and `Assurance`.
- `.lake/packages/mathlib` is a symlink to breadstuffs' pinned mathlib and sees
  8,105 mathlib oleans.
- Rust is pinned to `nightly-2026-06-21`; `prover/target` is 2.6G with about
  40,946 dep files; no Cargo profile lock was held.
- The repository instructions require single-file iteration and reserve
  `lake build Minidregg` for the integration gate, never mid-swarm.

Safe narrow commands:

```sh
cd /Users/ember/dev/minidregg
LEAN_NUM_THREADS=2 lake env lean Selvage/<TouchedFile>.lean
scripts/check-import-boundary.sh

cd /Users/ember/dev/minidregg/prover
CARGO_BUILD_JOBS=4 cargo nextest run --test <test-binary>
```

Hbox's `/home/hbox/dev/minidregg` was cold: no `.lake`, no project oleans, and
its 288M `prover/target` had zero deps in the normal debug/release dirs. A
toolchain probe unexpectedly invoked Lake dependency resolution and started
cloning mathlib. It was interrupted immediately, but left a 667M partial
`.lake/packages` (611M mathlib plus dependency clones). It remains untouched.
Do not treat it as warm or build in it. The durable fix is a project-aware
remote wrapper rooted at `/tank/minidregg-build/<lane>` with the same lease,
wrapper, disk-floor, verdict, and cache semantics as pbuild/hbuild; current
pbuild is hardwired to sync breadstuffs and cannot safely serve minidregg.

## Stale hbox session inventory

`box-health.sh` found 32 build-shaped processes and 10 watcher-shaped processes
older than one day. The safe subset below is structurally narrow: each systemd
session is already `State=closing`, contains only one orphan bash plus one
`sleep` (session 71192 has only bash), and the bash is an immortal self-match
loop using `pgrep -f`. Every listed root PID has PPID 1.

| session | root PID | age | root RSS KiB |
|---:|---:|---:|---:|
| 100878 | 1269578 | 13d04h | 2988 |
| 41819 | 1286163 | 53d05h | 3224 |
| 41830 | 1301780 | 53d05h | 3100 |
| 41835 | 1302717 | 53d05h | 2988 |
| 41841 | 1304147 | 53d05h | 3164 |
| 41845 | 1304747 | 53d04h | 4036 |
| 68141 | 2173395 | 43d08h | 2924 |
| 68255 | 2199046 | 43d07h | 3828 |
| 69307 | 2778728 | 42d18h | 4180 |
| 69839 | 3601607 | 42d13h | 2916 |
| 69888 | 3628863 | 42d13h | 3208 |
| 70282 | 3926391 | 42d03h | 3620 |
| 70541 | 4018088 | 42d00h | 3344 |
| 71192 | 907648 | 40d19h | 2648 |
| 71735 | 1211465 | 40d17h | 3204 |
| 71797 | 1247230 | 40d17h | 2852 |
| 71814 | 1324746 | 40d16h | 3176 |
| 71830 | 1455892 | 40d16h | 2908 |
| 71858 | 1467225 | 40d16h | 3144 |
| 71886 | 1477667 | 40d16h | 3616 |
| 71914 | 1486878 | 40d16h | 3332 |
| 71925 | 1494055 | 40d15h | 2888 |
| 71941 | 1635812 | 40d15h | 3508 |
| 84880 | 240027 | 30d21h | 3680 |
| 89276 | 947269 | 21d22h | 3124 |
| 95595 | 3407593 | 18d00h | 3300 |
| 95600 | 3408410 | 18d00h | 3424 |

Systemd-logind is the supported owner of these session scopes, and this host's
`loginctl` supports multi-session termination. Do **not** terminate them for
this sprint: together they account for only about 140 MiB and therefore do not
solve the memory alarm. The exact bounded command is retained here only as the
supported future hygiene operation, after a fresh ownership snapshot:

```sh
ssh hbox 'loginctl terminate-session \
  100878 41819 41830 41835 41841 41845 68141 68255 69307 69839 69888 \
  70282 70541 71192 71735 71797 71814 71830 71858 71886 71914 71925 \
  71941 84880 89276 95595 95600'
```

Do not include sessions `122196`, `130357`, `132850`, or `94075`: they contain
Python/dclutch/controller work, and session 130357 has a live
`solana-test-validator` consuming CPU. Their intent is not safely inferable from
age. No repository process-reaper exists; `sweep-build-lanes.sh` cleans artifact
generations, not processes.

Related breadstuffs lane leases are absent except `poa-arcade` and
`poa-nightwatch`, whose records are stale/orphaned with zero holders. Leave the
sessions alone for now and use only read-only health/lease reports:

```sh
scripts/box-health.sh --host hbox --no-lanes
scripts/lane-lease.sh reap-orphaned --host hbox --dry-run
scripts/sweep-build-lanes.sh --host hbox                 # report only
```

The installed hbox `~/bin/sweep-build-lanes.sh` is byte-drifted from this
checkout, so do not trust the scheduled sweep until the copy is refreshed. The
local checkout's `scripts/sweep-build-lanes.sh --host hbox` is the current code
and is safe in report-only mode. Applying a reap, refreshing the installed copy,
terminating sessions, or passing `--apply` was deliberately left for the main
operator.
