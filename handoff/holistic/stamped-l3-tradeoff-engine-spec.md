# L3 TradeoffEngine — deadline & department-aware ranking

> **Authority:** [ADR-024](../../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [L3 intelligence core](../../technical/layers/l3/L3-intelligence-core.md) · contracts: [`production-order.json`](../../contracts/schemas/plant/production-order.json), [`plant-department-graph.json`](../../contracts/schemas/plant/plant-department-graph.json), prescription `tradeoff`  
> **Audience:** intelligence-core / rulepacks agents  
> **Status:** Spec for P1 build — not yet in consumer runtime

---

## 1. Mission

Given a management-class Finding (stagger, TOD shift, shed, preheat timing), produce a **ranked set of bounded action options** that maximise energy/₹ benefit **subject to** open order deadlines and department incentive weights.

Deterministic numbers only. L4 formats prose and attaches the trade-off block to the Prescription.

---

## 2. Inputs

| Input | Source |
| --- | --- |
| Finding | L3 lane A (`delivery=l4`) |
| Open `ProductionOrder`s overlapping action window | L2 commercial context |
| `PlantDepartmentGraph` | L2 config store |
| Tariff / MD peak window | L2 + tariff engine |
| Candidate templates | Rulepack action library (`stagger_costart`, `load_shift_tod`, shed templates, `furnace_preheat_early`) |

---

## 3. Algorithm (v1 — boring)

```
1. Enumerate template-parameterised candidates (e.g. stagger_min ∈ {5,8,12};
   exclude_line_ids ∈ subsets that still break coincidence).
2. For each candidate:
   a. Simulate peak kVA / TOD exposure / holding kWh (existing simulators).
   b. Compute energy_benefit_inr via impact calculator.
   c. Collect orders on affected lines with due_at in [now, window_end].
   d. If any protected order (hot=true OR priority≤2 OR due within action delay):
        mark order_conflict; apply throughput_risk score.
   e. Weight by department incentive_weight.energy vs throughput.
3. Discard candidates that hit critical_assets without override flag.
4. Rank: score = energy_benefit_inr * energy_weight
              - order_risk_penalty * throughput_weight
5. Emit top-N (default 3) with tradeoff object + alternatives[].
6. If no ProductionOrder context: order_context=unknown; widen CI; do not invent due dates.
```

**Order risk penalty (P0 heuristic):** `minutes_of_delay_implied * orders_at_risk * priority_factor`. Document formula in rulepack `formula_ref`; tune via Improve Track A.

---

## 4. Outputs

Attached to Finding extras or L4 tool result → Prescription.tradeoff:

| Field | Required for mgmt_* |
| --- | --- |
| `energy_benefit_inr_monthly` | Yes |
| `throughput_risk` | Yes (string; may be "none detected") |
| `order_context` | Yes (`known` \| `partial` \| `unknown`) |
| `order_ids` | When known |
| `recommended_window` | Yes |
| `alternatives` | ≥1 when primary has order conflict |
| `department_owners` | Yes |

---

## 5. Rulepack touch points

| Rule | Change |
| --- | --- |
| `stagger_costart` | Call TradeoffEngine; prefer v2 params that exclude hot lines |
| `load_shift_tod` | Check order due windows before TOD shift recommend |
| `furnace_preheat_early` | Align preheat start to MES charge **and** order due |
| Shed templates | Prefer utilities / non-critical over production lines |

Suppressions already include `production_mix_change` — keep; add `order_deadline_block` when no safe alternative exists (emit Finding with `decision_class` but `delivery=lab_only` or low urgency Rx "monitor only").

---

## 6. Non-goals

- Optimal plant-wide MILP schedule
- Owning MES dispatch
- Learning weights online without Improve approval (ADR-025)

---

## 7. Acceptance (pilot)

1. With fixture plant graph + PO-8842 due 14:00, stagger Rx **must not** recommend Line 2 stagger before 14:00 as primary.
2. Alternative (Line 3 only or HVAC shed) appears in `alternatives[]`.
3. Without orders loaded, Rx still emits with `order_context=unknown`.
