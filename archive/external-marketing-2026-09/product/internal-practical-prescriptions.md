---
type: Product Architecture
title: "Internal — practical prescriptions (dual graphs)"
description: "Staff-only explainer for how Stamped compiles floor-ready Rx. Not a public blog."
tags: [stamped-energy, product, internal, l4, prescriptions]
timestamp: "2026-08-18T00:00:00Z"
---

# Internal — practical prescriptions

*Staff only. Client copy stays in [positioning](Stamped_Client_Positioning_and_Narrative_v1.md) and [demo cards](../../demo-decks/prescriptions-examples.md). Do not publish this as a blog.*

Stamped prescriptions must sound like a shift lead wrote them: named action, feasible Due, live orders/standby, industry overlay. That is **not** a better prompt on a template.

**How it works (say this internally)**

1. **Graph A** is the slow plant map (topology, owners, isolation, playbooks, typical envelopes). Refresh every few days. LLM is allowed on that batch.
2. **Graph B** is a live index on the same IDs (running, kW vs typical, orders, ToD). **No LLM.** L2 is truth.
3. **Path D** diffs live vs typical/allowed. That delta *is* Why and Due — including “Tuesday blocked; Thursday after Job 447.”
4. Templates still bound the **action family**. The quality path fills Who / When / Why from facts. Lane A (template, 0 LLM) stays for CI and degrade — it is not the default.

**Do not say** we run Graphiti, Microsoft GraphRAG, PlantGPT, or Neo4j. We steal *patterns* (entity-first, live overlay, community playbooks), not those products.

**₹** still comes from the calculator. The LLM judge scores language, never money.

Eval gold: [practicality rubric](../cross-cutting/05-prescription-practicality-eval.md). Architecture: [ADR-028](../../decisions/028-032/ADR-028-dual-plant-graphs-and-path-d.md).
