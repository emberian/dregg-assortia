import Theory.AuthorizationDeclaration

namespace WaterfallExactReplay

open Minidregg.Theory.TypedAuthorization
open Minidregg.Theory.AuthorizationDeclaration

theorem verbTag_of_decoded {kind : ResourceKind} {tag : Nat} {verb : Verb kind}
    (decoded : decodeVerb kind tag = some verb) : verbTag verb = tag := by
  expose_names
  fun_cases decodeVerb kind tag
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  grind +lax [decodeVerb, verbTag]
  expose_names
  focus ((simp_all (config := { maxSteps := 100000, maxDischargeDepth := 2 }) [decodeVerb, verbTag]; done))

/-- info: 'WaterfallExactReplay.verbTag_of_decoded' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs (whitespace := lax) in #print axioms verbTag_of_decoded

end WaterfallExactReplay
