# Construction checkpoint — September 26, 23:40 UTC

The autonomous Mini/fn construction goal remains active. This follows
[checkpoint 11](checkpoint-11.md) without changing its dated claims. The
results below refer to separate source snapshots, Stores, controllers and
tests; none makes the combined new Host a deployed service.

## Combined native host and receiving cost

Mini commits `d84790e` and `49314f5` qualify a combined UInt64 cSHAKE and
exact-readback persistent Host. The [169-source Mac/Linux build record](https://github.com/emberian/minidregg/blob/49314f5/docs/evidence/2026-09-26-mini-u64-exact-session/README.md)
pins the Mac binary SHA-256 `a7dd4605ef80d49a3cc9a9e5eeaed5cb8fc4bac4554ce7ea7562475aaa70717f`
and Linux binary SHA-256 `d413081bb6c6ac1c0699b5fdc22cf3a13fb87930ff49ac147ae994e2c364e7a3`.
The source and artifact gates passed in independent snapshots. The combined
[runtime evidence](https://github.com/emberian/minidregg/blob/49314f5/docs/evidence/2026-09-26-grain-performance/u64-exact-session.md)
uses the *same* retained 734,222-byte signed B call and private copied
accepted-one SQLite image: one warmed persistent submit took **23.22 s**,
versus **96.55 s** with exact readback and the older cSHAKE core and
**172.92 s** on the earlier persistent baseline. Its 132-byte Outcome and
final SQLite image are byte-identical across all three runs. These are
single matched measurements under shared load, not a general latency bound.
The combined Mac image also passed all four fresh physical readback cases,
rollback and same-height-fork poisoning, and the retained verifier-helper
path-replacement/removal pinning cases. The separate [helper-pinning record](https://github.com/emberian/minidregg/blob/d84790e/docs/evidence/2026-09-26-grain-performance/u64-exact-session.md)
describes exactly what source-path drift was tested. That is broader than the one-call
timing, yet remains scoped native evidence rather than hosted deployment.

## Hosted recovery and two distinct B workflows

Commit `e6b7874` records the [fresh 7715 one-pass policy-install crash](https://github.com/emberian/minidregg/blob/e6b7874/docs/evidence/2026-09-26-grain-interrupt-recovery/policy-crash-7715/README.md).
The fixture killed its own controller after confirmed generation-1 worker-law
installation but before attach. The replacement used exact lookup-only
recovery, preserved all four original receipt fields and call bytes, cleared
the pending slot, and attached at signed generation 1/status 2. This is a
fresh native recovery acceptance for that crash window, separate from the
earlier 7705 continuation and from live Hermes.

Commit `b58c209` records [two hosted peers on one content resource](https://github.com/emberian/minidregg/blob/b58c209/docs/evidence/2026-09-26-hosted-peers-reconcile-stale/README.md).
A's retained Hermes session loaded and reconciled the shared atom; native
tool edit and parent settlement confirmed, and an independent signed read
showed the new text. B's separate 7803/7804 stale-root publication was
refused during native preparation with `Reject.staleTarget`, **before a
signed call or outcome existed**. The old runtime nevertheless retained an
uncertain tool attempt 44 and reserve-2 hold; B's parent settled separately,
and a signed read showed no B content change. This is not a completed stale
retry, recovery, or B publication. The [physical worker record](https://github.com/emberian/minidregg/blob/b58c209/docs/evidence/2026-09-26-hosted-pair-linux/README.md)
shows separate scoped workers and closed cgroups but does not resolve the
Mini hold. The service used deterministic loopback providers and one Unix
account, not a paid provider or production tenant isolation.

The fn R2 receiving B is **another** Store/workflow. Its earlier exact
lookup confirmed the original accepted B call despite a lost submit
response; durable fn ACK and signed content/source-receipt readout remain
pending. Commit `1ec69bd` changes the Rust client's retained pending-call
migration to require explicit image and receipt evidence, with the owner
reporting **31/31 focused tests**. Its source is
[`drain.rs`](https://github.com/emberian/minidregg/blob/1ec69bd/native/resource-client/src/drain.rs)
and [`main.rs`](https://github.com/emberian/minidregg/blob/1ec69bd/native/resource-client/src/main.rs).
Commit `9735509` further binds migration to the retained attempt's exact
config snapshot bytes ([source](https://github.com/emberian/minidregg/blob/9735509/native/resource-client/src/drain.rs)).
Actual upgrade of that fn R2 B attempt is **in progress**. The current
socket/serving-image pin boundary is being repaired by the client/receiver
owners before they use it; these component changes are not an ACK or
completed migration. They do not resolve hosted peer B's uncertain tool hold.

## Agent-visible receipt and next resource operation

Commit `8d88b9e` makes the deterministic Hermes provider fixture strictly
extract the same tool's model-visible Mini publication receipt and stop on
that result. It does not use the receipt to select a next-prompt root. Its
[source hash](https://github.com/emberian/minidregg/blob/483e011/docs/evidence/2026-09-26-hermes-provider-strict-8801-linux/source-sha256.txt)
for `src/main.rs` is `1e488dc50022bdbc3552ac811610a8c1f4df3b31ff68850a08acb25f2dea0d71`;
the [Linux focused log](https://github.com/emberian/minidregg/blob/483e011/docs/evidence/2026-09-26-hermes-provider-strict-8801-linux/nextest.log)
passes **11/11** tests. A fresh actual Hermes receipt gate remains pending.
Fixture success does not retroactively turn older tool-state responses into
delivered publication receipts.

Commit `a933651` adds
[`GrainResourceBirthAuthority`](https://github.com/emberian/minidregg/blob/a933651/Compiler/GrainResourceBirthAuthority.lean)
and changes the grain-backed birth and ordinary birth source to share one
prepared authority update for birth grants and the composite operation
marker. This is source-level construction; actual composite birth admission
with tool settlement and parent witness has **not** passed. The next native
case must check the one-old-image authority semantics and exact durable
receipt, not infer them from a helper module.

Commit `d9edc9c` adds the
[whole-prefix release proposal](https://github.com/emberian/minidregg/blob/d9edc9c/docs/FN-RELEASE-DESIGN.md).
It proposes an agent's later signed Mini release decision over an exact
already-signed R carrier, with public-history authority and current parent
witness. Ember has not selected this design, and no release policy,
tool, outbox gate or automatic agent sharing is implemented. Today's R
still exposes its full original Mini prefix; a private workroom needs a
different selective or cross-Store construction.

Next receiving work is the exact retained fn R2 B migration/ACK/readout on
its qualified image. Independently, hosted peer B needs a source-owned
disposition for the pre-submit stale refusal and held allowance; the 8801
fixture needs an actual Hermes receipt run; composite birth needs native
admission. Keep these receipts and Stores distinct. No new public friend
onboarding, paid model/provider result, production deployment, private-prefix
release, or completed succinct assurance is claimed.
