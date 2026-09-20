# Charge-only host on the completed 11-event image

**PASS for this bounded regression.** The original New World runner completed
with `summary.json` reporting `result: PASS` and `acceptedEvents: 11`. A
consistent SQLite backup of its store was taken after the owner obtained a
positive signed policy view. The backup's full 115,541-byte logical `read-to`
image was byte-identical to the original run's final image.

On that same private snapshot, the installed charge-only host accepted the
owner's signed policy query and returned the **exact 130-byte view** from the
original host. It then processed the original signed owner-repair call and
returned the **exact 58-byte admission refusal** from the original host. The
private store's complete logical `read-to` bytes were unchanged after both
calls. The private SQLite file hash also stayed unchanged. These are replay
and lockout checks on the completed image, **not** a second full New World
journey.

The executed host was
`/Users/ember/dev/minidregg/.lake/build/bin/minidregg-host`, SHA-256
`3107faf3583e4c4926feb8931edee6e0aea4f800617bc0969d9d3c845caebe4d`.
The original host SHA-256 was
`0da9f1392fad3913356e3a495f0d3ab4f1a247aec8988a9f90312666e9ccadc1`.
`result.json` contains exact hashes, timings, and comparison results;
`original-summary-projection.json` is a bounded projection of the captured
original `summary.json`, whose full-file SHA-256 is recorded in `result.json`.

A private fixture was created with:

```sh
sqlite3 -readonly ORIGINAL_STORE/forward-link.sqlite3 \
  ".backup 'PRIVATE_STORE/forward-link.sqlite3'"
```

Its pinned config used a literal `storageRoot` replacement; reversing that
replacement and comparing with the original config returned exact bytes. The
two executed host commands were:

```sh
/usr/bin/time -p /Users/ember/dev/minidregg/.lake/build/bin/minidregg-host \
  PRIVATE/pinned.json query PRIVATE/rule-30011-observe-signed.bin \
  PRIVATE/new-rule-30011-view.bin

/usr/bin/time -p /Users/ember/dev/minidregg/.lake/build/bin/minidregg-host \
  PRIVATE/pinned.json submit PRIVATE/cycle-no-owner-bypass-call.bin \
  PRIVATE/new-no-owner-bypass-outcome.bin
```

Here `PRIVATE` is
`/tmp/minidregg-cycle-20260919/acceptance/charge-final-lockout-private-20260919T234828Z`;
`ORIGINAL_STORE` is the original runner's
`/tmp/minidregg-cycle-20260919/acceptance/new-world-final-run1/artifacts/store`.
The accepted query ran 23:49:00–23:51:07 UTC (127.08 s, exit 0); the refused
submit ran 23:52:57–23:55:06 UTC (129.25 s, exit 0). `query-time.log` and
`submit-time.log` retain the bounded `/usr/bin/time -p` output. The public
policy projection and decoded refusal are included. No keys, configs, signed
observations, signed calls, raw views/outcomes, or stores are archived.
