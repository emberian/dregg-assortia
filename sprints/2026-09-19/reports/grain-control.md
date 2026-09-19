# Hosted Hermes grain control: source-grounded design note

Read-only investigation, 2026-09-19. No repository edits, builds, tests, services, SSH, or Git operations were performed. Paths below use **B** = `/Users/ember/dev/breadstuffs` and **A** = `/Users/ember/dev/dregg-assortia`.

## Verdict

There is useful substrate, but there is no easy integration that currently yields a durable hosted Nous Hermes grain. The closest reusable pieces are:

- `agent-platform` for the HTTP control vocabulary, tenant locking, service roles, vat lifecycle transitions, logical prepaid rent, session carrier format, and R0/R1/R2 verification surfaces;
- `dregg-agent::Session` for cap-gated goals, a cumulative receipt chain, logical action/spend budgeting, and full report reconstruction;
- `grain-turn` for kernel admission of action commitments and the owner-envelope path;
- `deos-hermes::AcpClient` for an actual unforked `hermes-acp` subprocess and standard MCP registration.

Those pieces are not joined at a durable boundary. The served platform creates an empty in-memory registry on each start, its lease cells and local node are in RAM, `wake_from_lease` first requires that RAM tenant, SSH attach restores only an account-level consumed number and signer seed, and the ACP client creates a new Hermes session for each prompt. The result is useful in-process semantics and adapters, not restartable hosted grains.

This should proceed as a small DREGG grain-control lifecycle with ACP/MCP/SSH adapters. Full STARK assurance need not gate useful execution, but the control plane must state the boundary honestly: current R2 commits an action intent/admission turn; it does not prove the external tool effect or make that effect exactly once. `B/agent-platform/src/lib.rs:1077-1119`; `B/grain-turn/src/finalize.rs:218-242`.

## Existing mechanisms and their actual semantics

