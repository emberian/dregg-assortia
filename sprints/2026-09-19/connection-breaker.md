# Disconnect as a circuit breaker

September 19 follow-up to the [protocol review](protocol-review.md). **Design and source investigation only.** No implementation, builds, tests, process interruption, service calls or deployment were performed. This refines the prior pause proposal; it does not claim an existing guarantee.

## Ember's revised target

> I'm thinking that disconnecting should immediately interrupt all ongoing tool or other things, so taht people can have "disconnect as circuit breaker" be a valid mental model, with the*option* to "connect softly" (ie, disconnect doesn't break, it just waits for someone to reconnect).

Default disconnection should actively interrupt ongoing work, not merely prevent the next agent step while current tools finish. A soft connection is an explicit alternative. Asked whether soft disconnect means finishing current work and waiting or continuing autonomously, ember selected:

> Keep working within the existing authority and budget.

The two intended modes are therefore **normal: disconnect trips the execution circuit breaker** and **soft: disconnect leaves execution running under the existing authority and budget**. Soft attachment does not expand permissions, reset a budget or hide expiry. Exact wire names and mode-change authorization remain design work.

The previous preference to resume after reconnection still supplies context. After a hard interruption, resumption means continuing a retained task after reconciling its operations; it cannot promise to resurrect every terminated subprocess or undo an already accepted external effect. After a soft disconnect, reconnect attaches to the same ongoing task and replays retained events rather than launching a second task.

## Source findings and their limits

Upstream Hermes has substantial cancellation machinery: ACP `cancel` reaches `AIAgent.interrupt`, which signals the agent thread, concurrent tool threads and registered active children. These are cooperative signals, not a universal confirmation that all effects stopped. The local terminal backend separately terminates process groups and escalates; the provider helper shuts down supported request transports. Sources include upstream `acp_adapter/server.py:1211–1222`, `run_agent.py:2376–2442`, `tools/environments/local.py:619–690`, and `agent/chat_completion_helpers.py:125–253`.

Asynchronous delegation has a separate lifetime: the background branch removes its children from the parent's active-child list and registers a separate cancellation callback (`tools/delegate_tool.py:2490–2538`). Consequently, a Hermes background label or shell `&` cannot, by itself, be our authorization to survive disconnect. Every child needs an explicit execution owner and cancellation scope.

The ACP prompt handler also drains queued prompts after computing cancellation state; its inspected drain loop contains no cancellation guard (`acp_adapter/server.py:1594–1660`). A subsequent prompt clears the cancel event. This is a reason to fence the controller queue as well as interrupt the current call. Exact ACP SDK behavior on EOF was not inspected: application entry hands lifetime to `acp.run_agent` (`acp_adapter/entry.py:250–264`), so no disconnect-to-complete-stop claim follows from the explicit cancel route alone.

See the [bounded Sol cancellation report](reports/hermes-circuit-breaker.md) for the complete source trace and [its inventory](circuit-breaker-inventory.json) for source identities. These are source observations, not measured stop latencies or end-to-end acceptance.

