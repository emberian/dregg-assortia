# Start here: DREGG handoff

Prepared September 19, 2026 (final cycle evidence extends into September 20 UTC), for a person or agent who has not followed the conversation. This is a navigation and restart guide; [graph.jsonld](graph.jsonld) owns work status, and dated evidence owns measured results. No private chat history or access to ember's machine is required to understand the handoff.

## First reading, in order

1. This page, then [the completed Mini cycle result](sprints/2026-09-19/cycle-1-result.md). The result distinguishes implemented behavior, actual native runs, proof/build scope and remaining work.
2. [Current work](CURRENT.md) and [project map](MAP.md). Repository inventory hashes are historical observations, not assertions about today's checkout. Check Git before editing.
3. [Intent](intent.md), especially its dated clarifications; [hosted Hermes direction](sprints/2026-09-19/direction.md), [disconnect semantics](sprints/2026-09-19/connection-breaker.md), and [the decision to build in Mini](sprints/2026-09-19/rebuild-in-mini.md).
4. The destination repository's instructions, the relevant work record and actual source. Older orientations, the initial cycle contract and the integration checkpoint retain their dated scope; the completed result supersedes their pending cycle-1 statuses.

For someone receiving a feature assignment, also read [the contributor guide](contributing/README.md). No new owner is assigned by this document. Wisper is working on separate low-level networking; the preserved resource-host brief is unassigned.

## What we are building, and settled decisions

Friends and Discord participants should inhabit a programmable DREGG resource world through a complete hosted **Nous Research Hermes Agent** experience, potentially entered through SSH. Shared research, social/story/game resources and public computations can coexist. The resource world should grow beyond its first interface, including participant-operated nodes. A plain hosted chatbot would not satisfy the intent. The exact first shared activity and network protocol are still open.

- **Mini is the construction home.** Bread is reference material; evaluating or preserving all its machinery is not a prerequisite. Assortia is the suite's knowledge and project-management hub. [The map](MAP.md) links Clutch, infrastructure, cloud, research and coordination repositories without treating them as one implemented system.
- **Lean owns semantics and admission; Rust supplies physical custody/client work.** Ember rejected a new Python platform. Existing Python hub tools are accepted. Untracked Python implementation attempts are not the chosen architecture or build entry point.
- **Rules change without implicitly revoking grants.** Uses face the current rules. Resources may deliberately lock their own management; there is no implicit owner repair bypass.
- **Hard disconnect is a circuit breaker.** Interrupt foreground tools/work and support recovery on reconnect. Explicit soft attachment permits continued work under existing authority and budget. A kernel generation fence exists; physical interruption and effect reconciliation still need implementation.
- **Initial hosted OpenRouter-key custody is acceptable.** BYO keys, metering, TLSNotary/parsing evidence and optional external unforked Hermes support are intended. They are not delivered by this cycle. Custody and proof of a recorded exchange are different guarantees.
- **Operate the intended semantics before full STARK assurances are complete.** This does not authorize overstating proof/deployment scope or bypassing semantic guards.
- **Contributed hosting and Solana utility remain goals.** The devnet intention is real locked $DREGG with penalties recorded only. The exact asset operation, custody/exit terms and deployment are undecided; this record is not authority to move assets.
- **Release cadence is the 13th and 26th.** The next target is September 26, with a desired demo around September 22–23. This is a momentum cadence, not a settled promise of all features above.
- **Git remains primary.** Fossil's issues/discussion features are an undecided option. Commit/push scoped work regularly; ember permits per-commit unsigned fallback when unavailable for 1Password signing. Do not change global signing settings.

## The verified stopping point

The [cycle result](sprints/2026-09-19/cycle-1-result.md) is the detailed answer. In brief: signed persistent task/content resources, atomic mixed-resource transactions, narrower authority, current-law observation, grant-preserving rule changes, per-capability revocation, exact retry/restart receipt recovery and deliberate management lockout execute through the native host and Rust client.

| Evidence | Exact boundary |
| --- | --- |
| Complete fresh eleven-event native journey | Mini `12e6608`, host SHA prefix `0da9f139`; PASS in 10,380 seconds. Includes actual lost reply, ten historical recoveries, unchanged full logical image on refusals/retries, stale-worker fencing and denied owner repair. |
| Latest full source-matched build | Mini `66d74dd`, host SHA prefix `3107faf3`; 581/581 local Lean sources matched, full umbrella/native build passed. |
| Latest executable runtime checks | Exact birth plus selected accepted/refused replay operations, including the final eleven-event history. **Not a second fresh full journey.** |
| Client and legacy acceptance | Both Rust-client recipes and native legacy scenario passed at their explicitly recorded sources; see the result's version table. |

