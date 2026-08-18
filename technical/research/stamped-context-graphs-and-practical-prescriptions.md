---
type: Product Architecture
title: "Context graphs, live twins, and practical prescriptions — research + gap"
description: >-
  How industrial systems produce plant-now advice; what Stamped already has;
  what we adopt, adapt, or reject. Companion to the ML citations bibliography.
  Authority for implementation: ADR-028 and L4-plant-context-graphs.md.
tags: [stamped-energy, technical, research, context-graph, graph-rag, l4, prescriptions]
timestamp: "2026-08-18T00:00:00Z"
status: Accepted research companion — does not override L4 SSOT until ADR-028
---

# Context graphs and practical prescriptions

*Companion to [ML citations](stamped-research-and-ml-citations.md), [L4 SSOT](../layers/l4-l6/L4-knowledge-and-reasoning.md), [ADR-017](../../decisions/016-020/ADR-017-l4-adaptive-retrieval-and-web-trust.md), [ADR-024](../../decisions/024-026/ADR-024-holistic-plant-decisions.md). Architecture that this research recommends: [L4 plant context graphs](../layers/l4-l6/L4-plant-context-graphs.md) · [ADR-028](../../decisions/028-032/ADR-028-dual-plant-graphs-and-path-d.md). Eval: [practicality rubric + demo gold](../cross-cutting/05-prescription-practicality-eval.md).*

> **Purpose.** Explain how others produce *practical* plant advice, map that onto Stamped L4, and name the gaps that make our demo cards better than our compiler. This is CORE vs FRONTIER honesty — we do **not** run Graphiti, PlantGPT, or Neo4j today.
>
> **Gold bar.** [Demo prescriptions](../../demo-decks/prescriptions-examples.md) — named floor action, feasible Due, industry overlay, Example 6 (Tuesday blocked → Thursday after Job 447).

**How to read the lanes**

| Lane | Meaning |
|---|---|
| **CORE — product of record (after ADR-028)** | Dual plant graphs + Path D + quality-default compile + L5 compile-trace |
| **FRONTIER — evaluate / do not take as a dependency** | Graphiti, Microsoft GraphRAG, PlantGPT, Neo4j, full ISA-95 MES ontology |

**Citation tags:** **[VERIFIED]** primary source checked this pass · **[GENERAL]** standard in the field · **[FROM SSOT]** already in L4/L5 ADRs.

---

## 0. One-slide map

| Pattern | What it is for | Stamped today | After ADR-028 |
|---|---|---|---|
| Knowledge graph | Slow meaning: assets, owners, SOPs, typical envelopes | Path G **deferred**; department graph is static JSONB | **Graph A** (canonical), refresh every few days |
| Live / digital-twin index | Fast now: running, orders, shift, ToD/MD | L2 measurements + `ProductionOrder` exist; L4 does not pack them at compile | **Graph B** — same node IDs, event updates, **no LLM** |
| Context pack | What matters for *this* Finding | Path H hop-2 = document siblings | **Path D** (delta) + Path G hop + Path H playbooks |
| Hybrid RAG | Find playbook text | Path H sparse+dense RRF over 5 seeds | Keep Path H; filter by vertical + class |
| LLM-as-judge | Language quality after facts | Specified in defense brief §3.11; not on Rx path | Judge **practicality** after deterministic gates; 10+ calls allowed |
| Staff debug UI | Human verifies the compile | L5 console: card + AD-5 gate | Console tabs: graph, retrieval, compile loop, eval. **Not L6.** |

---

## 1. Knowledge graph vs context graph vs live twin

### 1.1 Graph → knowledge graph → context graph

