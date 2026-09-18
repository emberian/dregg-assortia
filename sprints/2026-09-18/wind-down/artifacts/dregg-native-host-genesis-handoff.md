# Native host genesis and public CLI acceptance handoff

Frozen on wind-down. ONE active source compile ran and FAILED. No genesis probe, public CLI probe or executable run occurred. No Git operations. Exact source/log/dependency hashes are in `/tmp/dregg-native-host-genesis-sources.json`.

## Files and immediate repairs

Owned files:
- Kernel/NativeHostGenesis.lean
- scripts/probe-native-host-genesis.lean
- scripts/probe-native-host-cli.lean

Active source command was `LEAN_NUM_THREADS=2 lake env lean -o .lake/build/lib/lean/Kernel/NativeHostGenesis.olean Kernel/NativeHostGenesis.lean`; session61995 finished and compiler seat1 released. `/tmp/dregg-native-host-genesis-compile.log` records:
1. Unknown `LawfulCodec` at139/153; import is transitive but missing namespace open `Minidregg.Theory.IndexedProgram`.
2. fund_conserves at232: `ih _ issuerPresent ...` resolves its book to original book; explicitly pass `book.applyPosting ...` to the induction hypothesis.
3. Built structure at374 hit deterministic heartbeat200000 timeout atwhnf; its projections then cascade. Consider local irreducibility for Profile.compilerProfile/semantics as other native modules use, or a scoped increased elaboration budget, then inspect next diagnostics.
No source repairs or retry were launched after wind-down. The shell wrapper also assigned the zsh readonly variable `status`, so wrapper exit1 alone is not evidence. Actual Lean diagnostics and missing olean establish failure; use a safe task-specific exit variable or bash nexttime. Compiler-generated `sorry` warnings came from elaboration errors; no explicit sorry/admit was authored.

The active compile imported OLD canonical Registry olean while admission was beginning the AccountSupported source-law update. Profile also awaits observation semantic pin. This is not a strengthened-Registry check; newrun must first emit coordinated dependencies.

## Source API and semantics

NativeHostGenesis.Config has deployment/federation/tariff/expectedSemantics/issuerEpoch/genesisHeight/factoryPredicate/enrollments/factoryController/meterAllowance. Enrollment now has supplied public KeyRecord, accountId, spendCapabilityId, controlCapabilityId, factoryObserveCapabilityId, initialBalance, accountPredicate. Distinct explicit grants are created for account owner/delegation, account installPolicy control, and singleton factory observe. No create/install authority implicitly supplies observe rights. Factory law must explicitly allow observation; arbitrary authored laws may deny themselves and no fallback bypass is introduced.

Strict configCodec composes actual key, policy token and charge codecs. build profile config returns Except Error (Built profile config); buildBytes returns dependent config/built pair. Built.seed/image/authority expose derived zero-history seed and actual complete physical authority load. Host checks manifest agreement and pins exact seed hash. Config includes no private keys or fixture signer. Initial balances are internal Book allocations by existing mint-posting algebra against explicit issuer well, with general total-zero proof; meter allowance separate. No Solana deposit/stake/token claim. Fund/initialBook API is now also consumed by admission's NativeHostBookInvariant; preserve names/definitions while repairing proof.

Checks source-written: profile mismatch; duplicate subjects/key IDs/public keys/accounts/cap IDs; physical role conflicts; enrolled factory controller; active/revoked/algorithm/length keys; full canonical cell laws; physical source-address collisions; actual complete anchored authority. Key possession and arbitrary predicate liveness are not claimed.

## Focused genesis probe (UNCOMPILED/UNRUN)

`lake env lean --run scripts/probe-native-host-genesis.lean PUBLIC-KEY-A.bin PUBLIC-KEY-B.bin` takes real supplied public key bytes. It exercises current native BabyBear/scalar29 fixture profile, strict config roundtrip/trailing refusal, actual key payload/epoch enrollment, conserved budget, zero-history restore/complete directory and authority, plus malformed/profile/identity/key/physical collision refusals. Six axiom printouts are source-written only.

## Public compiled CLI probe (UNCOMPILED/UNRUN)

`lake env lean --run scripts/probe-native-host-cli.lean HOST VERIFIER SQLITE-STORE OPENSSL` targets actual `.lake/build/bin/minidregg-host`. Generates fresh Ed25519 keys in temporary client custody using installed OpenSSL3; host sees public keys/detached signatures only. All mutations go through compiled CLI; no kernel receiver or internal prepare bypass. Fixture readback is local administrator assertion, not a public unauthenticated query.

Driver source currently performs:
- actual genesis SOURCE-CONFIG→zero-history image+pinnedJSON; bootstrap idempotence; absent ordinary-open refusal;
- public challenge→observe-assemble→prepare SIGNED before every mutation signing plan; actual external signature→assemble→submit;
- explicit observe grants and authored observe branches; Bob narrower observe+mutate with no delegate verb;
- signed own-account query exact cut [(asset0,100)], Alice's cap targeting Bob-account refusal; after birth, stale challenge refusal with same external diagnostic and no output file;
- birth→owner mutation→two rule replacements retaining original grants→actual Alice/Bob delegation→Bob native mutation;
- policy denial and wrong recipient signature preserving bytes; six accepted mutations only, exact conserved Book balances;
- fresh-process lookup and exact retry of all six original calls preserving exact receipts/finalimage, malformed call rejection;
- scratch-only physically replayable journal corruptions: unsupported event ingress, altered eventId, changed exactCharge. Actual public describe/open must refuse each and preserve scratch bytes; live original image never mutated.

Observation codec/controller, semantic replay module, strengthened Registry/Profile and host CLI are other lanes' unchecked/currently moving source. Driver signatures/methods may need adjustment once they compile. No claim this journey ran. ResourceView codec is now exported by foundations; protected queries are always signed. Useful extra replay tooth suggested by birth-review but NOT applied: set child.notAfter to exact invocation height genesisHeight+5, so final open at+6 proves original-height replay beyond current expiry without extra transactions.

## Resume order

Coordinate two-thread compiler seat with authority. Emit strengthened Registry and final Profile/observation dependencies; repair/emitsourceGenesis; compile/run focusedGenesisprobe with freshpublickeys; compile actualHost/observation/replay; build actualexecutable onlywithownerapprovedbudget; compile/runpublicCLIprobe. Run errors through exactlog+exitcapture, then capture new source hashes and coherent artifactchecks. Preserve current immutable RED record.
