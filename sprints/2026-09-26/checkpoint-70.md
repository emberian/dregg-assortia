# Checkpoint 70 — workroom recovered; integrated app admission continues

September 27, 2026. This supersedes checkpoint 69's pending workroom recovery.
The full SPK platform objective remains active; no combined deployed preview
is established by these component and live workroom results.

Mini **6d9980f** adds the reviewed append-only recovery from the retained jq
metadata failure. The first signed query was re-inspected and reused; the
remaining workroom queries and six parent delegations ran successfully in the
original retained r3 Store. Evidence committed at **e47f504** lives in
`docs/evidence/2026-09-27-r3-workroom-recovery/`: eight born views, signed birth
evidence SHA `71604759803d1e97915310314cf15b50ad6afc0f1b6947d32feaee07805c69ad`,
completion marker, archive/manifests, and bounded keyless results.
The successful USER unit invocation was `3637e759f4284bb98c58c76f49316c99`;
its journal recorded 3m40.700s CPU and 1.8 GiB peak. Original failed actions
remain retained. Store after these accepted delegations:
`449278317fac429751ee208b39f5d6b97328c3fa84bf4fbcf6f1a962bb4bf5a9`.

The separately launched app/handoff USER invocation
`a2edf13df50a4e43a499fde91e613ead` then terminated with status 1. Its first
app tool reservation received an explicit admission refusal, before app birth
was authored/submitted. Signed pre-read showed tool7902 at generation0/status0,
remaining50/reserved0; Store stayed at the hash above. Source transition law
allows reserve from running status1/2, while attach moves detached status0 to
running and increments generation. Owner client_session is implementing an
explicit signed attach and fresh reserve recovery, preserving the refused
nonce43000 attempt and auditing downstream generation assumptions. Do not clear
phase markers or blindly re-run the driver. No INSTALL or START has occurred.

Mini **eca6906** closes the operator parser gap for mixed human/v3-agent resident
routes. Focused Linux tests passed 5/5 plus strict Clippy; shell/schema evidence
is in `docs/evidence/2026-09-27-spk-resident-mixed-route/`. This does not create
accepted ticket/grant lineage. **d48aa81** adds read-only accepted event27
inspection, including source-owned grant digest, verifier-selected initialized
root, exact receipts and original event22 descriptor bytes. The new CLI is
`HOST CONFIG inspect-accepted-agent-lifetime-grant INGRESS.bin OUTPUT.json`.
Narrow Lean checks passed in an isolated coherent9cd closure; native successor
qualification and actual accepted-grant invocation are pending. Owner
agent_api_host is joining this projection to protected controller/resident
custody rather than inventing fixture values.

## Parallel integration, still in progress

- build_native is qualifying local Ternary Bonsai 2 27B on hbox's AMD RX6750XT,
  using pinned official PTQ1/Vulkan artifacts under /tank. It reports successful
  private local chat, structured tools and SSE with usage. Retained public
  qualification evidence and actual unforked Hermes through Mini remain to be
  joined; this is not the complete model/grain journey.
- runtime_review implemented GitWeb read/edit/commit/push tools through the
  existing per-request Mini dispatch/settlement path. Component tests passed,
  but independent review is closing loopback authentication/read-mode mutation
  and hidden MCP tool exposure before root adopts the batch.
- mini_app_contract owns the physical STOP service and exact Fenced/Stopped
  recovery; root registered its CLI pending the service's checked implementation.
- fn_mini_review and fn_contracts own chosen Git commit/file → Mini atom → fn
  publication → independent recipient → frontier/ACK/readback. Review found
  concrete lost-reply/finalize, latest-lookup and exact-target/AtomId gaps; those
  remain implementation work. No script-only pass proves native publication.
- linux_hosting is preparing a fresh isolated qualified format8 fn node on
  hbox under `/tank/dregg-preview/fn-gitweb-r3-20260927`. Existing protected fn
  nodes and Claude's active development checkout are outside that write scope.

Ember selected local Bonsai for the preview and additionally clarified the
paid offering: users buy credits with **$DREGG** to use **OpenRouter models**,
alongside homelab inference. “Chonga” was informal language, not a provider or
product. See [the source audit](../../research/payment-inference-2026-09-27.md)
and [intent](../../intent.md). Existing payment/provider code is relevant, but
transactional crediting and durable paid-request integration remain work; no
paid call or unspecified account spend has been performed.
