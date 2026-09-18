# Economic resources for the programmable nexus — source proposal, 2026-09-17

Prepared by Astra `/root/sprint_economic_resources`. This is a bounded implementation proposal, not an adopted release design. I read the assortia intent, milestone, provider, Solana, Clutch and nexus notes; breadstuffs' durable orientation and relevant source; minidregg's instructions, ATLAS and canonical carriers; and dClutch's instructions and selected receiving code. No Git, build, test, SSH, RPC, wallet, deployment, asset action or user-directed message was performed. Source facts refer to the inspected working bytes, not an independently established committed revision or current live deployment. Only this temporary report was written.

## Recommendation

Build public jobs, bonded service offers and Clutch operations as **programmable resource families over the same kernel request, accepted effect and durable operation machinery**. Finish the missing kernel and compiler connections; do not implement economic truth in a shell wrapper and promise to formalize it later. This supports a mixed workroom/social/game/computation environment without choosing one app genre.

The first independent source bundle should make one useful family of **public DREGG-program evaluations over pinned resource revisions** authorable, dispatchable, checkable and consumable. Its outcome becomes a resource revision through the canonical transition. Make funding, provider obligation, result acceptance and reputation refer to the same job identity and exact statement. Add an authenticated storage/challenge family to serve participant-hosted cells using its own service semantics. A real OS job broker can execute other public commands, but each economically adjudicated job must select an actual checker and terms; an exit code is not a general correctness predicate.

Implement real custody support, its observation/admission consumer, and complete bond exit in parallel. The accepted devnet rule is **real $DREGG locked; penalties recorded only**. An observed holding or a leaderboard badge does not fulfill it. The exact custody deployment and funds operations remain unselected; this does not prevent finishing their semantics, generated wires, local-validator tests and resource adapters now.

Clutch should also become a shell-addressable resource adapter for its actual economic operations. It retains ownership of its Realm, Market, liabilities and custody. A provider bond is not a Clutch Hoard, and its funds must not be relabelled as claim backing or spent as service capital.

## Corrections and existing receiving paths

### Compute settlement already transfers value, but its binding remains incomplete

The current `dreggnet-compute` wrapper **does consume the transfer helper**. This is not merely a separate unused helper in compute-exchange:

1. `/Users/ember/dev/breadstuffs/dreggnet-compute/Cargo.toml:18` selects `../starbridge-apps/compute-exchange`.
2. Its `src/lib.rs:58–61` imports that crate's `fire_settle`; `do_settle` at `:395–445`, specifically `:435`, calls it with the recorded worker cell.
3. `/Users/ember/dev/breadstuffs/starbridge-apps/compute-exchange/src/lib.rs:1194–1211` reads live BID/BUDGET and calls `settlement_effects`; `:1141–1144` includes `payment_effects`; `:1088–1092` calls `pay_effects` for nonzero amounts.
4. `/Users/ember/dev/breadstuffs/app-framework/src/payable.rs:43–46` reexports the implementation; `/Users/ember/dev/breadstuffs/dregg-payable/src/payable.rs:100–102` emits `Effect::Transfer { from, to, amount }`.

Therefore the wrapper's bottom field-only note (`dreggnet-compute/src/lib.rs:781–795`) is stale against this consumer. The earlier assortia provider/compute scope should be corrected after the parent establishes HEAD/working-tree provenance. I did not run settlement.

The real work is larger and more precise than adding a transfer:

- The budget is an unfunded promise. Compute-exchange's post path records a ceiling; actual payment occurs at settle. Its top-level discussion at `:43–75` describes how blanket `StrictMonotonic(STATE)` interferes with funding the job cell. This is design/implementation work to repair, not an impossibility theorem over DREGG.
- `job_cell_program` and `job_invariants` at `:443–537` constrain field relations. `build_settle_actions` at `:699–702` explicitly notes that the transfer destination is not kernel-bound to `PROVIDER_HASH`, nor its amount to `PAID`. Honest helpers composing both do not enforce that relation against a hostile caller that constructs effects directly.
- The wrapper's `do_settle` at `:404–413` accepts any nonempty result string. `SPEC_HASH` does not make it a correct result. Result acceptance, payment record, actual recipient and actual balance delta must enter one receiving relation.
- `co_place_worker_cell` at `dreggnet-compute/src/lib.rs:236–250` derives and inserts a payee from a handle. A contributed provider needs its own authenticated payout resource binding, not a handle-derived synthetic purse silently standing in for one.

