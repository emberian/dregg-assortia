# Overnight construction checkpoint — September 26, 08:43 UTC

The overnight goal remains active. The new Mini host now builds on Mac and Linux, and integrated grain/fn receiving runs are underway. This is an intermediate checkpoint; the previous [checkpoint](checkpoint-2.md) preserves earlier evidence.

## Linked receiving system

Mini [b7de616](https://github.com/emberian/minidregg/commit/b7de616) records two native executables from the same frozen B source: build-relevant Lean at `591a5a9` plus the grain audit correction at `3744eb2`. Both passed all 162 Host dependency modules, native linking, usage checks and post-build source-hash verification. Mac SHA-256 is `c2a1fd3699338f28eaf1d076b53cbd1bf27b4438b857b0482666205b334a394c`; Linux is `faf1f8371f692c404acd5b4c5727bd2019249c1b5f7d1850022789d35f4ee30f`. [Build manifests](https://github.com/emberian/minidregg/tree/b7de616/docs/evidence/2026-09-26-mini-final-b) distinguish these gates from the separate pending umbrella check.

This source includes grain birth/policy authoring, parent-generation witnesses, persistent B fn opcodes 12/13, variable-length Message-ID handling, stack-safe codecs and the V2 evidence package. Later A reply and empty-page changes are separate builds. Fresh signed grain journeys are running on both platforms. In the fresh distinct-node fn run, B's real typed socket poll, signed submission through that socket, exact Mini export, transaction-selected ACK and matching fn cursor position passed. The subsequent Q/A exchange is still running; its final verdict is not claimed here.

The Mac executable exported the second accepted signed call from a real B history into a 326,022-byte V2 package. An independent pin with empty storage paths re-admitted it and returned the original receipt with accepted count 2. [The package, receipt and exact configurations](https://github.com/emberian/minidregg/blob/b7de616/docs/evidence/2026-09-26-fresh-fn/mini-b-two-event-v2.md) preserve that evidence. Carriage of this larger package through fn remains a receiving test to perform.

## Lifecycle and protocol repairs

Mini `c0eeacd` checkpoints durable held-charge markers, exact lost-reply lookup, conservative recovery, a separate administrative socket, bounded ACP/MCP queues and named resource reads. An unresolved lookup remains unresolved; it does not prove an earlier submit failed. Reconciliation uses signed Mini settlement, and external-effect acknowledgement remains a distinct action. Focused Rust checks passed; native lifecycle evidence is still being collected. The public connector cannot dispatch administrative reconciliation.

The hosted tool surface now selects a named resource and its observe grant. Publication uses a separate tool grain allowance and a parent-generation witness in the same Mini transaction. The active acceptance recipe creates actual parent, tool and publication resources and drives these tools through the real MCP/controller/native path. Its ACP peer is deterministic protocol scaffolding. Actual upstream Hermes initialization has passed separately in Linux confinement; a deterministic local model-protocol fixture is being prepared to test unmodified Hermes's tool loop without making a paid provider request.

Two new receiving gaps are being repaired rather than left as service limitations:

- fn can scan 16 unrelated events and return an empty advancing page. Mini previously rejected it and would poll that same page forever. `9004b28` records a gateway-authorized progress-only Mini atom before ACK, with exact historical cursor recovery, scoped status checks and idle handling. General Lean facts and narrow source checks pass; real neutral-page liveness is the next native test. A-side use of the same mechanism is following.
- The runtime created a new Hermes session for every prompt. Upstream supports durable `session/load`; the runtime is adding task-bound session identity and explicit handling when an interrupted first prompt never persisted. No silent claim of resumed conversation is acceptable.

The maximal selected-profile codec probe also passed with the full nested opcode-12 JSON response: 5,660,971 bytes including the opcode, below the 6,194,884-byte frame cap by 533,913 bytes. This uses synthetic maximal byte shapes and does not establish authentication or transport of a real maximal fn article. The earlier raw intent size was not the wire response size.

## Fn qualification and next work

Read-only inspection found fn's already-qualified `bbf52159` image includes the larger composite/consumer bounds. Its immutable hbox qualification manifest passed 58/58 hashes. [The captured qualification](https://github.com/emberian/minidregg/blob/867da1c/docs/evidence/2026-09-26-fresh-fn/fn-bbf52159-qualification.md) resolves image availability; the old specification's limits still need alignment. The first B socket baseline retains qualified `1a9dd747` and its smaller selected profile. Subsequent full A/B and larger-carriage trials should use the qualified newer image. Claude's fn checkout and protected live node remain untouched.

Continue the actual receiving runs, fix concrete failures, and then connect a newly accepted grain publication to fn correspondence and another Mini's readable resource. Preserve the immutable B build while linking the committed A/skip changes. Finish physical launch fencing and conversation continuity, and exercise the real upstream Hermes tool loop. The provider-custody proposal uses a separately funded Mini provider task before HTTP forwarding; that gateway is still unimplemented. No token/stake or real provider request has been made by this cycle.

Root continues to own integration, scoped commits/pushes and the graph. The scope remains the shared programmable infrastructure Ember requested; this checkpoint is not a stopping point or a deployed-service claim.
