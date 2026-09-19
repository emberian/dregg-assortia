# Matched signed query at eight-event history

The same signed observation was run sequentially against the same frozen SQLite history and pinned configuration. The challenge decodes as an authorized resource query for object 1600 at height 18 (eight events after genesis). Parent host SHA256 `5ec9755d2013d136d22626ca6823ef324c75b1b65cd8e0ac829546ac8a1ed68c`; charge-materialized host SHA256 `3107faf3583e4c4926feb8931edee6e0aea4f800617bc0969d9d3c845caebe4d`. Each command and input hash is recorded here. The fixture, config contents, signatures, store, and query results are not archived.

Both `query` commands exited 0, produced a canonically decoded resource view, and returned byte-identical 98-byte output (SHA256 `150eed7b0d582a748bf4008677e942a412091afaf334caf1452f2d541c6ed396`). The full 97,386-byte logical image, read via the SQLite helper's `read-to ROOT OUTPUT` before and after each query, remained byte-identical (SHA256 `5183efaa85c8e2248ae2b150ca439d803ab447d0ad08e13fb9f2299a5156e6db`). The physical SQLite file hash also remained unchanged. `verification.txt` records the comparisons.

| Host | Wall | User CPU | System CPU |
| --- | ---: | ---: | ---: |
| Parent 5ec | 105.51 s | 103.75 s | 0.93 s |
| Charge 310 | 91.66 s | 89.83 s | 0.73 s |

The charge host saved 13.85 s wall (13.13%, 1.151× speedup) and 13.92 s user CPU (13.42%) in this one sequential late-history trial. Other system activity was present during measurement.

Two earlier small-workload measurements found no gain. The one-event task query took 33.55 s on host `0da9f139...` and 35.63 s on charge host `3107faf3...`. The fresh signed birth took 49.43 s on host `ea8d229f...` and 63.59 s on charge host `3107faf3...`. Inputs and output bytes match within each pair (`other-workloads-verification.txt`); only manifests, timings, bounded public JSON, and hashes are archived here. These older hosts are **not** the immediate parent `5ec9755d...`, and these comparisons do **not** isolate the two-file charge delta. Together with the history-eight result, they show workload-dependent performance rather than a general speedup.

The exact commands use the pinned config and signed query paths in `old-command.txt` and `new-command.txt`. Timing came from `/usr/bin/time -lp`; start/end UTC and bounded timing lines are retained. No interpreter was used for either query.
