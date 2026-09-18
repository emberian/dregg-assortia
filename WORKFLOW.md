# Keeping the hub current

`graph.jsonld` owns current work records and scoped source assertions. Generated pages display those facts; dated notes explain interpretations and retain run evidence. Do not maintain a second handwritten status board.

## At a work handoff

Record the intended capability, user-visible result, actual receiving consumer, exact write scope, owner/reviewer, prerequisites, next action and closure condition. For externally delegated features, link the concrete interface contract and a runnable acceptance harness. A proposed interface is marked proposed and has an upstream owner; an existing interface has source/revision evidence.

An internal agent lane and a substantial contributor feature can contain different amounts of work. Both need a legible boundary. Task availability must come from a stable, usable contract, not merely from finding files the swarm is not editing.

## After a checkpoint or useful result

1. Capture the actual source identities, command/configuration, result and relevant output. A failed or unrun check remains so. Store a bounded evidence artifact here when its original log is temporary.
2. Add a dated `Source` and link it to the appropriate assertion/work item. Preserve older source hashes; do not relabel an old result as a new run.
3. Update owner, `status`, `progress`, `nextAction`, `blockedBy` and `updatedAt`. Change the closure condition only when scope actually changes, recording why.
4. Run `python3 hub.py check`, `python3 hub.py render`, and `python3 hub.py render --check`. Commit and push relevant hub changes alongside implementation checkpoints.

## Work states

| State | Meaning |
|---|---|
| `backlog` | Identified work without a current assignment or sufficiently complete handoff. |
| `ready` | Brief, write scope and acceptance are present; no blocking prerequisite remains. It may still be unassigned. |
| `active` | A named owner is progressing it. Partial dependencies can remain while independent work continues. |
| `blocked` | A named prerequisite prevents further meaningful progress. |
| `done` | The stated closure is met, with explicit linked completion evidence. |

Use `blockedBy` for actual blocking records. `dependsOn`, `related`, and `sources` retain context and provenance; they are not interchangeable with blockers. A dependency cycle needs design repair. The checker rejects cycles, ownerless active tasks, falsely ready blocked work, dangling graph links and completion without evidence.

## Decisions and uncertainty

Keep ember's accepted direction distinct from agent proposals. A question about intent differs from unimplemented agreed behavior, an unconsumed implementation or an unexercised path. Assign the next action accordingly. No absence of a graph edge establishes that source or functionality is absent.

Source snapshots, component checks, integrated journeys and live deployment each have their own scope. Documented does not mean fixed; component passed does not mean the user can use it. A discovered gap stays an implementation task unless it follows from the actual system model.

The current Git records do not settle the choice of a future issue/discussion service. Any later interface should consume these stable work identities and provenance instead of creating an unrelated project history.
