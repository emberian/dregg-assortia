# Design investigation — durable evidence for hosted upstream Nous Hermes over OpenRouter

Date: 2026-09-19  
Status: **SOURCE-REVIEWED / PROPOSED**. This is a read-only design note over the current working tree. No build, test, model call, external service, or dated live-provider run was performed. It does not update repository status.

## Finding

The missing object is not another response attestation. It is one durable relation spanning four facts that currently live on separate rails:

1. a named user or delegated subject was authorized to make one bounded invocation;
2. the provider request was deterministically constructed from that invocation and the already-committed conversation state;
3. a pinned TLSNotary presentation authenticated that exact request and its response in one session with the intended gateway; and
4. the unmodified upstream Hermes agent consumed that exact authenticated response according to its actual protocol and execution semantics.

The current tree has substantial pieces of all four, but no verifier checks their conjunction. In particular, the TLSNotary verifier initially recovers authenticated sent bytes, while both live zkOracle adapters narrow them to `AuthenticSession { server_name, connection_time, response_body }` and discard the request (`zkoracle-live/src/verify.rs:31-44,60-82`). The request body is also not disclosed by the TLSNotary prover: the local Messages path reveals `req.without_data()`, the target, and headers (`zkoracle-live/src/tlsn_live.rs:510-532`), and the live Bedrock path does the same (`zkoracle-live/src/tlsn_bedrock.rs:271-287`). Thus the present verifier cannot establish that the authenticated provider session carried the prompt, messages, tools, model parameters, and prior observations the authorized invocation required.

The exact acceptance relation needed for attempt `j` is:

```text
Authorized(auth_context, subject, delegation, invocation)
∧ request_j = Serialize(Construct_v(invocation, committed_state_(j-1)))
∧ TLSNVerify(presentation_j,
             notary_anchor, gateway_host,
             sent = HTTP(method, path, public_headers, request_j, hidden_auth_value),
             received = response_j)
∧ ProtocolParse_profile(response_j)
∧ consumed_j = Consume_v(response_j)
∧ Bind(receipt_or_envelope,
       invocation_id, attempt_j, H(request_j), H(response_j), H(consumed_j),
       predecessor_state, successor_action_or_finish)
```

`Authorized`, `Construct_v`, and `Consume_v` must be independently checkable and versioned. For unmodified upstream Hermes, the exact `Construct_v` and `Consume_v` relations are not identified by the Breadstuffs source reviewed here. They may include streaming/SSE framing, accumulated deltas, multiple or parallel tool calls, and Hermes-internal state transitions. The deterministic first-choice/first-tool consumer described below belongs to Breadstuffs' internal `dregg-agent` brain; it must not be silently treated as upstream Hermes semantics. A proof of any proper subset must report the subset, rather than collapse to one “verified provider” boolean.

There are therefore two useful but different targets:

- **Delegated request-policy conformance:** prove that the authorized/delegated subject permitted this destination, selected OpenRouter model, tool surface, user-input binding, limits, and attempt, and that the authenticated request obeyed those fields. This is narrower and can be valuable before upstream Hermes is made fully replayable.
- **Full construction and consumption:** additionally prove that upstream Hermes constructed every authenticated request from its complete committed state and consumed the authenticated response/event stream exactly according to its real execution semantics. A broker or TLSNotary wrapper alone does not prove arbitrary upstream Hermes execution.

## What the current verifier actually returns

**SOURCE-REVIEWED.** `VerifiedResponse` contains `response_body`, `server_name`, `connection_time`, and `sent_redacted` (`zkoracle-live/src/tlsn_live.rs:215-226`). Both genuine TLSNotary presentation verifiers retain those sent bytes: the fixture-root Messages verifier at `zkoracle-live/src/tlsn_live.rs:549-600`, and the Mozilla-root, pinned-notary real-host verifier at `zkoracle-live/src/tlsn_live.rs:814-875`.

The higher live zkOracle interface loses them. `TlsnLeg` and `TlsnHostLeg` both call `session_of`, which copies only server, time, and response body (`zkoracle-live/src/verify.rs:31-44,60-82`). `AuthenticSession` has no request field (`zkoracle-prove/src/authentic.rs:219-229`), and `VerifiedZkOracle` exposes only that session plus a provenance enum (`zkoracle-prove/src/attestation.rs:145-156`). The shared downstream legs consequently weld and parse only the response body (`zkoracle-prove/src/attestation.rs:500-549`).

The variants do not close the gap elsewhere:

