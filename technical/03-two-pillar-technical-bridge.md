---
type: Product Architecture
title: "Stamped Energy — Two-Pillar Technical Bridge (L0–L6)"
description: "Maps Load & Energy Efficiency Intelligence and Prescriptive Equipment Intelligence onto the existing L0–L6 stack — Finding tags, engine ownership, verification paths, Improve loop, and minimal eng gaps. No layer rewrite."
tags: [stamped-energy, technical, two-pillar, load-management, equipment-intelligence]
timestamp: "2026-07-26T11:30:00Z"
---

# Two-Pillar Technical Bridge (L0–L6)

*Companion to research-repo canon: `Stamped_Two_Pillar_Technical_Framing_v1.md` (stamped-energy `core-product/`).*  
*Read after [02-technical-architecture.md](02-technical-architecture.md). Does **not** replace layer specs — it tags how product pillars sit on the stack.*

**Honesty:** `[~]` approximate · `[!]` evolving.

---

## 1. Purpose

Founders explain Stamped Intelligence in **two technical sections** on calls:

1. **Load & Energy Efficiency Intelligence** (Pillar 1)  
2. **Prescriptive Equipment Intelligence** (Pillar 2)

Engineering still builds **one** L0–L6 system. This bridge answers: which engines, Finding tags, verification paths, and small schema/rulepack changes are needed so the two sections are real — not just slides.

**Non-goals:** website redesign, CNN models, vibration PdM, full computerized maintenance management system, OT write-back.

---

## 2. What stays identical

| Decision | Status |
| --- | --- |
| Read-only on OT (L0) | Unchanged |
| L1–L6 layer boundaries | Unchanged |
| Event flow `Measurement → Finding → Prescription → LedgerEntry / WorkflowEvent` | Unchanged |
| Human-in-the-loop WhatsApp + dashboard (L5/L6) | Unchanged |
| **Verified with evidence** as commercial trust anchor | Unchanged (ops-cleared ledger primary; DISCOM bill optional secondary — never lead with “bill-verified”) |
| Not an in-house vibration predictive-maintenance company | Unchanged |
| Four client deck pillars (Physics / Models / Agents / Closure) in [stamped-research-and-ml-citations.md](stamped-research-and-ml-citations.md) | Compatible — product pillars are a *different* cut (outcomes); deck pillars remain *how we reason* |

---

## 3. Layer map

```
L0  Plant systems (shared)
L1  Connect & normalise (shared)
L2  Universal Repository (shared)
L3  Intelligence core ──┬── Pillar 1 engines (demand, tariff, pure waste, thermal timing, source-mix)
                        └── Pillar 2 engines (specific-power maintenance drift, trip/duty, coarse signature)
L4  Knowledge & reasoning (shared prescription agent; template packs split by pillar)
L5  Closure & verification (shared workflow; Verify path branches by pillar)
L6  Experience (shared UX; optional pillar filters on queue)
```

| Layer | Shared vs split | Notes |
| --- | --- | --- |
| **L0** | Shared | Meters, SCADA, PLC, bills — same taps |
| **L1** | Shared | Normalisation unchanged |
| **L2** | Shared | Time-series, energy graph, commercial context, baselines, ledger |
| **L3** | **Split by engine / Finding tag** | Same numeric layer; tag `pillar` or `value_domain` on Findings |
| **L4** | Shared agent, **split playbooks** | Rule/RAG packs: `energy_efficiency/*` vs `equipment_health/*` |
| **L5** | Shared workflow; **Verify branch** | Evidence M&V (ops-cleared) for both; bill confirmation optional for some Pillar 1 wins; maintenance closure + post-action curve for Pillar 2 |
| **L6** | Shared | Filter prescription queue by pillar; one plant dashboard |

---

## 4. Pillar 1 → L3 engines (technique families A–E)

Product technique families from the framing canon:

