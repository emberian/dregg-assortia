# Homelab preview: intended service shape

Dated September 28, 2026; construction is in progress.

**Audience:** Pug and Wisper, as a request for an outside read. This is an
orientation to the intended homelab service and the current design boundary; it
is not an assignment, an operator runbook, or authorization to deploy. Please
point out where the topology, trust boundaries, or lifecycle assumptions do not
fit the machines and services we actually have.

## The service we are aiming for

DREGG is intended to be a programmable resource world that friends can share.
People and agents should be able to create and govern durable resources, compose
their operations, delegate narrow rights, and use the same resources through
more than one interface. A hosted Nous Hermes agent is a central interface, not
the product by itself. Bounded SPK applications should eventually run as
instances within that world. Selected public resources or versions may move
between participants through `fn`, which is treated as a semi-untrusted
transport.

The semantic authority belongs to Mini: authored rules and the native receiver
decide whether a signed operation is admitted. Rust clients and services perform
custody, communication, and process work around that authority. A name, URL,
MCP tool, or successful transport receipt must never grant access on its own.
Installing an application version is a separate authorized operation from
receiving or publishing its bytes.

## Logical topology

The intended request path is:

1. A participant enters through a user-facing session, potentially SSH, a
   browser, Discord, or an agent interface. The final first entrance and public
   protocol have not been selected.
2. A foreground Hermes session interprets the request and calls bounded tools.
   Those tools use the common Mini client path rather than inventing per-family
   semantics or selecting authority from a user-visible name.
3. The client authors and signs an exact request; Mini's native Host checks
   current rules and authority and records the accepted operation in the
   relevant durable Store. Retries look up the original attempt and receipt;
   they must not turn an uncertain result into a fresh admission.
4. If authorized, an SPK instance runs under its own lifecycle and resource
   rights. The host controls package, process, and volume custody; Mini remains
   the source of semantic admission.
5. For sharing, a publisher selects bytes or a version under Mini authority.
   `fn` may carry that selection and return a transport acknowledgement. The
   receiving side still verifies and admits it. A transport ACK is not proof
   that Mini accepted content or that an application may execute it.

This is a logical decomposition, not a claim that these components currently
form one service. In particular, the captured r3 boundary has real package
materialization but refused INSTALL completion at claimed count 29. It did not
produce an installed, running shared application journey.

## Principals, keys, and state

The intended authority chain distinguishes the human participant, the
participant's signing identity, the hosted agent/session, the operator, and any
host provider. A delegated capability should name its scope and be admitted by
Mini; enrollment IDs or allocated capabilities are not grants. A shared
application does not become owned by the operator merely because the operator
runs its process.

Signing keys authorize exact requests. Provider credentials authorize inference
requests and must stay behind the provider-custody boundary. Ember has accepted
initial hosted custody of OpenRouter keys as a product direction, while BYO
keys and locally hosted inference are also desired. That custody path, account
ownership, secret isolation, metering, and user-visible disclosure are not
qualified as a joined service here. Never put credentials in this document or
in an app's ordinary resource state.

State has distinct owners:

- Mini's signed history and Store are the authority for admitted resource
  changes and original operation receipts.
- Host lifecycle records own install/start/stop attempts and their recovery.
- An SPK instance's durable volume belongs to that instance's custody contract;
  it is not interchangeable with the Mini authority Store.
- A Hermes conversation/session and provider settlement have their own
  retention and recovery rules; they do not replace resource history.
- `fn` retains transport/release information only within its contract. It is
  not authoritative for Mini grants or private history.
- Source packages, manifests and selected public releases have provenance and
  version identities separate from runtime state.

Backup and restore must preserve these identity boundaries. A copied database
or volume is not automatically a valid restored service: recovery must check
source identity, exact history, current authority, pending operations, and
whether external effects already happened. The backup schedule, retention,
encryption, restore drills, and recovery-point objective are open operator
decisions.

## Foreground work and service lifecycle