| Mechanism | Reusable meaning | Lifetime / recovery | Semantic difference that matters |
|---|---|---|---|
| `AgentPlatform` tenant registry | Per-grain lock, owner, caps, budget, lifecycle, session, lease, minter/node, ACL | `Mutex<HashMap<host, Tenant>>`; `new()` starts empty | Process lifetime only. There is no open/reload path, so restart loses the inventory needed to find any carrier. `B/agent-platform/src/lib.rs:214-285,319-352,451-460` |
| Rent/provision | Opens hosted cap bundle, session, prepaid lease/vat, workdir, owner | Inserts one `Tenant` in RAM | `funding = rent * 1024` seeds a synthetic cell balance; it is not external collection or custody. Workdirs default under `/tmp/dregg-grains`. `B/agent-platform/src/lib.rs:539-667`; `B/agent-platform/src/bin/agent-platform.rs:56-57` |
| Vat lifecycle | Legality-checked `Created/Running/Sleeping/Lapsed/Reaped` transitions on the lease cell | Survives only as long as the in-memory lease cell survives | `sleep` retains the whole Tenant; `wake` only flips lifecycle. `wake_from_lease` reconstructs a Session from a carrier but begins with `tenant_arc(host)`, so it cannot recover after a process restart without a separately persisted/restored Tenant and Cell. `B/agent-platform/src/lib.rs:287-305,1365-1444` |
| Session carrier | Full report, receipt secret, committed-turn manifest, history, plus root/length slots | Logically reconstructable from the lease heap | Good serialization/root-check semantics, but the only current carrier lives inside the in-memory `HostedLease` Cell. “Heap alone” means within a retained Tenant, not a disk/node restart boundary. `B/agent-platform/src/lib.rs:1577-1680` |
| `Session` state | Receipt chain, cells, action log/counts/sequence, goal history; can restore byte-identical report | Across goals in one object; full restore is available if a caller durably supplies report, history, secret | It is a Rust object, not a store. `Session::wake_from_report` is the right reconstruction primitive once durable control supplies its inputs. `B/dregg-agent/src/session.rs:247-269,320-365`; `B/dregg-agent/src/agent.rs:1855-1947` |
| SSH `ConsumedStore` | Per-account cumulative consumed value and receipt signing seed | JSON file under `DREGG_AGENT_STATE_DIR` or `~/.dregg-agent/state` | It does **not** store the report, cells, original receipt chain, goal history, workspace identity, grain identity, or Hermes session. Reattach opens a fresh Session and inserts a carryover receipt. `B/dregg-agent/src/session_store.rs:31-54,72-117`; `B/dregg-agent/src/bin/dregg-agent.rs:1099-1131`; `B/dregg-agent/src/agent.rs:1527-1582` |
| `ConsumedStore` failure/concurrency behavior | Monotonic `max(prior,current)` on a successful single-writer update | File rename with a fixed `.tmp` sibling | Corrupt/unreadable is treated as zero, which widens prior headroom; the source test explicitly expects this. There is no lock/transaction/fsync. Concurrent attaches can load the same baseline, spend independently, and persist `max` rather than the sum; concurrent first attach can race signer creation. These concurrency results are direct inferences from the read-modify-write implementation. `B/dregg-agent/src/session_store.rs:100-143,146-181,202-209,321-330` |
| Session action budget | Per-subject logical budget and exactly-once `(agent, seq)` keys | Two in-memory `HashMap`s | It meters flat action cost or explicit `amount_cents`; it does not meter CPU, wall time, tokens, storage, network, or provider rent. Exactly-once is only within the meter process. `B/dregg-agent/src/agent.rs:443-455`; `B/dregg-agent/src/meter.rs:155-164,224-273` |
| Hosted lease/prepaid rent | Schedule checks, reserve/cursor draw, checkpoint/lapse fields | A plain Cell held by its caller | `check_bill` and `discharge` are logical cell mutations. External settlement is separate. Prepaid audit treats an unreadable/missing prepaid binding as “nothing to lapse,” and `cell_mut` entrusts callers with economics. `B/hosted-lease/src/lib.rs:144-197,199-237,271-309` |
| Platform billing | Tenant-serialized gate → external `Settlement::settle` → local discharge | Process-local critical section | Not crash-atomic across the external settlement/local cursor boundary. A stable charge id can make a settlement implementation idempotent, but the platform has no durable operation journal or restart reconciliation. `B/agent-platform/src/lib.rs:1022-1074` |
| Service ACL | Owner=Admin plus revocable Viewer/Driver/Admin map; routes use it | In-memory per Tenant | This is application authorization, deliberately separate from the cryptographic share. It disappears on restart. The bare server trusts caller-supplied `X-Dregg-Subject`; a deployment must terminate authentication ahead of it. `B/agent-platform/src/lib.rs:680-743`; `B/agent-platform/src/share.rs:39-53`; `B/agent-platform/src/serve.rs:601-615`; `B/agent-platform/src/bin/agent-platform.rs:1-20` |
| Kernel owner envelope | Owner public key gates authority-widening turns on the worker | In the worker Cell/runtime | This is closer to kernel authority than the ACL. It governs selected Delegate/SetPermissions/VK changes, while the host still drives ordinary state turns. Absence of a renter anchor opens an unenveloped worker. `B/agent-platform/src/node.rs:277-287`; `B/agent-platform/src/lib.rs:890-905` |
| `grain-turn::ToolGatewayMinter` | Commits `calls_made`, prior-history root, consumed total, heap root, action commitment, optional attestation | In-memory runtime/ledger/log | It is admission/accounting metadata. The kernel turn is minted before the session meter draw and before the external tool. It does not contain the later tool result. Deadline is `i64::MAX/2`, explicitly not actual lease expiry. `B/grain-turn/src/lib.rs:292-340,492-587`; `B/dregg-agent/src/agent.rs:1681-1838` |
| Served `NodeMinter`/`LocalNode` | Stable minter across drives and finalized receipt chain inside one Tenant | Ledger, log, hash index are `Arc<Mutex<...>>` in RAM | External node forwarding is explicitly a deploy step. The served minter writes consumed/heap/action/attestation but omits `HISTORY_ROOT_SLOT`, unlike `ToolGatewayMinter`; therefore the two claimed turn shapes are not identical on the history weld. `B/agent-platform/src/node.rs:1-42,87-118,342-405`; compare `B/grain-turn/src/lib.rs:508-536` |
| R2/R3 verification | R2 binds agent receipts to recorded kernel turn hashes; R3 adapter exists | Depends on retained report/manifest/runtime artifacts | R2 does not re-execute or establish the external effect. R3 has an acknowledged multi-effect nonce/head mismatch across turns; attestation slot 8 is outside the current eight-field finalizer. `B/agent-platform/src/lib.rs:1103-1119`; `B/grain-turn/src/finalize.rs:26-36,66-86,218-242` |
| `dregg-agent attach` | A forced-command target suitable for `authorized_keys`; interactive line REPL and one-shot `SSH_ORIGINAL_COMMAND` | One fresh process/session per attach | This is not an SSH daemon, account/key provisioner, PTY workspace, or durable conversation. Default workdir is `/tmp/...-{pid}`. Hosted raw shell is refused because OS isolation is not wired. Budget-save failure only warns and permits exit. `B/dregg-agent/src/bin/dregg-agent.rs:915-923,1012-1075,1165-1240` |
| OpenAI-compatible brain | Host-held provider key and fresh brain per goal | No provider conversation continuation | Every REPL goal constructs a new brain/conversation. DREGG goal history persists only in a live Session/carrier; it is not a Hermes thread. `B/dregg-agent/src/bin/dregg-agent.rs:1243-1337`; platform equivalent `B/agent-platform/src/lib.rs:957-1019` |
| Hermes in `dregg-agent` | Nous Portal/OpenAI-compatible model path; optional ndjson wrapper | Per invocation | Bare Hermes ACP is not spoken here. Without an explicit `DREGG_HERMES_CMD` wrapper the CLI-shaped path is recorded replay, even if Hermes is installed. `B/dregg-agent/src/hermes.rs:1-47,98-177` |
| Hermes in `deos-hermes` | Real ACP JSON-RPC subprocess, permission callback through `HermesGateway`, and MCP server registration | Child and ACP client are process-local; Drop kills the child | This is the strongest external-unforked adapter. Each `drive_prompt` performs `initialize` and `session/new`; there is no durable session id, resume/load, or integration with AgentPlatform lifecycle. `B/deos-hermes/src/acp_client.rs:1-41,171-210,311-377,599-677` |
| Hermes confinement | Real forked protection-domain sandbox with one endpoint | Process lifetime | The current strongest sandbox denies `execve`, so it cannot run an external Hermes binary; the confined body is a Rust stand-in. External unforked Hermes and this sandbox are currently separate paths. `B/deos-hermes/src/confined.rs:14-41` |

