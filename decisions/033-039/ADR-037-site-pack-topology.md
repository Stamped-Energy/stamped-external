# ADR-037: Site-pack topology as plant structure SSOT

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-031](../028-032/ADR-031-l1-l2-context-records.md) · [ADR-034](ADR-034-plant-situation-model-and-memory.md) · [`technical/l4/02-plant-structure.md`](../../technical/l4/02-plant-structure.md) · [`technical/l4/18-contract-deltas.md`](../../technical/l4/18-contract-deltas.md) |

---

## Context

Cross-asset checks need flow, buffers, lag, and shared resources. If L4 alone owns topology, L3 detectors and L5 verification cannot use it. If every suggestion becomes structure without an owner, the graph drifts from plant truth.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Ownership | Plant structure lives in the **site pack** (versioned, owner-reviewed) |
| 2 | Publication | L1 publishes typed topology records → L2 (contract delta in `18-contract-deltas.md`) |
| 3 | Content | Areas/lines; flow edges (direction, buffer, lag); shared resources with capacity; meter hierarchy; asset→resource draws |
| 4 | L4 use | PSM builder reads topology via **builder reads** (bulk/list), separate from the agent tool catalog |
| 5 | Suggestions | Models may propose missing links as suggestions with evidence and expiry; enter the site pack only on named owner confirmation |
| 6 | Rejection memory | Rejected suggestions are remembered; not re-proposed without new evidence |
| 7 | Missing structure | Cross-asset check without required structure returns `unknown`; unknown in a constraint neighbourhood → withhold |
| 8 | Commissioning | Per family/pattern: minimum topology, shared-resource, constraint, and verification-signal evidence before activation |

---

## Consequences

- Topology is plant truth shared across layers, not an L4 private cache of inventable edges.
- Builder reads are not agent tools and cannot write.

---

## Rejected alternatives

- L4-only topology config.
- Auto-accepting model-proposed edges into live structure.
- Requiring a full plant ontology before the first card.
