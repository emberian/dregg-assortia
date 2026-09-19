# Final local client run

The Rust `mini` client completed the local host journey on 2026-09-19 from
21:02:25 to 21:09:49 UTC (444 seconds). The command exited 0:

```sh
native/resource-client/acceptance.sh \
  /tmp/minidregg-cycle-20260919/build/native-theta-birth-order-20260919T205800Z/minidregg-host \
  /tmp/minidregg-client-final-combined-20260919T210700Z
```

The source and executable used in this run had these SHA-256 hashes:

| Input | SHA-256 |
| --- | --- |
| `minidregg-host` | `0da9f1392fad3913356e3a495f0d3ab4f1a247aec8988a9f90312666e9ccadc1` |
| `mini` executable | `615e9129fbbf6c37c03b195312d4ab2ea5f43c6a83a31051c26728d797f5dc57` |
| `Host/Json.lean` | `b2b6de00be8f4daf85bed5b29bf6167432284a0a99a04eab5d865728e0e5d6be` |
| `native/resource-client/src/main.rs` | `cca1bcab4e53c8293a053031a21e9738f18fa8abd3b9e77b6650cd5ecca9bbfe` |
| `native/resource-client/Cargo.lock` | `66064ff0691df864d6fd33d8d623ac289732ed8e98cde0e0e2bf6da49d4f0de0` |
| `native/resource-client/acceptance.sh` | `a4593c89e6c19cb7ce096139c08fd372b2ed9ec8fed55d26448b0ef27e802e42` |

The client generated a fresh signer and pinned deployment, birthed content
object 600 and declared object 601, and committed a typed content operation
after deliberately losing its first outcome delivery. Reusing the retained
signed call recovered the same historical receipt by submit and lookup. It
then committed one mixed content/scalar transaction. Its signing roles were
`4,4,8,8,1`: two mutation signatures, two current observation signatures,
and shared authority. The joint receipt was replayed from the exact same
call without advancing the current image boundary or height 13. Authorized
final queries showed atom 7001 with payload `68656c6c6f` and newly created
declared field 0 with value 1. The born declared page's neutral field 1
remained 0.

`acceptance.json` and `run-evidence.json` summarize the run. The receipt and
view JSON files are copied directly from the successful attempt; the three
boundary files and signing roles are bounded projections of public host
presentations. `first-outcome-delivery-error.txt` records the deliberately
missing output path. `focused-checks.log` records format, clippy, nextest 4/4,
and shellcheck passes.

This archive contains no private key, operator config, signed call, signature,
or SQLite store. Full local attempt artifacts remain in the temporary evidence
directory named in the command above.
