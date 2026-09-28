# Recovery miniswarm — September 28

Ember supplied the external recovery brief and requested a mix of Sol and Luna
to review it. Three Sol lanes reviewed resource contracts, hosting, and operation
lifecycles/publication; two Luna lanes reviewed navigation and acceptance.
The lanes read source and retained evidence. No new implementation, builds,
acceptance runs or deployments occurred. Root corrected hub navigation/state
to reflect the already established review mode; this does not adopt the
proposed construction contracts below.

Source basis: Mini committed `4e5d674`, Bread `c4fb8e9c7`, Assortia `35136d7`,
with separately owned Mini WIP present. References below are paths within Mini
unless noted. Existing evidence retains its own source/image identity.

## Proposed work packages and receiving consumers

| Package | Existing mechanism and consumer | Manual coordination to replace | Closure that resists another fixture |
|---|---|---|---|
| Common resource operations | Native client author/query/prepare/sign/submit/lookup; CLI and Hermes consume the same semantic requests | Copied IDs, roots, grants, intent JSON and bespoke MCP family configuration | Two independently onboarded people and Hermes author rules, compose resource operations and exercise narrow delegation; an additional resource created after implementation needs no numeric-ID selection or platform edits |
| Participant namespaces and references | Checked kernel birth, controller birth custody, existing application references/catalog | Operator-reserved per-participant ranges and copied shared-reference config | Concurrent controllers reserve identities durably, collisions refuse safely, restart neither reuses an uncertain reservation nor invents an accepted birth; names never confer authority |
| Hosting reconciliation and routing | Existing INSTALL/START/STOP custody records and resident/volume adapters | Per-instance install/resident config scripts and Git-specific forwarding transforms | Independent instances plus a qualified non-Git profile use one ordinary mechanism; interrupted effects recover exactly or explicitly remain unresolved |
| Operation-family completeness | Source author kinds, codecs, Host dispatch, replay and client command definitions | Remembering which operation has which historical decoder or recovery route | Mechanically checked coverage plus runtime lifecycle cases for exposed families; unsupported versions refuse and exact lookup never becomes fresh admission |
| Selected publication consumer | Existing selected publisher/release custody, event14 source authority, event13 receiving and fn progress | GitWeb-specific export/join orchestration | Two independent Stores exchange selected content through real fn, with disclosure, tampering, destination, duplicate and uncertain-POST cases |

The first two packages share an interface boundary and must not independently
invent incompatible resource handles. Hosting and publication consume those
identities but retain their own operation-specific recovery rules. One
integration owner must pin the coherent candidate and qualify Gates A–C.

## Source-grounded contract boundaries

**Resource operations.** `native/resource-client/src/main.rs:972–1150` already
authors and retains intents, obtains signed observations and source-authored
Plans, signs exact headers, retains `call.bin` before submission and provides
current queries; historical retry starts near line1191. Extend this consumer.
`Compiler/NativeObservationCodec.lean:18–48` is the current typed intent/read
boundary. The friendly operation descriptions must remain source-owned rather
than a second Rust semantics. Client-side composition proposes effects; it
does not acquire authority by computing them.

`native/grain-runtime/src/shared_app_refs.rs:120–152,392–482` supplies useful
reference/provenance behavior; its separate reads are not one coherent
snapshot. Admission must still join actual state and current permissions.
`resource_tools.rs:327–349` and `application_tools.rs:30–107` use configured
ranges plus ordinals. Namespace provisioning is genuinely additional work,
not a renamed existing kernel allocator. A shared transaction over several
resources is also distinct from multiparty co-signing: the current client
signs Plan headers using one local key. Gate A can exercise narrow delegation
between principals without claiming a new co-signing protocol.

**Hosting.** Do not introduce a competing operation journal. INSTALL v3
(`native/spk-host/src/install_v3.rs:375–700`), resident START
(`resident_service.rs:599–708,834+`) and STOP
(`lifecycle_v3_stop_service.rs:1154+`) already own exact attempts and recovery.
The common path should derive or index instance placement/configuration against
these authorities, dispatch an applicable existing operation, and report
uncertainty. A new durable binding is justified only for a fact not already
derivable from admitted identity and custody. No blind generic retry loop.
Foreground disconnection must not become authority to stop a shared service.

The `/repo.git/` specialization crosses controller, host, materialization and
descriptor adapters; deleting a guard in `application_api_tools.rs` alone is
not a generalization. Extend the signed path mapping and its exact request
comparison through every consuming layer. The retained app-selection inventory
names sntfy with a root API prefix as a possible non-Git witness. Its package
qualification/native run remain unverified; this is a candidate, not an adopted
or deployed profile.

**Operation coverage and fn.** Derive coverage from actual definitions in
`Host/Json.lean:2073–2155`, `Host/Main.lean:1362–1481` and the replay/client
consumers. A handwritten opcode checklist would become another twin. The exact
generation mechanism still needs design; source search alone is not a gate.
`selected_publisher.rs:439–530` and `selected_release.rs:240–290` already retain
the relevant publisher/recipient custody. A general selected-version consumer
should call them, replacing orchestration in `scripts/fn-gitweb-preview/join.sh`.
Keep historical receipt recovery distinct from present authorization, and fn
ACK distinct from Mini admission. Receiving content does not authorize executing
it or installing an app version.

## Acceptance and cost

Gate A must include user-authored supported laws and composed operations, not
only preselected family names. Gate B needs both additional instances and a
materially different profile. Gate C needs unrelated private source material
that is demonstrably absent from the selected carrier. Across gates, changed
law/revocation, lost reply, cold recovery and refusal state must be observable.
An explicit unresolved outcome is preferable to a duplicated effect, but is
not evidence of seamless recovery.

Checkpoint68's 418.68-second birth and 241.01-second cold lookup describe their
private pinned workload. Checkpoint76 separately records a persistent-session
birth improvement from158.229 to80.972 seconds with identical receipts/Store.
Neither qualifies interactive latency of the future integrated candidate.
Measure stages, history growth, warm/cold behavior and supported contention
on that candidate; do not substitute increased timeouts for performance work.

## Navigation correction and next discussion

The immediate correction uses existing graph work states and blockers. The
recovery review is current; old construction next actions are deferred behind
it, with original next actions retained in the graph for reassessment. Historical
checkpoints and their hashes remain unchanged. A structured mandate/context-pack
generator is a later hub improvement, not a prerequisite for platform work.

Next discussion: accept or revise the common operation/reference/namespace
boundary and choose a coherent construction batch. Gates A–C and the packages
above remain proposals; this review does not authorize live retry, funding,
deployment or a new implementation swarm by itself.
