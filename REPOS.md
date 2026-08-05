# Stamped product repositories

Consumer repos mount this platform pack as a git submodule at `external/`.

| Repo | GitHub | Layer | Submodule | Platform pin (target) | README snapshot |
|------|--------|-------|-----------|----------------------|-----------------|
| connectors-edge | `Vinayak-RZ/connectors-edge` | L1 plant | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/connectors-edge.md](consumers/readmes/connectors-edge.md) |
| connectors-cloud | `Vinayak-RZ/connectors-cloud` | L1 cloud | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/connectors-cloud.md](consumers/readmes/connectors-cloud.md) |
| connectors-bill | `Vinayak-RZ/connectors-bill` | L1 bill | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/connectors-bill.md](consumers/readmes/connectors-bill.md) |
| universal-repositary | `Vinayak-RZ/universal-repositary` | L2 (stamped-l2) | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/universal-repositary.md](consumers/readmes/universal-repositary.md) |
| intelligence-core | `Vinayak-RZ/intelligence-core` | L3 engine (stamped-l3-core) | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/intelligence-core.md](consumers/readmes/intelligence-core.md) |
| intelligence-rulepacks | `Vinayak-RZ/intelligence-rulepacks` | L3 artifacts (stamped-l3-rulepacks) | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/intelligence-rulepacks.md](consumers/readmes/intelligence-rulepacks.md) |
| intelligence-evals | `Vinayak-RZ/intelligence-evals` | L3 eval (stamped-l3-eval) | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/intelligence-evals.md](consumers/readmes/intelligence-evals.md) |
| knowledge-reasoning | `Vinayak-RZ/knowledge-reasoning` | L4 (stamped-l4) | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/knowledge-reasoning.md](consumers/readmes/knowledge-reasoning.md) |
| closure-verification | `Vinayak-RZ/closure-verification` | L5 (stamped-l5) | `external/` | `v2026.08.05` (`5900531`) | [consumers/readmes/closure-verification.md](consumers/readmes/closure-verification.md) |
| stamped-l6 / experience-integration | `Vinayak-RZ/stamped-l6` (seed) / live `experience-integration` | L6 | `external/` | `v2026.08.05` (`5900531`) | Seed: [consumers/stamped-l6/](consumers/stamped-l6/) |

**README snapshots index:** [consumers/readmes/README.md](consumers/readmes/README.md)

**Current platform:** tag [`v2026.08.05`](https://github.com/Stamped-Energy/stamped-external/releases/tag/v2026.08.05) · contracts **0.11.2** · Wave A = generic-energy (`idle_load` + `compressor_sp_drift` + practicality gates) · Wave B = order-aware tradeoff/negotiation

**L4 handoff:** [handoff/l4/stamped-l4-architecture-handoff.md](handoff/l4/stamped-l4-architecture-handoff.md) · [ADR-017](decisions/016-020/ADR-017-l4-adaptive-retrieval-and-web-trust.md)

**L5 handoff:** [handoff/l5/stamped-l5-architecture-handoff.md](handoff/l5/stamped-l5-architecture-handoff.md) · [build plan](handoff/l5/stamped-l5-build-plan.md) · [ADR-019](decisions/016-020/ADR-019-l5-runtime-and-consistency.md) · [ADR-020](decisions/020-023/ADR-020-l5-mv-claim-governance.md) · [ADR-021](decisions/020-023/ADR-021-l5-notification-and-evidence.md) · [internal console](handoff/holistic/improve/stamped-l5-internal-console-handoff.md)

**L6 handoff:** [handoff/l6/stamped-l6-architecture-handoff.md](handoff/l6/stamped-l6-architecture-handoff.md) · [UI charter](handoff/l6/stamped-l6-ui-ux-charter.md) · [build plan](handoff/l6/stamped-l6-build-plan.md) · [ADR-022](decisions/020-023/ADR-022-l6-bff-runtime-boundary.md) · [ADR-023](decisions/020-023/ADR-023-l6-ems-and-analyst-context.md)

**Platform repo:** `Stamped-Energy/stamped-external` — see [SUBMODULE.md](SUBMODULE.md)

Update this table when a consumer bumps its pin or a README snapshot is re-synced.
