import Compiler.Sp800185Cshake256Core
import Init.System.IO

open Minidregg.Compiler.Sp800185Cshake256

def main (arguments : List String) : IO Unit := do
  let count := (arguments[0]?.getD "20").toNat?.getD 20
  let size := (arguments[1]?.getD "4096").toNat?.getD 4096
  let payload := (List.range size).map (fun n => UInt8.ofNat (n % 251))
  let started ← IO.monoNanosNow
  let mut checksum := 0
  for index in [:count] do
    let output := cshake256Bytes "DREGG.THETA.MICROBENCH/v1".toUTF8.toList
      (UInt8.ofNat index :: payload)
    checksum := checksum + (output.map UInt8.toNat).sum
  let finished ← IO.monoNanosNow
  IO.println s!"count={count} payload={size} ns={finished-started} checksum={checksum}"
