# Construction checkpoint — September 27, 01:40 UTC

The overnight goal remains active. [Checkpoint 15](checkpoint-15.md) retains
the dedicated-account Hermes A→B→A workroom result. This checkpoint advances
provider settlement and operator hosting, and records a real fn restart
failure before any transport cursor was advanced.

## A native charge, and a held uncertain response

Mini `90f1bb8` preserves [bounded native metering evidence](https://github.com/emberian/minidregg/blob/90f1bb8/docs/evidence/2026-09-26-provider-metered-runtime-native/README.md).
Immutable runtime `1c56596` (Linux SHA `b584a937…`), provider Host
`51f790fa…`, client `fee5bc86…` and deterministic upstream `9dcf2125…`
processed one actual 37,069-byte Hermes request. The source-owned usage
quote reported 1 input and 2 output tokens; the ordinary signed Mini
settlement charged 3 at accepted count 11. The signed provider view showed
remaining 47, reserved 0. Exact request/response, quote, settlement-call and
receipt identities remain in private custody; bounded projections are
committed. This is provider-reported synthetic usage, not a paid invoice.

A separate fresh Store received one response without terminal usage. The
native quote refused, reserve 3 remained held, and Hermes retry caused no
second upstream completion. That effect was not silently settled for zero.
HTTP 422, interruption during quoting and post-settlement crash recovery
remain separate gates.

An attempted HTTP 422 gate instead exposed enabled Hermes auxiliary title
generation competing for the prompt's provider lease. No upstream completion
occurred, so it is not a 422 result. Subsequent source inspection found that
successful settlement already permits another distinct request under the
same prompt, while an unresolved request blocks it. The observed auxiliary
task cancellation left just such a hold. Sequential multi-request native
acceptance and an explicit auxiliary-purpose policy are next; disabling
titles alone does not establish normal multi-turn hosted Hermes metering.

## fn progress: two measured failures and the current repair

The first own-R gate refused fn's qualified header prefix. Mini `4089f24`
repairs framing while requiring the complete authored carrier tail to match;
`9e4ac1c` qualifies the rebuilt Mac Host `6e76d0da…`.

That image accepted one signed Mini tag-9 progress record at count 4 while
fn's ACK remained zero. Restarting the same A service then proposed a new
operation instead of finding the accepted one. [Mini `21ed0c5`](https://github.com/emberian/minidregg/blob/21ed0c5/docs/evidence/2026-09-26-ownr-native/second-red-README.md)
preserves the accepted receipt and restart failure. The second proposal was
not submitted; fn was not ACKed. The durable identity incorrectly included
the per-start temporary executable-copy path. `2b6db7d` changes own-R binding
to the stable configured fn identity already used by the other paths; its
narrow Lean check passed. A qualified rebuild and fresh native
accept→restart→repeat→ACK gate are pending. The old accepted malformed-bound
record is preserved, not reinterpreted as success under the repair.

## Hosting and resource construction

Mini `a3dbcdd` adds the [private operator stack installer](https://github.com/emberian/minidregg/blob/a3dbcdd/deploy/grain-host/OPERATOR-STACK.md).
Its actual systemd pre-start guard passed with `NoNewPrivileges=yes`, and a
changed helper pin refused before execution. Read-only quiescence checks
passed on both dedicated task controllers. The first live migration stopped
safely at a frontend readiness check; diagnosis found a permission-probe
disagreement with named ACL access. Actual file-read/socket-connect probes
are replacing that check before migration and signed-root restart acceptance
continue. Boot startup remains explicitly unqualified;
no reboot, public SSH key installation or public service is claimed.

Composite grain-backed resource birth is wired through native authoring,
admission and replay (`fa7d4c4`, `fbd4401`). The fresh acceptance script now
requires a signed worker birth with atomic allowance settlement, an owner
bare-birth positive control and the exact worker factory-policy refusal.
The source-qualified Linux composite build is complete. The first signed
fixture refused during factory observation: its law omitted permission to
observe before preparing a birth. A fresh fixture with that permission is
running; no composite receipt is claimed yet. Its frozen Host still predates
the latest own-R identity repair.
MCP creation will be exposed only through the real durable birth lifecycle,
with receipt recovery and the newly issued capabilities.

The terminal frontend and exact legacy B44 operator-audit recovery are
under integration. Terminal source tests do not establish a deployed user
entrance; the separate old B44 hold is still unresolved. Guarded native
suffix builds now support explicitly declared inserted modules (`d152602`),
with a positive source-closure comparison and three refusal probes; this is
build provenance, not a new runtime acceptance result.

## Transport trust and next core work

Ember's explicit principle is that fn is semi-untrusted. The
[disclosure contract](fn-publication-disclosure-contract.md) and
[selective-origin proposal](https://github.com/emberian/minidregg/blob/7522ab6/docs/FN-SELECTIVE-ORIGIN-PROPOSAL.md)
separate owner-authorized messages admitted by the receiver from independently
proved historical Mini acceptance. Current full-prefix evidence discloses
unrelated prior history. New release and historical-selection kernel work
must preserve that distinction; no encryption suite, private sharing
protocol or selective cryptographic proof is delivered by this checkpoint.
Mini `c4f5c83` adds a general theorem selecting the exact admitted record,
ingress and original receipt from verified replay. Its narrow Lean check
passed; it specifies part of the historical relation without providing a
private cryptographic witness or changing the current evidence exporter.