| Family | Techniques (abbrev.) | Primary L3 engines | Example Finding categories |
| --- | --- | --- | --- |
| **A** Peak & coincidence | Forecast, attribution, stagger, shed, soft MD/CMD | Demand/MD · Attribution · Rules | `md_spike_coincidence`, `md_forecast_breach`, `stagger_opportunity` |
| **B** Tariff & commercial | TOD shift, CMD sizing, PF ops, bill M&V | Tariff/PF · Bill context (L1/L2) | `tod_shift_opportunity`, `cmd_oversized`, `pf_penalty_ops` |
| **C** Thermal & process timing | Preheat/precool, hold setback, batch–TOD | Rules/physics · Baseline · Calendar | `furnace_hold_waste`, `preheat_too_early` |
| **D** Pure energy waste | Idle kill, off-shift HVAC, artificial air demand (ops) | Waste classifier · Anomaly · Baseline | `idle_offshift`, `hvac_empty_hall`, `air_pressure_setpoint` |
| **E** Source mix | Solar/grid/WHR/DG dispatch | Source-mix (P1 build) | `solar_export_mismatch`, `dg_vs_grid` |

**Grey-zone:** if the prescribed action is **inspect/clean/repair** (e.g. filter), tag Pillar 2 even if ₹ energy is large — see §6.

**Capability modules ([01-product-architecture](01-product-architecture.md)) → Pillar 1:** modules 2 (baseline/SEC as efficiency), 3 (demand), 4 (tariff), 5 (utility waste when action is ops/schedule), plus 6–8 shared.

---

## 5. Pillar 2 → L3 engines (technique families F–J)

| Family | Techniques (abbrev.) | Primary L3 engines | Example Finding categories |
| --- | --- | --- | --- |
| **F** Efficiency drift → maintenance | Specific-power drift, utility performance drift, leak survey proxy | Rules (compressor/chiller/furnace packs) · Anomaly | `compressor_sp_drift_maint`, `chiller_kw_per_tr_drift`, `air_leak_survey_focus` |
| **G** Trip / duty early warning | Trip clusters, abnormal duty, startup signature change | Anomaly · Rules · Attribution | `trip_cascade_risk`, `heater_on_while_idle_inspect` |
| **H** Coarse load signature | Imbalance / unexplained continuous draw (SCADA tags) | Anomaly · Graph | `feeder_unexplained_draw` |
| **I** True condition monitoring | Motor current signature analysis, vibration, RUL % | — | **Out of L3 v1** — partner feed later |
| **J** Full CMMS | Parts, labour, inventory, auto WO write-back | — | **Out of scope** (L5 WhatsApp is enough) |

**Capability modules → Pillar 2:** slice of module 5 where action is maintenance work; prescription/execution/verification (6–8) shared; optional equipment-health map already sketched in L6 UX.

**Honest non-build:** do not add kilohertz motor current signature analysis pipelines to L1/L3 in P0–P1. 1–15 minute meters + SCADA tags only.

---

## 6. Finding taxonomy change (minimal)

Today Findings carry waste-category style tags (see [L3](layers/L3-intelligence-core.md)). Add a **value-domain** (name flexible) without breaking contracts:

| Field | Values | Rule |
| --- | --- | --- |
| `value_domain` `[!]` | `energy_efficiency` \| `equipment_health` | Required on new Findings once rolled out |
| Existing `category` / `waste_category` | Keep | Still used for savings math and playbooks |

**Assignment rule (grey-zone):**

1. Primary action is schedule / setpoint / stagger / shutdown / tariff → `energy_efficiency`  
2. Primary action is inspect / clean / repair / replace / AMC check / leak survey → `equipment_health`  
3. If both plausible → prefer `equipment_health` when the work is routine maintenance; else `energy_efficiency`

L4 uses `value_domain` to select playbook corpus and prescription template tone. L5/L6 can filter queues.

**Contract note:** additive optional field first (backward compatible); promote to required after fixtures updated — bump `contracts/CHANGELOG.md` when schema lands. Until then, eng can use a parallel config map `category → value_domain`.

---

## 7. Prescription, Verify, Improve

