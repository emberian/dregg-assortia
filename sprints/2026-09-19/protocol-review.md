# September 19 protocol review

Three bounded Sol investigations, reviewed by Astra. **Source inspection only:** no project builds, tests, provider calls, services, deployments or implementation changes. The [direction record](direction.md) distinguishes ember's choices from proposals. The [September 18 checkpoint](../2026-09-18/wind-down.md) remains the latest captured execution evidence.

## Findings that change the design

| Question | Source-supported result | Remaining obligation |
|---|---|---|
| Can we host upstream Nous Hermes? | The inspected checkout has persistent session state, CLI/ACP entry points, MCP clients and configurable provider endpoints. A version-pinned, unmodified Hermes inside a persistent isolated grain is a plausible architecture. | Exercise the actual full hosted journey, including interruption/reconnect. Provider overrides, auxiliary calls, subagents and fallbacks need route-specific acceptance; the main base URL alone is not complete metering. |
| Does Bread's grain service already give us that host? | It provides session carriers, logical rent/budget rules, tool admission and adapters. Its platform registry, lease carrier and local node are held in memory. `wake_from_lease` needs the retained tenant. | Durable grain discovery, store/workspace/custody mappings, restart recovery and operation reconciliation are substantial implementation work. Current sleep/wake tests do not establish process-crash recovery. |
| Does a committed action turn establish tool completion? | The current path commits the kernel turn, draws a separate budget, executes the tool, seals a receipt and later checkpoints. | Define one durable admission/reservation decision and separately retain external results. A post-admission budget refusal or a lost tool response cannot become an ordinary no-effect refusal safe to repeat. |
| Do TLS and parsing certificates prove authorized provider use? | TLS machinery authenticates exchanges under its host/notary assumptions. Current higher-level adapters drop authenticated sent data; existing POST presentations omit request bodies. Response CFG establishes syntax. | Bind actual request bytes to authority and request policy, retain the request transcript, handle actual streaming/schema semantics, and distinguish that from proving how upstream Hermes constructed and consumed the exchange. |

Reports and exact source references:

- [Grain control and persistence](reports/grain-control.md), `/root/design_grain_control`, Sol.
- [Upstream Hermes and protocol edges](reports/hermes-edges.md), `/root/design_hermes_edges`, Sol.
- [Provider evidence](reports/provider-evidence.md), `/root/design_provider_evidence`, Sol.
- [Source and artifact inventory](inventory.json): repository revisions, inspected-source hashes and copied report hashes. These identify inspected bytes, not passing builds.

Root independently re-read the platform constructor/wake path, the action loop's admission/budget/effect sequence, upstream provider resolution and ACP load/resume/cancel, and the request-dropping TLS adapter/disclosure/render verifiers. Other detailed findings remain attributed agent source reviews, including explicitly labeled inferences. Reports are proposals where they recommend future architecture.

## Proposed division of responsibilities

Specify the DREGG meanings first: stable grain identity, kernel authority, exact operation identity, durable outcomes, recovery, budgets and evidence. The host supervises the physical realization of that resource. A service role or SSH login must not create an owner-management bypass; resources can deliberately govern and lock their management under the accepted policy decision.

Then project those operations into adapters:

- SSH can provide the hosted interactive entrance.
- ACP can drive Hermes conversations and stream their UI/tool events.
- MCP can expose DREGG operations to either hosted or external unforked Hermes.
- A custom DREGG control interface can express resource lifecycle, operations and evidence that these adapters do not define.

This is a proposal, not a frozen protocol selection. It does not require inventing a new transport. The lasting contract is the meaning of operations and retained results across implementation changes. The request/result codec, profile, identity and authorization rules must be versioned; a replacement implementation cannot silently reinterpret existing signed operations.

Keep these objects distinct: DREGG grain/resource, human principal, host process, workspace, Hermes conversation, active task, provider request attempt and actual tool operation. One person may own several grains; one grain may have several conversations. A reconnect is not a new resource, and a new provider attempt is not a harmless retry of an already completed operation.

## The new pause requirement

Ember's revised preference is foreground pause on disconnect and continuation on reconnect, with continued unattended work requiring explicit background launch. This should apply to the controlling attachment of the task, not to any spectator or unrelated connection to the grain.

Proposed task transitions:

```text
Running foreground -> Pause requested -> Paused -> Reconcile -> Running foreground
Running background -> continues under its own authority, budget and stop conditions
```

`Pause requested` immediately prevents new dispatch. Already-dispatched work is interrupted where the runtime supports it; otherwise its result or uncertain status is retained without advancing the agent into another step. Reconnect may arrive while interruption is still in progress. It must join the same task and wait for a safe continuation boundary, not start a second driver.

This is not yet guaranteed by upstream session storage. Current ACP `cancel` signals an interrupt and retains an interrupted prompt in process state; `load_session`/`resume_session` restore and replay conversation history. Neither inspected operation establishes durable suspension and exactly-once continuation of arbitrary tools. Furthermore, upstream `resume_session` creates a new session when the requested one is missing. A DREGG continuation must check the returned identity and explicitly report missing state instead of accepting a silent replacement. Sources: upstream `acp_adapter/server.py:1129–1222`, `acp_adapter/session.py:169–183`.

A small grace/detection interval may absorb transport flaps, but its duration and spending semantics remain open. Foreground inference/tool spending stops as the task quiesces; retained storage and already-authorized hosted resources have separate lifecycles and costs. Reconnection rechecks authority, rule revisions, expiry and budget. Explicit background designation needs durable scope and cancellation, including whether spawned child jobs inherit it.

Acceptance must cover disconnection before dispatch, after a provider/tool accepts work but before its response, during streaming, and after result persistence but before display. It must also cover reconnect during pausing, host restart, two would-be drivers, a missing Hermes session, and grant/budget changes while paused. The outcome must be retained progress or an explicit unresolved operation, never silently repeated paid work.

## Evidence and credentials

Initial hosted custody is accepted. A separate credential broker can hold the raw OpenRouter key and issue a narrow, revocable token to the grain. Its enforcement and metering must include every enabled inference route; upstream configuration alone is not isolation or complete accounting.

Two proposed assurance scopes must stay distinct:

1. **Delegated request-policy conformance:** authenticate the actual exchange and check that its request matches the granted destination/model/input/tool/budget constraints. This still requires new integration.
2. **Full construction and consumption:** establish that the complete upstream Hermes state produced those exact request bytes and consumed that exact response/event sequence into its next state. A broker or JSON certificate alone does not establish this. The old internal `dregg-agent` parser is not the upstream Hermes consumer.

TLS to OpenRouter identifies the gateway exchange under the selected notary trust; it does not prove opaque model inference or complete key-use accounting by an adversarial custodian. Preserve exact evidence scope in the resource result. Evidence required by an operation cannot silently degrade when notarization or parsing fails.

## Next discussion

The strongest architectural direction is one durable, kernel-governed resource service with replaceable Hermes/client adapters. The exact kernel choice is still open. Mini's measured authority/resource journey is valuable, while its compiled public host remains unfinished; Bread has broader consumers and concrete service machinery, with the recovery and effect-ordering gaps above. Neither name settles the receiving path.

Before a new implementation wave, select that receiving path and freeze the operation, pause/recovery and credential-use meanings needed for one actual hosted-agent journey. Completing these semantics is core product work even while succinct proofs remain incomplete. The current source review estimates no delivery date and claims no deployment readiness.
