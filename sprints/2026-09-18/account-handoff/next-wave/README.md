# Unapplied next-wave work

These are preserved scratch sources, patches, baseline identities and checks. They are not imported by a production repository. Read each owner handoff before using them. Do not apply every patch independently: the shared full-request codec currently has 16 fields, while the selected generation/revision separation requires 17. Coordinate one representation and version migration, then migrate and exercise all receiving consumers.

`delegation/` contains checked Family/State/Effects drafts and 32-law audit; `checker/` contains checked mixed-lineage checker/witness and 21-law audit, with its registry draft explicitly unchecked. `authority/` contains byte-compatible low-codec checks and proposed ParentLink wire changes. Runtime/birth evidence is outside this directory. Rebuild scratch artifacts safely; no olean mirror was copied.
