# September 18 wind-down

Ember asked us to stop opening work and wind down. Every MiniDregg compiler lane is released and its queue cancelled. No next wave is authorized by this checkpoint. The one already-running hbox capture finished PASS; its lease is released with zero holders. All agents and build jobs are stopped. Work records are available for resumption, not claims of agents still running.

Mini commits **3832661** (receivers/consumer checkpoint) and **b86c800** (unfinished native host) are pushed on main. Bread **9ce713877** contains the tested executor-family changes and the first game fixture separation. Bread **ddda6170a** separately checkpoints the NightWatch source-only fixture move and HORIZON handoff; no runtime result below includes that move. Exact repository snapshots and bounded copied evidence are in [wind-down/inventory.json](wind-down/inventory.json). Captures retain their original paths; the inventory maps those paths to durable copies here.

## What actually ran

- **Joined native journey PASS:** paid resource birth, invocation by the issued owner grant, two source-rule replacements, exact original grants/generation preserved, current-rule refusal, Alice-to-Bob narrower delegation, Bob's real signed invocation at revision 2, SQLite reopen, and exact historical retries after credential expiry. Wrong signer, altered recipient, scope amplification, duplicate identities and unauthorized redelegation refuse. [Journey handoff](wind-down/artifacts/dregg-resume-journey-handoff.md), [exact native manifest](wind-down/artifacts/dregg-resume-born-joined-source.json).
- **Independent installer PASS:** repeated installations and owner mutations, deliberate management lockout, unchanged grant bytes, no duplicate charge/write on historical replay. Ember explicitly chose that a resource may govern and lock its own management; there is no implicit owner repair bypass. [Installer evidence](wind-down/artifacts/dregg-resume-install-checkpoint.json).
- **Real Ed25519/SQLite signature path PASS:** 17-field request, independent source revision, revision-only tampering, signed legacy-domain/frame refusal and missing-field refusal. Lower physical and source-admission migration checks passed. Remaining root/consumer and generated Rust integration is unfinished. [Signature handoff](wind-down/artifacts/dregg-resume-signatures-handoff.md).
- **Bread:** eleven focused native/factory tests passed in 1.289 seconds; actual executor-family initialization took 41.285 milliseconds. The existing JS-agent/World Hermes test passed in 0.073 seconds, all ten requests/error recovery included. That Hermes test reaches narrow DelegAdmit; it does not establish external Hermes service integration. Actual full-byte PQ passed in 191.471 seconds. [Runtime handoff](wind-down/artifacts/dregg-resume-runtime-checkpoint.md).

**Source attribution matters:** the native Mini journeys used the saved pre-factor declared controller `ca22fd700…`; its [exact source](wind-down/artifacts/dregg-declared-before-history-codec.lean) is retained. Current HEAD contains an uncompiled strict signed-ingress codec factor, plus a later uncompiled stronger Registry Book law. Those passing executions are not evidence that all of b86c800 works. No full `lake build Minidregg`, linked host, or public CLI acceptance ran.

## Unfinished host work, preserved explicitly

The source now connects signed observation/preparation, the same loaded image throughout admission/publication, semantic revalidation of historical operations, externally supplied genesis keys, and a shell/stdio process. This is substantial unfinished implementation.

**NativeHostCodec compilation failed** at `framed_canonical`: an already strict codec was supplied where the theorem requires the underlying codec. **Genesis compilation failed** on a missing `IndexedProgram` namespace, an induction argument and a structure elaboration timeout. The later observation, Context, Replay, Host/Main and CLI checks never started. [Host diagnostics and ordered handoff](wind-down/artifacts/dregg-resume-host-handoff.md), [genesis handoff](wind-down/artifacts/dregg-native-host-genesis-handoff.md).

The host review found real obligations: unsigned preparation could reveal private balances through failures; physical replay alone did not prove historical authorization; the Book law admitted nonzero unregistered balances. Source fixes are preserved, but none is called completed host enforcement. The isolated Book support theory passed; its Registry/application integration did not run. Observation and Book semantic profile pins still need adding. The print-only Book audit still needs exact axiom pins. Draft `docs/NATIVE-HOST.md` includes stale command examples, called out in the host handoff.

