# ADR-025: Improve loop (step 06) — ML calibration + agent preferences

| Field | Value |
| --- | --- |
| **Status** | Accepted (revised 2026-08-01) |
| **Date** | 2026-07-30 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-024](ADR-024-holistic-plant-decisions.md) · [ADR-027](ADR-027-plant-calibration-champion-promote.md) · [ADR-018](../016-020/ADR-018-l4-pilot-execution-knowledge-reasoning.md) · [ADR-020](../020-023/ADR-020-l5-mv-claim-governance.md) · [04-evaluation-and-quality](../../technical/cross-cutting/04-evaluation-and-quality.md) · [`improvement-signal.json`](../../contracts/schemas/closure/improvement-signal.json) · [`plant-preference-profile.json`](../../contracts/schemas/plant/plant-preference-profile.json) · [`improve-cycle.json`](../../contracts/schemas/closure/improve-cycle.json) |

---

## Context

The product operating loop was five steps: Connect → Observe → Decide → Execute → Verify. Calibration and supervisor reason codes exist in the eval spine but are not a **named product step**. Negotiation objections, followed-vs-ignored contrasts, and richer outcome signals are not captured into a single Improve pipeline.

Product lock: add **step 06 Improve** — plant-scoped, **human-gated on every cycle**. Not a new L7 repo.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Loop | Canonical six steps: Connect → Observe → Decide → Execute → Verify → **Improve** |
| 2 | Shape | Cross-cutting weekly job in L5 `improve/` module |
| 3 | Tracks | **A** ML calibration + fine-tune/shadow · **B** agent preference profile |
| 4 | Signals | Append-only `ImprovementSignal` from L5 workflow / ledger / negotiation / admin |
| 5 | Scope | **Plant-scoped only** until ≥20 plants + consent for anonymised fleet aggregates |
| 6 | Gates | **Human approval on every ImproveCycle** before Track A/B apply; ML promote via ADR-027 |
| 7 | Cadence | **Weekly** per plant |
| 8 | Rx gate | Optional `stamped_rx_gate_enabled` — staff approve before client sees Rx |
| 9 | UI | L5 Internal Console (Stamped staff only); plant notes scratchpad (manual, not automated Track C) |

---

## 1. Operating loop (canonical)

| Step | Layers | Improve feedback |
| --- | --- | --- |
| 1 Connect | L1 | — |
| 2 Observe | L2 + L3 | Threshold / baseline updates from Track A (after human approve) |
| 3 Decide | L3 + L4 | Preference profile from Track B (after human approve) |
| 4 Execute | L5 + L6 | Rx delivery; optional Stamped pre-review gate |
| 5 Verify | L5 | Ledger calibration points |
| **6 Improve** | L5 + L3 | Reads 4–5; writes draft cycles; staff approve |

---

## 2. Two tracks

### Track A — ML calibration + fine-tune loop (L3 + L5)

Threshold tuning from reject/"not real" rates; impact shrinkage from predicted/realised ledger ratios; plant fine-tune on customer data → shadow → human promote ([ADR-027](ADR-027-plant-calibration-champion-promote.md)). **No continuous online retrain in P0.**

### Track B — Agent preferences (L4)

Plant preference profile keys: `dept_priority_weights`, `effort_gate`, `evidence_format`, `negotiation_patterns`, `owner_map_corrections`. Built from followed-vs-ignored contrast + negotiation + richer signals. Staff approve in L5 console before L4 apply.

### Plant notes (manual)

Staff jot plant down-points in L5 Internal Console. Not consumed by Improve job. UI/config changes applied manually by engineering.

---

## 3. Non-goals

- Auto-deploy of new Rx logic or model weights without review
- Cross-plant fleet learning in v1
- Customer-facing "AI is learning about you" UX copy in P0
- Automated developer UI report (former Track C)
- Seventh layer repository

---

## Consequences

- Contracts: `improvement-signal.json` 1.1.0, `improve-cycle.json`, `calibration-patch.json`, `model-run.json`, `plant-admin-settings.json`
- Spec: [stamped-improve-pipeline-spec.md](../../handoff/holistic/improve/stamped-improve-pipeline-spec.md)
- L5 Internal Console for Improve cycles, Rx gate, ML promote

---

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| New L7 Improve service | Premature; L5 job + console suffices |
| Silent online learning into L4 | Trust / safety risk |
| Track C automated markdown report | Replaced by manual plant notes UI |
| Improve in L6 customer nav | Wrong audience |
