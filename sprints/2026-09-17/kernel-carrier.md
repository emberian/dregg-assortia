# Kernel carrier and first core implementation bundle

2026-09-17. Astra source investigation for the autonomous sprint. No code edits,
builds, runtime executions, git operations, or remote operations were performed.
All paths below are relative to `/Users/ember/dev/minidregg` unless marked otherwise.

## Recommendation

Use **first-order operation data admitted by an installed, committed `Pred`
policy**, then the existing **`AcceptedCellEffect` / complete request binding →
`TypedCellHyperedge` or `MultiCellHyperedge` → payload-bearing `DataIntent`** as
the authoritative semantic path. A programmable shell constructs and composes
the operation data. This is already a meaningful kernel programming model:
friends can install rules, write and remix callers, delegate authority, and
change resources under those rules. A new imperative kernel language is not a
prerequisite silently added to ember's “at some level” requirement.

This selects minidregg's accepted semantic direction, not a claim that a running
receiving node currently completes it. Adopting minidregg as the September 26
receiving runtime remains the sprint recommendation to the root, not an earlier
user decision. Breadstuffs clients may become compatibility clients of this
path; they must not retain another authority interpreter.

The decisive prior choices are accepted D-0002 and the Rust-native authority
decision, both 2026-08-09:

- `docs/decisions/D-0002-canonical-hyperedge-kernel.md`: canonical typed effects,
  flat hyperedges, complete request binding, same canonical pre-state, one patch,
  explicit physical settlement.
- `docs/decisions/2026-08-09-rust-native-authority.md`: Lean owns meaning and
  admission; native code returns candidate bytes/error, not acceptance.
- `ATLAS.md`: widen the source/compiler; replace the old consumer; no parallel
  executor or hand-authored AIR. The new user instruction to repair the whole
  critical path reinforces this existing rule.

## The first implementable core change

**Repair the current declared-action safety claim in its consumers, rather than
starting with a codec-only change or another abstract interface.**

`Theory/DeclaredActionLowering.lean:44–71` permits `.create` and `.write` at any
`StateKey`, including account balances and another resource's object/program
coordinates. `Declaration target` does not index its actions by that target.
The only additional requirements in `ValidAt` / `Accepted` are exact root and
ordered guard/post equality (`:418–470`). `Action.postings` emits entries only
for `.move` (`:100–112`). `Kernel/DeclaredActionExecution.lean:70–76` then declares
conservation by summing those postings. Thus a direct account-balance write has
zero declared postings while changing the actual balance field. The mixed
positive witness at `Kernel/DeclaredActionExecution.lean:279–326` even creates
and writes object 700 while authorizing a batch against an account target.

This is an admitted-model mismatch. It is not a demonstrated network exploit.
The proof-integrity lane independently confirmed it. No consuming canonical
policy adapter was found that adds target/footprint or real-state conservation
to this action path. A hypothetical restrictive policy is not a repair of the
kernel's advertised law.

### Smallest coherent repair in the existing path

1. Add a decidable, source-owned scoped-action discipline to
   `Theory/DeclaredActionLowering.lean`, or replace `Action` with the equivalent
   target-indexed constructors. Object writes name the authorized object;
   program writes name the authorized program. Raw create/write must not mutate
   account balances. A move must be authorized against its debited source.
   Do not retain mixed-authority batches by declaring one target to own them
   implicitly: construct multiple admitted incidences instead.
2. Strengthen accepted action semantics with a proved connection between actual
   account-balance changes and ordered postings. A useful exact statement is:

   ```lean
   -- Proposed statement, not an existing declaration.
   accepted_post_balance (accepted : Accepted ... pre declaration)
       (account : ResourceId .account) (asset : Digest) :
     balance accepted.cellEffect.prepared.post.logical account asset -
       balance pre.logical account asset =
         postingDelta declaration.postings account asset
   ```

   The finite-total theorem follows from this and endpoint coverage; proving
   merely that the list of postings sums to zero is insufficient. Alias cases
   such as source = destination, repeated writes, absent versus stored zero,
   stale expectations, and changed resource IDs must remain in scope.
