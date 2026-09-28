# Recovery construction result — September 28

Working evidence record for the 22:40–00:10 UTC batch. Final runtime results
will be added before handoff. This is not deployment qualification.

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
  output path; that was a build-driver error, not a source failure.
- Mini `bae39a8` is the first qualified Linux common client; `0007925` adds
  named delegation with exact attempt binding and requires observation rights
  in references intended for a receiving workspace. Its native qualification
  is a separate artifact from the first client.
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
  historical package-v1 bytes remained exact. These are pre-Store checks, not
  INSTALL, START or a running application.

## Important remaining connection: participant provisioning

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

## Recovery and sharing cases found during review

The controller can propose and submit a delegation, but its MCP surface does
not yet export the recipient reference. The common CLI owns publication and
recipient import. A confirmed submission alone does not establish another
Hermes grain's discovery or use.

Review also found that a stale factory observation can produce a retained op91
refusal before any birth call, leaving same-name create stuck on the old reply.
That is a pre-submission recovery case, distinct from an uncertain admitted
operation; any repair must preserve exact custody once a call exists. Final
source/run status for this counterexample belongs in the qualification record.

## Integration and deployment remain separate

The preserved r3 INSTALL refusal was not retried. No token movement, public
deployment, existing live Store repair, or inference spend occurred. Recipient-specific deployment communications are kept outside Git. Persvati
and hbox are development/build machines, not the intended homelab. Homelab
placement has not been inventoried or selected in this batch.

The next acceptance must join independent participant provisioning, common
human/Hermes operations, current-law refusal, and cold recovery on one pinned
candidate. Hosting needs actual lifecycle reconciliation and a second package
through that path. Selected exchange needs independently credentialed receiving
and explicit transport/cursor compatibility, beyond a successful article POST.
