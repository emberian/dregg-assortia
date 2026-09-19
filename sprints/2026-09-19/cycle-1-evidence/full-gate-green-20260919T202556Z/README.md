# Full umbrella gate — September 19, 20:25:56–20:28:16 UTC

The preserved wrapper `build.log` records `lake-gate Minidregg PASS 59s` and `lake-gate Host.Main:leanArts PASS 12s`. The line-numbered umbrella excerpt ends with `Build completed successfully (9107 jobs).` Those are actual completed gate results, not inferences from the process exit or prior component checks. Overall compilation/linking elapsed 140 seconds.

`manifest.txt` identifies Lean 4.30.0, the complete umbrella scope, source/module counts and the linked host. Its binary SHA-256 is `f4c507ad39d625609dcd304e455d34944310ed336412d8b4f5f6a6878e3070e1`. `usage_exit=1` records invoking the executable without required CLI arguments; it is not the gate verdict.

`source-sha256.txt` names the exact 584 source files checked for this build. Root's original `canonical-source-recheck.txt` contains 584 `OK` lines and no other lines; `source-match-summary.txt` is a bounded count of that captured result, not a new execution. Snapshot `git_head=8305b6e…` is its initial Git identity, not a claim that its later overlays are represented by that commit alone.

Commands, compiler flags, artifact hashes, wrapper concurrency summary and bounded completion excerpts are included. `original-logs.sha256` identifies the full temporary logs; the large warning/proof traces are omitted. Source and executable hashes are distinct: this host is not the separately built guard-cache host used for the adjacent birth benchmark.

This archive does not claim a completed native scenario, security deployment, succinct proof, provider execution or live token operation. Complete native integration remained pending at this checkpoint. No build was rerun to make the archive.