## Identity map

The design must stop using these as if they were one identity:

| Identity | Current source | Required treatment |
|---|---|---|
| Authenticated human/account | `X-Dregg-Subject` or attach `--account` | Auth adapter output; never the grain primary key and never trusted directly from an unauthenticated client. |
| Host name | Tenant map key; lease CellId and placement token are derived from it | Mutable route/alias. Renaming or moving must not create a new grain. |
| DREGG grain/resource | Worker CellId plus lease Cell/state | Immutable durable primary identity. Persist the mapping to every adapter/process/provider object. |
| Session/agent id | Forced to `agent:session:{account}` | Insufficiently specific: two grains owned by one account receive the same visible agent id, although they have different clouds/secrets. Include immutable grain id/epoch in future identities. `B/dregg-agent/src/session.rs:368-388` |
| Receipt signer | Random per platform grain; persistent per account in SSH store | A custody handle/version, scoped to one grain epoch. Do not equate it with owner identity. |
| Kernel owner key | Optional renter anchor public key | Resource authority input; distinct from the host executor signer and service ACL. |
| Host executor key | Optional platform-wide seed; absent by default | Provider/operator attestation identity, not renter identity. `B/agent-platform/src/lib.rs:343-350` |
| Hermes ACP session id | Result of each `session/new` | Runtime/conversation handle, persisted only if Hermes offers a supported resume contract; never grain identity. |
| OS process/PID | AgentPlatform, SSH attach, Hermes child | Ephemeral observation only. Recovery adopts/restarts by durable grain and operation ids, never by PID alone. |