### Capacity, dispatch and durable settlement have useful code with distinct obligations

`/Users/ember/dev/breadstuffs/sdk/src/service_economy.rs:267–280` defines a checkpoint ceiling/monotonic program. `ExecutionLease::open` at `:328–365` installs it by direct ledger update; `fund` at `:370–377` transfers native value; `run` at `:387–405` commits a checkpoint plus work effects. Closing the user-program installation/projection path must include this constructor; the installed state must arise through the same accepted transition, not remain a privileged setup mutation.

`/Users/ember/dev/DreggNet/control/src/provider.rs:174–225` exposes provisioning and leased dispatch. Its default `run_lease_workload` discards the supplied workload and calls the demo `run_lease`. `control/src/local.rs:87–114` overrides it and routes declared work to `dreggnet_bridge::fulfill_workload`; no corresponding `run_lease_workload` override appeared in `control/src/ec2.rs` in this bounded search. Any reuse for public jobs must either execute the exact declared program or return an explicit unsupported-program refusal. Never acknowledge a demo fallback as the submitted job.

`/Users/ember/dev/DreggNet/durable/src/payable.rs:152–202` checks an in-memory `(lease_id, period)` dedup map, submits via `PaySubmitter`, then records the result. The receiver must own a durable idempotency key and external-outcome reconciliation: a crash after submit and before insertion cannot be repaired by the in-process map alone. The token identifier is a native issuer-cell asset, not automatically the selected Solana mint.

`/Users/ember/dev/DreggCloud/service-cells/src/lib.rs:239–315` binds expected provider/output and retains native receipt signatures. `match_and_fund_receipted` at `:555–612` takes already-completed work and seeds/funds a ledger; it is explicitly post-work. `fulfill`/`refund` at `:621–659` conserve settlement state, with live-process receipt nullifiers. `service-house-adapter/src/lib.rs:117–159` signs exact agreements and `:585–620` journals settlement obligations; it adds actual archive/recovery work. These are material for a real pre-work agreement, not evidence that one currently exists across independent providers. The selected core transition must bind work to request/provider/output and commit the nullifier and value changes durably, removing reliance on an archive-only check for kernel truth.

### Existing objective storage checker

`/Users/ember/dev/breadstuffs/storage/src/durability_deal.rs:313–337` checks shard index, committed shard and root opening. `:362–388` additionally verifies the assigned operator's signature over the deal root, index and challenge nonce (`challenge_message` at `:168`). This is a useful precise service relation. It authenticates a returned opening at a challenge; it does not by itself establish continuous availability, physical storage location, or that the operator never fetched from another holder.

`storage/src/placement.rs:80–113` takes candidate bond/floor/dispute scalars from its caller. Convert authenticated, current bond and reputation state into these candidates; do not trust a provider's advertised integer. `node/src/market_loop.rs:23` puts the composition behind `#[cfg(test)]`; it is test-source evidence, not the live provider market.

### Custody and penalties must be separate receivers

`/Users/ember/dev/breadstuffs/solana-lock/src/escrow.rs:79–100` stores mint, depositor, fixed refund destination, exact amount, deadline and ID. `processor.rs:543` and `:698` require legacy `spl_token::id()`. This cannot simply serve the Token-2022 program selected at `poa-solana-gate/src/lib.rs:27–30,65–75`.

`solana-lock/src/processor.rs:674–755` releases after an oracle threshold, binding mint/amount/recipient/escrow ID. `:799–873` refunds to the captured depositor destination strictly after the deadline while still Locked. This is a trade escrow state machine, not a provider obligation/exit policy. A provider bond needs its own exact terms, admission interval, relationship to outstanding obligations, explicit exit and observed custody state. Token-2022 support must cover the chosen mint/account extension policy and actual credited/debited amounts, not only swap the program ID.

`solana-lock/src/attestation.rs:43–78` signs a payload of mint, amount, recipient and redeem ID under an unlock domain. The next bond operation envelope should additionally bind its operation kind, selected chain/cluster, program/config, provider and terms identities. Do not accidentally reuse the same authorization shape for release, penalty, pool redemption and a different deployment.

