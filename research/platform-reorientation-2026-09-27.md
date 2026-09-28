# Platform reorientation — September 27, 2026

Ember rejected the drift toward a bespoke GitWeb demonstration and requested a new goal followed by code-tree exploration. This is the resulting source/evidence map, not an implementation plan or a declaration of deployment readiness. Root and five bounded Sol investigations inspected Mini, Bread, hosting, programming surfaces and fn. No builds, tests or live mutations were performed for this review. Mini's reviewed committed baseline is `4e5d674`; existing working-tree changes remain separate. Older captured runs retain their own source/image qualifications.

**Current direction:** build the programmable infrastructure in Mini, with application grains as instances. First review this map with Ember; do not automatically resume the fixture construction. Checkpoint 78 remains the preserved live deployment boundary. The new active goal requires independent resource/application instances without platform source edits, hand-assigned fixture identities or bespoke orchestration scripts.

## What exists, and where it stops

### 1. A real programmable resource kernel and native client

`native/resource-client/src/main.rs:141–173,1018–1088` exposes author, submit, query and retry. The client obtains source-authored signing headers, signs and durably retains the call, and submits it for native admission. `Host/Json.lean:2073–2155` accepts supported typed birth, policy-install, delegation, revocation, content, resource/joint and grain intents.

Birth is not merely inserting an operator-supplied row: `Host/ApplicationCurrentBirthAuthoring.lean` derives current epochs against the pinned runtime; `Kernel/ResourceBirthPolicyController.lean` checks current factory policy, funding, schemas and credentials; `Kernel/ResourceBirthController.lean` derives allocation, Book transfer and final cell laws. `Kernel/DeclaredResourceController.lean` joins targets into a real multi-cell transaction. Native replay consumes birth and policy installation in `Kernel/NativeHostReplay.lean:1647–1659`.

There is executed evidence beyond source: [native workroom members](../../minidregg/docs/evidence/2026-09-26-workroom-native-members/README.md) records two subjects, content creation/edits, delegation, stale-root refusal and revocation. [Application birth](../../minidregg/docs/evidence/2026-09-27-application-birth/README.md) records typed application/session creation and delegated observation on a separate Store.

This materially advances the [September 17 programming audit](minidregg-programming.md), whose missing practical authoring/receiving paths must not be repeated as current absences.

**Identity-allocation follow-up:** the kernel's checked allocator admits caller-selected identities; it does not choose globally fresh IDs for a new participant (`Theory/ResourceBirth.lean:39–47`, `Kernel/ResourceBirthController.lean:40–61`). Hosted controllers choose `configured range start + journal ordinal` for targets and owner/control grants (`native/grain-runtime/src/resource_tools.rs:327–349`). Application/session families reserve corresponding ranges for every member of the bundle (`application_tools.rs:30–107`). Configuration checks compare ranges against other families and known peer IDs, not other independently configured controllers. Kernel admission still prevents a colliding creation from overwriting an existing resource. Before dispatch, the controller persists its advanced ordinal and a no-submit operation marker (`main.rs:10080–10111`); its journal separately checks duplicate names, targets and grants (`:1658–1700`). These are meaningful local allocation/recovery mechanisms, but do not establish general participant namespace provisioning. “Kernel-derived allocation” above means checked materialization and authority/accounting effects, not automatic selection of every identity.

### 2. Several meanings of programmability, with different boundaries

* **Rules as data:** `Pred/Core.lean` provides predicate trees over state slots. `Kernel/PolicyInstallController.lean:194–231` accepts supported replacements under current authority. Existing rules may deliberately prevent future management. Compiler support and the runtime profile constrain the accepted fragment.
* **Effects as data:** `Theory/DeclaredActionLowering.lean` and `Kernel/DeclaredResourceScalar.lean` accept ordered guarded create/write/move actions. Content operations have their own canonical action grammar. Users choose operations and arguments without rebuilding the host.
* **General computation:** the above does not establish an uploaded-code executor. `programCode` is integer-valued state; the standard birth JSON does not expose `declaredProgram` storage. `Theory/IndexedProgram.lean` is a dependent program/handler foundation, not by itself a serialized external programming service. The older audit also identified an EVM-fragment interpreter and a specialized native arithmetic consumer; this review did not requalify those paths as a general executable application runtime.
* **Hosted software:** SPK execution is a separate physical hosting mechanism. Its program identity, installation and authority must be connected to the resource world. Editing Git content does not itself install executable software.

