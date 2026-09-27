# Mini publication over fn: trust and disclosure contract

Status: **design investigation, not an approved protocol or implemented
assurance**. Read 2026-09-27 against Mini source at `0013189` and fn source
at `f23a5e46a`. This note separates Ember's explicit trust principle,
source-grounded consequences, and proposed implementation choices. It does
not change the dated
[construction checkpoint 15](checkpoint-15.md).

## Explicit user principle and derived security requirements

Ember explicitly clarified that fn is a **semi-untrusted transport** for
DREGG application content. Analyze the boundary assuming it may inspect,
alter, replay, reorder or withhold carried bytes. The following are derived
requirements for a private DREGG publication design, not separately settled
user choices: a Mini receiver independently decides admission; an fn POST
acknowledgement, Store cursor, retention claim, article signature or peer
statement is not a Mini operation result; release requires DREGG-governed
authority over its exact disclosure scope. If plaintext confidentiality from
the transport is required, it needs end-to-end encryption to authorized
recipients. Publishing evidence should reveal only bytes the release
authority covers, rather than treating authority over one resource as
permission to expose the current full-Mini-history package.

These requirements do not select an encryption suite, key protocol, release
capability, selective proof or public realm. A separate public realm is an
option to assess, **not** a required workaround or an automatic cure.
Nothing here asserts those mechanisms already exist or makes completion of a
STARK system a prerequisite for a soundly scoped first protocol.

## What current source actually proves and reveals

