# DREGG-native nexus: bounded Solana utility orientation — 2026-09-17

Scope: read-only inspection of `breadstuffs`, `dregg-infra`, `DreggCloud`,
`DreggNet`, and the narrow portal pointer to `joshi`. No RPC, wallet, build,
test, deployment, or dClutch investigation was performed. Source is separated
below from retained execution evidence.

## Decision-relevant result

There are three composable seams, but none is presently a complete public
provider/stake market:

1. **Proposed: holder-gated access is the nearest composable first utility.** It can grant a
   wallet holder a short-lived, replay-protected DREGG-native *access
   capability* for a House, local-first workroom, Hermes session, or a
   self-hosted node's resource offer. It observes a balance; it does not lock,
   spend, settle, or prove execution.
2. **Proposed: a provider bond can use the Solana escrow program only
   after a Token-2022 cutover and deployment.** Its current two-terminal-state
   escrow offers a candidate release/refund shape, but it cannot custody the
   mint pinned by the current holder-gate configuration today.
3. **Proposed: metered resource payment can use the existing DREGG cell/lease rails,
   with a Solana lock/mirror as the funding boundary.** The dregg-side payment
   and resource records exist separately; source documentation reports a dated
   devnet oracle-attested exercise. They are not yet a deployed, trustless,
   configured-mint provider settlement path.

This aligns with self-hosting: a House/node may validate membership and record
resource/service evidence locally, while a remote provider must not be treated
as eligible, bonded, paid, or correct merely because a wallet passed an
admission check.

## Current exact Solana-facing effects

| Path | Configured subject / receiver | What it actually effects | What it does **not** establish |
|---|---|---|---|
| PoA holder admission | Mint `XkeTXo1125vz5H9svJpGiw4JvLbN8VmMu9cmMvspump` and Token-2022 program `TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb` pinned by the current mainnet holder-gate configuration; node holding API | Wallet signs an exact challenge; server source fetches finalized token accounts, decodes them, and persists/issues a short-lived `BetaRpcAttested` capability bound to player, federation, origin, mint and slot. | No inspected chain artifact establishes a current balance, token-program ownership, or issued capability. The code path has no token movement, escrow, governance weight, provider registration, payment, proof anchoring, or remote-execution correctness. The node API source implements the beta RPC route, not the consensus-feed upgrade. |
| Consensus proof of holdings | Same policy; consumer is `dregg-governance::grant_weight` / weighted ballot engine | A `ConsensusVerified` holding, if supplied by the anchored feed, can become a Lean-decided weight grant after wallet-owner binding and snapshot/nullifier checks. | No observed live feed/provider deployment was established by this bounded trace; a plain RPC holding is explicitly refused for weight. This is proof anchoring/verification of a snapshot, never a transfer or lock. |
| Holder portal | `dregg_gate` roster made on hbox, consumed by `dregg_portal` on the anchor | The deployment README reports a portal that grants read access from a pushed holder roster and deliberately makes no chain request at the public edge. | No current live portal/roster evidence was inspected. If operated as described, it is an access gate: the roster is an off-chain decision/snapshot, not a Solana program mutation, an escrow, or a settlement receipt. Product source/state is in the separate `joshi`/host deployment, not this repo. |
| Lock/mirror + escrow program | Mint is chosen when its vault config is initialized; current program requires legacy `spl_token::id()` | Program source has SPL transfers into a pooled vault or a per-escrow PDA; escrow has exactly-one terminal `Released` or `Refunded` state, and release requires threshold ed25519 attestations. A lock record is designed for a DREGG relayer/mirror credit. | It cannot lock the mint pinned by the current holder-gate configuration: that configuration specifies Token-2022 while every custody path requires the legacy token program. No deployed program/configuration for that mint was found in this bounded inspection. Token-2022 support alone would not establish safe provider-bond authority, verdict binding, or release policy. A lock is neither a provider verdict nor a correctness proof. |
| Resource/platform evidence | DreggCloud service cell + signed House archive; dreggnet-compute job cell; DreggNet Payable rail | Service cells commit capacity/meter state and output/receipt fields; the House archive preserves signed work/lease/escrow/settlement evidence. Compute Exchange records a requester/worker/budget lifecycle. DreggNet's Payable seam specifies one conserving DREGG-cell transfer per lease period. | DreggCloud expressly marks independent provider and economic slashing unavailable. Compute's result is only nonempty text and its budget fields are not wallet transfers. The DreggNet source is a native cell asset rail, not an adapter from a Solana mint/lock. |

### Mint/network answer

The only inspected holder-gate configuration targets **Solana mainnet-beta**
and pins the public mint above. `GateConfig::path_of_angels_mainnet` pins the
genesis hash, origin/domain, mint and Token-2022 program; its minimum is one raw unit.
The devnet bridge harness deliberately mints a **stand-in legacy SPL token**,
not real `$DREGG`. No private endpoint or credential is reproduced here.

