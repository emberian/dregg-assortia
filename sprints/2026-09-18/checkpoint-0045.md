# September 18, 00:45 EDT — current implementation and contributor handoff

This checkpoint records component evidence and open integration work. It does not declare the September 26 experience ready. Earlier [September 17 observations](../2026-09-17/checkpoint-2330.md) retain their dates and scope.

## Published work

| Repository | Published commit | Scope |
|---|---|---|
| breadstuffs | `c63e79bb4` | Atomic setup batches, exact history/cursor checks and rejected-candidate recovery. The later joined run below has two failures. |
| breadstuffs | `3b9497753` | SDK registration discovers six linked PQ exports without initializing Lean. The first actual call still initializes the real Lean implementation. |
| minidregg | `2a6ca15` | Mandatory source-family postconditions on accepted effects and actual joint post-state. |
| minidregg | `ccf75e9` | Compact reactive-terminal encoding, exercised with actual full-width cSHAKE values. |
| minidregg | `d5ba835` | Source-owned preparation computes the exact joint tuple before binding portals and authorization. |
| minidregg | `584b600` | Complete authority catalogue/shards, canonical resource registry, ordered Book operations, and resource-birth preparation. Preparation is not authorization or durable publication. |

The shared trees also contain subsequent edits. These commit identities are checkpoints, not claims about every later worktree byte. Root owns commits/pushes and preserves unrelated work. Breadstuffs uses the existing push hook's explicit dead-document-reference exception; its secrets scan still runs.

## What ran

- [Four SDK candidate tests](evidence/sdk-candidate-before-lazy.txt) passed before lazy initialization: paid late refusal, explicit rollback/unwind, nested checkpoints and deferred single observer publication. Each process took about 213–214 seconds. The [captured source manifest](evidence/sdk-candidate-before-lazy-source.json) fixes the tested scope.
- [Lazy PQ registration](evidence/lazy-pq.txt) passed through the installed full-byte ML-DSA key generator, including the NIST ACVP kg26 public-key check. Six route registrations leave Lean uninitialized; first use initializes it. That intentional first-use test took 188.347 seconds and is in the heavy set. [Source manifest](evidence/lazy-pq-source.json).
- [World/history attempt 2](evidence/world-batch-attempt2.txt) ran 16 of 18 selected tests: **14 passed, two failed, two were not run** because nextest stopped on failure. Both failures compare intermediate recorded roots across reopen; final state/receipt checks preceding those assertions passed. Repair and rerun are active. [Source manifest](evidence/world-batch-attempt2-source.json).
- The earlier real Hermes bridge passed through actual operations, readback and receipt retention after a later JS exception. Its startup fix is being remeasured; no new Hermes timing is asserted here.

## Current integration work

Birth-to-first-use exposed missing pieces that component proofs could not establish alone. The swarm is implementing committed signing-key bytes/epochs, exact-request capability-use witnesses, initial policy records stored in immutable source cells, and separate resource-edit versus policy-replacement authority. One source-owned runtime profile must give birth, invocation and policy installation compatible policy semantics.

The actual receiving journey remains: create a resource and its initial policy/owner rights/charge atomically; invoke under current authority; delegate a narrower operation to another participant; change policy only with the distinct controlling right; recover all accepted results after restart. Shared interfaces and their affected consumers are still converging. Subject-to-subject delegation needs an explicit authorized edge: existing holder-narrowing alone cannot represent it. The strict attenuation law must remain intact.

The native SQLite receiver and strict Ed25519 helper have component checks. Neither by itself closes the whole source-authorized resource journey. Known proof-statement weaknesses in the older stack remain separate tracked work; this checkpoint makes no new STARK security claim.

## The hub is part of the deliverable

Ember clarified that an external contributor, Wisper, is waiting for a legible, specific task. Assortia must now operate as a living knowledge index and project-management hub. Its graph owns current work records; generated views provide the current board and task details. Dated reports retain historical evidence instead of pretending to be current status.

Root initially proposed graph navigation as a first contributor task. Ember rejected that direction: Wisper should own substantial product work, giving Android application scaffolding with an embedded DREGG node and system/UI integration as an example. Ember then identified Wisper as an experienced backend/platform engineer suited to broad systems work, and suggested DreggNet/cloud as another possible area. The swarm is comparing existing mobile/runtime/cloud boundaries before proposing a concrete feature handoff. Graph tooling is internal agent work. No task has been assigned and no message has been sent to Wisper.

Solana custody configuration, provider job selection and the exact public September 26 offering still require decisions. The accepted devnet intent remains real stake locked with penalties recorded only. No live funds or public deployment have been touched in this sprint.

## Subsequent runtime measurement

The [four SDK tests after lazy registration](evidence/sdk-candidate-after-lazy.txt) pass in0.026–0.047 seconds each. That combined command did **not** select the feature-gated Hermes test. The separate [exact js-agent Hermes run](evidence/hermes-after-lazy.txt) passes in191.097 seconds: runtime/JS construction is now below10ms, but first connected verified admission takes about191seconds. The lazy repair removed eager initialization; first-use archive initialization remains active implementation work. SDK tests return to the default set; the actual slow bridge and intentional full-byte PQ first-use test stay heavy. The [captured source manifest](evidence/sdk-hermes-after-lazy-source.json) covers the lazy registration/SDK/bridge source; subsequent cache replacement edits were present in the later exact bridge build, so this is not a claim that the two builds had identical complete trees.

Minidregg checkpoints `c41d77e` (exact capability use, distinct policy replacement, regenerated artifacts) and `303280f` (source-profiled order compilation and canonical consumers) were committed and pushed. Three shared authorization modules and27 affected artifact modules passed; six compiler/profile modules passed at recorded source hashes. Native source-authorized receiving is still converging separately.
