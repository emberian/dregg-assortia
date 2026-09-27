# Checkpoint 23 — native routes and integration boundaries

September 27, 2026. Continues [checkpoint 22](checkpoint-22.md). The five
[parallel journeys](parallel-journeys.md) remain the acceptance scope.

Mini [776ba59](https://github.com/emberian/minidregg/commit/776ba59) commits
native lifecycle BEGIN submission/lookup (22/23), selected source publication
submission/lookup (24/25), and historical native replay for both families.
Source-owned authoring constructs the publication signing header and assembles
the native envelope from a detached 64-byte signature. The client does not
invent a native envelope. Source authorization and external delivery remain
separate operations.

The route cut is Main `27352f02`, Replay `b408832d`, and source authoring
`1ccba9a6`. The build lane reports a passing private 22-module Lean closure.
Root observed the bounded native build process running on Persvati; no linked
binary or native acceptance result for this cut is claimed here. The snapshot
pins committed Host.Json `c198d393`, excluding subsequent composite-birth WIP.

## What the connected journeys still need

App sharing must authenticate original issuance from a verified prefix, then
check current authority for each dispatch. Review found that the committed
share source used genesis grant fields for later issuance; the correction uses
current issuer/policy epochs and height. That correction and its receiving
route are still under construction. Caller-supplied issue bytes are not a
historical admission witness. Participant access to the ticket itself also
needs a real grant.

Lifecycle BEGIN records pending work. A separate durable current claim must
bind its original authority and exact process generation before physical
launch. Introducing claim phases changes the authored policy AST; historical
BEGIN replay must preserve the exact old policy as well as recognize the new
version. No implicit owner repair privilege is introduced.

The physical app adapter is being connected to Mini-derived principal and
permission bits. Its fd3 RPC driver needs continuous servicing and one request
deadline across session creation and dispatch. An uncertain response must not
cause an automatic resend. GitWeb's earlier physical acceptance remains
separate from this Mini-authorized HTTP path.

The hosted Hermes lane reports a deterministic-provider read/publish/finish
run and physical hard-disconnect cleanup. Its follow-up signed query found
the parent still reserved after the harness stopped the controller too early.
Native interruption/recovery is therefore not yet qualified by that run;
bounded evidence and recovery are being collected. This is not real-model
acceptance.

Selected publication still needs durable sender state joining exact source
authorization, exact carrier bytes, fn POST uncertainty, and recipient
admission. A source receipt does not prove POST, and transport acknowledgment
does not authorize installation. Restricted source signing and the publisher
adapter are assigned together to close that gap.

The graph owns current assignments. Complete two-person browser/API usage,
real-model Hermes, and the integrated deployed service remain open. Existing
source/component checks must not be cited as that service.