- Generic portable verification returns only the UTF-8 response body (`zkoracle-live/src/endpoints/generic.rs:50-62`).
- GitHub and Coinbase producers preserve `sent_redacted` in an unsigned modeled envelope (`zkoracle-live/src/endpoints/github.rs:31-42,95-105`; `zkoracle-live/src/endpoints/price.rs:42-53,81-100`), but their genuine live verifier still goes through `TlsnHostLeg` and its request-dropping `session_of`.
- Bedrock has a stronger standalone verifier: it pins host, notary key, and a disclosed `/model/{model_id}/converse` target (`zkoracle-live/src/tlsn_bedrock.rs:300-397`). It still redacts the entire request body (`:271-287`). It is not the `MpcTlsLeg` used by `verify_zkoracle_live_host`; that generic leg invokes the Coinbase-shaped verifier and does not accept an expected model id (`zkoracle-live/src/verify.rs:55-73`). `attest_turn_bedrock` first runs the stronger verifier inside the producer, then packages the presentation (`deos-hermes/src/attest.rs:373-403`), while its third-party test verifies the package through generic `verify_zkoracle_live_host` (`deos-hermes/tests/narrator_model_provenance_live.rs:117-130`). A portable acceptance therefore does not itself recheck the Bedrock model target.
- The modeled presentation adapter signs both sent and received bytes, but verifies server/notary/signature/redaction and then returns only the response (`zkoracle-prove/src/authentic.rs:147-180,281-340`). Its fixture request has a method/path and headers but no request body (`zkoracle-prove/src/authentic.rs:414-477`). It cannot stand in for the missing provider-request relation.

There is also a rail-separation problem. The normal hosted Breadstuffs brains construct and consume provider requests directly; the attestation helpers are later, separate operations. `run_hosted_agent_attested` runs the brain and then builds a self-signed shaped response from `report.agent_text` (`deos-hermes/src/host.rs:371-407`; `deos-hermes/src/attest.rs:215-256`). `attest_turn_live` sends a caller-supplied prompt and reply to a local echo server (`deos-hermes/src/attest.rs:278-324`). `attest_turn_bedrock` does authenticate a real Bedrock response, but it is a standalone call and does not show that an agent loop consumed its extracted reply (`deos-hermes/src/attest.rs:366-403`). The in-tree provider callers return only parsed JSON to their brains with no evidence object (`deos-hermes/src/brain.rs:603-616,777-834`; `dregg-agent/src/brain.rs:673-717`). These call sites demonstrate the missing weld, but they are not the upstream Hermes provider protocol.

## Reuse and gap table

