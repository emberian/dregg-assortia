# Checkpoint 34 — native compile gate and recovery findings

September 27, 2026. Continues [checkpoint 33](checkpoint-33.md).
The integrated deployed platform goal remains active; a joined shared service
and a real-model hosted journey have not been established.

The exact `3a11046` native build is **failed, not qualified**. It reused 53
source/artifact-qualified modules and passed through module 201, then module
202 (`Kernel.NativeHost`) attempted to construct Replay's private `Derived`
constructor externally. A typed Replay-owned ordinary-invocation constructor
is committed in Mini `ebddd8e`, isolated from ongoing frontier changes, for
a finite repair build. The two affected modules passed independent narrow
Lean compilation against the committed dependency closure; linking and native
acceptance remain pending.
The failed logs and checkpoints are preserved. Neither its partial objects
nor the experimental Core-only relink are release-qualified binaries.

Mini `e3705ee` records an actual unforked Hermes tool call interrupted at
hard EOF while its current-birth author child was held before submission.
The child was reaped; no birth intent or application was installed. The tool
allowance was released through Mini. Parent settlement and uncertain-effect
acknowledgement required explicit audited operator recovery. This used a
synthetic provider, not a paid model. The subsequent same-session continuation
loaded the original Hermes session but found `office resource birth family is
exhausted`: the interrupted attempt had consumed ordinal zero in a one-slot
family. The owner is repairing durable birth identity/retry handling; increasing
the fixture limit would not establish correct recovery.

Mini `f5f5458` adds the six conditional lifecycle-completion source modules.
They bind the configured physical report signer, source-derived management
command, current app/package policy and signatures, and physical package read
guard. Their historical candidate is deliberately conditional: only Replay's
same admitted walk may establish the original claim provenance. Native event18
receiving, configuration parsing, host reporting and actual completion remain
work. Narrow Lean checks are not a completed lifecycle.

Independent review of the proposed fn frontier found a cross-gateway denial
of service: an unrelated historical writer could copy a consumer's scope fields
and trigger a collision. That cut remains uncommitted. The chosen construction
direction is an explicit source-authorized durable consumer registration,
uniquely binding its namespace to a gateway and an exact initial anchor. Fresh
registration starts at zero; legacy adoption must name an authenticated exact
receipt. Transport ACK alone is not authority. Rotation requires a new registered
namespace or a separately authorized migration, not a silent cursor reset.

The resident SPK host and separate agent-dispatch purse are still being joined.
Review found missing dispatch fencing during recovery, a hard-EOF check missing
after native reads before send acknowledgement, and a zero-settlement crash
window. These are being repaired before the agent route opens. The intended
physical owner remains one long-lived supervisor with the actual fd3 connection,
fixed per-caller Web/API bindings, and source-checked lifecycle/dispatch receipts.
Focused mocked tests do not establish that joined path.

Next acceptance work: build the isolated constructor repair; derive real signed
GitWeb descriptor/schema roots and run positive-rate ticket/Book recovery;
complete source-authenticated lifecycle and same-process delivery; repair and
rerun interrupted birth recovery; then exercise shared participants, agent
delegation, restart, fn publication/receiving and the real-model journey.
