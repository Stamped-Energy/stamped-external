# ADR-025: Improve loop (step 06) — ML calibration + agent preferences + UI report

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-07-30 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-024](ADR-024-holistic-plant-decisions.md) · [ADR-018](ADR-018-l4-pilot-execution-knowledge-reasoning.md) · [ADR-020](ADR-020-l5-mv-claim-governance.md) · [04-evaluation-and-quality](../technical/cross-cutting/04-evaluation-and-quality.md) · [03-two-pillar-technical-bridge §7](../technical/03-two-pillar-technical-bridge.md) · [`improvement-signal.json`](../contracts/schemas/improvement-signal.json) · [`plant-preference-profile.json`](../contracts/schemas/plant-preference-profile.json) |

---

## Context

The product operating loop was five steps: Connect → Observe → Decide → Execute → Verify. Calibration and supervisor reason codes exist in the eval spine but are not a **named product step**. Negotiation objections, followed-vs-ignored contrasts, and per-plant UI friction are not captured into a single Improve pipeline.

Product lock (2026-07-30): add **step 06 Improve** — simple, plant-scoped, human-gated. Not a new L7 repo.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Loop | Canonical six steps: Connect → Observe → Decide → Execute → Verify → **Improve** |
| 2 | Shape | Cross-cutting monthly job (not L7); lives in L5 or L3-eval `improve/` module |
| 3 | Tracks | **A** ML calibration · **B** agent preference profile · **C** monthly developer UI report |
| 4 | Signals | Append-only `ImprovementSignal` from L5 workflow / ledger / negotiation |
| 5 | Scope | **Plant-scoped only** until ≥20 plants + consent for anonymised fleet aggregates |
| 6 | Gates | Human approval before agent rank / UI layout changes; ML promotion via existing T4 gates |
| 7 | Cadence | Monthly default; weekly optional for calibration math only |
| 8 | Reason codes | Reuse L5 taxonomy — no parallel supervisor labels |

---

## 1. Operating loop (canonical)

| Step | Layers | Improve feedback |
| --- | --- | --- |
| 1 Connect | L1 | — |
| 2 Observe | L2 + L3 | Threshold / baseline updates from Track A |
| 3 Decide | L3 + L4 | Preference profile from Track B |
| 4 Execute | L5 + L6 | UI config pins from Track C (after dev review) |
| 5 Verify | L5 | Ledger calibration points |
| **6 Improve** | Cross-cutting | Reads 4–5; writes plant config |

---

## 2. Three tracks

### Track A — ML (L3)

Threshold tuning from reject/"not real" rates; impact shrinkage from predicted/realised ledger ratios; baseline refresh; champion/challenger promotion (existing MLflow/T4 gates). **No continuous online retrain in P0–P1.**

### Track B — Agent preferences (L4)

Plant preference profile keys: `dept_priority_weights`, `effort_gate`, `evidence_format`, `negotiation_patterns`, `owner_map_corrections`. Built from followed-vs-ignored contrast + negotiation objections. Engineer reviews `PreferenceDelta` before apply.

### Track C — Developer UI report (L6)

Internal monthly markdown/PDF: closure summary, friction hotspots, negotiation themes, evidence gaps, suggested nav pins / card defaults. Developers implement as **plant-scoped L6 config** — not forked code.

---

## 3. Non-goals

- Auto-deploy of new Rx logic without review
- Cross-plant fleet learning in v1 ([ADR-018](ADR-018-l4-pilot-execution-knowledge-reasoning.md) L4 non-goal)
- Customer-facing "AI is learning about you" UX copy in P0
- Seventh layer repository until fleet scale demands it

---

## Consequences

- Contracts: `improvement-signal.json`, `plant-preference-profile.json`
- Spec: [stamped-improve-pipeline-spec.md](../handoff/stamped-improve-pipeline-spec.md)
- Product/docs: six-step loop in `01-product-architecture`, Forge design system, two-pillar §7
- Improve v1 (Phase 2): report + contrast + calibration, no auto-promote
- Improve v2 (Phase 3): preference profile with approval gate

---

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| New L7 Improve service | Premature; one cron job suffices |
| Silent online learning into L4 | Trust / safety / eval regression risk |
| Fleet-wide preference sharing now | Overfits early plants; privacy |
| Real-time UI mutation from Improve | UI churn; monthly report + human apply is enough |