Host primitives provide useful enforcement mechanisms. Linux cgroup v2 can freeze a subtree, report when freezing has completed, and kill a subtree including descendants. Freezing is asynchronous; the controller must inspect completion. Workloads must be confined so they cannot move out of the controlled subtree. This is a candidate Linux host implementation, not proof that our current hosts supply it. [Linux kernel cgroup v2 documentation](https://docs.kernel.org/admin-guide/cgroup-v2.html#core-interface-files).

Network failure detection is a separate interval. An explicit stop/disconnect request can trigger the breaker on arrival; a silent network loss needs failure detection. OpenSSH's client-alive settings define such a timeout rather than instantaneous knowledge of a vanished client. A per-task attachment lease may be needed above SSH, especially where several channels share one transport. [OpenSSH client-alive configuration](https://man.openbsd.org/sshd_config#ClientAliveInterval).

Remote cancellation is weaker than local enforcement. For example, the inspected MCP cancellation specification permits a recipient to ignore cancellation when a request cannot be cancelled, and describes races with completed responses. A cancellation notification cannot stand in for confirmed remote stoppage. [MCP cancellation specification, 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/cancellation). No protocol version was selected by consulting this example.

## Proposed enforceable contract

1. **The controlling attachment authorizes a defined execution scope.** It owns foreground inference, tools, subprocesses and delegated children, including work an agent happens to call asynchronous. A spectator connection must not keep that scope alive or stop another controller's scope.
2. **A detected hard disconnect immediately trips that scope.** Fence new operation admission and provider dispatch, request cancellation of active calls, and suspend/terminate the local execution domain with host enforcement. Do not insert an extra completion grace period after detecting the disconnect. Local stop completion and remote acknowledgements are observed outcomes, not inferred from sending a signal.
3. **Use a durable generation for each attachment/execution authority.** A tripped generation stays invalid after reconnect or host restart. A delayed worker, reconnecting transport or late response cannot regain authority merely because a new connection exists. Reconnection obtains fresh authority after checking the current resource rules, remaining budget and unresolved operations.
4. **Keep the controller and journal outside the stopped workload.** They must retain the cutoff, cancel broker-side work, collect late results, record uncertain outcomes and reconcile before continuation. Freezing the whole controller with its agent would defeat this responsibility.
5. **Make survival of disconnect explicit.** Selecting soft mode permits the attached execution scope to continue within its existing authority and budget. Independently launched background work has its own budget and cancellation contract. The UI needs to make both disconnect-surviving arrangements visible. Under normal mode, ordinary subagents and shell background processes stay covered by the breaker unless an authorized operation placed them in an independent background scope.
6. **Report what actually stopped.** Distinguish breaker tripped/admission fenced, local execution stopped, remote cancellation requested/confirmed, and external outcome still unknown. An already committed resource transaction remains committed. A provider may still finish or bill an already accepted request; retain that evidence without allowing its late result to launch further work under the tripped authority.

This is a proposed extension to canonical execution authority, not an independently authoritative HTTP-session flag. The selected kernel/host contract must determine where these generations and checks live, the order of stop versus effect admission, and what evidence a receiver accepts. Connection presence and a host watchdog also have explicit clock/trust assumptions; they must not silently reuse Mini's commit-count clock as wall time.

Immediate interruption and durable continuation put different requirements on the implementation. Cooperative interrupt is useful for cleanup and retaining context. Host suspension/termination supplies enforcement when a tool ignores the request. A suspended process preserves more transient state; a killed one requires reconstruction from durable task/operation records. Neither mechanism alone stops work already accepted by an independent remote service.

## Acceptance to design before implementation

- Disconnect during inference, a long terminal command, parallel tools, delegated agents, a browser operation and a remote MCP call. Observe the actual stop of every locally owned process and refusal of further admitted effects.
- Include a process that forks, ignores cooperative cancellation or tries to detach. Verify it remains within the foreground execution scope. Check that an explicitly authorized background scope is unaffected.
- Distinguish an explicit disconnect from a blackholed connection and controller crash. Specify and measure detection time separately from local stop time. Partitioned remote workers need their own expiry/fencing contract; no instantaneous distributed-stop claim.
- Race disconnect against dispatch, commit, response delivery and reconnect. Keep completed results, reject stale authority, preserve uncertain operations and avoid duplicate paid actions.
- Restart the host after a breaker trip; stale sessions/credentials remain stopped. Reconnect to missing/corrupt state refuses clearly. Reconnect during stopping does not create a second driver or revive the old generation.
- Exercise soft mode separately: continuation after disconnect uses the same authority and budget, survives only within their limits, and reconnect attaches without duplicate execution. Mode changes must be authorized and visible. Soft mode must never be silently selected because interrupting a particular tool is inconvenient.

Implementation remains wound down. These requirements identify necessary host/core/adapter work; they do not downgrade the desired circuit breaker to whichever cancellation behavior happens to exist today.
