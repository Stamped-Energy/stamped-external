# L1 canonical contracts

Shared schemas and MQTT topic conventions for all L1 publishers (edge agent, bill ingest) and L2 consumers.

**Package name (when published):** `stamped-l1-contracts`  
**Canonical source:** this directory in **[stamped-platform](https://github.com/vinayak-rz/stamped-external)** ([ADR-011](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md))

| Artifact | Status |
| --- | --- |
| JSON Schemas (`schemas/{topic}/*.json`) | **Implemented** — nested by topic (envelope, telemetry, intelligence, closure, plant, config) |
| Golden fixtures (`fixtures/{topic}/*.json`) | **Implemented** — valid payloads + `fixtures/golden/dedupe_golden.json` |
| [TOPICS.md](TOPICS.md) | Draft topic layout |
| [CHANGELOG.md](CHANGELOG.md) | Starts at 0.1.0 |

**CI:** run [../scripts/contracts/contract-check.sh](../scripts/contracts/contract-check.sh) from consumer repo (path: `external/scripts/contracts/contract-check.sh`).

**Bootstrap:** [../handoff/README.md](../handoff/README.md). See [ADR-001](../decisions/001-005/ADR-001-l1-repo-split-and-boundaries.md).
