# Checkpoint 20 — parallel journeys and receiving core

Recorded September 27, 2026, 04:59 UTC. This follows [checkpoint 19](checkpoint-19.md)
and the [parallel journey contract](parallel-journeys.md). Current ownership is
in the graph. No integrated public service is established by this checkpoint.

## Committed Mini changes

| Revision | Result and evidence scope |
| --- | --- |
| `2c34802` | Dispatch candidate separates app/manifest/enrollment observation from session mutation witnesses. It remains a candidate, not execution authorization. |
| `2e60a9c` | Typed application and session birth JSON authoring passes an executable Lean source check. Exact-source native Host build is still running; no new native birth result yet. |
| `60f0b76` | Portable signed GitWeb package/interface evidence. Real GitWeb execution is being qualified separately. |
| `f308bfa` | Fresh two-subject native application acceptance harness, syntax and ShellCheck green. Checks independent signatures, observe-only delegation, exact native refusals, unchanged logical image and original historical receipt after reopen. Not yet run against the new Host. |
| `d12faf1` | Hosted provider configuration accepts `maxIterations` from 1 through 6, preserving default 6. Five focused nextest tests and strict all-target clippy passed. This is a configuration bound, not evidence of a paid-model run. |
| `15ae0b0` | Canonical ordered permission schema, role resolution and denied/ceiling properties pass direct Lean checking. Resolution alone grants no authority. ViewInfo authoring and dispatch bit binding remain integration work. |
| `b6373d7` | Selected public-release ingress, native owner-signature/current-law admission, durable CAS receiver and exact retained-event retry selection pass narrow independent Lean checks. Native Host/Replay routing and actual fn transport remain under construction. Private recipient-only mode is refused until confidentiality exists. |
| `3d97102` | Preserves completed terminal FIFO-close fix and framed-output probe. Historical physical hard/soft disconnect evidence retains its old exact runtime identity; the new probe separately verifies stale completion handling and escaped model output. |

Implementation and evidence are in [Mini](https://github.com/emberian/minidregg).
Each revision names its own scope; none upgrades an earlier fixture into a
combined service test.

## Design corrections governing integration

Participant-owned enrollment cannot establish an app permission ceiling.
Sharing needs app-issued authority admitted with current app law and exact
ticket birth, then checked independently of the participant's requested role.
Each ticket has a separate resource rather than consuming one of four entries
in a shared content page.

App start and session rebind increment their runtime generations. Durable share
tickets must not pin those generations, or normal wake/reconnect would revoke
sharing accidentally. Requests still check current generations for process and
session fencing. The first ticket design retains package/interface/schema
identity, so upgrade continuity remains a separate explicit design obligation.

The hosted real-provider path exists, but metadata-only inspection found no
`providerTask` configured on the active 7801, 7803 or 9301 controllers. Existing
Hermes evidence uses a local deterministic provider. A real-model run needs a
fresh qualified configuration and credential; no paid call occurred here.
The worker currently shares host networking. A private Unix gateway plus an
isolated worker network is being implemented, preserving the controller's key
custody, per-prompt token, native reservation and uncertainty handling.

## Next integrated evidence

Run the source-matched two-participant birth/recovery harness; qualify one
GitWeb push, exact guest fetch, browser view and persisted wake; consume the
role/share and lifecycle receivers in native dispatch; connect selected release
to native replay and existing authenticated fn projection; qualify the isolated
provider gateway before a real-model run. Keep these journeys converging on the
same Mini authority and persistent resources.
