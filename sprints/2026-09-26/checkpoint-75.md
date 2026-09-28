# Checkpoint 75 — real local model context; installation path correction

September 28 UTC, 2026. Continues [checkpoint 74](checkpoint-74.md).
The integrated shared application journey remains incomplete.

## Actual model, with its upstream requirement

Mini `c2127ac` and correction `2a0321d` retain the local model evidence in
`docs/evidence/2026-09-27-hermes-context-64k/`. Unforked Hermes refuses a custom
provider context below 64,000 tokens. The earlier 7,168-input profile therefore
failed session creation before inference. The real Bonsai server now loads a
65,536-token slot with q4 KV caches and flash attention on hbox, authenticated
and loopback-only at port18081. Root independently observed its active invocation
`1a3be0a0dacb42cf92a826a454d7cbeb`, PID3457733. This is a bounded qualification
unit with a two-hour lifetime, not a permanent public deployment.

Direct chat and streaming tool protocol checks passed. The actual captured
upstream first request, containing 16 built-in tools but no Mini MCP catalog,
returned 8,947 prompt plus23 completion tokens in140.74 seconds. No paid
provider was called. Separate A/B controller candidates use65,024 input and512
output tokens. They remain unstarted; exact app authority, full catalog size,
and appropriate request/worker deadlines still need integration. Candidate
configuration hashes and paths are retained in Mini's
`2026-09-27-multi-provider-host/r3-config-review.md`.

The first model evidence commit captured final status bytes with an earlier
manifest and memory description. `2a0321d` corrects that mismatch explicitly;
root verified every final manifest entry before the correction commit.

## INSTALL boundary and sole writer

The r3 Store remains admitted through count27. mini_app_contract owns the
installation writer. The first cb55 operator invocation
`79bbde60dfff49cb854ce32ab309ac54` ran idle and was stopped after pure
`prepare-install-0001` refused the original Store helper's group-writable
ancestor. The refusal preceded Store replay and INSTALL journal creation.
Original config and binaries are preserved. Root subsequently observed the
operator inactive and volume8401 absent.

Exact original Store/signature helper bytes have been promoted into protected
root-owned executable paths. A narrowly scoped config rebind is being reviewed;
it permits only those two helper path replacements plus the already reviewed
provider services. It must preserve original app receipt equality and the full
Store before any mutation. The next preparation needs a new numbered attempt,
the exact committed scripts, and an explicitly pinned rebound broker config.
No INSTALL/START or app execution is established by this checkpoint.

Subsequent root review committed the shell/jq helper relocation in Mini
`5ac12f0`. Its 11-entry manifest passes. An uncommitted Python config probe
was replaced rather than adopted; its private executed history is retained.
The fresh broker `minidregg-r3-operator-v2.service` is active at invocation
`e7d5f3442d574b588c362bc6ce8111a8`, PID3491541, using rebound config SHA
`64c4d53d5a2b23299f9fb77f2ced70f59f6d33e7d6287cc82995c77ef840f5e5`.
The sole pure preparation is `minidregg-r3-prepare-install-v2.service`,
invocation `670871036976425ca411a8c533b402d0`, PID3492436. Root confirmed it
active with CPU progress during cold replay. Its retained attempt is
`continuations/gitweb-journey/prepare-install-0002` inside r3; the intended
journal is `/var/lib/minidregg/spk/install-ops/gitweb-r3-0002`.
Poll that invocation; do not launch another preparation or Store writer.

## Source corrections and remaining integration

Only the five event22 ticket births are grain-backed and consume tool7902's
three-unit charge. Event27 lifetime grants use ordinary resource-birth
admission and require separately quoted factory funding, not tool reserves.
The earlier seven-times-three budget estimate was wrong. Five tickets consume15
of the retained25 tool units, assuming no intervening consumption. The reserve
wrapper is being restricted accordingly; it must preserve one-send and
read-only recovery across reply loss and interrupted readback.

Mini `c5565d5` now commits that event22-only reserve wrapper, including numbered
readback attempts/logs and a reserve nonce spacing requirement. Root verified
its six-entry manifest; native r3 acceptance remains ahead. Mini `9d84b6e`
commits the budget correction while preserving the historical wrong estimate
as explicitly superseded evidence.

The GitWeb human journey helper is Rust, with a persisted exact commit intent,
one receive-pack, and read-only lookup recovery. Focused check and strict
Clippy passed at source SHA71170393; it still needs an exact release artifact
and native entrance component test before live use. Actual GitWeb is smart
HTTP with separate human Web views. Neither a compiler check nor a remote ref
replaces Mini dispatch receipt reconciliation.

Mini `9d84b6e` also commits that exact Rust helper and source-check evidence.
The builder subsequently reports a qualified release artifact on hbox at
`/tank/dregg-build/minidregg-spk-gitweb-9d84b6e/bin/gitweb-human-journey`, SHA
`bc0e40e87101ab8413eea5e8b0604e4e34acac48d90bfa89b53c919e24f7af18`.
Portable release evidence and the actual native-entrance/Git component probe
are with build_native and shared_resource_tools respectively.

The ordinary-birth optimization `2721253` has a qualified binary recorded in
`98a79e2`. Its private persistent-session differential is now producing exact
receipt and Store comparisons; fallback evidence remains with fn_mini_review.
Do not replace the live cb55 Host during INSTALL from the build result alone.

Independent fn remains ready at ACK2 without a selected article. The full next
journey is unchanged: actual package INSTALL/START, five tickets and two lifetime
grants, separate human and Hermes use of one resident app, then explicit export
of a real selected file through Mini content8001 and fn to recipient600.

Ember's paid-inference intent is linked from HANDOFF to the
[payment audit](../../research/payment-inference-2026-09-27.md): $DREGG service
credits for OpenRouter alongside local inference. This does not establish paid
service accounting or authorize a particular paid test call.
