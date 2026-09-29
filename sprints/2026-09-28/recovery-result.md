# Recovery construction result — September 28

Evidence for the 22:40–00:10 UTC recovery batch. A fresh two-participant resource
journey and actual fn receiving ran; this is not deployment qualification or
completion of Gates A–C.

## What changed

The common Mini resource client now owns a participant workspace: named
references, authenticated inspection, source-authored operations, retained
submission and exact recovery. Named references remain hints. A narrower
delegation is authored from same-image resource, policy and parent-capability
observations and still faces Mini admission. Hermes uses the same client
contract, rather than a separate implementation of resource semantics.

Participant enrollment now has Lean construction, native receiving and replay,
plus a client that retains the sponsor request and new key's proof of possession.
Enrollment admits a signing key only. Durable namespace reservations coordinate
controllers under one operator UID; they neither grant rights nor establish a
globally authoritative allocator.

Ordinary birth has a source-owned current-image authoring route. Checked signed
API paths replace the Git-only consumer restriction. Versioned SPK package and
launch codecs preserve historical Git bytes while admitting other checked
prefixes. The signed sntfy package supplies a materially different consumer.

Actual fn format 8 and current format 10 probes exposed a protocol mismatch:
their retained reports are `fn-r`, while the existing Mini coverage path expects
`fn-e`. A separate, explicit transport-only receiving path uses fn's own
`consumer-article` decoder and Mini's signed selected-release admission. It
does not fabricate coverage evidence, advance event-17 coverage, or ACK delivery.

## Candidate and evidence boundaries

- Mini `e22d16b` is the corrected native runtime candidate. The preceding
  `81b740b` native build failed at module 321 because importing the new package
  codec made an old unqualified `codecV2` reference ambiguous. The corrected
  build reuses the last qualified baseline, not the failed build as a falsely
  successful cache. A separate failed invocation used a nonexistent baseline
  output path; that was a build-driver error, not a source failure. The corrected
  build passed all 363 Lean modules and native linking at 23:49:37 UTC. Host ELF
  SHA-256 is `723940446d3e0256bd446b07ca8d67ea9d67295d8c7cc78e08bb2487ffbe3db2`;
  source and artifact manifests passed readback checks. Runtime results below
  are separately scoped to their recorded clients and fixtures.
- Mini `bae39a8` is the first qualified Linux common client; `0007925` adds
  named delegation with exact attempt binding and requires observation rights
  in references intended for a receiving workspace. Its qualified Linux ELF is
  SHA-256 `3e9cb1ca488995a0a591ea6db8f9b4b6b59d9629782daf6babb294620c74513d`.
- Mini `f4d27d1` carries the updated Hermes consumer, including verified
  pre-submit refusal recovery with zero tool charge. `bdf6e73` adds the focused
  regression: the real recovery method consumes fixture refusal artifacts;
  missing or changed evidence leaves the operation pending. The 141-test
  component suite passed. This is not a native fault-injection journey.
- Source enrollment checks include proof-of-possession, sponsor/current-law
  refusal, duplicate identities, no implicit grant, and cold native replay.
  See Mini's `docs/evidence/2026-09-28-participant-key-enrollment/`.
- General SPK codec proofs and explicitly reported compiled finite checks live
  in Mini's `docs/evidence/2026-09-28-spk-profile-codecs/`.
- Real Store workspace inspection, policy change, resource operation and exact
  recovery ran against the older September 19 Host. That demonstrates client
  compatibility; it does not qualify the new enrollment or current-birth routes.
- Sntfy's signed package was parsed, materialized and inspected on hbox. Source
  author/inspect checks produced package-v2 and launch-v3 descriptors; Git's
  historical package-v1 bytes remained exact. The actual native `qualify-launch`
  path then passed against the qualified Host, producing the same package and
  launch bytes as the source checks. This joins signed parse to source-authored
  descriptors; it remains pre-Store, not INSTALL, START or a running application.

## Actual same-Store participant journey

The corrected Host and final client have now admitted a fresh newcomer through
the public socket on a fresh one-sponsor Store. Namespace allocation selected
subject `9594942322447678104` and key ID `10489544371237092821`; no newcomer
genesis edit or operator socket was used. Plan, seal and submit took 2.427,
0.546 and 0.807 seconds respectively, with accepted count 1. This is actual
key enrollment; resource rights were granted separately in the following steps.

On that same Store, the sponsor's ordinary `workspace create` then passed through
the current-image op91 route, using automatically allocated target and capability
IDs after the enrollment event. It installed accepted record 2 in approximately
4.2 seconds for this workload. This is not a comparison with the substantially
different historical ordinary-birth workload or a broad latency qualification.

