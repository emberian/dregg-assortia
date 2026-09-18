/-
# Compiler.TypedAuthorizationRequestCodec -- the common request, on the wire

`HyperdocumentOperations.Config` demands `LawfulCodec (Request .object)` and
nothing supplied one, which gates every carrier that needs a `Config`.

It belongs here rather than in `Theory/`.  Byte transport is a compiler
concern, the framework for it is `Tower256ConcreteBackend.StreamCodec` -- a
prefix codec carrying `decodePrefix (encode value ++ suffix) = some (value,
suffix)`, so sequential composition needs no delimiter -- and the neighbouring
tag codecs for resource kinds and verbs already live in
`SemanticTurnReceiptDescriptor`.  `Theory/` could not import any of it, which
is the correct reason it is not the home for this.

The whole construction is `xmap` over `nat` for each wrapper field, `product`
right-nested for the record, and `rfl` for the retraction, since structure eta
makes rebuilding a record from its own projections definitional.  Naturals ride
`StreamCodec.nat`'s base-255 little-endian digits, so the encoding is
logarithmic in each field.
-/
import Compiler.Tower256ConcreteBackend
import Theory.AuthorizationDeclaration

namespace Minidregg.Compiler.TypedAuthorizationRequestCodec

open Minidregg.Compiler.Tower256ConcreteBackend
open Minidregg.Theory.IndexedProgram
open Minidregg.Theory.TypedAuthorization
open Minidregg.Theory.AuthorizationDeclaration

set_option autoImplicit false

/-! ## Wrapper fields -/

def subjectIdStream : StreamCodec SubjectId :=
  StreamCodec.xmap StreamCodec.nat SubjectId.value SubjectId.mk
    (by intro value; cases value; rfl)

def policyIdStream : StreamCodec PolicyId :=
  StreamCodec.xmap StreamCodec.nat PolicyId.value PolicyId.mk
    (by intro value; cases value; rfl)

def federationIdStream : StreamCodec FederationId :=
  StreamCodec.xmap StreamCodec.nat FederationId.value FederationId.mk
    (by intro value; cases value; rfl)

def resourceIdStream (kind : ResourceKind) : StreamCodec (ResourceId kind) :=
  StreamCodec.xmap StreamCodec.nat ResourceId.value ResourceId.mk
    (by intro value; cases value; rfl)

/-! ## The one dependent field

`Verb` is kind-indexed, so at a fixed kind it is a finite tag.  The tags agree
with `SemanticTurnReceiptDescriptor.verbTag` on the object constructors, which
keeps one numbering in the tree rather than two. -/

def objectVerbTag : Verb .object -> Nat
  | .observeObject => 1
  | .mutateObject => 2
  | .delegateObject => 3

def objectVerbOfTag : Nat -> Verb .object
  | 1 => .observeObject
  | 2 => .mutateObject
  | _ => .delegateObject

theorem objectVerbOfTag_tag (verb : Verb .object) :
    objectVerbOfTag (objectVerbTag verb) = verb := by
  cases verb <;> rfl

def objectVerbStream : StreamCodec (Verb .object) :=
  StreamCodec.xmap StreamCodec.nat objectVerbTag objectVerbOfTag
    objectVerbOfTag_tag

/-! ## The request -/

abbrev RequestTuple :=
  Digest × Digest × FederationId × SubjectId × Nat × ResourceId .object ×
    Verb .object × Digest × Digest × Nat × Nat × Digest × PolicyId × Nat × Nat

def requestTupleStream : StreamCodec RequestTuple :=
  StreamCodec.product digestStream (StreamCodec.product digestStream
    (StreamCodec.product federationIdStream (StreamCodec.product subjectIdStream
      (StreamCodec.product StreamCodec.nat
        (StreamCodec.product (resourceIdStream .object)
          (StreamCodec.product objectVerbStream (StreamCodec.product digestStream
            (StreamCodec.product digestStream (StreamCodec.product StreamCodec.nat
              (StreamCodec.product StreamCodec.nat (StreamCodec.product digestStream
                (StreamCodec.product policyIdStream
                  (StreamCodec.product StreamCodec.nat StreamCodec.nat)))))))))))))

