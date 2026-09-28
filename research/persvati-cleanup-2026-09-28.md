# Persvati build-cache cleanup — 2026-09-28

Ember requested removal of accumulated Mini build directories. Cleanup removed
866 inactive `.lake/build/lib` and `.lake/build/ir` directories beneath
`/home/ember/build/minidregg-*`, including dependency compilation caches.
Sources, dependency source checkouts, evidence, logs, native binaries, and
runtime Stores were not selected for removal. No services were stopped.

Measured results:

| Measure | Before | After |
|---|---:|---:|
| `/home/ember/build` | 464 GiB | 94 GiB |
| Old `minidregg-overnight-20260926` tree | 205 GiB | 27 GiB |
| Filesystem available space | 83,886,657,536 bytes | 481,289,908,224 bytes |
| Filesystem utilization | 96% | 75% |

Two warm trees were explicitly excluded:

- `/home/ember/build/minidregg-2721253-native-20260927`
- `/home/ember/build/minidregg-event28-diagnostic-next-20260927`

Reuse these for future qualified builds after checking source and ownership.
Older snapshots retain sources and artifacts but no longer have warm compiled
libraries. Do not interpret a cache miss as a source regression.

Before deletion, no compiler processes or pbuild lease records were found in
the inspected build scope; all open paths were captured through root `lsof`.
The plan and apply passes refused any selected cache with an open path.
Four live binaries under the build root had identical SHA-256 hashes after
cleanup, and the three identified native Host PIDs remained present.

The on-machine audit is `/home/ember/build-cleanup-20260928/`: exact candidate
and removal lists, cache sizes, open paths, before/after filesystem readings,
and `live-binaries.sha256`. Removal-list SHA-256:
`66933bc83451724d53627d1fef1c0f0dcdc8a49d966e2108d822d3e6f0772406`.
This was build-cache maintenance, not a deployment or functional test.