## The effect-ordering boundary

The current action path is:

1. service cap check;
2. kernel `mint_turn` (writes action/cost projection and increments `calls_made`);
3. in-memory session meter draw;
4. external tool or filesystem/shell effect;
5. agent receipt seal;
6. after the whole goal, lease-carrier checkpoint.

Source: `B/dregg-agent/src/agent.rs:1652-1838`; platform checkpoint: `B/agent-platform/src/lib.rs:945-954`.

Consequences:

- A session-budget refusal can occur **after** a kernel turn was committed, leaving a turn with no budget draw, effect, or agent receipt. Existing R2 source tests cover under-budget minting and executor refusal, not minter-plus-session-budget refusal. `B/dregg-agent/src/agent.rs:2323-2418`.
- A crash after meter draw but before/during the tool can leave a charge with no retained result.
- A crash after a non-idempotent external effect but before the agent receipt/checkpoint can make retry unsafe.
- A crash after receipt seal but before carrier checkpoint loses the latest recoverable Session even though kernel/node state may have advanced.
- The committed kernel fields describe requested action/cost/pre-effect heap, not the actual tool result. `verify_agent_run` checks signature continuity and consumed≤budget, not effect completion. `B/dregg-agent/src/agent.rs:1055-1084`.

This does not require waiting for full STARKs. It requires a durable operation record and truthful state labels before offering hosted execution.

## Candidate durable control state machine

Use the existing vat lifecycle as the **desired resource state**, with a small durable reconciliation envelope around it. One row is keyed by immutable `grain_id`; every mutation carries a stable `operation_id` and expected record revision.

```text
Absent
  -> Allocating(request_id, owner, profile, store_id, provider_key)
  -> Recovering(provider_ref?, lease_cell_ref, image_ref)
  -> Ready(vat=Running, endpoint, recovered_boundary)
  -> Quiescing(op_id) -> Sleeping(vat=Sleeping, checkpoint)
  -> Recovering(op_id) -> Ready
  -> Lapsing(charge_id/evidence) -> Lapsed
  -> Reaping(op_id, provider_ref?) -> Reaped

Any external-call boundary may become:
  Uncertain(op_id, kind, prior_revision, idempotency_key, last_observation)
  -> reconcile by lookup/adopt/observe -> one of the states above
```

Rules:

- Persist intent before provider creation, process spawn, settlement, tool dispatch, stop, or deletion. Store the original request bytes and idempotency key.
- Readiness means the correct store/profile/lease/image/node history and custody handles were recovered, the workspace was mounted, and the Hermes/control endpoint passed its actual health check. A spawned PID is not readiness.
- Keep an action operation substate whose durable decision is `Prepared -> AdmittedAndBudgetReserved -> EffectUncertain -> Succeeded(result) | Refused | Failed(result)`. `AdmittedAndBudgetReserved` should be one defined durable transition. If the selected stores cannot make it atomic, use an explicit recoverable reservation protocol (for example `BudgetReserved -> KernelAdmitted`) with stable operation identity and reconciliation for every intermediate state. This is deliberately **not** the current kernel-admit-then-possibly-budget-refuse ordering: once kernel admission occurred, a later budget problem must remain a visible operation/reservation to reconcile and cannot be reported as though nothing happened.
- Recovery first looks up/reconciles the original operation and adopts an existing backend/process where possible. It never creates a replacement grain under the same identity merely because RAM is empty.
- Acknowledged event cursors and ACP/conversation checkpoints are consumer records tied to a grain boundary. They are not kernel mutations unless the resource contract explicitly makes them so.

This is the same product boundary already recorded in `A/contributing/resource-host-lifecycle.md:29-44,46-63,77-86`; that document is a draft, not evidence of an implementation.

## Five consequential decisions

