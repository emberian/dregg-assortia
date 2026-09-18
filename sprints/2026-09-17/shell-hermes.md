# Shell, external Hermes, and authored kernel resources

2026-09-17. Astra `/root/sprint_shell_hermes`. **Initial source investigation and implementation proposal; no builds, agent sessions, node probes, deployments, or Git commands were run.** Root subsequently authorized the partial-script receipt repair described at the end; those source edits have passed a scoped rustfmt parse check, with runtime validation pending. Sources below describe the initial inspected mechanism; recorded historical demos were not reproduced.

## Recommended product and execution shape

Build a **headless, authenticated programmable resource service** that is the receiving consumer of the selected kernel, with three equal clients: an ordinary shell running `dregg` commands/scripts, external Hermes using the DREGG MCP tools, and the cockpit. A friend should be able to author a resource's rule/program, install it with authority, call it from a script, share a narrower capability with another person or agent, and reopen the exact same resource/history from another client after restart.

The shell should initially be a useful ordinary shell with a DREGG CLI and a JS orchestration surface, not a newly invented shell grammar. This is a recommendation about the entrance, **not a proposal to preserve old core shortcomings**. The installation, invocation, authority, semantic execution, canonical patch, and durable publication all need to be completed through the kernel. Implement missing core machinery rather than forwarding raw effects to a permissive local ledger.

Keep two programming roles precise:

1. **Installed resource behavior:** versioned canonical program/rule data whose interpretation constrains or computes the accepted transition in the kernel. A method name must designate that installed behavior, and arguments/effects must be bound to the actual evaluated program and pre-state.
2. **Orchestration:** JS, shell pipelines, or an agent discover resources, compute proposals, invoke methods, await results, and compose operations. Their authority is the session's delegated capability. JS evaluation need not itself be a STARK-proven computation for every authorized kernel invocation to be checked. If a task promises proven program execution, the task uses the matching evaluator/compiler/proof path rather than treating a JS return value as proof.

The kernel and program lanes currently recommend the minidregg canonical typed carrier. `minidregg/docs/decisions/D-0002-canonical-hyperedge-kernel.md` is an accepted **minidregg architectural decision**, dated August 9; it does not by itself select the September 26 release runtime. The minidregg-first sprint receiving path remains a recommendation. Whatever receiving runtime is selected, these clients must share its real identities, authority state, durable operation IDs, and results.

## What exists and what each source actually establishes

