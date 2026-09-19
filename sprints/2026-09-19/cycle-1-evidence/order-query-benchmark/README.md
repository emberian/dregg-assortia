# Previously stalled task query

The exact signed query from the interrupted `new-world-fullgate-run1` was retried against its unchanged one-event store with the combined theta/birth/order host. It returned exit 0 in **33.55 seconds** and decoded as the expected task resource: generation 0, status 0 (paused), remaining 100, reserved 0, no exposed balances.

The earlier candidate was interrupted after profiling showed all 1,502 active samples in order-witness bit generation; its complete latency is unknown. No exact before/after speedup is claimed for this query. The new timing includes semantic history verification. See the manifest for the executable and signed-query hashes, exact command and timestamps. `view.json` is the public decoded fixture response; no configuration, signed call, store or key is archived.

The complete New World journey was still running when this query evidence was captured. This result does not replace that acceptance check.
