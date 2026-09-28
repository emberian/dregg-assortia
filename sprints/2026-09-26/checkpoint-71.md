# Checkpoint 71 — app recovery running; model, tools and transport converge

September 27 local / September 28 UTC, 2026. The full platform goal remains
active. No combined browser/Hermes/GitWeb/fn deployment is yet established.

The app prerequisite audit found **both** parent7901 and tool7902 detached.
Mini **61405c5** preserves the refused reserve43000 and adds signed parent
attach/reserve, tool attach/reserve, then the retained app/session birth and
reopen checks. It also repairs the future fixture's prerequisites. Root
reviewed the full source and reran syntax/ShellCheck before launch. The one
bounded USER unit `mini-spk-platform-r3-app-attach-recovery-client-session.service`
was independently observed active with PID3248238 and invocation
`eb28b8d18f7e4a9f8ae0fe3d280dad67`. This is a running attempt, not an app
receipt. client_session owns the r3 Store exclusively; do not relaunch on
observation timeout or clear its retained attempts.

## Committed integration and actual component evidence

- **18166e5** adds hosted Hermes GitWeb read/edit tools over the existing Mini
  metered dispatch path. Real Git CGI exercised empty-repository first push,
  readback and second push; 135 runtime tests and strict Clippy passed. Review
  repaired invocation-local proxy authentication, hidden public MCP exposure,
  and read-mode handling of Git upload-pack POST. Actual SPK use remains next.
- **f9b2e53** records the real local Bonsai2 PTQ1 model on hbox's AMD GPU:
  authenticated loopback chat, structured tools, SSE and a tool-result round
  trip. The model is not yet joined to hosted Hermes through Mini. Upstream
  Hermes6d8a8beb is staged with a locked ACP environment; its direct check
  passes, but the isolated launcher encountered hbox's namespace restrictions.
  linux_hosting is investigating scoped host configuration, not host-network
  fallback.
- **b52b20c** records the actual isolated format8 fn node, private loopback
  listener, protected control socket, TLS/auth checks and empty registered
  consumer. It also records the source-qualified d48aa81 native Host. The
  malformed-input probe on that older Host timed out during history replay;
  it is inconclusive. **8c13c42** rejects malformed grant ingress before replay
  and exposes the source ticket digest; its qualified native successor is
  building separately. No accepted event27 runtime result is implied.
- **d001233** imports an explicitly chosen Git commit/file into an existing
  Mini content resource, retains the exact signed mutation and recovers by
  lookup plus signed readback. Root reran Git-selection and fake-Mini recovery
  checks, including the private socket. These are component tests, not a real
  GitWeb-to-Mini import.
- **b307251**, followed by **b52b20c**, joins selected content publication to
  fn and independent recipient/frontier/ACK/readback. Root reran recovery
  command tests, including latest absent lookup and oversized assembled article
  refusal. No real selected article has been published. Recipient preparation
  is separate from r3; source selection remains owner7's content8001/cap89.

Evidence is retained under Mini `docs/evidence/2026-09-27-hermes-gitweb-tool`,
`2026-09-27-bonsai2-local`, `2026-09-27-fn-preview-node`, and
`2026-09-27-native-host-d48aa81`. Source and test scopes remain distinct from
live acceptance.

Next: collect the app recovery's exact outcome; complete INSTALL/START and
source-accepted event22/27 route issuance; join the isolated unforked Hermes
worker to local inference and shared GitWeb; then select actual app bytes for
the fn journey. STOP supervisor partial-write recovery has seven focused
passing tests and is under independent review before root adoption. Paid
OpenRouter credits remain the agreed additional offering, with no paid call
or token transfer performed.