The settled interaction preference is circuit-breaker behavior: ordinary
foreground Hermes work should stop when its participant disconnects. An
explicit soft attachment may let work continue under the authority and budget
already granted. Background work would need its own explicit status, authority,
and budget. A participant disconnect must not stop a shared SPK service used by
other people. Nor does returning a cancellation response prove that a child
process or external effect actually stopped; physical interruption and effect
reconciliation still need qualification.

The host should distinguish durable shared services from disposable foreground
workers, and should preserve uncertain outcomes for exact recovery. Restart,
reconnect, provider settlement, and service adoption each have separate
lifecycles. This document does not choose the final supervisor, containment
mechanism, or service manager.

## Network boundaries

SSH is an intended possible entrance, not a confirmed public interface. Hermes
has an MCP-facing tool surface in source, but its current deployment/configuration
is not established here. A browser entrance, Discord interface, HTTPS listener,
TLS termination point, and public hostnames all remain to be selected and
qualified. Do not infer that a source-level route is externally reachable.

The intended private side contains Mini's native Host and Store, signing and
provider custody, SPK lifecycle control, instance volumes, and administrative
access. Public or participant-facing endpoints should expose only authenticated
session and application operations. Exact firewall rules, network segmentation,
operator access, host-to-host trust, and TLS/key rotation need an explicit
deployment design; this overview does not claim those controls are in place.

## Machine placement is still a proposal

Place logical roles before assigning machines. A useful future deployment may
separate a CPU-oriented build/coordination role, a Mini authority and durable
Store role, an inference/GPU role, and SPK execution/volume custody. These roles
can share a physical host only with an explicit resource and failure-boundary
decision.

Persvati is a candidate for CPU/build work. Hbox and its `/tank` storage are
candidates for GPU inference and larger persistent data; a local Ternary Bonsai
2 27B inference target has been considered and measured separately. Neither
candidate assignment establishes the final service placement or a joined
hosted Hermes deployment. The September 28 Persvati cleanup removed old Lean
compilation caches; it did not stop services or validate a deployment. Three
older Mini Host processes were observed alive during that cleanup, but that
observation does not qualify them as a usable public preview or as the service
to adopt.

The current implementation batch is WIP: it is adding a common Mini workspace
CLI/Hermes tool path, durable identity reservations for same-operator
controllers, generic signed API paths with explicit Lean v2/v3 profiles, and a
selected-version `fn` exchange consumer. The native runtime-principal enrollment
receiving path was identified as missing and is being implemented. None of
these pieces has integrated qualification yet. The current r3 INSTALL refusal
and checkpoint records remain the concrete deployment boundary; source work,
component checks, and old live processes do not establish a running shared
service.

## What is not authorized by this preview

Real $DREGG stake and provider penalties are future product work. The intended
devnet concept is to lock real stake while recording penalties rather than
deducting them, but custody, eligible jobs, adjudication, withdrawal, and
deployment remain undecided. No token movement, paid inference spend, public
deployment, user onboarding, or private-history publication follows from this
document. These choices need explicit product and operational decisions.

## Questions for Pug and Wisper

This is an invitation for review, not a work order. Useful feedback would be:

- Which logical roles should be separate, and what placement constraints do
  Persvati and hbox actually impose?
- What should the first user entrance expose, and where should authentication
  and TLS terminate?
- Which service/session lifecycles or recovery boundaries are missing from this
  model?
- What backup and restore guarantees would make a small shared preview
  operationally credible?
- Which parts of this proposed trust boundary are impractical for
  participant-operated hosts?

Ember has authorized the current [90-minute construction batch](../sprints/2026-09-28/recovery-construction.md). Its owned lanes are implementing and qualifying these connections; this document is the deployment discussion, not a report that they already form a service. The source map and its proposed receiving consumers are in
the [September 28 recovery miniswarm](../research/recovery-miniswarm-2026-09-28.md);
the [September 27 platform reorientation](../research/platform-reorientation-2026-09-27.md)
and [project handoff](../HANDOFF.md) preserve the reviewed system boundary and
dated evidence. The [payment/inference audit](../research/payment-inference-2026-09-27.md)
and [Persvati cleanup record](../research/persvati-cleanup-2026-09-28.md)
describe those narrower scopes.
