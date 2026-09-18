# Native preparation read boundary (source audit, 2026-09-18)

This is an audit of the actual four `NativeHost.prepareLoaded` branches and
their called controllers, not a claim of compiled noninterference. Source is
being migrated concurrently; references name definitions rather than unstable
line numbers. Private account balances remain private. Root explicitly permits
logical/physical resource and authority page IDs, allocation/occupancy metadata,
commitments, current policy/key counters as public routing/challenge metadata.
That does not classify payloads, whole capability records, or history as public.

## Common validation and returned bytes

`validateLoaded` loads the complete directory and complete authority, checks
every present cell's `CanonicalCellRegistry.CellLaw`, verifies every selected
immutable policy source's identity/revision/runtime semantics, and finds the
factory head. These are trusted consistency reads, not permissions to return
all loaded data. Inconsistent-image diagnostics should not become an
unauthenticated oracle. The returned signing plan includes runtime domain and
semantics, image boundary, height, canonical finalized draft, and native signed
headers. `signingHeader` selects the subject's current key but does not prove
possession of its private key.

One separate concern: `CredentialSignedEnvelopeController.registryDigest` is
base-257 encoding into an unbounded Nat, not a hiding cryptographic commitment.
It encodes the selected key registry projection, including its complete public
KeyRecord (subject/public key/activation and revocation metadata), authority
root and catalogue revision. It contains no private key. Treating this as an
opaque hash while classifying only key ID and epoch public is unsound. This
needs a deliberate metadata classification or a real commitment change.

## Birth

The host calls lower `ResourceBirthController.Concrete.prepareDraft`, which
derives grants/auxiliary creates and invokes `prepareBirth`. It does not first
run upper `ResourceBirthPolicyController.preparePending`. In particular,
FeeBound and FundingBound are later submission checks. Arbitrary requested
amounts/endpoints can therefore reach ordered Book admission during unsigned
preparation. `sourceCapabilities` are only counted after lower preparation;
they are not looked up or authenticated there.

Internal reads: pinned factory role/layout and root; complete Book including
accounts/balances; all relevant capability/policy/key/channel/revocation
metadata in authority; directory permanent-use/tombstone occupancy; immutable
initial source consistency. Lower grant preparation checks global child-cap ID
freshness, marker freshness, issuer and policy generation, ancestry/channel
state and revocation. It then derives exact physical updates.

Private oracle-sensitive logical footprint is every distinct funding posting
source plus the fee payer, across all assets named by those operations. Ordered
solvency checks use the intermediate balance after previous transfers/fees, not
the initial balance repeatedly. Authorization of only creator/first payer is
insufficient. Each existing debit account needs its exact `observeAccount`
authority under its current policy. A policy on account metadata alone must
not accidentally release the whole shared Book.

Public account membership covers source/destination existence. Internal
posting also adds to destination balances, but the current plan contains no
Book post-state or recipient balance. There is no reason to require a grant
over the fee collector merely because the trusted update computes its credit.
Moving input-only FeeBound/FundingBound checks before private evaluation is
useful but does not remove debit-account observation.

Registration currently also checks no balance support at a purported fresh
account, across all assets. The present loaded Book law only requires correct
physical identity and a present Book. The codec intentionally roundtrips
`witnessHiddenBook`, so a nonzero unregistered balance is accepted by that law
and distinguishable by registration. Root assigned a core repair: finite
`Book.AccountSupported` law (every nonzero balance coordinate's account is in
Book.accounts), enforced on loaded/final Books, with preservation through
genesis, registration, all admitted operations and batches. On supported Books,
registration admission is exactly account freshness. Do not exempt hidden
reads simply because a client labels an allocation fresh; use the enforced
invariant. No whole-Book observation permission is needed for this repair.

