# Clutch contribution to a DREGG-native nexus — bounded orientation, 2026-09-17

## Scope and evidence

Read-only source/history inspection on 2026-09-17. I read the live dClutch tree
“/Users/ember/dev/dclutch” at 6967e79 (dirty worktree preserved), its current handoff
and selected newest evidence, plus the separate dragons-clutch record/archive. I did
not build, test, query an RPC/frontend, read credentials, or submit anything. “Current
live” below therefore means no new observation.

The active implementation is dClutch; Dragon's Clutch says its dclutch/ subtree is a
publication copy and the archive is historical context
([README](/Users/ember/dev/dragons-clutch/README.md:5),
[dClutch AGENTS](/Users/ember/dev/dclutch/AGENTS.md:22)). Archive evidence is useful for
requirements/counterexamples, never a current runtime claim.

## What Clutch can contribute

Clutch is a bounded-state, fully-backed **claim and settlement capability**. It can add
economic finality when a nexus operation has an immutable outcome partition, payoff,
source/window/fallback, and collateral policy. It is not itself a general social graph,
local-first resource store, DREGG cell/node runtime, or Hermes client.

| Nexus boundary | dClutch contribution | Required nexus contract |
|---|---|---|
| Semantic controller | Lean-owned ABI/transition definitions emit Rust and TypeScript layouts; a Market names immutable Realm, Product, source policy, manifest, and releases. | Compile a specific resource/social commitment into a canonical, exhaustive/disjoint outcome/payoff object. Free-form posts, mutable rankings, or unspecified “community verdict” do not enter this boundary. |
| On-chain economic settlement | Hoard-backed complete sets, claims, Direct exchange, redemption, capability funding and closure. | Exact Solana Realm (token program, mint, adapter release, authority policy), accounts, funding quote, release and route manifest. dClutch remains owner of liability/custody facts. |
| External price observation | Pyth Sponsored Push Source admits a pinned on-chain PriceUpdateV2, candidate/certificate and settlement. | A Pyth price-data transport/publisher obtains and posts the external update; dClutch receives the authenticated Solana account and immutable source-release selection. This is separate from the requested Hermes agent/ACP integration. |
| External Hermes agent/ACP | No contribution established by this inspection. | The nexus must define agent identity, user consent, tool/resource protocol, durable local state, publication receipts, and any DREGG node/cell relationship. dClutch can later settle a narrowly specified result, but does not evidence this integration. |
| User surface | Market page does finalized reads, exact preview, wallet intent/transaction signatures, pre-send journal and completion observation. | Nexus supplies discoverability, operator-published route/release document, wallet policy and an honest statement of what the claim means. |

The Lean package calls itself the one place a dClutch protocol fact is stated so Rust and
browser code can be printed from it
([formal README](/Users/ember/dev/dclutch/formal/dclutch-semantics/README.md:1)).
That is a strong *inside-dClutch* semantic-controller interface; it neither generates a
DREGG controller nor substitutes for DREGG semantics.

### Trace: Direct claim purchase

1. The market page opens a seven-step flow: finalized inspection, Position readiness, signed
   seller offer, preview, wallet preparation, signing and send
   ([panel](/Users/ember/dev/dclutch/apps/dclutch-web/components/MarketTradePanel.tsx:137),
   [steps](/Users/ember/dev/dclutch/apps/dclutch-web/components/MarketTradePanel.tsx:363)).
   The user picks an outcome and ticket; an offer does not reserve seller claims
   ([panel](/Users/ember/dev/dclutch/apps/dclutch-web/components/MarketTradePanel.tsx:411)).

2. The SDK reads a finality floor, Core Market, Registry manifest, Direct program
   set/descriptor/config, Direct root, Claims aggregate and user Position. It names missing
   Direct capability, activation root, release evidence, or Position as a wall rather than
   accepting a static display as authority
   ([spine](/Users/ember/dev/dclutch/packages/dclutch-sdk/lib/directTradeSpine.ts:157),
   [walls](/Users/ember/dev/dclutch/packages/dclutch-sdk/lib/directTradeSpine.ts:249)).

3. The browser calculates the crossing from signed seller ticket, buyer nonce, exact
   collateral account and atom quantity. It rechecks both participants/nonces before the
   detached buyer intent signature
   ([flow](/Users/ember/dev/dclutch/apps/dclutch-web/lib/tradeFlowMachine.ts:380),
   [recheck/sign](/Users/ember/dev/dclutch/apps/dclutch-web/lib/tradeFlowMachine.ts:443)).
   Submission is intentionally outside the read-only SDK and is journalled first
   ([rationale](/Users/ember/dev/dclutch/apps/dclutch-web/lib/tradeFlowMachine.ts:47)).

