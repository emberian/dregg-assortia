# Provider / homelab orientation — 2026-09-17 (read-only)

## Finding

No connected public homelab-provider market with resource
advertisement, $DREGG staking, reputation, challenge intake, and live slashing.
The closest existing pieces are useful and should be modeled as separate seams:
the DreggNet managed-provider runtime, the breadstuffs compute escrow offering,
the DreggCloud bounded service-cell path, and the node relay-custody referee.
A receipt establishes only the particular committed transition/evidence it
binds; it does not establish correct remote execution, available capacity, or a
stake consequence unless a verifier and executable settlement path say so.

## Existing paths and what they enforce

1. **DreggNet provider/runtime model: configured operators, not discovery.**
   `DreggNet/control/src/provider.rs` defines a `VmProvider` abstraction and
   `control/src/ec2.rs` implements an AWS EC2 provider; `control/src/fleet.rs`,
   `control/src/server.rs`, `gateway/src/vats.rs`, and `durable/` handle
   owner-scoped persistent servers, mesh reachability, workflow recovery and
   lease fulfillment. A provider is selected/configured by the control plane;
   there is no stake-gated registration, peer resource advertisement, open
   eligibility auction, reputation score, or slashing in that layer. EC2's live
   provision test is explicitly ignored/gated by `DREGGNET_EC2_LIVE=1`.

2. **There is a real execution-lease/metering formal substrate.**
   `breadstuffs/sdk/src/service_economy.rs` opens/funds/runs an
   `ExecutionLease`; `hosted-lease/` offers obligation or fused-prepaid
   metering, and `hosted-durable/` supplies settlement/meter outbox mechanics.
   `PrepaidLease.lean` and `HostingLease.lean` are the formal-model anchors.
   These establish capacity authorization and accounting for a known lease;
   they are not a provider-discovery or provider-stake protocol.

3. **Compute Exchange has enforced job-cell budget accounting, but not a token
   escrow or verifiable remote compute.**
   `breadstuffs/dreggnet-compute/src/lib.rs` wraps
   `starbridge-apps/compute-exchange`: post records a budget, one worker claims
   under a provider capability at a price no higher than budget, and requester
   settlement enforces `PAID + REFUNDED == BUDGET` in committed fields. Its
   honest-scope section is explicit that this is **not** an `Effect::Transfer` /
   `dregg-payable` wallet-to-wallet token balance move. Execution is also stubbed:
   the result is non-empty text, `SPEC_HASH` does not bind it to a correct output,
   and the proposed full path (confined worker plus verifiable-compute proof) is
   absent. It has neither timeout/challenge/slash nor provider reputation. Thus
   field-accounting and lifecycle refusal are enforced; monetary settlement and
   result correctness are not.

4. **DreggCloud service cells bind an expected digest and make timeout a refund,
   not a fault verdict.** `DreggCloud/service-cells/src/lib.rs` has a signed
   Grain offer, expected provider/output commitments, a prepaid lease checkpoint,
   and a service market. A mismatched output commitment refuses release; after
   `timeout_height`, renter refund is permitted exactly once. Its assurance table
   labels output meaning, receipt-to-request binding, nullifier durability,
   remote settlement/independent provider, and economic slashing as host-only,
   unavailable, or unwired. `service-house-adapter/` durably signs/replays this
   operated one-provider archive. This is the clearest current timeout vs
   incorrect-result distinction, but not a multi-provider adversarial market.

5. **A formalized/evaluable custody-fault-to-slash construction exists, but its
   live effect is incomplete.** `breadstuffs/node/src/relay_dispute.rs` uses
   `dregg_captp::custody::adjudicate_from_inbox` to form a bounded `SlashPlan`.
   `build_slash_turn` composes executor-enforced bond/dispute updates and
   conserving restitution/remainder transfers; its optional junior tranche is
   explicitly a `$DREGG` `AssetId` holding and uses price-free proportional
   forfeiture. `relay_slash_intake` can construct/test an executor turn with the
   cell program. The legacy HTTP dispute route still mutates an in-process mirror,
   and the intake turn is not wired into the live node submission pipeline. Its
   source also names a refund-witness gap. Thus a positive referee verdict can
   cause a tested model/executor effect, but no observed running path currently
   seizes a deployed provider bond.

6. **$DREGG support is a typed asset/custody design, not current economic stake
   evidence.** The slash code has an `AssetId` junior bond, while DreggNet's
   durable payment adapter resolves a token as a 64-hex issuer-cell asset and
   can submit conserving transfers. I found no current deployment configuration,
   funded provider bond, stake registry, or publicly checkable $DREGG custody
   state tying a provider identity to a minimum stake. Existing compute/service
   demos use integer amounts and configured/generic asset identities. Do not call
   them monetary $DREGG staking.

7. **No current fake-slash leaderboard implementation was located.** Direct
   searches found no devnet `fake slash -> leaderboard/reputation` path in the
   assigned repositories. The desired devnet rule should therefore be designed
   as: an independently checkable verdict writes a non-monetary reputation event;
   it must not call the same transfer/bond-seizure path as production. A timeout
   should record availability/noncompletion separately from a proved incorrect
   result or custody fault.

8. **Known local machines are build/ops topology, not a resource inventory.**
   `dregg-infra` fixes roles such as workhorse/hbox/persvati for PoA and build
   operations; `edge/headscale/config.yaml` discusses headless build/prove/
   homelab nodes. `breadstuffs/HORIZONLOG.md` records dated hardware measurements
   (notably hbox and persvati) for build scheduling. No source-backed registry
   advertises heterogeneous peer capacity, resource attestations, eligibility,
   or availability guarantees. Treat those documents as local configuration and
   dated observations only.

## Practical model boundary

The shortest honest next model is not one “provider” node. Keep distinct:

- provider identity and a signed resource/availability advertisement;
- stake custody and the exact asset/amount/floor it can lose;
- job specification, result commitment, and the verifier that decides it;
- timeout/noncompletion, incorrect-result, and custody-fault verdict classes;
- devnet reputation/leaderboard effects versus production conserving seizure;
- a receipt/settlement record versus proof of execution or a trust guarantee.

The inspected paths currently supply useful formal/evaluable pieces for the
lease meter and relay custody verdict, plus real job-cell accounting transitions.
The joins between them are the missing product/protocol work.
