# Construction checkpoint — September 27, 01:00 UTC

The autonomous Mini/fn construction goal remains active. This follows
[checkpoint 14](checkpoint-14.md), which remains an immutable snapshot. Three
separate committed Mini evidence sets now advance hosted peer use, provider
quoting and A-side inbox presentation. Their Host images and Stores are not
one combined deployment.

## Two dedicated accounts, one hosted workroom

Mini `2c455a4` records the [fresh two-account unforked Hermes workroom
sequence](https://github.com/emberian/minidregg/blob/2c455a4/docs/evidence/2026-09-26-cross-uid-hermes/README.md).
Separate `miniworka26` (UID 1001) and `miniworkb26` (UID 1002) workspaces,
frontends and keys used one operator-owned private Mini Store and content
resource 8001. A deterministic loopback provider selected tool calls through
unmodified upstream Hermes ACP; no external model API or application-side
workroom Store participated. The operator retained the full signed attempts
privately; the committed pages are selected projections of signed views.

A created atom 7401 at accepted count 15 and independently signed-read its
root. B signed-read that exact root, edited the atom at count 23, and
signed-read the new root. The original A Hermes session loaded again with
`loadVerified:true`, read B's exact root, and reconciled the atom at count
31. A and B then independently signed-read the same final root and
byte-identical view (SHA-256
`692b69da1b11e6b8c853eaa9f2d1ca3d0178f76c007b4ee8d8783c5eff05df3f`).
The accepted tool outcomes retain all four native receipt fields. Both final
journals have no child, pending call, hold, settlement due, prompt or
unresolved external effect; hosting observed fenced empty cgroups. The
successful model-visible `mini_publish` tool text is a task/root
acknowledgement, while the separately retained native outcome carries the
historical publication receipt.

The [bounded manifest](https://github.com/emberian/minidregg/tree/2c455a4/docs/evidence/2026-09-26-cross-uid-hermes)
pins Mini Host SHA-256
`d413081bb6c6ac1c0699b5fdc22cf3a13fb87930ff49ac147ae994e2c364e7a3`,
client `fee5bc861d74c9e432db2374ede36b62852a80346a46f1dc89133dfa79bf11eb`,
runtime `27cc1b4766a5b276a069345bffa581383c787c308352b5241216dd6b17bea176`
and upstream ACP wrapper
`d9b2b31dcce207f8397a7e1606a6d8586a25e661744b610340d83b2c0c25b7ee`.
This is actual same-session hosted peer resource collaboration with physical
cleanup. It does not mean these edits traversed fn, prove external model
behavior, or resolve the separate old hosted peer B attempt-44 hold.

## Read-only provider quote

Mini `0b56357` records [native op19 usage quoting and refusal
cases](https://github.com/emberian/minidregg/blob/0b56357/docs/evidence/2026-09-26-provider-metering-native/README.md)
through certified 171-module Linux Host SHA-256
`51f790fa55f734772c37330dc0ab7408f3438d4e168b74bd6432d0b1cdb111f6`
and client SHA-256
`fee5bc861d74c9e432db2374ede36b62852a80346a46f1dc89133dfa79bf11eb`.
An isolated copy of the gateway-r1 Store and its exact retained request
bytes were used; the original Store was not changed. Config pinned provider
7204, model `mini-hermes-protocol-fixture` and tariff version 1. A completed
SSE stream with terminal usage and `[DONE]` yielded a typed charge-3 quote
and source-authored settle operation under reserve 3. Unterminated `[DONE]`,
missing terminal usage, and a valid stream under reserve 2 each returned an
explicit opcode-255 refusal. The four bounded raw frames and typed quote
are retained in the evidence directory.

This is a quote over **provider-reported** usage, not an invoice or an
accepted Mini charge. No upstream request, signing operation, settlement or
paid usage occurred in this gate. Runtime still must bind the exact
request/response/header bytes, tariff/model, signed provider hold and parent
witness before ordinary Mini settlement admission. The work toward that
integration remains separate from this read-only result.

## Typed A inbox on the retained workroom reply

Mini `247e57e` qualifies [Mac and Linux typed-view Host
images](https://github.com/emberian/minidregg/blob/247e57e/docs/evidence/2026-09-26-mini-provider-typedview/README.md).
Each independently certified a 171-module source closure. A seven-module
suffix rebuild incorporated the one changed source, `Host.FnInboxView`;
the base pins an earlier
`Kernel.ResourceBirthController` blob, so this is not a claim that either
binary matches every file of Mini `247e57e`. The Mac Host SHA-256 is
`8e24573962ec54d81ecd6859dc2dd5b8158610f926401aa903a1ec6eb4ba7524`;
Linux is
`454b06489e9f1787124c91e881eeced9b3b95c0ece81c69a4113e67d3461e2de`.

The [read-only linked Mac Host presentation](https://github.com/emberian/minidregg/blob/247e57e/docs/evidence/2026-09-26-workroom-content-reply/README.md)
of the *same retained signed A view* renders `preparedOriginOutbox`,
`aReplyResult` and `aReplyInbox`. Its JSON exactly matches the earlier
module-only Lean probe, and all three entries share the accepted origin
receipt, operation and R identity; the inbox carries the exact signed Q
source and fn Store sequence 5. The original Q admission/ACK used the
separately qualified core-only Host and did not run again here. This suffix
neither migrated A's live Store nor created a new Mini transaction.

Automatic own-R cursor progress is still pending: the retained Q→A run
directly ACKed A's own R through an operator harness, without an accepted
Mini tag-9 skip. New own-R source and client changes have not yet passed
their native gate. Metered runtime recovery, native composite birth and
agent-controlled fn release likewise remain construction work. The
public-history release design has not become contributor consent or an
implemented sharing authority.
