# Hosted upstream Hermes: protocol edges and DREGG boundary

**Scope and evidence.** This is a read-only source investigation on 2026-09-19. I did not build, test, launch Hermes, start a service, inspect a live network endpoint, use SSH, or mutate either repository. The upstream checkout at `/Users/ember/pug/hermes-agent` declares version **0.17.0** in both `pyproject.toml:10` and `hermes_cli/__init__.py:17`. “Upstream Hermes” below means that checkout. “Existing DREGG integration” means `/Users/ember/dev/breadstuffs/deos-hermes`; it is a separate Rust ACP client/MCP prototype and must not be treated as Nous Hermes itself. Product intent is the complete hosted experience plus, if practical, external unforked Hermes (`/Users/ember/dev/dregg-assortia/sprints/2026-09-19/direction.md:5-19`).

## Finding

An **unmodified, version-pinned upstream Hermes is a source-supported candidate for the hosted product** if the grain is the isolation and persistence unit. This investigation does not constitute runtime acceptance of that deployment. Run Hermes normally inside a per-tenant grain, persist its Hermes home and working files, and let the user enter through SSH into the ordinary Hermes CLI/TUI. That preserves the useful upstream surface instead of recreating it: the ACP preset alone includes terminal/process, files, web, browser, skills, memory, session search, code execution, and delegation (`H/toolsets.py:371-387`, where `H` is `/Users/ember/pug/hermes-agent`).

The protocols then have distinct roles:

* **SSH** transports the complete interactive shell and Hermes CLI. It is also a practical carrier for ACP stdio (`ssh grain hermes-acp`) through a small client-side bridge.
* **ACP** drives a Hermes conversation, streams UI/tool events, and creates/loads/resumes its sessions. It is not a network daemon or a universal execution-control callback.
* **MCP** adds tools that Hermes may call. It is the right adapter from Hermes into the canonical DREGG operation service. It does not remotely drive Hermes.
* **Provider configuration** can send inference through a DREGG credential/metering proxy without modifying Hermes. The grain should receive a short-lived scoped proxy token, never the user’s raw OpenRouter key.

The DREGG supervisor must remain outside Hermes and own grain lifecycle, OS confinement, budgets, credential delegation, and durable DREGG operation semantics. ACP and MCP are adapters to that contract, not the contract itself.

## Modes that preserve unforked upstream Hermes

| Mode | What stays upstream-configurable | DREGG-owned adapter/boundary | Practical limit |
|---|---|---|---|
| Hosted full experience | Upstream CLI/TUI, gateway, sessions, skills/memory and all normal tools run unchanged inside the grain; local terminal backend | SSH account/entry, grain lifecycle, persistent volumes, sandbox, resource meters, inference proxy and DREGG MCP | Strong isolation comes from the grain, not Hermes tool permissions |
| Remote editor/control of hosted grain | Upstream `hermes-acp` stdio process and its session new/load/resume protocol | Authenticated SSH/stdio or relay that selects the grain and carries bytes | ACP has no built-in network listener; one driver per conversation is still required |
| External Hermes using DREGG | External installation keeps its own conversation/provider state; standard configured HTTP or stdio MCP adds DREGG resources, and upstream SSH terminal backend can optionally target a hosted workspace | Tenant-authenticated DREGG MCP endpoint and optional SSH workspace credentials | MCP is additive and agent-to-tool; it neither replaces built-ins nor controls the agent |
| External controller operating a hosted Hermes grain | Hosted grain still runs the upstream ACP server and persistent state | Controller opens an authenticated ACP-over-SSH/relay channel to that grain | This needs a transport/session-routing adapter, not an upstream Hermes fork |

In all four modes, the inference broker can remain an upstream configuration choice: OpenRouter mode supports an alternate `OPENROUTER_BASE_URL`, and named custom providers support a base URL plus `key_env` and transport mode. The DREGG-specific code lives at the broker, supervisor, ACP transport edge, and MCP service.

## What persists, and what can coexist

