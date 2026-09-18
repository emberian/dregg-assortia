# Operations orientation — 2026-09-17 (read-only)

## Recommendation

The materially closest offering path is **a DreggCloud House composed with
breadstuffs**, not DreggNet alone. DreggCloud already provides an operated,
durable House with a browser Workbench, a House/substrate transition journal,
Cipherclerk command custody, and a concrete signed-member journey in
`Expedition`. Breadstuffs supplies the prospective community's capability,
receipt, agent/tenant, Hermes, document, and composition primitives.

DreggNet is the nearer path only if the first product is a paid managed-runtime
service. Its gateway/control/bridge/durable layers model persistent,
owner-scoped server workloads, but it does not supply the friends/invitation,
collaborative-document, or local-first social surface.

## Evidence-backed refinements

1. **Connected member journey exists, but is Expedition-shaped.**
   `DreggCloud/docs/EXPEDITION-HOUSE-INTEGRATION.md` specifies and describes a
   deployed hbox create -> join -> round -> propose -> vote -> resolve -> restart
   -> replay journey. A Host signs the exact invitee key and the joining key
   proves possession; the public mutation routes admit only exact signed Ed25519
   envelopes. This is the strongest current friend/invite/custody path.

2. **Persistence and custody are stronger than a UI save.** The same contract
   treats the canonical replay-verified Expedition archive as source of game
   truth. It journals archive-first settlement, binds a House checkpoint and a
   breadstuffs campaign cell/receipt, and fails closed on tampering, rollback,
   mismatched projections, or incomplete recovery. It explicitly does not make a
   member key native dregg authority or federation consensus.

3. **House identity is real but bootstrap remains operator-centric.**
   `DreggCloud/docs/SELF-HOSTING.md` documents a persistent House ID/local
   Ed25519 seed, one active Cipherclerk profile, hybrid signed ordinary commands,
   and no bearer override after enrollment. It also says the product is an
   operator-controlled experiment, not an unattended public multitenant service;
   the browser member seed is localStorage with no multi-device recovery or secure
   credential store.

4. **Hermes and tenant mechanics are substrate capabilities, not the delivered
   social product.** `breadstuffs/deos-hermes/src/acp.rs` implements an ACP
   permission seam that routes Hermes tool calls through a cap-gated
   `HermesGateway`. `agent-platform/README.md` defines a hosted cap-and-budget
   bounded tenant session, and `dregg-agent/src/session_store.rs` guards persisted
   session budgets across reconnect. DreggCloud depends on these organs, but the
   active public community/House journey does not yet establish an end-to-end
   Hermes-per-member offering.

5. **Git/document work has capable primitives but no operated workroom.**
   Breadstuffs `dregg-doc/` supplies repository/document/review/proposal concepts.
   The desktop composition repair at breadstuffs `5b28d0826` made a document
   composition gesture commit citations and receipts. But
   `DreggCloud/docs/SEMANTIC-HOUSE-WORKROOM.md` says the semantic workroom route,
   schema, landing repository, and presentation do not exist. Its
   `semantic-workflows` custody component retains/replays a bounded proposal
   archive but explicitly is not a House route or landing executor.

6. **No Fossil VCS product seam was found.** The relevant `fossil` hits are
   internal historical/registry language, not an integration with Fossil SCM.
   Treat “Git primary, Fossil non-VCS tracking” as a product decision needing a
   new explicit adapter and evidence model, not as a feature already available.

7. **DreggNet is a useful runtime complement, not the social front door.**
   Its `gateway/src/vats.rs`, `control/src/server.rs`, `durable/`, `bridge/`, and
   `exec/` implement owner-scoped persistent endpoints, durable workflow
   recovery, metering, and an owned execution engine. This can host a member or
   agent process later. Its README frames it as the operated paid execution
   layer; it lacks the DreggCloud Expedition-style signed invite/collaboration
   surface.

8. **dClutch is adjacent operational work, not the community path.**
   `dregg-infra` main `140b2b41fc23` contains two separate dClutch commitments:
   the anchor mainnet observer relay (`9349c51588f7`, recorded one live observed
   cycle/public signed log) and the hbox devnet activity supervisor
   (`hbox/dclutch-activity/`). The latter is intentionally unactivated by default:
   its example values remain `UNCONFIGURED`, default mode is `armed-no-send`, and
   `VALIDATE_LATER.md` lists activation checks. It competes for hbox/operator
   attention but does not provide community identity, invitations, tenancy, or
   Hermes. The relay's append-only public observation log could be an external
   evidence pattern, not a user community backend.

## Boundaries to preserve in planning

- distinguish House/operator custody, browser-member key custody, and native
  capability authority;
- distinguish House/archive replay evidence from federation finality;
- record each code claim separately from captured/deployed evidence and from
  current dirty worktree state;
- use DreggCloud's Expedition path as the concrete social prototype while
  keeping the semantic workroom and Hermes tenancy as named integration work.