3. Consume the discipline in `Compiler/DeclaredActionBytes.compile`, so invalid
   raw bytes cannot construct a `Compiled` object. Consume it in `ValidAt` and
   in a computable admission function that uses the actual `CellState.validate`
   result rather than `Classical.choice` of an existence theorem. Then make
   `Kernel/DeclaredActionExecution.resourceLaw` read actual accepted pre/post
   changes; its proof follows from the preceding theorem.
4. Update `Compiler/DeclaredActionAir` so the same scoped admission conditions
   enter its source relation and reflection theorem. Do not leave an old
   guard-only emitted relation beside a strengthened executor. Update its
   generated witness construction and the page adapter
   `Compiler/DeclaredEffectPageMaterializer.AcceptedDelta` accordingly.
5. Replace the invalid mixed witness with actual multi-incidence composition.
   Keep hostile witnesses for the old raw balance-write and wrong-target cases,
   and prove that bytes cannot reach `typedCommit` / durable intent for them.

This is a bounded first wave with existing consumers, not a claim that those
consumers are already a user-facing node. It repairs real core semantics now;
the following receiver bundle is what makes it a release pathway.

### Do not create a second money kernel while repairing it

`Theory/CanonicalResourceKernel.lean` already has the stronger implementation:
`Operation` (`:123`) uses natural amounts; `Admission` (`:205`) requires present
endpoints and solvency except explicit issuer-well mint, plus lease freshness;
`Operation.apply` (`:165`) derives the actual book; `Accepted.conserves` (`:350`)
is about that installed book. `Kernel/CanonicalResourceEffect.bookDelta`
(`:341`) and `typedResourceLaw` (`:348`) derive the delta from accepted post
minus canonical pre. The accepted typed family and multi-cell adapter exist.

The sprint receiving service should dispatch monetary actions to that family
and migrate the raw legacy account-field consumer out. The first repair above
is useful while this cutover is in progress; leaving two authoritative money
interpreters at sprint completion would violate the repository's own design.
The book's current materializer (`Theory/CanonicalResourceKernel.lean:266`) is
still a countability/unary existence witness, so giving this family a practical
codec and materializer is required receiving work, not optional polish.

## What is programmable now, and what is not the same thing

| Existing object | Actual meaning | Required receiving work |
|---|---|---|
| `CanonicalPolicyAdmission.PolicyRecord` (`:36`) | First-order `Pred` transition rule, policy ID/version/domain/semantics/previous link | Computable canonical codec, authenticated installed record, current authority/policy selection, exact projection of admitted pre/post state |
| `DeclaredActionLowering.Action` (`:44`) | Ordered effect data, including computed arithmetic for moves | Scope/conservation repair above; byte/controller/durable consumer |
| `CanonicalResourceKernel.Operation` (`:123`) | Effect-producing resource computation with actual-book conservation | Practical book/operation codecs; computable admission; endpoint and durable consumer |
| `Theory.IndexedProgram.Program` (`:51`) | Typed free-program semantic foundation with dependent continuation functions | Not itself the serialized installed language. Reification is needed before arbitrary programs of this type cross bytes |
| `Effects.EffectSpec` (`:84`) | Generic sequential derivation theorem; first instance uses `Kernel.move` | Its own residual names the open registry/weld/frame/witness work. A shared syntax theorem is not a deployed registry |
| `Theory.EvmFragment` + Stage-0 native work 9103 | Real restricted bytecode semantics; concrete native path proves fixed 256-bit add | Not an arbitrary user-uploaded program/effect producer |

`StateKey.programCode` is an integer-valued key. Selecting request verb
`.installProgram` from resource kind does not add an evaluator of that integer.
Use the real `PolicyRecord.predicate` for rule authoring instead of presenting
this field as a VM.

`Pred.eval` checks a candidate old/new pair; it does not compute a new pair.
Shell programs may compute proposals and submit typed operations. If ember
wants installed entry functions to compute their own effects inside the kernel,
extend the first-order source vocabulary and compile that same source through
the existing fold machinery. Do not embed host callbacks or pretend that
`Pred` already has this role. This additional language choice need not block
the first authored-policy + shell milestone.

## Executable receiver bundle after the first repair

The following is a concrete implementation proposal, not existing code:

