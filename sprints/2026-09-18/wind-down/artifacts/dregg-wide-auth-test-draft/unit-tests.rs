#[cfg(all(test, dregg_direct_present))]
mod auth_builder_tests {
    use super::imp;
    use crate as dregg_lean_ffi;
    include!(concat!(env!("CARGO_MANIFEST_DIR"), "/tests/support/direct_auth_cases.rs"));

    #[test]
    fn direct_auth_builders_preserve_every_digest_coordinate() {
        use crate::marshal::{marshal_turn_hosted, WireAuth};
        for case in cases() {
            for auth in [case.valid, case.altered] {
                for nested in [false, true] {
                    let auth = if nested {
                        WireAuth::OneOf { candidates: vec![auth.clone()], proof_index: 0 }
                    } else { auth.clone() };
                    let (host, state, turn) = accepted_auth_case(auth.clone());
                    let wire = marshal_turn_hosted(&host, &state, &turn).unwrap();
                    let request: serde_json::Value = serde_json::from_str(&wire).unwrap();
                    let expected = &request["turn"]["root"]["auth"];
                    assert!(!expected.is_null());
                    let encoded = crate::ffi::with_executor(|| Ok(imp::encode_auth_for_test(&auth))).unwrap();
                    let actual: serde_json::Value = serde_json::from_str(&encoded).unwrap();
                    assert_eq!(&actual, expected, "{} nested={nested}", case.name);
                }
            }
        }
        let status = crate::lean_initialization_status();
        assert!(status.executor_ready);
        assert_eq!(status.default_full, None);
    }
}
