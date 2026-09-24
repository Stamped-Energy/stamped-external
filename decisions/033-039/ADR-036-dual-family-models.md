# ADR-036: Dual-family plant models and offline council

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-033](ADR-033-l4-decision-runtime.md) · [`technical/l4/11-models-and-seams.md`](../../technical/l4/11-models-and-seams.md) · [`technical/l4/13-improvement.md`](../../technical/l4/13-improvement.md) |

---

## Context

Single-model drafting correlates errors. Same-family judges prefer their own outputs. Plant runtime needs low latency and cost control; improvement work needs stronger critique without blocking the floor.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Plant runtime pair | Provider-agnostic dual-family slot; default DeepSeek V4.1 Flash (`deepseek-flash`) + GPT-5.6 Luna |
| 2 | Hosting | Hosted API or self-hosted open weights per deployment |
| 3 | Pro upgrade | DeepSeek V4.1 Pro replaces Flash in its slot when released, via replay — each plant owner accepts (or opts in to auto-accept global model pins) |
| 4 | One-family mode | Two correlated samples, stricter numeric thresholds, grounded-hypothesis lane off; sample disagreement on action seams → withhold |
| 5 | Offline council | Opus 5.5 + GPT-5.6 Sol — never on the plant request path |
| 6 | Confidence | Cross-family agreement is the confidence signal on seams; calibrated against outcomes; not a model self-score |
| 7 | Disagreement | Action / owner / constraint-affecting / verification / terminal → **withhold** (hard gate `action_seam_disagreement`); routing seams → registry default |
| 8 | Seam records | Every seam decision is logged for Jev / classifier replacement |

---

## Consequences

- Model pins live in the release lockfile; nothing promotes itself.
- Offline council proposes playbook/prompt deltas; named owner accepts after replay and shadow.
- Amends research `14`/`15` soft fallback to generative agent on low confidence.

---

## Rejected alternatives

- Single plant model with self-critique only.
- Averaging model scores into a gate.
- Strong council models on the live plant path.
- Silent weight post-training on raw closures.
- Soft fallback to generative agent on low confidence.

---

## What would change this

- Dual-family agreement anti-correlates with verified closures → revisit agreement as confidence for that seam (ADR).
- Flash→Pro replay fails plant accept rate → keep Flash.
- One-family miss rates match dual-family at stricter thresholds → optional hypothesis under extra hard gates (ADR).

---

## v1 slice

Dual-family default; one-family mode available; Opus/Sol offline only; all catalog seams LLM-only until Jev beats logged records.