| Source path | Existing mechanism | Sprint consequence |
|---|---|---|
| `deos-js/src/attach.rs:47–91, 288–372` | `WorldSink` supplies whole-ledger reads and effect commits. An attached affordance can hold literal effects; an empty effects vector uses the old counter-bump behavior. `fire_raw_effects_as` can name another actor, relying on the receiver for authority. | Reuse the scripting engine and client ergonomics; replace the overly weak actor/effects/hash interface with authenticated invocation and typed operation results. An `AuthRequired` lattice label is not a delegated credential. |
| `starbridge-v2/src/agent_attach.rs:77–98` | `WorldSinkAdapter.fire_effects` calls `World::turn` then `commit_turn`, **discarding the supplied method as `_method`**. | Preserve method/program identity through the new request and evaluator. Merely connecting the old bridge can erase method-scoped semantics. |
| `deos-hermes/src/main.rs:458–529` | MCP startup creates a fresh `AgentCipherclerk`, mints a session token, constructs fixed example key/token values and `bump`/`escalate` affordances, and calls `with_run_js`. It does not compose `with_world_bridge`. | Replace example startup with persisted participant identity and a real delegated session, configured to the selected service. Do not just add a socket flag around the private setup. |
| `deos-hermes/src/world_bridge.rs:71–103, 206–219, 240–268` | Wire is `WithLedger`, `FireEffects { agent, method, effects }`, and `MintOpenCell`. Peer trust rests on directory permissions; there is no in-band authenticated session. The read response includes all cells. | This wire is not the multi-user boundary. Introduce versioned authenticated requests, authorized reads, bounded frames, per-session quotas, structured errors, and operation-status lookup. Do not expose arbitrary actor selection to friends or agents. |
| `deos-hermes/src/node_hands.rs:195–218, 249–297` | `NodeJsHands` builds a `NodeWorldSink` from a cipherclerk and uses `run_attached_on`. Its sink is consumed by the first call; the second returns `SinkConsumed`. | There is already a remote path worth reusing or replacing deliberately. A persistent agent session requires a reusable authenticated client and recovery, not one-call ownership of the transport. |
| `dregg-sdk-net/src/node_world_sink.rs:121–190, 261–285, 448–471` | Builds and signs a rich `SignedTurn`, posts `/turns/submit`, then performs a receipt-list read. A not-yet-visible receipt becomes an error. Reads fail by not invoking the callback. | Preserve signed participant identity, but replace Boolean/error finality with `Pending`, `Refused`, `DurablyCommitted`, and transport-unknown states; reconcile exact operation identity after interruption. A missing receipt is not evidence that nothing committed. |
| `dregg-sdk-net/src/deos_server.rs:1–22, 132–165` | Discovery advertises names and authority labels; the caller supplies effects. | Discovery does not establish installed program execution. Implement an invocation that resolves pinned behavior at the receiver and derives/checks its actual effects. |
| `deos-hermes/tests/node_backed_round_trip.rs:1–29, 35–37, 86–104` | The integration test uses `dregg_sdk_net::test_support::TestNode` with a real TurnExecutor and a funded open cell. | Useful transport/executor test source, not evidence of the intended full node, durable restart, current proof mode, or external Hermes consumer. |
| `cli/src/main.rs:53–87`; `cli/src/commands/turn.rs:1–15, 27–77` | Existing CLI packaging, profiles, JSON output and shell completion are useful. Generic turn commands use node-operator bearer JSON ingress with a thin effect set; quick actions default to operator authority. | Keep the CLI, add the participant resource/program commands against the shared request API. Do not hand out the node operator's bearer as each friend's identity. |
| `starbridge-v2/src/bin/dregg_mcp.rs:273–302, 315–351` | Inspector harness accepts viewer/rights parameters and operates its session World; other tools include boot/restore. | Reuse its reflection projections and interaction vocabulary, but do not deploy its test/operator surface as the authenticated friend-facing server. |
| `deos-hermes/src/mcp_server.rs:489–554, 603–641` | `terminal` admits and receipts the command, but its Unix body ignores `_command`, executes sandbox probes and an acknowledgment, then claims the command ran. | Implement the real command/job runner, capture exit/output, and publish its completion through the resource path. A copy change alone does not meet the task. |
| `deos-terminal/src/model.rs:218–275`, `transport.rs:1–38` | Actual PTY and terminal transport exist. Browser transport's URL is ambient in the inspected source. | Connect a terminal to the authenticated per-user shell/job session; do not equate PTY existence with authorization or confinement. |

Two particularly concrete correctness repairs are independent of the final carrier:

* `deos-js/src/js.rs:874–895` extracts the attached applet after evaluation, but returns only `Err(e)` if JS throws. The applet may already contain committed receipts. `deos-hermes/src/run_js.rs:344–362` then returns `fires_committed: 0` and an empty receipt list. **Preserve operation outcomes and the applet/client even on script error.** A script that commits once and then throws must show that commit and must not silently repeat it when resumed.
* `deos-hermes/src/tool_effects.rs:42–53, 147–169` uses a single FNV-derived field plus script length for the script witness. The comment that distinct scripts produce distinct witnesses is false as a general binding claim. Bind the exact canonical request/script/program bytes using the selected full-width digest representation and retain retrievable source artifacts. This is the same provenance obligation as program installation, not an excuse to leave a weak event forever.

The local-first lane identified a newer SDK transport that should be unified rather than copied. I checked `dregg-sdk-net/src/remote.rs:432–480, 538–555`: `RemoteRuntime` signs the federation-bound nonce, uses per-agent receipt continuity, and retries a head race by re-signing only the envelope. `NodeWorldSink` still reads a global receipt head; current ingress compares against the agent's head (`node/src/signed_turn_validation.rs:663`). `RemoteAuthorizedTurn::submit` still returns its `RemoteReceipt` immediately on HTTP `accepted`, so its signing mechanics are a useful existing basis but its completion type is not the durable operation contract. Reuse and repair these common SDK mechanics instead of adding a sidecar with its own identity/nonce rules.

