# ADR-034: Plant Situation Model and memory

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-25 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-031](../028-032/ADR-031-l1-l2-context-records.md) · [ADR-033](ADR-033-l4-decision-runtime.md) · [ADR-037](ADR-037-site-pack-topology.md) · [`technical/l4/03-plant-situation-model.md`](../../technical/l4/03-plant-situation-model.md) · [`technical/l4/06-memory.md`](../../technical/l4/06-memory.md) |

---

## Context

Per-Finding context packs cannot see portfolio conflicts, recurring patterns, or shifting bottlenecks. An L2-owned plant graph would turn every topology change into a store migration and reopen the “graph becomes the product” failure (`17`). Memory must improve recommendations without poisoning thresholds or inventing outcomes.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | PSM | Derived, versioned, per-plant model in the **L4 operational store** — a cache with provenance, not a system of record |
| 2 | Structure source | Site-pack topology published L1→L2 (ADR-037); PSM builder reads via builder reads |
| 3 | Temporal views | State episodes, conditioned baselines, bottleneck residence, shared-resource envelopes, constraint intervals, change points, pre/post-action windows |
| 4 | Bitemporal | Each element carries effective time and recorded time; run snapshots are **as-known-at** |
| 5 | Graph walk | PSM builder and propagation code walk structure; models request typed zoom reads only |
| 6 | Admission | An element exists only if a family, pattern, or constraint kind reads it |
| 7 | Memory tiers | Working ledger (per run); Hindsight plant bank; Hindsight dialogue banks (Ask); case library (authority for outcomes); negative memory; procedural memory under release lockfile |
| 8 | Outcome authority | When Hindsight disagrees with the case library, the case library wins and the disagreement is traced |
| 9 | Cross-plant | Not in v1; designed as a future seam (anonymised, owner-approved) |

---

## Consequences

- Late L2 corrections do not rewrite what replay says L4 knew.
- Models never traverse the plant graph or assign evidence tiers.
- Ineligible closes set outcome to null; proof counts require independent eligible closures across shifts and dates.

---

## Rejected alternatives

- L2 owns the plant graph as product.
- Single shared memory for Ask and decision runtime.
- Cross-plant priors in v1.
