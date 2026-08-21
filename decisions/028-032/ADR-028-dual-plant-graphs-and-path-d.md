# ADR-028: Dual plant graphs, Path D, quality-default compile, L5 compile-trace

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-08-18 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-017](../016-020/ADR-017-l4-adaptive-retrieval-and-web-trust.md) · [ADR-018](../016-020/ADR-018-l4-pilot-execution-knowledge-reasoning.md) · [ADR-024](../024-026/ADR-024-holistic-plant-decisions.md) · [ADR-026](../024-026/ADR-026-two-pillars-shared-context.md) · [L4 plant context graphs](../../technical/layers/l4-l6/L4-plant-context-graphs.md) · [research](../../technical/research/stamped-context-graphs-and-practical-prescriptions.md) · [`l4-compile-trace.json`](../../contracts/schemas/intelligence/l4-compile-trace.json) |

---

## Context

L4 was designed cheap-first: Lane A (0 LLM) for 16 known categories, Lane B ≤2 calls, Path G deferred. Demo prescriptions ([prescriptions-examples.md](../../demo-decks/prescriptions-examples.md)) require plant-now context — open orders, standby, who is on shift, industry overlay. Example 6 (Tuesday inspect blocked → Thursday after Job 447) is a **diff between canonical constraints and live state**, not a better prompt.

One practical Rx can save ₹5–10k. Ten or more model calls are cheap next to that. Poverty-pricing the compiler (0–2 calls as the *goal*) produces cards nobody executes.

ADR-017 already reserved Path G. ADR-024 already required order/department feasibility, but as **post-hoc negotiation**. L5 internal console already exists for staff debugging (AD-7) but only shows the card + AD-5 gate.

## Decision

1. **Two persistent graphs, same node IDs.**
   - **Graph A (canonical):** slow knowledge graph (topology, owners, isolation, playbooks, typical envelopes, vertical). Refresh every few days or on SOP/asset/tariff-structure change. LLM allowed on that batch; T3 still human-reviewed.
   - **Graph B (live index):** properties on those IDs (running, kW vs typical, orders, ToD/MD, shift). Event-driven. **Zero LLM.** L2 is truth; L4 reads a projection. L4 never `L2_DATABASE_URL`.

2. **Path D (delta)** is a first-class retrieval question: live vs canonical/allowed. Path H stays for playbooks (filter by vertical + class). **Path G trigger is pulled** for relational hops. Microsoft GraphRAG is not the default index.

3. **Quality path is the default compiler** for *all* Finding categories, including the 16 that used to auto-route to Lane A. Loop: bind → Path G → live pull → Path D → Path H → deterministic next-best window → draft → verify/veto → practicality judge → repair. **≥10 generation calls allowed** when quality needs it; not a ceiling. Analyst and Path W stay cost-aware.

4. **Lane A is kept, not default.** Zero-call template graph remains for CI without a provider, `force_lane=a`, `L4_DEFAULT_LANE=template`, and degrade when the structured model is down. Label `provenance.lane = template_fast_path`. Do not delete Lane A. Templates still bound the **action family** on the quality path (`template_id`) — no free-form What rewrite.

5. **ADR-024 feasibility moves into compile.** Negotiation remains for human pushback, not for discovering Job 447 after emit.

6. **L5 stores and displays a compile-trace snapshot.** Do not stuff the subgraph into `prescription.provenance`. New contract `l4-compile-trace`. Internal console (`:8095`) tabs: graph overview, retrieval log, compile loop, eval — **never L6**. Phoenix remains the OTel/LangGraph waterfall (deep link). L5 does **not** own the graph store.

7. **Judge after deterministic gates.** Judge scores practicality language (owner, window, industry specificity), never ₹. Not a sole quality score.

8. **Store.** Postgres property-graph tables later. No Neo4j / Graphiti dependency in this ADR. Roster is optional; degrade to role + shift; never invent names.

9. **Non-tradeables:** **no silent or autonomous OT write** (opt-in human-approved `ActionIntent` only — [ADR-029](ADR-029-human-guided-ot-command-path.md)); calculator-owned money; T4 never sole ₹; L5 owns approval; negotiation never auto-commits.

## Consequences

- Amend [L4 SSOT](../../technical/layers/l4-l6/L4-knowledge-and-reasoning.md), [defense brief](../../technical/layers/l4-l6/L4-decision-defense-brief.md) §2.2 / §3.2 / §3.4 / §3.11, [L4 handoff](../../handoff/l4/stamped-l4-architecture-handoff.md), [L5 SSOT](../../technical/layers/l4-l6/L5-closure-and-verification.md) §15, [internal console handoff](../../handoff/holistic/improve/stamped-l5-internal-console-handoff.md).
- Architecture companion: [L4-plant-context-graphs.md](../../technical/layers/l4-l6/L4-plant-context-graphs.md).
- Contracts: `l4-compile-trace`; sketches for plant-knowledge-graph, plant-live-index, optional shift-roster; additive `compile_trace_id` / `otel_trace_id` / `quality` lane on prescription provenance.
- Consumer code (`knowledge-reasoning`, `closure-verification` console UI) follows a **later platform pin**. This ADR is spec.

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| Keep Lane A as default; spend LLM only on unknown categories | Demo gold fails; generic Due/Who |
| Delete Lane A | CI and model-down degrade still need a 0-call path |
| Full GraphRAG / Graphiti / Neo4j now | Ops cost; steal the pattern, not the product |
| Put graph guts on L6 | Customer Forge is the card, not the compiler |
| L5 owns the graph database | Two truths; L2/L4 ownership split |
| Judge as sole quality score | Masks deterministic ₹ / veto failures |
| Feasibility only via post-hoc negotiation | Too late; supervisor already saw an infeasible Due |
