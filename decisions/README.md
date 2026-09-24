# Architecture decisions (cross-repo)

Decision records for the Stamped platform. Distributed via submodule at `external/` ([ADR-011](011-015/ADR-011-stamped-platform-submodule-distribution.md)).

**Product framing lock:** [ADR-030](028-032/ADR-030-five-domain-decision-loop.md) — five-domain choose / assign / verify.

ADRs live in number buckets. Start with the index below.

| ADR | Title | Status | Path |
| --- | --- | --- | --- |
| [ADR-001](001-005/ADR-001-l1-repo-split-and-boundaries.md) | L1 repo split, edge packaging, schemas, transport, tag mapping | Accepted | `001-005/` |
| [ADR-002](001-005/ADR-002-build-all-aws-networking.md) | Build-all software, plant networking, AWS cost-first | Accepted | `001-005/` |
| [ADR-003](001-005/ADR-003-connectors-edge-monorepo.md) | connectors-edge monorepo | Accepted | `001-005/` |
| [ADR-005](001-005/ADR-005-edge-agent-go-architecture.md) | Go edge-agent architecture | Accepted | `001-005/` |
| [ADR-007](006-010/ADR-007-connectors-cloud-repo-charter.md) | connectors-cloud repo charter | Accepted | `006-010/` |
| [ADR-008](006-010/ADR-008-layer-repo-topology-and-interfaces.md) | Layer-per-repo topology; L1→L6 interfaces | Accepted | `006-010/` |
| [ADR-009](006-010/ADR-009-stamped-l2-repo-charter.md) | stamped-l2 repo charter | Accepted | `006-010/` |
| [ADR-010](006-010/ADR-010-deployment-profiles-and-portability.md) | Three deployment modes | Accepted | `006-010/` |
| [ADR-011](011-015/ADR-011-stamped-platform-submodule-distribution.md) | stamped-platform submodule SSOT | Accepted | `011-015/` |
| [ADR-012](011-015/ADR-012-l3-artifact-repo-topology.md) | L3 artifact repos | Accepted | `011-015/` |
| [ADR-014](011-015/ADR-014-promotion-record.md) | Promotion record (lab never promotes without record) | Accepted | `011-015/` |
| [ADR-015](016-020/ADR-015-l3-dual-lane-lab-detections.md) | L3 dual-lane lab detections | Accepted | `016-020/` |
| [ADR-019](016-020/ADR-019-l5-runtime-and-consistency.md) | L5 runtime charter | Accepted | `016-020/` |
| [ADR-020](020-023/ADR-020-l5-mv-claim-governance.md) | L5 claim governance | Accepted | `020-023/` |
| [ADR-021](020-023/ADR-021-l5-notification-and-evidence.md) | L5 notification + evidence | Accepted | `020-023/` |
| [ADR-022](020-023/ADR-022-l6-bff-runtime-boundary.md) | L6 BFF runtime boundary | Accepted | `020-023/` |
| [ADR-025](024-026/ADR-025-improve-loop-step-06.md) | Learning from closed cards | Accepted | `024-026/` |
| [ADR-030](028-032/ADR-030-five-domain-decision-loop.md) | Five-domain decision loop (product framing) | Accepted | `028-032/` |
| [ADR-031](028-032/ADR-031-l1-l2-context-records.md) | L1–L2 context records data plane | Accepted | `028-032/` |
| [ADR-033](033-039/ADR-033-l4-decision-runtime.md) | L4 decision runtime (Finding → card proposal) | Accepted | `033-039/` |
| [ADR-034](033-039/ADR-034-plant-situation-model-and-memory.md) | Plant Situation Model and memory | Accepted | `033-039/` |
| [ADR-035](033-039/ADR-035-l4-discovery.md) | L4 discovery (beyond Finding intake) | Accepted | `033-039/` |
| [ADR-036](033-039/ADR-036-dual-family-models.md) | Dual-family plant models and offline council | Accepted | `033-039/` |
| [ADR-037](033-039/ADR-037-site-pack-topology.md) | Site-pack topology as plant structure SSOT | Accepted | `033-039/` |
| [ADR-038](033-039/ADR-038-soft-gates-opportunity-ledger.md) | Soft gates, opportunity ledger, and exploration | Accepted | `033-039/` |
| [ADR-039](033-039/ADR-039-registries-and-stage-graph.md) | Registries and expandable stage graph | Accepted | `033-039/` |
| [ADR-040](040-044/ADR-040-l4-production-hardness.md) | L4 production hardness (queue, lifecycle, ports, controls) | Accepted | `040-044/` |

**Archived / superseded (2026-09 cleanup):** ADR-004, ADR-006, ADR-014 (TS FM), ADR-016, ADR-017, ADR-018, ADR-023, ADR-027, ADR-028, and `asset-id-migration.md` → [`../archive/cleanup-2026-09/adrs/`](../archive/cleanup-2026-09/adrs/). Also recoverable on tag `v2026.09.24`. Withdrawn earlier: ADR-013, ADR-024, ADR-026. ADR-029 under marketing archive.

Architecture SSOT: [`../technical/STAMPED_ARCHITECTURE.md`](../technical/STAMPED_ARCHITECTURE.md)  
Handoff: [`../handoff/README.md`](../handoff/README.md)  
Design / brand: [`../design/`](../design/)
