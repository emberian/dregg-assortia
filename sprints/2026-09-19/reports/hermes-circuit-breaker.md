# Hermes disconnect / circuit-breaker audit — 2026-09-19

Scope: source-only inspection of the current `/Users/ember/pug/hermes-agent` checkout.
No Hermes process, build, test, provider call, MCP call, or remote command was run.
This is a design finding, not runtime acceptance evidence.
## Verdict

Upstream ACP cancellation is a useful cooperative interrupt, but it is not a circuit breaker.
`cancel()` records the prompt, sets an event, calls `AIAgent.interrupt()`, and returns without
waiting for inference, tool workers, children, or remote effects to become quiescent
(`acp_adapter/server.py:1211-1223`).

The best no-fork candidate is therefore to keep upstream Hermes inside a DREGG-owned isolated
runtime, translate connection loss into both the upstream interrupt and a supervisor-owned
cancellation epoch, and let the supervisor enforce the hard boundary. Upstream source alone
cannot support the claim “disconnect stops all work immediately.”
## Cancellation path and actual stop strength
1. ACP → agent. The prompt runs in a thread-pool executor (`acp_adapter/server.py:1545-1557`).
   ACP cancel sets `cancel_event`, copies the prompt into `interrupted_prompt_text`, and calls
   `agent.interrupt()` (`acp_adapter/server.py:1211-1223`). There is no completion acknowledgement,
   join, or cancellation generation in this path.

   The ACP entry point delegates lifetime handling to `acp.run_agent(...)`
   (`acp_adapter/entry.py:255-262`); this source does not establish that transport EOF invokes
   `HermesACPAgent.cancel()`. Disconnect→cancel must be an explicit DREGG/controller guarantee.
2. Agent flag fan-out. `AIAgent.interrupt()` sets `_interrupt_requested`, signals the main
   execution thread and registered concurrent-tool thread IDs, and calls `interrupt()` on
   `_active_children` (`run_agent.py:2401-2442`). Tool signaling is thread-scoped
   (`tools/interrupt.py:1-15,39-70`), so it only works where the tool polls `is_interrupted()`
   on the signalled thread.
3. Conversation loop. The loop checks the flag between iterations
   (`agent/conversation_loop.py:589-599`). An interrupt during a provider call is caught, current
   messages are persisted, and an interrupted result is built
   (`agent/conversation_loop.py:1966-1977,4539-4557`). Finalization persists messages before
   clearing interrupt state (`agent/turn_finalizer.py:135-143,325-370`).
4. Provider calls. OpenAI-compatible and Anthropic calls run in daemon worker threads which may
   outlive the turn (`agent/chat_completion_helpers.py:125-150`). On interrupt the caller marks
   the request cancelled, closes/aborts its transport, and raises without joining the worker
   (`agent/chat_completion_helpers.py:528-548`). Streaming uses the same pattern
   (`agent/chat_completion_helpers.py:2565-2570,2623-2641`). This strongly interrupts the client
   socket, but cannot prove an already accepted provider request stopped or ceased billing.
5. Bedrock is weaker. Non-streaming calls use cached boto3 `converse()` without a request-local
   client to close (`agent/chat_completion_helpers.py:209-231`), while the generic interrupt
   returns immediately (`agent/chat_completion_helpers.py:528-548`). Streaming passes a
   cooperative callback to its decoder, yet raises without joining its daemon worker
   (`agent/chat_completion_helpers.py:1703-1718`). A live worker can outlast the cancelled turn.
## Tools, subprocesses, and stale results
6. Sequential tools. Hermes checks the flag before each tool and cancels the rest
   (`agent/tool_executor.py:770-789`). The active call is synchronous
   (`agent/tool_executor.py:1214-1227`). A tool that does not poll the interrupt runs to completion;
   its result is appended to history before Hermes notices and skips later calls
   (`agent/tool_executor.py:1390-1420`). This is a direct late-result admission path.
7. Parallel tools. Workers register their threads and receive the interrupt bit
   (`agent/tool_executor.py:462-478`), but still write eventual results to the shared array
   (`agent/tool_executor.py:492-544`). The waiter cancels unstarted futures and allows running
   workers three seconds (`agent/tool_executor.py:572-604`). Source-level inference: because this
   is inside `with ThreadPoolExecutor(...)` (`agent/tool_executor.py:562-570`), normal context exit
   waits for running noncooperative futures. Their real results are then selected instead of
   cancelled placeholders (`agent/tool_executor.py:625-669`). A hung tool can delay completion to
   its own ceiling, and late results remain admissible.
