# One full typed request codec — source-only proposal

Status: reviewed against current source after the 278ed6a checkpoint. No repository source edited. The byte-preserving full codec and actual artifact/native compatibility laws now pass isolated /tmp proof checks; see `/tmp/dregg-full-request-codec-draft-check.json` and `/tmp/dregg-request-compatibility-draft-check.json`. ParentLink and Request representation changes remain held until root release after the current receiving/native checkpoint. Names below are implemented in scratch only, not in the shared repository.

## Decision and concrete scope

Extend the existing `Compiler/TypedAuthorizationRequestCodec.lean`. It will own the sole full `AuthorizationDeclaration.RequestWire` word projection, exact inverse, canonical stream, dependent `SomeRequest` stream, and a fixed-kind view. Reuse the actual `AuthorizationDeclaration.encodeRequest`, `decodeRequest`, resource-kind tags and global verb tags. Do not add another request record or semantic authorization relation.

The first patch is byte-preserving extraction only:

1. Authority owns additions in `Compiler/TypedAuthorizationRequestCodec.lean` and named universal codec laws.
2. Carrier owns or explicitly releases the narrow forwarding change in `Compiler/DeclaredHyperedgeArtifact.lean`.
3. Native owner owns or explicitly releases the narrow forwarding change in `Compiler/CredentialSignatureAdmission.lean`.
4. No changes to Theory.Request, RequestWire fields, Family, State, page formats, native signature verification, or runtime profile identity in this extraction patch.

The dependency remains acyclic: low request codec imports `Compiler.Tower256ConcreteBackend` plus `Theory.AuthorizationDeclaration`; neither imports authority Entry/Domain, Artifact, ResourceBirth, SignatureAdmission, or a receiving controller. The artifact and native admission then import the low codec. Entry already imports it.

## Existing representations and exact byte contract

`Theory.AuthorizationDeclaration` already owns the full dependent request projection. Its current `RequestWire` has 16 natural-valued coordinates in this exact order:

`domain, semantics, federation, resourceKind, subject, subjectKeyEpoch, target, verb, argsDigest, effectsDigest, nonce, height, preStateRoot, policyId, policyEpoch, cost`.

`Compiler.DeclaredHyperedgeArtifact.requestWords` currently spells that projection out. `Compiler.CredentialSignatureAdmission.requestBytes` prefixes `DREGG/AUTH/REQUEST` UTF-8 followed by byte 1 to `(StreamCodec.list StreamCodec.nat).encode` of those words. Preserve this equality universally for every `SomeRequest`; a few golden vectors are supplementary evidence only.

The low codec's existing `requestStream` / `requestCodec` is a different object-only transport used by HyperdocumentCodec: 15 compact scalars, no resource-kind coordinate, no list-count prefix. It is not the native full-request encoding. Leave that public transport ABI and its current bytes unchanged during extraction; document it explicitly as the object transport and never use it for a delegated origin. This is one existing transport of `Request .object`, not a competing full `SomeRequest` format. In particular, its total fallback object-verb decoder must not be reused as the new typed request parser.

## Proposed API in the existing low module

```text
requestWords          : RequestWire -> List Nat
requestWireOfWords    : List Nat -> Option RequestWire
requestWordCount      : Nat
requestWireStream     : StreamCodec RequestWire
requestWireCodec      : LawfulCodec RequestWire
someRequestStream     : StreamCodec SomeRequest
someRequestCodec      : LawfulCodec SomeRequest
requestStreamFor      : (kind : ResourceKind) -> StreamCodec (Request kind)
requestCodecFor       : (kind : ResourceKind) -> LawfulCodec (Request kind)
requestFrame          : List UInt8
signedRequestBytes    : SomeRequest -> List UInt8
```

`requestWords` is moved, not copied. Its inverse has the sole exact-length record reconstruction. `requestWordCount` and the field-order correspondence theorem relate this to the existing `requestFieldOrder`; downstream consumers do not reproduce a literal count. The current exact inverse necessarily handles 16 words. A future field addition changes this one boundary and its proofs.

`requestWireStream.encode` is exactly the existing length-prefixed natural list encoding. Its decoder rejects a count different from `requestWordCount` before decoding that many fields, reconstructs the exact wire, and checks canonical consumed bytes. The raw wire codec accepts any well-formed raw RequestWire value, including unrecognized numeric kind/verb tags, because RequestWire itself is untyped data; this does not construct typed authority.

`someRequestStream` calls the existing partial `decodeRequest`. Unknown kind tags and unknown or wrong-kind global verb tags fail. No default verb, fabricated request, arbitrary caller decoder, countable encoding, or permissive fallback participates. Canonical prefix acceptance requires `input = encode(request) ++ returnedSuffix`, rejecting primitive-natural aliases as well as malformed/trailing whole messages. `.toLawful` then requires an empty suffix.

`requestStreamFor kind` is only an indexed view of `someRequestStream`: encode packages the actual kind; decode checks the recovered kind, transports the dependent request only after that equality, and otherwise refuses. It does not write a second field list. The kind coordinate stays in the encoded payload even when the outer consumer already knows its kind.

