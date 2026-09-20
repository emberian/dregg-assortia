# Mini construction cycle 1 — completed core result

Recorded September 19, 2026. [Current board](../../CURRENT.md) · [Exact evidence](cycle-1-evidence/INDEX.md) · [Initial contract](cycle-1.md).

Ember chose Mini as the construction home for the New World and requested one substantial implementation cycle. The work builds the resource semantics and physical client/receiver that a hosted agent can use. Bread remains reference material. No new Python platform was introduced.

## What now executes

The native Lean host and Rust `mini` client operate signed, persistent resources: source-authored rules, scalar state and typed content, narrower grants, current-law observation, atomic multi-resource changes, explicit per-capability revocation, and exact historical receipt recovery. Singleton changes use the same transaction receiver. Rust handles custody, signing and retained evidence; Lean owns semantic authoring and admission.

The combined native scenario has created a task and content, delegated a worker's rights, revised rules without invalidating the grants, reserved and settled task permission units alongside content changes, recovered a deliberately lost reply, and refused an invalid second transaction leg without changing the entire durable image. A hard-disconnect transition advances the task generation; the old worker's freshly signed mutation is refused. This is the kernel fence for interruption, not a claim that an external process has been stopped.

The [complete native New World run](cycle-1-evidence/final-new-world/README.md) **passed**, from **21:03:47 to 23:56:48 UTC**, with wrapper exit 0 and **10,380 elapsed seconds (2h53m)**. It finished with exactly eleven accepted events. All ten restarted historical lookups/resubmissions returned original receipts without changing the durable image or charging again. Current rules refused both ordinary observation and direct-submit bypasses; changing a guess about hidden content produced identical public refusal bytes. Deliberate management lockout refused the owner’s repair attempt and preserved the entire durable image. The task finished paused at generation 2, with 70 permission units remaining and none reserved; the participant’s exact content bytes were committed. These are local execution results with synthetic balances, not deployed succinct assurance.

## Source and executed-artifact scope

| Result | Source / artifact |
|---|---|
| Core native New World and legacy scenarios; Rust mixed-resource client | Mini `12e6608`; host `0da9f139…`; compiled runner `dbd2539a…`. Exact source closure is archived. |
| Complete Rust authority-client scenario, 904.65 seconds | `b119f86` host `5ec9755d…`; script `63612f5`. The additional Lean source change exposes a policy's source-derived address and reversible predicate in authorized JSON. |
| Latest full umbrella and native build | Mini `66d74dd`; 581/581 compiled source files match Git. Literal umbrella 585 seconds; full gate/native build 661 seconds. Both native build paths produce identical host `3107faf3…`. |
| Latest executable runtime evidence | Exact signed birth and receipt; exact accepted query over eight-event replay; stale-worker refusal matching the original bytes; then an accepted locked-policy query and refused owner repair over the final eleven-event history. The exact original outputs and entire logical image were preserved; see the [final-history replay](cycle-1-evidence/charge-final-lockout/README.md). These are focused checks on the later proved charge-materialization change, not a second fresh complete New World run. |

The [complete legacy regression](cycle-1-evidence/final-legacy/README.md) passed in 1,066 seconds. The [Rust mixed-resource client](cycle-1-evidence/final-client/README.md) passed in 444 seconds; its focused Rust checks passed 4/4, plus format/lint checks. The [authority client](cycle-1-evidence/final-client-authority/README.md) exercised ordinary JSON policy authoring/roundtrip, a permitted Bob write, prohibited escalation, revocation, and original receipt recovery without advancing the public image boundary. The full New World scenario supplies the separate complete stored-image checks.

The installed executable is `minidregg/.lake/build/bin/minidregg-host`, SHA-256 `3107faf3583e4c4926feb8931edee6e0aea4f800617bc0969d9d3c845caebe4d`; a local provenance JSON sits beside it. The Rust client and its two runnable recipes are documented in [the Rust client README](https://github.com/emberian/minidregg/blob/66d74dd/native/resource-client/README.md). Fresh source-authored genesis and the current profile/wire epoch are used; this cycle does not migrate an old deployed store.

## Performance and proof work

General equality proofs support the cast, birth-source projection/identity, order-bit, Keccak-theta and finite-charge computation changes. The actual receiver and replay consumers were rebuilt. Waterfall was used for three real proof searches; replayed ordinary scripts do not import it, and the canonical codec proof is integrated without a new production tactic dependency.

The matched birth comparison improved from 223.78 to 49.43 seconds with identical inputs and receipt bytes. A formerly stalled signed task query completed in 33.55 seconds. The later charge-only comparison at eight events improved 105.51 to 91.66 seconds against its immediate parent, with identical view bytes and unchanged whole logical image. That is one sequential trial under concurrent system activity. Earlier one-event query and fresh-birth comparisons against other baseline hosts found no gain (33.55→35.63 and 49.43→63.59 seconds); they do not isolate the two-file charge delta.

Current latency is not suitable for an interactive shell. Fresh processes semantically re-admit the retained signed history, and repeatedly encode/hash growing images. Charge materialization is complete; a persistent verified host session is a separately specified, unimplemented next core step. Its cache must preserve exact checked history and refresh current authority, rather than cache authorization decisions.

## Cycle accounting and next construction

Mini advanced from `a328f0e` through `66d74dd`: 19 commits, 85 files changed, 10,168 insertions and 1,198 deletions. These counts describe the patch, not its correctness. Planning began around 18:08 UTC; the first explicit clock observation was 18:16:09. An account interruption occupied roughly 19:47–20:07. The final native verdict arrived at 23:56:48 UTC, roughly 5h49m after planning began; final archival/commits followed. No exact active-effort or comparative model-cost estimate is claimed.

The next experience still needs a persistent, responsive receiving process and the real Hermes/tool supervisor: connect/disconnect modes, process interruption and recovery, credential-service access and actual metering. Provider execution, contributed-node hosting, Solana stake/utility operations and deployed STARK assurance remain implementation work. Explicit generation-wide native revocation and a delegated grant surviving two rule changes remain open in W-GRANT-REVISION. Worker generation in this cycle is an authored per-subject resource law, not a generic native predicate grant caveat.

The completed evidence closes W-JOINT-POST, W-AUTHORITY-NATIVE, W-POLICY-SOURCE, W-AUTHORIZED-DELEGATION, W-PROGRAMMABLE-PATH and W-NATIVE-HOST. W-CHARGE-MATERIALIZATION is separately complete with its scoped measurements. W-M26-DESIGN and W-GRANT-REVISION remain active; W-HOST-SESSION remains unimplemented. The next cycle should join core latency work and the actual hosted agent lifecycle through these same resource semantics.
