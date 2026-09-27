# Checkpoint 69 — live workroom birth accepted; coherent Host built

September 27, 2026. Supersedes the live-state boundary in
[checkpoint 68](checkpoint-68.md): the original retained **r3 Store now has
accepted count 1**. The platform and [complete journeys](demo-convergence.md)
remain unfinished.

Mini **2ad9735** preserves the live result and raw evidence in
`docs/evidence/2026-09-27-r3-live-birth/`. After a fresh exact-call lookup returned
absent with unchanged genesis, the successor Host submitted the original call
once. Result: confirmed/installed in **344.57 seconds**. A separate cold lookup
returned confirmed/replayed in **110.53 seconds**, with identical four receipt
fields and unchanged Store. Physical Store SHA:
`e5515e158fdfb03afdafc3951a3a73c2b779bac37eb8428a146c8244611e30e5`.
These are hbox **user-manager** systemd units; querying the system manager does
not observe them. Both invocations are terminal. No second submit occurred.

The protected action is
`/var/lib/minidregg/spk/fixtures/gitweb-v2-20260927-client-session-r3/continuations/first-birth-retry-0002`.
Mini **62bbb98** provides exact append-only receipt adoption. Adoption passed:
original attempt now has new `retry-0002.{bin,json}` installed and
`retry-0003.{bin,json}` replayed, with durable provenance. Original call/config,
attempt metadata and historical absent retry remain unchanged; no original
`outcome.json` was invented. Two action metadata files required mode-only
tightening to 0600; hashes were unchanged.

Mini **a93343e** qualifies the coherent **9cd8c93** Host: 353/353 Lean modules,
native link and artifact checks pass. It combines the finite-lookup repair with
the resident inspection fields. hbox staged binary:
`/tank/dregg-build/minidregg-9cd8c93-host/bin/minidregg-host-9cd8c93-r1`,
SHA `0728c9161e6a60bbbc257eb6e41bd505683358027c94c221776b8de13a558ce9`.
Evidence: Mini `docs/evidence/2026-09-27-native-host-9cd8c93/`.
No integrated runtime test of this newer binary is claimed. Rust artifact pins
remain in checkpoint 68. Build jobs are terminal.

## Immediate continuation boundary

The reviewed retained base continuation has not completed. Its first preflight
refused a group-writable original runner; a byte-identical protected copy fixed
that. The next attempt created `base-resume-0001/workroom.started`, then failed
before any native operation because its Unix socket pathname exceeded SUN_LEN.
No `workroom.completed` or app attempt exists; Store stays at the accepted hash
above and the failed unit has no remaining Mini/Host child.

Owner `client_session` is repairing the generated launcher to use a short
private runtime socket, preserving persistent journals under r3. Root requested
an explicit reviewed recovery action retaining old scripts/hashes/phase markers
and stderr, with proof of pre-native failure before running the same workroom
body once. Do not clear the started marker or blindly rerun the driver. Scope
is base through application handoff only, before INSTALL/START. No recovery
execution is established by this checkpoint; inspect current lane evidence.

Remaining obligations include practical latency, app installation/start and
same-resource human/agent use, physical STOP/recovery, authorized real-model
Hermes, selected content publication and independent fn receiving. No preview
service or complete demo is established.
