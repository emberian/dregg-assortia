# Current authoring and Hermes inventory (source-only)

**Method.** Read-only source review on 2026-09-17. I ran no builds, binaries, or
tests. Therefore every assertion headed “test source” describes an assertion in
test code, not an observed passing execution.

## 1. `CardEditor` has real mutations, but its default host is a fresh embedded ledger

`CardEditor::adopt` takes an owned `Applet`, a manifest, an author, and a held
authority. Its three public operations check that authority first:

* `edit_view` changes a `ProgramSource` held in the editor, copies the folded source
  into the in-memory manifest, then fires an internal `__authorship__` affordance;
  that fire is its receipt ([card_editor.rs:425-545](</Users/ember/dev/breadstuffs/deos-js/src/card_editor.rs:425>)).
* `set_field` registers a temporary `__set_field__` affordance and fires it
  ([card_editor.rs:547-567](</Users/ember/dev/breadstuffs/deos-js/src/card_editor.rs:547>)).
* `add_affordance` changes the in-memory manifest and the applet's live affordance
  map, then fires the same authorship turn ([card_editor.rs:569-589](</Users/ember/dev/breadstuffs/deos-js/src/card_editor.rs:569>)).

That fire does execute a `Turn` and returns a `TurnReceipt`, but an `Applet` is
constructed with `DreggEngine::new(EngineConfig::for_testing())` and Symbolic
witness mode by default ([applet.rs:115-171](</Users/ember/dev/breadstuffs/deos-js/src/applet.rs:115>)); the generic fire builds and executes that embedded turn on the applet's
own ledger ([applet.rs:311-377](</Users/ember/dev/breadstuffs/deos-js/src/applet.rs:311>)). This is an actual in-process state transition, not a `starbridge_v2::World::commit_turn` call.

The initial `PortableApplet::mint` writes the manifest blob to the new cell heap,
but later editor changes do not write the amended manifest back to that heap.
`reseal` only returns a manifest clone and `remint` makes a *fresh* applet
([portable.rs:173-212](</Users/ember/dev/breadstuffs/deos-js/src/portable.rs:173>), [card_editor.rs:591-604](</Users/ember/dev/breadstuffs/deos-js/src/card_editor.rs:591>)). Thus an edit is retained in the live editor/applet object and can be carried only by an explicit reseal/remint handoff; it is not automatically stored in the cockpit World.

## 2. The rendered cockpit card deliberately has two different substances

The current cockpit mode-card mount first creates an `AttachedApplet` over
`WorldSinkAdapter::live(world)` for binds and button fires, then separately mints a
portable applet solely for the `CardEditor` ([card_surface.rs:1693-1738](</Users/ember/dev/breadstuffs/starbridge-v2/src/dock/card_surface.rs:1693>)). `WorldSinkAdapter::live` clones the cockpit's `Rc<RefCell<World>>`; a fire builds
`World::turn` and calls `World::commit_turn` ([agent_attach.rs:39-97](</Users/ember/dev/breadstuffs/starbridge-v2/src/agent_attach.rs:39>)). Those are the same World/object identity the cockpit renders.

By contrast, `ModeCardSurface::edit_view` calls the separate editor and swaps the
re-folded tree into `CardPane`; its comment is exact that the live attached applet is
untouched ([card_surface.rs:1913-1986](</Users/ember/dev/breadstuffs/starbridge-v2/src/dock/card_surface.rs:1913>)). So the visible “edit from within” user action is reachable and repaints the current pane, but its provenance/state reside in the separate portable editor applet, not the focused live cell. `set_field` and `add_affordance` have no corresponding mode-card UI caller in the source search; their current callable entries are the Rust API and the JS authoring API below.

