from pathlib import Path
import json, hashlib, difflib
root = Path('/Users/ember/dev/breadstuffs')
stage = Path('/tmp/dregg-direct-auth-width-20260918')
lean_path = 'metatheory/Dregg2/Exec/FFIDirect.lean'
rust_path = 'dregg-lean-ffi/src/lean_direct.rs'
lean = (root/lean_path).read_text()
rust = (root/rust_path).read_text()
helper_start = lean.index('/-- **THE FULL-WIDTH DIGEST CARRIER.')
helper_end = lean.index('/-- ⚑ **THE HEAD CROSSES WHOLE', helper_start)
old_helper = lean[helper_start:helper_end]
new_helper = '''/-- Four low-first 64-bit limbs compose a full-width unsigned digest. Receipt-chain heads and
credential digests share this carrier. Composition stays in Lean; the C caller supplies limbs.
The helper is unexported because callers use the typed builders below. -/
def natOfLimbs (l0 l1 l2 l3 : UInt64) : Nat :=
  l0.toNat + (l1.toNat <<< 64) + (l2.toNat <<< 128) + (l3.toNat <<< 192)

/-- A nonzero upper limb cannot collapse to any 64-bit digest. -/
theorem natOfLimbs_high_limbs_do_not_fit_u64 (l0 l1 l2 l3 n : UInt64)
    (h : 0 < l1.toNat ∨ 0 < l2.toNat ∨ 0 < l3.toNat) :
    natOfLimbs l0 l1 l2 l3 ≠ n.toNat := by
  have hn : n.toNat < 2 ^ 64 := n.toNat_lt
  simp only [natOfLimbs, Nat.shiftLeft_eq]
  omega

#assert_axioms natOfLimbs_high_limbs_do_not_fit_u64

'''
auth_start = lean.index('/-! ## `AuthW` builders')
auth_end = lean.index('/-! ## `WCaveat` builders', auth_start)
old_auth = lean[auth_start:auth_end]
new_auth = '''/-! ## `AuthW` builders (`Authorization Nat Nat`, 10 ctors; `oneOf` recurses).

Every digest coordinate crosses as four low-first limbs, matching the full 256-bit JSON carrier.
Proof blobs, token identifiers, action/resource bindings, and candidate indices retain their
existing `UInt64` carrier. The `_w` names distinguish these signatures from the retired narrow ABI. -/

@[export dregg_d_auth_signature_w]
def authSignatureW (pk0 pk1 pk2 pk3 sig : UInt64) : AuthW :=
  .signature (natOfLimbs pk0 pk1 pk2 pk3) sig.toNat
@[export dregg_d_auth_proof_w]
def authProofW (vk0 vk1 vk2 vk3 pf ba br : UInt64) : AuthW :=
  .proof (natOfLimbs vk0 vk1 vk2 vk3) pf.toNat ba.toNat br.toNat
@[export dregg_d_auth_breadstuff] def authBreadstuff (tok : UInt64) : AuthW := .breadstuff tok.toNat
@[export dregg_d_auth_bearer_w]
def authBearerW (dm0 dm1 dm2 dm3 ds : UInt64) (stark : Bool) : AuthW :=
  .bearer (natOfLimbs dm0 dm1 dm2 dm3) ds.toNat stark
@[export dregg_d_auth_unchecked] def authUnchecked : AuthW := .unchecked
@[export dregg_d_auth_captp_w]
def authCapTpW (im0 im1 im2 im3 sm0 sm1 sm2 sm3 isig ss : UInt64) : AuthW :=
  .capTpDelivered (natOfLimbs im0 im1 im2 im3) (natOfLimbs sm0 sm1 sm2 sm3) isig.toNat ss.toNat
@[export dregg_d_auth_custom_w]
def authCustomW (st0 st1 st2 st3 pf : UInt64) : AuthW :=
  .custom (natOfLimbs st0 st1 st2 st3) pf.toNat
@[export dregg_d_auth_oneof]
def authOneOf (cands : List AuthW) (i : UInt64) : AuthW := .oneOf cands i.toNat
@[export dregg_d_auth_stealth_w]
def authStealthW (otp0 otp1 otp2 otp3 eph0 eph1 eph2 eph3 sig : UInt64) : AuthW :=
  .stealth (natOfLimbs otp0 otp1 otp2 otp3) (natOfLimbs eph0 eph1 eph2 eph3) sig.toNat
@[export dregg_d_auth_token_w]
def authTokenW (key0 key1 key2 key3 sig : UInt64) : AuthW :=
  .token (natOfLimbs key0 key1 key2 key3) sig.toNat

/-- The executor receives every digest coordinate at its full width, including the ephemeral key
that the current reference stealth verifier does not inspect. These equalities hold for all limbs. -/
theorem lift_authSignatureW (pk0 pk1 pk2 pk3 sig : UInt64) :
    liftAuthW (authSignatureW pk0 pk1 pk2 pk3 sig) =
      .signature (Int.ofNat (natOfLimbs pk0 pk1 pk2 pk3)) (Int.ofNat sig.toNat) := rfl

theorem lift_authProofW (vk0 vk1 vk2 vk3 pf ba br : UInt64) :
    liftAuthW (authProofW vk0 vk1 vk2 vk3 pf ba br) =
      .proof (Int.ofNat (natOfLimbs vk0 vk1 vk2 vk3)) (Int.ofNat pf.toNat) ba.toNat br.toNat := rfl

theorem lift_authBearerW (dm0 dm1 dm2 dm3 ds : UInt64) (stark : Bool) :
    liftAuthW (authBearerW dm0 dm1 dm2 dm3 ds stark) =
      .bearer (Int.ofNat (natOfLimbs dm0 dm1 dm2 dm3)) (Int.ofNat ds.toNat) stark := rfl

theorem lift_authCapTpW (im0 im1 im2 im3 sm0 sm1 sm2 sm3 isig ss : UInt64) :
    liftAuthW (authCapTpW im0 im1 im2 im3 sm0 sm1 sm2 sm3 isig ss) =
      .capTpDelivered (Int.ofNat (natOfLimbs im0 im1 im2 im3))
        (Int.ofNat (natOfLimbs sm0 sm1 sm2 sm3)) (Int.ofNat isig.toNat) (Int.ofNat ss.toNat) := rfl

theorem lift_authCustomW (st0 st1 st2 st3 pf : UInt64) :
    liftAuthW (authCustomW st0 st1 st2 st3 pf) =
      .custom (Int.ofNat (natOfLimbs st0 st1 st2 st3)) (Int.ofNat pf.toNat) := rfl

theorem lift_authStealthW (otp0 otp1 otp2 otp3 eph0 eph1 eph2 eph3 sig : UInt64) :
    liftAuthW (authStealthW otp0 otp1 otp2 otp3 eph0 eph1 eph2 eph3 sig) =
      .stealth (Int.ofNat (natOfLimbs otp0 otp1 otp2 otp3))
        (Int.ofNat (natOfLimbs eph0 eph1 eph2 eph3)) (Int.ofNat sig.toNat) := rfl

theorem lift_authTokenW (key0 key1 key2 key3 sig : UInt64) :
    liftAuthW (authTokenW key0 key1 key2 key3 sig) =
      .token (Int.ofNat (natOfLimbs key0 key1 key2 key3)) (Int.ofNat sig.toNat) := rfl

#assert_axioms lift_authSignatureW
#assert_axioms lift_authProofW
#assert_axioms lift_authBearerW
#assert_axioms lift_authCapTpW
#assert_axioms lift_authCustomW
#assert_axioms lift_authStealthW
#assert_axioms lift_authTokenW

/-- Test support for inspecting the actual credential built by the native caller through the
existing canonical encoder. Execution itself still passes objects directly. -/
@[export dregg_d_auth_encode_w]
def authEncodeW (auth : AuthW) : String := encodeAuthW auth

theorem authEncodeW_eq (auth : AuthW) : authEncodeW auth = encodeAuthW auth := rfl
#assert_axioms authEncodeW_eq

@[export dregg_d_authwlist_nil]  def authWListNil : List AuthW := []
@[export dregg_d_authwlist_cons] def authWListCons (x : AuthW) (xs : List AuthW) : List AuthW := x :: xs

'''
new_lean = lean.replace(old_helper, '').replace(old_auth, new_helper + new_auth)
ext_start = rust.index('        fn dregg_d_auth_signature(')
ext_end = rust.index('        static dregg_d_authwlist_nil:', ext_start)
old_ext = rust[ext_start:ext_end]
new_ext = '''        fn dregg_d_auth_signature_w(pk0: u64, pk1: u64, pk2: u64, pk3: u64, sig: u64) -> Obj;
        fn dregg_d_auth_proof_w(
            vk0: u64, vk1: u64, vk2: u64, vk3: u64, pf: u64, ba: u64, br: u64,
        ) -> Obj;
        fn dregg_d_auth_breadstuff(tok: u64) -> Obj;
        fn dregg_d_auth_bearer_w(dm0: u64, dm1: u64, dm2: u64, dm3: u64, ds: u64, stark: u8) -> Obj;
        static dregg_d_auth_unchecked: Obj;
        fn dregg_d_auth_captp_w(
            im0: u64, im1: u64, im2: u64, im3: u64,
            sm0: u64, sm1: u64, sm2: u64, sm3: u64, isig: u64, ss: u64,
        ) -> Obj;
        fn dregg_d_auth_custom_w(st0: u64, st1: u64, st2: u64, st3: u64, pf: u64) -> Obj;
        fn dregg_d_auth_oneof(cands: Obj, i: u64) -> Obj;
        fn dregg_d_auth_stealth_w(
            otp0: u64, otp1: u64, otp2: u64, otp3: u64,
            eph0: u64, eph1: u64, eph2: u64, eph3: u64, sig: u64,
        ) -> Obj;
        fn dregg_d_auth_token_w(key0: u64, key1: u64, key2: u64, key3: u64, sig: u64) -> Obj;
        #[cfg(test)]
        fn dregg_d_auth_encode_w(auth: Obj) -> Obj;
'''
builder_start = rust.index('    unsafe fn build_auth_w(')
builder_end = rust.index('    unsafe fn build_caveat_list(', builder_start)
old_builder = rust[builder_start:builder_end]
new_builder = '''    unsafe fn build_auth_w(a: &WireAuth) -> Obj {
        match a {
            WireAuth::Signature { pubkey, sig } => {
                let [pk0, pk1, pk2, pk3] = digest_limbs(pubkey);
                dregg_d_auth_signature_w(pk0, pk1, pk2, pk3, *sig)
            }
            WireAuth::Proof {
                vk,
                proof,
                bound_action,
                bound_resource,
            } => {
                let [vk0, vk1, vk2, vk3] = digest_limbs(vk);
                dregg_d_auth_proof_w(vk0, vk1, vk2, vk3, *proof, *bound_action, *bound_resource)
            }
            WireAuth::Breadstuff { token } => dregg_d_auth_breadstuff(*token),
            WireAuth::Bearer {
                deleg_msg,
                deleg_sig,
                stark,
            } => {
                let [dm0, dm1, dm2, dm3] = digest_limbs(deleg_msg);
                dregg_d_auth_bearer_w(dm0, dm1, dm2, dm3, *deleg_sig, *stark as u8)
            }
            WireAuth::Unchecked => dregg_d_auth_unchecked,
            WireAuth::CapTpDelivered {
                intro_msg,
                sender_msg,
                intro_sig,
                sender_sig,
            } => {
                let [im0, im1, im2, im3] = digest_limbs(intro_msg);
                let [sm0, sm1, sm2, sm3] = digest_limbs(sender_msg);
                dregg_d_auth_captp_w(
                    im0, im1, im2, im3, sm0, sm1, sm2, sm3, *intro_sig, *sender_sig,
                )
            }
            WireAuth::Custom { kind_stmt, proof } => {
                let [st0, st1, st2, st3] = digest_limbs(kind_stmt);
                dregg_d_auth_custom_w(st0, st1, st2, st3, *proof)
            }
            WireAuth::OneOf {
                candidates,
                proof_index,
            } => {
                let mut acc = dregg_d_authwlist_nil;
                for c in candidates.iter().rev() {
                    acc = dregg_d_authwlist_cons(build_auth_w(c), acc);
                }
                dregg_d_auth_oneof(acc, *proof_index)
            }
            WireAuth::Stealth {
                one_time_pk,
                ephemeral_pk,
                sig,
            } => {
                let [otp0, otp1, otp2, otp3] = digest_limbs(one_time_pk);
                let [eph0, eph1, eph2, eph3] = digest_limbs(ephemeral_pk);
                dregg_d_auth_stealth_w(otp0, otp1, otp2, otp3, eph0, eph1, eph2, eph3, *sig)
            }
            WireAuth::Token { issuer_key, sig } => {
                let [key0, key1, key2, key3] = digest_limbs(issuer_key);
                dregg_d_auth_token_w(key0, key1, key2, key3, *sig)
            }
        }
    }

    /// Full 256-bit digest as low-first limbs; Lean composes the same `Nat` as the JSON codec.
    fn digest_limbs(d: &crate::marshal::Digest) -> [u64; 4] {
        crate::marshal::WideInt::from_be_bytes32(d.0).limbs_le()
    }

'''
new_rust = rust.replace(old_ext,new_ext).replace(old_builder,new_builder)
replacements = [dict(path=lean_path,old=old_helper,new=''),dict(path=lean_path,old=old_auth,new=new_helper+new_auth),dict(path=rust_path,old=old_ext,new=new_ext),dict(path=rust_path,old=old_builder,new=new_builder)]
(stage/'replacements.json').write_text(json.dumps(replacements,indent=2)+'\n')
for name,old,new in [('FFIDirect.lean',lean,new_lean),('lean_direct.rs',rust,new_rust)]:
 (stage/(name+'.before')).write_text(old)
 (stage/name).write_text(new)
 (stage/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+'.before',tofile=name)))
print(json.dumps({'scratch':str(stage),'shared_source_modified':False,'exports':[ 'dregg_d_auth_'+x+'_w' for x in ['signature','proof','bearer','captp','custom','stealth','token','encode'] ],'lean_sha256':hashlib.sha256(new_lean.encode()).hexdigest(),'rust_sha256':hashlib.sha256(new_rust.encode()).hexdigest()},indent=2))
