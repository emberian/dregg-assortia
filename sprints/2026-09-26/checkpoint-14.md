# Construction checkpoint — September 27, 00:38 UTC

The autonomous Mini/fn construction goal remains active. This follows
[checkpoint 13](checkpoint-13.md) without changing its dated facts. The
three newly captured journeys use separate fixtures and authority scopes:
two Unix accounts on one private Mini Store, a fresh Hermes stale-root
attempt, and an operator-assisted fn Q→A reply to the workroom R. Source
construction and a linked Host profile smoke are recorded separately from
those native results.

## Two Unix accounts, one native resource Store

Mini commit `8d29aa2` records [signed cross-UID native use](https://github.com/emberian/minidregg/blob/8d29aa2/docs/evidence/2026-09-26-mini-cross-uid/README.md)
on a fresh four-principal Store. One operator-owned private Mini Host, two
operator-owned per-task frontends, and distinct UID 65534/UID 1 client
accounts used separate keys, configs, attempt directories and sockets. The
fixed ordinary client `d52077e` sent image-pinned v2 envelopes; the earlier
version-one pre-forward refusal in checkpoint 13 is not counted as native
authority evidence. UID 65534 signed-created content atom 7401 at accepted
count 10; UID 1 signed-read its new root and edited it at count 11. Both
then signed-read the same final root. Each cross-used the other's read
capability and received signed observation refusal with no view. Neither
could read the other's key/config or traverse the operator's private Store.

The [manifest and selected receipts](https://github.com/emberian/minidregg/tree/8d29aa2/docs/evidence/2026-09-26-mini-cross-uid)
pin Linux Mini Host SHA-256 `d413081bb6c6ac1c0699b5fdc22cf3a13fb87930ff49ac147ae994e2c364e7a3`,
ordinary client `fee5bc861d74c9e432db2374ede36b62852a80346a46f1dc89133dfa79bf11eb`,
and final frontend `0675e61e6ae9517439f2eec29fa8c740c069f9f1f52e25e84ba463e6192140dd`.
Some lock/socket/ACL adversarial probes used earlier frontend source hashes;
the final source was directly exercised for the signed operations. This is
real native grant enforcement across two OS accounts, not yet two hosted
controllers, Hermes sessions, SSH entrants or independent backend tenants.
Dedicated `miniworka26`/`miniworkb26` accounts with private frontends have
since been provisioned for a further gate; no controller/Hermes result for
those accounts is included here.

## Fresh stale-root refusal and cleanup

Commit `61f4186` records a [fresh 8901/8902 Hermes native run](https://github.com/emberian/minidregg/blob/61f4186/docs/evidence/2026-09-26-pre-submit-refusal-native/README.md).
The tool retained a signed empty content root, the owner independently
created atom 7401, and the tool tried to create atom 7402 against its old
root. Host returned an exact 128-byte opcode-255 frame containing the
canonical Lean refusal `Reject.staleTarget` in phase `prepare`. The archived
signed observation, attempt manifest/config, frame and decoded outcome have
matching hashes; no `call.bin` or submit dispatch artifact existed. The
runtime then signed a zero-charge tool settlement and disconnect, accepted
at counts 15 and 16, leaving no pending operation or hold in the final
journal. The provider observed that refusal and cleanup. This is a
successful typed **pre-submit** refusal and release in this fresh fixture,
not a general transport-fault recovery and not a retrofit of hosted peer
B's earlier unresolved attempt 44.

## Workroom Q→A on fn

Commit `6828c7f` records [operator-assisted Q→A completion](https://github.com/emberian/minidregg/blob/6828c7f/docs/evidence/2026-09-26-workroom-content-reply/README.md)
for the same Mini workroom edit and R whose B inbox and ACK passed in
checkpoint 13. Mini's source-owned Q planner selected the accepted B
transaction and durably reread its prepared slot; its signer durably reread
the signed slot. An initial signer invocation using local rather than hbox
secret-key paths failed with `transport-fault` before retaining a carrier;
the next invocation reopened the same prepared slot and signed with the
qualified generation-2 keyset. Both qualified fn nodes accepted Q, and
native HDR reported its verified identity. No second R was posted.

A's first catalog poll encountered its own R. The operator harness required
the exact retained R Message-ID and directly ACKed that cursor, then A's
next typed poll proposed Q at fn sequence 5. **No accepted Mini tag-9 skip
preceded the own-R ACK**, so this is not a crash-safe automatic progress
decision. A signed Mini transaction accepted Q at count 4; typed op15
returned `fnAck: durable-accepted` for fn Store 5/5. The accepted result,
inbox, retained Q cursor/event and signed A target-600 view reopen and
match the independently verified Q source and A origin correspondence.
The currently linked Host's generic A view still labels entries `other`
with a B-oriented interpretation. New `Host.FnInboxView.render` source
decodes schema 10/6/7 on that retained signed view as origin outbox,
reply result and reply inbox, but this typed A renderer passed only a
module-level source probe; it is **not linked into the public Host**. A
transported accepted upstream content edit was checked through R, B, Q
and A provenance; A did not locally edit that upstream content resource.

## Provider and composite boundaries

The committed [`567fa58` provider source](https://github.com/emberian/minidregg/blob/567fa58/Kernel/ProviderMetering.lean)
owns strict parsing, tariff and bounded quote over provider-**reported**
usage. A new native Host build has been reported with a profile smoke, but
its bounded build evidence is not yet published; no op19 receiving journey,
invoice authentication, hosted provider settlement or paid usage is claimed.
Composite birth's current source/proof work has not yet produced an
accepted native joint birth/settlement/witness call. Unstaged source under
construction is not counted as this checkpoint's evidence.

Next gates are the dedicated-account controller/Hermes test, source-matched
read-only op19 quote and usage settlement, native composite birth, and a
source-owned crash-safe own-R skip before automatic A progress. Hosted
peer B's old held attempt still needs its separate disposition. Whole-prefix
fn agent release remains an unselected design proposal, not an implemented
sharing authority.
