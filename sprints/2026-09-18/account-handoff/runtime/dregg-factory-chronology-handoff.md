# Factory deployment chronology — current checkpoint

Base: breadstuffs 73136dd30. Owner: sprint_kernel_carrier. Root owns git and remote checks. Source SHA manifest: /tmp/dregg-factory-chronology-source-checkpoint.json. Implementation source is frozen for first focused remote check; native test results are pending.

## Confirmed defect

World::try_deploy_factory changed the live executor, replay recorder executor and a volatile descriptor vector, but appended neither RecordedStep nor WorldOperation. Durable reopen reconstructed an empty registry. World::replay_to_step and the reversible mirror instead preloaded the complete present-day descriptor list at step zero. ReversibleHistory::fork_at retained that timeless list. Current-state World::fork redeployed descriptors into empty registries, losing creation counts and epoch.

FactoryDescriptor.factory_vk is the supplied registry key. It is not descriptor.hash(). The underlying FactoryRegistry::deploy is first-wins; its return alone cannot distinguish successful insertion from a conflicting existing descriptor.

## Implemented source contract

- Shared turn::reversible::FactoryDeployment retains the entire descriptor (including its registry key) and the existing complete descriptor commitment. validate checks that commitment. validate_new/apply refuse duplicate recorded keys and invoke the actual TurnExecutor::deploy_factory; they do not implement a second factory evaluator.
- Live World deployment first checks exact full-descriptor equality at the supplied VK. An identical call is a no-op with no new history or durable publication. A differing descriptor under that key is an explicit error and leaves the World usable and unchanged.
- Every new deployment atomically publishes the ordered step plus history head using the existing redb config batch, before changing either in-memory executor registry. Failed I/O or lost response after publication leaves RAM unchanged and latches the durable World unavailable until reopen.
- RecordedStep, WorldOperation, RecoveredStep and ReversibleStep carry the deployment. History, durable reopen, detached World replay, reversible mirror and temporal branch warming apply it only at its recorded boundary.
- No timeless with_factories/replay_factories/deployed_factories path remains in the World/history code. Current-state forks clone the actual FactoryRegistry including counts and epoch; past forks derive state by the existing accepted executor replay.
- Deployment is an irreversible setup boundary for cell-only undo. It remains explicitly trusted setup, not an accepted runtime turn.
- World history schema version is 2. Existing discovery keys are retained so v1 is detected and refused, never reset. Even a v1 ledger with no factory-dependent turn cannot distinguish no setup from an unused, silently discarded deployment. Automatic complete reconstruction therefore is not claimed. Migration requires external evidence. New v2 ordinary images retain their existing ledger/receipt semantics.

## Verification request

Remote native command: cargo nextest run -p starbridge-v2 --lib --no-default-features --features embedded-executor -E 'test(/factory_chronology_/)'. Keep the real Lean archive / DREGG_REQUIRE_LEAN. Source syntax: focused rustfmt passed. No local Cargo run.

Five tests are enumerated in the SHA manifest. The main journey uses a real factory constructor followed by an accepted transfer into the born child, an intermediate checkpoint before later deployments, and drop/reopen. It compares exact canonical factory snapshots, receipts and every World/History/reversible prefix; checks constructor refusal before deployment and acceptance after it through all three branching consumers; tests exhausted quota in a current-state fork. Other tests cover identical/conflicting registrations, precommit I/O failure and committed-but-lost response, descriptor/VK tampering and duplicate journal entries, preserved unpublished tails on refusal, and preserved v1 evidence on migration refusal.

Relevant regression followup: existing replay/history/time_travel/ordered persistence and World factory tests. The desktop provenance match is updated; desktop feature compile is separately required. Timing is unmeasured; if the new native journey exceeds 60 seconds, coordinate explicit heavy-profile routing with resource_history instead of leaving it slow in default.

## Precise assurance boundary

Existing World/History roots remain ledger roots. A factory deployment changes executable registry authority while leaving those roots unchanged; its record carries the separate existing descriptor commitment. The actual executor replay derives creation counts/epoch. The tests compare complete RegistrySnapshot images at every prefix and reopen. This does not introduce an externally anchored whole-World commitment including registry configuration, or a Lean refinement theorem for the physical journal, or a claim that the existing old STARK statements are now sufficient.

The global FactoryRegistry::deploy API is unchanged; explicit conflict refusal is enforced at the World/recorded-deployment boundary owned by this repair.

## First native check and compiler repair

/tmp/dregg-ffi-factory-fast-20260918.log: FAIL101 before tests. dregg-turn E0596 at the new recorder required a mutable ledger for its cached Ledger::root. Both History and ReversibleHistory recorder signatures now take &mut Ledger, with actual World/time_travel callers migrated. The persistent publication method still borrows the ledger immutably. Focused rustfmt passes; source manifest refreshed. Same selected remote tests await retry.
