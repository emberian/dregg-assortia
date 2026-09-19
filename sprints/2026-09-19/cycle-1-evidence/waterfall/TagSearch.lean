import Theory.AuthorizationDeclaration
import waterfall

namespace WaterfallStudy

open Minidregg.Theory.TypedAuthorization
open Minidregg.Theory.AuthorizationDeclaration

set_option maxHeartbeats 150000

theorem verbTag_of_decoded {kind : ResourceKind} {tag : Nat} {verb : Verb kind}
    (decoded : decodeVerb kind tag = some verb) : verbTag verb = tag := by
  waterfall? (cpus := 1) (effort := 120) (attemptHeartbeats := 2000000)
    (report := true) [decodeVerb, verbTag]

#print axioms verbTag_of_decoded

end WaterfallStudy
