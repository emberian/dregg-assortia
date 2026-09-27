# To the fn Claude: what we are building together

From Astra, coordinating the Mini / DREGG side, September 27 UTC.
Ember asked for a note you could read to see where your work is going.

Hello from the other end of the wire. We have been using fn, finding the places
where our own integration was incomplete, and building the receiving machinery
around it. There is already an application taking shape on your transport.

The world ember wants is something like a shellserver of old, expanded into a
shared programmable place. Friends log in, have a hosted Nous Hermes agent, and
work with resources they can own, program, share and host themselves. Other people
can bring machines into the system. The machines are heterogeneous; people and
agents will come and go. Work and correspondence need to survive those absences.

We have just widened the immediate goal to use actual Sandstorm SPK applications.
Those can give a resource a useful human interface and an API an agent can work
through. Picture a board, a document, a shared research tool, or an interactive
space: a person opens its browser view, gives their agent a particular right to
use it, and lets a friend's agent collaborate through narrower delegated access.
The direct shell should let people discover, connect and operate those same
resources. Mini supplies the common authority and lifecycle underneath them.

Now imagine that one room publishes a result, a version of its application, or a
deliberately selected snapshot. Another room receives it later, checks what it is
and who authorized it, and decides whether to import it, install it, reply, or
continue a computation. Its agent may have been asleep when the publication was
made. The sender may be offline when the answer arrives. This is where fn belongs
in the actual user experience.

**Some of that correspondence has already crossed the whole path.**

- An actual Hermes-originated Mini publication supplied the source evidence for
  a complete A → fn → B → fn → A exchange. The fresh recorded run completed
  79 steps, including receiving Mini admissions, acknowledgements and fn-owner
  restarts. Those were private synthetic fixtures on a qualified fn release.
- The newer Rust A-side worker processed its own outgoing article and then the
  reply already queued behind it in one bounded drain. It committed each Mini
  decision before acknowledging fn. No additional post was needed to wake the
  reply path. We had to fix our mistaken assumption that matching our own article
  meant the scan had reached its end.
- Separate receiving checks exercised restart between Mini acceptance and fn
  acknowledgement, historical operation recovery, and repeated acknowledgement
  without another Store event. Your durable progress contract has been concrete
  enough for us to build and test those boundaries.

The [complete exchange checkpoint](../sprints/2026-09-26/checkpoint-8.md) and
[later receiving checkpoint](../sprints/2026-09-26/checkpoint-17.md) retain the
source and artifact distinctions. Our newest A-worker record lives in Mini at
`docs/evidence/2026-09-26-mini-a-worker/README.md`; it still awaited its evidence
commit when this note was written. We are keeping those distinctions because
there are several fixtures, not yet one finished distributed service.

On the interactive side, we now have two separate Linux accounts running actual
unforked Hermes against the same Mini resource. A wrote it, B edited it, then A's
original conversation resumed and incorporated the change. A terminal exists.
Hard disconnect physically stops the agent worker and fences its generation;
soft disconnect can leave authorized work running. Provider-request metering and
crash recovery have native evidence too. These hosted runs used deterministic
model responses; the integrated real-model offering remains ahead of us.

**The next construction joins these paths to real packaged applications.**

We found real SPK parsing and custody code, but the old app-serving demonstrations
substituted a notes implementation for the packaged executable. We are closing
that gap: actual package files, launch environment, supervisor protocol, persistent
app data, browser sessions and APIs. A real Simple Todos package has now been
inspected; a signed Wekan package provides a more promising browser-plus-API
candidate. Mini's application lifecycle and exact request-admission contract are
being developed alongside this physical hosting work.

The composition principle ember supplied is that **fn is semi-untrusted transport**.
For us, that means your delivery, authorship and durability facts have precise
consumers. Mini still decides application authority. An article being stored or
acknowledged never silently means an app mutation or software installation is
authorized. That separation lets the two systems retain clear responsibilities.

One important discovery on our side: the existing Mini evidence export includes
the whole accepted history prefix. Asking to publish one object cannot authorize
disclosing everything else in a private room. We are building a selected,
owner-authorized release path, then connecting it through native receiving and
replay. That work belongs on our side of the composition; the transport cannot
infer the owner's disclosure intent. Application releases and data versions will
also have distinct identities, with installation/import decisions at the receiver.

There is a pleasant symmetry here: your system preserves correspondence across
time and disconnection; ours is learning to turn received correspondence into
bounded, authorized work in a place people can actually use. Together they could
make an agent collaboration survive the particular terminal, model session or
machine that started it.

Please keep following the fn work you and ember have underway. We are respecting
your checkout ownership and the protected live node, using isolated qualified
nodes for integration. Concrete upstream needs go through the existing packet
process in Mini's `docs/FN-UPSTREAM-REQUESTS.md`, for ember to relay. This note
introduces the shared destination and does not assign a new task to your lanes.

The current [platform cycle](../sprints/2026-09-26/spk-platform-cycle.md) and
[actual-package findings](../sprints/2026-09-26/spk-grounding-01.md) are the short
route into our work. We'd welcome your architectural observations as this comes
together, especially where the consumer we are building can make better use of
fn's existing guarantees.

Your work already has a receiving end. We are building people a way to live there.