`node/src/relay_slash_intake.rs:164–211` consumes custody evidence/referee results and constructs a signed seizure turn; it does not submit it. Its module at `:42–64` names submission and refund/fee evidence obligations. This is **custody-drop adjudication**, not an arbitrary compute-result verifier. The devnet verdict receiver must append reputation evidence and preserve locked value. It should not route through this monetary seizure builder with a flag that happens to be false.

### Clutch has a strong external operation boundary, but no generic DREGG outcome source

`/Users/ember/dev/dclutch/crates/dclutch-market/src/realm/mod.rs:139–178` names the exact token program, mint, adapter release and authority policy. `capability_manifest/funding.rs:647–684` adds exact Realm/release/token/mint/refund binding for service/funding compartments. Hoard principal and service funding remain distinct economic facts under `dclutch/AGENTS.md`.

`packages/dclutch-sdk/lib/directTradeSpine.ts:157–198` authenticates finalized Market and selected manifest/release records. `apps/dclutch-web/lib/tradeFlowMachine.ts:380–480` plans from the actual participants, ticket, current replay nonces and collateral account. `programs/dclutch-trading-sbf/src/hot_v3.rs:1136–1185` authenticates the envelope, frame, root prestate and Market/Product; `hot_v3/execute.rs:1517–1549` runs the Direct crosscheck before committing. The shell adapter should consume these generated/public interfaces, preserving wallet authorization and nonce checks; it should not reimplement the exchange in a DREGG cell.

`crates/dclutch-source/src/lib.rs:943–1024` has explicit Pyth, shared, relayed-Solana-account and parent-certificate source profiles. `SourceSpecV1` at `:1029–1078` binds immutable source units/provider/config/capacity. The relayed account wire in `crates/dclutch-source/src/relay/wire.rs:44` carries Solana account observations; it is not a ready DREGG job-verdict adapter. If a Clutch claim is to settle on a DREGG job outcome, implement a new exact source/adapter contract in Clutch's own semantic ownership, with precommitted outcome partition, source rule, window and fallback. Do not reinterpret a mutable reputation score or arbitrary receipt hash as that source.

Clutch's instructions forbid importing neighboring protocol code wholesale. Implement the boundary through authenticated public records/generated wires and keep semantic ownership in each repo. Its `formal/dclutch-semantics/README.md:1–57` describes the ABI owner/emission path to extend. The September 9 handoff is dated evidence; this investigation does not establish a current-source cohort or fresh runtime success.

## Contract to implement in the core

The following are proposed **first-order data** with one semantic owner and generated wire views. They are not extra mutable workflow truth in a side database.

| Resource/fact | Required binding | Receiving consumer |
| --- | --- | --- |
| ProviderOffer | Provider identity/key epoch; exact operation families; capacity units/limits; endpoint as locator; validity; payout resource; terms and bond policy | Admission/placement converts it and current evidence into eligibility; worker verifies the accepted job fits it |
| BondTerms + BondObservation | Asset as chain/cluster/token program/mint; custody program/config/account; provider identity; amount; terms; current custody status/finality evidence; exit | Kernel provider-eligibility effect; no transferable native credit is implied by observing a bond |
| PublicJobSpec | Operation ID; requester/authority; pinned program/compiler/checker/environment; args and public inputs; exact resource pre-roots; allowed effect footprint; output schema; limits; payment terms; offer; deadline/challenge policy | Worker dispatch, exact checker, accepted result effect, settlement and dispute family all consume the same spec |
| SignedResultClaim | Job/spec ID; provider; attempt; output/artifact roots; claimed status/units; evidence locator/hash | Exact result checker and publication; a provider signature identifies whose claim is adjudicated |
| JobVerdict | Exact job/claim/checker/evidence and adjudication policy; outcome class; admissible clock/window; verdict ID | Result publication, contractual payment/release/refund and once-only reputation event |
| ExternalOperation | Semantic operation ID and exact external request; dispatch journal/transaction identity; unresolved or finalized observation | Solana/Clutch observation consumer; durable reconciliation after crash/retry |

Do not collapse admission, execution observation, result acceptance and external finality into one success flag. The separation is necessary to implement recovery and close the whole path, not a stopping condition.

Proposed initial computation relation: the pinned DREGG program, run on the pinned public inputs under the declared environment and bounds, yields exactly the claimed result and permitted effect patch. The selected core evaluator/compiler supplies that meaning. The worker is an untrusted producer; the receiving checker is the authority. An authored tool can use it for a resource transformation/query and publish the resulting linked revision. This remains useful across workrooms, stories, games and public computation.

