# SPK construction checkpoint — September 27 UTC

The active platform goal remains the integrated shared application journey in
[the cycle brief](spk-platform-cycle.md). This checkpoint records component
progress and an actual hosted resource result. No packaged app has yet been
executed or served to a participant, and no real model was used in this run.

## Reusable package and application protocol

Bread `028bc02718bec8fc5820aa73c4e765a6fad5fc53` moved its signed SPK,
Cap'n Proto archive and manifest decoding into the standalone
`sandstorm-package` crate, with Bread's existing API reexported through
`sandstorm-bridge`. The leaf parsed the signed Simple Todos and Wekan packages.
Its independent narrow test ran 14 parser cases; the Bread facade ran three.
Wekan's approximately 525 MiB uncompressed archive still requires an explicit
larger decode bound; the ordinary 256 MiB limit rejects it. These checks did
not execute either app. See Bread `sandstorm-package/README.md`.

Mini `c6c13ca` adds `native/spk-rpc`, a private typed supervisor endpoint using
Sandstorm schemas pinned to `a97cf3ee19d3bf2761cd597583ca5d998de425d8`.
One real Unix socketpair test passed bootstrap, view discovery, Web/API session
setup, identity callback and an inline WebSession GET against a fake peer.
It has no public listener or Mini admission yet. The source and limits are in
Mini `native/spk-rpc/README.md`.

The signed Simple Todos SPK is a plausible first browser launch; its bridge
config declares no external API. Wekan has API routes and `apiPath="/"`, but
inspection of its bundled REST middleware found that the relevant routes need
a Meteor user token. A Sandstorm API token alone has not been shown to pass
that check. The bounded package inspection is in
[grounding 1](spk-grounding-01.md) and `/tmp/spk-mini-probe/EVIDENCE.md` on the
development machine. App selection for the browser-plus-agent acceptance is
therefore still open pending an isolated real run and a working authorization
path.

The package-parser audit found concrete untrusted-input gaps: a tiny composite
list can request very many zero-width descriptors, directory pointers can
cycle through recursive archive decoding, and the XZ library buffers a whole
decoded block before the parser's output limit applies. Bread's parser lane is
repairing the structural bounds. Physical package ingestion needs a bounded
process memory and time budget even after that repair. The reproducer and line
references are in `/tmp/spk-parser-audit/EVIDENCE.md` locally. Mini's new
`native/spk-host` and `deploy/spk-host` source is under review, with an
isolated persvati extraction of Simple Todos and a harmless fd3/namespace/quota
launch test. Neither test ran the packaged executable.

## Mini lifecycle and hosted Hermes

Mini `7c2fa64` adds Lean `ApplicationGrain`, its laws and a three-resource
birth descriptor. It distinguishes an app's lifecycle from an AgentGrain,
uses pending phases for installation/start/stop/upgrade, and pairs the app
with package and snapshot content resources. The three modules compiled in an
independent narrow Lean snapshot without `sorry` or `#guard`. This source
does not yet supply native app birth, checked physical completion, session
enrollment or HTTP dispatch. A content operation counted by the current law
can be a no-op; actual package identity still needs a typed checked receiver.

Mini `a98f480` exposed operator-approved resource birth families to hosted
Hermes tools; focused Rust suites passed 60/60 runtime and 15/15 fixture tests.
The separate [hosted run](https://github.com/emberian/minidregg/blob/9d7b2c5/docs/evidence/2026-09-27-hosted-birth-9301/README.md)
used unforked Hermes with a deterministic provider and the actual Mini Host.
It created resource 9303, read it and published atom 9304. On controller
restart, the original composite birth's read-only lookup refused while the
subsequent publication lookup replayed. The parent budget remains held and
no second birth was attempted. The exact cause is a missing composite-birth
branch in `NativeHost.lookupLoaded`; a scoped repair is compiling and will be
checked against a **copy** of the retained Store before any live recovery.

The next whole-path gate is a real SPK process under the reviewed sandbox,
followed by Mini checked app/session admission, browser and agent access to the
same durable app, physical restart and uncertain-request reconciliation. Only
after that can selected app/data version publication through fn and a real
model establish the requested integrated journey. Previously green fn, terminal
and metering fixtures remain separate evidence, not that combined journey.
