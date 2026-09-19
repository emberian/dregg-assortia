# Contributing to DREGG

Contributors should be able to own a substantial part of the product, with a clear interface to the rest of the system. Assortia supplies the architecture, contracts, decisions, ownership and acceptance evidence needed to do that.

DREGG is a programmable resource world. People and agents create and operate resources under explicit authority; accepted changes and their history should survive restart and be usable by other authorized participants. The September 26 sprint is connecting the kernel, policies, durable runtime and user/agent surfaces. [The project map](../MAP.md) identifies the repositories; [the board](../CURRENT.md) identifies current owners.

## The next product work package

The preserved proposal is **[persistent DREGG resource hosting](resource-host-lifecycle.md)**: a substantial platform subsystem covering provider reconciliation, native-host recovery, supervision, custody, owner commands, operation status and resumable events. It is unassigned. The brief names inspected source interfaces, missing exports and crash/restart acceptance scenarios; its September 18 owner references are historical.

On September 19, ember reported assigning Wisper separate low-level networking work outside our critical path, superseding the earlier hosting proposal for him. The networking task's exact scope is not recorded here. Hosting's receiving runtime and exact contract still need design work. The [cloud review](../research/cloud-host-2026-09-18.md) and [mobile inventory](../research/mobile-2026-09-18.md) explain the inspected starting points.

The handoff must contain:

- The user journey and visible behavior the contributor owns.
- Exact interfaces for node lifecycle, identity/authority, commands, state/events, persistence and errors; which exist and which have named upstream owners.
- Concrete cloud or Android system/UI responsibilities, with identity, permission and lifecycle behavior specified.
- Repository/file ownership, build artifacts, a runnable integration harness and compatibility/version rules.
- Acceptance scenarios covering useful operation, refusal, disconnection, restart/retry and interaction with another participant.

The runtime and product owners must agree on that boundary. A contributor should not have to reconstruct it from swarm chat or guess which similarly named kernel path is intended. Follow [W-ANDROID-CONTRACT](../work/records.md#w-android-contract) for the unassigned hosting-contract work; the stable ID retains the original Android example.

Graph browsing and project-index maintenance are internal agent work. They are not the feature being offered to Wisper.

## Starting work

Read the feature brief and its interface contract, then coordinate its work ID and file scope with ember. Assignment is explicit; mention of a person in planning does not assign them. Read the destination repository's local instructions before implementation. The swarm works in shared trees, so a feature handoff must name files and owners that can change independently.

A useful contribution handoff names the commits, behavior delivered, commands and results actually observed, unresolved interface questions, and the next integration action. Proofs, tests and deployment are reported separately. [The workflow](../WORKFLOW.md) describes how that evidence enters the hub.

To inspect this hub alone:

```sh
python3 hub.py board
python3 hub.py show W-ANDROID-CONTRACT
python3 hub.py check
python3 hub.py render --check
```