1. **Versioned wire and installed rule payload.** Extend existing lawful prefix
   codecs for the selected family declarations and complete typed request;
   install `PolicyRecord` bytes and canonical digest in the credential-policy
   registry. Reuse the existing cSHAKE framing machinery. Policy replacement is
   an authorized operation checked against the old policy and exact current
   authority epoch, then journaled with its registry root change.
2. **One Lean receiving controller.** Decode bounded canonical input, resolve
   the family and schema from authenticated generated catalog data, reopen exact
   current cells, derive the common request, verify the presentation, select the
   exact installed policy, compute the family patch, and construct the complete
   bound accepted effect. It may accept opaque native work bytes only through
   the Lean-selected checker. Refusal returns no new state.
3. **One shared canonical-state projection.** Build policy's `oldState/newState`
   from actual materialized pre and the single validated candidate post. Do not
   accept independent client-supplied policy states merely because configurable
   digest functions say they match. Retain exact argument binding from
   `Theory/AcceptedCellEffectRequestBinding.Bound` (`:111`).
4. **Payload-bearing settlement.** Generalize the existing
   `Assurance/HyperdocumentGuardedDurable.PublicationPlan` pattern. It retains
   exact content/event post bytes, the authority read guard, nullifiers, charge,
   and stable replay envelope. Use `Kernel/DurableDataIntent.DataIntent` (`:99`),
   not a new roots-only journal. The shared physical receiver must install all
   chosen family writes atomically and retain retry identity.
5. **Actual caller and recovery.** CLI and agent clients submit the same request
   bytes. Test rule installation, valid invocation, forbidden invocation, stale
   rule/authority epoch, response loss, restart, identical retry, and reopened
   state with an unchanged receipt identity. This is the first release-path
   completion criterion. The existing fixed forward-link fixtures do not
   establish this dynamic consumer.

Candidate ownership boundaries are `Compiler/CanonicalPolicyAdmission.lean`
and a practical policy codec module; `Theory/DeclaredActionLowering.lean` /
`Compiler/DeclaredActionBytes.lean` /
`Compiler/DeclaredActionAir.lean` /
`Kernel/DeclaredActionExecution.lean` for the safety repair; and a generated
family controller plus generic guarded-durable adapter for the receiver.
The exact names of new files should be assigned by the root. `Compiler.lean`,
prover library/Cargo files, and V2 artifacts contain foreign WIP; no ownership
of those is assumed here.

## Authority projection: existing machinery, real integration obligation

`Kernel/DeclaredActionExecution.projection` (`:37`) is literally
`project := fun _ => authState`. It cannot become the deployment proof that
authority is read from the action pre-state. Its current integer effect schema
does not contain the typed credential records necessary to implement that
projection.

The reusable source is `Theory/CredentialAuthorityState.authState` (`:150`):
capabilities, revocation, policy addresses and epochs, and key epochs come from
one canonical authority cell. `Kernel/CanonicalPolicyRegistry.guardPolicyRegistry`
(`:299`) retains that exact registry root in durable read guards.
`Assurance/HyperdocumentGuardedDurable.PublicationPlan` (`:78`), its
`toDataIntent` (`:119`) and `intent_readGuards` theorem (`:156`) already connect
a separately canonical authority pre-cell to a multi-cell publication.

Generalize this existing guarded canonical snapshot pattern for the receiver;
do not manufacture a correct projection for the all-Int legacy schema. A
separate canonical read-only authority cell is fine when its exact root is
part of the accepted dependency and atomic preflight/replay identity. Merely
closing over an ambient `AuthState` is not. A later fully generic multi-cell
API should retain these read dependencies explicitly rather than rediscovering
them independently per adapter.

The executable authorization checker already exists:
`Theory/AuthorizationDeclaration.verify` (`:538`) and
`verify_accepted_authorized` (`:693`). The latter exposes `Nonempty Authorized`;
the receiving constructor should retain/reconstruct actual presentation data
computably instead of choosing a token through `Classical.choice`.
`Compiler/CanonicalPolicyAdmission.admit` (`:237`) already performs the policy
portion, but starts from existing `Evidence` and exact epoch proof. It is not
by itself a raw credential-byte endpoint.

## Practical codecs can start now

No application-genre or economic decision blocks these changes:

- `Compiler/Tower256ConcreteBackend.StreamCodec` has logarithmic base-255
  naturals, sums, products, options and lists (`:38–227`).