## The canonical operation contract to implement

Use the carrier/program/resource lanes' canonical types rather than creating a second semantics in MCP. A transport envelope can contain the following fields, with canonical binary encoding and generated JSON/CLI projections:

* protocol version; kernel semantics/evaluator version; deployment/federation identity;
* authenticated subject plus key epoch; session/delegation reference and evidence;
* typed resource ID; expected revision/root; expected program ID and revision;
* installed entry/method and canonical typed arguments; full argument digest;
* exact declared or derived effects digest, cost quote/bound, policy ID/epoch;
* nonce, request/operation identity and replay domain; height/deadline policy;
* authoring/source provenance references when relevant, without embedding signing secrets.

These are not novel substitutes for the kernel: `minidregg/Theory/TypedAuthorization.lean:89–106` already defines domain, semantics, federation, subject, subjectKeyEpoch, typed target/verb, argsDigest, effectsDigest, nonce, height, preStateRoot, policyId, policyEpoch and cost. The program entry/version and practical invocation binding still need integration. The service must derive/check request data from the actual program and canonical state; it must not accept independently mutable roots or let a supplied `effectsDigest` stand in for evaluation.

Resolve discovery, reads and writes under the same authenticated session. A client-supplied `actor`, `viewer`, or `rights` field must never manufacture authority. A person's SSH identity is a way to start an enrolled session; the authenticated DREGG principal and delegated permissions remain explicit. Long-lived root keys stay outside the untrusted shell/agent process; the process receives only the capability/signing access authorized for its session. The receiving kernel checks current authority and revocation at commit, not just when the tool list was constructed.

The response should separate:

* **Refused:** typed reason, stage, request ID, and no committed resource mutation.
* **Pending:** operation ID, accepted request digest, and status/subscription endpoint. This acknowledges custody of a request, not success.
* **DurablyCommitted:** exact operation/request ID, program/evaluator identity, pre/post resource revisions, durable event/receipt identity and applicable finality evidence. Readback resolves the same pinned state.
* **Transport unknown:** request identity retained so reconnect queries status; never blindly reconstruct/sign a new request with a fresh nonce.

One invocation/hyperedge is atomic under the selected kernel contract. A script can contain multiple such invocations and partially finish: retain every completed/pending outcome if a later call or JS evaluation fails. If a user asks for a joint transaction, they submit an explicit batch/hyperedge whose whole footprint the kernel validates; do not imply that an entire arbitrary JS script rolls back.

The resource lane proposes exact content/behavior/presentation revisions and a single content+event durable transaction. Its strong existing source is `minidregg/Assurance/HyperdocumentGuardedDurable.lean`: `PublicationPlan` retains the exact publication, canonical post bytes, authority pre-root and replay envelope. It explicitly requires a physical `ImplementationRefinement`; a successful local event append is not that completion.

## Actual entry surfaces and product tradeoffs

| Entrance | What friends get | Concrete work | Recommendation |
|---|---|---|---|
| SSH + ordinary shell + `dregg` CLI/JS runner | Familiar shellserver, scripts, pipes, files for drafts, easy co-development; same resource IDs available elsewhere | Per-user/session enrollment; new program/resource commands; authenticated service; real process isolation; persistent workspace/session handling | Primary human entrance. A CLI is not a lesser kernel integration if every resource operation reaches the real evaluator and durable receiver. |
| External Hermes + DREGG MCP | A familiar agent that can discover, author and invoke the same resources | Session-specific tools, schema discovery, complete typed results, real external process confinement and provider access; ACP for conversation/lifecycle | Build alongside the CLI, against the same service. Do not replace Hermes with the Rust stand-in and call that external integration. |
| Cockpit + inspect/author terminal panes | Visual resource graph, rich view, delegated collaboration and provenance | Replace private editor ownership, read current canonical revisions, publish edits through the service, reconnect terminal/agent sessions | Parallel receiver cutover. It should not need to own the ledger process for a friend's shell to work. |
| New DREGG shell language | Potentially elegant direct composition | Parser, language tooling, quoting, editor, debugging and an additional authoring compatibility commitment | Optional later language design. No user instruction makes this a prerequisite. |

