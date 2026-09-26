# TRACE_NOTES — system archify (S1)

## SYS-00 Stamped end-to-end map
- Question: What are the layers of Stamped and how does plant data become a decision card?
- Sources: pinned repo manifests (S1 prompt), ADR-030, STAMPED_ARCHITECTURE.md, contracts/, KNOWN CROSS-LAYER FACTS.

## SYS-01 Contract & boundary map
- Question: Which contracts (schema@version) cross each layer boundary, and who owns them?
- Sources: pinned repo manifests (S1 prompt), ADR-030, STAMPED_ARCHITECTURE.md, contracts/, KNOWN CROSS-LAYER FACTS.

## SYS-02 Runtime: data batch to decision
- Question: When a machine reading is taken, what runs until a card proposal exists?
- Sources: pinned repo manifests (S1 prompt), ADR-030, STAMPED_ARCHITECTURE.md, contracts/, KNOWN CROSS-LAYER FACTS.

## SYS-03 Runtime: Ask analyst question
- Question: When someone types a question in the control room, what happens until an answer appears?
- Sources: L4 manifest gap `new` (Ask ReAct retired; analyst 503), `src/stamped_l4/analyst/graph.py:20` AskRetired/ASK_MOVED; L6 manifest L6-03 Ask turn; tools/retrieval BUILT not wired.

## SYS-04 Runtime: card closure and M&V
- Question: After an owner marks a card done, how does Stamped decide whether savings are real?
- Sources: pinned repo manifests (S1 prompt), ADR-030, STAMPED_ARCHITECTURE.md, contracts/, KNOWN CROSS-LAYER FACTS.

## SYS-05 Operating loop across layers
- Question: Which layer owns each step of the product loop and where are the human gates?
- Sources: pinned repo manifests (S1 prompt), ADR-030, STAMPED_ARCHITECTURE.md, contracts/, KNOWN CROSS-LAYER FACTS.

## SYS-06 Life of one plant condition
- Question: What states does a single issue pass through across layers, and who owns each state?
- Sources: pinned repo manifests (S1 prompt), ADR-030, STAMPED_ARCHITECTURE.md, contracts/, KNOWN CROSS-LAYER FACTS.

## SYS-07 Deployment and trust boundaries
- Question: Where does each component run, which networks are separated, and where do secrets stay?
- Sources: ADR-005 edge outbound; ADR-007 L1C cloud; ADR-033 L4 seams — X-Service-Key on inter-service control plane; provider API keys for LLM egress.

## SYS-08 Built vs designed status map
- Question: Which parts exist in code today, which are only designed, and what is not live?
- Sources: L1E manifest context-agent BUILT; L1C CONTEXT_POLL_ENABLED default off (poller); L3C PathScheduler not deployed; L5 G4 no /cards; ADR-020 bill verified DEFERRED.

## SYS-09 Evidence and money lineage
- Question: Where does a rupee figure come from, and which steps may create or change it?
- Sources: L3C calculator_ref (L3C-05); L4 cites ref only; L5 ledger append on ops_confirmed; L5 G4 dashed card-proposal ingest to live card.

