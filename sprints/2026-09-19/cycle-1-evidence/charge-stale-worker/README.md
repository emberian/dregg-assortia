# Charge-only host: stale-worker refusal on frozen eight-event history

**PASS.** A private copy of the frozen eight-event SQLite store was used to
submit the already-signed stale-worker call through the latest charge-only
host. The submitted call returned a canonical admission refusal whose **exact
58 bytes** match the outcome from the original semantic host. The SQLite
store helper's full 97,386-byte `read-to` logical image was **byte-identical**
before and after (`cmp`), and the private SQLite file hash did not change. The
original frozen store was read and copied only; its hash also stayed unchanged.
No shared benchmark store was opened for writing.

The exact native submit was:

```sh
/usr/bin/time -p \
  /tmp/minidregg-cycle-20260919/build/native-charge-20260919T220000Z/minidregg-host \
  /tmp/minidregg-cycle-20260919/acceptance/charge-stale-worker-private-20260919T222815Z/pinned.json \
  submit \
  /tmp/minidregg-cycle-20260919/acceptance/charge-stale-worker-private-20260919T222815Z/cycle-stale-worker-call.bin \
  /tmp/minidregg-cycle-20260919/acceptance/charge-stale-worker-private-20260919T222815Z/new-outcome.bin
```

The copied pinned config differed only in `storageRoot`; literal text
substitution preserved the full-width `expectedSeed`. Before and after submit,
`minidregg-link-sqlite-store read-to PRIVATE_STORE OUTPUT` produced the two
logical-image files compared with `cmp`. `cmp` also compared the new binary
outcome with the original host outcome. The frozen challenge decoded at height
18, consistent with eight accepted events after genesis height 10.

Submit exited 0. The process ran 2026-09-19 22:28:46–22:30:02 UTC and took
76.46 seconds real time. The executed host SHA-256 is
`3107faf3583e4c4926feb8931edee6e0aea4f800617bc0969d9d3c845caebe4d`;
the original host SHA-256 is
`0da9f1392fad3913356e3a495f0d3ab4f1a247aec8988a9f90312666e9ccadc1`.
`result.json` records the call, refusal, logical-image, and SQLite hashes, plus
both exact-byte comparisons. `public-outcome.json` is the decoded refusal;
`time.log` is the bounded `/usr/bin/time -p` output.

This archive contains no key, pinned config, signed call, raw outcome, or
SQLite store. The private fixture remains outside Assortia.
