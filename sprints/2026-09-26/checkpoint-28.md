# Checkpoint 28 — physical roots and complete sharing approval

September 27, 2026. Continues [checkpoint 27](checkpoint-27.md).

The first source-publication refusal exposed a shared implementation error:
signed observations bind the materialized resource payload root, whereas the
durable compare-and-swap guard binds the complete physical cell root. Requiring
those two roots to be equal refused a valid source. Changing the signed root or
removing the physical guard would not be a repair.

Mini `d3ccff2` supplies a general physical-read-root theorem and repairs selected
source publication. `676e8c3` repairs dispatch read guards. `9aec865` repairs
share issuance and binds the custody plan to the complete canonical Request,
including payer, funding and source capabilities, rather than only the ticket
specification. The independent twelve-module narrow check is preserved in
[Mini's custody/physical evidence](https://github.com/emberian/minidregg/tree/9aec865/docs/evidence/2026-09-27-application-share-issue-custody-physical).
These are source gates; the older native images do not contain the repairs.
An independent full native build from the exact `9aec865` archive is the next
integration input. Lifecycle begin/claim root repairs remain in progress.

Mini `306620b` preserves a separately qualified Linux current-birth Host, whose
210 source files were checked against the pinned baseline and overlay. Its
fresh direct fixture accepted an actual application birth. That run subsequently
stopped on an incorrect fixture expectation about scalar-page presentation;
it does not establish a complete application/session journey. A fresh corrected
run is required, followed by the hosted Hermes creation path.

Chronological dispatch replay, participant signing custody, browser bootstrap
and the exact-readback dispatch receiver are advancing in separate owned lanes.
The private fn-control bridge qualified status, position and inspection only;
no poll or ACK is established by that result. The old source-publication attempt
still has no accepted source publication or POST. No complete shared service,
real-model run or public deployment follows from this checkpoint.

The [five parallel journeys](parallel-journeys.md) remain the acceptance scope:
shared apps, programmable resources, hosted agents, persistent hosting and
publication between nodes. They must converge on the same governed persistent
work, including differing participant permissions and recovery, rather than
remaining separately successful component fixtures.