- `Compiler/TypedAuthorizationRequestCodec.lean` already encodes the complete
  object request compositionally. Extend kind-indexed verbs/requests instead of
  inventing another envelope.
- Replace `DeclaredActionLowering.declarationCodec` (`:277`) and
  `CanonicalResourceEffect.operationCodec` / `postingCodec` (`:106`, `:137`)
  unary codes. Replace `CredentialAuthorityPolicyRegistry.policyRecordCodec`
  (`:77`) using `Encodable.ofCountable` with an explicit recursive tag grammar.
- A shared codec foundation should live below `Theory` if Theory consumes it;
  do not import candidate compiler modules into Theory. Move/generalize the
  existing combinators rather than copy them.
- Strengthen wire admission beyond `decode_encode`: `StreamCodec.toLawful`
  only checks trailing input consumption, and existing bool/tag mappings accept
  aliases. Require canonical re-encoding equality or strict parsers, bounded
  byte/AST/list depth, and reject unknown tags/versions/trailing bytes.
- For finite maps/sets, choose stable sorted finite encodings with proven
  duplicate rejection and support correspondence. This is a representation
  decision, not an invitation to replace dependent maps with an unrelated state.

Codec changes must advance their version/pins and update actual generated
consumers in the same wave. A codec green alone is not evidence of a runtime.

## Compiler/proof boundary that must remain in the implementation plan

`Compiler/PredCompile.supported` (`:370`) currently rejects `le` and `monotone`.
Implement the needed range/order lowering and witnesses; do not advertise all
existing `Pred` constructors as compiled. `witnessed` is supported only with
first-party fail-closed meaning; no arbitrary external discharge follows.
Field-cast injectivity is a named premise today and must become actual bounded
limb/range checks on deployed representations.

`Compiler/DeclaredActionAir.descriptor_accepts_iff_run` (`:412`) is a useful
guard-fold reflection theorem over a descriptor specialized to `fields`.
`pinSystem` pins the generated expected/observed reads, and `CodesBounded` is an
external premise. It is not yet an installed generic program STARK proving
arbitrary state openings under the public pre-root. The root/read-opening and
range relations must enter the deployed statement; an untrusted author may not
choose a per-state descriptor and thereby choose what is trusted.

`Compiler/NativeKernelPlan` and `Compiler/DescriptorEval` supply actual Lean
descriptor checking and candidate filling; `EvmStage0NativeDeployment` provides
a concrete generated native example, work 9103. Reuse that byte/error-checker
shape and authenticated work catalog. Do not reintroduce a Rust semantic
interpreter or protocol verifier.

The old `Compiler/DeclaredHyperedgeArtifact` is consumed by
`Assurance/DeclaredHyperedgeHistoryBinding` and `BinaryTowerHeaderCodec`, while
the typed kernel is used by Grain/reactive/hyperdocument families. Scoped
search found no declared-action native endpoint. The old joint artifact is
therefore a remaining compiler/history consumer cutover, not proof that the
typed receiving path already exists.

## Checks and completion gates

- General preservation and actual-post binding theorems, not case tests alone.
- Built positive witness and hostile witnesses for raw balance mutation,
  authority-target substitution, changed program bytes, stale version/epoch,
  reused nonce, omitted incidence, and malformed/noncanonical wire.
- Exact generated-artifact/embedded-byte agreement, authenticated family/work
  IDs, and old consumer removal; caller reachability before “complete.”
- Narrow Lean file builds and import-boundary gate during implementation; root
  schedules umbrella `lake build Minidregg` only after shared interfaces settle.
- Filtered native lifecycle tests for the selected receiver; no broad crate
  suite for an orientation/codec patch.
- Actual two-user shell/agent invocation, refusal, durable restart/retry and
  readback. Physical transaction/crash evidence and proof-system security
  claims remain separate gates, each completed where the release depends on it.

There is no blocking ember product question for the first scoped-action repair,
computable admission, strict codecs, or same-state authority binding. Receiving
runtime selection and the exact initial installed policy/operation set are root
integration decisions to make explicitly. New effect-producing kernel language,
money/cluster choices, and broad arbitrary native execution should not be
silently selected by this lane.
