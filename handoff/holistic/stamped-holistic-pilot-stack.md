# Holistic pilot stack — L1–L6 deployment checklist

> **Authority:** [ADR-024](../../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [ADR-025](../../decisions/024-026/ADR-025-improve-loop-step-06.md) · [REPOS.md](../REPOS.md) · [deployment-profiles.md](./deployment-profiles.md)  
> **Goal:** Replace fixture-only L6 demo with an integrated Path B (or A) pilot

---

## 1. Minimum integrated stack

| Layer | Repo | Pilot must have |
| --- | --- | --- |
| L1 | connectors-edge + cloud (+ bill) | Incomer meter + bill; production CSV **or** ERP export |
| L2 | universal-repositary | `ProductionRecord` 1.1+, `ProductionOrder`, department graph config |
| L3 | intelligence-core + rulepacks | TradeoffEngine on `stagger_costart` / TOD / preheat |
| L4 | knowledge-reasoning | Prescription templates + negotiation API (Phase 2) |
| L5 | closure-verification | Workflow + Improve signal emit |
| L6 | stamped-l6 | BFF → L5 live; fixtures = fallback only |

Platform pin: run `git -C external describe --tags` and `external/VERSION`; bump submodule after contracts **0.10.0**.

---

## 2. Pre-flight

- [ ] `git submodule update --init --recursive` in every consumer
- [ ] `external/scripts/contracts/contract-check.sh` green
- [ ] Deployment profile chosen: `local-dashboard` or `cloud` ([ADR-010](../../decisions/006-010/ADR-010-deployment-profiles-and-portability.md))
- [ ] Plant department graph loaded (fixture → real)
- [ ] At least one open ProductionOrder with `due_at_utc` for trade-off demo

---

## 3. Data path smoke

1. L1 publishes measurement + production_order envelopes  
2. L2 ingest 8090 accepts; query returns order  
3. L3 emits Finding `md_overlap` with tradeoff-ready assets  
4. L4 emits Prescription with `decision_class=mgmt_schedule` + `tradeoff`  
5. L5 queue shows Rx; WhatsApp optional in shadow  
6. L6 `/prescriptions` lists from L5 (not only `demo.ts`)  
7. Shadow mode ≥2 weeks before WhatsApp on ([02-technical-architecture §17.2](../../technical/STAMPED_ARCHITECTURE.md))

---

## 4. Demo → pilot gate (L6)

| Before | After |
| --- | --- |
| [`consumers/stamped-l6` fixtures](../consumers/stamped-l6/src/fixtures/demo.ts) as sole data | BFF env `L5_BASE_URL` + SSE |
| Negotiation UI mocked | Fixture negotiation → then live L4 |
| Improve report N/A | Monthly job dry-run on workflow fixtures |

Keep fixtures as **offline / Storybook / CI** mode when `USE_FIXTURES=1`.

---

## 5. Pilot success metrics (holistic)

| Metric | Target `[~]` |
| --- | --- |
| Order-aware stagger Rx | ≥1 plant live |
| Mgmt Rx with `order_context≠unknown` when orders loaded | 100% |
| Negotiation resolves defer/dispute | ≥30% (Phase 2) |
| First Improve monthly report | Generated for pilot plant |
| Hero narrative | ₹ energy primary; order co-benefit secondary |

---

## 6. Explicit out of scope for first pilot

- Named SAP PM write-back  
- Cross-plant Improve fleet learning  
- Full department Gantt as MES replacement  
- OT control writes  
