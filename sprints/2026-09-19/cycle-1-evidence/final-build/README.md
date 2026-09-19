# Cycle 1 native build evidence

Source commit: `12e66083e2d028133f236d62c24bfe02af3b861e`.
The initial copied snapshot was based on an earlier commit; the overlay ledgers
record each later source replacement. The final source manifests were checked
byte for byte against this committed Git tree: 581/581 umbrella files and
153/153 native host files passed. The untracked Uwueave source was excluded
from the final umbrella import closure by restoring committed `Compiler.lean`
inside the isolated snapshot.

The literal `lake build Minidregg` final gate passed in 177 seconds with a
serialized Lean compiler wrapper. `Host.Main:leanArts` passed in 10 seconds.
The complete native link used 153 source modules, 2,933 package modules, and
3,086 object files. The final-gate host is a Mach-O arm64 executable with
SHA-256 `fe68c5095882b80f1d9a55ab9d8f959c0b0c8662dee454b543160a17bb5c9906`.
The manifest records its original temporary path. Building and CLI usage
smoking are separate from runtime acceptance.

The earlier direct native candidate rebuilt the exact 38-module transitive
reverse dependency closure of `Compiler.PredOrderGadget` after the theta and
birth optimizations. Its 153 host source hashes match the same committed tree.
The linked host SHA-256 is
`0da9f1392fad3913356e3a495f0d3ab4f1a247aec8988a9f90312666e9ccadc1`.
The compiled acceptance runner uses that host's exact 3,086-object response
and the public driver source SHA-256
`cbe8f996d6ab6462d35bef27a659ee62eec32c7c74d1c02caaf8ea7589deaf6d`;
its executable SHA-256 is
`dbd2539ac5a91eb4dec6f381f41fd2cba276214cc8ed637c1221fba7537a994e`.

This directory contains manifests, bounded build-log excerpts, commands,
source and executable hashes, and the overlay ledger. It does not contain
private keys, runtime fixtures, or large executable binaries.
