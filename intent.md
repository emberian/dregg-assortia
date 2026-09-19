# Intentions retained from the current conversation

Initially recorded 2026-09-17; dated clarifications follow. These are ember's instructions and preferences, not claims about implementation. The [September 19 direction](sprints/2026-09-19/direction.md) is the latest product and operating update.

## First people and social arrangement

> the first users are mostly the people in the discord or my friends

> i basically want to offer to them a "shellserver" of yore, except built around our *own* cloud&dreggic offerings, and *hopefully* full Hermes integration

## What people do there

> inside the "shellserver" they should be metaprogramming a suite of dreggic resources that allows for social, xanadu, distributed, local-first computations...

The resource world is the lasting object. Hermes is a desired interface and participant in that world. An ordinary hosted chatbot does not by itself fulfill this request.

## Programmable nexus, Solana, and participant-operated nodes

Asked to choose a research workroom, social/game space, or public-computation workshop as the first activity, ember did not select one:

> I'm not... sure yet, honestly.

The next clarification identifies the desired shape of the offering:

> ideally would be dreggic/dregg-native, offer *some* kind of on-chain Solana something

> genuinely get the token going into 'utility.'

> remember that we have ~/dev/dclutch / ~/dev/dragons-clutch as well

> basically a "programmable nexus" that will **grow outwards to encompass all we offer and can doo**

> they can of course run their /own/ dregg nodes and host cells and whatnot!!

The initial set of activities remains open. The design direction is an extensible DREGG-native resource world that includes the Clutch work in its planning, offers meaningful Solana participation/token utility, and admits participant-operated nodes and cell hosting. The exact economic mechanism, chain/cluster, resource interfaces, and September 26 scope have not been chosen. The fieldbook in the earlier assistant draft is an example, not an accepted product target.

Ember then clarified that selecting one application genre is unnecessary:

> the "first application" can honestly be a mix of things, as long as its programmable at the dregg kernel level / integrated with a programmable shell at *some* level

Record the mixed offering as explicitly acceptable and kernel-level programmability / programmable-shell integration as central to it. The exact programming language, shell surface and depth of integration remain open. Neither a new shell language nor an entirely graphical authoring environment is specified by this instruction. The assistant's new-tool exercise is a proposed acceptance test for this direction, not a replacement for it.

## How the project becomes resumable

> I think we need to treat this as a semantic web / knowledge graph problem and do a lot of work *scaffolding how we will even think about this project, what it is doing, what it has ongoing, etc etc... we could make a new ~/dev/dregg-assortia for this...

The initial problem includes stale documents, conflicting accounts, incomplete integrations, research artifacts outside their intended consumers, and knowledge held only in sessions or ember's memory. The graph should represent useful capabilities and intentions as well as defects.

## Git and Fossil

> when i suggest fossil, i suggest it primarily for its *non-vcs* properties (issues, etc); we do want to continue using git-primarily.

Git remains primary. Fossil is a candidate for collaboration and project tracking. Preserving selected breadstuffs history/reference material is a separate decision; the conversation did not authorize treating the whole repository as retired.

## Method and authority

Ember invited recursive Terra assistance and a few turns of discussion about how to organize the work, then explicitly empowered deeper orientation and questions. The initial orientation used bounded read-only investigations and created reversible orientation artifacts. No implementation cutover, deployment, public posting, or tracking-system choice was made by that pass.

Ember subsequently updated the delegation preference: **mostly Astra**, with **Sol used selectively for bounded work**. The current nexus review follows that preference; the earlier Terra reports remain attributed evidence from the orientation.

The existing build/proof disciplines remain relevant. A working product slice should use the intended semantic substrate and expose its real remaining obligations; a separate throwaway semantics is not assumed acceptable.

Ember subsequently made the intended scale and method explicit:

> comprehensively rip & tear to address any gaps (implementing as far up and down every part of the whole stack at all times), instead of accepting limitations and working around them

> this is supposed to be a LONG sprint, and at least 20-60% of it is probably just work on the core system to get it up to snuff for our present purposes.

> remember to be swarming wide at all times !

Treat missing core/compiler/proof/runtime support as work to implement for the intended experience. Do not turn the current implementation boundary into an accepted product limitation or route around a refusing guard. The percentage is ember's planning expectation, not a measured allocation or ceiling. Use a broad, coordinated swarm with concrete ownership and frequent integration through the same resource journey.

Ember then deputized autonomous work, made the laptop, `ssh persvati` and `ssh hbox` available for the night, and noted that hbox primarily uses `/tank` because its root disk is usually full. Existing lease, memory and build disciplines still apply. Ember remains available for check-ins and consequential questions, and explicitly authorized reaching them through the old Telegram bot supporting `/chreatures`, to be located using `cv`. That authorization is a communication route, not evidence that a particular bot destination has been verified. No credentials or chat identifiers belong in assortia.

Ember also explicitly requests regular commits and pushes in every involved repository, including work-in-progress checkpoints that may not yet compile. Root owns those Git operations, commits named task files and preserves unrelated staged/unstaged work. Checkpoint publication does not establish test or integration success; the convergence record must retain that distinction.

## Current investigation and contributed hosting

Asked which earlier demo felt closest, ember answered:

