import Compiler.ResourceAuthorityProjection
import waterfall

namespace WaterfallStudy

open Minidregg.Compiler.ResourceAuthorityProjection

set_option maxHeartbeats 150000

theorem bytesSlots_length (stem : String) (offset : Nat) (bytes : List UInt8) :
    (bytesSlots stem offset bytes).length = bytes.length := by
  waterfall? (cpus := 1) (effort := 120) (attemptHeartbeats := 2000000)
    (report := true) [bytesSlots]

#print axioms bytesSlots_length

theorem bytesSlots_append (stem : String) (offset : Nat) (xs ys : List UInt8) :
    bytesSlots stem offset (xs ++ ys) =
      bytesSlots stem offset xs ++ bytesSlots stem (offset + xs.length) ys := by
  waterfall? (cpus := 1) (effort := 180) (attemptHeartbeats := 2000000)
    (report := true) [bytesSlots]

#print axioms bytesSlots_append

end WaterfallStudy
