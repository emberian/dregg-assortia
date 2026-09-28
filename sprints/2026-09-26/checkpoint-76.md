# Checkpoint 76 — enrollment is a required native path

September 28 UTC, 2026. Continues [checkpoint 75](checkpoint-75.md).

The retained pure INSTALL preparation remains active under invocation
`670871036976425ca411a8c533b402d0`. Both cold Host identity checks matched;
the base original-call lookup completed, and successor lookup was active at
the last owner observation. No INSTALL receipt is claimed yet. Keep this
single attempt and mini_app_contract's sole writer ownership.

## A missing step, now assigned

The five accepted session births create scalar sessions and **empty** content
descriptors. `ApplicationGrainSessionBirth` explicitly leaves enrollment to a
later authorized operation. Born sessions are not enrolled sessions.
`ApplicationDispatchAdmission` requires an installed, generation-bound
`ApplicationGrainSessionEnrollment` matching the dispatched session.

Current operator tooling has no source-owned enrollment path. fn_mini_review
owns its construction. Existing session/content laws, stable enrollment atom,
strict codec and initial/renewal actions are reusable. The planned event28
wrapper will reuse joint session/descriptor admission and add a separately
authorized current app observation with an atomic read guard. Private plan and
assembly ops82/83 and submit/receipt lookup84/85 are allocated for this work.
These are assignments and protocol reservations, not implemented behavior.

The extra native guard matters: generic DRC commands have one subject, and
adding an app serving-witness target would require app mutation authority.
Bob and both Hermes controllers have app-observe rights, not app-mutate rights.
Do not expand their authority just to enroll a session. Source authoring should
select an admitted ticket, derive its participant/origin/session fields, check
signed interface/schema and role ceiling, select current serving app generation,
and retain exact initial or renewal preimages. Native admission and replay must
enforce those joins; a planner-only check is insufficient.

Resident configuration requires at least one fixed ticket entrance, but its
preflight does not require installed enrollment. Source inspection therefore
supports this order: **INSTALL → tickets/entrance custody → START → enroll
against actual serving app generation → usable dispatch**. Early HTTP requests
must refuse while enrollment is absent. START advances app generation, so
enrolling against its predecessor is wrong. Do not hardcode generation2 merely
because that is the expected first r3 start.

## Corrected ticket roles and useful runtime results

Mini `de307f2` removes a false shell comparison between issuer grain parent7901
and the recipient Hermes origin7920/7921. The source contract keeps them
separate. The issuer now binds its grain parent to the exact request/policy and
recipient origin to the selected allocation/scope. Candidate origin0 remains
provisional until matched by authorized enrollment; do not present it as a fact
installed by session birth. Later event26 checks current parent generation
separately from that historical origin.

Mini `3886bb3` retains the ordinary-birth runtime gate: one private paired
persistent-session birth improved from158.229 to80.972 seconds with identical
receipts and Store. Lost-CAS-reply recovery, stale readback followed by lookup,
equal-byte AlreadyPresent, and cold historical replay passed at their stated
scope. Live r3 still uses cb55 during INSTALL.

The actual native-entrance/Git component probe found a Rust client recovery bug:
under inherited umask0002, Git made writable local directories that lookup
correctly refused. shared_resource_tools has added process umask0077 and is
rerunning the fresh fixture. The prior release artifact is not qualified for
this corrected source. The test uses real Git behind the native Unix credential
parser, but does not establish Mini dispatch or signed-package execution.

runtime_review owns a typed read-only Mini op56 preview command so ticket
preparation can use the persistent operator Host instead of an extra cold replay
per ticket. agent_api_host owns wrapper consumption after qualification. Exact
request, plan and signing-slot checks remain required.

The local model's unchanged bounded invocation expires at03:16:33 UTC on
September28. Systemd refused an in-place extension; Mini `84784fe` retains that
observation. Verify terminal state before deliberately launching another bounded
invocation if needed. No current caller or inference failure justifies a duplicate
GPU load.

The complete human/agent/shared-app/restart/fn journey remains open. These fixes
serve that journey; their individual checks do not establish a usable preview.
