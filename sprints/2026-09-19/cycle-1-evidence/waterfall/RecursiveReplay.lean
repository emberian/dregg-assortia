import Compiler.ResourceAuthorityProjection

/- The ordinary scripts below are copied from pinned Waterfall's checked
   suggestions. This file deliberately has no Waterfall import. -/
namespace WaterfallReplay

open Minidregg.Compiler.ResourceAuthorityProjection

theorem bytesSlots_length (stem : String) (offset : Nat) (bytes : List UInt8) :
    (bytesSlots stem offset bytes).length = bytes.length := by
  expose_names
  fun_induction bytesSlots stem offset bytes
  expose_names
  focus
    (first
      | assumption
      | rfl
      | contradiction)
  expose_names
  focus ((simp_all (config := { maxSteps := 100000, maxDischargeDepth := 2 }) [bytesSlots]; done))

/-- info: 'WaterfallReplay.bytesSlots_length' depends on axioms: [propext] -/
#guard_msgs (whitespace := lax) in #print axioms bytesSlots_length

theorem bytesSlots_append (stem : String) (offset : Nat) (xs ys : List UInt8) :
    bytesSlots stem offset (xs ++ ys) =
      bytesSlots stem offset xs ++ bytesSlots stem (offset + xs.length) ys := by
  expose_names
  (revert ys; fun_induction bytesSlots stem offset xs)
  expose_names
  focus ((simp_all (config := { maxSteps := 100000, maxDischargeDepth := 2 }) [bytesSlots]; done))
  expose_names
  grind +lax [bytesSlots]

/-- info: 'WaterfallReplay.bytesSlots_append' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs (whitespace := lax) in #print axioms bytesSlots_append

end WaterfallReplay
