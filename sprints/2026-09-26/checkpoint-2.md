# Overnight construction checkpoint — September 26, 08:08 UTC

The overnight goal remains active. This checkpoint records real receiving results and the next coherent build; it is not a release or a completed hosted service. Read [checkpoint 1](checkpoint-1.md) for the earlier source changes and [the brief](overnight.md) for the assignment.

## Native receiving now exercised

The initial native host, SHA-256 `edad4dad46dd1f7d0084ec881f046e281c2a134ebdadb8cf28843935b5933308`, passed the full Lean umbrella, host compilation and native link. Its 591 compiled source hashes were verified. The [published manifest and receiving evidence](https://github.com/emberian/minidregg/tree/54e40e6/docs/evidence/2026-09-26-host-session) identify its exact basis and overlays. This executable predates the new grain authoring, fn opcodes 12/13, wide evidence profile and reply Message-ID fix.

The existing native client journey passed with birth, content and joint transactions and exact lost-reply recovery. Two additional tests replaced a live persistent host's image through the real SQLite CAS: a valid older prefix, and a different valid same-height branch. Cold hosts accepted each replacement as valid; the already-running host refused the rollback or changed verified prefix and closed permanently. This tests continuity within a running session, not an external anti-rollback anchor across restarts.

A real Unix-socket client journey also passed after exposing and repairing Darwin's `set_read_timeout` failure. One host process served source authoring, authorized observation and exact historical lookup/submission; both retries returned the original receipt. Altering the client's pinned configuration bytes was refused before dispatch. The current frame-bound update has focused Rust tests; it has not yet transported the maximal fn report.

## Distributed correspondence and host transport

A fresh fn exchange with **distinct Mini A/B identities** completed all 77 harness steps using the older pinned Mini executable. A second frozen-recipe run completed 80 steps with shell exit 0: B recorded its operation, revoked the gateway mutation grant, exported the original exact cursor/report, acknowledged it, and A recorded and acknowledged the reply. This supports historical ACK after revocation in that older direct-command path. It does not transfer the result to the new persistent opcodes. The gateway refusal probe separately used the newer receiver source, a valid ordinary mutation grant, and full unchanged-image comparison; [its source and evidence](https://github.com/emberian/minidregg/blob/59144e7/docs/evidence/2026-09-26-fresh-fn/gateway-negative.md) retain that distinction.

The Linux SSH connector now delivers output, interrupts on hard connection loss, and allows soft reconnection. Separately, the actual bubblewrap/systemd launcher stopped descendants that escaped the ordinary process group with `setsid`, withheld controller keys and state, and stopped worker units when their controller unit stopped. [These captures](https://github.com/emberian/minidregg/tree/3f97061/deploy/grain-host) are explicitly component tests. They have not yet demonstrated a native Mini grain running through that Linux service.

## Current construction boundary

Mini `591a5a9` checkpoints atomic grain birth and policy renewal, a delegated parent-generation witness for joint publication, multi-event portable evidence, and typed persistent B-side fn poll/ACK. A request supplies no fn path or untrusted cursor; operator-pinned manifests select the service, and ACK names an already accepted Mini transaction. A-side persistent reply operations are the next separate batch.

Mini `9024368` replaces recursive byte-stream encoding/decoding and strict comparison with stack-safe implementations. General Lean theorems establish equality to the prior wire and admission behavior, with the existing axiom gates unchanged. Actual 150,058-byte resource-command and 380,107-byte signed-call roundtrips passed, including malformed/truncated refusals. Larger full-consumer envelopes remain under test. The next full native build includes these changes and the new grain/fn authoring; no later source may inherit the initial binary's acceptance results.

The Rust grain controller and keyless MCP edge are committed at `3f97061`. Ongoing fixes cover queue fairness, prompt-phase gating, reconnect crash consistency, explicit signed reconciliation and named shared-resource reads. The native acceptance recipe now creates actual parent/tool/publication resources and exercises MCP through a deterministic ACP protocol peer. That is a component fixture, not a live model. Actual upstream Hermes ACP initialization passed locally; provider selection prevented session creation. Linux upstream installation is being prepared without credentials or model requests.

Fn's current source already widens signed-composite and consumer-poll representation bounds (`4979f0a35`, inspected at `3b6870a6`). Its consumer specification still describes the historical limits. Our qualified isolated image is `1a9dd747`, so Mini's selected reader profile and evidence remain bounded to that qualification. [Packet 002](https://github.com/emberian/minidregg/blob/2aeaf64/docs/FN-UPSTREAM-REQUESTS.md) requests a matching qualified image/profile and documentation alignment; it does not ask for a duplicate cap patch. Claude's shared checkout and live node remain untouched.

## Next receiving gates

1. Finish the coherent native build; run real signed grain lifecycle, publication, stale-parent refusal and reconnect/recovery acceptance.
2. Exercise B's public Unix-socket poll → signed Mini submit → exact fn ACK in the distinct-node exchange, then add A's typed route.
3. Export and independently verify an actual multi-event native prefix, then exercise the complete supported large-envelope path.
4. Run the native grain through Linux SSH, cgroup confinement and actual upstream Hermes. Keep configured allowance units separate from measured provider usage.
5. Connect named shared-resource reads/publications to the fn inbox and correspondence so the offered shell inhabits the same resource system.

Root is continuing integration. Mini checkpoints are pushed regularly. Bread's continuity entry was merged with independent incoming CI changes and pushed as `3e2506c8b`; staged and unstaged foreign patch bytes were unchanged. Its documented `DREGG_ALLOW_DEAD_DOC_REFS=1` exception was used only after the existing doc-reference gate failed (89 gating sites); the other push checks remained enabled.
