# Final legacy native scenario

The compiled public acceptance driver completed against the combined host on
September 19, 2026, from 21:03:48 to 21:21:35 UTC. The wrapper records exit 0
and 1,066 elapsed seconds (its integer elapsed counter differs by one second
from the formatted timestamps).

`manifest.txt` records the exact command, committed source, driver, host and
helper hashes. The host is `0da9f1392fad3913356e3a495f0d3ab4f1a247aec8988a9f90312666e9ccadc1`,
whose 153 Lean source files match Mini commit `12e6608`; see the independent
[committed-source build evidence](../final-build/README.md).

`run.log` is the complete captured public driver output. All six accepted
mutations, two rule replacements preserving the existing grants, narrowed
Bob delegation and invocation, current-rule refusal, conserved Book and
single birth charge passed. Fresh processes recovered every original
receipt by historical lookup and exact signed-call retry without changing
the final physical bytes. The scenario also refused forged histories with
hidden balance, unknown ingress, changed event and changed charge, and
refused malformed signatures and outer encoding without mutation.

This is the legacy scalar/authority regression scenario. It is separate
from the New World task/content scenario, hosted Hermes deployment and
generation-wide native revocation. Earlier interrupted attempts remain
interrupted; this directory records the final complete run only. No private
key, deployment configuration, raw signed call or store is archived here.
