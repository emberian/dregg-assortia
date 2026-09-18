# Wire-string parser draft handoff (2026-09-18)

Status: **staged in `/tmp`, incomplete wave, unbuilt and untested**. Nothing in the shared
workspace was edited. No Cargo command, Lean command, native lane, hbox job, branch, worktree,
stash, or commit was used. The only executable check was `rustfmt --edition 2021 --check` against
the scratch copy; it passed after the draft was formatted.

## Frozen artifacts

- Apply-patch draft: `/tmp/marshal-string.patch`
  - SHA-256: `3f2d5a1acc8c88d9522211b470a8bdcc270f55902f5eba93fcd51fa40097d6f3`
- Full scratch result for inspection only:
  `/tmp/resume_wire_strings/dregg-lean-ffi/src/marshal.rs`
  - SHA-256: `5d2a298cbdbd6bda13ad35c7a78eeb6bec4c4f406c2b77d5364126a0976148f4`
  - Do not copy this whole file over a moving shared tree; apply/rebase the narrow regions.

## Baseline source hashes

- `dregg-lean-ffi/src/marshal.rs`
  `bf14de3d55cb375841cc6eb1de3ee4096e0504502eb65cdf084244add4eb0a4a`
- `dregg-lean-ffi/src/lean_direct.rs`
  `036e74fe624c2763082c0c20ecdc0d64e0c0e3046280a22b6d7e89363e81b91a`
- `metatheory/Dregg2/Exec/FFI.lean`
  `8a76f85582318d61e57f6b6b10a6ab743de02e6357ae9b642d0ba01c63cf4a62`
- `metatheory/Dregg2/Exec/FFI/Narrow.lean`
  `5ed6d20abf4e3b8775f3820c38b549881a62e7e3d2cef76bab3f7188b128f81c`

## Completed draft scope

The `marshal.rs` draft repairs `Parser::string` so raw UTF-8 advances by one Unicode scalar
instead of casting each byte to `char`. It adds strict standard JSON escapes (`\"`, `\\`, `\/`,
`\b`, `\f`, `\n`, `\r`, `\t`, `\uXXXX`), combines valid UTF-16 surrogate pairs, and rejects
unescaped control bytes, bad/short escapes, lone surrogates, and unterminated strings.

Three same-file unit tests cover:

1. Raw `café 猫 🧁` plus the existing quote/backslash wire escapes.
2. Solidus and control escapes, BMP `\u03bb`, and astral `\uD83E\uDDC1`.
3. `\x`, non-hex/short `\u`, high-without-low, high-plus-non-low, lone-low, raw newline,
   missing closing quote, and trailing backslash rejection.

The tests call the actual private parser and require EOF. They were **not run**.

## Incomplete/deferred scope

- No end-to-end `unmarshal_result` Unicode-field test was added. The direct parser test catches
  the reported byte-cast defect, but a future continuation should add one real output-envelope
  case as integration coverage.
- Root later approved escaping U+0000–U+001F in both JSON producers, then the user wound the wave
  down before that edit started. `marshal.rs::push_json_escaped` still escapes only quote and
  backslash. The Lean function named `jsonEscape` actually lives in
  `metatheory/Dregg2/Exec/FFI/Narrow.lean`; wide call sites are in `FFI.lean` at the record-field
  and `setfield` encoders. No Lean/Rust producer changes or named Lean theorem/axiom pins were
  drafted.
- The Lean parser still accepts only quote/backslash escapes. This Rust draft can decode a strict
  JSON superset, including surrogate escapes; producer/parser parity across both languages remains
  future work.

## Separate direct-boundary finding (reported, not edited)

At the baseline, `lean_direct.rs:315-317` uses
`CString::new(s).unwrap_or_default()`. Any interior-NUL string is silently replaced with an empty
CString, creating a semantic collision with the empty field name.

Exact consumers are:

- recursive `WireValue::Record` field names in `WireState`, through `build_value` and
  `dregg_d_fieldlist_cons` (`lean_direct.rs:384-394`);
- every `WireAction::SetField.field` in the recursive `WForest`, through `build_action` and
  `dregg_d_act_setfield` (`lean_direct.rs:472-505`), including `Exercise` inner actions and child
  forests.

The correct fallible boundary is a complete recursive preflight before any Lean object is built or
consumed in `run_direct`/`run_direct_profiled`, plus the state-only identity measurement path.
Threading a late `CString` error through consuming builders risks leaking already-created Lean
objects. Runtime/root subsequently selected length-aware direct string transport instead; that
implementation remained proposed/unimplemented at wind-down.

## Intended future validation

After rebasing the narrow patch on the then-current sources, the requested native-lane filter was:

`cargo nextest run -p dregg-lean-ffi -E 'test(/json_string_parser_tests/)'`

Also run the existing `marshal_conformance` target and any new end-to-end Unicode envelope test.
These are instructions only; no validation was launched in this task.
