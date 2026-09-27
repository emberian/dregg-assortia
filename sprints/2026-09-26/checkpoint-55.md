# Checkpoint 55 — lifecycle completion and integration defects

September 27, 2026. Continues [checkpoint 54](checkpoint-54.md). The full [platform goal](spk-platform-cycle.md) remains active.

Reviewed Mini commits:

- **0332202:** source-authored STOP with canonical inspection preserving STOP rather than echoing INSTALL. Two narrow Lean checks pass. This does not establish a physical STOP: review subsequently found the target-incarnation mismatch below.
- **4bedbce:** guarded Rust continue binds the admitted create receipt/custody and signed continue command; fresh op26 claim handling compares the exact callback, original ingress, volume, process and receipt. Fourteen scoped tests and strict Clippy pass. Physical INSTALL/START remains guarded pending completion and custody integration.
- **ce91492:** lifetime-dispatch projection, receipt-only lookup and fresh-CAS receiver, plus separate source authoring for the current parent generation. Four serial Lean checks pass. Recovered/already-present images cannot mint another delivery permit. No Host/controller delivery is established by this cut.
- **cacc4ae:** private completion plan/assembly routes70/71 and strict committed-v3 claim inspection. The plan selects admitted claim history, verifies the distinct physical custodian report and checks current package/law; op38 still re-admits. Source-matched Host checks and focused broker test pass. A linked combined Host is being prepared from this exact commit, not a floating worktree.

Evidence is in Mini docs/evidence/2026-09-27-spk-lifecycle-stop-author/, spk-v3-continue-claim-client/, agent-lifetime-dispatch-receiver/, and lifecycle-launch-completion-host/ (all directories use the full date prefix). These are component qualifications, not a deployed integrated journey.

## Defects found by cross-layer review

The source authorization operation ID is a full cSHAKE256 digest value. Rust's physical VerifiedBegin operation_id was u64, so almost every real source-authorized launch would fail conversion. agent_api_host owns preserving the complete canonical decimal identity through the physical journal; truncation is not an acceptable mapping. The guarded cut above predates that repair.

STOP increments the operation generation but must stop the already-running process incarnation. Current authoring instead names the next generation's unit; its report check repeats that wrong target. mini_app_contract owns a receiver-enforced historical running-completion binding, including actual unit/invocation/cgroup, with current phase/generation checks. This must be enforced at admission/replay, not merely by the friendly author. Historical v2 behavior remains separate. The new physical report author/signing route and Rust stop/completion consumer must agree with the repair.

## Continuing work and live handle

The corrected event22 fixture remains active as mini-event22-r2-client-session.service, PID3594014, invocation5167adaea3c74d7e9f7d2d7715ffa18b. Its pre-reserve status1 check passed; the agent reports it is submitting the tool reserve. Poll this same unit before treating it as stopped. No share-issue or integrated base result is claimed yet.

Root requested the next independent combined native build from exact cacc4ae using guarded warm-cache reuse. This is an executable integration step and reusable compiler output, not evidence that pending report/STOP/lifetime routes are included. build_native owns the immutable snapshot, bounded compiler seats and manifest. fn_mini_review owns shared Main/Json/broker hooks; fn_contracts owns event27 grant author/receiver; runtime_review owns event26 authoring; client_session owns the live fixture and subsequent fresh integrated base. Agent names are ownership records, not proof of a running process.

Next physical milestones remain real signed GitWeb INSTALL/create, signed completion, repaired STOP/continue and persistent volume recovery, followed by two participant web/API/CLI use and hosted real-model Hermes with hard/soft disconnect. Selected fn publication/receive and measured core latency remain required. Provider model/spend and protected credential staging are still pending; no charged model call has been run for this integrated fixture.