> honestly none of it :( let's investigate just what we have now.

No existing demo is the selected product target. The immediate work is a present-state investigation.

On practical resources and the provider model:

> we have some 'homelab' hosting available to us, which is an unknown amount of extermely heterogenous resources....

> IDEALLY we'd be allowing people to contribute hosting resources for *certain* "publicly executable" jobz... integrated with uhh an optimistic/slashing-based reputation thing for the providers?

> we want to require providers to put up real $DREGG.

> "Fake-slash" it during devnet ... it'd just show up on a leaderboard instead of us actually charging them, at least during devnet

Asked whether devnet stake should actually be locked or merely simulated against verified holdings, ember answered:

> Lock real stake; record penalties only

This settles the intended devnet rule: providers lock real $DREGG; adjudicated penalties are recorded in reputation/the leaderboard without deducting the penalty from the locked balance. The custody mechanism, withdrawal/release conditions, eligible job semantics, dispute procedure, and any later monetary enforcement remain to be designed. No asset operation has been performed or is authorized by recording this decision.

## Release cadence and the next experience

Ember identifies the next task as establishing a consistent design intent and implementing it across the critical pathways required by the next user experience milestone:

> we have a consistent release cadence of the 13th and the 26th, and we presently have 9 days until the next Release Day.

> at swarmcycling speed, that 9 days is usually 27-50 swarmcycles

Recorded on September 17, 2026: the next release day is **September 26, 2026**. The cycle range is ember's report of the team's working pace, with ember participating in quality and design decisions; it is not a measured estimate for a particular scope. Plan substantial coherent work against this cadence. Do not substitute conventional staffing estimates or assume that every open research question will close within it.

The request has advanced from inventory alone to using that inventory to establish shared design intent and an implementable experience. The exact September 26 experience, receiving runtime, and release promises are not yet selected. [The release discussion draft](milestones/2026-09-26.md) is an assistant proposal, not an accepted design.

Historical context and exact cv session/message references are in [the intent archaeology](research/intent.md). Adopted goal/stop-hook instructions are distinguished there from ordinary user prose.

## Substantial external contribution (September 18 clarification)

**Superseded as Wisper's assignment on September 19:** ember assigned him separate low-level networking work outside the critical path. The following retains the earlier decision history; resource-host lifecycle is now unassigned design work.

Assortia is intended as a living knowledge index and project-management hub that makes substantial product work legible to outside contributors. Wisper is waiting for a specific opportunity. Ember rejected graph-tooling maintenance as that contribution, giving Android scaffolding with an embedded DREGG node and specified system/UI responsibilities as the scale of work intended. Ember subsequently suggested DreggNet/cloud as another possible fit for an experienced backend/platform engineer trusted with broad systems work.

Ember subsequently selected **cloud/resource-host lifecycle** as the area to offer Wisper. The exact kernel/host contract and first receiving runtime are still to be worked out together. This selects the contribution area; Wisper has not been contacted or assigned by the agents. The contributor can own design and implementation; this is not limited to consuming a finished API or building a UI wrapper. Internal hub tooling remains the agents' responsibility.

## Policy replacement and existing grants (September 18 decision)

Asked whether an owner changing resource rules should preserve existing grants under the new rules, with revocation separate, ember selected:

> Keep grants; check the new rules (Recommended)

The intended behavior is now settled. Source revision and grant-revocation generation must be distinct. Existing grants remain subject to their own scope, current signatures, expiry and the newly installed rules; this decision does not bypass those checks or promise that every old operation remains allowed. At the time of this decision, installation conflated revision and generation and invalidated grants. Current implementation and validation are tracked in W-GRANT-REVISION; this decision record does not establish completion.


## Resource management can govern itself (September 18 decision)

Asked whether ownership should provide a separate management right that can repair rules even when ordinary rules deny every operation, ember selected:

> Let resources deliberately govern—and potentially lock—their own management

A resource may deliberately deny further policy updates, including updates proposed by its owner. There is no implicit owner recovery bypass. Grant preservation across source revisions is independent: the grants remain present, and every attempted use still faces the current rules. Operational restart/recovery preserves accepted state; it does not override resource policy. The policy installer and host acceptance checks must retain a deliberate management-lockout case.

## Hosted Hermes and present operating mode (September 19 clarification)

Ember wants a complete hosted **Nous Research Hermes Agent** experience on our resources, with metering and DREGG kernel/shell programmability. SSH is one suggested entrance. External unforked Hermes support is desirable if practical; ACP, A2A, MCP and a custom interface are under discussion, with a preference leaning custom rather than an accepted selection.

Users may bring OpenRouter keys; ember explicitly accepts initial hosted key custody with Hermes receiving permission to request key use. The desired TLSNotary/parsing evidence must substantiate authorized request construction, not merely syntactic validity. Hosted custody remains a trust relationship, including the possibility of unrecorded use. Full STARK assurance need not precede operating the intended system semantics.

The desired demo date is approximately September 22–23, allowing iteration before September 26. Release days are a momentum cadence. Implementation remains wound down while the laptop is occupied by the separate formal-news project. A few read-only Sol investigations and lightweight project-record maintenance are authorized; earlier broad swarm authorization does not restart builds. See the [dated record](sprints/2026-09-19/direction.md) for exact distinctions between accepted direction, proposals and open questions.

Ember subsequently revised the disconnect preference: ordinary foreground Hermes work should pause on disconnect and resume on reconnection; only explicitly backgrounded work continues unattended. This supersedes the immediately preceding answer to continue the current task within budget. The exact interrupt/recovery mechanism, connection-loss detection and in-flight-operation handling remain design work.
