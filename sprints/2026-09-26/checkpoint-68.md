# Checkpoint 68 — exact retained birth and cold reopen pass privately

September 27, 2026. Continues [checkpoint 67](checkpoint-67.md). The full
[demo journeys](demo-convergence.md) remain incomplete; no live r3 deployment
or real-model acceptance follows from this checkpoint.

Mini **6d34efd** repairs the measured admitted-branch lookup bottleneck.
The pinned Lean 4.30 `Fin.cases` uses induction; nested result selectors spent
CPU evaluating discarded intermediate results. Mini now selects directly by
zero/predecessor. A general dependent-function equality theorem preserves the
original result; the checked theorem uses only `propext` and `Quot.sound`.
Admission checks, order, credentials and exact read guards are unchanged.

The certified **2649 source plus this one repair** built all 351 Lean modules
and native code. ELF SHA-256:
`2c28356f8c59dc5ec4d17c594ed718bca3f73f336790c8eb30bb395557f28bf7`.
This is not the later complete Host source. The binary is on hbox under
`/tank/dregg-build/minidregg-r3-fin-repair-20260927/` and its source/build
artifacts on persvati under
`/home/ember/build/minidregg-2649-fin-repair-20260927/`.

## Actual qualification

The unchanged retained 212,637-byte r3 ordinary-birth request was submitted
once against a private copy of its genesis Store. Result: **confirmed/installed**,
accepted count **1**, **418.68 seconds** wall time. A separate cold process
performed exact-call lookup: **confirmed/replayed**, **241.01 seconds**, with
identical transaction/event/count/image-boundary fields. Root read both typed
outcomes. The physical Store stayed byte-identical across lookup.

The original r3 Store remains untouched and lacks accepted app/ticket/grant
lineage. The private result is not a receipt for that live Store. Creation and
cold recovery are still far too slow for the intended interactive experience.
Instrumented stage timings are not interchangeable with production timing;
no speedup ratio is claimed. All diagnostic/build/run jobs in this lane were
terminal at qualification closeout.

Evidence: Mini `docs/evidence/2026-09-27-ordinary-birth-performance/`.

## Ready artifacts and continuation

Mini **e52995f** preserves exact committed **6d34efd** Linux release builds of
SPK host, grain runtime, provider bridge and Mini CLI, with source and ELF
hashes. All four built from an isolated Git archive without foreign WIP.
Artifacts remain under `/tank/dregg-build/minidregg-6d34efd-rust-closeout/`;
portable manifests/logs are in Mini
`docs/evidence/2026-09-27-rust-artifacts-6d34efd/`. Nothing was installed.

Mini **9e03806** updates the existing same-Store continuation driver to verify
the original attempt's Host separately from the fixed reviewed successor.
It durably records both before later mutation. ShellCheck, syntax and evidence
hash checks passed. No live continuation ran. The driver still needs actual
live submit and exact lookup receipts; private-copy receipts cannot substitute.

Next: qualify a coherent current Host cut with this repair and the committed
resident/controller inspection interface, then resume the original r3 journey
with preserved attempt provenance. Address remaining admission/replay costs
from measured source work; do not silently widen interactive deadlines.
Physical STOP integration, same-app browser/agent use, real-model authorization
and selected Git content publication/independent fn receiving remain required.
Preserve all unrelated working-tree changes. No new broad swarm is authorized
by this checkpoint; Ember requested precise closeout with low remaining usage.