The sponsor then used a named-reference proposal to delegate only observation
and mutation to the newcomer (record 3). The receiving workspace imported the
published reference, performed a signed read, and used its own newly enrolled
key to create scalar field 2 with value 1 (record 4). Signed readback returned 1.
Exact delegation lookup returned the historical transaction/event pair.

After stopping and reopening the same private server with the same pinned
binaries, enrollment lookup returned the same receipt in 0.317 seconds and the
newcomer's signed read returned field 2 = 1 in 0.713 seconds.

Finally, ordinary sponsor policy control installed deny-all law (record 5).
The newcomer's current read and the owner's attempted repair through the common
surface were refused at signed observation. These were observation refusals,
not fabricated direct management-submit tests. Exact recovery of the previous
newcomer operation still returned record 4's successful receipt. The fixture
retains the deliberately locked resource. See Mini's
`docs/evidence/2026-09-28-newparticipant-runtime/` for receipts and boundaries.

## Remaining connection: independent creation provisioning

The current genesis factory's object grant permits observation but not
delegation. Its program grant permits policy control and revocation, not
delegating an object grant. Enrolling a new key therefore does not yet give
that participant the factory observation and payer rights needed for independent
resource birth. Allocating IDs or changing a client configuration cannot fix it.

A sponsor-created ordinary resource with a delegable grant can support shared
use by the newcomer. Independent creation needs a designed provisioning path:
either a fresh bootstrap profile with explicitly delegable factory observation,
or a source-owned factory-management provisioning operation for existing Stores,
plus an account/funding path. Neither was silently added to make the fixture pass.

## Actual selected exchange through fn

The qualified e22 Host carried one selected atom through a fresh actual format10
fn node to recipient Mini event13 admission. Exact retry returned the same
receipt as replayed without another submission. A separately authorized signed
query found the exact packet in one recipient atom. The selected payload occurred
once; the fixture's unrelated source atom was absent from the packet. Wrong-root
admission and altered expected-article checks refused at their recorded boundaries.

This run had separate Stores but one owner credential; it did not qualify an
independently credentialed friend. It made no fn-e, event17 or cursor ACK claim.
The orchestrated final `verify-transport` phase refused because it passed the
wrong authoring kind. `ef64f97` fixes that one-line client bug and passes focused
checks; the fixed wrapper was not rerun end to end. The recorded successful
readback used the original pinned client's ordinary signed query. The fn lane's
client has its own recorded binary pin, distinct from the participant client.
See Mini's `docs/evidence/2026-09-28-selected-exchange/`.

## Recovery and sharing cases found during review

The controller can propose and submit a delegation, but its MCP surface does
not yet export the recipient reference. The common CLI owns publication and
recipient import. A confirmed submission alone does not establish another
Hermes grain's discovery or use.

Review also found that a stale factory observation can produce a retained op91
refusal before any birth call, leaving same-name create stuck on the old reply.
That is a pre-submission recovery case, distinct from an uncertain admitted
operation; any repair must preserve exact custody once a call exists. This
source-reviewed liveness case remains unimplemented and runtime-unqualified.

The native controller/MCP fixture encountered a stale managed worker-generation
policy after its intentional hard stop. The exact-law guard refused attachment;
ordinary signed owner repair installed generation 2 law. Controller recovery
then installed generation 3 law and admitted attachment, reaching soft idle.
The following resumed agent command stopped on a missing Hermes configuration
file before ACP/MCP prompt, so no workspace MCP mutation was qualified. This
is operator-assisted partial recovery. The fixture used a deterministic agent;
neither a real Nous Hermes inference turn nor a complete hosted session ran.
The exact boundary is recorded in Mini's
`native/grain-runtime/RESOURCE-WORKSPACE-EVIDENCE-2026-09-28.md`.

## Integration and deployment remain separate

The preserved r3 INSTALL refusal was not retried. No token movement, public
deployment, existing live Store repair, or inference spend occurred. Recipient-specific deployment communications are kept outside Git. Persvati
and hbox are development/build machines, not the intended homelab. Homelab
placement has not been inventoried or selected in this batch.
All new private resource, fn and controller test services were stopped after
evidence capture. Their Stores, exact calls and receipts were retained. Unrelated
working-tree changes and the preserved live fixture were left intact.

Next, complete independent creation provisioning and the actual hosted-agent
consumer of these same resources, including restart and refusal recovery.
Hosting needs lifecycle reconciliation and the second package through that path.
Selected exchange needs independently credentialed receiving, the corrected
orchestration rerun and explicit transport/cursor compatibility. Mechanical
operation-family lifecycle/dispatch coverage remains a separate unimplemented
work package; individual source and runtime positives do not establish it.