`signedRequestBytes request = requestFrame ++ someRequestStream.encode request`. `requestFrame` keeps the exact current UTF-8 marker plus byte 1. The outer `DREGG/AUTH/SIGNED-REQUEST` domain and existing SignedEnvelope header codec are unchanged.

## Required general laws before consumer cutover

- `requestWireOfWords_requestWords`: the exact raw word inverse for every RequestWire.
- `requestWireOfWords_exact`: a successful inverse returns exactly the input words; wrong arity refuses.
- `requestWords_injective` and `requestWords_length = requestFieldOrder.length`.
- `encodeRequest_of_decodeRequest`: successful typed decoding reconstructs the exact original wire. Prove against the existing strict Theory kind/verb decoder, not a new tag mapping.
- Prefix roundtrip for raw wire, SomeRequest, and every fixed kind, for every suffix.
- Canonical prefix acceptance and whole-message accepted-byte re-encoding, including primitive aliases and appended bytes.
- Full typed request encoding injectivity across resource kinds; exact request-field separation follows from it.
- Fixed-kind mismatch and invalid-kind/verb refusal.
- `artifact_requestWords_exact`: the forwarding artifact projection is universally equal to its current word order.
- `native_requestBytes_exact`: forwarding native request bytes are universally equal to the current frame plus exact length-prefixed 16-word payload. Existing request-injectivity and checked-receipt laws then delegate to the shared law.
- Existing object-transport encoding and its original stream composition laws remain unchanged.

Use named theorems and existing axiom accounting. No golden vector, compiled decision, hash-injectivity premise, or bare runtime assertion substitutes for these laws.

## Consumer forwarding

`DeclaredHyperedgeArtifact.requestWords` becomes an abbreviation/forwarding definition to the low codec, retaining its current API name and exact artifact bytes. Its length theorem forwards to the shared count theorem. Artifact schema version and generated outputs should remain byte-identical in extraction.

`CredentialSignatureAdmission.requestFrame` and `requestBytes` become forwarding definitions to the low source. Its current `requestWords_injective` / `requestBytes_injective` names may remain compatibility theorem aliases. It no longer needs to reach into the higher artifact layer merely to obtain the full request representation. The checked receipt, selected committed key, native verifier process, frame binding, exact nullifier and actual request authentication remain unchanged.

`PolicyInstallController` currently consumes artifact requestWords for its request digest. The preserved artifact API/bytes keep that consumer unchanged in extraction. Later it may call the shared low source directly as a narrow dependency cleanup, with the same equality obligation.

## ParentLink consumer after representation release

The approved semantic owner introduces `LineageOrigin kind = strict | delegated (Request kind)` and `ParentLink kind = { parent : Capability kind, origin : LineageOrigin kind }`. `CredentialAuthorityEntryCodec` then composes the existing capability codec with an explicit origin tag and `requestStreamFor kind` for the delegated payload. It serializes the actual stored type; no parallel lineage or out-of-band signature table.

The request is the historical source-derived delegation operation. The codec proves exact data preservation, not historical authorization. The mandatory family mode contains the actual exact-parent capability authorization; the shared lineage checker verifies mixed lineage shape and canonical parent/suffix anchoring. Recipient invocation uses the recipient's current native key and does not reauthorize an old grantor signature against today's key.

The stored representation change requires page wire 3 -> 4, full authority state wire 2 -> 3, the actual authorityShard registry schema 91003/v3 -> v4, and matching root/customization/catalogue/runtime pins. Reject old bytes under the new identity; do not relabel the live new stream as a historical decoder. The next-catalogue example derives its next authority version from the pinned current version and will advance coherently. Physical catalogue wire syntax need not change merely because listed shard roots change; inspect its actual payload rather than inventing a blanket version bump.

Universal new laws must show full stored-capability roundtrip/injectivity and distinguish strict versus delegated origin and every request coordinate, plus wrong-kind request refusal. Outer canonical page/state decoders remain exact and globally routed. Move any necessary structural DecidableEq instance to the agreed foundation owner when ParentLink lands; do not leave a second conflicting instance in the codec.

## Possible policyRevision wave is separate from extraction

The proposed revision/generation split would add a seventeenth request coordinate. No such field or default is added now. If root releases that change together with ParentLink, the shared Theory wire, this one full codec/inverse, request frame version, containing authority carrier versions, declaration/emission pins, receiving projections, and native/replay probes change in one coherent wave. An old request must refuse under the new frame; missing revision is never interpreted as zero. Existing object-only transport consumers also require an explicit versioned migration when the underlying Request changes, not silent extra-field reuse.

Do not conflate AuthorizationDeclaration's current schema version 3 (which also commits verifier vocabulary) with the native request frame's current version 1 or authority page version 3. Each identity tracks its actual contract.

## Check and ownership order

After release, one two-thread focused seat checks the low codec first, then the two narrow forwarding consumers in dependency order and their source pins. Owner-coordinated native signature and declared-resource smoke probes verify unchanged wire interoperability; preserve actual source/binary/check hashes. No umbrella or shared representation refresh is part of extraction. Root owns full closure and Git.

The scratch full codec and compatibility files emitted no oleans and changed no repository source. The ParentLink composition sources under `/tmp/dregg-authorized-delegation-draft/Compiler/` still require the isolated new Family/State closure. Current compiler handoffs are tracked separately by the coordinator, not frozen into this design document.