Thus “the kernel isn't programmable” is wrong; “friends can program the whole platform through the current Hermes catalog” is also wrong.

### 3. Hosted Hermes exposes a much narrower interface

`native/grain-runtime/src/mcp.rs:264–325` exposes status, signed reads and bounded publication, with optional birth/application/session families and application routes from configuration. `resource_tools.rs:21–45,260–278` fixes each family's factory, payer, policy and ID range; the model selects a family rather than defining the entire contract.

This family mechanism has actually executed: [hosted birth 9301](../../minidregg/docs/evidence/2026-09-27-hosted-birth-9301/README.md) records unforked Hermes creating, reading and publishing a note using a deterministic provider. Its restart defect remains explicitly recorded; a copied-Store repair is not a repaired live journey. The earlier [two-account Hermes run](../../minidregg/docs/evidence/2026-09-26-cross-uid-hermes/README.md) records independent reads and three publications.

The later Bonsai A/B review configurations expose only status/read/publish, with no configured birth families or application routes ([catalog evidence](../../minidregg/docs/evidence/2026-09-27-hermes-mcp-readiness/README.md)). Do not describe optional source features as available in that deployment. The SSH entrance accepts Hermes/status/conversation/disconnect commands; it is not yet a general DREGG shell.

**Follow-up: discovery is partial, not absent.** `native/grain-runtime/src/main.rs:12093–12175` builds the MCP application catalog from verified retained application-birth records and configured shared references, filtered through allowed session families. `shared_app_refs.rs:1–9,121–152,392–482` separates a name/historical receipt pointer from authority: resolving a shared reference checks historical birth/issue receipts and performs separately authorized current reads of app, manifest, snapshot and ticket. Those separate reads do not establish a single-image relationship; source admission must still check that join. This is existing reusable discovery machinery, although shared entries remain operator-pinned and the catalog is controller-local and application-specific. Do not replace it with another unrelated catalog.

The native observation protocol itself selects an already known `(kind, target, capability)` and one of resource/policy/capability views (`Compiler/NativeObservationCodec.lean:18–46`). It does not enumerate all readable resources. Its public challenge is not a read grant (`Kernel/NativeObservationController.lean:365–405`). The authority catalogue enumerates physical authority shards (`Compiler/CredentialAuthorityDomain.lean`), not a user-facing resource directory. Application interface descriptors already bind interface identity/version/kind and permission schema (`Kernel/ApplicationDispatchManifest.lean:29–82`); they are not a generic method signature catalog. These distinct meanings of catalogue/interface must remain separate when designing the common surface.

### 4. Reusable hosting mechanisms, manually assembled instances

`native/spk-host/src/main.rs:31–80` has install, resident and custody entrypoints. `install_v3.rs:271–370` obtains source-qualified lifecycle receipts. `resident_service.rs:834–1033,1242–1310` verifies the signed package/volume/custody and serves human and agent entrances through one resident. `deploy/spk-host/spk-var-volume` is parameterized volume machinery. Source lifecycle identity and volume derivation are parameterized too.

The assembly boundary is concrete: `scripts/spk-platform/prepare-install-config.sh:351–389` and `prepare-resident-config.sh:43–73,222–290` encode the fixture's application, identities, sessions, keys and routes. `journey.sh` manually sequences installation, physical adoption and resident configuration. The Rust configuration structures are more general than these scripts. However, `native/grain-runtime/src/application_api_tools.rs:170–180` itself still requires `/repo.git/`, so not every app-specific restriction is confined to fixtures.

Our surveyed entrypoints did not reveal a general controller that takes accepted allocations and reconciles host placement, custody, lifecycle and route registration. This is a scoped inference, not a claim that every file was exhausted. Restart also needs substantive work: `resident_service.rs:599–708` can inspect prior START state but refuses reuse without fd3 reattachment and requires source STOP.