4. Trading’s Solana program dispatches Hot execution only after its named routes. It
   authenticates envelope, invocation, frame, root-prestate digest, Market/root and Product
   runtime ([dispatch](/Users/ember/dev/dclutch/programs/dclutch-trading-sbf/src/lib.rs:1095),
   [Hot entry](/Users/ember/dev/dclutch/programs/dclutch-trading-sbf/src/hot_v3.rs:1136)).
   Direct InlineOrdinary then selects configuration and runs its Direct crosscheck before
   commit ([crosscheck](/Users/ember/dev/dclutch/programs/dclutch-trading-sbf/src/hot_v3/execute.rs:1517),
   [guard](/Users/ember/dev/dclutch/programs/dclutch-trading-sbf/src/hot_v3/direct.rs:311)).
   The nexus must commit its semantics before this boundary as immutable records; dClutch
   executes the bounded economic consequence, rather than interpreting a live DREGG graph.

### Pyth price-source trace — distinct from Hermes agent/ACP

The founding browser reads an on-chain sponsored PriceUpdate via the Source family WASM
decoder, requiring its Receiver program and a finalized floor
([reader](/Users/ember/dev/dclutch/apps/dclutch-web/lib/sourceProviderV1.ts:840)).
The retained Pyth evidence says an external pusher consumes **Pyth's price-data service
named Hermes** and a chain payer,
whereas dClutch starts at immutable SourceSpecV1(PythSponsoredPushSnapshot) and fixed
on-chain Receiver/Push releases
([evidence](/Users/ember/dev/dclutch/docs/evidence/PYTH_CREDENTIAL_FREE_DEVNET_2026_08_29.md:55),
[path](/Users/ember/dev/dclutch/docs/evidence/PYTH_CREDENTIAL_FREE_DEVNET_2026_08_29.md:75)).
That makes a Pyth-update publisher a possible nexus provider/cell job, with its own
update-signer/payer custody, publication log, monitoring and penalty policy. It provides
no evidence about the separately requested external Hermes agent/hermes-acp user-agent
integration, its resource protocol, or local-first user state; those need their own
integration contract and evidence.

## $DREGG: exact current role and viable first use

No exact $DREGG mint address, fee recipient, stake account, payment route, or penalty
record was established by the selected current source/cohort material. Cohort 17 calls its
mint keys/collateral-mint.json; the guide calls devnet assets “test tokens”
([cohort](/Users/ember/dev/dclutch/tools/cohort/cohorts/17.json:61),
[guide](/Users/ember/dev/dclutch/docs/guides/trader.md:1)). Do not equate these synthetic
assets with real $DREGG.

The implemented attachment point is a **dogfood Realm**, not token-name branching:
RealmV1 binds token program, collateral mint, adapter release and mint/freeze authority
policies ([Realm](/Users/ember/dev/dclutch/crates/dclutch-market/src/realm/mod.rs:139)).
A real $DREGG Realm could back a specifically founded Market’s payouts/complete-set
collateral. A separate funding quote can use Realm collateral, binding Realm, adapter,
token program, mint and refund beneficiary
([binding](/Users/ember/dev/dclutch/crates/dclutch-market/src/capability_manifest/funding.rs:647)).

Selected Direct fees are denominated in that Market’s collateral and go to its
founder-selected fee_recipient, not a protocol treasury
([guide](/Users/ember/dev/dclutch/docs/guides/trader.md:60)). A 50-bps-per-side fee has
retained two-transaction local evidence, but not $DREGG/devnet proof
([fee evidence](/Users/ember/dev/dclutch/docs/evidence/FEE_SECOND_TRANSACTION_PAIR_2026_08_31.md:95)).

A defensible initial utility is therefore: **$DREGG as the exact backing of a narrowly
defined redeemable claim, or a precommitted provider/service funding compartment.**
“Stake to operate a DREGG node” with recorded-only penalties needs a new
nexus-owned stake/slashing state machine; dClutch’s fully-funded Market accounting must
not be relabelled as that. This follows the recorded direction that DREGG is not required
collateral or a hard-coded semantic branch
([intent](/Users/ember/dev/dclutch/docs/INTENT.md:309)).

