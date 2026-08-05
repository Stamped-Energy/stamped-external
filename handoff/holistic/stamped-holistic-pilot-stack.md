# Holistic pilot stack — L1–L6 deployment checklist

> **Authority:** [ADR-024](../../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [ADR-025](../../decisions/024-026/ADR-025-improve-loop-step-06.md) · [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md) · [REPOS.md](../../REPOS.md)  
> **Goal:** Integrated pilot — **generic-energy first**, then order-aware (Phase 5)

---

## 0. Sequencing

| Wave | Scope |
| --- | --- |
| **A — Generic energy** | MD/PF/ToD + `idle_load` + `compressor_sp_drift` → practical Rx → L5 gate/console → L6 live |
| **B — Holistic** | ProductionOrder + TradeoffEngine + negotiation + Discuss + weekly Improve full |

Do not block Wave A on Wave B.

---

## 1. Minimum integrated stack (Wave A)

| Layer | Repo | Pilot must have |
| --- | --- | --- |
| L1 | connectors-edge + cloud (+ bill) | Incomer + key feeders; idle/output tags; compressor kW + pressure; bill MD/PF |
| L2 | universal-repositary | Baselines for SEC/duty; Finding/Prescription ingest |
| L3 | intelligence-core + rulepacks | Emit `idle_load` + `compressor_sp_drift` with `value_domain` |
| L4 | knowledge-reasoning | Templates for those categories + AD-5 fields |
| L5 | closure-verification | Gate scoring; internal console all-Rx; WhatsApp shadow |
| L6 | stamped-l6 / experience-integration | BFF → L5 live; approved-only lists |

Platform pin: `external/VERSION` ≥ **2026.08.01** and contracts ≥ **0.11.2**.

---

## 2. Pre-flight

- [ ] Submodule updated in every consumer
- [ ] `external/scripts/contracts/contract-check.sh` green
- [ ] Deployment profile: `local-dashboard` or `cloud`
- [ ] Plant gate profile loaded (`practicality_gate_mode`, optionally `stamped_rx_gate_enabled=true`)
- [ ] (Wave B only) Department graph + open ProductionOrder with `due_at_utc`

---

## 3. Data path smoke (Wave A)

1. L1 publishes measurement envelopes (incomer + idle tags + compressor)  
2. L2 ingest accepts; baseline query returns matched window  
3. L3 emits Finding `idle_load` **and** `compressor_sp_drift` (or MD + one of these) with `value_domain`  
4. L4 emits Prescription with What/Why/Who/Effort/Impact/When + evidence + mv_plan  
5. L5 scores gate; internal console shows Rx (including fail path); WhatsApp optional in shadow  
6. L6 `/prescriptions` lists from L5 (not only fixtures); excludes withheld/pending review  
7. Shadow mode ≥2 weeks before WhatsApp on  

---

## 4. Demo → pilot gate (L6)

| Before | After |
| --- | --- |
| Fixtures as sole data | `L5_BASE_URL` + live |
| No staff visibility into bad Rx | L5 Internal Console all-Rx + diagnostics |
| Improve N/A | Weekly ImproveCycle dry-run |

Keep fixtures as offline / CI when `USE_FIXTURES=1`.

---

## 5. Pilot success metrics

| Metric | Target `[~]` |
| --- | --- |
| ≥1 Pillar 1 + ≥1 Pillar 2 finding | Yes |
| Client Rx has verification + feasibility fields | 100% |
| Incomplete Rx withheld from L6 | 100% |
| Internal console shows all Rx | Yes |
| Force send/stop audited | 100% |
| Order-aware stagger | Wave B |

---

## 6. Explicit out of scope (Wave A)

- Named SAP PM write-back  
- TradeoffEngine / Discuss / ProductionOrder dependency  
- Cross-plant Improve fleet learning  
- OT control writes  