**Neo4j, “What is a context graph” (2026).** *[VERIFIED]* [neo4j.com/blog/agentic-ai/what-is-context-graph](https://neo4j.com/blog/agentic-ai/what-is-context-graph/)

- A **graph** answers: what is connected?
- A **knowledge graph** adds meaning (types, business relations).
- A **context graph** connects that meaning to *this task*: conversation, tools, decision traces — “which context is relevant now, and why?”

**Arya.ai, “Knowledge Graphs vs. Context Graphs”.** *[VERIFIED]* [arya.ai/blog/knowledge-graphs-vs-context-graphs](https://arya.ai/blog/knowledge-graphs-vs-context-graphs)

KG is the map of the business. A context graph adds decisions, timing, exceptions, outcomes — memory for *why* a choice was made.

**TrustGraph.** *[VERIFIED]* A context graph is still a knowledge graph; the distinction is *optimisation*: extract a query-relevant subgraph into an LLM window (Turtle/JSON-LD/Markdown), plus reified agent traces.

**Steal:** two *persistent* graphs (canonical + live) plus a *query-time* pack. Do **not** rename the whole platform “the context graph.”

**Reject:** treating “context graph” as a product we must buy.

### 1.2 Industrial KG + digital twin

Smart-manufacturing KG surveys (e.g. *Computers in Industry* 2024, “Making knowledge graphs work for smart manufacturing”). *[GENERAL]* KGs are used because manufacturing data is relational: asset ↔ process ↔ maintenance ↔ decision. The hard part is *contextualising* a live plant, not storing triples.

Digital twin + KG fusion papers (2026 DT–KG “Q-layer” style work). *[GENERAL]* Twin = live state; KG = semantics and constraints. Fusion is what lets a system explain *why*, not only *what*.

**PlantGPT / DomainWise (Tridiagonal).** *[VERIFIED]* Marketing + architecture claims: SAP + sensors + P&IDs + maintenance logs → agents; KG as auditable decision path. We do **not** claim feature parity.

**OnBrain (open Graph RAG + Neo4j + Chroma).** *[VERIFIED]* [github.com/prajwal-priyadarshan/OnBrain](https://github.com/prajwal-priyadarshan/OnBrain) — manuals/work orders → entity graph + vector store + cited answers. Closer to our *analyst* surface than to money-bearing Rx.

**PlantGraphExpert (Computers & Chemical Engineering 2026).** *[VERIFIED]* OntoCAPE + Tennessee Eastman — P&ID/PFD exploration for *fault diagnosis*, not energy prescriptions.

**ISA-95 / IEC 62264.** *[GENERAL]* Personnel, equipment, material, production capability. We already half-have this: [`plant-department-graph.json`](../../contracts/schemas/plant/plant-department-graph.json) + [`production-order.json`](../../contracts/schemas/plant/production-order.json).

**Steal:** ISA-95-shaped nodes; live properties on equipment / order / personnel.

**Reject:** full MES ontology, P&ID vision, chemical OntoCAPE, “plant OS.”

### 1.3 Live / temporal graphs (no LLM on the hot path)

**Graphiti (Zep / getzep).** *[VERIFIED]* [github.com/getzep/graphiti](https://github.com/getzep/graphiti)

- Incremental episodes; no Microsoft-GraphRAG-style batch rebuild
- Bi-temporal facts (`t_valid` / `t_invalid`); invalidate, do not delete
- Hybrid search (semantic + keyword + graph); typical sub-second query
- Built as *agent memory*, often on Neo4j

**Steal:** live facts as property updates with validity; structure built once.

**Reject (this spec):** Neo4j + Graphiti as a production dependency. Postgres property-graph tables (later) + L2 as live truth is enough for 1–2 plants. Upgrade if temporal queries fail a labelled slice.

### 1.4 Retrieval: hybrid is the mechanism; delta is the question

**HybridRAG** (vector + BM25 + graph hop). *[GENERAL]* Sparse finds tag names, standard clauses, model numbers; dense finds paraphrases. Path H already does FTS + dense + RRF. *[FROM SSOT]*

**Microsoft GraphRAG.** Community summaries over *static* corpora. Wrong default for live plant state (orders, standby, shift).

**ADR-017 Path G.** *[FROM SSOT]* Reserved for `asset_type ↔ waste_category ↔ measure ↔ standard_ref` over L2 graph + curated edges. Deferred until two-hop docs fail a labelled slice.

**Steal:** Path H stays for playbooks. Path G for relations. **Path D (delta)** is the *question*: live vs canonical. Hybrid does not discover Job 447.

### 1.5 Quality loops / LLM-as-judge

**L4 decision defense §3.11.** *[FROM SSOT]* Deterministic gates on 100% of outputs; LLM judge only on residual language. Do not ask a model whether ₹ matches the calculator.

Industry pattern: draft → schema/claim verify → judge rubric → repair → abstain. Judges that *are* the quality score hide deterministic failures.

**Steal:** judge scores *practicality* (owner, window, industry specificity), never ₹. Loop until practical or abstain. **≥10 generation calls allowed** on the Rx path; not a ceiling.

**Reject:** judge-as-sole-score; stopping at 2 calls because a 2026-07 SSOT said cheap.

---

## 2. Gap analysis — demo gold vs compiler

Gold: [prescriptions-examples.md](../../demo-decks/prescriptions-examples.md). Compiler: Lane A templates (0 LLM) by default for 16 categories; Lane B Path H + ≤2 calls; Path G deferred; ADR-024 negotiation is **post-hoc**.

| Demo need | Example | Lane A / Path H today | Gap |
|---|---|---|---|
| Named floor action | “Inspect COMP2 filter in next low-load window” | Category template: generic inspect / stagger copy | Template is a family, not a plant-now card |
| Feasible Due | Ex. 6: Tue blocked → Thu after Job 447 | `when: next_shift_start` | Orders + standby not packed at compile |
| Live standby | COMP1 at 90% → cannot isolate COMP2 | Not read | Live index property `available_as_standby` |
| Open orders | Job 447 air-using line | `ProductionOrder` contract exists; L4 barely uses it | Compile-time feasibility (move ADR-024 earlier) |
| Who on this shift | Electrical lead · Shift B · Feeder A | Role string (`utilities lead`) | Roster optional; degrade to role+shift; never invent names |
| Industry overlay | Steel holding, cement kiln+mill+WHR, pharma setback | Five seed playbooks, generic energy | Vertical + AssetClass on Graph A + Path H filters |
| Evidence on flip | Tags + window + baseline | Finding evidence_refs | Keep; delta facts must be *extra* evidence, not instead |
| Staff can verify | — | Phoenix optional; L5 shows card + AD-5 gate | Compile-trace on L5 console |

**How we improve (leverage order, not novelty)**

1. Treat the demo deck as **eval**, not brochure.
2. **Keep Lane A; stop making it the default.** Quality path for all categories. Lane A = CI / `force_lane=a` / model-down degrade, labelled `template_fast_path`.
3. Pull Path G. Two-hop documents cannot encode standby × order × owner.
4. Move ADR-024 feasibility **into compile**. Negotiation stays for human pushback.
5. Quality over pricing on Rx (10+ calls). Analyst / Path W / indexing stay cost-aware. Calculator owns ₹.
6. Do not copy telemetry into a second graph DB. Graph B = L2 projection.
7. Degrade honestly on people.

---

## 3. Adopt / adapt / reject

| Pattern | Decision | Why |
|---|---|---|
| Canonical plant KG (Graph A) | **Adopt** | Path G trigger in ADR-017; demo needs relations |
| Live index on same IDs (Graph B) | **Adopt** | Event updates, zero LLM; L2 already has measurements + orders |
| Path D delta pack | **Adopt** | This *is* Example 6 |
| Path H hybrid RAG | **Keep** | Playbooks; add vertical/class filters |
| Path G relational hop | **Pull trigger** | Document hop-2 is the wrong graph |
| Lane A 0-LLM graph | **Keep, not default** | CI, degrade, explicit force |
| Template family on quality path | **Keep** | Bounds What; no free-form rewrite |
| Quality-default compile + judge | **Adopt** | Early-stage ₹/Rx economics |
| L5 compile-trace UI | **Adopt** | Staff verify; not L6; not a second Phoenix |
| Graphiti / Neo4j | **Reject for now** | Ops cost; steal the *pattern* |
| Microsoft GraphRAG as default | **Reject** | Static corpus summarisation |
| Full ISA-95 / MES product | **Reject** | ADR-026 two pillars + shared context |
| Judge as sole quality score | **Reject** | Defense brief §3.11 |
| Poverty-pricing Rx (0–2 calls as goal) | **Reject** | Quality wins on this surface |

---

## 4. Honesty footer

- We do not run Graphiti, PlantGPT, or Neo4j in production.
- CORE after ADR-028 is the dual-graph compiler + L5 snapshot display.
- FRONTIER names are for technical conversations and watchlists.
- Demo ₹ figures remain `[illustrative]` until M&V lock.

*Research pass: 2026-08-18. Implementation authority: ADR-028, not this note.*