| Existing component | Reusable statement | Exact gap for hosted OpenRouter/Hermes |
|---|---|---|
| `/drive` subject/ACL gate | A verified upstream subject with Driver-or-higher may submit `{goal, tools}` (`agent-platform/src/serve.rs:72-80,349-364,601-615`; owner/ACL resolution at `agent-platform/src/lib.rs:680-692`). | The subject, role/delegation evidence, authorization decision, limits, and request bytes are not carried into `drive_live`; only host, goal, and tools continue (`agent-platform/src/serve.rs:618-625`; `agent-platform/src/lib.rs:975-1020`). There is no durable authorized-invocation object. |
| Breadstuffs OpenAI-compatible brain | The in-tree `dregg-agent` brain deterministically builds a request from model, ordered messages, advertised tools, and temperature (`dregg-agent/src/brain.rs:445-476,575-663`). OpenRouter is already a supported configurable base shape (`:498-519`). | This is reusable only if this internal brain is the execution target. The requested target is unmodified upstream Nous Hermes; its actual request constructor, streaming mode, state inputs, and retry behavior remain to identify. The current host key is also selected from process environment, not a per-user hosted key record (`agent-platform/src/lib.rs:975-995,1798-1804`). |
| Breadstuffs response consumer | The in-tree brain deterministically takes the first choice and first tool call, parses arguments, canonicalizes aliases, and maps it to an action (`dregg-agent/src/brain.rs:774-863,936-979`). | These are `dregg-agent` semantics, not evidence about upstream Hermes. Upstream Hermes may consume streaming deltas and multiple/parallel tool calls. Its actual consumer relation, ordering, and state update must be captured before a full execution claim is available. |
| TLSNotary transcript verifier | Genuine presentation verification, Web-PKI host pin, notary-key pin on the real-host path, authenticated response, and redacted sent view (`zkoracle-live/src/tlsn_live.rs:814-875`). | POST/OpenRouter path is not implemented. Current disclosures omit request bodies. `session_of` discards even the disclosed sent view. |
| Bedrock live path | A real POST path exists, with a durable notary option and an explicit model target pin (`zkoracle-live/src/tlsn_bedrock.rs:88-116,181-206,300-397,449-467`). | Request body remains hidden, and the model-target check is not part of the generic zkOracle live verifier used for portable acceptance. It is Bedrock/SigV4-specific, not OpenRouter/Bearer. |
| zkOracle response weld | Authenticated response bytes are committed, CFG-checked, and optionally checked by an injection STARK; splicing another response fails (`zkoracle-prove/src/attestation.rs:107-143,500-549`). | The weld starts at the response. It does not bind authorized input, constructed request, request transcript, response projection, or ensuing action. |
| JSON CFG certificate | `verify_cfg_compact` re-tokenizes the exact body and checks a complete leftmost derivation (`zkoracle-prove/src/cfg.rs:758-801`). | It proves one JSON body is syntactically JSON. All strings collapse to `JTok::Str` (`zkoracle-prove/src/cfg.rs:32-55,213-272`). It does not parse SSE framing or a stream of events/deltas, nor prove OpenRouter schema, selected-model reporting, field meaning, tool-call assembly, ordering, or parallel-call semantics. |
| Render attestation | `verify_render_reproducible` checks the committed template and rerenders from supplied data byte-for-byte (`zkoracle-prove/src/render.rs:310-325`). | `verify_render_attestation` alone ignores `template_commit` and proves only output commitment plus JSON well-formedness (`:287-308`). `render` concatenates hole bytes and only rejects `{{`; it is not a general JSON escaper (`:122-145`). Reuse the reproducibility relation or a typed serializer, not the weaker well-formed check. |
| Witnessed nondeterminism envelope | A request digest over endpoint and request JSON can be paired in order with the raw provider response, and replay detects request divergence (`dregg-agent/src/envelope.rs:96-122,197-210,599-678`). | The recorder asserts the response; it does not authenticate provider origin (`:19-39`). Product wiring and signed/root binding are explicitly not built (`:36-39,318-322`). It also excludes the key from identity. This is a good consumption/order skeleton after TLS evidence replaces the recorder assertion. |
| Attestation-to-turn commitment | `attestation_commitment` fingerprints the real presentation bytes and response-side evidence, and can be placed on a landed turn (`deos-hermes/src/attest.rs:66-127`). | Fingerprinting an opaque presentation does not prove the authorization/request/consumption relation. The modeled `presentation.sent` may be a separately constructed envelope rather than the real authenticated request. |
| Key handling | Provider keys are kept outside request bodies and Debug output; live transport places them in the Bearer header (`dregg-agent/src/brain.rs:109-190,205-217,326-389`). | `key_reached_provider` is a success-path boolean, set only after `complete` returns `Ok` (`dregg-agent/src/brain.rs:564-568,683-703`). A request may have left before a timeout/decode/error, and multiple calls collapse into one bit. TLS redaction proves secrecy of disclosed evidence, not which user's key/account was used or that the custodian used it nowhere else. |
| Notary operation | Durable, pinnable notary keys and host/notary verification machinery exist (`zkoracle-live/src/tlsn_bedrock.rs:449-467`). | Current live-host design documentation says the separate notary is still hosted by the prover's operator, not an independent public party (`docs/deos/ZKORACLE-ENDPOINTS.md:105-111`). The evidence contract needs an explicit notary identity/epoch and trust grade. |

## Minimal durable contract

### 1. `ProviderInvocationV1`

This is the authorization object, created before any provider traffic and signed or receipt-bound by the grain/authorization service.

Required fields:

- `invocation_id`, tenant/grain/session id, nonce, issue time, expiry;
- authenticated `subject_id`, authorization decision, role, and delegation/grant reference;
- exact user input bytes or a content commitment, plus the committed predecessor conversation/state root;
- permitted tools/caps, budget, maximum provider attempts, token/cost ceiling, and terminal deadline;
- gateway policy: scheme, host, port, method, path, exact selected OpenRouter model id, routing/provider constraints, streaming policy, sampling/inference parameters, system-prompt version, and tool-schema version;
- for the narrower policy-conformance tier, a `request_policy_id` describing the exact fields and constraints the verifier checks;
- for the full execution tier only, `constructor_id` and `consumer_id` identifying the actual upstream Hermes request constructor and response/event-stream consumer;
- opaque `key_id` owned by the authorizing user, with custody-policy version. Never the key or an unsalted raw-key hash.

For delegation, the authorization statement should mean “subject S may spend user U's hosted key `key_id` for this invocation under these limits,” rather than infer delegation from the fact that S had Driver role at some later verification time.

### 2. `ProviderAttemptV1`

One record per actual call, including calls produced by unknown-tool retries or subsequent reason/act/observe steps.

