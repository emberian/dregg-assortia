# Checkpoint 73 — physical installation handoff and independent fn admission

September 27 local / September 28 UTC, 2026. Continues
[checkpoint 72](checkpoint-72.md). Full shared-platform acceptance remains open.

## Retained live work

Root rechecked r3 recovery USER invocation
`eb28b8d18f7e4a9f8ae0fe3d280dad67`: active, PID3248238. It remains
client_session's exclusive Store writer. The owner reports installed Alice Web
session19, Bob Web21 and Alice API23; Hermes A/B sessions and final readbacks
remain pending. These admissions do not establish physical app execution.

The independent recipient USER invocation
`0bd504d15df045b19a86de2cd75c36eb` was also active, PID3336075.
Mini **c4f1b8c** records event20 registration at count3 and event19 empty-page
progress at count4, exact receipt-only lookups and source-checked fn ACK2.
fn is at frontier3 with zero selected articles. The source r3 Store was not
changed by recipient work. Evidence and the 17 private-artifact hashes are in
Mini `docs/evidence/2026-09-27-fn-gitweb-recipient/`.

## Reviewed integration changes

- Mini **8d7a3f8** connects INSTALL preparation to a retained physical
  materialization request, read-only signed installed-image inspection, and
  source-bound volume-witness adoption. Interrupted pure actions retain
  numbered attempts. Source shell checks and an isolated CLI build passed;
  positive deployed image inspection and actual INSTALL/START remain pending.
  A root inbox hardlink crash-recovery refinement is subsequent WIP.
- **4d73b01** checks agent ticket origin against the source-current parent task
  and generation before planning. Focused shell/schema checks passed; no live
  event22/event27 has been claimed.
- **c4f1b8c** also records unforked Hermes ACP initialization using the exact
  deploy-compatible `launcher/bwrap` path. Its contents match the previously
  qualified private launcher. No model prompt, provider bridge or app tool call
  occurred; workers stopped after the probe.
- Human issuer/entrance WIP now binds the complete accepted package, interface,
  schema and role permissions before native token creation. Independent review
  closed the earlier coarse-ticket-ID gap. Read-only probe recovery is being
  refined before committing that cut.

Build owner reports **cb55b81** shared-provider/shared-lifetime Host qualified:
SHA `89973efe154b3f53bb279a931a93aed0b0a1d341d759dc776dca635dda01c354`,
hbox `/tank/dregg-build/minidregg-cb55b81-host/bin/minidregg-host-cb55b81-r1`.
Source353/353 and reused artifacts10203/10203 matched. The owner is checking
actual provider-list profile/quote behavior and serializing Rust successors;
the new SPK CLI build from8d7a3f8 is queued after them. No shared Host config
has been installed into the live r3 Store service yet.

## Next receiving boundary

Finish existing session recovery and receive an explicit Store-writer handoff.
Then install/start the signed GitWeb package, issue actual separate human and
agent tickets, and connect the separately confined Hermes workers to the same
app and Bonsai service. Distinct runtime roots and provider configurations are
being prepared without starting a second r3 writer. Exercise real shared use,
revocation/disconnect/restart, and selected GitWeb content through fn afterward.

The user's “chonga” means paid OpenRouter models, not a named provider. The
[payment audit](../../research/payment-inference-2026-09-27.md) retains the
$DREGG-only service-credit direction and the existing SQLite atomicity and
uncertain-request gaps. Immediate inference integration remains local Bonsai;
no paid request has been made.
