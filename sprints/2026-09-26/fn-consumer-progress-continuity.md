# Consumer progress across empty and selected pages

September 27, 2026. Construction decision and acceptance requirements, **not
implemented assurance**. This extends the semi-untrusted transport boundary in
[the publication contract](fn-publication-disclosure-contract.md).

The isolated fn run accepted a signed Mini empty-page progress record from
position 0 to 2, then acknowledged cursor 2 through the typed historical
selector. fn ACK appended its own local Store event: durable ACK was 2 while
frontier became 3. Repeating empty-page ACK cannot eliminate that tail. A next
selected article at sequence 3 has cursor 4 and must not be rejected merely
because its sequence differs from ACK 2.

Qualified local fn polling scans at most 16 consecutive sequence-checked
events and stops at the first article matching the pinned consumer query.
That is a local observation, not evidence that every remote article arrived.
Mini must still independently admit the exact owner-signed selected release
under the recipient's current authority.

Reserved event 17 will durably bind gateway-authorized coverage to the pinned
consumer scope, previous ACK, selected sequence/cursor, exact cursor/report/
source/Message-ID commitments, and the original admitted selected-release
receipt. The configured gateway signs local-observation testimony; it does
not replace the release owner's authority. Private Host authoring obtains the
observation through pinned native polling. Caller-supplied observation fields
are not an attestation. Fresh ACK retains exact live repoll and position checks;
lost ACK replies recover through the original durable records.

**One source-owned progress ordering must cover both empty and selected
pages.** Current `FnConsumerProgress.decide` recognizes an exact empty-page
marker but does not derive a latest monotone frontier. An event-only coverage
record cannot silently inherit an ordering guarantee that does not exist.
Implementation must define and check the admitted predecessor, reject gaps,
forks and stale competing advances, and preserve exact historical retries.
Whether this is represented by checked state or an admitted-history projection
remains the implementing lane's design choice; a naked monotone transport
cursor is insufficient.

The acceptance sequence is empty → selected → empty → selected, with duplicate
submissions, changed scope, competing advances, restart, lost Mini completion,
and lost fn ACK response. Refusals preserve the logical Mini image; recovery
must not resend an application effect or import unrelated content. Historical
tag-9 records remain recognizable without retroactively claiming they carried
the new ordering proof.

Owners: fn_contracts for source admission, fn_mini_review for Host integration,
shared_resource_tools for custody and the native fixture; root reviews their
joined result. Publication stays held until the relevant new path is qualified.
