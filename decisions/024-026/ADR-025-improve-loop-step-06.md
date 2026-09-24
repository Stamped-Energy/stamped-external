# ADR-025: Learning from closed cards — ML calibration + agent preferences

| Field | Value |
| --- | --- |
| **Status** | Accepted (revised 2026-08-01; identity revised 2026-09-24) |
| **Date** | 2026-07-30 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-030](../028-032/ADR-030-five-domain-decision-loop.md) · [ADR-027](ADR-027-plant-calibration-champion-promote.md) · [ADR-018](../016-020/ADR-018-l4-pilot-execution-knowledge-reasoning.md) · [ADR-020](../020-023/ADR-020-l5-mv-claim-governance.md) · [04-evaluation-and-quality](../../technical/cross-cutting/04-evaluation-and-quality.md) · [`improvement-signal.json`](../../contracts/schemas/closure/improvement-signal.json) · [`plant-preference-profile.json`](../../contracts/schemas/plant/plant-preference-profile.json) · [`improve-cycle.json`](../../contracts/schemas/closure/improve-cycle.json) |

---

## Context

The product loop is **detect → recommend → assign → act → verify**, with optional **propose learning** after close ([ADR-030](../028-032/ADR-030-five-domain-decision-loop.md)). Verified, no-change, and rejected cards are all learning events. A production threshold still needs named-owner acceptance.

This ADR names the L5 Improve job that turns closed-card signals into draft calibration and preference updates — plant-scoped, **human-gated on every cycle**. Not a new L7 repo. Not an energy-savings pitch.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Loop | Closed cards feed Improve; default product loop remains recommend/assign/verify |
| 2 | Shape | Cross-cutting weekly job in L5 `improve/` module |
| 3 | Tracks | **A** ML calibration + fine-tune/shadow · **B** agent preference profile |
| 4 | Signals | Append-only `ImprovementSignal` from L5 workflow / ledger / negotiation / admin |
| 5 | Scope | **Plant-scoped only** until ≥20 plants + consent for anonymised fleet aggregates |
| 6 | Gates | **Human approval on every ImproveCycle** before Track A/B apply; ML promote via ADR-027 |
| 7 | Cadence | **Weekly** per plant |
| 8 | Card gate | Optional `stamped_rx_gate_enabled` — staff approve before client sees a card |
| 9 | UI | L5 Internal Console (Stamped staff only); plant notes scratchpad (manual) |

---

## 1. How Improve sits on the stack

| Stage | Layers | Improve feedback |
| --- | --- | --- |
| Ingest / normalize | L1–L2 | — |
| Detect | L3 | Threshold / baseline updates from Track A (after human approve) |
| Recommend | L4 | Preference profile from Track B (after human approve) |
| Assign / act | L5 + L6 | Card delivery; optional Stamped pre-review gate |
| Verify | L5 | Evidence and closure states |
| Propose learning | L5 + L3 | Reads closed cards; writes draft cycles; staff approve |

---

## 2. Two tracks

### Track A — ML calibration + fine-tune loop (L3 + L5)

Threshold tuning from reject/"not real" rates; impact shrinkage from predicted/realised ratios when a ledger exists; plant fine-tune on customer data → shadow → human promote ([ADR-027](ADR-027-plant-calibration-champion-promote.md)). **No continuous online retrain in P0.** Modeled estimates stay labeled modeled.

### Track B — Agent preferences (L4)

Plant preference profile keys: `dept_priority_weights`, `effort_gate`, `evidence_format`, `negotiation_patterns`, `owner_map_corrections`. Built from followed-vs-ignored contrast + negotiation + richer signals. Staff approve in L5 console before L4 apply.

### Plant notes (manual)

Staff jot plant down-points in L5 Internal Console. Not consumed by Improve job. UI/config changes applied manually by engineering.

---

## 3. Non-goals

- Auto-deploy of new recommendation logic or model weights without review
- Cross-plant fleet learning in v1
- Customer-facing "AI is learning about you" UX copy in P0
- Automated developer UI report (former Track C)
- Seventh layer repository
- Silent production rule change without named-owner acceptance

---

## Consequences

- Contracts: `improvement-signal.json` 1.1.0, `improve-cycle.json`, `calibration-patch.json`, `model-run.json`, `plant-admin-settings.json`
- Spec: [stamped-improve-pipeline-spec.md](../../handoff/holistic/improve/stamped-improve-pipeline-spec.md)
- L5 Internal Console for Improve cycles, card gate, ML promote

---

## Alternatives considered

| Option | Rejected because |
| --- | --- |
| New L7 Improve service | Premature; L5 job + console suffices |
| Silent online learning into L4 | Trust / safety risk |
| Track C automated markdown report | Replaced by manual plant notes UI |
| Improve in L6 customer nav | Wrong audience |
