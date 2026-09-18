> Bounded source review by the Sol build-pool agent, September 18, 2026. No builds or deployments were performed. Recommendations are proposals; the receiving brief is [resource-host lifecycle](../contributing/resource-host-lifecycle.md).

# Candidate boundary: durable resource-host lifecycle and DreggNet adapter

## Recommendation

Give an experienced backend/platform contributor one substantial subsystem: a **durable resource-host supervisor** that reconciles a logical vat/node host with a provider resource, drives metering and idle/lapse cleanup, records auditable lifecycle events, and exposes owner-scoped lifecycle operations through DreggNet. Its first backend can be `LocalProvider`; EC2 integration follows the same contract once remote worker registration exists.

This is a coherent consuming boundary, but the existing implementation is not production lifecycle code yet. It should be repaired at the join rather than wrapped and declared complete.

## What exists now (source at 2026-09-18)

- `DreggNet/control/src/provider.rs:174-220` defines `VmProvider`: provision, terminate, list/status, and funded workload dispatch. It has provider machine IDs and workflow instance IDs, but no provider-neutral `ensure/adopt(logical_host_id)` or reconciliation contract.
- `DreggNet/control/src/server.rs:540-694` has a durable `ServerStore`/`ServerFleet`. Records retain lease, machine ID, metering cursor, endpoint and checkpoint root. `reload`, however, calls `provision` for every running record (`:657-665`) and overwrites `machine_id`; with a real provider this can duplicate a resource after a control-plane crash. It recreates an empty `ComputeCell` while retaining only the checkpoint commitment (`:677-683`), not a restorable image.
- The fleet already contains useful state transitions and tests: launch/wake, prepayment, `meter_period`, failure-isolated `tick_uptime` (`:1165-1269`), independent idle reap (`:1272-1309`), stop/destroy (`:1312-1323`), checkpoint/fork behavior, and restart accounting in `control/tests/persistent_servers.rs`.
- `DreggNet/gateway/src/vats.rs:261-288` serves authenticated `POST /v1/vats` and owner-scoped GET list/item. Create funds, creates and launches a fleet record (`:291-294`). The file explicitly records two unreconciled rent rails, ignored requested size/region, and absent stop/wake/fork HTTP verbs (`:39-52`).
- `DreggNet/gateway/src/main.rs:548-584` constructs this plane with `LocalProvider`, a file store, and an in-process conserving ledger. No production call site drives `tick_uptime` or `reap_idle`; period-one prepayment is therefore not an ongoing supervisor.
- `DreggNet/control/src/ec2.rs:497-564` really provisions, lists, polls and terminates EC2 through the AWS CLI. Workload dispatch still requires a registered mesh worker; the missing remote deploy/registration plane is surfaced as `Unimplemented`, with tests at `:726-788`.
- `DreggNet/control/src/node_api.rs` has a settlement adapter with a durable write-ahead dedup ledger. The gateway vat construction does not currently use it.
- `DreggNet/gateway/tests/no_free_compute.rs` checks funding refusal/admission. `gateway/tests/live_wireup.rs` has shipped-gateway coverage, but its cross-repository real-node case is ignored and environment-dependent. These are useful tests, not evidence of an operated provider lifecycle.
- `dregg-infra/edge/compose/` and `edge/deploy.sh` deploy the current node/web/catalog/observability stack. They do not deploy the DreggNet vat gateway or its metering/reaper. Infrastructure integration should come after the deterministic lifecycle contract.

## DreggCloud evidence and constraint

`DreggCloud/REORIENT.md:16-18` labels DreggNet requirements/architecture archaeology and rejects rebuilding a conventional global control plane. Reuse its hard-won protocol rules, not its product topology. `service-house-adapter/src/lib.rs` provides archive-first signed operations, exact replay, poisoning after uncertain persistence, typed settlement-only reopen refusal, and public offline archive audit. Current limitations are stated in `DreggCloud/HORIZONLOG.md:74-110`: House admission is not atomic with daemon operation, does not custody daemon capacity/seeds, and is not federation-visible. The 2026-07-11 hbox lifecycle artifacts under `service-house-adapter/verification/` are historical evidence only.

The new supervisor should therefore make uncertainty explicit: journal intent before provider effects, reconcile after every restart, and enter a typed blocked/settlement-only state when it cannot prove whether a resource exists or a charge/effect committed. Do not copy DreggCloud code into DreggNet or claim federation finality.

## Owned files and contracts

Contributor-owned core:

- `DreggNet/control/src/provider.rs`: add logical-host discovery/adoption and idempotent reconciliation semantics, including an explicit Unknown outcome.
- New focused module such as `DreggNet/control/src/supervisor.rs`: durable operation journal, recovery state machine, timer driver, per-host task supervision, event/status projection, and deterministic shutdown.
- `DreggNet/control/src/server.rs`: route fleet startup and lifecycle effects through the supervisor; preserve existing settlement and state-machine laws.
- `DreggNet/gateway/src/vats.rs` plus focused gateway tests: stop/wake/destroy/status/events, owner scoping, idempotency keys, and honest degraded states.
- Focused fake-provider/restart tests in `DreggNet/control/tests/`; optional EC2 adapter changes stay in `control/src/ec2.rs` after the core contract is green.

Upstream contract, coordinated rather than reimplemented:

- Bread’s reusable node-host seam from `breadstuffs/node/src/lib.rs` and boot recovery: open/init, ready/status, submit/lookup, event resume, quiesce/stop. The review in `/tmp/dregg-android-runtime-contract-review.md` shows today’s `run(Cli)` owns process globals/signals and lacks a stoppable embedded handle. The contributor should consume that extracted host interface when available, never create a second executor or persistence model.
- DreggCloud House/custody and federation remain owned by their current maintainers; this subsystem emits exact lifecycle evidence that a later custody adapter can authorize.
- `dregg-infra` receives deployment manifests only after the supervisor has deterministic restart tests.

## First acceptance journey

Using a deterministic fault-injecting provider, durable temp store, real settlement ledger, and the local reusable node host:

1. An authenticated, funded owner creates a vat with an idempotency key. The supervisor journals intent, provisions once, opens the node host, prepays period one, and reports Ready with a monotonic event cursor.
2. Inject a crash after provider creation but before the durable completion marker. On reopen, reconciliation adopts the same provider resource; it neither provisions nor charges twice. If discovery is ambiguous, status becomes typed Unknown and no destructive/provider effect runs.
3. Drive the supervisor clock: each period settles exactly once; exhausted funding lapses and releases once; the independent stale timer releases a wedged host even when metering fails.
4. Stop then wake. The same logical host identity and durable node/world state return; a checkpoint hash alone is not accepted as proof of restored state.
5. A different owner cannot read, operate, or resume the event stream. Destroy is idempotent. Replaying the journal yields the same terminal status and audit event chain.

Acceptance should run entirely on a clone with fake/local providers and no cloud credentials. A separate opt-in EC2 test may prove adoption of a tagged instance and registered worker; it must not be required for the core suite.
