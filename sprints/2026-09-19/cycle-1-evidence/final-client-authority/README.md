# Mini authority client: completed local process journey

**PASS, process exit 0.** The fresh two-signer run used the ordinary Rust `mini`
client and the source-owned JSON authoring in `minidregg-host`. Alice birthed a
scalar object, installed a rule, delegated a narrower observe/mutate object
capability to Bob, and revoked it after Bob's own signed write. Accepted counts
were exactly 1 through 5: birth, policy install, delegation, Bob's write, and
revocation. Alice's disallowed write and Bob's attempted policy replacement
were fully signed calls refused at host admission. After revocation, Bob's new
signed read returned no view and his new signed create of *absent* field 2
returned no plan. Retrying Bob's original retained call returned the identical
historical receipt and did not advance the authorized current image boundary,
height, or observed scalar state.

The canonical source identities are:

| Item | Identity |
| --- | --- |
| Authority script | `native/resource-client/authority-acceptance.sh`, source commit `63612f5`, SHA-256 `ff060ce20410c7c31539a855e0c17f1f9beb5b7e937c2089fe3129f809abff50` |
| Policy-view source | `Host/Json.lean`, commit `b119f868742edd687064ff4449c05595e8f26e0d`, SHA-256 `a28fb3281c2c04409c14520757978abcabb38defb5ccd86776919befc35e03af` |
| Executed native host | `/tmp/minidregg-cycle-20260919/build/final-client-api-host-20260919T212000Z/minidregg-host`, SHA-256 `5ec9755d2013d136d22626ca6823ef324c75b1b65cd8e0ac829546ac8a1ed68c` |

The host was built from the frozen semantic source plus the narrow authorized
`view-policy` presentation addition in `Host/Json.lean`; its isolated build
manifest is retained here. The existing NewWorld run used the earlier semantic
host and supplies stronger exact physical-image checks. This client script
checks the current public image boundary, height, and authorized resource view;
it does **not** compare full storage bytes.

The exact completed command was:

```sh
MINI=/Users/ember/dev/minidregg/native/resource-client/target/debug/mini \
STORE_BINARY=/Users/ember/dev/minidregg/native/hyperdocument-link-sqlite-store/target/debug/minidregg-link-sqlite-store \
SIGNATURE_BINARY=/Users/ember/dev/minidregg/native/credential-signature-verifier/target/debug/minidregg-credential-signature-verifier \
/usr/bin/time -p \
  /tmp/minidregg-cycle-20260919/authority-client-script-final2/authority-acceptance.sh \
  /tmp/minidregg-cycle-20260919/build/final-client-api-host-20260919T212000Z/minidregg-host \
  /tmp/minidregg-cycle-20260919/authority-client-final2-20260919T215438Z \
  > /tmp/minidregg-cycle-20260919/authority-client-final2.log 2>&1
```

The fresh fixture was created at **2026-09-19 21:54:50 UTC** and the final
summary/log was written at **22:09:54 UTC**. `/usr/bin/time -p` measured
**904.65 seconds** real time. The command exited 0. The script SHA-256 embedded
in `authority-acceptance.json` matches the immutable executed copy and the
committed source. `focused-checks.log` records shell syntax, ShellCheck,
receipt-shape, refusal, retry, state, and exact policy byte-roundtrip checks.

`policy-before-view.json` and `policy-after-view.json` are authorized decoded
current-source views. The initial empty predicate and installed nested
`any`/`all` rule were each reconstructed from the public JSON fields, passed
back through `mini author --kind policy`, and compared byte-for-byte with the
canonical view bytes. `policy-roundtrips.json` gives both source-authored
binary hashes and lengths. The five installed receipts and Bob's replayed
receipt are separate decoded JSON files. The state projections contain only
height, boundary, authority root, resource root, and scalar entries. The two
admission-refusal outcomes and the four friendly refusal intents are retained
with `refusal-records.json`, which states the signed-call and signed-observation
stage reached. `earlier-attempts.md` separates non-passing fixture runs from
this completed run.

No private keys, signatures, signed calls, operator configs, or stores are in
this archive. The original local fixture remains outside Assortia.
