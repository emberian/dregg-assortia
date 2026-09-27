# Checkpoint 60 — deployed birth profile repaired; native dispatch convergence

September 27, 2026. Continues [checkpoint 59](checkpoint-59.md). The full
[parallel journeys](parallel-journeys.md) remain required; no integrated shared
service or real-model Hermes session is established by this checkpoint.

The f461f39 Host build completed and was qualified in Mini **419ee86**. Its ELF
SHA-256 is `3bbdc8474cca00a3a080f9120acba39ee551ca47d9506573dc37115dc26df55b`.
The linked executable correctly inspects all fifteen canonical signing headers
in the retained failed event22 plan. This supersedes checkpoint59's live-link
status. It does not turn the earlier failed issue into an accepted ticket.

Fresh event22 r3 is running on hbox under user unit
`mini-event22-r3-client-session.service`, invocation
`a74500a1b3a9487a91a253e6d6a86f8b`, private root
`/tank/dregg-build/minidregg-event22-r3-client-session`. It has completed its
app/session setup, reopened receipt lookup and pre-reserve signed query, and
entered tool reserve. No accepted op54 ticket is yet claimed. Client-session
owns this Store; do not restart it because a replay takes minutes.

The separate integrated GitWeb base r2 is terminal, exit1 after 52.07 seconds.
Its matching genesis/profile semantics were rejected by birth authoring, which
reconstructed a partial profile without the configured completion custodian.
Mini **2649f49** fixes the core: supplied deployment coordinates must match,
then authoring uses the entire deployed profile. Both op7/direct authoring and
current-image application/session authoring pass that configuration. The
semantics equality, seed and current-height checks remain. Serial Lean checks
passed through Main, and executable checks passed the eleven existing cases,
ten configured birth routes, ten wrong-custodian refusals, seven configuration
mismatches and the loaded context. See Mini's
`docs/evidence/2026-09-27-birth-runtime-profile/`. A new exact 2649f49 native
Host build is assigned to build-native; source execution is not native retry
success. Keep the failed r2 Store and attempt files intact, and use a fresh
integrated r3 after the successor qualifies.

Reviewed source cuts:

- **fe6002e**, evidence **e6737ff**: operator-private event26 routes 76–81,
  with fresh-CAS permit 76, receipt-only lookup 77, paid plan/assembly 78–79 and
  reserve plan/assembly 80–81. Source plans expose app/session physical roots.
- **d752df7**: client paid custody binds original grant/reserve receipts,
  refreshes the source plan before signing, retains exact ingress and marks
  before its one submit. Lost-reply recovery uses numbered receipt lookups.
  Four focused tests, formatting and strict Clippy passed. Its exact Linux
  client built on Persvati; ELF SHA-256
  `08a1605a804cab92fd262bf82e951e9c2b3c1573d2ba8a593ff97888962d7acf`, at
  `/tmp/minidregg-d752df7-resource-client-build/target/release/mini`.
- **540fbfa**: INSTALL preparation checks an explicitly qualified Host against
  original receipts and unchanged logical Store, permitting reuse when the
  base already uses that binary. The STOP journal hook checks exact running
  identity and volume under lock, persists Fenced before systemd action, and
  audits stop before persisting Stopped. Physical callers remain separate work.
- **e5615b3**: pure SPK lifetime plan/permit comparisons preserve original
  issuance independently of current generations and pre/post-reserve purse
  roots. Root review fixed a 64-versus-32 hexadecimal systemd invocation-ID
  mismatch. Four Linux component tests and strict Clippy passed; this is not
  yet a resident fd3 route.
- **1693c08**: STOP target comparison joins retained source frames and full-width
  receipt fields to the actual journal/volume identity. Two Linux tests and
  strict Clippy passed; physical invocation still requires the fresh claim.
- **37f572f**: publishes the failed integrated r2, exact Linux client build and
  matched native query timing evidence.

The private Host's verified source plan is the authority for app/session roots
before purse custody signs. The reserve signature commits the ordinary bounded
purse hold and context; it does not independently attest every projected
physical root. Paid admission must recheck current roots before any fresh
delivery permit. Drift can leave a reserved hold requiring reconciliation;
reserve acceptance alone never permits fd3 delivery. Stable Hello lineage must
remain distinct from per-dispatch current generations and exact operation
bindings so hard reconnect does not freeze old authority into static custody.

Latency remains a material core problem. On independent copies of the same
post-reserve Store, old55 and f461 returned identical 101-byte signed query
views and left each Store unchanged. The two f461 samples took 83.04/81.72
seconds; old55 took 104.61/158.02 seconds. Old-source variation and concurrent
host load preclude a stable speedup estimate or attribution to one change.
See Mini's `docs/evidence/2026-09-27-native-query-latency-55-f461/`.

Next convergence: qualify the 2649 Host and retry actual GitWeb base; obtain
event22's accepted ticket before event27→reserve→paid native chaining; finish
source-bound resident START/STOP and dynamic v3 controller/resident wiring;
then exercise actual human and agent entrances in the same persistent app.
Two participants, delegated/revoked access, physical hard/soft disconnect and
restart, selective fn publish/receive, actual-model Hermes and programmable
CLI remain completion obligations. Independent component greens do not close
them. Root owns scoped commits; other sessions' work remains untouched.
