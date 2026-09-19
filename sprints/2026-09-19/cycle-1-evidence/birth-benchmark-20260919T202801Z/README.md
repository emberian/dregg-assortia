# Matched-input native birth — September 19, 20:28:01 UTC

The captured `manifest.txt` records exit 0. `time.log` records 223.78 seconds wall time, 218.41 user seconds and 1.77 system seconds. The public `outcome.json` is `confirmed` with confirmation `installed` and accepted count `1`; it retains the exact transaction, event and image-boundary identifiers. This is a successful single birth, not the complete native multi-resource acceptance journey.

The benchmark reused the exact signed birth and pinned genesis of the preceding native acceptance run, with independent fresh storage. Their hashes are retained in the original manifest. This is the meaning of *matched*. Neither signed call bytes, genesis bytes, runtime configuration, signing material nor the storage directory were copied.

The benchmark executable SHA-256 is `02f3750a53a7620857273ef632fd6c9a41b02a511d7b76c4d0a5e918ad1ee855`. `host-build-manifest.txt`, `host-affected-source.sha256`, `source-overlay.tsv` and `component-build.log` identify its eleven-module birth-guard rebuild. The base optimized host manifest and affected-source manifest identify the preceding fifty-module rebuild; the earlier baseline build is retained elsewhere in this archive. `usage_exit=1` in build manifests is the no-arguments CLI probe, not this benchmark's exit status.

The executable is distinct from full-gate host `f4c507ad…`. The full umbrella's 584-file canonical-source match is recorded separately; this benchmark does not by itself prove identical complete source closure between the two executables.

No comparable uninterrupted old birth timing is retained, and root reports that the preceding run's birth completed before a matching measurement could be captured. Therefore **223.78 seconds is a measured successful birth, not a speedup**. It remains too slow for an interactive experience. Complete native integration was still pending at this checkpoint.

`stdout.log` is the original empty output capture. Original artifact hashes are retained. The captured benchmark manifest does not contain its exact shell invocation, so none is reconstructed here as if observed. No benchmark was rerun to make the archive.