The last implementation checkpoint is `66d74dd`; Mini `d84c753` adds the completed-cycle documentation. Bread `bca445bad` adds continuity only. Assortia `fedbe4d` contains the completed result/evidence before this handoff update. New handoff commits do not imply another runtime validation.

The complete evidence index and checksum manifest are [here](sprints/2026-09-19/cycle-1-evidence/INDEX.md). Proofs, compiled execution and deployed service are separate. Whole-image comparisons refer to the logical image returned by the store helper, not arbitrary SQLite file bytes. Native balances are synthetic. No complete hosted Hermes service, physical tool interruption, contributed-provider service, live Solana operation or deployed STARK assurance was established.

## Where to resume implementation

This is a proposed order, not a new assignment or implementation launch. Current work IDs and closure conditions remain in [the board](CURRENT.md) and [work records](work/records.md).

1. **W-HOST-SESSION: make the native receiver persistent and responsive.** Read [the concrete proposal](sprints/2026-09-19/next-cycle-host-session.md), then `Host/Main.lean`, `Kernel/NativeHost.lean` and `Kernel/NativeHostReplay.lean` in Mini. Fresh processes currently replay retained signed history. Preserve verified-prefix equivalence, current authority refresh, exact-preimage CAS, uncertain readback, original receipts, verifier identity and restart behavior. Cache no authorization decisions. This remains core construction, not a request to wrap the current latency in a UI.
2. **W-GRAIN-RUNTIME / CONTROL / TOOLS / BROKER: connect real Hermes and tool supervision to those resources.** Define process ownership, hard/soft disconnect, reconnection, background authority, custody and metering together. Inspect upstream Hermes at `~/pug/hermes-agent` if available; do not confuse a Bread component with a complete hosted deployment. The older Python wave and House reuse are not accepted implementation contracts.
3. **W-GRANT-REVISION: finish generation-wide native revocation and the delegated-grant/two-rule-replacement native case.** Preserve existing per-capability and current-law regressions. The current worker-generation restriction is authored resource law, not a generic predicate grant caveat.
4. **W-M26-DESIGN / W-SOLANA-UTILITY:** select the visible shared activity and exact economic operation with ember as needed. Tie the choice to the same resource semantics and participant-hosting direction.

The persistent-host proposal includes concrete counterexamples and acceptance requirements. Physical interruption needs evidence about the actual child process and external effects, not only a cancellation response. No successor needs to repeat the entire archaeological survey before implementing an owned next step.

## Run and verify without reconstructing the conversation

The hub can be inspected on its own with Python 3.10+:

```sh
python3 hub.py check
python3 hub.py render --check
python3 hub.py show W-HOST-SESSION
```

Run these from Assortia. Validate archived cycle bytes from the evidence directory:

```sh
cd sprints/2026-09-19/cycle-1-evidence
shasum -a 256 -c SHA256SUMS
```

Mini pins Lean in `lean-toolchain` (4.30.0 for this cycle), dependencies in `lakefile.toml` / `lake-manifest.json`, and Rust dependencies in each crate's manifest/lockfile. Its [client README](https://github.com/emberian/minidregg/blob/d84c753/native/resource-client/README.md) describes the executable JSON authoring, bootstrap, submit, query and retained-call retry interfaces. The two acceptance scripts generate their own fresh fixture keys, configuration and genesis; an outsider does not need our private fixtures.

From an independently prepared Mini checkout/snapshot, build the three small Rust executables as needed:

```sh
CARGO_BUILD_JOBS=2 cargo build --manifest-path native/resource-client/Cargo.toml
CARGO_BUILD_JOBS=2 cargo build --manifest-path native/credential-signature-verifier/Cargo.toml
CARGO_BUILD_JOBS=2 cargo build --manifest-path native/hyperdocument-link-sqlite-store/Cargo.toml
```

With the native host and helpers present, these are the actual client recipes (each output directory must be new; `jq` is required):

```sh
native/resource-client/acceptance.sh "$PWD/.lake/build/bin/minidregg-host" /tmp/mini-handoff-client-001
native/resource-client/authority-acceptance.sh "$PWD/.lake/build/bin/minidregg-host" /tmp/mini-handoff-authority-001
```

