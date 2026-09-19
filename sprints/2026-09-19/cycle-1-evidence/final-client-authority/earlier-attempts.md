# Earlier authority-client attempts (not PASS)

- `/tmp/minidregg-cycle-20260919/authority-client-run-20260919T213200Z`
  ended nonzero after 169.94 seconds. Its test expected Alice's forbidden
  mutation to fail before a call was signed; the host actually assembled the
  signed call and returned a canonical admission refusal. The script's
  assertion, not admission, was wrong. No final PASS is claimed from it.
- `/tmp/minidregg-cycle-20260919/authority-client-run2-20260919T213700Z`
  ended nonzero after 466.59 seconds. Its test made the same early-refusal
  assumption for Bob's policy-management attempt. The host again returned a
  fully signed admission refusal. A focused continuation on that partial
  fixture separately confirmed revocation, Bob's fresh read/invoke refusals,
  and original-call retry; it was not a complete script PASS.
- `/tmp/minidregg-cycle-20260919/authority-client-final-20260919T215242Z`
  was intentionally interrupted with exit 143 after 78.31 seconds, after
  birth and during the subsequent install challenge. Review found that the
  script's post-revocation `create` targeted already-present neutral field 1,
  so refusal could have had an unrelated cause. The untouched frozen script
  copy was not reused. The canonical script was corrected to absent field 2,
  refrozen with SHA-256 `ff060ce20410c7c31539a855e0c17f1f9beb5b7e937c2089fe3129f809abff50`,
  and run from a fresh deployment. Only that final2 run is marked PASS.
