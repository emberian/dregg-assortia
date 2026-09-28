# Checkpoint 78 — native enrollment core and real grant prerequisites

September28 UTC,2026. Continues [checkpoint77](checkpoint-77.md).

Mini `e06b2fa` commits the event28 enrollment source, current construction,
signed admission, physical read guards, same-walk Replay join, authoring and
inspectors. Seven exact modules passed direct Lean checks in a private cb55
overlay; root rechecked their hashes before committing. Evidence lives at
`minidregg/docs/evidence/2026-09-27-session-enrollment/EVENT28-SOURCE.md`.
Native submit/lookup, Main/JSON routes and Rust custody integration remain
in progress. This source checkpoint is not a deployed enrollment.

## Correcting allocated authority versus admitted authority

The earlier statement that Bob and both agents *have* app-observe grants was
too strong. The fixture allocated their capability IDs, but no corresponding
delegations have been admitted. All five ticket-observe grants are also absent:
event22 creates the issuer's ticket owner/control grants only. Enrollment must
wait for actual narrow delegations, not merely an allocated ID.

| Participant | Session owner | Descriptor owner | App read | Manifest read | Ticket read |
| --- | --- | --- | --- | --- | --- |
| Alice Web8 | 147 | 149 | owner141 | owner143 | delegate173 from171 |
| Bob Web9 | 151 | 153 | delegate184 from141 | delegate185 from143 | delegate183 from181 |
| Alice API8 | 161 | 163 | owner141 | owner143 | delegate193 from191 |
| Hermes A10 | 241 | 243 | delegate274 from141 | delegate275 from143 | delegate273 from271 |
| Hermes B20 | 341 | 343 | delegate374 from141 | delegate375 from143 | delegate373 from371 |

Session/descriptor owner capabilities already cover their corresponding
observe and mutate operations. Ticket parents become available only after
their event22 issue. Every listed delegate remains **planned**, not admitted.
Manifest IDs185/275/375 were checked against the current allocation/scripts
and approved for a protected append-only delegation overlay. Preserve the
immutable retained r3 allocation and bind the overlay separately.

Root source review caught a second mistaken shortcut: separate observation
envelopes do not allow Alice's manifest capability143 to stand in for another
participant. `ResourceTransaction.requestFor` fixes each observation's subject
to the joint command subject; the signature header follows that subject.
Bob and both agents therefore need their own manifest observe grants too.
No new app-mutate authority or mixed-subject ABI is needed.

agent_api_host owns the exact narrow delegation workflow and its recovery
checks. mini_app_contract remains sole live writer while INSTALL is unfinished.

## Exact ongoing wait and model readiness

INSTALL remains at claimed count29 with its original completion refused and
receipt absent. The read-only admission diagnostic uses an exact private Store
copy and retained ingress on Persvati. Its third scope
`run-p458798-i989909962.scope`, invocation
`935766b8c5d44e1c9347f8965759bc97`, was independently observed running by root.
Earlier diagnostic attempts failed before Store access due to PATH and a Lean
root-main name collision; neither was an admission verdict. Do not resubmit
the original completion while the exact source predicate is being diagnosed.

The current A/B Hermes configs expose only status/read/publish MCP tools; the
GitWeb routes need accepted event22/27 lineage and route pins. Consequently the
earlier builtin-only inference measurement does not qualify the eventual full
tool catalog. A360-second request timeout is proposed for the first integrated
pilot, with outer worker bounds still to be reconciled and actual catalog
latency still to be measured. The original local model invocation remains
unchanged and expires at03:16:33 UTC.
