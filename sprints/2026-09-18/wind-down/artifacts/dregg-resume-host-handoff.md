# Native host lane wind-down — 2026-09-18

Frozen on the user's instruction. No source edits or new checks after wind-down. Seat 2 released; no owned compiler process remains. Exact source/log hashes and prior checked artifacts: `/tmp/dregg-resume-host-checkpoint.json`. Prior four-module evidence preserved unchanged: `/tmp/dregg-host-profile-checkpoint.json`.

## Measured results

GREEN, current source byte-identical to emitted checkpoint: Compiler/BabyBear.lean, Compiler/EmitSerialize.lean, Compiler/CanonicalRuntimeProfile.lean, Compiler/NativeHostProfile.lean. The field definition is extracted once, retaining actual compiler identity. BabyBear/29 has kernel-proved order no-wrap and lemmas exposing actual integer-range/cast checks. The runtime profile binds migrated revision/generation, shared request framing, install/delegation projection, logical-clock rule and native host wire identity; receiver-specific parameters are pinned.

RED: NativeHostCodec attempt 2 (session 24701, exit 1); `/tmp/dregg-host-NativeHostCodec-attempt2.log` has exactly one error at line 45. `framed_canonical` accidentally instantiates strictCodec_canonical with the already strict framed codec, yielding a double strictCodec type mismatch. No source sorry was added. On resumption, factor the raw framed codec into a named definition and explicitly pass that raw codec to the theorem, or explicitly unfold the existing definition. This is a proposed repair, not tested.

Never checked: NativeObservationCodec, NativeHostContext, NativeObservationController, NativeHostReplay, NativeHost, Host.Main. No linked host executable or public CLI journey exists yet. Genesis owner independently reports RED (missing IndexedProgram LawfulCodec namespace, fund_conserves induction application, Built structure heartbeat then cascades); `/tmp/dregg-native-host-genesis-compile.log`. Do not infer a host green from the separate direct receiver journey green.

## Source delivered and actual boundaries

NativeHostCodec defines strict Draft, SigningPlan, four-family SignedCall, sealed receipt and Outcome codecs. It owns the sole imageBoundary hash reused by Context/observation. Full canonical SignedHeader bytes are signed externally; no raw DataIntent public mutation.

NativeHost loads once; open is wired to the source semantic history verifier. Height derives from genesisHeight plus the same image's accepted count. Actual four receiveLoaded paths use exact-image CAS; no admission on one image followed by hidden rebase. Historical receipts bind original prefix position. All rejected fresh submissions are exposed uniformly; blind writes and recipient credits do not acquire an artificial observe prerequisite.

Unsigned preparation had a real account-balance/existence oracle. Public prepare is now wired in source to actual per-resource observation authorization, using the SAME Opened snapshot. It only exposes preparation diagnostics after authorization of the exact read footprint. Query is the selected resource/account cut, policy or own observation grant; never a whole Book or arbitrary authority dump. Public challenge exposes explicitly classified protocol metadata. Timing noninterference is not claimed. The gate and wiring have not been compiled and must not be described as closed security work yet.

Main has source CLI and framed stdio for actual genesis/bootstrap, describe, challenge, observe-assemble, authenticated prepare/query, mutation assemble/submit and replay lookup. Genesis is explicit absence-only initialization, not policy repair. Resource policy may intentionally lock management. The actual source policy must govern all management paths.

## Ownership / interfaces on resumption

- Host lane: Compiler/BabyBear.lean, EmitSerialize.lean extraction, CanonicalRuntimeProfile.lean, NativeHostProfile.lean, NativeHostCodec.lean, NativeObservationCodec.lean, Kernel/NativeHost.lean, Host/Main.lean, lakefile.toml target, docs/NATIVE-HOST.md.
- birth_review: Kernel/NativeHostContext.lean (exact extraction from host, same namespace), Kernel/NativeHostReplay.lean and bounded DeclaredResourceController parser factoring. `NativeHostReplay.verifyLoaded config durable : IO (Except Failure (Verified config durable))`; host returns verified.opened. Context was NOT emitted.
- foundations: Kernel/NativeObservationController.lean. `Context deployment durable` retains exact loaded directory/authority. `challenge context profile federation genesisHeight intent`; `authorize native context profile federation genesisHeight signed` returns private AuthorizedIntent retaining actual proofs and optional queryResult. Source frozen, never checked.
- genesis: Kernel/NativeHostGenesis.lean strict config/buildBytes; scripts/probe-native-host-cli.lean actual public workflow driver. Neither public CLI execution nor native linking has run.
- admission: AccountSupported invariant and Book law integration. Isolated theory GREEN; actual registry-law migration pending root coordination.

## Remaining pinned decisions / ordered convergence

1. Repair the one NativeHostCodec proof and emit it narrowly, then NativeObservationCodec and Context; obey global two-process/two-thread build coordinator.
2. Compile/reconcile observation, replay and genesis actual modules, then NativeHost/Main. Profile must add `DREGG.RUNTIME.OBSERVATION.EXACT-IMAGE-RESOURCE-AND-ACCOUNT-CUT/v1` plus the coordinated Book AccountSupported law marker before asserting final operational identity. These pin/law edits were deliberately NOT made before wind-down. No schema truncation or hidden width reduction.
3. Finish actual Book support-law integration so hidden balances outside declared accounts cannot influence preparation. Wire representation remains lossless and unchanged; semantic identity changes.
4. Update `docs/NATIVE-HOST.md`: currently source-draft; old prepare DRAFT example, unsigned-prepare-pending prose, stdio 0–3 list, and unfinished-query tail are stale relative to newer uncompiled source. Preserve this distinction until checks pass.
5. Obtain bounded native build capacity. Laptop has Lean oleans/generated C but no C objects or archives for Mini or Mathlib; a linked host build is a cold C closure. EmitSerialize remains transitively imported despite BabyBear extraction. Do not launch uncontrolled umbrella work locally.
6. Compile/run actual executable with operator-supplied ephemeral keys and genesis. Public challenge/sign/prepare/sign/submit path must witness paid birth → two policy replacements preserving grants → delegation to Bob → Bob invocation → restart/exact retry; include uniform refusal, authorized account cut, stale read challenge, malformed physical/semantic history refusals. Source-only driver is not evidence.

## CLI source contract for fixture owner

`minidregg-host CONFIG.json genesis SOURCE-CONFIG.bin GENESIS.bin PINNED-CONFIG.json`; bootstrap GENESIS.bin; challenge INTENT.bin CHALLENGE.bin; observe-assemble CHALLENGE.bin SIGNATURES.bin SIGNED.bin; prepare SIGNED.bin PLAN.bin; query SIGNED.bin VIEW.bin; assemble PLAN.bin SIGNATURES.bin CALL.bin; submit/lookup CALL.bin OUTCOME.bin. Mutations return Outcome; observe failures are constant observation refused via IO.ofExcept, nonzero exit, no output file written by failed handler. Stdio opcodes 0 describe, 1 authorized prepare, 2 submit, 3 lookup, 4 challenge, 5 authorized query. These are current source contracts, uncompiled.

No succinct-STARK deployment claim, full-width arithmetic completion claim, or complete public host acceptance claim.
