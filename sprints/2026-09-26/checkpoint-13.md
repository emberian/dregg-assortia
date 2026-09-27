# Construction checkpoint — September 27, 00:15 UTC

The autonomous Mini/fn goal remains active. This continues
[checkpoint 12](checkpoint-12.md) without editing its dated snapshot. The
result scopes below are separate: a fresh Hermes receipt fixture, a copied
Host-image mismatch, a live retained B call, a standalone fn bridge, and
source-level composite/provider work. No result below establishes a new
public deployment or a complete new R/Q exchange.

## Immediate hosted receipt

Mini commit `7bfa946` captures a [fresh 8801/8802 unforked Hermes gate](https://github.com/emberian/minidregg/blob/7bfa946/docs/evidence/2026-09-26-hermes-immediate-publication-receipt/README.md).
The corrected strict provider, source `5ebaaff`, saw the **same** `mini_publish`
tool result shown to Hermes. Its nested historical receipt had the exact
transaction ID, event ID, accepted count 12, and image boundary of the
confirmed Mini operation 20 and durable journal; the 133-byte canonical
outcome SHA-256 `0a39047c15ddab7d7a117b5dca9a95533f61b19c93089adbc783246e785b1af3`
matched the journal's retained outcome hash. The provider stopped on that
receipt and the controller settled. The later signed query boundary was
correctly **not** equated to the historical publication boundary. The
earlier strict fixture produced a false negative on that comparison; it is
preserved separately. This demonstrates delivery to the local deterministic
provider's tool-result input, not remote model consumption or permission to
discard recovery state (`reported:false`).

## Retained fn B receipt and acknowledgement

Commit `99ca8c7` introduced a version-two client socket envelope carrying
the expected Mini Host executable hash. The [copied and live gate](https://github.com/emberian/minidregg/blob/2a96e20/docs/evidence/2026-09-26-mini-host-image-pin/README.md)
records a fail-closed copied fixture: the worker expected new image
`49e8e6f0…` while the broker served old image `919c3b7b…`; the exact call
was only looked up, no retry or ACK was authored, and the worker entered
Held. In a **separate live B migration**, the matching image's read-only
lookup recovered the original confirmed/replayed four-field Mini receipt at
accepted count 3. Its first ACK then refused in phase `fn-session` after fn
cursor inspection. A standalone bridge probe with unset `FN_B3_IMAGE`
produced the same missing-image error; the launch environment cause is
diagnosed, not proven by an immutable process-environment manifest. The
first refusal did not become an ACK.

Commit `f64acf0` adds a [standalone operator-pinned fn bridge](https://github.com/emberian/minidregg/blob/f64acf0/docs/evidence/2026-09-26-fn-operator-bridge/README.md)
that checks the selected fn image, core, runtime, and OpenSSL hashes and no
longer depends on ambient `FN_B3_IMAGE` or fault-injection variables. A
read-only inspection of the retained cursor produced byte-identical output
to the historical explicitly configured bridge; negative hash cases
refused before output. This is transport setup, not itself a B ACK.

Commit `2d592de` adds explicit Held-ACK recovery anchored to the exact
previously confirmed call and all four receipt fields; the owner reported
**35 focused Rust tests passing**. The actual retained fn R2 B worker was
subsequently resumed on the separately qualified core-only Mac Host
SHA-256 `49e8e6f05fd1f86c88e8920e66e3827b6a026bb265bd305e4438bc1fb2e4ed41`,
not the combined host used for checkpoint 12's timing. Its lookup
reconfirmed the original receipt, op13 reported durable fn ACK accepted at
fn Store transaction/sequence `3/3`, and a fresh signed B inbox view
matched the original A content edit: target 8001, atom 7401, exact revised
text and all four Mini origin receipt fields. The raw signed-view bytes are
SHA-256 `58590dd26a2818a88c2609778426ceda2bd4f0a34c2c4d5ac31b8154289d3f68`;
the typed JSON is `10bc1afa40f3228b1a8be2faf04dcf404bd6a0ed4e700d2e777aabb6d4004c9d`.
The earlier refused ACK remains a separate retained attempt. The bounded
[keyless B completion record](https://github.com/emberian/minidregg/tree/3f7bc7b/docs/evidence/2026-09-26-host-session/workroom-b-content-completion)
pins the call, Host, client, lookup, ACK and signed read. It does not claim
a new B-local edit to content 8001. Q→A is handed to a separate lane and is
not yet a completed new roundtrip.

This fn R2 B is distinct from hosted peer B 7803/7804's pre-submit
stale-target attempt and retained tool hold in [checkpoint 12](checkpoint-12.md).
Commits `21beea2` and `9d940fc` wire source-level classification and exact
retention of a durable native pre-submit refusal before the client returns
custody failure. Focused runtime/client tests are owner-reported passing;
the new `9d3c5aa` strict stale-root Hermes fixture is awaiting its fresh
8901 native gate. This source work has not reconciled the old hosted B hold.
The two Stores, attempts and receipts must remain separate.

## Composite birth and provider/frontend construction

Commit `aca9247` adds [strict canonical signed birth-plus-grain ingress](https://github.com/emberian/minidregg/blob/aca9247/Kernel/GrainResourceBirthPolicyController.lean)
and ties the user draft, grain command nonce, target/observation envelopes,
domain and semantics to one source shape. Commit `28e3f58` adds
[general authority-preparation proofs](https://github.com/emberian/minidregg/blob/28e3f58/Compiler/GrainResourceBirthAuthority.lean)
that the combined operation consumes its marker while preserving the birth
fields and grants in the single prepared authority post. These are kernel
source/proof advances over checkpoint 12, not an actual admitted composite
birth, signed joint candidate or usable Hermes tool. Its native admission
gate remains required.

Commit `567fa58` adds [Lean-owned provider usage parsing, quote and bounds](https://github.com/emberian/minidregg/blob/567fa58/Kernel/ProviderMetering.lean)
with a Host presentation and op19 source seam. Narrow arithmetic/parser
checks passed; a source-matched native op19 build and receiving run remain
pending. The general rounding and budget lemmas describe a quote over
**provider-reported** token counts; they do not authenticate an invoice,
prove hosted settlement or record a paid-provider call. A cross-UID
frontend has passed a private transport/ACL probe for two
OS accounts reaching only their own frontend and the shared private Mini
host. A fresh independent four-principal Store provision also passed. Its
first cross-UID ordinary signed query from UID 65534 was refused **before
forwarding** with `frontend requires exact pinned v2 Mini envelope`: the
ordinary client still sent version one. Client wiring is in progress; this
is **not** a Mini native-authority rejection or signed two-controller
query/mutation acceptance. A separate hostile default-ACL inheritance
probe passed locally. These bounded tests remain in private fixture paths;
neither WIP path changes the live 780x controllers.

The [whole-prefix fn release design](https://github.com/emberian/minidregg/blob/d9edc9c/docs/FN-RELEASE-DESIGN.md)
remains a proposal, not an Ember-selected policy or an agent sharing tool.
Next gates are Q→A on the pinned fn bridge, a fresh 8901 typed pre-submit
refusal and recovery run, source-matched native op19 receiving, actual signed
two-UID frontend operations after client v2 wiring, and native composite
birth. The old hosted B hold needs its own disposition. A component pass is
not a substitute for any of those receiving consumers.
