# Overnight construction checkpoint — September 26, 07:28 UTC

This is an intermediate checkpoint while the overnight goal remains active, not a release or stopping point. [The construction brief](overnight.md) records ember's authorization and the recovered starting point. Mini main contains the implementation checkpoints below; integrated native acceptance is still running or waiting for the new executable.

## Published implementation

| Mini commit | Change | Measured scope at this checkpoint |
| --- | --- | --- |
| `14e4981` | Operational replay constructs admitted-step traces; cached history composes with a checked exact-prefix extension. | Isolated narrow Lean check passed. Reported theorem axioms are Lean's standard `propext`, `Classical.choice`, and `Quot.sound`. The native helper/OS refinement is still an explicit boundary. |
| `e46cd47` | Durable fn reply creation context, versioned sidecars, exact source parsing, and source-owned grain intents with atomic publications. | Narrow module builds and focused source/codec probes passed. |
| `d0cc5cd` | Independent gateway identity and policy pin, current subject-lock law, pinned historical selectors, removal of arbitrary sixteen-event consumer-history caps. | Narrow module checks passed. Actual signed non-gateway receiving refusal is a separate pending probe. |
| `d60abb8` | Persistent refreshed host session, source authoring/inspection/assembly operations, pinned verifier executable, gateway and reply-profile integration, exact-source ACK checks. | Narrow Host/Main dependency chain passed. Full umbrella/native build is underway. |
| `bc3a581` | Private Unix-socket broker and resource-client transport, exact retained calls, bounded request/reply waits. | Nine focused Rust tests passed, including stalled pipes and preserving repeated argument order. Native client-to-session acceptance remains pending. |
| `01e6448` | Bounded native builders support Linux x86_64 and macOS arm64. | Shell syntax/static checks passed; this is not a completed Linux build. |
| `791a6d2` | Reply Message-ID parser reads the canonical variable-length digest encoding. | Narrow build and 64/68-hex-character regression probes passed. The failed fresh fn exchange motivated this repair. |

All these checkpoints were pushed to Mini main. They exclude other sessions' compiler/prover/licensing WIP and rejected untracked Python platform scripts. Exact compiled-source manifests govern forthcoming binaries; a nearby provenance file is not sufficient evidence.

## Failures exposed by fresh inputs

The qualified fn exchange previously reused an old Mini fixture. Recreating custody, genesis and a gateway resource revealed two independent failures:

1. The actual B-side observation intent was 102,872 bytes, exceeding its configured 100,000-unit cost allowance. A fresh explicit 300,000 allowance let the real B transaction, export and ACK proceed. Authorization was not weakened.
2. After signed Q peering and restart, A rejected the generated Message-ID. Publication encoded a digest using a variable-length canonical Nat codec, while parsing assumed exactly 66 hexadecimal characters. The fresh identity produced 68. The parser repair above removes that assumption; no key search was used to hide the failure. The complete exchange must be rerun on its rebuilt host.

The fn harness still takes one Mini input set for both sides. Mini now contains an adaptation under construction that patches a private copy of the exact existing harness to accept separate A/B genesis/configuration/keys/policies. The upstream request is `PKT-codex-001` in Mini's `docs/FN-UPSTREAM-REQUESTS.md`. Claude's shared fn tree and protected live node are untouched.

## Work actively converging

- **Physical grain runtime:** signed Mini observation and source-owned reserve/settle/fence transitions, hard/soft terminal attachment, actual upstream Hermes ACP, retained attempts, process supervision and restart reconciliation. Source compiles and a normal process-group descendant-stop test passes. This is not yet a hosted-user acceptance result.
- **Hermes resource tools:** controller-side MCP with a distinct tool-task budget, configured publication targets, and atomic parent-generation/state checks. A separate tool task alone does not inherit its parent's disconnect fence; the joint receiving path must enforce that relationship. Source work and adversarial review are active.
- **Bootstrap:** atomic native grain birth with the actual AgentGrain initial page and policy; reproducible task/tool-task custody and grants. Avoid manually reconstructing semantics in shell fixtures.
- **Persistent fn operation:** operator-fixed manifests/control paths, an empty-payload poll request, claim derivation from fn's projection, and a typed returned decision/intent. The public Rust socket will expose it only after compilation and receiving checks.
- **General portable evidence:** remove the first-event-only evidence restriction while retaining exact original receipts and fully verified prefixes. Byte limits must agree across source, carrier, report and transport; fn's selected Store article limit must support the chosen profile.
- **Linux hosting:** isolated persvati user-systemd/cgroup and bubblewrap probes, followed by actual containment integration. Ordinary process groups do not stop descendants that escape with `setsid`; no stronger guarantee is claimed from the existing test.

Root integrates and commits. Sol lanes own separate files; `runtime_review` checks failure paths and `build_native` coordinates at most two local Lean compiler seats. Persvati has pinned dependencies/cache in an isolated lane, ready for Linux compilation. Build and native runtime evidence will supersede the pending statuses here through new dated records, without rewriting this checkpoint.

## Semantic boundaries retained

Fn ACK declares durable processing already recorded by Mini; it may settle an exact historical inbox after a Mini mutation grant is revoked. A fresh application operation still faces the current gateway pin, policy and authority. ACK must match the exact retained carrier, source and cursor/report, not only transaction coordinates.

A hard disconnect physically interrupts owned execution before waiting for Mini. Previously submitted external work can have an uncertain result; durable reconciliation and the kernel generation fence are separate from process death. No worker receives the controller's custody key by virtue of an MCP connection. Hosted provider custody/metering, live economic operations and deployed STARK assurance are not established by this checkpoint.