They take minutes, not milliseconds. Scripts support explicit `MINI`, `STORE_BINARY` and `SIGNATURE_BINARY` paths. Retained attempt directories contain private keys and signed requests: keep those local, archive only bounded public evidence. Do not reuse a live store for acceptance.

For a native rebuild, read Mini `scripts/build-native-host.sh --help` and `scripts/build-native-acceptance-runner.sh --help`. Use a real independent source/package snapshot, then its `.minidregg-native-snapshot` marker; the marker alone does not establish isolation. The host command is `scripts/build-native-host.sh --umbrella --output NEW_ABSOLUTE_BUILD_DIR --binary NEW_ABSOLUTE_BINARY_PATH`. The runner builder takes that build's `minidregg-host.rsp` and must run in the same snapshot. Its native invocation is `RUNNER --new-world HOST VERIFIER SQLITE_STORE OPENSSL NEW_ARTIFACT_DIRECTORY`. All executable paths should be absolute. See the [original run manifest](sprints/2026-09-19/cycle-1-evidence/final-new-world/manifest.txt) for the exact executed command, and [latest build evidence](sprints/2026-09-19/cycle-1-evidence/charge-build/README.md) for the rebuilt closure.

The recorded build was macOS arm64. The current shell builders contain macOS-specific `time`/`nm` options; a Linux build recipe is not validated by this evidence. Cold package preparation and a one-command portable bootstrap remain gaps. Do not launch an unbounded Lake build to compensate. The wrapper serializes Lean and bounds C jobs; `LEAN_NUM_THREADS` alone is not a Lake process-count limit. Materialize independent writable package state, never symlink another active checkout's `.lake` into the build. For Bread work, use its own `AGENTS.md`, lane leases and `pbuild` verdict discipline; do not run the entire debug gauntlet to orient.

## Local artifacts, shared work and continuity

- On ember's machine the installed host is `~/dev/minidregg/.lake/build/bin/minidregg-host`, SHA-256 `3107faf3583e4c4926feb8931edee6e0aea4f800617bc0969d9d3c845caebe4d`, with adjacent `.provenance.json`. Verify before reuse. It is not a Git-distributed binary.
- Build snapshots, compiled runners and private run directories are under `/tmp/minidregg-cycle-20260919/`. They are ephemeral conveniences, not portable handoff dependencies. Source, safe logs, manifests and outcome summaries are committed; binary/private-image bytes are not. Fresh acceptance creates new fixtures if those directories disappear.
- The completed cycle's agents/builds are not future task owners. Board `active` records retain root responsibility for unresolved work, not proof of a running process. Recheck current processes and ownership before starting work or reclaiming build seats.
- Mini and Bread contain unrelated staged, unstaged and untracked work from other sessions. Preserve it. In particular, Mini's compiler/prover/projection/licensing edits and Bread's FHE/circuit/turn edits were outside the completed cycle. Never sweep them into a handoff commit or delete them as debris. Compare current Git state; this is not an exhaustive or perpetual inventory.
- Root owns commits in shared trees; use current `main`, no shared-tree branch/worktree changes, stash, reset or cleanup. Commit only reviewed named files; `commit --only` still includes every hunk in those files. When the configured signer is unavailable, `git -c commit.gpgsign=false commit ...` is the authorized per-commit fallback.
- On this Mac, `/usr/bin/git` was blocked by an unaccepted Xcode license; `/Library/Developer/CommandLineTools/usr/bin/git` worked. Use that path if still needed rather than changing machine-wide license/settings. Homebrew-first PATH supplies the Python needed by repository hooks.
- Bread's last documentation push used its explicit `DREGG_ALLOW_DEAD_DOC_REFS=1` escape for existing repository-wide broken references; no native/proof gate was waived. [Exact publication scope](sprints/2026-09-19/cycle-1-evidence/bread-continuity/final-push.md) is preserved. Reinspect any future failure; this is not a standing hook bypass.
- `ssh persvati` and `ssh hbox` are available to authorized local work; check capacity and leases, use `/tank` on hbox, and follow repository build instructions. Machine access and secrets are not prerequisites for reading this public record.

When handing on again, follow [WORKFLOW.md](WORKFLOW.md): update graph-owned work, add dated evidence without rewriting old source hashes, regenerate views, and update this entry point if the stopping point changes. Preserve unresolved questions as questions. Link to the evidence rather than copying another divergent status ledger.
