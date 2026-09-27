# Parallel platform journeys — September 27

Ember clarified that construction should advance several substantial journeys
in parallel, with depth through the core as well as breadth of applications.
GitWeb is one integration path, not a replacement scope for the
[active platform goal](spk-platform-cycle.md). Current owners and state remain
in the graph; this document defines the acceptance structure.

| Journey | User-visible milestone | Required depth |
| --- | --- | --- |
| Shared applications | An agent pushes a project change; another participant reviews the same persistent GitWeb grain in a browser. A read-only participant can fetch but cannot push. | Signed package ingestion, actual process, exact Web/API transport, current Mini role authority, two subjects, restart and observed app state. Other packages exercise additional interfaces rather than inheriting this result. |
| Programmable resources | Participants create resources and sessions from the shell, inspect them, delegate bounded access, change rules, and revoke a grant. | Source-owned birth, current signed authority, atomic state changes, grants preserved across policy revision, deliberate management lockout, exact historical receipts after reopen. |
| Hosted agents | Real-model unforked Hermes uses the same governed resources under a user budget and returns to its session after disconnect. | Key custody, exact provider/model selection, durable reservations and settlement, tool supervision, hard interruption, explicit soft continuation, and uncertainty after external effects. A deterministic provider remains a component fixture. |
| Hosting and recovery | An app persists independently of any one agent; operators can install, wake, stop and recover it with an inspectable lifecycle. | Mini pending operation and current claim, exact image/process generation, bounded physical host, checked host report with its trust boundary stated, and no blind repeat after an uncertain result. |
| Publication between nodes | A participant explicitly publishes selected project content or an app/data version, and another node receives it for separately authorized use. | Source authorization for the selected bytes, no unrelated private-prefix disclosure, durable sender/receiver state, fn treated as semi-untrusted transport, and separate receiver import/install authority. |

These journeys should converge repeatedly. A grant that allows an agent to
write a shared app must mean the same thing after reconnect and after package
restart. Publication should take the version produced by actual work, not an
unrelated export fixture. A recipient node must retain its own authority to
accept and use received material. Latency should be measured on these paths:
cold start, warm request, reconnect, and retained-history recovery are distinct
workloads. Core improvements should preserve accepted history and current-law
checks rather than cache an old authorization decision.

## Immediate authority correction

The reviewed dispatch candidate at Mini `2c34802` separates the session/agent
mutation witnesses from app/manifest/enrollment observation and stores a special
pending event. That separation is useful but **does not authorize app use**.
Session birth gives its participant control of the enrollment descriptor;
therefore its selected role cannot establish the participant's permission
ceiling. An app observe grant plus a self-edited `allAccess` enrollment would
be an invalid authorization design.

The next receiver must establish app-issued sharing authority independently of
that request: a Mini-governed ticket or equivalent native issuance binds the
app, participant, interface/schema and permission ceiling. Its issuer must
have current app authority at the actual admitted issuance; constructing a
descriptor with an owner-looking identifier proves nothing. Dispatch checks
the current ticket/grant, resolves the requested role against the installed
schema, and refuses any effective bit above that ceiling. Ticket storage must
support more than four participants; adding one atom per ticket to a single
four-entry page is not a scalable design.

## Evidence and construction boundaries

[Checkpoint 19](checkpoint-19.md) records the actual Simple Todos process and
persisted wake, copied-Store historical birth repair, and candidate Mini source.
Mini `2e60a9c` subsequently adds typed application/session JSON authoring with a
passing executable source check; its full native build and two-participant
Store acceptance are separate gates. Mini `60f0b76` preserves signed GitWeb
package/interface evidence; it does not claim GitWeb execution. Current
construction includes native lifecycle admission, role resolution and app-issued
authority, private package qualification, real-provider readiness, and selected
fn release receiving. Their independent results must be joined and exercised
before any combined service claim.
