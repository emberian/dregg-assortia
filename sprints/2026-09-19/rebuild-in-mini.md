# Build the New World in Mini

Recorded after the September 19 Bread/Mini microswarm. This settles the construction direction that the orientation left open.

Ember's clarification:

> Don't you think we should be just rebuilding into mini what we need for the New World? i don't want to get stuck in an optional morass when we can just rebuild. After all, bread's machinery can be rebuilt.

Mini is the implementation home for the new resource world and the capabilities needed to operate it. Rebuild the required functionality there according to its coherent semantics. Bread supplies requirements, algorithms, failure cases and historical evidence; preserving its architecture or making it the initial runtime is not a project requirement.

The work follows the intended user experience: authorable resources and laws, typed content, atomic joint operations, authority and disclosure, durable tasks and external attempts, hosting, and actual Hermes access. Extend the existing Mini foundations where sound. Rebuild missing operational machinery within the Mini system, with source-owned semantics and physical handlers that implement those semantics.

Reuse is an implementation convenience when a component clearly fits. It is not a prerequisite investigation, a separate migration programme, or a reason to preserve incompatible contracts. Standard libraries and upstream Hermes remain useful dependencies. The directive does not require reproducing every Bread feature or discarding working Mini machinery.

The next design work is a concrete construction contract for this system, followed by bounded implementation assignments through one integrated user journey. The source findings in [the orientation](core-orientation.md) remain relevant; its alternative-runtime framing and emphasis on selective Bread machinery reuse are superseded. No implementation fleet or builds were started while recording this decision.
