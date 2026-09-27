# Actual SPK and protocol grounding — September 27 UTC

This advances the [platform cycle](spk-platform-cycle.md). It records inspection
and one parser repair, not an application deployment.

## Local Simple Todos package

An isolated Rust harness in `/tmp/spk-mini-probe` compiled copies of Bread's
`spk.rs`, `capnp_wire.rs` and pre-repair `manifest.rs`. Only the unused grain
representation was stubbed; signature, decompression and archive parsing used
the actual source. The release/offline run completed on the real 23,632,200-byte
`DreggNet-pub/sandstorm-bridge/fixtures/sample.spk`. SHA-256:
`5830d70137cdae158118884da8790870fb095a07996cfe7708fb0155df45232e`.

The signed package identifies Simple Todos v5, marketing version `2015-10-30`,
App ID `0dp7n6ehj8r5ttfc0fj0au6gxkuy1nhw2kx70wussfa1mqj8tf80`. Its command is
`/sandstorm-http-bridge 8000 -- /opt/app/.sandstorm/launcher.sh`; the launcher
starts its packaged Node application. It contains a bundled MongoDB executable
and uses writable `/var`. No package program was executed.

The separate bridge configuration is a 16-byte empty Cap'n Proto struct: API path
empty, no powerbox API declarations, no ViewInfo. This was checked directly from
the archive, independently of the incomplete manifest projection. Therefore this
specific package cannot establish the external HTTP API journey. Its browser/DDP
application remains useful for the first real execution test. Agent access must
not be invented from the presence of an HTTP bridge port.

Source hashes: `spk.rs` `f4fc171119049297f034f4d4afe0a83356d32a388f37c34a7ab4f33166738f19`;
`capnp_wire.rs` `843d2b958a62f0afc138699b225bc7c481de342cd9b401efcbce469e9ca417ff`;
`manifest.rs` `9fbbcc91f1e9209cdda4bc38a7a1b8e8d19bee84a1ac0fda9bdb7fb99e82678d`.
The bounded local findings file hashes
`577b4ce8504ddc24ba92feb63b0df195c0b90fb3288fa9c61356fa5aa429b3a0`.
The scaffold does not establish the complete Bread crate's correctness or runtime.

## Real protocol changes the implementation target

The upstream supervisor provides a two-party Cap'n Proto socket on fd 3, exports
SandstormApi, and obtains the application's UiView. The packaged HTTP bridge
implements web/API sessions, response metadata and WebSockets. The physical
host should reuse that packaged bridge and implement the app-facing supervisor
contract, with a correctly materialized read-only package filesystem, writable
POSIX `/var`, and isolated temporary state.

Bread's simplified HTTP facade loses query strings and response headers, supports
only four methods, and has no WebSocket forwarding. Its archive flattening loses
symlinks and executable modes. Its permission gate conflates invalid authority
with a valid empty permission bitset. These need replacement or extension for
real compatibility; the in-process demo does not establish that compatibility.

[Wekan's upstream package definition](https://github.com/wekan/wekan/blob/main/sandstorm-pkgdef.capnp)
has API support and an observer role with zero permission bits. Wekan is the next
candidate, pending inspection of a specific signed release and its actual API
authentication behavior. The local capability gate must not infer that a valid
zero-bit role has no right even to open the application.

## First implemented repair

Bread `48166150e` preserves manifest command environments and prepends the
deprecated executable path as the upstream schema requires. The test fixture was
generated and independently decoded by the official Cap'n Proto CLI using pinned
Sandstorm revision `a97cf3ee19d3bf2761cd597583ca5d998de425d8`. Eight isolated
parser tests passed; complete-crate and packaged execution checks did not run.
[Portable fixture and scope](https://github.com/emberian/dregg/blob/48166150e/sandstorm-bridge/fixtures/command-manifest.md).

A subsequent separate frozen harness (`/tmp/spk-mini-probe-fixed`) combined the
real SPK reader with the edited manifest source, SHA-256
`542862e850e6da3e1398258f971c5b2ed754c2da0cd90f8e218f505e8a4ade61`.
Its release/offline run verified and decoded the same signed Simple Todos package
successfully. Both action and continue commands now retain
`PATH=/usr/local/bin:/usr/bin:/bin` and `SANDSTORM=1`. This adds actual package
compatibility evidence for the parser repair, still without executing the app.

## Core construction now owned

Mini's proposed ApplicationGrain law keeps the shared application lifecycle separate
from an AgentGrain's per-session work. Full package/snapshot commitments live in
typed content resources, joined with lifecycle transitions. Every app delivery can
cause effects, even GET. A generic no-op DRC receipt or a hash placed in its nonce
does not prove dispatch authority: the dispatcher needs a checked ingress binding
the exact request, current app/interface grant and agent/session generation.

Sol owns new `Kernel/ApplicationGrain.lean` and `ApplicationGrainLaws.lean` only;
native authoring, admission/replay and physical dispatch remain required integration.
There is no deployed DispatchPermit, SPK executor, or public app service yet.
