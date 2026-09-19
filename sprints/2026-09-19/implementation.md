# September 19 — agent grain implementation resumed

Ember explicitly authorized a new swarm to build **an agent grain platform**. This supersedes the earlier wind-down and bounded design-only mode. The current effort is the complete hosted Nous Hermes experience, with a persistent programmable DREGG resource world and initial hosted OpenRouter-key custody. Wisper's separately assigned networking work is outside this critical path.

## Selected receiving path

Astra's implementation choice is Mini's canonical native receiver for resource operations. The hosting code lives in `breadstuffs/agent-platform/hosted`, as the Python `dregg_grain` package. Python owns operational journaling, custody, transport and actual process enforcement; resource rules, grants, lifecycle transitions and budget acceptance come from source-authored Mini programs and the actual signed receiver. Upstream Hermes remains unmodified.

Normal disconnect closes input, fences the execution generation and stops the full owned Linux process scope. Physical interruption must not wait for a slow canonical request. The canonical trip is reconciled separately. Soft disconnect retains the same execution under existing authority and budget. A late result is evidence, not authority to resume; ambiguous paid work must not be redispatched. These are implementation obligations, not claims of completed acceptance.

## Coordinated ownership

| Lane | Files / receiving consumer |
|---|---|
| root | Platform composition, integration acceptance, hub records, scoped commits/pushes |
| resume_host | Mini host/context/replay, Main and actual bounded native link |
| resume_authority | Registry/profile pins, Book enforcement and observation controller/codec/audits |
| resume_genesis | Explicit native genesis and public CLI acceptance |
| grain_kernel | Source-owned grain/task policy and general declared-field transition projection |
| host_json (Sol) | Mini source-owned JSON authoring/inspection and detached signature codec |
| grain_tools (Sol) | Thin actual native client, retained exact attempts, scoped MCP resource tools |
| grain_control | Durable operational control registry, authenticated local ingress and CLI |
| grain_runtime | Actual upstream Hermes PTY/session supervision, Linux confinement and interruption |
| grain_broker | Encrypted provider-key custody, scoped tokens, bounded dispatch, evidence and recovery |

There are at most two local Lean compiler processes. Current hbox measurements show substantial ACL2 load and memory use; only bounded lightweight runtime tests go there, under `/tank`. Persvati has measured memory/disk capacity for an isolated, claimed and bounded native C build. Historical machine-role notes do not override current measurements.

## User-journey acceptance

1. An authenticated friend provisions a persistent grain backed by actual signed Mini resource birth.
2. They enter real upstream Hermes, ask it to create/read/program/invoke a DREGG resource, and retain the accepted native receipt.
3. A second authority receives a narrower grant and can exercise exactly that grant; current rule revisions and deliberate management lockout retain their agreed meaning.
4. A normal connection drop fences broker/tools and stops all local descendants; retained output and uncertainty survive restart, and reconnection cannot replay an ambiguous paid operation.
5. An explicit soft connection detaches and reconnects to the same running scope under unchanged authority and budget.
6. The scoped broker uses a host-custodied credential only after native acceptance, retains exact request/attempt/response evidence, and refuses unsupported proof requirements or unbounded provider spend.
7. The service and native store restart, reconstruct their retained identities, and finish reconciliation without inventing a successful external effect.

Component tests are useful progress, but this journey remains open until executed. No new full-system STARK assurance, TLSNotary request certificate, public deployment, live provider spend, or on-chain economic operation is implied by this checkpoint. Those are separately owned implementation/selection obligations.
