# Checkpoint 72 — admitted app, confined Hermes startup, remaining shared-host seams

September 27 local / September 28 UTC, 2026. Full shared-platform acceptance
remains open. This updates [checkpoint 71](checkpoint-71.md).

## Actual retained r3 progress

The single USER recovery invocation `eb28b8d18f7e4a9f8ae0fe3d280dad67`
remains active under client_session's exclusive Store ownership. Parent
attach/reserve and tool attach/reserve are installed at counts13–16. Root
independently read the installed app receipt at count17:

- transaction `56109813319068059536196546150374919716842390241189456125589206890373738641302`
- event `54638337395155920686298871137603502384755884298955031771825836616268407460215`
- boundary `39758358278986623941309516373267208335239146052466564230245533901313688222945`

The owner subsequently verified exact app replay at count17 and the retained
image comparison; session reserve is installed at count18, and Alice Web
session birth is installed at count19. Its readbacks/replay and the remaining
participant births are still running. This is application-resource admission,
not physical package installation or running GitWeb. Preserve the original
refusal, recovery directory and unit; do not restart on observation timeout.

## Reviewed and committed work

- Mini **9f1fded** provides the source-authorized resident STOP supervisor.
  Review closed partial report/assembly recovery and concurrent op38 submission
  through a protected operation-wide lock. Eight focused tests and strict
  Clippy passed; actual same-Store STOP/continue remains unrun.
- **c5a5d45** issues agent lifetime grants from retained event22 lineage;
  **4be853c** issues agent tickets using the real signed package's API
  interface and explicit, nonobsolete role permissions. Shell/schema gates
  passed. Neither is a live accepted ticket/grant result.
- **7313d9f** retains actual unforked Hermes6d8a8beb startup in a network-isolated
  hbox worker. Root checked the separate network namespace, loopback-only
  addresses, absent external route, ACP initialization and stopped worker.
  The dedicated root-owned bubblewrap/AppArmor profile leaves global restrictions
  unchanged. **bf1906a** updates the launcher guide. No model prompt or MCP
  call occurred in this startup check.
- **37f0cb2** records qualified native Host8c13c42 and malformed-grant rejection
  in 5.49s without Store mutation. Predecessor d48 timed out at180s; this is
  fail-fast evidence, not accepted event27 evidence.

## Integration now being finished

One persistent Host must serve both agents. Source review discovered singular
provider and lifetime-dispatch pins that would admit only one configured route.
The coordinated Lean/Rust batch adds bounded operator service lists: continuity
selects a provider from the signed reserve targets, metering selects its fixed
tariff, and lifetime dispatch requires one exact full selector match. Legacy
scalar metering keeps its v1 wire; list metering uses v2. Rust suites passed
136/136 and101/101 plus strict Clippy; Lean validation and combined native
qualification remain pending. Do not deploy two independent Store writers as
a substitute.

mini_app_contract owns physical INSTALL/START preparation after base handoff.
The journey needs explicit signed-package materialization between INSTALL
claim and completion, plus source-bound volume creation/attestation. Recovery
must inspect an existing installed image without inventing an old ingest
execution receipt. agent_api_host is adding human ticket issuance/custody for
Alice/Bob entrances; agent-only tickets do not satisfy human START routes.

The independent fn recipient now has empty content600 under owner7 law and
progress601 under gateway8 law. Event20 planning exposed fn's launcher-relative
core path when the Host snapshots just its executable; the owner is pinning
the complete runtime through an absolute-path wrapper. No real selected app
article has been published or ACKed. Source remains r3 content8001/cap89.

Qualified Linux18166e5 runtime/bridge and Mini binaries are available;9f1 SPK
build is queued. These precede the uncommitted shared-host batch. Hermes r2
composition is waiting on one existing hbox copy job. Hbox currently reports
heavy disk waits with a healthy pool and available memory; preserve running
handles and avoid duplicate jobs. Persvati remains the bounded build lane.

Next acceptance remains: finish all participant births, physical INSTALL and
START, source-accepted human/agent grants, actual shared browser/CLI/Hermes
operation with local Bonsai, lifecycle/disconnect/revoke recovery, then selected
real GitWeb content through Mini and fn to independent signed readback.
