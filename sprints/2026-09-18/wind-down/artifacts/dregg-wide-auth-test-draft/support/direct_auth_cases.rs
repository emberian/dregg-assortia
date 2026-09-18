// Credential transport fixtures for the existing Crypto.Reference echo portal.
// They do not represent real signatures or establish cryptographic soundness.
use dregg_lean_ffi::marshal::{Digest, WireAuth};

pub struct AuthCase {
    pub name: &'static str,
    pub valid: WireAuth,
    pub altered: WireAuth,
    /// The existing portal does not consume stealth's ephemeral key.
    pub mutation_refuses: bool,
}

fn alter(digest: &mut Digest) {
    digest.0[0] = 0xd1;
    digest.0[8] = 0xb2;
    digest.0[16] = 0xa3;
}

pub fn cases() -> Vec<AuthCase> {
    let mut out = Vec::new();
    let mut add = |name, valid: WireAuth, mutation: fn(&mut WireAuth), mutation_refuses| {
        let mut altered = valid.clone();
        mutation(&mut altered);
        assert_ne!(
            valid, altered,
            "fixture mutation must change its named coordinate"
        );
        out.push(AuthCase {
            name,
            valid,
            altered,
            mutation_refuses,
        });
    };
    add(
        "signature.pubkey",
        WireAuth::Signature {
            pubkey: Digest::from_u64(7),
            sig: 7,
        },
        |a| {
            if let WireAuth::Signature { pubkey, .. } = a {
                alter(pubkey)
            }
        },
        true,
    );
    add(
        "proof.vk",
        WireAuth::Proof {
            vk: Digest::from_u64(7),
            proof: 7,
            bound_action: 0,
            bound_resource: 0,
        },
        |a| {
            if let WireAuth::Proof { vk, .. } = a {
                alter(vk)
            }
        },
        true,
    );
    add(
        "bearer.deleg_msg",
        WireAuth::Bearer {
            deleg_msg: Digest::from_u64(7),
            deleg_sig: 7,
            stark: true,
        },
        |a| {
            if let WireAuth::Bearer { deleg_msg, .. } = a {
                alter(deleg_msg)
            }
        },
        true,
    );
    let captp = WireAuth::CapTpDelivered {
        intro_msg: Digest::from_u64(7),
        sender_msg: Digest::from_u64(11),
        intro_sig: 7,
        sender_sig: 11,
    };
    add(
        "captp.intro_msg",
        captp.clone(),
        |a| {
            if let WireAuth::CapTpDelivered { intro_msg, .. } = a {
                alter(intro_msg)
            }
        },
        true,
    );
    add(
        "captp.sender_msg",
        captp,
        |a| {
            if let WireAuth::CapTpDelivered { sender_msg, .. } = a {
                alter(sender_msg)
            }
        },
        true,
    );
    add(
        "custom.kind_stmt",
        WireAuth::Custom {
            kind_stmt: Digest::from_u64(7),
            proof: 7,
        },
        |a| {
            if let WireAuth::Custom { kind_stmt, .. } = a {
                alter(kind_stmt)
            }
        },
        true,
    );
    let stealth = WireAuth::Stealth {
        one_time_pk: Digest::from_u64(7),
        ephemeral_pk: Digest::from_u64(11),
        sig: 7,
    };
    add(
        "stealth.one_time_pk",
        stealth.clone(),
        |a| {
            if let WireAuth::Stealth { one_time_pk, .. } = a {
                alter(one_time_pk)
            }
        },
        true,
    );
    add(
        "stealth.ephemeral_pk",
        stealth,
        |a| {
            if let WireAuth::Stealth { ephemeral_pk, .. } = a {
                alter(ephemeral_pk)
            }
        },
        false,
    );
    add(
        "token.issuer_key",
        WireAuth::Token {
            issuer_key: Digest::from_u64(7),
            sig: 7,
        },
        |a| {
            if let WireAuth::Token { issuer_key, .. } = a {
                alter(issuer_key)
            }
        },
        true,
    );
    out
}

pub fn accepted_auth_case(
    auth: dregg_lean_ffi::marshal::WireAuth,
) -> (
    dregg_lean_ffi::marshal::WireHostCtx,
    dregg_lean_ffi::marshal::WireState,
    dregg_lean_ffi::marshal::WireTurn,
) {
    use dregg_lean_ffi::marshal::*;
    let state = WireState {
        cells: vec![
            (
                0,
                WireValue::Record(vec![
                    ("balance".into(), WireValue::int(100)),
                    ("nonce".into(), WireValue::int(7)),
                ]),
            ),
            (
                1,
                WireValue::Record(vec![("balance".into(), WireValue::int(5))]),
            ),
        ],
        bal: vec![(0, 0, 100), (1, 0, 5)],
        ..Default::default()
    };
    let turn = WireTurn {
        agent: 0,
        nonce: 7,
        fee: 0,
        valid_until: 1000,
        block_height: 0,
        prev_hash: Digest::default(),
        root: WForest {
            auth,
            caveats: vec![],
            children: vec![],
            action: WireAction::Balance {
                actor: 0,
                src: 0,
                dst: 1,
                amt: 30,
                asset: 0,
            },
        },
    };
    (WireHostCtx::diag(), state, turn)
}