def requestTuple (request : Request .object) : RequestTuple :=
  ⟨request.domain, request.semantics, request.federation, request.subject,
    request.subjectKeyEpoch, request.target, request.verb, request.argsDigest,
    request.effectsDigest, request.nonce, request.height, request.preStateRoot,
    request.policyId, request.policyEpoch, request.cost⟩

def requestOfTuple (tuple : RequestTuple) : Request .object where
  domain := tuple.1
  semantics := tuple.2.1
  federation := tuple.2.2.1
  subject := tuple.2.2.2.1
  subjectKeyEpoch := tuple.2.2.2.2.1
  target := tuple.2.2.2.2.2.1
  verb := tuple.2.2.2.2.2.2.1
  argsDigest := tuple.2.2.2.2.2.2.2.1
  effectsDigest := tuple.2.2.2.2.2.2.2.2.1
  nonce := tuple.2.2.2.2.2.2.2.2.2.1
  height := tuple.2.2.2.2.2.2.2.2.2.2.1
  preStateRoot := tuple.2.2.2.2.2.2.2.2.2.2.2.1
  policyId := tuple.2.2.2.2.2.2.2.2.2.2.2.2.1
  policyEpoch := tuple.2.2.2.2.2.2.2.2.2.2.2.2.2.1
  cost := tuple.2.2.2.2.2.2.2.2.2.2.2.2.2.2

theorem requestOfTuple_tuple (request : Request .object) :
    requestOfTuple (requestTuple request) = request := rfl

def requestStream : StreamCodec (Request .object) :=
  StreamCodec.xmap requestTupleStream requestTuple requestOfTuple
    requestOfTuple_tuple

/-- **`LawfulCodec (Request .object)` exists.**  One of the three codecs a
`HyperdocumentOperations.Config` demands. -/
def requestCodec : LawfulCodec (Request .object) := requestStream.toLawful

/-! ## Teeth: the encoding separates requests that differ where it matters

`decode_encode` alone does not forbid a codec that collapses a field -- it
would still round-trip if the type were a subsingleton, and `Request` is not.
These check the two fields authority most depends on: a codec that lost the
target would let one object be authorized and another installed. -/

theorem requestCodec_separates_target
    (request : Request .object) (other : ResourceId .object)
    (different : request.target ≠ other) :
    requestCodec.encode request ≠
      requestCodec.encode { request with target := other } := by
  intro same
  apply different
  have decoded := congrArg requestCodec.decode same
  rw [requestCodec.decode_encode, requestCodec.decode_encode] at decoded
  exact congrArg Request.target (Option.some.inj decoded)

theorem requestCodec_separates_effectsDigest
    (request : Request .object) (other : Digest)
    (different : request.effectsDigest ≠ other) :
    requestCodec.encode request ≠
      requestCodec.encode { request with effectsDigest := other } := by
  intro same
  apply different
  have decoded := congrArg requestCodec.decode same
  rw [requestCodec.decode_encode, requestCodec.decode_encode] at decoded
  exact congrArg Request.effectsDigest (Option.some.inj decoded)

/-- And the stream codec composes: encoding a request in front of arbitrary
trailing bytes still decodes to exactly that request and exactly that suffix.
This is the property `LawfulCodec` alone does not carry, and the reason a
`Declaration` codec can be built on top of this one. -/
theorem requestStream_composes (request : Request .object)
    (suffix : List UInt8) :
    requestStream.decodePrefix (requestStream.encode request ++ suffix) =
      some (request, suffix) :=
  requestStream.decodePrefix_encode request suffix

/-! ## Axiom pins -/