`HERMES_HOME` is the upstream source of truth for Hermes state (`H/hermes_constants.py:54-76`); configuration and `.env` are under it (`H/hermes_constants.py:590-607`), and the session database is `{HERMES_HOME}/state.db` (`H/hermes_state.py:108`, `H/acp_adapter/session.py:401-418`). The database is SQLite/WAL and explicitly anticipates gateway, CLI, and worktree-agent processes sharing it (`H/hermes_state.py:658-728`). Session rows retain source, model/configuration, system prompt, parent, and cwd and can be reopened (`H/hermes_state.py:1339-1409`).

ACP is durable rather than process-bound. Its session manager persists history to the shared database and transparently restores an evicted/restarted ACP session (`H/acp_adapter/session.py:169-242`, `:423-543`). `session/load` and `session/resume` replay the prior transcript before returning (`H/acp_adapter/server.py:1129-1209`). Persisted ACP provider metadata includes provider, base URL, API mode, model, and cwd, but not the API key; restore recreates the agent and resolves credentials again (`H/acp_adapter/session.py:433-445`, `:488-526`, `:603-613`). This is compatible with rotating a scoped inference token.

CLI and ACP can share one `HERMES_HOME` safely at the storage level. The CLI’s explicit ID resolver does not filter by source, and its resume path loads any matching row/history (`H/hermes_cli/main.py:1263-1297`, `H/hermes_cli/cli_agent_setup_mixin.py:444-521`). The ordinary CLI recent-session browser does filter to source `cli` (`H/cli.py:5977-5992`), while ACP restoration explicitly rejects non-ACP source rows (`H/acp_adapter/session.py:471-490`). Cross-frontend continuation therefore exists asymmetrically in current code; it should not be advertised as a stable interchange guarantee without an acceptance test for tool/history shapes.

Multiple frontends may coexist against the database, but **one driver should own a conversation at a time**. ACP’s per-session `runtime_lock` and queued-prompt handling protect concurrent prompts only inside one ACP process (`H/acp_adapter/session.py:169-182`, `H/acp_adapter/server.py:1365-1381`). There is no cross-process conversation lease. A DREGG supervisor lease should prevent a CLI, gateway, and another ACP process from advancing the same session simultaneously. Separate Hermes sessions can operate concurrently in one grain.

For restart/reconnection, persist at least:

1. `HERMES_HOME` (state DB, config, skills, memory and Hermes-owned state);
2. the user workspace/home needed by tools;
3. the DREGG grain identity and operation journal outside Hermes;
4. no long-lived raw provider credential in either volume.

`HERMES_HOME` alone is not a filesystem sandbox. Upstream deliberately distinguishes it from the OS user’s real `HOME`; host installs default tool subprocesses to the real home, while containers may use `{HERMES_HOME}/home` (`H/hermes_constants.py:412-465`).

## ACP: useful remote control, not the authority boundary

The upstream ACP adapter is a **stdio JSON-RPC process**: stdout is reserved for protocol traffic, it loads the Hermes environment, and calls `acp.run_agent(...)` (`H/acp_adapter/entry.py:1-14`, `:75-104`, `:212-257`). To drive a hosted grain remotely without an upstream fork, the client or DREGG edge can spawn `ssh <grain> hermes-acp` and relay its stdin/stdout. This preserves the upstream ACP implementation; the bridge supplies authentication, grain lookup, transport lifetime, and audit correlation. A long-running custom network wrapper is optional rather than necessary for the first hosted experience.

ACP-provided stdio, HTTP, or SSE MCP servers are registered during new/load/resume and added to the agent tool surface (`H/acp_adapter/server.py:788-850`, `:1109-1188`). The client must resend dynamic MCP descriptors when loading/resuming: ACP persistence saves provider/cwd/history, not the per-session MCP server definitions (`H/acp_adapter/session.py:423-445`). Use a session-specific authenticated DREGG MCP URL or a stdio adapter whose environment contains only an opaque session credential.

ACP does **not** make those MCP tools exclusive. `_expand_acp_enabled_toolsets` defaults to `hermes-acp` and appends `mcp-<server>` (`H/acp_adapter/session.py:140-155`); `_make_agent` hardcodes `['hermes-acp']` plus configured MCP servers (`H/acp_adapter/session.py:585-600`). Consequently, an unmodified ACP session retains Hermes terminal/file/browser/etc. alongside DREGG tools. For the complete hosted experience this is desirable inside a real grain sandbox. If a product mode requires a DREGG-only tool list, it needs an upstream option for replace/explicit-empty semantics or a maintained fork; passing only one MCP server does not achieve it.