1. **Choose one immutable grain identity and durable system of record.** The grain id must key the lease Cell/image, workspace volume, node/minter state or external-node locator, owner/key epochs, ACL revision, Hermes runtime record, charge cursor, and operation journal. Account, DNS/host alias, ACP session, and PID remain mappings. This is prerequisite to adoption and non-duplication.

2. **Freeze the execution/result boundary before calling actions exactly once.** Decide whether the kernel turn represents authorization, reservation, or durable acceptance; then retain the external effect outcome separately. Replace the current mint-before-budget-refusal sequence with one durable admission-plus-budget-reservation decision, or an explicit reservation protocol whose intermediate states recover and reconcile under the same operation id. Post-admission budget refusal cannot erase the committed turn. For non-idempotent tools, require downstream idempotency/lookup or leave the operation `Uncertain` until reconciled. A signed receipt cannot manufacture knowledge about a lost external response.

3. **Choose the Hermes continuity contract.** A long-lived unforked `hermes-acp` child gives native Hermes state but needs a supervisor, stable workspace, provider credential injection, health/readiness, and an ACP resume/export contract. If Hermes cannot resume a session, persist DREGG transcript/tool state and explicitly start a new Hermes session with reconstructed context; do not claim the same Hermes conversation. The existing ACP/MCP adapter is a good wire component, not a session manager.

4. **Make canonical resource authority authoritative at control routes.** SSH/OIDC/webauth authenticates a caller; DREGG credentials and resource rules decide whether that caller may perform resource-governed management or use. The current Viewer/Driver/Admin ACL is reusable as a route filter, cache, and defense-in-depth check, but it must derive from or obey the selected canonical resource authority where that authority governs the operation. It must not create an independent Admin path around a resource rule. Preserve the selected self-governing rule: a resource may lock out even its owner; operator recovery must not become an authority bypass. `A/contributing/resource-host-lifecycle.md:31-42`.

5. **Name three separate meters.** Hosting rent/lease, agent/tool spend, and physical resource quotas have different units and enforcement. Current `USD-CENTS`/action costs and `calls_made` do not bound CPU/RAM/token/storage use. Choose a real clock source and biller, durable charge identity/lookup, settlement evidence, and fail-closed corruption behavior; bind kernel grant deadline/lifecycle to lease expiry rather than the current far-future constant.

## Exact integration obligations

1. **Durable open/recovery before serving.** Add a store-backed registry load around `AgentPlatform`; serialize/version the lease Cell and terms, vat state, carrier, owner/ACL, renter checkpoint, stable workdir/volume id, runtime/profile ids, node/minter state or external-node reference, committed-turn/history data, and key-custody handles. Reject missing/corrupt/incompatible images. `wake_from_report` can reconstruct the Session after this layer supplies its inputs.

2. **Durable operation journal and reconciliation.** Journal provider, process, settlement, lifecycle, and tool operations with original bytes, stable idempotency key, state, observations, and retained result. Implement lookup/adopt for lost responses. Make billing recover `settle`-succeeded/`discharge`-unknown without double paying. Refuse reconnect/spend when the consumed record is corrupt or cannot be locked.

3. **Unify action admission order and evidence.** Make admission and budget reservation one durable transition, or persist each recoverable reservation state and reconcile it under the same operation id. Prevent silent orphan kernel turns on session-budget refusal: if kernel admission happened, retain that fact and resolve its reservation rather than returning a no-op refusal. Persist dedup keys and bind a retained effect-result record to the admitted action. Preserve `EffectUncertain` across crashes. Decide which side can retry. This work is needed for system semantics even if R3 remains deferred.

4. **Choose and persist the canonical kernel/node path.** Either persist the local node ledger/log/worker identity/counters or submit to and recover from an external node. Implement the currently absent external forwarding. Align served `NodeMinter` with the canonical `grain-turn` history-root write, bind lease deadline/epoch, and retain sufficient manifests/checkpoints for restart verification.

5. **Build a real Hermes supervisor adapter.** Integrate `deos-hermes::AcpClient` with grain lifecycle, one child/runtime record per running grain, stable cwd/volume, host-held OpenRouter credential injection, MCP registration limited to the DREGG tool bridge, permission/result correlation to operation ids, cancellation/timeout, health, logs, and restart. Determine supported Hermes session resume/export empirically against the selected version before promising conversation continuity.