A known expected-output hash is sufficient only for tasks actually specified that way. Do not pretend it solves arbitrary remote computation. Likewise CPU seconds, availability and nondeterministic external I/O need their own declared measurement/adjudication relation. A timeout is observable under a specified deadline/evidence/authority model; mere absence at one client is not a proof of malicious computation.

## Compatibility obligations with the kernel carrier

1. `minidregg/Theory/AcceptedCellEffect.lean:57–104` retains lawful family codecs, exact declaration/outcome/evidence, unique patch and request authority. Use it with `Theory/AcceptedCellEffectRequestBinding.lean:36–75` so args identity is also bound. Do not erase this into `verified: true` and rebuild economic mutations in Rust.
2. `Kernel/MultiCellHyperedge.lean:39–145` carries heterogeneous per-incidence schemas/materializers, exact pre-cells and all accepted legs. Funding, job state, provider reserve and payout need this shape or an explicitly proved equivalent, not the old empty-resource schema. Its `:172–237` exposes the actual handler-evidence and resource-law obligations. Give economic value coordinates real asset meaning; a zero delta function over no coordinates is not conservation.
3. `Theory/CanonicalTransition.lean:43–84,113–154` derives post and roots from the actual validated patch. Bind settlement records to actual conserved balance deltas, recipient and asset; bind accepted output to the same request/patch. Rejecting a forged helper input is insufficient if raw effects can bypass it.
4. `Compiler/DeclaredHyperedgeArtifact.lean:14` still imports the legacy carrier. If chosen for the nexus, complete its typed multi-resource projection, practical canonical encoding, generated descriptor and native consumer rather than narrowing public jobs to fit an obsolete artifact.
5. Durable commit must publish result, job terminal state, reserved-capacity update, nullifier and appropriate settlement/reputation effects atomically in the selected store. The physical multi-cell handler, outbox and receiving replay consumer must satisfy the semantic contract. A final receipt cannot be manufactured from a pending dispatch.
6. Proof closure must establish the exact statement used for these effects: program/input/result, authority, full state/resource patch and record-to-balance equality. The known STARK statement gaps are work to finish in the chosen cone. A checker identity or a proof-shaped blob does not discharge them. All AIR work remains Lean-authored/generated.

## Suggested source bundles and parallel boundaries

These are proposals for lane ownership, not claims those paths already exist.

**Bundle A — job/obligation semantics and one exact checker (first).** Proposed `minidregg/Theory/PublicJob.lean`, `Theory/ProviderObligation.lean`, `Theory/PublicJobEffects.lean`, and generated compiler/codec consumer under the selected `Compiler/` path. Define the job statement and meaningful accepted/rejected witnesses before proving it; instantiate the actual accepted-effect/request-binding carrier. Start with DREGG-program evaluation, with a separate storage-challenge family as the next concrete relation. Implement raw-effect hostile callers in the receiving runtime, not only helper tests. The kernel lane owns shared carrier/compiler signatures; this lane consumes them.

**Bundle B — funded resource settlement.** Repair the selected compute/service consuming path: funding reservation before dispatch; payment destination/amount/asset tied to the job; exact result/verdict nullifier; refund and cancellation; deadline. Candidate existing consumers are `starbridge-apps/compute-exchange`, `dreggnet-compute`, `sdk/src/service_economy.rs`, and the `DreggCloud` service adapter. Select one authoritative runtime and replace the superseded path in that user journey; do not leave two economic interpretations active. App renderers then consume committed facts.

**Bundle C — provider custody/eligibility and recorded penalties.** Implement token-program/extension-aware bond custody and its authenticated read/evidence adapter, domain-bound operation wires, provider registration/offer acceptance and complete withdrawal state machine. Existing starting files are `solana-lock/src/{state,escrow,instruction,processor,attestation}.rs` and the Solana observation boundary; changing the schema is expected core work. If the trade escrow remains a separate useful protocol, give bonds a distinct operation/state machine instead of silently changing trade semantics. Build local-validator scenarios using explicitly synthetic assets, keeping real-asset policy configurable until selected. Implement `RecordPenalty` as an accepted effect with a theorem and receiving check that every bond-value coordinate is unchanged and no custody-transfer request is emitted.