ACP permission is also selective. Its callback adapts `request_permission` specifically to Hermes’s dangerous-command approval API and fails closed on timeout (`H/acp_adapter/permissions.py:107-166`). The callback is thread-local (`H/tools/terminal_tool.py:161-200`) and is installed around the agent run, alongside a separate edit-approval requester (`H/acp_adapter/server.py:1398-1428`, `:1446-1511`). Terminal invokes the approval path only when pre-exec guards flag a command (`H/tools/terminal_tool.py:2084-2117`); ordinary commands need no ACP permission request. ACP `tool_call` updates are progress/observation messages, not interceptors.

Therefore DREGG authorization must occur in the DREGG MCP/service operation itself. ACP events may correlate UI state to a DREGG operation ID, and dangerous/edit approvals remain useful user interaction, but neither is evidence that every tool was authorized or executed by DREGG.

## MCP and remote tools

Upstream MCP supports stdio subprocesses and HTTP servers with headers (`H/cli-config.yaml.example:801-838`). Hermes namespaces their tools as `mcp_<server>_<tool>` (`H/tools/mcp_tool.py:3637-3666`), so a DREGG server advertising `terminal` becomes, for example, `mcp_dregg_terminal` rather than replacing the built-in `terminal`. Registration is process-global and idempotent by server name (`H/tools/mcp_tool.py:2783-2808`, `:4019-4059`); two ACP sessions in one process cannot safely reuse one server name for different tenant endpoints because the second registration is skipped. Use one Hermes/ACP process per grain as the simplest tenancy boundary, or globally unique server names plus an explicit cleanup/rebind design.

Upstream also has a coherent **SSH tool backend**, but it represents a different topology from “Hermes hosted in the grain.” It keeps the agent local while terminal calls execute remotely (`H/cli-config.yaml.example:195-208`). Each call spawns SSH, while cwd and environment snapshots persist and ControlMaster reuses the connection (`H/tools/environments/ssh.py:36-98`). File tools share the same configured terminal environment and live cwd (`H/tools/file_tools.py:642-772`, `H/tools/file_operations.py:722-791`), so terminal/read/write/patch act on the remote workspace together. The sync helper separately mirrors selected credentials, skills, and cache (`H/tools/environments/file_sync.py:50-76`), not the whole workspace or the conversation DB.

This SSH backend is useful when an externally installed Hermes should use a DREGG-provided compute workspace. It does not itself provide DREGG authority, metering, or isolation, and it leaves conversation/config/provider state on the machine running Hermes. For the hosted product, running Hermes **inside** the grain with the local backend is simpler and more complete; the grain supervisor provides the confinement. For external unforked Hermes, offer both an authenticated DREGG MCP endpoint for resource operations and, optionally, an SSH workspace for ordinary terminal/file work.

The host sandbox is load-bearing. Upstream’s own file-read denial explicitly states that it is not a security boundary because the terminal runs as the same OS user and can `cat` credential files (`H/agent/file_safety.py:148-184`, `:226-289`). Tool-list filtering and dangerous-command prompts do not replace a tenant UID/VM/container, mount policy, cgroup/resource limits, and network policy.

## Inference endpoint and credential custody

Current upstream can use a custom provider without code changes. New-style `providers:` entries accept a base URL, `key_env`, and `api_mode`/`transport`, and the runtime resolver loads them (`H/hermes_cli/runtime_provider.py:508-610`). Named custom runtimes use the configured base URL and default to OpenAI chat-completions mode unless another supported mode is selected (`H/hermes_cli/runtime_provider.py:804-924`). The general resolver applies named custom configuration before built-in provider resolution (`H/hermes_cli/runtime_provider.py:1388-1465`). For OpenRouter specifically, `OPENROUTER_BASE_URL` remains supported, including explicit OpenRouter proxy context and OpenRouter-key selection; `OPENAI_BASE_URL` is deliberately no longer the generic endpoint override (`H/hermes_cli/runtime_provider.py:958-1032`).

The recommended credential path is:

