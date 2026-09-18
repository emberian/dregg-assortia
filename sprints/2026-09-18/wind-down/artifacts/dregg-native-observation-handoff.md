# Native observation boundary — wind-down handoff (2026-09-18)

**SOURCE DRAFT ONLY. Never compiled or executed.** User requested wind-down
before a compiler seat became available. No test result or executable-security
claim attaches to this new module. Foundation migration is separately GREEN in
`/tmp/dregg-resume-foundations-checkpoint.json`; do not conflate them.

Owned source: `Kernel/NativeObservationController.lean`.
Exact digest/line count: `/tmp/dregg-native-observation-source-checkpoint.json`.
No Git operations performed by this subagent.

## Concrete finding and agreed contract

Unsigned birth preparation calls lower Book admission before native signatures,
source capabilities and upper FeeBound/FundingBound checks. Varying arbitrary
fee/funding amounts could distinguish another account's solvency. Fresh submit
also prepared before signature verification and returned detailed failures.
Host lane closed unsigned prepare and sanitized every fresh submit refusal;
blind mutation remains permitted, and read rights are never inferred from
mutate/delegate/install or ownership. Resources may intentionally lock their
own management. There is no owner recovery bypass.

Root explicitly classifies domain/profile/federation, commitments (including
resource roots), height, policy generation/revision, complete selected public
KeyRecord, logical IDs and allocation/occupancy/routing metadata as public.
Existing registryDigest is reversible base257 byte binding, NOT hiding. No
private key appears. Resource contents, balances and private history remain
protected. Timing noninterference is not claimed.

## Source API

The host lane owns `Compiler/NativeObservationCodec.lean` and the only
`NativeHostCodec.imageBoundary`. It exports strict codecs for:

- GrantRef { kind, target, capability }
- QueryView = resource | policy | capability (the exact observing grant only)
- Query { kind, target, view }
- Purpose = query Query | prepare NativeHostCodec.Draft
- Intent { subject, nonce, purpose, grants }
- Challenge { intent, domain, semantics, federation, imageBoundary, height, headers }
- Signed { challenge, signatures }
- intentIdentity: one source-owned cSHAKE commitment of canonical intent bytes

The new controller imports that codec, never NativeHost (avoids a cycle).

`Context (deployment) (durable)` contains LoadedDirectory durable and the
complete Loaded authority anchored to that SAME durable.snapshot.

`challenge context profile federation genesisHeight intent : Except String Challenge`
returns only existing exact SignedHeader bytes and approved public metadata.
Every unauthenticated error is exactly `observation refused`.

`authorize native context profile federation genesisHeight signed :
 IO (Except String (AuthorizedIntent context profile federation genesisHeight
 signed.challenge.intent))`

AuthorizedIntent has a private constructor and retains the suppliedChallenge,
source-derived challenge equality, exact source read-footprint check, and one
CheckedGrant per listed grant. Each CheckedGrant retains Selected source page,
actual private native signature receipt, actual Authorized token, and literal
result of authorizeSelected. No host-selected verifier or positive bool mints
read authority. Reusing a signed challenge on a changed image uniformly fails.
This is one exact loaded snapshot read; no write/CAS occurs.

The host must construct the Context from its Opened value, authorize, and only
then call internal prepareLoaded on the SAME Opened and exact intent draft.
It must not reload/rebase between checking and private preparation. Submit's
uniform-refusal path stays independent and does not acquire observe requirements.

`AuthorizedIntent.queryResult : Option (List UInt8)` emits only the selected
view after complete authorization. `.resource` uses `resourceViewCodec`:
frame DREGG/NATIVE-HOST/RESOURCE-VIEW/v1 then (PackedCell.bytes of exact selected
resource, List (assetNat, exactInt) for selected account only). `.policy` uses
PolicyRecordCodec.encode for current selected source. `.capability` uses
storedCapabilityStream for the exact observing grant including its lineage;
there is no arbitrary other-cap ID query.

## Read footprint and source binding

- query: exactly the named typed target.
- invoke: command target, same subject.
- install: actual target kind from source-owned role metadata; ordinary observe
  grant separate from program-shaped installPolicy control.