Required fields:

- `invocation_id`, monotonically increasing `attempt_no`, predecessor state root, and an internal attempt nonce;
- exact canonical request bytes, or both the bytes and their domain-separated digest; method/path/host and all non-secret headers;
- at the policy tier, `request_policy_id` plus the field-by-field conformance result; at the full tier, `constructor_id` and reproducibility evidence showing those bytes equal `Construct_v(invocation, predecessor_state)`;
- TLSNotary presentation bytes, pinned notary key id/epoch, authenticated gateway host, session time, HTTP status, authenticated sent view, and authenticated received bytes;
- response bytes/digest and a pinned protocol profile: either one non-streaming JSON response or an authenticated SSE event sequence with framing, ordering, termination, and delta assembly checked before any JSON/schema claim;
- where applicable, JSON `CompactCert` objects for the actual JSON messages/events plus a strict OpenRouter schema result; the body-level CFG alone is insufficient for SSE;
- for full execution evidence, `consumer_id`, every consumed response span/event, assembled message, all selected tool calls (including multiple/parallel calls and their ordering), normalized consumed values, and their digests;
- disposition: `consumed`, `rejected_before_consumption`, `transport_failed`, or `ambiguous_after_send`; for `consumed`, the exact successor action/finish and the receipt/envelope/turn hash that used it;
- a signed custody event naming `key_id`, attempt number, endpoint, request digest, start time, and outcome class.

The durable root must be committed into the same signed/landed record that commits the resulting action. An unattached proof file and a separately attested agent message are insufficient. At the narrower policy tier, this binds authorization to the authenticated request/response and records what was handed toward Hermes; it still does not prove how arbitrary upstream Hermes consumed it.

### 3. Disclosure policy for the first hosted version

The minimal implementable policy is to reveal the complete request body, method/path, and non-secret headers to the authorized verifier, while redacting only the `Authorization: Bearer …` value. That supports direct delegated-policy checks immediately and makes byte equality with a deterministic constructor checkable once upstream Hermes's actual constructor relation is identified.

If prompts must be hidden from the verifier, a new relation is required: equality between a commitment to the authorized/constructed request and the hidden TLS transcript bytes. The current code has no such proof. A response CFG certificate or a hash stored beside a redacted transcript cannot establish that equality by itself.

The existing secret checks are endpoint-specific placeholder searches (`VerifiedResponse::api_key_hidden`, `zkoracle-live/src/tlsn_live.rs:228-233`; modeled check at `zkoracle-prove/src/authentic.rs:320-329`). For an arbitrary user OpenRouter key, the proof must instead establish which header positions were withheld and that the header name/scheme were disclosed. It must not claim that the same secret did not occur elsewhere unless that is separately checked under custody.

## Failures, retries, and custody consequences

**Retries are new attempts.** The in-tree `dregg-agent` illustrates why: it may make many provider calls across steps and up to four immediate calls when its own parser sees an unknown tool (`dregg-agent/src/brain.rs:673-717`). This does not define upstream Hermes retry behavior. Whatever upstream Hermes actually does, each network call gets a new `attempt_no`, request, transcript/effect record, cost status, and disposition. Never overwrite or collapse attempts. At the full tier, each state transition identifies the exact response/event sequence it consumed; earlier failures and rejected parses remain in the ordered chain.

**Timeout after send is ambiguous.** It may have reached or charged the gateway even when no usable response returns. The current success-only `key_reached_provider` bit cannot account for this. Record `ambiguous_after_send`, do not assert “key unused,” and count it against retry/cost limits until provider-side evidence resolves it.

**Evidence failure limits the grade.** If the TLSNotary presentation is absent, the host/notary pin fails, or request-policy conformance fails, the attempt cannot receive even the policy-conformant transport grade. If full request equality, protocol/schema handling, or the Hermes consumption link is absent, it cannot receive the full construction/consumption grade. A product may expose an explicitly lower-grade fallback, but it must not reuse a stronger verified bit.

**Hosted custody is acceptable but changes the claim.** Store each user token encrypted under a custody service, address it by opaque `key_id`, restrict decryption/use to the provider-call worker, support rotation/revocation, and issue an append-only signed custody event for every attempted use. TLSNotary can show that a secret Authorization value was withheld in a session; it cannot show which account/key value it was, nor prove the custodian never used it in another session. Sole egress plus a signed append-only log strengthens operational accounting under the host/custodian trust assumption. It is not cryptographic proof of complete key use against a dishonest custodian unless independent enforcement makes bypass or omitted log entries detectable, such as a separately controlled egress boundary, hardware-backed enforcement, or provider-side audit evidence. Until then, report “custodian-recorded use of key slot `key_id` for this attempt,” not “the key was used only here” or “all uses are accounted for.”