## Proposal 1 — holder-sponsored resource access

**Product effect.** A member signs their wallet challenge to sponsor their
DREGG identity, then receives an expiring capability to join a House, open a
Hermes-backed resource session, request a bounded service cell, or enter a
local-first workroom. A self-hosted House can retain the resulting receipt and
enforce its own capacity/quota policy without custody of the holder's wallet.

**Existing composition.** The node API does the challenge, exact wallet
signature, finalized RPC account retrieval and durable capability issuance.
`poa-solana-gate` already prevents a beta RPC capability from carrying
governance weight. DreggCloud provides the resource-side primitive: a cap-gated
verifier service with committed prepaid meter state, and its operated adapter
retains signed evidence across restart. The portal demonstrates a less-native
holder-access surface reported by its deployment README to use an hbox-pushed roster.

**Required seam.** Define a bounded `HoldingCapability -> House/Hermes/resource
grant` verifier that consumes the receipt once or links its expiry/nullifier to
the local member/session capability. No such downstream consumer appeared in
the `poa-solana-gate` call-site search. For a production-grade holding claim,
wire `HoldingFeedSource`/snapshot evidence and a governance-pinned weak
subjectivity anchor into the node route; today `verify_consensus_source` is a
library entry, while the delivered HTTP route issues `BetaRpcAttested` evidence.

**Self-hosting impact.** Strong fit: each owner can choose whether a holding is
an invite criterion or a limited allocation criterion, while keeping actual
resource authority in native capabilities. It does not impose a hosted provider
or a common custody pool. It should never qualify a host as a paid/bonded
provider.

## Proposal 2 — provider bond with real custody; devnet verdict ledger

**Product effect.** A provider publishes a signed resource offer and locks the
user-selected real `$DREGG` amount into a per-provider/per-offer bond. A separate
verifier emits one of three distinct outcomes: timeout/noncompletion,
incorrect-result, or custody fault. Under the stated devnet rule, the outcome
writes only a signed, append-only reputation/leaderboard event and does not
seize funds. The distinct outcome classes keep a timeout from being silently
treated as an incorrect-result or custody verdict.

**Existing composition.** `solana-lock` already has per-escrow PDAs, captured
refund destinations, deadline refunds, exact terminal status, and M-of-N
ed25519-authorized release. `node/src/relay_dispute.rs` (covered in the
provider orientation) separately constructs a dregg `SlashPlan`; DreggCloud
already distinguishes refund/release and calls an economic slash loop
unavailable. These are useful inputs, not a connected path.

**Blocking implementation gaps.**

* The lock program uses `spl-token` v6 and rejects every token program except
  `spl_token::id()`; the current holder-gate configuration pins Token-2022.
  Token-2022 account/transfer support and extension-safe validation are a
  necessary compatibility change, not sufficient provider-bond safety.
* Establish a compatible deployed program and vault for the selected mint. The June 28
  devnet note reports that no lock program was deployed for that exercise; this
  inspection did not establish a current deployment for the configured real mint.
* Bind provider identity, offered resource, asset/amount/floor, expiry,
  recipient, and the exact admissible verdict to the escrow ID. Add the
  provider registry/eligibility and an independent verifier path. Neither the
  current DreggNet configured-provider control plane nor DreggCloud creates
  this market.
* Implement the devnet reputation ledger as a non-monetary receiver of a
  verified verdict. Do not reuse the custody-release instruction for it.

**Self-hosting impact.** It permits a homelab operator to stake against a
specific offer without handing the machine or account control to a central
host. It does require them to accept a published, bounded verifier and bond
terms; a self-hosted resource that declines them can still participate as an
unbonded friend/community service.

## Proposal 3 — escrowed resource payment via DREGG-native cell settlement

**Product effect.** A renter funds a DREGG-cell execution/service lease; a
provider's cell receives a conserving payment only when the native service
agreement reaches its release condition. A Solana lock/mirror can fund that
cell value at the boundary, allowing users whose holdings match the configured
Solana mint to pay for resource capacity without confusing the imported credit
with proof of a provider's work.

**Existing composition.** DreggCloud's service agreement has a provider,
payment asset, expected output, price and timeout; its archive retains output
commitment, turn/receipt hashes, balances and stage. Its assurance table says
fund/release/refund conservation is verified while output meaning,
receipt-to-request weld and independent-provider settlement remain weaker or
unavailable. DreggNet's Payable settlement has a typed `PaySubmitter`, exact
per-lease-period deduplication and an optional native turn hash. The bridge's
oracle-attested devnet exercise describes a real **stand-in** SPL lock ->
conserved mirror credit -> `resolve_pay` route.

**Blocking implementation gaps.** The Solana source-to-native asset identity
is not joined to `payment_asset`/DreggNet's 64-hex issuer-cell asset. The
devnet bridge's executable trust is an oracle attestation; its structure-only
inclusion does not authorize a mint, and the consensus-anchored path needs a
snapshot/geyser feed plus stake-vote evidence. No current lock-program deployment
for the selected real mint was established here; the inspected program is
legacy-token-only. The service result still needs an objective
verifier before a release can be described as correctness-contingent payment.

