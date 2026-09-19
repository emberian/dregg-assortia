# Cycle 1 client API native build

This build adds the `inspect view-policy` JSON presentation to the prior final
host. The only source delta in the 581-file compiled closure is
`Host/Json.lean`: SHA-256 `b2b6de00be8f4daf85bed5b29bf6167432284a0a99a04eab5d865728e0e5d6be`
→ `a28fb3281c2c04409c14520757978abcabb38defb5ccd86776919befc35e03af`.
The previous source manifest SHA-256 is
`b8ba155a3cd571c830b79370464e1344aa6123f3e44dc7f0d40f2f454f00ef94`;
the new manifest SHA-256 is
`e4ad0c4665c70ce8c44714961cfa26104b7113a107f1c6b56c29757a87389202`.
Every listed source byte matches Git commit
`b119f868742edd687064ff4449c05595e8f26e0d` (581/581). The isolated
snapshot was cloned from the earlier final snapshot, with distinct file inodes
and no package symlinks. The parent build's manifest SHA-256 was
`afa8670a0acee225f572d8f5eb050923327ec3c1baf9108f92ddbfcd4aa68864`;
its executable SHA-256 was
`fe68c5095882b80f1d9a55ab9d8f959c0b0c8662dee454b543160a17bb5c9906`.

The literal `lake build Minidregg` gate passed in 8 seconds and
`Host.Main:leanArts` passed in 18 seconds. The native host link used 153 host
source modules, 2,933 package modules, and 3,086 object files. The bounded
builder used at most one real Lean compiler; elapsed build time was 81 seconds.
The new Mach-O arm64 host SHA-256 is
`5ec9755d2013d136d22626ca6823ef324c75b1b65cd8e0ac829546ac8a1ed68c`.
The original temporary binary path is recorded in `manifest.txt`. The CLI
usage smoke passed; the separate Rust authority recipe is not claimed here.

This directory contains bounded logs, exact source and artifact manifests,
the one-file overlay ledger, and build commands. It contains no private keys,
runtime fixtures, or executable binary.
