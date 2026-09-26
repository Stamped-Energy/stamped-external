# Handoff — agent navigation

> **Audience:** AI agents and engineers bootstrapping consumer repos (`connectors-*`, L2…L6).  
> **Architecture first:** [../technical/STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md) → [../technical/layers/](../technical/layers/) → [../technical/l3/](../technical/l3/) or [../technical/l4/](../technical/l4/) for depth.  
> **Framing lock:** [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md) — five-domain decision loop. Prior framing: tag `v2026.09.24` only.  
> **Path moves:** [PATH_MAP.md](PATH_MAP.md)

This folder is **integration playbooks** (bootstrap, deploy, prompts). Prefer `technical/layers/`, `technical/l3/`, and `technical/l4/` for architecture. Handoffs may retain historical build detail behind authority banners.

**Paste into any consumer `AGENTS.md`:** [agents/prompts/consumer-platform-prompt.md](agents/prompts/consumer-platform-prompt.md)  
**Holistic / plant context (mandatory with platform prompt):** [agents/prompts/stamped-holistic-consumer-prompt.md](agents/prompts/stamped-holistic-consumer-prompt.md)

---

## Folder map

| Folder | Contents |
| --- | --- |
| [agents/prompts/](agents/prompts/) | Consumer agent prompts (platform, holistic, L3 dual-lane, L3 ops-clearance) |
| [agents/onboarding/](agents/onboarding/) | Repo onboarding paste-ins (L2, L6, bill) |
| [holistic/](holistic/) | Shared context: MES/ERP, tradeoff, negotiation, improve, audit, pilot |
| [l2/](l2/) | Universal repository handoffs (`core/` + `ops/`) |
| [l3/](l3/) | L3 build order (historical; prefer `technical/l3/`) |
| [l4/](l4/) | L4 architecture handoff → decision runtime |
| [l5/](l5/) | L5 architecture + build plan |
| [l6/](l6/) | L6 architecture, UX, IA, stubs |
| [connectors/](connectors/) | Bill / cloud / edge playbooks |
| [deployment/](deployment/) | Deployment profiles |

---

## Quick start by repo

| Repo | Architecture | Handoff start |
| --- | --- | --- |
| Any | [../technical/STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md) | [agents/prompts/consumer-platform-prompt.md](agents/prompts/consumer-platform-prompt.md) |
| L1 connectors | [../technical/layers/L1-connect.md](../technical/layers/L1-connect.md) | [connectors/](connectors/) |
| `universal-repositary` (L2) | [../technical/layers/L2-universal-repository.md](../technical/layers/L2-universal-repository.md) | [l2/core/stamped-l2-spec.md](l2/core/stamped-l2-spec.md) |
| L3 core / rulepacks / evals | [../technical/l3/](../technical/l3/) | [agents/prompts/stamped-l3-dual-lane-consumer-prompt.md](agents/prompts/stamped-l3-dual-lane-consumer-prompt.md) |
| `knowledge-reasoning` (L4) | [../technical/l4/](../technical/l4/) · [../technical/l4/30-as-built.md](../technical/l4/30-as-built.md) | [l4/stamped-l4-architecture-handoff.md](l4/stamped-l4-architecture-handoff.md) |
| `closure-verification` (L5) | [../technical/layers/L5-closure.md](../technical/layers/L5-closure.md) | [l5/stamped-l5-architecture-handoff.md](l5/stamped-l5-architecture-handoff.md) |
| `experience-integration` (L6) | [../technical/layers/L6-experience.md](../technical/layers/L6-experience.md) | [l6/stamped-l6-architecture-handoff.md](l6/stamped-l6-architecture-handoff.md) |

### Setup (submodule)

```bash
git submodule add https://github.com/vinayak-rz/stamped-external.git external
cd external && git checkout v2026.07.30 && cd ..
```

Run contracts: `external/scripts/contracts/contract-check.sh`

### stamped-l2 one-line mission

**stamped-l2** is the Universal Repository — six stores in one Postgres+TimescaleDB DB, consuming `StampedRecordEnvelope` from connectors-cloud, serving L3–L6.

Also read: [ADR-008](../decisions/006-010/ADR-008-layer-repo-topology-and-interfaces.md), [ADR-009](../decisions/006-010/ADR-009-stamped-l2-repo-charter.md), [ADR-010](../decisions/006-010/ADR-010-deployment-profiles-and-portability.md), [ADR-011](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md).