On resumption, repair the narrow codec and genesis failures, finish coordinated Registry/profile integration, check observation/replay/host, and then run the public signed CLI journey. Integrate new modules into the root import closure and finish the previously queued consumers/generated outputs. Root imports were deliberately not edited during wind-down. The actual authorized generation-revocation receiver remains separate unfinished work; lower rotation proofs do not establish that public operation.

Both local Lean compiler seats are free. Preserve the two-process/two-thread limit. Linking Mini remains a cold native C closure: local oleans/generated C exist, but local and inspected remote Mini/mathlib native objects/archives were absent. Hbox storage belongs under `/tank`; choose a bounded build lane when resuming. Do not launch a whole local build to discover its cost.

## Bread repairs staged for resumption

The direct ABI still truncates nine full-width digest coordinates across seven credential variants. Existing differential cases use a mismatched previous receipt and therefore establish refusal parity, not accepted-action fidelity. Full-width builders, an encoder, proof pins and accepted/high-bit tests are preserved **unapplied and uncompiled** in [the staged patch manifest](wind-down/artifacts/dregg-direct-auth-width-20260918/staged-manifest.json) and [test manifest](wind-down/artifacts/dregg-wide-auth-test-draft-manifest-20260918.json). Eight consumed coordinates should refuse high-bit changes in the reference-echo fixture; stealth ephemeralPk is ignored by existing semantics, so preserve exact transport without inventing a refusal claim. These checks do not establish cryptographic verification.

Strict JSON UTF-8/escape/surrogate decoding is a staged parser patch only. Producer control escaping and length-aware direct NUL transport remain unfinished. [String handoff](wind-down/artifacts/resume_wire_strings/HANDOFF.md). No staged patch was applied during wind-down.

The checked NetworkJudge/DeckDescent fixture separation did **not** demonstrate the hoped-for inclusive startup speedup: NetworkJudge still takes approximately 54 seconds. A linked-member audit confirms the fresh objects really excluded the moved definitions. Imported startup cost remains. Root's separate NightWatch fixture move preserves all 40 named definitions/proofs and the existing assurance suffix by source audit, but has no post-change Lean/native measurement. All moved proof checks remain in assurance modules; no security guard was disabled.

## Final running capture

Actual **`pbuild: VERDICT outcome=PASS status=0`**, all five selected tests passed in **802.039 seconds**. Hermes: 0.073s; full-byte PQ: 191.471s; foreign native-thread full-first lifecycle: 204.100s; narrow followed by concurrent full initialization: 203.382s; ST owner/mode exclusion: 203.013s. Four other tests were excluded by the requested filter; no selected test skipped. [Exact result and timing table](wind-down/artifacts/dregg-resume-final-runtime-results-20260918.json).

The measured executable includes 9ce713877's executor changes and NetworkJudge/DeckDescent cuts. It excludes the NightWatch cut and staged credential/string repairs. Hbox lane `hcargo` lease was released successfully, `holders_remaining=0`. No next build wave launched.

## Continuity and remaining product decisions

Wisper's selected area is cloud/resource-host lifecycle. The [contributor brief](../../contributing/resource-host-lifecycle.md) remains a proposed contract with owned upstream gaps; no assignment or contact occurred. Friends' programmable shell/nexus, own nodes, social/local-first resources and meaningful Solana use remain the product direction. Devnet intent is real stake locked with penalties recorded only; asset/cluster/custody/exit and the concrete first economic operation remain undecided. No real-asset operation or deployment ran.

Foreign working changes were preserved. Mini's `Compiler.lean`, README/licensing and Uwueave/Rust work are outside these commits. `scripts/probe-authority-domain.lean` remains an older untracked probe, unrun this wave. Bread's pre-existing staged/unstaged test/formatting changes, images and other untracked material were left alone. The Git snapshots list exact remaining paths. All implementation checkpoints use the existing main branches.
