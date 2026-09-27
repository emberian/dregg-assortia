# Checkpoint 36 — receiving closure and physical integration gaps

September 27, 2026. Continues [checkpoint 35](checkpoint-35.md). The full
platform goal remains active; no combined deployment or real-model run is
claimed.

Mini `1412947` commits the corrected fn namespace registration and ordered
frontier replay. Event20 binds a gateway-independent namespace to an explicitly
authorized gateway and initial anchor. Events17/19 require its exact admitted
registration receipt and share the predecessor claim. Completion replay also
retains the original lifecycle claim from the same admitted walk. Narrow source
checks and independent review passed; native fn receiving remains pending.

Gateway rotation has a concrete limitation: `fnGateway` is not in the runtime
parameter commitment, while historical replay checks the configured pin. A
changed pin can therefore invalidate the old prefix. The first implementation
requires a fixed operator pin per deployment. A new fn namespace alone does
not implement rotation. Historical issuer provenance and migration remain
separate work; `70824ca` corrects the protocol record accordingly.

Mini `21955e2` fixes birth-family exhaustion after an interrupted authoring
attempt. A durable default-false marker distinguishes proven pre-submit work
from legacy or potentially submitted attempts. Only the former can reclaim an
unoccupied tail ordinal, after signed zero settlement, in one atomic journal
write. Five focused tests passed. The actual hard-EOF/recovery/same-session
Hermes rerun is being prepared from that exact archive.

Mini `589b62c` commits event18 completion receiving and receipt-only lookup,
private operations38/39, strict resident claim inspection and configured
custodian-key parsing. The receiver checks current law and admitted original
claim, submits once, and requires exact physical post-image readback. This
fixed source is the next native build cutoff; the prior qualified binary is
still `ebddd8e`. No completion has yet been physically accepted.

Resident-host review found missing integration work before exposing HTTP:
check the exact systemd MainPID before consuming the one-shot launch claim;
protect pinned helper/config paths against ancestor replacement; record native
START completion before requests can reach fd3. Pure authoring stages did not
yet provide management and package-observation credential challenges from the
current verified image. Private operations44/45 are now allocated for that
source-owned prepare/assemble path. Rust must consume those exact headers,
not reconstruct authorization itself. The service must multiplex separately
pinned browser/API callers through one resident SPK process and RpcDriver.

The fresh positive-tariff fixture successfully created the app and session,
then stopped on a wrapper path error before any share plan or ticket submission.
The two-path repair is committed in `70824ca`. A distinct second attempt uses
that known pre-share base with new request/evidence paths; uncertain native
effects are not being retried. Its final outcome remains pending.

Next acceptance joins: finish positive-rate sharing; finish the real interrupted
birth recovery run; qualify `589b62c`; consume native completion signing plans
in the physical supervisor; integrate shared-resource discovery into both
controllers and paid agent dispatch into the actual Hermes tool path. The
agent event21 must record the original reserve's one-use claim and physical
purse guard while deferring settlement until a definite reply or explicit audit.
