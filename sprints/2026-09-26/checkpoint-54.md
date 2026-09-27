# Checkpoint 54 — native package qualification and fresh physical authority

September 27, 2026. Continues [checkpoint 53](checkpoint-53.md). The full [platform goal](spk-platform-cycle.md) remains active; this is not a deployed-service announcement.

Reviewed and pushed Mini commits:

- **1cad3e9:** real signed GitWeb passes offline native v2 qualification through the signature-verifying Rust SPK reader and source-qualified Mini Host. Exact ordered create/continue commands and descriptor hashes agree. The first attempt's file-mode refusal and successful protected-copy retry are retained. No Store or app was created by this gate.
- **4db02ad:** physical launch handoff requires the actual CAS winner, not merely exact readback. The old ordinary result classification stays compatible. Lean receiver/probe checks pass; a separate actual pinned SQLite concurrent test returned one Installed and one AlreadyPresent for identical expected/proposed bytes.
- **fdcb74d:** private source-bound INSTALL/create/continue BEGIN and claim authoring, fresh lifecycle submission and receipt-only historical recovery reach Host/Main. Main and lower receiver both prevent an already-present or recovered claim from producing another launch frame. Six scoped Host checks and the focused private-broker test pass. A newly linked current Host is still required.
- **20998dd:** event26 replay joins the original event22 ticket, event27 grant and v3 reserve through one verified history, preserving the initialized grant write's exact root. Replay, NativeHost and Session direct checks pass. Runtime projection/receiver and current-generation controller integration remain separate work.

Portable evidence is in Mini docs/evidence/2026-09-27-spk-launch-offline-native/, lifecycle-claim-fresh-cas/, lifecycle-launch-v3-host/, and agent-lifetime-dispatch-replay/ (each directory has the full date prefix).

The corrected event22 r2 unit is running on its own fresh Store: mini-event22-r2-client-session.service, invocation5167adaea3c74d7e9f7d2d7715ffa18b, observed PID3594014. The old failed r1 Store is preserved. Independently, prepare.sh created the protected integrated fixture at /var/lib/minidregg/spk/fixtures/gitweb-v2-20260927-client-session-r1; run-base.sh is queued after the separate event22 run to bound CPU. No combined A/B Store is yet claimed.

Next convergence: finish completion op70/71 and committed-claim inspection; wire the real Rust INSTALL/create/continue consumer; finish lifetime dispatch authoring/Host/controller consumers; build one source-qualified combined Host; run the shared browser/API/direct-CLI journey with hosted unforked Hermes. The final model call requires a staged real provider credential; current recorded Hermes evidence uses a deterministic local fixture. Selected fn transport and actual latency measurement remain required. No transport receipt establishes installation authority.
