# Architecture audit — Holistic plant effectiveness (ADR-024 / ADR-025)

> **Date:** 2026-08-05 (reconciled) · Original: 2026-07-30  
> **Scope:** Platform pack (`stamped-external`)  
> **Method:** Ponytail-audit + completeness vs client positioning narrative  
> **Out of scope for this pass:** Full consumer runtime code — tracked in L1–L6 repos under `L1-L6/`

---

## Verdict

**Platform SSOT is current at contracts 0.11.2 / VERSION 2026.08.05 path.**  
Generic-energy pilot path (MD/PF/ToD + `idle_load` + `compressor_sp_drift`) is the first consumer build; order-aware TradeoffEngine / negotiation is **Phase 5**.

**Framing lock:** [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md) — two pillars + shared context. Not MES.

---

## 1. What exists (inventory)

| Layer of truth | Artifact | Status |
| --- | --- | --- |
| Decision | ADR-024 / 025 / 026 / 027 | Accepted |
| Contracts | **0.11.2** — Improve admin + practicality gate profile on `plant-admin-settings` 1.1.0 | Present + fixtures |
| Contracts | 0.10.0–0.10.1 — orders, tradeoff, negotiation workflow events | Present |
| Spec | TradeoffEngine, negotiation, MES/ERP, Improve, pilot stack, **internal console AD-7** | Present under `handoff/` |
| Client narrative | [Stamped_Client_Positioning_and_Narrative_v1.md](../../technical/product/Stamped_Client_Positioning_and_Narrative_v1.md) | Canonical |

**Validation:** `scripts/contracts/contract-check.sh` must stay green.

---

## 2. Ponytail audit

| Tag | Finding |
| --- | --- |
| `yagni:` | No L7 Improve service — weekly job in L5 |
| `yagni:` | Gate profile extends `plant-admin-settings` — no new config DB |
| `native:` | Reuse `pending_stamped_review` / `withheld` / approve / withhold |
| `yagni:` | No Neo4j for department graph |
| — | Lean for platform pack |

**net:** Do not add Improve microservice or fleet-learning store in P1.

---

## 3. Architecture completeness vs operating loop

```
Connect → Observe → Decide → Execute → Verify → Improve
```

| Step | Platform ready? | Consumer (generic-energy first) |
| --- | --- | --- |
| 1 Connect | Meter/bill + optional ProductionOrder | Pilot: meters + bill + idle/compressor tags |
| 2 Observe | Baselines + department graph schema | Pilot: SEC/duty baselines |
| 3 Decide | Dual-pillar Finding + TradeoffEngine spec | Pilot: MD/PF/ToD + idle + compressor_sp; TradeoffEngine → Phase 5 |
| 4 Execute | Negotiation spec + revision schema | Pilot: assign + WhatsApp shadow; Discuss → Phase 5 |
| 5 Verify | Ops-first ADR-020 | Existing L5 path |
| 6 Improve | Weekly ADR-025 + console | Human-gated; full use Phase 5 |

---

## 4. Consistency gaps

| Gap | Severity | Action |
| --- | --- | --- |
| Consumer submodule pins below 2026.08.01 | High | Bump to latest platform before Rx gate work |
| Marketing site may still say five-step | Low | Update stamped.work when messaging ships |
| Negotiation enums | Done | Fixed in contracts 0.10.1 |
| Internal console all-Rx / force-send | Medium | Spec'd in console handoff; implement in L5 consumer |

---

## 5. Generic-energy pilot path (priority)

1. L1 signals for idle + compressor SP  
2. L2 baseline/evidence queries  
3. L3 emit `idle_load` + `compressor_sp_drift` with `value_domain`  
4. L4 templates (already present in knowledge-reasoning)  
5. L5 gate + internal console (all Rx, force send/stop, gate profile)  
6. L6 live BFF approved-only lists  

**Then** Phase 5: ProductionOrder + TradeoffEngine + negotiation + Discuss.

---

## 6. Recommendation

1. Ship platform pin with contracts **0.11.2**.  
2. Use [stamped-holistic-consumer-prompt.md](../agents/prompts/stamped-holistic-consumer-prompt.md).  
3. Do **not** open a seventh layer repo.

---

*Reconciled 2026-08-05 — findings + generic-energy sequencing.*