| Path | Pillar 1 (`energy_efficiency`) | Pillar 2 (`equipment_health`) |
| --- | --- | --- |
| **L4 output** | Rx with ₹ energy-cost impact primary | Rx with risk / maintenance action primary; ₹ optional co-benefit |
| **L5 Execute** | Same WhatsApp / owner workflow | Same |
| **L5 Verify** | **Mandatory** ops-cleared evidence / potential vs realised ledger; DISCOM bill **optional** secondary | Maintenance closure + post-action curve (e.g. specific power recovery); bill optional |
| **L5 Improve (loop 06)** | Acted vs ignored → MD/waste ranking | Acted vs ignored → early-warning thresholds / false-positive suppression |
| **Commercial SOW** | 60-Day Proof Run / **verified with evidence** success clause (not “bill verification program”) | Same — ops-cleared evidence; avoided downtime need not appear on the invoice |

Improve maps to existing calibration / suppression / HITL feedback patterns in L3/L4/L5 — not a new layer. Document as explicit product step **06 Improve** in UX copy.

---

## 8. Module regrouping (product arch view)

For decks and [01-product-architecture](01-product-architecture.md) alignment (no need to renumber modules immediately):

| Pillar | Modules / engines |
| --- | --- |
| Shared | 1 Connect · 6 Prescription · 7 Execution · 8 M&V · 9 Benchmark · 10 Sustainability export |
| Pillar 1 | 2 Baseline/SEC (efficiency) · 3 Demand · 4 Tariff · 5 Utility waste (**ops** actions) · source-mix |
| Pillar 2 | 5 Utility waste (**maintenance** actions) · trip/duty packs · equipment-health anomaly |

---

## 9. Build priority (aligned with framing, not a new roadmap)

| Priority | Capability | Pillar |
| ---: | --- | --- |
| P0 | MD forecast + spike post-mortem + stagger Rx | 1 |
| P0 | Idle / off-shift pure waste Rx | 1 |
| P0 | Prescription card + owner + WhatsApp | Shared |
| P0 | Evidence M&V ledger (ops-cleared; bill confirmation optional) | 1 (+ optional energy co-benefit for 2) |
| P0–P1 | Specific-power early warning → maintenance Rx (filter/fouling) | 2 |
| P1 | Feeder MD attribution; TOD/CMD/PF; thermal timing setback | 1 |
| P1 | Trip/duty early warnings | 2 |
| P2 | Soft shed confirm; source-mix; vibration/temp partner feed | 1 / 2 |
| P3 | CMMS write-back | 2 edge |
| — | Motor current signature analysis / in-house vibration / OT write | **Do not build yet** |

---

## 10. Engineering gap list (minimal)

| Gap | Action | Urgency |
| --- | --- | --- |
| `value_domain` on Finding (or category→domain map) | **Done in contracts 0.9.0 / Finding 1.2.0** — required `value_domain` + equipment-health categories | — |
| Rulepack ownership folders | `domain/energy_efficiency/*` vs `domain/equipment_health/*` (or tags on existing packs) | P0 |
| L4 playbook split | Separate retrieval namespaces / templates per domain | P1 |
| L5 Verify branch | Maintenance evidence fields on ledger / workflow (optional downtime / curve recovery) | P1 |
| L6 queue filter | Pillar / domain filter chip | P1 |
| Improve metrics | Acted / ignored / false-positive rates per domain into calibration | P1 |
| Partner PdM ingest | Consume third-party vibration/MCSA as Findings tagged `equipment_health` | P2 (already product-arch intent) |

**No layer rewrite required.** No new L3 “CNN” path. Prefer rules + baselines already specified in [L3-intelligence-core.md](layers/L3-intelligence-core.md).

---

## 11. Cross-links

| Doc | Role |
| --- | --- |
| Research canon (stamped-energy) | `core-product/Stamped_Two_Pillar_Technical_Framing_v1.md` — names, taxonomies A–J, grey-zone, loop 01–06 |
| [01-product-architecture.md](01-product-architecture.md) | Modules → layers |
| [02-technical-architecture.md](02-technical-architecture.md) | Engineering SSOT |
| [L3](layers/L3-intelligence-core.md) | Engines and Finding shape |
| [L5](layers/L5-closure-and-verification.md) | Workflow, WhatsApp, M&V |
| [stamped-research-and-ml-citations.md](stamped-research-and-ml-citations.md) | Client Physics/Models/Agents/Closure narrative |

---

*End of bridge — keep layers stable; split value domains in Findings and playbooks.*