Suggested command sketch, **not an existing CLI claim**:

```text
dregg inspect <resource>
dregg program install <resource> --source rules.json --expect <revision>
dregg call <resource>@<program-revision> <entry> --args args.json
dregg run workroom.js
dregg op status <operation-id>
dregg share <resource> --to <principal> --verbs observe,append
dregg history <resource>
```

The JS API can offer typed `resources.inspect/invoke`, `programs.install`, `operations.wait`, and an explicit batch constructor. Generate discovery/schema and documentation from the actual accepted program vocabulary. The runtime should return structured values, not the present i32-only completion plus receipt count.

## External Hermes: current installed source, not the June memory

I located but did not execute the installed Homebrew Hermes. `/opt/homebrew/bin/hermes-acp` points to the **2026.8.31** package; its launcher selects the packaged Python ACP entry point.

Under `/opt/homebrew/Cellar/hermes-agent/2026.8.31/libexec/lib/python3.13/site-packages/`:

* `acp_adapter/session.py:140–155` still uses `toolsets or ["hermes-acp"]`; its `_make_agent` at `:637–641` explicitly starts with `["hermes-acp"]` plus configured MCP servers.
* `acp_adapter/server.py:1126–1186` registers provided MCP servers then refreshes an **additive** tool surface. It retains `hermes-acp` as fallback and includes configured memory-provider tools.
* `acp_adapter/permissions.py:1, 117–155` supplies dangerous-command approvals. The current server additionally installs edit approval handling at `server.py:1960–1972`. This is still **not a universal callback proving every tool invocation crossed the DREGG kernel**.
* On the DREGG side, `deos-hermes/src/acp_client.rs:461–504` performs the gateway action on `session/request_permission`. `:543–555` merely records `tool_call`/`tool_call_update` notifications. A tool that needs no ACP permission request does not enter that gateway branch merely by emitting a notification.

Therefore implement both the actual external process and the tool authority path:

1. Launch the real external Hermes in a scoped hosted workspace, retaining its ACP conversation/session protocol.
2. Register DREGG MCP with a session-specific authenticated connection, not a freshly minted private ledger. Tool-call correlation maps to the canonical operation ID.
3. Offer DREGG read/program/invoke/history tools and the orchestration runner. Do not make mutation depend on whether a model happened to trigger an ACP permission dialog.
4. Reconcile completed/failed tool updates with service receipts/status. Do not execute the same script once in an ACP permission hook and again in the MCP tool handler. Exactly one service invocation owns the operation.
5. Constrain Hermes's ordinary filesystem/process/network surface through the host sandbox and explicit granted workspace. A tool-list restriction is useful ergonomics and reduces accidental paths; it is not the sole authority boundary. If choosing a DREGG-only tool surface, implement an explicit-empty session toolset override in a version-pinned Hermes source/package and verify no additive base or configured MCP leaks back in. Do not patch the globally installed package in place and forget the provenance.
6. A permitted local draft file write remains a local workspace operation; installing it or changing a shared resource must use the canonical kernel operation. If a filesystem materialization is offered as a shared-resource editor, its save/import is the same accepted publication path, not a direct heap mutation.

`DreggHost` has real confined Rust brain paths and later live HTTP brain support; its source does **not** make an external Python Hermes process confined merely because the module uses the name Hermes. Preserve those paths where useful, but validate the explicitly desired external consumer.

## Real shell execution and jobs

Complete the current `terminal` path as a real, bounded process operation. The input binds executable/runtime image, argv or exact shell script, cwd/workspace revision, environment allowlist, input artifacts, CPU/memory/time/output limits and permitted network. The host records admission, starts the actual process, streams bounded stdout/stderr, handles resize for interactive PTY, supports cancellation, and publishes exit status/output artifact identities. An admission receipt is not process completion and a process exit is not result correctness.