[INSTALL](../../minidregg/docs/evidence/2026-09-27-spk-v3-install-consumer/README.md), [mixed entrances](../../minidregg/docs/evidence/2026-09-27-spk-resident-mixed-route/README.md) and [lifetime recovery](../../minidregg/docs/evidence/2026-09-27-lifetime-controller-recovery/README.md) evidence establish bounded components. They do not establish a completed same-Store shared service. The preserved r3 deployment has physical package materialization but refused INSTALL completion, not a running shared GitWeb grain.

### 5. fn publication is meaningful; discovery remains incomplete

`Theory/Hyperdocument.lean` has typed document/atom/version identities, links and disclosure-bound transclusion references. `Theory/HyperdocumentInterface.lean:4–22` explicitly leaves authenticated history resolution to another layer; these types are not a served federated resolver.

Mini's selective release path is substantial: current signed observation selects actual source bytes (`Host/FnSelectiveReleaseAuthoring.lean`), event14 checks source publication authority, and event13 independently checks recipient policy and atomically stores content/nullifier. This is different from the older FnEvidence export containing the complete accepted source prefix. Neither should be advertised as the other's privacy or proof guarantee.

Fn carries articles and supplies scoped consumer progress. It does not supply Mini authority, and ACK does not prove resource validity or remote completeness. `scripts/gitweb-content-export` and `scripts/fn-gitweb-preview/join.sh` currently compose the selected-version path as fixtures. A general authenticated name/version discovery and opening interface remains unestablished in the inspected consumers.

### 6. Bread contains useful interface precedents, not one ready-made replacement

* `app-framework/src/invoke.rs:51–129` resolves typed methods against cell interfaces and produces signed ordinary effects; `deos_app.rs` composes capability-gated affordances and mounted HTTP invocation. Nameservice is a consumer.
* `deos-js-runtime/src/world.rs` exposes cell-world method discovery and invocation. `deos-hermes/src/world_bridge.rs` connects submitted JS to a served World over framed socket RPC; `starbridge-v2/src/agent_attach.rs` is a consumer. This provides a concrete scripting/discovery precedent. It is distinct from the hosted Nous Hermes process and does not establish JS execution proofs.
* `agent-platform` implements rented sessions and role-gated operations. `dreggnet-offerings/src/host.rs` hosts heterogeneous Rust offerings with open/advance/resume. These are not arbitrary uploaded SPK deployment services.
* `starbridge-v2` has an app registry and desktop shelf, but the starter app set is hardcoded. Several naming systems exist; they are not one qualified universal namespace.
* `sandstorm-package` verifies/extracts SPKs; that alone does not host them. The bridge labels some mappings as stand-ins.

Bread also contains an older Python hosted-Hermes controller, separate from its Rust platform. Its presence does not change Ember's explicit rejection of a new Python implementation. Use existing behavioral lessons without silently promoting it into the chosen architecture.

## Consequences to discuss before implementation

We have advanced core functionality while leaving the human/agent operating surface and physical orchestration fragmented. Calling all progress fixture work would erase real gains. Continuing to complete fixture steps without consuming these mechanisms through common interfaces would repeat the failure identified in Mini's own `ATLAS.md`.

The next design needs to answer three connected questions:

1. How does an authorized person or agent discover, inspect, author and compose operations on resources through one coherent client surface?
2. How does accepted resource/application intent become durable hosting, recoverable custody and accessible sessions without hand-written per-instance configuration?
3. How do named resources and selected versions cross nodes through semi-untrusted fn while preserving explicit authority and disclosure?

These are not requests to invent three new frameworks. Existing client/admission, resident/lifecycle, typed reference and release mechanisms should receive real consumers. The precise implementation scope remains for the evidence review with Ember.

Clutch/payment/provider economics, compiler/prover completeness, and the full distributed convergence substrate were not re-audited here. Their earlier research records remain navigation, not newly verified claims. Preserve frozen WIP and the live checkpoint; no further GitWeb-only implementation was authorized by this orientation step.
