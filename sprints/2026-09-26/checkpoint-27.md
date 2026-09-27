# Checkpoint 27 — admitted history and participant entry

September 27, 2026. Continues [checkpoint 26](checkpoint-26.md).

Mini `b07628f` adds executable one-index selection in the native replay walk.
It returns the actual admitted before/after checkpoint, exact record and receipt,
and proofs connecting it to the verified target. A bounded Lean check passes.
This repairs the missing executable connection described in checkpoint 25;
it does not itself authorize a new dispatch or lifecycle claim.

Mini `5a76cf9` adds a compact shared issue-evidence type for live dispatch and
replay. It requires an actual accepted issue and full recorded-intent equality.
Chronological membership remains a separate requirement. The active replay
integration must accumulate evidence only after admitting each issue, seed
suffix verification from previously verified context, and reject a dispatch
that depends on a later issue. `cf28084` supplies the guarded pending intent
and exact wrapper/event identity proofs. Native dispatch/CAS and physical
delivery are still missing.

Mini `dee702b` adds private participant HTTP custody with six focused passing
tests and strict Clippy. Review corrected unchanged browser form writes,
direct bookmark entry, empty write bodies and HEAD behavior. Every authenticated
request still returns 503. Token bootstrap, private TLS entry, participant
signing and checked Mini delivery remain active integration work.

Mini `a6bcefa` adds successful-build prefix reuse, checking source, generated
artifacts and external inputs before reusing a prefix. Seven isolated guard
cases pass. Actual native reuse awaits a newly checkpointed full baseline;
older successful builds are not silently qualified. Mini `49cbaa4` records the
completed source-publication/share-issue Linux Host; root compared all 209
source hashes against the exact baseline and eight pinned overlays.

The first source-publication test stopped at planning refusal, before source
op24 or any fn POST. That run is retained while the cause of refusal
is investigated. Earlier native recipient acceptance remains valid in its own
scope. Current-birth Host compilation is active in a separate snapshot; the
hosted fixture uses the Rust deterministic provider from `8fec18a`, with explicit
synthetic usage. Success must come from native receipts, signed reads and
recovery, not the provider's stage counter.

Review also found that sharing custody must approve payer, funding and source
capabilities as well as the ticket specification. A separate in-progress Plan
v2 retains the complete source-authored Request for exact approval comparison.
Unsigned planning stays on an operator-only socket, separate from participant
receiving. No complete shared browser/Hermes service, paid-model run or public
deployment is established by this checkpoint.