The full native card mount is not default: `starbridge-v2` defaults only to
`embedded-executor`; `desktop` includes `agent-js`, `dev-surfaces`, and `card-pane`
([Cargo.toml:151-174](</Users/ember/dev/breadstuffs/starbridge-v2/Cargo.toml:151>), [Cargo.toml:277-301](</Users/ember/dev/breadstuffs/starbridge-v2/Cargo.toml:277>)). The actual onboarding buttons that call the mode-card edit route are further
gated by `dev-surfaces` plus `card-pane` ([frame.rs:615-670](</Users/ember/dev/breadstuffs/starbridge-v2/src/cockpit/frame.rs:615>)).

## 3. Human and agent authoring use the same editor object model, via a JS thread-local

`JsRuntime::run_authoring` places an owned `CardEditor` in `CURRENT_EDITOR`, evaluates
confined JS, and returns that editor to the caller; it says explicitly that editor is
independent of any crawl/drive target ([js.rs:897-946](</Users/ember/dev/breadstuffs/deos-js/src/js.rs:897>)). The JavaScript surface exposes exactly
`deos.editor.editView`, `setField`, and `addAffordance`
([js.rs:559-596](</Users/ember/dev/breadstuffs/deos-js/src/js.rs:559>)); native handlers reject
a card ID other than the installed editor's own card before calling the three methods
([js.rs:1511-1523](</Users/ember/dev/breadstuffs/deos-js/src/js.rs:1511>), [js.rs:1590-1751](</Users/ember/dev/breadstuffs/deos-js/src/js.rs:1590>)).

`RunJsAuthoringTool` admits a `run_js` call through `HermesGateway`, adopts the supplied
card/manifest into that editor, and runs this JS surface ([run_js.rs:416-516](</Users/ember/dev/breadstuffs/deos-hermes/src/run_js.rs:416>)). `LiveAuthoringHands` receives its card via a factory, runs the tool, and records the
editor receipts ([live_js.rs:202-292](</Users/ember/dev/breadstuffs/deos-hermes/src/live_js.rs:202>)). Neither path supplies a persistence callback that inserts the amended card blob into a Starbridge World.

## 4. An external Hermes MCP call is executable code, but its default `run_js` resource is private

The `mcp-server` binary is a real stdio MCP server and an external Hermes session can
register it as `mcp_dregg_run_js` / `mcp_dregg_terminal`
([main.rs:350-455](</Users/ember/dev/breadstuffs/deos-hermes/src/main.rs:350>)). However its startup host calls `with_run_js` only under `deos-hermes/js-agent` and never
calls `with_world_bridge` ([main.rs:458-529](</Users/ember/dev/breadstuffs/deos-hermes/src/main.rs:458>)). `deos-hermes` has `default = []`; `js-agent` and `node-brain` are opt-in
([Cargo.toml:203-229](</Users/ember/dev/breadstuffs/deos-hermes/Cargo.toml:203>)).

Consequently, a source-level default MCP `tools/call run_js` is either unavailable
without `js-agent`, or runs `RunJsTool::run_on`, which mints the agent's own private
embedded `Applet` ([mcp_server.rs:309-384](</Users/ember/dev/breadstuffs/deos-hermes/src/mcp_server.rs:309>), [run_js.rs:231-285](</Users/ember/dev/breadstuffs/deos-hermes/src/run_js.rs:231>)). It has a real embedded receipt, but no shared cockpit resource effect.

An MCP `tools/call terminal` has a distinct concrete path: after gateway
admission it calls `run_command_in_confined_pd` ([mcp_server.rs:489](</Users/ember/dev/breadstuffs/deos-hermes/src/mcp_server.rs:489>)). **The shell follow-up read the function body:** on Unix its `_command` parameter is unused; it runs fixed sandbox probes and an Endpoint acknowledgment, not the submitted shell command ([mcp_server.rs:603](</Users/ember/dev/breadstuffs/deos-hermes/src/mcp_server.rs:603>)). The returned text nevertheless says the command ran. Its receipt/probe verdict therefore must not be treated as evidence of requested command execution. The cockpit PTY is a separate path. No external Hermes/MCP session was run in this review.

## 5. The live-World MCP bridge is implemented but must be explicitly composed