**Self-hosting impact.** A House can operate its own service and keep the
archive/receipts local, while payment remains a native, conserving transfer.
Interoperable payment would require every participating host to agree on the
asset issuer and bridge evidence policy; it does not require resource discovery
or make a single host a global marketplace.

## Receipts/runs located versus source only

* **Retained claim, not presently available artifact:**
  `docs/deos/SOLANA-DEVNET.md` records a 2026-06-28 devnet run. The associated
  ignored test expects an ephemeral
  `/tmp/dregg-solana-devnet/manifest.json`; no such manifest or other captured
  Solana run bundle was found in the inspected repository paths. Treat the
  document as a dated report until that bundle is re-presented or re-run.
  Its described lock used a devnet stand-in token and the oracle-attested
  mirror leg; it is not evidence of a real `$DREGG` lock.
* **PoA holder gate:** implementation, tests, and persistence code are present.
  I found no preserved live admission receipt/run in the inspected paths, so no
  claim is made that the mainnet holder API has issued a capability.
* **Portal:** its deployment README reports the access portal as live and
  identifies on-host roster/session state. No current live evidence was
  inspected. This repository contains the deployment declaration, not the
  `dregg_portal` product code or a preserved roster/receipt; it cannot establish
  an on-chain mutation statement.
* **Service/resource:** source can retain a signed `service-archive.json`, but
  no concrete operated archive/run was found under the inspected DreggCloud
  checkout. dreggnet-compute and Payable examples/tests are source-level
  evidence, not a found live provider settlement.

## Load-bearing verification files

1. `/Users/ember/dev/breadstuffs/poa-solana-gate/src/lib.rs:27-96` — pinned mint,
   Token-2022, mainnet policy; `:197-292` beta RPC observation validation;
   `:294-332` consensus-evidence entry; `:1379-1470` sealed consensus admission.
2. `/Users/ember/dev/breadstuffs/node/src/poa_holding_api.rs:1-8` — transport
   boundary; `:69-79` RPC seam; `:160-210` finalized account query; `:297-334`
   endpoints; `:520-536` beta admission receiver.
3. `/Users/ember/dev/breadstuffs/bridge/src/solana_holdings.rs:56-145` — public
   mint and Token-2022 policy. `/Users/ember/dev/breadstuffs/bridge/src/solana_feed.rs:258-261,
   1026-1074` — feed contract and snapshot implementation.
4. `/Users/ember/dev/breadstuffs/dregg-governance/src/holding_weight.rs:696-788,
   1060-1084` — consensus-only weight decision and ballot consumer.
5. `/Users/ember/dev/breadstuffs/solana-lock/src/lib.rs:1-42` and
   `/Users/ember/dev/breadstuffs/solana-lock/src/instruction.rs:22-64` — actual
   lock/escrow state intent; `/Users/ember/dev/breadstuffs/solana-lock/src/processor.rs:139-176,
   257-296,529-624,715-873` — legacy-token requirement, transfers and terminal
   escrow transitions.
6. `/Users/ember/dev/breadstuffs/bridge/tests/solana_devnet_e2e.rs:1-51,127-212`
   and `/Users/ember/dev/breadstuffs/docs/deos/SOLANA-DEVNET.md:10-47,98-153`
   — retained scope and limits of the dated devnet exercise.
7. `/Users/ember/dev/DreggCloud/service-cells/src/lib.rs:63-114,314-377` and
   `/Users/ember/dev/DreggCloud/service-house-adapter/src/lib.rs:1-15,115-285`
   — resource capacity, assurance boundaries, and durable signed evidence.
8. `/Users/ember/dev/dregg-infra/edge/portal/README.md:1-61,190-206` — reported
   holder portal operation and roster boundary; `/Users/ember/dev/DreggNet/durable/src/payable.rs:1-20,91-104,152-235`
   — native per-period payment/receipt seam.

## Parent review and external protocol reference

The parent re-read the holder policy and beta HTTP admission, the legacy-token
checks and transfer construction in `solana-lock`, and the dated devnet runbook.
The source-level compatibility finding is confirmed for those inspected bytes;
there was no fresh chain query, build, asset operation, or custody audit. The
three product mechanisms above remain agent proposals.

Token-2022 is deployed at a distinct program address and may carry extension
state beyond the legacy account layout. This supports treating token-program
compatibility and selected-mint extension policy as explicit integration work;
it does not establish the safety of a modified escrow. See the official
[Token-2022 documentation](https://www.solana-program.com/docs/token-2022).
Program-derived addresses permit program-authorized signing through the runtime;
using one alone does not supply provider, release or dispute policy. See
[Solana's PDA documentation](https://solana.com/docs/core/pda).
