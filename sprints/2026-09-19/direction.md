# September 19: hosted Hermes and durable protocols

This records ember's current product direction and the questions being investigated. It is conversation evidence, not an implementation or deployment result. It updates the September 18 plans without changing their captured results.

## Accepted direction

**Offer a complete hosted Nous Research Hermes Agent experience.** Ember clarified:

> ah yes i did also mean a complete hosted hermes experience, when they log into the server (via ssh?) they would get a hermes experience that we host on our resources, that we can meter how we do.

SSH is a suggested entrance, not a selected protocol. The enduring product intent remains a programmable DREGG resource world for friends and the Discord community. Hosting Hermes must connect to that world and its actual kernel/shell operations. The exact first shared activity is still open.

**Support external unforked Hermes if practical.** This is additional to the complete hosted experience. Ember suggested remote control of an agent grain and is considering ACP, A2A, MCP or a custom interface, leaning custom. No protocol has been selected. Breadstuffs' `deos-hermes` is intended to integrate with Nous Hermes; the locally available upstream checkout is `~/pug/hermes-agent`.

**Bring an OpenRouter key; hosted custody is acceptable initially.** Asked whether a DREGG credential service may hold the user's OpenRouter key while Hermes receives permission to request its use, ember answered:

> Yes—hosted key custody is acceptable initially

Ember wants TLSNotary plus parsing certificates to substantiate that submitted requests followed authorized user inputs: a verifiable provider. This is a desired assurance, not a claim that current components establish it. In accepting hosted custody, ember was explicitly told that TLS evidence does not prevent the custodian from making unrecorded requests. Exact credential-use authority, request construction, evidence requirements and accounting remain design work.

**Operate the intended semantics before complete STARK assurance.** Ember wants to offer and run the system's semantics while full STARK assurances remain incomplete. This does not select a kernel or establish that either current implementation is ready. Source authorization, actual operations, persistence and host isolation still need their real receiving paths. A proof-shaped artifact must retain its exact statement and assumptions.

**Wisper's assignment has changed.** Ember reports:

> I set Wisper to work on a specific low-level networking thing so he won't be doing the thing we discussed, he'll be focused on something outside our critical path.

The earlier cloud/resource-host lifecycle brief remains useful unassigned design work. It is no longer Wisper's planned assignment or a dependency on his availability. The networking task's details were not supplied in this conversation; do not invent its scope or completion state.

## Cadence and current operating constraint

As of September 19, ember would ideally have a runnable demo in about three to four days, September 22–23, leaving time to iterate before September 26. Release days on the 13th and 26th maintain momentum and audience engagement; ember explicitly says they are not a big event. This is a desired schedule, not a promise that a chosen scope has been estimated or completed.

Implementation remains wound down while the laptop is busy with the separate `~/dev/fn` session. Ember authorized a few Sol agents for bounded repository exploration. The current work is read-only investigation and lightweight project-record maintenance; no build, deployment or implementation wave was restarted. The [September 18 wind-down](../2026-09-18/wind-down.md) remains the latest captured implementation checkpoint.

## Assistant proposals still under discussion

- Treat a grain as a durable DREGG resource, distinct from its host process, login connection and individual Hermes conversations.
- Specify DREGG authority, commands, operation identity, persistence/recovery, budgets and evidence independently of the chosen client transport. ACP could adapt Hermes conversations, MCP could expose DREGG tools, and SSH could provide a hosted interactive entrance. These are candidate roles, not an accepted protocol stack.
- Bind credential-use authority to an explicit request construction: model and routing policy, conversation/context inputs, tool definitions and requested limits. Bind evidence to the authenticated exchange and the result actually consumed. A syntax certificate alone does not establish authorized construction.
- Separate inference charges, host resource measurements and DREGG operations. Retain the source and assurance of each measurement rather than presenting all usage as cryptographically proven.
- Give external operations durable request and attempt identities, including an explicit uncertain outcome after response loss. Retry behavior must not silently duplicate paid work.
- Exercise a real hosted agent creating/programming a resource, delegating a narrower right to a friend, having the friend's agent use it, and returning after restart. This is a proposed acceptance journey, not a selected demo or a passing test.

## Questions for the source investigations

1. Which grain/session/control and persistence paths actually exist, and which would receive these operations?
2. How much of hosted and external unforked Hermes can use upstream configuration, ACP and MCP today? What still needs a DREGG adapter or real host isolation?
3. What do the present TLS and parsing certificates bind, and where must authorization, exact request bytes, retries and consumed results be connected?

These investigations inform the durable protocol design. They do not choose Bread versus Mini by name or infer readiness from old documentation.

## Foreground work pauses on disconnect (revised September 19 preference)

Ember initially selected continuing the current task within its budget, then explicitly withdrew that answer:

> actually i regret that answer. if something wasnt launched explicitly backgrounded, a disconnection event should interrupt/*pause* ongoing processing but it should resume when they reconnect? wdyt?

The current preference is therefore: foreground agent work pauses when its controlling connection disconnects and resumes when the user reconnects; only explicitly backgrounded work continues unattended. The earlier keep-going answer is superseded. Pausing an agent task does not itself stop hosting the underlying DREGG resources.

Assistant recommendation, with exact mechanics still to design: stop dispatching new inference/tool work, request interruption of active work where supported, and retain its durable task/operation state. Already-dispatched external work can finish or remain uncertain; preserve its outcome and charges, and reconcile before retrying. Reconnection to the same task rechecks current authority and remaining budget before continuation. A bounded transport-loss detection interval, single controlling attachment, and explicit durable background-task designation belong in the lifecycle contract. This is stronger than merely replaying a conversation transcript and is not yet implemented or tested.
