# L1 canonical contracts

Shared schemas and MQTT topic conventions for all L1 publishers (edge agent, document ingest) and L2 consumers.

**L1–L2 context records (ADR-031):** closed record catalog, `…/context` wrapper, dedupe material, and L4 tool allowlist — operator narrative in [`../technical/L1-L2-DATA-PLANE.md`](../technical/L1-L2-DATA-PLANE.md); decision in [ADR-031](../decisions/028-032/ADR-031-l1-l2-context-records.md). Packs: `packs/` · tools: `tools/l2-query-tools.json` · topics: [TOPICS.md](TOPICS.md).

**Package name (when published):** `stamped-l1-contracts`  
**Canonical source:** this directory in **[stamped-platform](https://github.com/vinayak-rz/stamped-external)** ([ADR-011](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md))

| Artifact | Status |
| --- | --- |
| JSON Schemas (`schemas/{topic}/*.json`) | **Implemented** — nested by topic (envelope, telemetry, intelligence, closure, plant, config). ADR-033: `decision-case`, `decision-trace`, `card-proposal`, `opportunity-ledger-row`. ADR-029: `action-intent`, `machine-capability`. ADR-028: `plant-knowledge-graph`, `plant-live-index`, `shift-roster`, `l4-compile-trace` (deprecated) |
| Golden fixtures (`fixtures/{topic}/*.json`) | **Implemented** — valid payloads + `fixtures/golden/dedupe_golden.json` |
| [TOPICS.md](TOPICS.md) | Draft topic layout |
| [CHANGELOG.md](CHANGELOG.md) | Current: **0.15.0** unreleased (see changelog) |

**CI:** run [../scripts/contracts/contract-check.sh](../scripts/contracts/contract-check.sh) from consumer repo (path: `external/scripts/contracts/contract-check.sh`).

**Bootstrap:** [../handoff/README.md](../handoff/README.md). See [ADR-001](../decisions/001-005/ADR-001-l1-repo-split-and-boundaries.md).