- delegate: typed target and observation capability ID MUST equal parentId;
  this proves actual parent use and prevents probing someone else's lineage
  through an unrelated target observe grant. Delegate-only remains blind-submit.
- birth: factory object plus every distinct existing debit account from ALL
  descriptor.resourceBatch operations (including invalid fee/funding drafts).
  Existing Book.accounts is public namespace metadata. A proposed registration
  cannot hide an existing debit source. Accounts absent from that namespace
  have zero balances once the admission lane's AccountSupported invariant is
  enforced. Newborn intermediate funds derive from zero and client-authored
  ordered postings. Recipients need no observation grant just to receive credit.

Exact grant target order must equal source-derived footprint. Grants never
select a different semantic resource or an independently supplied read set.

The policy candidate is a validated EMPTY patch on the ACTUAL selected page;
request.preStateRoot is that page root. Full-image commitment is in source
bindingBytes and effectIdentity, binding the Book dependency too. Same source
builds 17-field observe Request, signingHeader, candidate, projected old/new and
current-policy admission. Generation and revision come from actual authority.
Native signature verification, sourceCapabilityOnlyEvidence, canonicalWitness
and CanonicalPolicyAdmission.admit are reused; no policy evaluator twin.

Policy projection: requestSlots, intent/bytes, resource/bytes (same declared-page
codec as invocation), account/bytes for own sparse account cut, and scalar
account/balance/<asset> entries. Sparse zero means absent, consistently with
Book balances. The account cut is computable DFinsupp.comapDomain' and canonical
asset-sorted entries, never the entire shared Book or authority shard.
Host agreed to add projection pin
DREGG.RUNTIME.OBSERVATION.EXACT-IMAGE-RESOURCE-AND-ACCOUNT-CUT/v1 in the next
coordinated profile refresh; verify it was actually added before deployment.

Draft named lemmas: accountBalanceMap_exact, accountCut_noninterference
(arbitrary other-account balances/account list/leases cannot change this cut),
observation_request_actual_root, observation_preserves_resource,
observation_policy_views_equal, CheckedGrant.current_generation_and_source,
resourceView_roundtrip/canonical, accepted_footprint_exact. NONE checked yet.

## Next coordinated work / owners

1. Host finishes/emits NativeHostCodec and NativeObservationCodec after receiver
   dependencies. Root/authority grants one finite compile seat for this controller.
2. Run only the narrow emit command in the manifest; repair elaboration/proofs
   without weakening capability/policy/native checks. Known untested dependent
   areas: recursive checkGrants Fin.cases, private portal opacity, proof transport
   `same ▸ derived`, candidate post equality. These are untested, not known reds.
3. Account support lane (resume_admission): new Theory/CanonicalResourceBookInvariant
   emitted GREEN, including registrationAdmission_iff_fresh and
   registrationsAdmitted_accounts_only. At last report actual loaded/final
   CanonicalCellRegistry law wiring was still pending. Enforce it before claiming
   registration no longer has hidden-balance diagnostics. Source report:
   `/tmp/dregg-native-prepare-read-footprint.md`.
4. Host (resume_host): wire actual challenge/observe-assemble/authorized prepare
   and query transport, same Opened. Keep all preauthorization failures uniform.
5. Genesis/CLI (resume_genesis): adds explicit factory observe grant per enrollment,
   owner/Bob policy observe branches and child observe+mutate grant. Actual CLI
   driver rewritten for challenge -> external OpenSSL sign -> observe-assemble ->
   prepare SIGNED. That new flow was not executed at this handoff. Add valid own
   account query, Alice probing Bob with wrong cap/subject, stale image challenge,
   wrong parent and missing observation refusals; old blind mutation remains.
6. Pin ordinary axioms for draft lemmas after actual checking; add nonvacuity and
   refusal evidence on the actual public CLI. Refresh semantic profile once
   coordinated; current deployment source policies depend on its exact identity.
7. Root owns named Git checkpoint and umbrella insertion/integration gate later.

No extra global observer privilege, implicit owner repair, new Request schema,
new signature scheme, provider security claim, or timing secrecy was introduced.