There is a concrete existing spawn substrate to extend: `sel4/dregg-firmament/src/process_kernel.rs:1304–1418` has `spawn_pd_confined_exec`, exact image selection, argv/env construction, stdout/stderr pipe and confinement before exec. `sandbox.rs:136–152, 801–809` carries `exec_image` and emits the macOS image rule. **Do not infer Linux parity:** the inspected Linux `confine_sealed` (`sandbox.rs:923–930`) passes only `read_paths` to Landlock and installs the sealed filter; `:977–1033` denies `execve/open/openat`. A real Hermes/shell workload on hbox/persvati requires a deliberate executable Linux process tier and corresponding sandbox tests, not reusing the probe profile or disabling confinement globally. Profile selection must be checked, not silently approximated.

The process runner may reuse ordinary Unix shell behavior while the DREGG resource effects remain authorized kernel operations. For public contributed computation, the economic lane proposes pinned DREGG program evaluation over exact public resource revisions, with a declared checker over full output/effect footprint. Such jobs can reuse the core evaluator/proof path. General OS jobs produce an **execution observation** until their selected checker establishes a stronger result. Provider reputation or custody must not consume the old terminal probe receipt as evidence of delivery.

## Implementation bundles and ownership boundaries

These are proposed bundles to assign, not completed work. They can run in parallel behind a shared checked-in contract. Fixes should eliminate the old receiving paths as the new ones land; do not leave an alternate private default behind the same product command.

| Bundle | Primary modules / ownership | Concrete closure |
|---|---|---|
| 1. Canonical invocation + program lifecycle | Kernel carrier/program lanes; minidregg typed request, program codec/evaluator, install/invoke accepted effects | Authored program bytes and method arguments determine/check the accepted patch. Exact code/evaluator identity, authorization pre-root and source bindings survive lowering, proving and commit. |
| 2. Physical resource receiver + status | Resource/history lane; selected headless service/store | One durable content+event operation with idempotency, authorized readback, crash recovery and status. Same resource available independently of GUI or agent lifetime. |
| 3. Session/identity + reusable client | Shell lane; SDK transport and host bootstrap | Persisted human principal, narrower revocable agent session, authenticated typed envelope, authorized snapshots, Pending/Committed/Unknown handling, no operator-bearer substitution. |
| 4. Real CLI and JS authoring | `cli/src/commands/*`, `deos-js/src/attach.rs`, `js.rs`, shared API types | Install/update/invoke/read/history/share use bundle 3; method preserved; no counter fallback used as a generic program; script error retains prior outcomes; explicit atomic batch. |
| 5. External Hermes/MCP/ACP integration | `deos-hermes/src/main.rs`, `mcp_server.rs`, `run_js.rs`, `acp_client.rs`, `node_hands.rs`; pinned external integration if required | Actual external Hermes calls the typed service repeatedly, receives structured status, can author/install/invoke on shared resources, and cannot amplify its session authority. No double execution at ACP/MCP seams. |
| 6. Real process/job tier | `sel4/dregg-firmament/src/{process_kernel,sandbox}.rs`, terminal transport, host runner | Real requested commands execute with observed exit/output, bounded resources, confinement and cancellation on target Linux hosts. Broker outcomes become resource results under the applicable checker. |
| 7. Cockpit receiving cutover | Resource/history lane with cockpit/editor ownership | Card/editor actions and panes use the same canonical resource, program revision, operation result and history; no separate private authoring applet supplies a misleading success. |
| 8. Deployment and consumer evidence | Build/infra lane with shell/service owners | A clean release build launches the selected features and actual executables; two independent clients and restart prove the service contract on hbox or persvati. |

The immediate carrier-independent partial-progress repair is narrowly owned by `deos-js/src/js.rs` plus `deos-hermes/src/run_js.rs` and their actual consumer tests. The full service/client cutover spans bundles 1–5; a socket-only patch cannot satisfy it.

## End-to-end acceptance

Use one mixed programmable space with at least a shared workroom resource and a social/story/game resource consuming the **same** authoring/invocation machinery. Different applications are data/programs over the common contract, not two bespoke demo backends.