## Evidence ladder and current blockers

- **Current source:** browser/SDK/program paths exist, but the 2026-09-09 handoff says the
  fresh current-source all-program cohort is not deployed
  ([handoff](/Users/ember/dev/dclutch/docs/HANDOFF_2026_09_09_USAGE_PAUSE.md:50)).
- **Test source:** Direct Inline and generated ABI paths exist. The **2026-09-09 handoff**
  reports that its then-latest Direct mixed seller/fee-account repair lacked focused
  SBF/validator proof because unrelated dirty Structured code blocked compilation, and
  owed a frame capture. This inspection did not rerun that build or test
  ([handoff](/Users/ember/dev/dclutch/docs/HANDOFF_2026_09_09_USAGE_PAUSE.md:86)).
- **Captured local validator:** retained Direct simulation has three nonzero fills,
  fee settlement and restart, all founder-as-seller; not reciprocal liquidity. A separate
  Dealer run has nonzero fill/withdraw evidence against an older sealed runtime, explicitly
  not devnet/current-source convergence
  ([handoff](/Users/ember/dev/dclutch/docs/HANDOFF_2026_09_09_USAGE_PAUSE.md:55),
  [Dealer](/Users/ember/dev/dclutch/docs/evidence/DEALER_ACCEPTED_LOCAL_VALIDATOR_2026_09_08.md:35)).
- **Devnet record:** cohort 17 carries recorded program/market addresses; the Pages
  checkpoint records a static-site deployment. Neither is newly observed here, and cohort 17
  is the previous deployment, not a current-source release.
- **Mainnet/current live:** no mainnet claim; no live probe. The strongest archive lifecycle
  is explicitly a pinned local Pyth campaign, unpromoted and not devnet/mainnet
  ([archive](/Users/ember/dev/dragons-clutch/archive/handoffs/CURRENT_TRUTH.md:41)).

Before choosing a first activity, decide whether it needs (A) a bounded objectively
resolvable economic claim, (B) up-front provider/service funding, or (C) social/resource
publication without claim settlement. Only A/B naturally use dClutch. Do not select markets
because the code is present; compare semantic fit, source availability, operator burden,
funding and audience with a simple DREGG publishing/resource offering.

For A, require a real $DREGG Realm/mint policy; exact outcome/source/fallback definition;
a Pyth price-publisher/update operator contract where applicable; cohort/release/route
status; and fresh reciprocal runtime evidence for the chosen capability. Independently,
the external Hermes agent/hermes-acp integration needs its own user-consent, identity,
local-state, tool/resource, publication-receipt and DREGG-node/cell contract. For B,
define who earns/reclaims funds and which observed DREGG resource receipt closes the
obligation; no inspected dClutch source supplies that receipt semantics. For C, retain
dClutch as later settlement capability.

## Source set suitable for assortia hashing

1. /Users/ember/dev/dclutch/formal/dclutch-semantics/README.md:1-57
2. /Users/ember/dev/dclutch/crates/dclutch-market/src/realm/mod.rs:139-260
3. /Users/ember/dev/dclutch/crates/dclutch-market/src/capability_manifest/funding.rs:647-740
4. /Users/ember/dev/dclutch/apps/dclutch-web/components/MarketTradePanel.tsx:137-148
5. /Users/ember/dev/dclutch/apps/dclutch-web/lib/tradeFlowMachine.ts:304-405
6. /Users/ember/dev/dclutch/packages/dclutch-sdk/lib/directTradeSpine.ts:157-292
7. /Users/ember/dev/dclutch/programs/dclutch-trading-sbf/src/hot_v3.rs:1136-1185
8. /Users/ember/dev/dclutch/docs/HANDOFF_2026_09_09_USAGE_PAUSE.md:50-124

Limit: these paths establish interface/evidence status, not a dregg-assortia integration,
DREGG nodes/cells, Pyth-publisher operation, Hermes agent/hermes-acp integration, real
$DREGG deployment, or live user activity.

## Parent review

The parent re-read the active/released-tree instructions, Realm and funding
bindings, the Direct SDK reader and wallet preparation, the Trading Hot entry
and Direct crosscheck, the September 9 handoff, and the Pyth source evidence.
No build, program execution or current deployment check was run. The handoff's
compile/runtime statements remain dated evidence, and suggestions for a first
market or funding application remain proposals. In particular, Pyth's Hermes
price-data service must not be indexed as the external Hermes agent integration.