/-- info: 'Minidregg.Compiler.TypedAuthorizationRequestCodec.objectVerbOfTag_tag' does not depend on any axioms -/
#guard_msgs (whitespace := lax) in #print axioms objectVerbOfTag_tag
/-- info: 'Minidregg.Compiler.TypedAuthorizationRequestCodec.requestOfTuple_tuple' does not depend on any axioms -/
#guard_msgs (whitespace := lax) in #print axioms requestOfTuple_tuple
/-- info: 'Minidregg.Compiler.TypedAuthorizationRequestCodec.requestCodec' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs (whitespace := lax) in #print axioms requestCodec
/-- info: 'Minidregg.Compiler.TypedAuthorizationRequestCodec.requestCodec_separates_target' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs (whitespace := lax) in #print axioms requestCodec_separates_target
/-- info: 'Minidregg.Compiler.TypedAuthorizationRequestCodec.requestCodec_separates_effectsDigest' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs (whitespace := lax) in #print axioms requestCodec_separates_effectsDigest
/-- info: 'Minidregg.Compiler.TypedAuthorizationRequestCodec.requestStream_composes' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs (whitespace := lax) in #print axioms requestStream_composes


/-- Source-only extraction draft; existing object transport is imported unchanged. -/
def requestWords (request : RequestWire) : List Nat :=
  [request.domain, request.semantics, request.federation, request.resourceKind,
   request.subject, request.subjectKeyEpoch, request.target, request.verb,
   request.argsDigest, request.effectsDigest, request.nonce, request.height,
   request.preStateRoot, request.policyId, request.policyEpoch, request.cost]

def requestWordCount : Nat := requestFieldOrder.length

@[simp] theorem requestWords_length (request : RequestWire) :
    (requestWords request).length = requestWordCount := rfl

def requestWireOfWords : List Nat → Option RequestWire
  | [domain, semantics, federation, resourceKind, subject, subjectKeyEpoch,
     target, verb, argsDigest, effectsDigest, nonce, height, preStateRoot,
     policyId, policyEpoch, cost] =>
    some ⟨domain, semantics, federation, resourceKind, subject, subjectKeyEpoch,
      target, verb, argsDigest, effectsDigest, nonce, height, preStateRoot,
      policyId, policyEpoch, cost⟩
  | _ => none

@[simp] theorem requestWireOfWords_requestWords (request : RequestWire) :
    requestWireOfWords (requestWords request) = some request := by
  cases request
  rfl

theorem requestWireOfWords_exact {words : List Nat} {request : RequestWire}
    (decoded : requestWireOfWords words = some request) :
    requestWords request = words := by
  unfold requestWireOfWords at decoded
  split at decoded
  · cases Option.some.inj decoded
    rfl
  · contradiction

theorem requestWords_injective : Function.Injective requestWords := by
  intro left right same
  have decoded := congrArg requestWireOfWords same
  simpa only [requestWireOfWords_requestWords, Option.some.injEq] using decoded

/-- The exact consumed prefix is checked without needing value equality. -/
private def canonicalStream {α : Type} (codec : StreamCodec α) : StreamCodec α where
  encode := codec.encode
  decodePrefix bytes :=
    match codec.decodePrefix bytes with
    | none => none
    | some (value, suffix) =>
      if bytes = codec.encode value ++ suffix then some (value, suffix) else none
  decodePrefix_encode := by
    intro value suffix
    simp [codec.decodePrefix_encode]

private theorem canonicalStream_exact {α : Type} (codec : StreamCodec α)
    {bytes suffix : List UInt8} {value : α}
    (decoded : (canonicalStream codec).decodePrefix bytes = some (value, suffix)) :
    bytes = (canonicalStream codec).encode value ++ suffix := by
  cases parsed : codec.decodePrefix bytes with
  | none => simp [canonicalStream, parsed] at decoded
  | some pair =>
    rcases pair with ⟨actual, rest⟩
    simp only [canonicalStream, parsed] at decoded
    split at decoded
    next exactBytes =>
      cases Option.some.inj decoded
      exact exactBytes
    next => contradiction

private theorem canonicalStream_whole {α : Type} (codec : StreamCodec α)
    {bytes : List UInt8} {value : α}
    (decoded : (canonicalStream codec).toLawful.decode bytes = some value) :
    (canonicalStream codec).encode value = bytes := by
  unfold StreamCodec.toLawful at decoded
  cases parsed : (canonicalStream codec).decodePrefix bytes with
  | none => simp [parsed] at decoded
  | some pair =>
    rcases pair with ⟨actual, rest⟩
    simp only [parsed] at decoded
    change (if rest = [] then some actual else none) = some value at decoded
    split at decoded
    next empty =>
      have same : actual = value := Option.some.inj decoded
      subst actual
      have exactBytes := canonicalStream_exact codec parsed
      simpa only [empty, List.append_nil] using exactBytes.symm
    next => contradiction

