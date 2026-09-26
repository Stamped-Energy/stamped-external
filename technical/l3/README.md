# L3 — Intelligence core (detection)

*Status: as-built · 2026-09-26*  
*Authority:* [STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md) §4 · §6a · [ADR-012](../../decisions/011-015/ADR-012-l3-artifact-repo-topology.md) · [ADR-015](../../decisions/011-015/ADR-015-l3-dual-lane-lab-detections.md)

L3 turns L2 telemetry into contract **Finding** objects. Only dual-lane **`status=emitted` ∧ `delivery=l4`** leave for L4. Lab never promotes. Money cites tariff or tagged fallback. No `L2_DATABASE_URL`.

| Label | Meaning |
| --- | --- |
| **as-built** | `intelligence-core` · `intelligence-rulepacks` · `intelligence-evals` |
| **contract** | Finding **1.2.0** · RunArtifact **1.1.0** |
| **direction** | Broader detection science beyond the current engine list (SSOT §6a) |

## Repos

| Repo | Job |
| --- | --- |
| `intelligence-core` | Runtime: scheduler, engines, outbox, Lab HTTP |
| `intelligence-rulepacks` | YAML thresholds, tariffs, vertical priors (`RULEPACK_PATH`) |
| `intelligence-evals` | Offline eval CLI + Lab UI |

## Reading order

| Order | Doc | Role |
| --- | --- | --- |
| 1 | [`01-runtime.md`](01-runtime.md) | Pipeline, dual-lane, schedules, money |
| 2 | [`02-engines.md`](02-engines.md) | Engine catalog and enable flags |
| 3 | [`03-rulepacks-and-evals.md`](03-rulepacks-and-evals.md) | Rulepacks vs math; offline evals |
| 4 | [`04-finding-contract.md`](04-finding-contract.md) | Finding 1.2.0 → L4 intake |

## Hard rules

| Rule | Owner |
| --- | --- |
| No L2 SQL | Core clients are HTTP / fixtures only |
| Lab never promotes | Dual-lane invariant |
| Never invent ₹ | Tariff resolve + outbox forged-INR guard |
| Shipping a module ≠ shipping a Finding | Many engines need `ENABLE_*` or `PROOF_RUN=1` |

L4 intake contract detail: [`../l4/15-l3-l4-interface.md`](../l4/15-l3-l4-interface.md).