Finalized auxiliary pages do not include relocated unrelated old records in
the current implementation. `CredentialAuthorityDomain.runEdits` preserves
stable entryGroup/pageNumber routing. `Complete` equates old page numbers with
catalogue refs. `placePages` sends every old-ref page to existing physical
writes, and only missing-ref pages to newly allocated aux cells. Thus a new
authority aux page contains newly inserted descriptor grant/initial-policy/
marker records; initial policy-source aux bytes were supplied by the caller.
Fresh IDs derive from max permanent-use/reserved ID plus one, and number of
new pages reveals old occupancy, both now explicitly public. This conclusion
depends on the actual Complete/routing invariants and is source analysis, not
a newly checked theorem. Existing shard writes, which may contain unrelated
records, must not be added to the returned signing plan.

Factory private inspection should use its explicit `observeObject` grant.
Initially genesis provisioned only factory install-policy control; the host
owner is now adding a separate observe capability. Control never silently
implies observe.

## Invocation

`DeclaredResourceController.prepare` loads the requested target and authority,
checks target layout/role/root/schema, executes each declared write against the
actual old page, derives the final page, checks marker freshness/lowering and
loads the selected immutable source. `Page.applyWrite` compares caller-supplied
expected values with actual sparse fields; detailed guardMismatch, missing vs
present, overflow and invalid-page outcomes reveal private values/layout.
Repeated writes run sequentially. The supplied capability ID is not admitted
by this preparation path. Direct account invocation is currently rejected
with accountRequiresBook.

Require exact target `observeObject` or `observeProgram` before this private
preparation. Internal preserving reads of neighboring fields remain inside
the target's resource boundary. Account balances need the account-specific
Book projection, not generic account metadata or the Book physical cell.

## Delegation

`CapabilityDelegationController.prepare` observes the actual typed target,
reads the exact caller-selected parent capability, its stored lineage and
canonical ancestor suffixes, checks holder/delegation scope/verb/time/budget
shape, current issuer/policy generations, revoked/channel state, child ID and
marker freshness, then lowers authority updates and loads current source.
Unsigned detailed parentUnavailable/descent/lineage/shape errors can probe an
arbitrary parent ID even if the caller can observe the same target.

Require (1) exact target observation under its resource kind and (2) native
authenticated use/possession of the selected parent capability. One parent
grant may supply both if it has the observation verb; a separate target
observer does not establish parent possession. A delegation-only holder may
still submit a fully formed blind mutation with uniform refusal. Current
recipient signature is checked; historical grantor key signatures are not
revalidated. Whole authority shard bytes remain private.

## Policy installation

`PolicyInstallController.prepareChecked` checks authority root, guessed old
head/version/address, successor source version/previous address, new source
domain/runtime support, marker freshness and grouped authority placement.
Current head/counters/addresses are now public challenge metadata. Supplied
control capability is not checked during preparation. New source bytes are
caller input; arbitrary old source content is not thereby public. The lower
install branch itself does not evaluate old policy; common image validation
does load current immutable sources for consistency.

Private diagnostics require the ordinary observe grant for the actual governed
resource kind, followed by installPolicy control for the mutation. Owner
object/account/program grants have their matching observe verb; a separate
program-shaped policy-control grant contains only installPolicy. Do not coerce
an object/account observation into program observation merely because policy
installation is a program request. Control-only actors retain blind submit.

## Candidate-independent gate contract

Decode a strict canonical draft and derive its logical read needs before
private preparation. Bind the observation authorization to caller, domain,
runtime semantics, draft bytes/identity, exact snapshot commitments/current
policy revisions and capability IDs. Authorize no-op observation requests
through the actual native signature/capability/current compiled source gate.
Only then run private preparation and return its plan/diagnostics.

Suggested needs are typed resources `(kind,id)` plus a separate selected-parent
use requirement. Birth derives all debit-account IDs from all funding and fee
postings, deduplicates observer needs but preserves ordered operation semantics,
and adds explicit factory observation as required by its private policy view.
Invocation uses exact target. Delegation uses target plus parent possession.
Install derives governed kind from source-owned role metadata. Registrations
use the enforced Book support law and public account namespace.

Never mint a reusable prepare authorization for a different draft or changed
snapshot. Unauthorized/missing-cap outcomes must be uniform. Fresh submit can
remain blind and uniform-refusal; it need not demand observe authority for
every mutation. Observation output and policy projection must retain logical
resource cuts even when trusted execution loads a shared Book/authority page.
