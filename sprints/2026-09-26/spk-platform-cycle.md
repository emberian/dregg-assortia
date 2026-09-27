# SPK application platform cycle — September 27 UTC

Ember cleared the previous goal after a four-hour retrospective, then requested a
new goal that makes substantially greater use of the Sandstorm-compatible SPK
platform: existing apps provide both human web views and APIs agents can share.
Publishing versions through fn is part of the intended direction. The new goal is
active. Previous implementation lanes stopped safely; their WIP and scoped results
remain preserved. This record supersedes the overnight brief's assignment list,
not its evidence or the unfinished obligations in the graph.

## Outcome and acceptance

Deliver one coherent installed platform using the actual Mini kernel/runtime,
reusable Bread SPK machinery, unforked hosted Nous Hermes, and semi-untrusted fn.
Two separately authorized participants must be able to work with the same real
third-party application grain through its browser UI and agent API, discover and
operate resources through direct commands, delegate bounded access, and return
after restart/disconnection. Use a real model in the integrated acceptance, with
the hosted custody/metering contract. Select and exercise actual packages rather
than substitute the in-process notes demonstration.

Explicit version publication must transfer selected application releases or grain
data versions across fn without exporting unrelated private history. Receiving an
article does not authorize installing code, changing app state, or granting access.
Record source-qualified integrated evidence, deployment instructions and a portable
handoff. Prior independent fixture successes do not establish this acceptance.

## Grounded starting points

Read-only inspection used Bread `3e2506c8bc0c3cc650c21f15cd23e9ae434e86ca`,
Mini `700d6ba` plus preserved WIP, and DreggNet-pub
`6e948dc4fe9ddefe559f3268f79384c17d1415d5`. No package was executed by this
inspection, and no fresh crate-wide pass is claimed.

| Component | Inspected implementation | Construction needed |
| --- | --- | --- |
| Bread `sandstorm-bridge/src/spk.rs`, `capnp_wire.rs` | Signature/hash verification, bounded decompression, archive decoding and packing | Reuse in actual package ingestion; test against third-party artifacts |
| Bread `sandstorm-bridge/src/manifest.rs` | Catalog Cap'n Proto manifest, action/continue commands; bridge port inferred from argv | Separate bridge configuration, roles and APIs must be decoded/consumed; catalog path currently defaults permissions empty |
| Bread `sandstorm-serve/src/{custody,serve,body}.rs` | Exact-package custody, capability-aware serving, checkpoint before response; `NoBody` and `DemoNotesBody` | Packaged executable, filesystem and full app transport integration |
| DreggCloud `grain-serve` | Operated wrapper around the same serving code | No independent packaged-app implementation found in this wrapper |
| DreggNet-pub `sandstorm-bridge/src/exec_workload.rs` | Runs a hardcoded Python notes handler through the old executor; catalog test uses that handler | Does not execute the package's own program; do not import this as the missing executor |
| Mini native grain runtime | Hosted Hermes, terminal, physical worker supervision and signed resource tools | Application hosting and web/API entrance through Mini admission |

Bread body source SHA-256:
`ed341c1c0e672b03e0f530bf64f6de5e09ae200c6212353ff7d6cb33ee7a1b66`.
Manifest source SHA-256:
`9fbbcc91f1e9209cdda4bc38a7a1b8e8d19bee84a1ac0fda9bdb7fb99e82678d`.
Local third-party specimen: DreggNet-pub
`sandstorm-bridge/fixtures/sample.spk`, SHA-256
`5830d70137cdae158118884da8790870fb095a07996cfe7708fb0155df45232e`.
Historical tests identify it as Simple Todos; fresh package inspection is assigned.
Its presence is not evidence of a useful HTTP API or successful launch.

Upstream contracts to implement/reuse rather than infer from the local facade:
[HTTP APIs](https://docs.sandstorm.io/en/latest/developing/http-apis/),
[powerbox](https://docs.sandstorm.org/en/latest/developing/powerbox/),
[package schema](https://github.com/sandstorm-io/sandstorm/blob/master/src/sandstorm/package.capnp),
[grain schema](https://github.com/sandstorm-io/sandstorm/blob/master/src/sandstorm/grain.capnp).
Pin an exact upstream revision before implementation. URL path prefixes do not
substitute for permission enforcement. Do not assume every packaged app exports
every interface or that a package-format parser implements Sandstorm RPC.

## Proposed integration contract — not yet implemented

Mini owns application lifecycle, current grants, request authority, package/version
commitments, and publication decisions. Rust owns physical custody and execution.
Bread's `dga1_` verifier is not automatically equivalent to Mini's current typed
capability checks. Existing package/wire mechanisms are reuse candidates; semantic
decisions must use Mini admission rather than a second Rust rule implementation.

A long-lived application resource must be distinct from a user's paid AgentGrain
attempt. Human browser sessions, direct commands and agents designate the same app
resource, with their own subjects and delegated rights. Package installation,
initialization, wake, checkpoint, upgrade and shutdown need source-owned operations
and durable physical reconciliation. Reuse existing declared-resource transactions,
birth, grants, exact attempts and receipts where they satisfy the actual contract.

Every request delivered to an app is external execution, including HTTP GET,
unless an app-specific observational contract is established. Authorization must
bind the exact request, resource, generation and current grant. Delivery of bytes
followed by a lost reply remains uncertain; do not automatically resend a mutation
or infer rollback from a disconnected socket. App-supported idempotency can supply
stronger recovery evidence where actually implemented.

A hard Hermes disconnect fences that session's authority and stops its owned
request/tool processes. It must not implicitly kill a shared application or another
participant's work. Application shutdown is a separate authorized operation.
Already dispatched app effects may need reconciliation after the agent is stopped.

Legacy app databases and files are real external state. A snapshot commitment
records exact retained state and provenance; it does not prove the app's internal
business logic. Build consistent durable snapshots and bind them through Mini.
Keep app-release identity, data-version identity and publication authority distinct.
Complete selected-release receiving; a public-only full-history fixture is not the
product substitute for selective publication.

## First assignments and convergence

Root owns architecture, integration, graph, commits and the installed acceptance.
Sol `spk_compatibility` reads upstream/runtime requirements;
`spk_app_probe` inspects the real package and candidate APIs;
`mini_app_contract` maps the existing native authorizers to application operations.
These initial tasks are read-only or isolated artifact inspection. Implementation
ownership follows a grounded contract; previous paused lanes are not silently
restarted. No new shared service or untrusted package process is launched by this
brief.

The next implementation should close real SPK execution and app interface discovery
alongside Mini lifecycle/dispatch admission, then converge continuously through the
same installed app. Performance, persistent hosting, selected fn release, and the
unfinished hosted resource-creation path remain core work. Existing evidence stays
scoped to its original executable and Store.