6. **Supply actual process isolation and physical quotas.** The current hosted attach disables raw shell because its jail is unwired, while the strongest PD cannot exec external Hermes. Select a deployable container/VM/sandbox boundary that can run unforked Hermes, mount only its workspace and sockets, isolate credentials, constrain CPU/RAM/pids/disk/network, and report enforced limits. Keep tool-level DREGG authority inside that boundary.

7. **Make SSH an authenticated adapter.** Provision/rotate/revoke SSH keys and bind the authenticated principal to `grain_id`; expose attach/control and optionally a PTY inside the chosen isolation. Do not derive ownership from a client-provided `--account` or header. Restore the durable grain, workspace, and conversation/control cursor rather than opening a fresh account-level Session.

8. **Persist canonical grants/revocations and preserve kernel checks.** Reconstruct control permissions from the selected resource-authority boundary. If an operational ACL is retained for routing or defense in depth, bind its revision to that boundary, fail closed when stale or unavailable, and never let it add authority the resource does not grant. Continue verifying kernel credentials/resource policy for each actual operation. Never translate service Admin into raw mutation of Cell, ledger, or journal.

9. **Define observability and readiness.** Report runtime/profile/version, current desired and observed lifecycle state, recovered checkpoint/boundary, lease/charge status, Hermes process and ACP session status, workspace id, and network/finality level. Provide resumable events with retention-gap behavior. Keep local admission, durable local result, and node/federation finality distinct.

10. **Acceptance must inject crashes at every boundary.** Cover restart before/after provider create, kernel admission, budget reservation, external effect, result write, checkpoint, settlement, discharge, Hermes spawn, and stop. Retry the exact original operation and prove one backend, one charge, and the retained result or an honest `Uncertain`. Exercise two grains owned by one account and concurrent attaches, because current account-derived session ids/store semantics alias them.

## “Easy integration” assessment

- **External unforked Hermes via ACP/MCP:** wire-compatible foundation exists; easy hosted integration is **not supported**. Missing: lifecycle ownership, durable session/resume, provider-key custody policy in that path, result journal, isolation capable of exec, and AgentPlatform integration.
- **SSH login:** a forced-command REPL target exists; easy shellserver integration is **not supported**. Missing: SSH service/key management, stable grain mapping, durable full Session/conversation, persistent default workspace, safe hosted shell/PTY, and concurrent-account correctness.
- **Persistent grain/recovery:** the carrier and reconstruction primitives exist; process-crash recovery is **not supported** because the discoverable Tenant/lease/node are not persisted.
- **Metered hosting:** logical action budget and prepaid lease arithmetic exist; production metering is **not supported** without a clock/biller, durable settlement reconciliation, external value custody, physical resource accounting, and fail-closed store behavior. The default binary even leaves lapse disabled when `DREGG_OPERATOR_SUBJECT` is unset. `B/agent-platform/src/bin/agent-platform.rs:16-20,58-62`.
- **Proof assurance:** useful system execution can precede R3, using explicit R0/R1/R2 labels and retained operational evidence. It is not supported to describe R2 as proof that the external tool ran, nor to describe the current R3 adapter as faithful multi-turn on-ledger assurance.

## Evidence discipline

No new test was run. Test bodies were read only as source-level intended behavior. The prior captured September 18 result establishes that one JS-agent/World Hermes test passed at its recorded Bread snapshot; the handoff explicitly says it reaches a narrow `DelegAdmit` path and **does not establish external Hermes service integration**. `A/sprints/2026-09-18/wind-down.md:5,12-14,38-40`. The resource-host brief remains proposed/unassigned, and the native Mini host/export is unfinished; neither is a current deployment. `A/sprints/2026-09-18/wind-down.md:18-24,44`; `A/sprints/2026-09-18/account-handoff/design/dregg-native-host-export-proposal.md:1-3,19-27,47-55,57-59`.
