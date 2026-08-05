# ADR-027: Plant calibration patch and champion alias promotion

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-08-01 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-025](ADR-025-improve-loop-step-06.md) · [ADR-014](../011-015/ADR-014-ts-foundation-model-role.md) · [ADR-012](../011-015/ADR-012-l3-artifact-repo-topology.md) · [`calibration-patch.json`](../../contracts/schemas/closure/calibration-patch.json) · [`model-run.json`](../../contracts/schemas/closure/model-run.json) |

---

## Context

Improve Track A produces ML calibration drafts and plant fine-tune runs. Pretrained base models are adapted on customer plant data, evaluated in shadow, and must not flip to champion without human action.

---

## Decision

1. **Fine-tune/refit jobs** register artifacts as `@challenger` / `lane=shadow` only.
2. **Shadow predictions** never write L4 outbox or customer-facing findings.
3. **Human promote** in L5 Internal Console is the only path to `@champion` alias flip or approved `calibration_patch` apply.
4. **Rollback** retains prior champion; one-click revert in console.
5. **Evals** emit promotion **recommendation** only; no auto-promote.

---

## Consequences

- Contracts: `calibration-patch.json`, `model-run.json`
- L3 core: registry `promote` / `rollback` hooks
- L3 evals: shadow gates + recommendation artifact
- L5: ML promote APIs + console screens

---

## Non-goals

- Auto-promote on gate pass
- Fleet-wide model sharing without consent
- MLflow hosting (adapter interface only in P0)
