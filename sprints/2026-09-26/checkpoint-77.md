# Checkpoint 77 — real package materialization, refused INSTALL completion

September 28 UTC, 2026. Continues [checkpoint 76](checkpoint-76.md).

The real signed GitWeb package is now materialized on hbox. Mini admitted the
INSTALL BEGIN at count28 and its claim at count29. **Completion was refused**;
the original-ingress receipt lookup is absent. No second completion was sent.
This is a physically verified package and an unfinished authorized lifecycle,
not a running application. mini_app_contract retains sole live Store ownership
and is diagnosing the precise source admission predicate.

## Retained live evidence

The fixture root is
`/var/lib/minidregg/spk/fixtures/gitweb-v2-20260927-client-session-r3`.
The retained operation journal is
`/var/lib/minidregg/spk/install-ops/gitweb-r3-0002`.

| Step | Exact boundary |
| --- | --- |
| Pure preparation | User invocation `670871036976425ca411a8c533b402d0` completed. Both identities and original four-field receipts matched. Canonical Store hash remained `10e7805801a08e28a0c1e2d008619ec013c868a0d09fd9922795eafb4ffc6b27`. |
| BEGIN and claim | User invocation `56a6996a545a4753b3d7372df397b199` completed; counts28/29 retained. `install-prepared-v2.json` SHA `b8a2b1a44cf8d4b66885ffd16ff0ba2103a14ede250b9877061106d69efbac08`. |
| Physical ingestion | First attempt refused because the private inbox was absent. After root-owned0700 inbox initialization, distinct root invocation `7fdcaddb678941f68dd3731e55a28a92` completed with ingestion and inspection markers. |
| Actual image | `/var/lib/minidregg/spk/packages/sha256-2bbfe6d3c705dfb0696905ecd9c1d00d6554cc1224e63dc5545152af5f8f2caa`, root-owned0555. Root independently checked ownership and package SHA. |
| Read-only adoption | Completed; adoption JSON SHA `20fa80c9bb56f4f65fdeabd5d34fd9937b1e4d3cff4aca90d1d88c6ff2bafe5e`, joining original BEGIN/claim, prepared request and inspected image. |
| Completion op38 | User invocation `7d0abf2251c34a6396001bf0992259cc`, exit1, retained `completion-v2-author/op38-outcome.json` reports refused. |
| Original receipt op39 | User invocation `5cfb293adc8b4914a31c4a9a18091789`, retained lookup reports absent; no `install-completed-v2.json`. These terminal outcomes are owner observations, not inferred from collected-unit defaults. |

The source-derived volume identity is
`0e3f217b881900771c7bbcf5d15166b089cba6f2c96c787f93bc6e1e67036b47`.
Physical volume creation/attestation, tickets, START and enrollment still follow
successful INSTALL completion. Preserve the failed ingress and marker; diagnose
against the original count29 image before preparing any legitimate successor.

## Qualified consumers and remaining core work

Mini `e1a36c0` adds typed read-only `grain-share-issue-plan` over the persistent
operator's op56. Both ticket wrappers consume and pin its exact plan. Focused
client tests passed5/5 and strict Clippy passed. The exact committed release is
staged at `/tank/dregg-build/minidregg-mini-e1a36c0/bin/mini`, SHA
`2c0fee88774e003c1eac9c9a715a0f9c18c5a92bbe862c1bc651d695ca757e6a`.
This does not require restarting the current cb55 operator. Five ticket issues
need separate reserve3/settle sequences; event27 does not charge that tool.

Mini `8153a37` fixes the private Git client's umask and preserves a successful
real-Git/native-entrance lost-reply probe. The corrected helper is
`/tank/dregg-build/minidregg-spk-gitweb-umask-r1/bin/gitweb-human-journey`, SHA
`cea0692f412d3d24f84bb2a5d4eed32e90b89425e9f64b19cd1f2416b964be2a`.
This is component evidence, not yet actual signed-app dispatch.

Event28 enrollment construction and admission modules passed direct Lean checks
in a private overlay. They derive the exact ticket, check current serving app
and signed manifest, reuse session/content laws and add separately authorized
observations with physical read guards. Replay, native receiving and Host JSON
wiring remain in progress; Rust custody integration awaits the frozen ABI.
No live enrollment is claimed.

Real Bonsai remains an independently qualified local provider. Its existing
invocation expires at03:16:33 UTC; no extension or replacement is claimed.
No actual combined Hermes/Mini/shared-GitWeb/fn journey has completed.