private def rawRequestWireStream : StreamCodec RequestWire where
  encode request := (StreamCodec.list StreamCodec.nat).encode (requestWords request)
  decodePrefix bytes := do
    let (count, afterCount) ← StreamCodec.nat.decodePrefix bytes
    if count = requestWordCount then
      let (words, suffix) ← StreamCodec.decodeMany StreamCodec.nat count afterCount
      let request ← requestWireOfWords words
      some (request, suffix)
    else none
  decodePrefix_encode := by
    intro request suffix
    simp [StreamCodec.list, List.append_assoc,
      StreamCodec.nat.decodePrefix_encode, requestWords, requestWordCount,
      requestFieldOrder, StreamCodec.encodeMany, StreamCodec.decodeMany,
      requestWireOfWords]

def requestWireStream : StreamCodec RequestWire := canonicalStream rawRequestWireStream

def requestWireCodec : LawfulCodec RequestWire := requestWireStream.toLawful

theorem requestWireStream_canonical {bytes suffix : List UInt8} {request : RequestWire}
    (decoded : requestWireStream.decodePrefix bytes = some (request, suffix)) :
    bytes = requestWireStream.encode request ++ suffix :=
  canonicalStream_exact rawRequestWireStream decoded

theorem requestWireCodec_canonical {bytes : List UInt8} {request : RequestWire}
    (decoded : requestWireCodec.decode bytes = some request) :
    requestWireCodec.encode request = bytes :=
  canonicalStream_whole rawRequestWireStream decoded

private def rawSomeRequestStream : StreamCodec SomeRequest where
  encode request := requestWireStream.encode (encodeRequest request)
  decodePrefix bytes := do
    let (wire, suffix) ← requestWireStream.decodePrefix bytes
    let request ← decodeRequest wire
    some (request, suffix)
  decodePrefix_encode := by
    intro request suffix
    simp [requestWireStream.decodePrefix_encode, decodeRequest_encodeRequest]

def someRequestStream : StreamCodec SomeRequest := canonicalStream rawSomeRequestStream

def someRequestCodec : LawfulCodec SomeRequest := someRequestStream.toLawful

theorem someRequestStream_canonical {bytes suffix : List UInt8} {request : SomeRequest}
    (decoded : someRequestStream.decodePrefix bytes = some (request, suffix)) :
    bytes = someRequestStream.encode request ++ suffix :=
  canonicalStream_exact rawSomeRequestStream decoded

theorem someRequestCodec_canonical {bytes : List UInt8} {request : SomeRequest}
    (decoded : someRequestCodec.decode bytes = some request) :
    someRequestCodec.encode request = bytes :=
  canonicalStream_whole rawSomeRequestStream decoded

theorem someRequestStream_rejects_wire (wire : RequestWire) (suffix : List UInt8)
    (invalid : decodeRequest wire = none) :
    someRequestStream.decodePrefix (requestWireStream.encode wire ++ suffix) = none := by
  simp [someRequestStream, canonicalStream, rawSomeRequestStream,
    requestWireStream.decodePrefix_encode, invalid]

private def rawRequestStreamFor (kind : ResourceKind) : StreamCodec (Request kind) where
  encode request := someRequestStream.encode ⟨kind, request⟩
  decodePrefix bytes := do
    let (⟨actualKind, request⟩, suffix) ← someRequestStream.decodePrefix bytes
    if same : actualKind = kind then some (same ▸ request, suffix) else none
  decodePrefix_encode := by
    intro request suffix
    simp [someRequestStream.decodePrefix_encode]

def requestStreamFor (kind : ResourceKind) : StreamCodec (Request kind) :=
  canonicalStream (rawRequestStreamFor kind)