1. **Real participants:** two independent enrolled principals connect through shell/CLI and external Hermes. No test-only symbolic authority, fixed demo identity, global operator token or privately minted ledger in their resource path.
2. **Author and install:** one writes canonical program/rule data, installs it on an owned resource, and retrieves the stored bytes/digest/evaluator version after restarting both client and service. Changing existing-vocabulary behavior requires no host rebuild. Adding a genuinely new primitive correctly goes through kernel implementation/proof/version work.
3. **Invoke and refuse:** the authorized operation executes under that installed program; wrong method/version/args/effects/pre-root, out-of-scope target and revoked delegation refuse without a hidden resource mutation. Read authorization also applies; a failed or unauthorized read cannot silently resemble an empty world.
4. **Cross-client result:** another participant sees the exact committed revision/history through a different client. A human and Hermes act on the same resource ID, with the agent receiving narrower rights.
5. **Crash and retry:** kill/disconnect after submission but before acknowledgment. Recovery by operation identity returns the original result or resumes the pending request, with one mutation/charge/event. Stale-state refusal remains distinct from network ambiguity.
6. **Partial scripts:** commit one operation then throw in JS. The caller sees the committed receipt plus script error. Reconnect/resume cannot claim zero commits or duplicate the first operation. An explicitly joint batch separately demonstrates all-or-none behavior.
7. **Actual external consumer:** capture a real external Hermes ACP/MCP run issuing and reading at least two operations, including a refusal and corrective retry. Record executable/package revisions and selected tool/session configuration. Direct MCP tests and Rust ACP stand-ins alone are insufficient for this acceptance.
8. **Actual shell:** execute a command producing a unique expected stdout/artifact and a controlled nonzero exit. Verify its actual output/exit, cancellation and forbidden file/network/process reaches under the selected host profile. Probe-only verdicts cannot pass this test.
9. **Kernel assurance:** carry the source-authoritative evaluator and selected proof/producer mode through the actual receiver. Do not convert missing native coverage, invalid proof projection, stale program witness or codec gaps into an insecure fallback. The core/proof lanes own closing these obligations.
10. **Contribution path:** run the first pinned public DREGG computation on a second participant-controlled node, check its declared result and publish it as a usable resource. Resource receipt, computation verdict, provider reputation and Solana custody remain distinct linked facts with the exact operation identity.

The report's source findings identify work to close, not release limitations to accept. The main integration decision is the concrete source-authoritative receiver and program representation; once selected, these bundles need to converge on it rather than each landing a green isolated substitute.

## Authorized implementation checkpoint (validation pending)

Root authorized the script-error receipt repair independent of the carrier selection. Current edited files:

* `deos-js/src/js.rs`: attached evaluation returns the applet and actual receipt tape with a distinct `js_error` even when the script throws. Runtime target-loss remains an outer error; callers cannot read it as a clean zero-fire run.
* `deos-hermes/src/run_js.rs`: forwards the attached outcome instead of replacing a script exception with zero committed fires and no receipts.
* `deos-hermes/src/mcp_server.rs`: preserves admission separately from script status; a script exception now yields MCP `isError: true` while retaining the complete ordered resource receipt list and count. Existing `receipt` remains the first resource receipt for `run_js`, or the old gateway receipt for `terminal`. Additive `_deos` fields are `admitted`, `receipts`, and `scriptError`. The Unix terminal probe body is unchanged; its separate implementation obligation remains.
* `starbridge-v2/src/card_pane.rs` and `main.rs`: direct runtime consumers explicitly reject failed script completion and include prior committed receipts in diagnostics.
* `starbridge-v2/src/agent_attach.rs`: extends the existing real-World test with fire-then-throw and no-fire error; compares the retained receipt to the actual World's receipt and checks its field/height.
* `deos-hermes/tests/world_bridge_e2e.rs`: extends the existing MCP/socket/served-executor test with two fires then throw, runtime and syntax errors before any fire, continued readback, and exact equality of the MCP receipt list with the served ledger. The JS scenario runs on a bounded 64 MB stack thread, following the existing SpiderMonkey test convention. The two touched tests' old affordance tuples were updated to the current `Requirement::AtLeast` type.

All seven files passed rustfmt's parse check without modifying unrelated formatting. No Rust build or test has yet run. Intended narrow checks are the named `run_js_over_the_world_bridge_lands_on_the_served_world` and `agent_run_js_drives_the_live_cockpit_world` tests with their actual JS features, plus the feature-enabled direct consumer build. This repair does not create Pending/retry identity guarantees that the current sinks lack.