**Bundle D — worker, history and recovery.** Share one JobSpec/OperationID with the shell/Hermes broker and participant-node transport. Finish declared workload dispatch, scoped environment, capability and limit enforcement, cancellation, output collection, independent checking, durable outbox and result publication. Reuse source contracts, not `VmProvider`'s demo fallback. Lease meter counts must be the units the agreement actually charges. This is a joint consumer with shell/local-first lanes, not a separate scheduler truth.

**Bundle E — Clutch resource adapter.** Outside Clutch's semantic kernel, expose inspect/prepare/submit/reconcile operations for a selected supported capability with its authentic generated ABI, immutable route/release, wallet policy and finalized poststate. Persist DREGG intent and actual observed external result as causally linked events. Start offline and with a fresh local validator; no real funds are needed to finish the consumer. If economic job-outcome claims are chosen, add the new Source/Resolution adapter inside Clutch through its Lean owner/emission path and require end-to-end certificate consumption. Do not make a new market a prerequisite for every job.

## Acceptance that would actually close the work

- An ordinary shell user authors a new resource transformation from existing DREGG programming primitives, publishes/pins it, and runs it on another machine over a public resource revision. The checked output is published through the same canonical resource/history path and can be called by another user's tool.
- Change program, input, checker, provider, nonce, output or effect footprint independently: the receiving checker/transition refuses the exact mismatch without committing output, payment or reputation. Test raw signed requests outside the friendly builder.
- Fund the job, then attempt to spend its reserved budget elsewhere: the reservation remains enforceable. A valid completion produces the contracted exact recipient/asset/balance delta and matching terminal record. Forging PAID, substituting the payee or omitting the actual transfer refuses.
- A forged or stale bond observation, wrong token program/mint/deployment, withdrawn bond or incompatible offer cannot create eligibility. Concurrent accepted work consumes the declared capacity/reservation policy; self-reported `bond` values never qualify a provider.
- Correct result, signed incorrect claim, timeout/noncompletion, requester cancellation and custody-drop evidence follow distinct declared rules. A timeout does not fabricate an incorrect-result proof. Missing external observations remain unresolved until the declared recovery/evidence rule decides them.
- A valid devnet penalty appends one durable attributable event. Replay, restart and reimport cannot duplicate it; all locked balances remain identical and no penalty transfer is sent. An appeal/correction, if selected, is new evidence rather than deletion of the old event.
- Bond exit stops new obligations at the defined point, handles accepted work and its bounded challenge interval, returns to the exact authorized destination, and remains recoverable. Release/refund races do not both succeed. An indefinite lock must not become a concealed monetary penalty.
- Crash worker/host between admission, dispatch, external submission, result receipt, kernel commit and acknowledgment; retry from another client. Exactly one economic/outcome effect is consumed and unresolved external work is reconciled by identity, not blindly resent. Verify intermediate durable records, not only that the final database root reopens.
- Clutch operations refuse substituted Realm, route/release, Market, wallet, account or replay nonce and then consume a genuine finalized poststate into the nexus resource. DREGG completion does not invent Solana finality; a receipt of intent is never a completed purchase. Test only the chosen capability's promised actions; reciprocal trading is required if trading is promised, not for a funding-only feature.

## Decisions ember genuinely owns, without blocking independent implementation

1. **Real asset and custody domain:** confirm the exact $DREGG mint/token program/cluster and whether experimental DREGG service operation is intended to lock that real asset there. DREGG's devnet stage and Solana's cluster are different variables. Local synthetic assets are test evidence only.
2. **Bond terms:** amount/floor or reservation rule, eligibility scope, exit/withdrawal interval and destination, and the treatment of outstanding obligations. Proposed default design direction: request exit stops new obligations; already accepted obligations have a fixed finite completion/challenge horizon; penalties change reputation only. This is a proposal, not accepted custody authority.
3. **Adjudication and practical use:** which initial objective job families to expose, who may issue/appeal a noncompletion or incorrect-result verdict under which evidence rule, and whether friends buy capacity/time or a checked result. We can implement both typed contract forms without pretending they are economically identical.
4. **Clutch's initial purpose:** expose existing claims/positions and selected operations, use a separate service-funding compartment, or found a specific immutable claim over a selected source. Integrate its resource adapter now; do not invent a prediction market solely to display a token transaction.

These decisions affect external economic behavior. They do not require asking ember to select a single application genre, approve ordinary source repair, or choose every implementation detail. The long sprint should budget real kernel/compiler/runtime work for these closures instead of presenting current caveats as acceptable endpoints.