## Assurance boundaries

These claims must remain separate:

1. **TLS provenance:** a presentation under a pinned notary and Web-PKI policy authenticates a session with the gateway host and the disclosed request/response bytes. This is the strongest current reusable transport claim.
2. **Syntax:** the authenticated response is JSON. The current CFG certificate establishes this and no provider semantics.
3. **Delegated request-policy conformance:** the authenticated request stayed within the authorized destination, selected OpenRouter model, tools, input binding, attempt, and limits. This narrower relation does not prove that upstream Hermes deterministically constructed every byte from its entire state.
4. **Full authorized construction:** the exact authenticated request bytes equal the actual versioned upstream Hermes constructor applied to authorized input and complete committed Hermes state. This stronger relation remains to identify.
5. **Provider/model statement:** a pinned OpenRouter host returned the authenticated bytes for a request naming the selected OpenRouter model and routing policy. Hermes is the agent, not the model id. This does not prove that particular weights executed correctly, that the gateway's upstream routing report is truthful, or that inference was mathematically correct. TLS to a gateway authenticates the gateway, not an unseen upstream model operator.
6. **Hermes semantic consumption:** the actual upstream Hermes consumer assembled and consumed this exact authenticated response or SSE event sequence, including all multiple/parallel tool calls, and this exact result drove its next state/action. The deterministic in-tree first-choice/first-tool parser is not a substitute for this relation.
7. **Key-use accounting:** the custodian says it used user key slot `key_id` for each logged attempt. TLS redaction protects the secret; it does not supply complete account-level accounting or exclusivity.

A future STARK can strengthen an identified upstream Hermes construction/consumption relation, strict protocol/schema parsing, response projection, and local state transition after those relations are implemented and exercised against real provider traffic. A broker-side proof can establish only the broker's own request-policy and transcript handling unless it is cryptographically joined to Hermes's actual state transition. It cannot turn TLS gateway provenance into proof of opaque model-weight execution, and it should not replace or weaken existing provenance, CFG, injection, cap, budget, or receipt guards.

## Design decisions to make now

1. **Place evidence on upstream Hermes's actual provider boundary.** The OpenRouter/TLSNotary interposition must capture the exact request and response/event stream used by the same upstream Hermes invocation. It must expose durable attempt evidence and a consumption link from Hermes; a broker returning evidence beside bytes proves only broker handling until Hermes acknowledges and binds what it consumed. Do not attest a reconstructed `agent_text` after the fact and do not make a second model call for attestation.
2. **Adopt an explicit v1 disclosure boundary.** Reveal the exact OpenRouter request body to the authorized verifier and redact only the Bearer value. Defer private-prompt public proofs until a real hidden-transcript equality relation exists.
3. **Pin the policy tier now; identify Hermes semantics before claiming the full tier.** Freeze the OpenRouter endpoint, selected model/routing policy, permitted tools, input binding, streaming policy, and limits under `request_policy_id`. Then identify and version upstream Hermes's real serialization, SSE/delta handling, multiple/parallel-tool behavior, retries, state inputs, and error semantics before assigning `constructor_id`/`consumer_id` or claiming deterministic construction/consumption.
4. **Treat every network call as an ordered attempt.** Bind authorization, request, TLS transcript, response, parser result, custody event, and the one consumed successor action under `invocation_id + attempt_no`; record ambiguous failures and retries instead of summarizing them.
5. **Name custody and notary trust explicitly.** Use encrypted per-user hosted keys with opaque ids and a signed append-only attempt log. Pin a durable notary key/epoch; prefer an independently operated notary, or label an operator-run notary as such. Treat sole egress and signed logs as operational accountability under host trust; do not advertise cryptographically complete key-use accounting without independent enforcement that detects bypass and omission.

## Prior evidence record

**VERIFIED only as a dated run record, not re-run here.** The August reproduction executed 86 tests at commit `436c2a865a0a0e6b8222050ef27464750a0471d7` (`../degg-research/docs/research/ATTESTATION_SUITE_RERUN_2026-08-19.md:95-110,298-303`). Its six “model provenance fused” tests used `FixtureNotary` and an in-process TLSNotary server and performed no external network I/O; “live” meant the real MPC-TLS 2PC code path, not a third-party model provider (`:160-182`). The external Bedrock tests were deliberately excluded and ignored (`:256-263`). That record supports the local cryptographic plumbing and refusal tests. It does not support a claim that OpenRouter, Nous Hermes, or any actual hosted model request was authenticated or consumed.