[`FnEvidence.exportPackage`](https://github.com/emberian/minidregg/blob/0013189/Kernel/FnEvidence.lean)
selects an exact signed call's historical receipt and serializes the seed
plus **every accepted record through its accepted count**. Its verifier
independently checks a pinned domain, semantics and genesis, replays all
those bytes through Mini, checks the receipt at the prefix tip, and looks up
the exact signed call. The codec is a bounded native-prefix v2 package; its
size ceilings do not remove information. `DurableReceiverCodec` includes
seed cells and accepted writes, guards, nullifiers, charges and events, which
can include unrelated resources' bytes. Current `GrainOriginSource.render`
requires a named settled grain, parent witness and nonempty publication,
then base64-embeds the **whole package**. A target selector is not a filter.
The [Mini disclosure note](https://github.com/emberian/minidregg/blob/0013189/docs/FN-PUBLICATION-DISCLOSURE.md)
records the exact retained fields and a concrete 139,470-byte package.

[`GrainOriginPreparation`](https://github.com/emberian/minidregg/blob/0013189/Host/GrainOriginPreparation.lean)
checks an operator's whole-prefix intent and independently verifies before
rendering; it expressly does **not** establish earlier contributors' consent
or a grant. [`FnOriginOutbox`](https://github.com/emberian/minidregg/blob/0013189/Kernel/FnOriginOutbox.lean)
binds the verified origin and exact carrier before local posting; it does
not authorize broader disclosure or assert fn Store admission. The
[`FnConsumerOperation`](https://github.com/emberian/minidregg/blob/0013189/Kernel/FnConsumerOperation.lean)
and [`FnReplyConsumption`](https://github.com/emberian/minidregg/blob/0013189/Kernel/FnReplyConsumption.lean)
types distinguish independently checked carrier bytes from a locally
authenticated fn poll and an accepted Mini inbox transaction. The fn
[architecture](https://github.com/emberian/fn/blob/f23a5e46a/docs/architecture.md)
itself distinguishes transport acknowledgement, retention and application
outcome, and says stored evidence is not authority. A signed fn article can
support author/carrier identity; it does not grant DREGG read, publication
or mutation rights.

Mini's [`NativeObservationController`](https://github.com/emberian/minidregg/blob/0013189/Kernel/NativeObservationController.lean)
checks a signed, current-policy capability for a requested observation, and
[`DeclaredResourceController`](https://github.com/emberian/minidregg/blob/0013189/Kernel/DeclaredResourceController.lean)
requires an observe capability on relevant resource targets. Those checks
limit a local signed view. They do not authorize disclosure of all other
seed and accepted records in a full-prefix package. A grain's
[`operation.command`](https://github.com/emberian/minidregg/blob/0013189/Kernel/AgentGrain.lean)
can atomically join its target with named publications; that authorizes
admitted target effects under current policy, not export of unrelated Store
history. The earlier [Mini release proposal](https://github.com/emberian/minidregg/blob/0013189/docs/FN-RELEASE-DESIGN.md)
addresses a *public-history* Store only and is not an accepted solution for
a private mixed workroom.

## Proposed application contract

Treat fn as an adversarial delivery and storage surface. It may duplicate or
delay valid bytes without forging them, and may present different histories
to peers; cryptographic identity and local Store claims remain conditional
on their explicitly configured keys/checkpoints and implementations. A
receiver should decode one versioned DREGG publication envelope, check
canonical bytes, author/signature and the pinned source claim, enforce
its **own** subject/capability/policy and freshness/idempotence rules, and
submit one ordinary Mini transaction. Invalid, stale, unauthorized,
conflicting or unsupported envelopes refuse without mutating Mini. A
missing article is a liveness failure, not evidence that no publication
exists. A local fn cursor ACK means only that the consumer progressed its
own fn read position; Mini processing requires its own accepted receipt.
Any optional fn peer signed checkpoint must be explicitly pinned and can
strengthen a named fn-history observation; it must not silently replace
Mini admission or guarantee global availability/non-equivocation.

For an outbound article, define an **exact release scope** before posting:
origin deployment and receipt/call; resource or realm identifier and its
versioned disclosure profile; exact released plaintext/ciphertext bytes or
digest and format; named publication target; intended recipients or
public/peerable audience; article source/carrier identity, Message-ID and
Newsgroups; release authority, current generation/policy, allowance and
durable accepted release receipt. Newsgroups is routing, not recipient
access control. The release decision must be a DREGG-authorized transition
bound to exact bytes, not a Rust flag, one-resource observe grant, local
filename or fn acknowledgement. Because the carrier is known only after
origin article preparation/signing, exact-carrier release is naturally a
second Mini transition before POST; the current public-history design note
describes that non-circular ordering. Retried posts retain the same carrier
and release identity. A lost Mini reply uses exact-call recovery; an
uncertain fn POST retains the attempt and cannot infer whether a peer saw it.

For private data, encrypt the application payload **before** passing any
article to fn. The proposed envelope should use an authenticated encryption
scheme with domain-separated associated data binding version, source Mini
deployment/receipt, resource/realm, operation, recipient-key set or epoch,
and intended release scope. Recipient keys must be enrolled through a
DREGG-governed authority path (or an explicitly weaker named external
authority), with subject-to-key binding, rotation, revocation and a
decision about old ciphertext after revocation. Decryption alone is not
Mini admission: the receiver still checks provenance, authority, replay and
current local policy. Encryption hides designated plaintext from fn peers
without the key; it does not hide headers, sizes, timing, recipient/group
metadata or any unencrypted proof/witness fields. Key custody and the
cryptographic security of the selected suite require their own evidence.

## Evidence boundary: choices and missing kernel work

The present full-prefix verifier cannot safely publish one resource from a
private mixed Store: it reveals other history before the target operation,
including potentially secret seed cells and policy/authority material.
Filtering records and replaying the remainder is not a valid shortcut.
Admission of the selected operation can depend on resource births, current
policy heads, grants, parent grain state, read guards, nullifiers and
cross-resource writes. The selected receipt is a claim about the complete
history used by today's verifier. The versioned alternative must state
**which dependencies were checked** and what exact bytes are disclosed.

| Construction choice | Honest claim | Kernel/verifier work still needed |
| --- | --- | --- |
| Predeclared public-history Store or realm | Existing full-prefix replay is independently checkable if every seed and prior record was authorized for that audience from inception. Encrypt payloads that still need recipient-only reading. | Enforce public-history charter and whole-prefix release authority from genesis; audit all record fields, not just content. A new realm inside one physical Store is not isolated by today's prefix codec. |
| Operator-attested private-to-public copy | A named operator asserts that released bytes correspond to private material; recipient can independently check only the public event and operator signature. | New versioned attestation and authority/allowance rule, exact private receipt commitment and bytes, public target admission, key and revocation policy. Do not label it independent Mini historical re-admission of the private source. |
| Selective resource/realm evidence | Recipient checks an origin operation and precisely disclosed dependency set without learning unrelated records. This is the stronger desired private-workroom claim. | New authenticated state/history commitments or witness relation, resource/realm boundary, dependency-closure rules for policies/grants/parent/read guards/nullifiers, versioned proof/certificate codec, source-owned verifier and soundness/refusal tests. A verifier that trusted a host statement alone would be an attestation profile, not this claim. |

A cross-Store release transition may be one implementation of the last two
rows. Its public event must bind exact private-source identity and released
bytes; merely copying data to a fresh Store proves only the fresh Store
event. A succinct STARK could later compress a well-defined relation, but
the relation, privacy boundary and native acceptance rule must first be
specified. This design does not assume an existing selective proof or wait
for full proof-system deployment before choosing a limited, honestly named
attestation or public-history profile.

## Open implementation questions and acceptance

The team can continue designing a selective resource/realm evidence profile
and testing private workroom cases under the semi-untrusted transport
principle without asking Ember to choose a weaker workaround. The table
above compares possible claims and their costs; it is not a forced product
choice among three mutually exclusive options. Open implementation questions
include the exact dependency closure, release policy and authority locus,
recipient-key governance, versioned evidence format, and where an
operator-attested fallback would be explicitly distinguished from independent
Mini verification. Further user input is needed only if a genuine product or
policy choice cannot be resolved from the existing direction. No chosen
mechanism can be inferred from the one-resource `mini_publish` grant or the
completed fn R/B/Q/A fixture.

For any selected profile, acceptance should include: an unrelated secret
record immediately before the authorized operation that never appears in
the released bytes; refusal on changed ciphertext, recipient set, audience,
source receipt or carrier; stale generation and revoked release-capability
refusal; independent receiver Mini admission despite fn replay/reorder or
equivocation; duplicate/idempotent handling and withheld-message liveness
classification; exact-call recovery after lost Mini replies and uncertain
POST without a second carrier; and a separately named cryptographic/key
custody gate. The public-history profile cannot pass the secret-record case
in a mixed Store—it must use a genuinely public-from-inception boundary or
the case correctly refuses publication.
