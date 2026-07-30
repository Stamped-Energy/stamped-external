# Architecture audit — Holistic plant effectiveness (ADR-024 / ADR-025)

> **Date:** 2026-07-30  
> **Scope:** Platform pack (`stamped-external`) after Phase 0 holistic ideation deliverables  
> **Method:** Ponytail-audit (over-engineering) + architecture completeness vs plan  
> **Out of scope for this pass:** Consumer runtime code (L1–L6 product repos) — intentionally not built yet

---

## Verdict

**Phase 0 platform SSOT is complete and lean enough to ship as contracts + ADRs + handoffs.**  
Consumer implementation has **not** started — that is correct per plan (“no consumer code until ADR + contract bump”). The gap is **execution in product repos**, not missing platform docs.

**Framing lock (2026-07-30):** [ADR-026](../decisions/ADR-026-two-pillars-shared-context.md) — one product, **two pillars**, shared context. Holistic artifacts are **not** a third pillar or MES product. Efficiency (₹) is hero; effectiveness (OEE/order/downtime) is co-benefit language.

---

## 1. What exists (inventory)

| Layer of truth | Artifact | Status |
| --- | --- | --- |
| Decision | [ADR-024](../decisions/ADR-024-holistic-plant-decisions.md) | Accepted |
| Decision | [ADR-026](../decisions/ADR-026-two-pillars-shared-context.md) | Accepted — framing lock |
| Contract 0.10.0 | `production-order`, `prescription-revision`, `improvement-signal`, `plant-preference-profile`, `plant-department-graph` | Present + fixtures |
| Contract | `production-record` 1.1.0; Rx/Finding `decision_class`; Rx `tradeoff` | Present |
| Spec | TradeoffEngine, negotiation, MES/ERP, Improve pipeline, pilot stack, report template | Present under `handoff/` |
| Product copy | Six-step loop in `01-product-architecture`, Forge, two-pillar §7, L2 store table | Updated |

**Validation:** All paired fixtures in `scripts/contract-check.sh` validate against schemas (2026-07-30).

---

## 2. Ponytail audit (complexity / YAGNI)

Ranked findings on the **platform pack only** (what we added):

| Tag | Finding |
| --- | --- |
| `yagni:` | **No L7 Improve service** — ADR-025 correctly keeps one monthly job. Keep it that way. |
| `yagni:` | `plant-preference-profile` + `improvement-signal` are two schemas — justified (config vs event). Do not merge. |
| `shrink:` | Negotiation + Analyst are separate surfaces — correct; do not unify into one “chat god” API. |
| `delete:` | Nothing speculative in contracts that consumers must implement tomorrow except optional fields — good. |
| `yagni:` | `PlantDepartmentGraph` is config, not a graph DB — keep as JSON/Postgres rows; do **not** add Neo4j. |
| — | **Lean already for Phase 0.** Ship platform pin; build consumers against it. |

**net:** 0 lines to delete in platform SSOT; **do not** add an Improve microservice or fleet-learning store in P1.

---

## 3. Architecture completeness vs operating loop

```
Connect → Observe → Decide → Execute → Verify → Improve
```

| Step | Platform ready? | Consumer ready? |
| --- | --- | --- |
| 1 Connect | MES/ERP brief + `ProductionOrder` schema | **No** — L1 CSV/OData not wired |
| 2 Observe | Department graph schema; L2 doc updated | **No** — L2 store/API for orders/graph |
| 3 Decide | TradeoffEngine spec; `decision_class`/`tradeoff` | **No** — L3 engine + rulepack params |
| 4 Execute | Negotiation spec; revision schema | **No** — L4 API + L5 workflow + L6 Discuss |
| 5 Verify | Unchanged (ADR-020 ops-first) | Existing L5 path |
| 6 Improve | ADR-025 + pipeline + report template | **No** — monthly job not coded |

**Binding risks if consumers skip reading order:**

1. Implementing stagger without TradeoffEngine → energy-only Rx still breaks plant trust.  
2. Free-form LLM “rewrite What” instead of `prescription-revision` → safety regression.  
3. Auto-applying Improve preferences without `approval.status=approved` → silent behavior change.  
4. Building MES dispatch UI → violates ADR-024 non-goals.

---

## 4. Consistency gaps (fix before / during consumer work)

| Gap | Severity | Action |
| --- | --- | --- |
| Platform `VERSION` still `2026.07.12` while contracts are **0.10.0** | Medium | Tag release (e.g. `v2026.07.30`) and bump `VERSION` when merging to consumers |
| Finding `schema_version` still `1.2.0` with additive `decision_class` | Low | OK (BACKWARD); document in consumer prompts |
| Prescription nested inside `prescription-revision.revised_prescription` is loosely typed (`object`) | Low | Acceptable P0; tighten with `$ref` later if validators need it |
| Marketing site / how-it-works still says five-step | Low | Update stamped.work copy when product messaging ships |
| `connectors-bill-ui-ux-charter` still says “five-step” | Low | Align on next bill UI pass |
| No workflow-event enum values for `prescription.revised` yet | Medium | Add in contracts when L5 implements negotiation (or extend now if preferred) |

---

## 5. Per-repo work map (for planning agents)

| Repo | Primary read | Build focus |
| --- | --- | --- |
| connectors-edge / cloud | MES/ERP brief | Ingest `production_order` / CSV MES-lite |
| universal-repositary (L2) | Department graph + ProductionOrder | Store + query APIs |
| intelligence-core / rulepacks | TradeoffEngine spec | Deadline-aware stagger/TOD/preheat |
| knowledge-reasoning (L4) | Negotiation spec | `/v1/negotiation/revise` |
| closure-verification (L5) | Negotiation + Improve pipeline | Revision workflow + Improve signals/job |
| stamped-l6 | Negotiation UX + pilot stack | Discuss panel; BFF live; fixtures fallback |

**Single form for all of the above:** [stamped-holistic-consumer-prompt.md](./stamped-holistic-consumer-prompt.md)

---

## 6. Recommendation

1. **Commit/tag** stamped-external with contracts 0.10.0 + ADR-024/025 (if not already).  
2. Give each consumer agent the **holistic consumer prompt** (one form).  
3. Implement Phase 1 (orders + TradeoffEngine) before Phase 2 (negotiation + Improve v1).  
4. Do **not** open a seventh layer repo.

---

*End of audit — findings only; no consumer code changes in this pass.*
