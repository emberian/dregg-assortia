import Theory.AuthorizationDeclaration

namespace WaterfallReplay

open Minidregg.Theory.TypedAuthorization
open Minidregg.Theory.AuthorizationDeclaration

/- The generated proof applies fun_cases, then the same grind command in
   every non-default branch and simp_all in the impossible default branch.
   This normalizes those repeated leaf commands using all_goals. -/
theorem verbTag_of_decoded {kind : ResourceKind} {tag : Nat} {verb : Verb kind}
    (decoded : decodeVerb kind tag = some verb) : verbTag verb = tag := by
  fun_cases decodeVerb kind tag <;> grind +lax [decodeVerb, verbTag]

/-- info: 'WaterfallReplay.verbTag_of_decoded' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs (whitespace := lax) in #print axioms verbTag_of_decoded

end WaterfallReplay