1. The DREGG credential service stores the user’s raw OpenRouter key.
2. The supervisor issues the grain a revocable opaque token scoped to tenant/grain, model/routing policy, request and token budgets, expiry, and an audit/session identity.
3. Configure Hermes either as `provider: openrouter` with the DREGG broker as `OPENROUTER_BASE_URL` and the scoped token as `OPENROUTER_API_KEY`, or as a named custom OpenAI-compatible provider using `key_env`.
4. The broker validates scope, forwards with the raw key, meters provider usage, and journals request/attempt/result identities independently of host CPU/storage and DREGG kernel-operation accounting.

The token is visible to the Hermes process and its terminal; its narrow scope is what makes that acceptable. A raw OpenRouter key placed in the grain’s `.env`, config, or process environment is reachable by that same process regardless of file-tool guards. Protecting a raw credential from a fully capable same-process terminal would require a separate credential/inference process or an upstream credential-helper/transport change.

For the “complete” experience, the broker must faithfully implement the selected upstream wire behavior: streaming, tool calls, usage, errors/retries, reasoning fields, and any OpenRouter routing/caching behavior the chosen model uses. ACP restores endpoint metadata but re-resolves credentials, which permits central token rotation without rewriting transcripts (`H/acp_adapter/session.py:433-445`, `:518-526`). TLSNotary/parsing evidence, if added, should bind the authorized constructed request and the response actually consumed; provider configuration alone establishes none of that assurance (`A/sprints/2026-09-19/direction.md:15-21,35-42`, where `A` is `/Users/ember/dev/dregg-assortia`).

**Qualification: the provider finding establishes the configured main path, not every possible Hermes inference route.** Auxiliary tasks have their own router. In its default `auto` mode it first reuses the live main provider, model, base URL, API key, and API mode (`H/agent/auxiliary_client.py:3222-3321`); conversation compression explicitly passes the agent’s current main runtime into that router (`H/agent/conversation_compression.py:88-103`). Subagents likewise inherit the parent provider/base URL/key by default (`H/tools/delegate_tool.py:1124-1140`, `:1210-1223`). Those defaults support routing main calls, compression, and ordinary delegated children through the broker without a fork.

They are not a global egress guarantee. Every auxiliary task can override provider/model/base URL/key, and `auto` has configured and built-in fallback chains (`H/agent/auxiliary_client.py:4795-4868`, `:3323-3350`). Its direct OpenRouter fallback constructs a client using the compiled `OPENROUTER_BASE_URL` constant (`H/agent/auxiliary_client.py:1545-1563`; the constant is `https://openrouter.ai/api/v1` at `H/hermes_constants.py:663`), rather than the main runtime’s alternate URL. Delegation can also select a different provider or direct endpoint (`H/hermes_cli/config.py:1908-1920`, `H/tools/delegate_tool.py:2660-2769`). These counterexamples are enough to reject a claim that setting `OPENROUTER_BASE_URL` once proves complete inference metering.

Before claiming all inference is metered or that no raw key/request can egress, the deployment needs a bounded route inventory and runtime acceptance covering main turns, compression/other enabled auxiliary tasks, delegation, provider retry/fallback, and enabled plugins/tools. Pin or clear auxiliary/delegation overrides and fallbacks as appropriate; expose only broker-scoped tokens; and enforce a grain network allowlist so an overlooked route cannot reach a provider directly. Acceptance should record every outbound inference destination and correlate it to a broker operation. The no-fork conclusion remains a candidate architecture until that exercise and the hosted persistence/tool journeys run successfully.

## Existing `deos-hermes`: current reality

The Rust integration is useful prototype material, but it is not a hosted Nous Hermes implementation.

