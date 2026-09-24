# Holistic pilot stack — L1–L6 deployment checklist

> **Authority:** [ADR-030](../../decisions/028-032/ADR-030-five-domain-decision-loop.md) · [ADR-025](../../decisions/024-026/ADR-025-improve-loop-step-06.md) · [ADR-030](../../decisions/028-032/ADR-030-five-domain-decision-loop.md) · [ADR-029](../../decisions/028-032/ADR-029-human-guided-ot-command-path.md) · [REPOS.md](../../REPOS.md)  
> **Goal:** Integrated pilot — **generic-energy first**, then order-aware, then opt-in desk writeback

---

## 0. Sequencing

| Wave | Scope |
| --- | --- |
| **A — Generic energy** | MD/PF/ToD + `idle_load` + `compressor_sp_drift` â†’ practical Rx â†’ L5 gate/console â†’ L6 live |
| **B — Holistic + desk assign** | ProductionOrder + TradeoffEngine + negotiation + Discuss + weekly Improve; **desk assign/confirm** hardening (no OT write required) |
| **C — Opt-in writeback** | Human-guided ActionIntent â†’ L1 command tags — only after [ot-write-site-checklist.md](./ot-write-site-checklist.md) passes |

Do not block Wave A on Wave B. Do not enable Wave C without the site checklist.

---

## 1. Minimum integrated stack (Wave A)

| Layer | Repo | Pilot must have |
| --- | --- | --- |
| L1 | connectors-edge + cloud (+ bill) | Incomer + key feeders; idle/output tags; compressor kW + pressure; bill MD/PF |
| L2 | universal-repositary | Baselines for SEC/duty; Finding/Prescription ingest |
| L3 | intelligence-core + rulepacks | Emit `idle_load` + `compressor_sp_drift` with `value_domain` |
| L4 | knowledge-reasoning | Templates for those categories + AD-5 fields |
| L5 | closure-verification | Gate scoring; internal console all-Rx; WhatsApp shadow |
| L6 | stamped-l6 / experience-integration | BFF â†’ L5 live; approved-only lists |

Platform pin: `external/VERSION` â‰¥ **2026.08.01** and contracts â‰¥ **0.11.2**. Wave C needs contracts â‰¥ **0.13.0** (`action-intent`, `machine-capability`).

---

## 2. Pre-flight

- [ ] Submodule updated in every consumer
- [ ] `external/scripts/contracts/contract-check.sh` green
- [ ] Deployment profile: `local-dashboard` or `cloud`
- [ ] Plant gate profile loaded (`practicality_gate_mode`, optionally `stamped_rx_gate_enabled=true`)
- [ ] (Wave B only) Department graph + open ProductionOrder with `due_at_utc`
- [ ] (Wave C only) [OT write site checklist](./ot-write-site-checklist.md) signed; `writeback_enabled` only then

---

## 3. Data path smoke (Wave A)

1. L1 publishes measurement envelopes (incomer + idle tags + compressor)  
2. L2 ingest accepts; baseline query returns matched window  
3. L3 emits Finding `idle_load` **and** `compressor_sp_drift` (or MD + one of these) with `value_domain`  
4. L4 emits Prescription with What/Why/Who/Effort/Impact/When + evidence + mv_plan  
5. L5 scores gate; internal console shows Rx (including fail path); WhatsApp optional in shadow  
6. L6 `/prescriptions` lists from L5 (not only fixtures); excludes withheld/pending review  
7. Shadow mode â‰¥2 weeks before WhatsApp on  

---

## 4. Demo â†’ pilot gate (L6)

| Before | After |
| --- | --- |
| Fixtures as sole data | `L5_BASE_URL` + live |
| No staff visibility into bad Rx | L5 Internal Console all-Rx + diagnostics |
| Improve N/A | Weekly ImproveCycle dry-run |
| Execute button for all plants | Execute only when Wave C + capability; else Assign |

Keep fixtures as offline / CI when `USE_FIXTURES=1`.

---

## 5. Pilot success metrics

| Metric | Target `[~]` |
| --- | --- |
| â‰¥1 Pillar 1 + â‰¥1 Pillar 2 finding | Yes |
| Client Rx has verification + feasibility fields | 100% |
| Incomplete Rx withheld from L6 | 100% |
| Internal console shows all Rx | Yes |
| Force send/stop audited | 100% |
| Order-aware stagger | Wave B |
| Desk assign/confirm used for high-₹ Rx | Wave B |
| ActionIntent verified on beachhead command | Wave C (opt-in site) |

---

## 6. Explicit out of scope (Wave A)

- Named SAP PM write-back  
- TradeoffEngine / Discuss / ProductionOrder dependency  
- Cross-plant Improve fleet learning  
- **OT / SCADA write enablement** (deferred to Wave C + site checklist — [ADR-029](../../decisions/028-032/ADR-029-human-guided-ot-command-path.md))  
- Autonomous execute-within-limits  
- Direct VFD/servo / e-stop via Stamped  
