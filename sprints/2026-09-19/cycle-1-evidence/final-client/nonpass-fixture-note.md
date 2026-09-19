An earlier fixture run against host `f4c507ad…3070e1` was **not a pass**: its
script expected the newly born declared page to be empty, while the canonical
neutral page contains `object601.field1=0`. The fixture assertion was corrected
in `a47c727`; no result from that failed run was promoted into this archive.