* Its ACP client performs a DREGG gateway admission/action only when upstream sends `session/request_permission`; it merely records `tool_call`/`tool_call_update` notifications (`B/deos-hermes/src/acp_client.rs:460-555`, where `B` is `/Users/ember/dev/breadstuffs`). Because current upstream requests that permission only for flagged dangerous commands (and edits through another callback), this cannot supervise every Hermes tool. Executing a side effect at the approval moment also risks separating or duplicating admission and the tool’s later actual execution.
* Comments claiming the supplied MCP server becomes the model’s “only” tool source are false for current upstream. The same repository’s newer caveat correctly notes that MCP is additive (`B/deos-hermes/src/mcp_server.rs:23-31`), while older comments still claim exclusivity (`B/deos-hermes/src/acp_client.rs:332-360`, `:623-627`).
* The advertised MCP `terminal` reads and receipts the requested command, but `run_command_in_confined_pd(_command)` ignores it and runs only confinement probes plus an IPC acknowledgment (`B/deos-hermes/src/mcp_server.rs:517-588`, `:624-665`). It must not be described as a command runner.
* Default `mcp-server` startup constructs a fresh local cipherclerk/runtime/gateway and `McpToolHost::new(...)`, then installs an embedded `RunJsTool`; it never calls `with_world_bridge` (`B/deos-hermes/src/main.rs:466-527`). Consequently `run_js` defaults to its own embedded World (`B/deos-hermes/src/mcp_server.rs:316-356`). A fail-closed World bridge exists (`B/deos-hermes/src/mcp_server.rs:196-217`, `:399-438`; `B/deos-hermes/src/world_bridge.rs:42-49`), but the default startup does not compose it.

Retain this code as evidence and possible adapter parts, but build the new DREGG MCP adapter against the canonical hosted service. Do not “fix” the hosted product by adding a flag around the prototype’s private ledger or probe-only terminal.

## Recommended contract boundary

The **DREGG supervisor/control service** should own:

* durable grain identity; create/open/start/stop/snapshot/reconcile; process supervision;
* persistent volume attachment, tenant UID/VM/container, cwd/workspace policy, CPU/memory/disk/time limits, and network policy;
* authenticated principal/delegation and revocation for DREGG operations;
* credential custody and scoped inference-token issuance;
* separate meters for inference, host resources, and kernel/resource operations;
* a canonical idempotent operation contract with `Refused`, `Pending`, `DurablyCommitted`, and `TransportUnknown`, plus lookup/reconciliation by stable operation ID.

**Hermes** should own its conversation loop, prompts, model/tool behavior, session history, memory/skills, CLI/TUI, ACP stream, and MCP client. The **DREGG MCP adapter** should be a thin schema/transport projection of canonical discover/read/author/install/invoke/history/status operations. It must not invent resource authority or a second success model. The project’s existing design record already requires the same four operation outcomes and exact operation lookup after interruption (`A/sprints/2026-09-17/shell-hermes.md:42-67`) and places SSH/CLI, external Hermes/MCP, and cockpit as peers over one resource service (`A/sprints/2026-09-17/shell-hermes.md:73-75`).

## Five decisions to freeze

1. **Host unit:** one upstream Hermes process tree per tenant grain, pinned by package/source identity, with persistent `HERMES_HOME` and workspace. Run local tools inside the grain; SSH is the primary human entrance for the first slice.
2. **Protocol roles:** SSH carries the full hosted CLI; ACP-over-SSH/relay remotely drives conversations; MCP carries Hermes-to-DREGG calls. ACP notifications and permission dialogs are UI signals, never the kernel authorization boundary.
3. **Credential boundary:** raw OpenRouter keys stay in a host broker. Hermes receives only a short-lived, budgeted inference token and broker base URL. Meter inference at the broker and host resources at the supervisor.
4. **Operation boundary:** all shared-resource mutations use one canonical DREGG service with stable operation identity and refusal/pending/commit/unknown semantics. The MCP adapter returns those typed results; it does not execute a second copy in an ACP callback.
5. **Concurrency rule:** allow many sessions per grain, but exactly one active driver per conversation/session ID, enforced by a supervisor lease. Dynamic ACP MCP descriptors must be resent on load/resume, and per-grain process isolation avoids process-global MCP server-name collisions.

The incompatibilities that require an adapter or upstream change are now bounded: ACP needs a remote stdio carrier; dynamic MCP configuration is additive and not persisted; ACP permission is not universal tool middleware; MCP registration is process-global by server name; same-session locking is only in-process; and raw provider credentials cannot be hidden from Hermes’s own terminal. None prevents the hosted upstream product. They determine where DREGG must wrap it and where a later upstream contribution would improve replaceable toolsets, session leases, credential helpers, or remote ACP transport.