8. Terminal commands are the strongest built-in case. The shared poll loop checks interrupt,
   calls `_kill_process`, and returns code 130 (`tools/environments/base.py:653-669`). Local POSIX
   execution creates a process group (`tools/environments/local.py:595-612`) and escalates that
   group from TERM to KILL (`tools/environments/local.py:619-687`). This is a real local stop
   boundary, subject to kernel/process semantics.
9. SSH is not equivalent. `SSHEnvironment` spawns a local `ssh ... bash -c` process
   (`tools/environments/ssh.py:343-353`) and has no `_kill_process` override; the base only kills
   its `ProcessHandle` (`tools/environments/base.py:762-767`). Killing the SSH client does not prove
   the remote shell, descendants, or already committed effects stopped.
10. MCP polling notices interrupt every 100 ms, cancels the local future, and raises
    (`tools/mcp_tool.py:2919-2984`). The operation is `session.call_tool(...)` on the MCP loop
    (`tools/mcp_tool.py:3152-3162`). There is no DREGG operation epoch, server acknowledgement,
    rollback, or idempotency key here. Cancellation may propagate through the SDK, but cannot
    recall a remote side effect already accepted.
## Delegation escapes
11. Synchronous children are registered in `_active_children` (`tools/delegate_tool.py:1273-1280`)
    and receive `child.interrupt()` (`run_agent.py:2433-2442`). Batch collection fabricates
    interrupted entries when the parent flag is seen (`tools/delegate_tool.py:2279-2325`), but its
    executor context can still wait on noncooperative child futures
    (`tools/delegate_tool.py:2267-2277`). Their provider/tool limitations remain.
12. Background delegation deliberately removes every child from the parent's interrupt list and
    transfers ownership to an in-memory async registry (`tools/delegate_tool.py:2482-2535`).
    Top-level model delegations are forced to background mode (`run_agent.py:5200-5222`). Thus ACP
    cancel → parent `interrupt()` does not signal the normal top-level delegated work.
13. The async registry has a separate `interrupt_all()` which invokes stored callbacks but does
    not join or verify quiescence (`tools/async_delegation.py:519-544`). CLI `/stop` calls it
    explicitly (`hermes_cli/cli_commands_mixin.py:227-258`); ACP `cancel()` does not. Completed
    background results are still queued for reinjection (`tools/async_delegation.py:451-499`), so
    a post-disconnect completion can re-enter later unless DREGG rejects the old epoch.
## What survives and what “resumable” currently means

ACP persists returned history even for an interrupted turn (`acp_adapter/server.py:1564-1567`).
That preserves evidence, but also admits late tool results. Original-prompt salvage is only the
in-memory `interrupted_prompt_text` (`acp_adapter/session.py:169-183`), replayed only on a later idle
`/steer` (`acp_adapter/server.py:1319-1350`). Persistence stores cwd/provider/model metadata and
history, not the interrupted prompt, execution frontier, outstanding operations, or cancellation
epoch (`acp_adapter/session.py:423-467`). Async records are also process memory
(`tools/async_delegation.py:95-121,195-228`). This is conversation resumption, not durable task
continuation.

After a cancelled turn, ACP marks it idle and drains `queued_prompts` by recursively starting new
prompts (`acp_adapter/server.py:1637-1657`); prompt start clears `cancel_event`
(`acp_adapter/server.py:1388-1389`). Therefore cancel is not a scope-wide queue barrier.
## Required design decisions
1. Default disconnect creates a DREGG cancellation epoch, fences dispatch, and immediately
   suspends or stops controlled execution. Send ACP cancel for compatibility, but allow cooperative
   cleanup/drain only inside that already-revoked boundary; require quiescence acknowledgement.
   Soft disconnect explicitly continues within existing authority and budget.
2. Route every inference call through the scoped credential proxy and cancel/revoke all request IDs
   for the epoch. Socket close alone is not a provider-side stop or metering proof.
3. Register foreground tools, MCP/SSH jobs, background processes, async delegations, and review work
   under one DREGG epoch. Hermes “background” must not authorize survival across disconnect.
4. Retain late results as operation evidence, while quarantining cancelled-epoch callbacks from
   driving new work or appearing as fresh authorized success. Remote side effects need operation
   IDs plus idempotency/status/reconciliation; do not promise rollback from client cancellation.
5. Persist a separate resumable task record: intent, accepted checkpoints, outstanding operation
   IDs, cancellation reason/epoch, and safe continuation cursor. Hermes history remains context and
   evidence, not the task state machine.
