import Compiler.TypedAuthorizationRequestCodec
import Theory.AuthorizationDeclaration
import Compiler.DeclaredHyperedgeArtifact
import Compiler.CredentialSignatureAdmission

namespace Minidregg.Compiler.TypedAuthorizationRequestCodec

open Minidregg.Theory.IndexedProgram
open Minidregg.Theory.AuthorizationDeclaration
open Minidregg.Theory.TypedAuthorization
open Minidregg.Compiler.Tower256ConcreteBackend

set_option autoImplicit false

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


/-- Compatibility is with the actual current artifact, not a copied test encoder. -/
theorem requestWords_existing_artifact (request : RequestWire) :
    requestWords request = DeclaredHyperedgeArtifact.requestWords request := rfl

/-- Compatibility is with the actual current native message producer. -/
theorem signedRequestBytes_existing_admission (request : SomeRequest) :
    signedRequestBytes request = CredentialSignatureAdmission.requestBytes request := rfl

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

#print axioms requestWords_existing_artifact
#print axioms signedRequestBytes_existing_admission
#print axioms encodeRequest_of_decodeRequest

end Minidregg.Compiler.TypedAuthorizationRequestCodec