`McpToolHost::with_world_bridge(path)` makes `run_js` use a `SocketWorldSink`; absent
or dead socket refuses rather than falling back to the private applet
([mcp_server.rs:386-472](</Users/ember/dev/breadstuffs/deos-hermes/src/mcp_server.rs:386>)). The sink sends `FireEffects`; the cockpit-side `WorldSinkAdapter` turns that into
`World::commit_turn` ([world_bridge.rs:351-408](</Users/ember/dev/breadstuffs/deos-hermes/src/world_bridge.rs:351>), [agent_attach.rs:77-96](</Users/ember/dev/breadstuffs/starbridge-v2/src/agent_attach.rs:77>)). This means commit identity can be the cockpit World even though object identity cannot cross the subprocess boundary.

The cockpit binds/pumps that server only under `starbridge-v2/agent-js` and only when
`DEOS_WORLD_BRIDGE_SOCKET` is set ([construct.rs:306-335](</Users/ember/dev/breadstuffs/starbridge-v2/src/cockpit/construct.rs:306>), [live.rs:56-89](</Users/ember/dev/breadstuffs/starbridge-v2/src/cockpit/live.rs:56>)). The MCP binary's missing `with_world_bridge` composition above is therefore a present integration gap, not evidence that the ordinary external MCP call reaches the cockpit.

The bridge's read side sends copies of all cells and rebuilds a local `Ledger` for the
crawl ([world_bridge.rs:31-40](</Users/ember/dev/breadstuffs/deos-hermes/src/world_bridge.rs:31>), [world_bridge.rs:332-348](</Users/ember/dev/breadstuffs/deos-hermes/src/world_bridge.rs:332>)); it is a snapshot, not shared `Rc<RefCell<World>>` identity. Its write side targets the
served World.

## 6. The Hermes “effect witness” rail must not be mistaken for resource mutation

For ordinary ACP gateway tools such as `write_file`/`web_search`, `tool_effects`
adds an `EmitEvent` digest to the admission turn. The file write remains a syscall in
Hermes rather than a dregg cell effect ([tool_effects.rs:15-28](</Users/ember/dev/breadstuffs/deos-hermes/src/tool_effects.rs:15>), [tool_effects.rs:69-133](</Users/ember/dev/breadstuffs/deos-hermes/src/tool_effects.rs:69>)). This rail encodes authorized intent; it does not persist a file, URL response, or card.

The live-brain render bake names a related separation: even when it registers MCP,
it asks Hermes to *emit* JS and subsequently calls `run_attached_on` locally over a
shared `WorldSinkAdapter`, because MCP `run_js` arguments do not round-trip through
that ACP permission seam ([starbridge main.rs:6392-6416](</Users/ember/dev/breadstuffs/starbridge-v2/src/main.rs:6392>), [starbridge main.rs:6460-6478](</Users/ember/dev/breadstuffs/starbridge-v2/src/main.rs:6460>)). This is an in-process host execution of model-selected text, not proof that the MCP call itself crossed into the World.

## Evidence status and open questions

* **Test source only.** `deos-js/tests/card_editor.rs` asserts the embedded editor
  sequence, including remint portability ([card_editor.rs:71-253](</Users/ember/dev/breadstuffs/deos-js/tests/card_editor.rs:71>)). `deos-hermes/tests/world_bridge_e2e.rs` contains a feature-gated full MCP-bridge
  test using a synthetic `ServedWorld`, not a live Cockpit
  ([world_bridge_e2e.rs:316-356](</Users/ember/dev/breadstuffs/deos-hermes/tests/world_bridge_e2e.rs:316>)). I observed no execution result.
* **Question 1:** What persistent resource should own a card’s amended manifest and
  view-document after `ModeCardSurface::edit_view`—the focused World cell, a distinct
  card cell on that World, or an explicit export/reimport object?
* **Question 2:** Should the launched MCP server accept/configure the same bridge
  socket as the cockpit, and what authenticated process/session binding should own
  that bridge? Present source has a capable bridge and an uncomposed server startup.
