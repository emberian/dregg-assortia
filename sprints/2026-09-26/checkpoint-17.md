# Construction checkpoint — September 27, 02:10 UTC

The overnight goal remains active. This advances [checkpoint 16](checkpoint-16.md)
with separate native receiving, hosting and agent-loop results. These tests
use private synthetic Stores and deterministic model responses; they do not
establish a public service or authorize publication of private workroom history.

## Receiving and transport authority

Mini `60b9433` records the [fresh own-R progress gate](https://github.com/emberian/minidregg/blob/60b9433/docs/evidence/2026-09-26-ownr-native/pass-README.md).
The source-certified Host `c37a3507…` accepted one signed Mini progress record
at count 4 while fn's consumer ACK remained zero. After restarting the Mini
service, the same poll returned the historical operation with no new intent.
The exact accepted transaction then authorized ACK 4. Repeating that ACK
left fn's frontier unchanged at 5. The earlier two failures remain recorded;
their Stores were not relabeled or repaired into this result. Actual A-worker
draining of an own-R article followed by its queued reply remains a next gate.

Ember's principle remains **fn is semi-untrusted transport**. Mini `fbd466f`
adds the [distinct owner-release message and general codec/conflict proofs](https://github.com/emberian/minidregg/blob/fbd466f/docs/evidence/2026-09-26-selective-release-codec/README.md).
The signed bytes bind exact content, source context, recipient domain/target,
owner scope, audience and nonce. They do not prove source historical acceptance
or provide confidentiality. Mini `ca4fb64` adds a narrow-checked current-key
signature component for a restricted recipient-local owner law; the special
native receiving/replay path remains under construction. An ordinary gateway
write must not acquire owner-release provenance just by resembling its bytes.

## Installed services and actual terminal use

Mini `d55387e` repairs readiness checks to perform actual reads and socket
connections under the task UID. The [live operator-stack evidence](https://github.com/emberian/minidregg/blob/e856db1/docs/evidence/2026-09-26-operator-stack-live/README.md)
records successful installation and an explicit quiescent restart. Both task
controllers stopped, the Host/frontends restarted, signed content roots stayed
identical, and both controllers returned quiescent. Boot startup and persistent
storage placement remain unfinished; no public SSH keys were installed.

The committed `e213b4f` Linux runtime (`c95f87a8…`) passed release build,
50 tests and strict clippy. A [separate fresh 9101 terminal fixture](https://github.com/emberian/minidregg/blob/facf63a/docs/evidence/2026-09-26-terminal-live/README.md) has completed
Hermes publication and confirmed its content with signed Mini observation.
An in-flight hard EOF subsequently stopped the actual worker, emptied its
cgroup, fenced the task, and left the content unchanged. Its reserved allowance
remains held for reconciliation. Soft continuation and a usable reconnect/
recovery journey remain ongoing; stopping a process is not the whole lifecycle.

The [old same-UID B44 recovery](https://github.com/emberian/minidregg/blob/21eeb88/docs/evidence/2026-09-26-old-hosted-b44/README.md)
is complete. A narrowly scoped operator audit preceded clearing its ambiguous
pending attempt; native fence and zero-charge settlement followed. Exact lookup
and signed final reads confirmed zero reserve and unchanged parent/content.
This is an explicit operator custody audit, not fabricated proof of the old
client's unrecorded refusal. That deployment is distinct from the dedicated
accounts and the new terminal fixtures.

## Metering and creation

The native metering fixtures now include an actual HTTP 422 refusal, with
the exact response retained and reserve held, and three sequential requests
within one Hermes prompt: read, publish and final response. Each of those three
requests received its own source-authored usage quote and confirmed Mini
settlement, at accepted counts 11, 15 and 23. Final provider reserve is zero,
remaining allowance 41, with three exact replay entries. The driver stopped
after the third settlement; whole-conversation completion is not inferred.
Evidence lives in Mini's
[metered-runtime directory](https://github.com/emberian/minidregg/tree/ca4fb64/docs/evidence/2026-09-26-provider-metered-runtime-native).
Hard interruption during quoting and post-settlement restart remain separate
tests, as does eventual real-provider integration.

The [height-corrected composite build](https://github.com/emberian/minidregg/blob/21eeb88/docs/evidence/2026-09-26-mini-provider-composite-height-stable/README.md)
has matching 181-module Mac/Linux source manifests. Linux Host `30731bb4…`
created content resource 8301 through a grain-backed transaction at count 11,
settled the tool allowance, and returned a signed view through its issued grant.
The same-profile owner bare birth installed 8303 at count 12. The worker bare
birth refused; the runner had incorrectly expected an internal policy reason
where the public API deliberately returns uniform admission refusal.
[Mini `8c38991`](https://github.com/emberian/minidregg/blob/8c38991/docs/evidence/2026-09-26-grain-birth-native/r3/README.md)
preserves both positive receipts and the original runner failure. A separate
signed read confirmed the refused write left the image boundary unchanged.
A general fixture-law theorem establishes worker-bare refusal under its
stated projected fields; it does not reveal the hidden native refusal reason.
The future runner now asserts the actual public contract.

Dynamic creation is being integrated into the durable controller. Independent
review found charge-recovery windows before dispatch and after refusal, plus
a hard-disconnect versus subprocess-spawn race also present in publication.
These are active repairs. Birth configuration remains disabled by default;
the MCP tool is not yet advertised to hosted Hermes.

## Next core work

Continue actual A-worker and private workroom R→B→Q→A acceptance, finish
creation/refusal crash recovery and dispatch cancellation, exercise soft
terminal reconnect, and integrate owner-signed release into native admission
and replay. Cold and persistent latency profiling uses copied Stores only;
measured replay and repeated command hashing costs motivate an exact-semantics
optimization. Mini `8a81fa8` reuses command encoding/framing and proves request
equality for all inputs; the source-matched native benchmark is pending. It
removes no guards or replay checks.
