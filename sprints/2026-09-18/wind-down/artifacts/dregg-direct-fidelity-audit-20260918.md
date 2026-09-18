# Direct FFI fidelity audit, 2026-09-18

Evidence is source inspection unless an actual runtime artifact is explicitly named. Root authorized the credential-width repair; the runtime lane owns build.rs, initialization, native tests, and all remote compilation. This lane has not run Cargo or Lean.

## Nine credential coordinates lose their upper 192 bits

Before repair, dregg-lean-ffi/src/lean_direct.rs build_auth_w calls seven credential exports with digest_low(d), exactly bytes24..32 of the32-byte digest interpreted as u64. The affected fields are Signature.pubkey, Proof.vk, Bearer.deleg_msg, CapTpDelivered.intro_msg, CapTpDelivered.sender_msg, Custom.kind_stmt, Stealth.one_time_pk, Stealth.ephemeral_pk, and Token.issuer_key. Recursive OneOf calls the same builder. Actual metatheory/Dregg2/Exec/FFIDirect.lean exports accept UInt64 for those fields, and the existing generated C agrees with those narrow signatures.

The JSON input path does not narrow these fields: marshal Digest is32 bytes and to_hex32_bytes emits all64 digits; FFI.lean encodeAuthW/parseAuthW preserve the digest Nat, and liftAuthW maps it via Int.ofNat. FullForestAuth.portalVerify consumes eight of these coordinates. Its stealth arm intentionally ignores ephemeral_pk. The Crypto.Reference verifier compares statement and proof as Int: accepted fixture coverage establishes transport/executor behavior under that reference implementation, not real cryptographic security.

The receiving production consumer exec-lean/src/lean_shadow.rs run_shadow_state prefers direct execution without credential-width screening. Its auth_to_wire builds full Digest::from_bytes for proof/bearer/CapTp/custom/stealth/token. Contextual Signature production already explicitly normalizes to low64, a separate producer behavior. exec-lean/src/lean_apply.rs consumes run_shadow_state output through wire_state_to_ledger. Thus this is a production carrier mismatch, not only an uncalled FFI API.

Repair staged in `/tmp/dregg-direct-auth-width-20260918/`: seven renamed `_w` exports take four low-first limbs per digest. Lean composes them using the existing natOfLimbs used by receipt-chain heads. Rust uses the existing WideInt byte-to-limb projection. No Rust executor semantics are added. Old narrow exports have no outside consumers in the source inventory and are removed. Seven generalized lift equalities pin all nine fields; a high-limb inequality proves a nonzero upper limb cannot fit any UInt64. All have ordinary #assert_axioms pins. A canonical encodeAuthW export with its defining equality enables native transport checks of the ignored ephemeral key as well. At staging time these changes are not compiled or applied to the shared tree.

## Standing corpus does not exercise admitted execution

marshal::conformance_input_corpus contains49 cases (12 auth,30 action,7 structural). Every conf_turn_of/conf_turn_bh sets previous receipt to0xDEADBEEF. Host stored_head is0 for diag and4 for conf_host_populated. Admission.lean requires exact prevReceipt=storedHead, so these cases cannot reach successful body execution; other gates may reject even earlier. Every all_auths_demo digest is Digest::from_u64. Passing this corpus therefore cannot establish accepted-path parity or high-bit credential fidelity. Runtime is preserving the corpus and adding actual admitted transfers, high-bit mutations, recursive OneOf, and native credential serialization through production build_auth_w.

## Escrows, queues, and swiss are intentionally erased in both paths

FFI.lean stateOfWState explicitly drops retired escrows/queues/swiss; wstateOfState emits empty lists. FFIDirect.mkWState and Rust build_state/read_post_state match that canonical projection. Rejected branches also project through wstateOfState in both executors. Matching empty tables are not evidence that one path dropped live authority. The other nine state fields are built/read: cells,caps,bal,nullifiers,commitments,revoked,lifecycle,deathCert,delegate. All host fields are constructed; receipt heads already cross in four limbs.

## Additional bounded residuals, no changes authorized here

* direct mk_string uses CString::new(s).unwrap_or_default(), silently replacing a NUL-containing field name by the empty string; JSON lean_string_bridge instead rejects interior NUL. Production field-name mapping appears fixed ASCII. No reachable production exploit or native mismatch is claimed.
* marshal::Parser.string pushes each raw UTF-8 byte as a char, corrupting non-ASCII output names; direct read_owned_string uses UTF-8 decoding. This is a JSON Rust-decoder defect. Existing corpus string stress is escaped ASCII.
* direct read_owned_wide reads four modulo limbs with no check for magnitude>=2^256, whereas JSON Parser.wide refuses values beyond that carrier. No reachable executor-produced overflow witness has been established. Similar UInt64 Nat projections need an output-bound argument when values can grow.
* WireValue::Dig(u64) and JSON Parser.hex32 share low64 truncation. This is a shared carrier limitation, not a direct-only discrepancy; ordinary production state fields use full-width Int.
* JSON unmarshal_result rejects the empty-state malformed-wire sentinel whereas direct can return a rejected empty state. Whether a supported production input hits this difference has not been established.