def requestCodecFor (kind : ResourceKind) : LawfulCodec (Request kind) :=
  (requestStreamFor kind).toLawful

theorem requestStreamFor_canonical (kind : ResourceKind)
    {bytes suffix : List UInt8} {request : Request kind}
    (decoded : (requestStreamFor kind).decodePrefix bytes = some (request, suffix)) :
    bytes = (requestStreamFor kind).encode request ++ suffix :=
  canonicalStream_exact (rawRequestStreamFor kind) decoded

theorem requestCodecFor_canonical (kind : ResourceKind)
    {bytes : List UInt8} {request : Request kind}
    (decoded : (requestCodecFor kind).decode bytes = some request) :
    (requestCodecFor kind).encode request = bytes :=
  canonicalStream_whole (rawRequestStreamFor kind) decoded

theorem requestStreamFor_wrong_kind {actual expected : ResourceKind}
    (request : Request actual) (suffix : List UInt8) (different : actual ≠ expected) :
    (requestStreamFor expected).decodePrefix
      (someRequestStream.encode ⟨actual, request⟩ ++ suffix) = none := by
  simp [requestStreamFor, canonicalStream, rawRequestStreamFor,
    someRequestStream.decodePrefix_encode, different]

def requestFrame : List UInt8 := "DREGG/AUTH/REQUEST".toUTF8.toList ++ [1]

def signedRequestBytes (request : SomeRequest) : List UInt8 :=
  requestFrame ++ someRequestStream.encode request

theorem signedRequestBytes_existing (request : SomeRequest) :
    signedRequestBytes request =
      ("DREGG/AUTH/REQUEST".toUTF8.toList ++ [1]) ++
        (StreamCodec.list StreamCodec.nat).encode
          (requestWords (encodeRequest request)) := rfl

theorem signedRequestBytes_injective : Function.Injective signedRequestBytes := by
  intro left right same
  have samePayload : someRequestCodec.encode left = someRequestCodec.encode right :=
    List.append_cancel_left same
  have decoded := congrArg someRequestCodec.decode samePayload
  simpa only [someRequestCodec.decode_encode, Option.some.injEq] using decoded

#print axioms requestWireOfWords_exact
#print axioms requestWords_injective
#print axioms requestWireCodec_canonical
#print axioms someRequestCodec_canonical
#print axioms requestCodecFor_canonical
#print axioms requestStreamFor_wrong_kind
#print axioms signedRequestBytes_existing
#print axioms signedRequestBytes_injective


private theorem resourceKindTag_of_decoded {tag : Nat} {kind : ResourceKind}
    (decoded : decodeResourceKind tag = some kind) : resourceKindTag kind = tag := by
  cases kind <;> unfold decodeResourceKind at decoded <;>
    split at decoded <;> simp_all [resourceKindTag]

private theorem verbTag_of_decoded {kind : ResourceKind} {tag : Nat} {verb : Verb kind}
    (decoded : decodeVerb kind tag = some verb) :
    Minidregg.Theory.AuthorizationDeclaration.verbTag verb = tag := by
  cases verb <;>
    rcases tag with _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | _ | tag <;>
      simp_all [decodeVerb, Minidregg.Theory.AuthorizationDeclaration.verbTag]

theorem encodeRequest_of_decodeRequest {wire : RequestWire} {request : SomeRequest}
    (decoded : decodeRequest wire = some request) : encodeRequest request = wire := by
  unfold decodeRequest at decoded
  cases kindDecoded : decodeResourceKind wire.resourceKind with
  | none => simp [kindDecoded] at decoded
  | some kind =>
    cases verbDecoded : decodeVerb kind wire.verb with
    | none => simp [kindDecoded, verbDecoded] at decoded
    | some verb =>
      simp only [kindDecoded, bind, Option.bind, verbDecoded] at decoded
      cases Option.some.inj decoded
      have kindExact := resourceKindTag_of_decoded kindDecoded
      have verbExact := verbTag_of_decoded verbDecoded
      cases wire
      simp_all [encodeRequest]


#print axioms encodeRequest_of_decodeRequest

end Minidregg.Compiler.TypedAuthorizationRequestCodec
