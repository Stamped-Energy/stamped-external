# Handoff — agent navigation

> **Audience:** AI agents and engineers bootstrapping consumer repos (`connectors-*`, `stamped-l2`…`l6`).  
> **Architecture SSOT:** [../technical/STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md)  
> **Framing lock:** [ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md) — two pillars + shared context; not MES.  
> **Path moves:** [PATH_MAP.md](PATH_MAP.md)

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
| [l3/](l3/) | L3 build order |
| [l4/](l4/) | L4 architecture handoff |
| [l5/](l5/) | L5 architecture + build plan |
| [l6/](l6/) | L6 architecture, UX, IA, stubs |
| [connectors/](connectors/) | Bill / cloud / edge playbooks |
| [deployment/](deployment/) | Deployment profiles |

---

## Quick start by repo

| Repo | Start |
| --- | --- |
| Any | [agents/prompts/consumer-platform-prompt.md](agents/prompts/consumer-platform-prompt.md) |
| Holistic / management Rx | [agents/prompts/stamped-holistic-consumer-prompt.md](agents/prompts/stamped-holistic-consumer-prompt.md) → [holistic/](holistic/) |
| stamped-l2 | [l2/core/stamped-l2-spec.md](l2/core/stamped-l2-spec.md) · [agents/onboarding/stamped-l2-agent-onboarding.md](agents/onboarding/stamped-l2-agent-onboarding.md) |
| stamped-l3 | [agents/prompts/stamped-l3-dual-lane-consumer-prompt.md](agents/prompts/stamped-l3-dual-lane-consumer-prompt.md) · [l3/](l3/) |
| stamped-l4 | [l4/stamped-l4-architecture-handoff.md](l4/stamped-l4-architecture-handoff.md) |
| stamped-l5 | [l5/stamped-l5-architecture-handoff.md](l5/stamped-l5-architecture-handoff.md) |
| stamped-l6 | [l6/stamped-l6-architecture-handoff.md](l6/stamped-l6-architecture-handoff.md) · [agents/onboarding/stamped-l6-agent-onboarding.md](agents/onboarding/stamped-l6-agent-onboarding.md) |
| connectors-bill | [connectors/bill/connectors-bill-spec.md](connectors/bill/connectors-bill-spec.md) |
| connectors-cloud | [connectors/cloud/connectors-cloud-downstream-context.md](connectors/cloud/connectors-cloud-downstream-context.md) |
| connectors-edge | [connectors/edge/connectors-edge-portability-playbook.md](connectors/edge/connectors-edge-portability-playbook.md) |

### Setup (submodule)

```bash
git submodule add https://github.com/vinayak-rz/stamped-external.git external
cd external && git checkout v2026.07.30 && cd ..
```

Run contracts: `external/scripts/contracts/contract-check.sh`

### stamped-l2 one-line mission

**stamped-l2** is the Universal Repository — six stores in one Postgres+TimescaleDB DB, consuming `StampedRecordEnvelope` from connectors-cloud, serving L3–L6.

Also read: [ADR-008](../decisions/006-010/ADR-008-layer-repo-topology-and-interfaces.md), [ADR-009](../decisions/006-010/ADR-009-stamped-l2-repo-charter.md), [ADR-010](../decisions/006-010/ADR-010-deployment-profiles-and-portability.md), [ADR-011](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md).
