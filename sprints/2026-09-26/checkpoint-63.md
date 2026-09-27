# Checkpoint 63 — native binaries and source-derived delegation

September 27, 2026. Continues [checkpoint 62](checkpoint-62.md); all
[parallel journeys](parallel-journeys.md) remain open.

The exact **2649f49 Mini Host is certified**, not merely source-checked.
Persvati unit `minidregg-2649f49-host-r3.service` finished inactive/success,
MainPID 0 and ExecMainStatus 0. Root rechecked ELF SHA
`95cd66117983796e4887f03f3ddd25b048d70713fb56ae93c36dbbc379139285`
and manifest SHA
`582cbe40012b9502ab7f08a27a8c13c01ace58335a6afaa27bc4850e082c0301`.
Mini **53aa766** preserves the build evidence. The source/OLean snapshot is
frozen at `/home/ember/build/minidregg-2649f49-next-20260927`; executable at
`/home/ember/build/minidregg-2649f49-evidence/minidregg-host-2649f49-r3`.
This does not establish integrated fixture acceptance.

Correction to checkpoint 62's callable-START wording: **d38c782 contained the
reviewed library path but omitted the committed CLI registration**. The exact
archive build exposed that omission. Root reviewed and committed the narrow
`resident-run` registration as **bba0a7a**, then a new exact archive build and
CLI probe reached the resident handler. Linux executable:
`/tank/dregg-build/mini-spk-host-bba0a7a/bin/spk-host-bba0a7a`, SHA
`1d85b2f21039bc228262ca6a1b0bf52a0c26688f9a7324588d3fbde3679dd2e4`.
Both the earlier INSTALL-only artifact and corrected CLI artifact have scoped
evidence. No native START was run by these gates.

**5af52bd** connects sealed fresh STOP claims to the checked physical fence:
prior running generation/unit/invocation/cgroup, exact volume witness, durable
attempt marker, then identity/volume recheck under lock. Component tests and
Clippy pass; physical STOP remains untested. STOP BEGIN/assembly modules are
frozen WIP pending root review. Crash recovery needs a distinct method that
requires Fenced under the lock; a preliminary Fenced read followed by a method
accepting Running would permit a race. Historical op27 remains receipt-only.

**543e85a** adds explicit-kind, source-owned capability JSON inspection and the
same-Store `scripts/spk-platform/delegate-app-observe.sh` continuation. Parent
issuer, epochs, validity bounds, root and channels come from the actual signed
capability read. Children narrow holder, target and verb to Bob/Hermes A/Hermes
B observing app 8401. The reserved IDs 184/274/374 were checked for collisions.
The helper, Host.Json and focused executable check pass; script syntax and
ShellCheck pass. No delegation has run. A successor Host containing the new
inspector is required; 2649 lacks it. An independent successor cache is prepared
at `/home/ember/build/minidregg-capability-next-20260927`. Root owns Json/Main;
fn-contracts is adding a disjoint paid-ingress inspector for the same next cut.

The corrected exact event22 fee inspector completed with source-decoded fee
**517** for retained plan SHA
`6a0287c77c82e32508ece21a826d0125902b244c10fbf12ab1c07dfa43421e36`.
The original error and prepared request remain intact. Client-session launched
the reviewed one-shot continuation in hbox user unit
`mini-event22-r3-resume-client-session.service`, invocation
`89129a2ef44649ef9f98717c75b58bb4`; root observed it active with MainPID 185167.
It uses one op54 submission, payer debit verification, signed ticket read and
op55 receipt lookup after reopening. **No accepted-ticket result is claimed
at this checkpoint.** The source script and fee repair are WIP pending final
portable evidence/review; never rerun a submit after its durable marker exists.

Controller v3 reserve/recovery and detached payer signing have component greens,
but mark-send and resident delivery are not finished. The controller must receive
the exact paid ingress and fresh committed frame, use source inspection to join
them to its retained op78 plan and hold, and persist receipt/hashes before ACK.
The resident alone consumes fresh op76 delivery authority. A historical lookup
cannot create that authority. A missing strict plan/ingress inspector is being
implemented in Lean; no Rust codec substitute or seed sharing is accepted.

Corrected private replay timing attributes most measured time to derivation and
advance, not loaded-image validation. fn-mini-review is freezing evidence and
tracing the expensive records before proposing an optimization. No shared
semantic change has been made. Native same-Store INSTALL/create, two-user
access, real-model Hermes, restart/disconnect, direct commands and selective fn
publication/receiving still determine completion.
