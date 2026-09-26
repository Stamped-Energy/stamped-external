# TRACE_NOTES — system archify (S1 + reader F1/F1b)

## SYS-00 Stamped end-to-end map
- Question: What are the layers of Stamped and how does plant data become a decision card?
- Sources: pinned manifests; ADR-030; StubCardSink default (L4-G4); L5-G4 no /cards; L3C-G5 scheduler not deployed; hot path suppression+lane (L3C-new-hotpath).

## SYS-01 Contract & boundary map
- Question: Which contracts (schema@version) cross each layer boundary, and who owns them?
- Sources: contracts/, TOPICS.md, OpenAPI pins; transport/isolation card; L5-G4 dashed /cards ingest edge label.

## SYS-02 Runtime: data batch to decision
- Question: When a machine reading is taken, what runs until a card proposal exists?
- Sources: L1E buffer/MQTT QoS1 (L1E-G-new-expiry); L4 runtime inbox→DecisionTrace→StubCardSink; L5-G4.

## SYS-03 Runtime: Ask analyst question
- Question: When someone types a question in the control room, what happens until an answer appears?
- Sources: L4-new-ask / AskRetired 503; L4-07 designed ReAct; L6 L4_LIVE vs fixture Preview UX.

## SYS-04 Runtime: card closure and M&V
- Question: After an owner marks a card done, how does Stamped decide whether savings are real?
- Sources: ADR-020; workflow `verified` vs bill-verified; L5 worker fixture evidence default; L6-new-L5-push poll.

## SYS-05 Operating loop across layers
- Question: Which layer owns each step of the product loop and where are the human gates?
- Sources: L3C-new-hotpath suppression+lane; L3E eval gates offline only.

## SYS-06 Life of one plant condition
- Question: What states does a single issue pass through across layers, and who owns each state?
- Sources: pinned manifests; L5-G4 designed L4→L5 card hop.

## SYS-07 Deployment and trust boundaries
- Question: Where does each component run, which networks are separated, and where do secrets stay?
- Sources: ADR-005/007/033; X-Service-Key vs provider API keys.

## SYS-08 Built vs designed status map
- Question: Which parts exist in code today, which are only designed, and what is not live?
- Sources: L1E context-agent; L1C poller; L3C-G5; L5-G4; L4 hindsight.

## SYS-09 Evidence and money lineage
- Question: Where does a rupee figure come from, and which steps may create or change it?
- Sources: L3C calculator_ref; L5 ledger; L5-G4 dashed proposal hop.
