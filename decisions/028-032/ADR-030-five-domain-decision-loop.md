# ADR-030: Five-domain decision loop (product framing)

> **Amended 2026-09-26.** Company policy is now [`Stamped_Master_Document.md`](../../Stamped_Master_Document.md): **four outcomes** (quality and yield, energy and waste, uptime, dynamic scheduling) on one card. Cost, continuity/flow, and time are **effects**, not outcomes. Prefer the master document and [`technical/STAMPED_ARCHITECTURE.md`](../../technical/STAMPED_ARCHITECTURE.md) for live identity. Keep this ADR for topology, hard-stop spine, and historical five-domain wording — do not teach the five-domain list as current product identity.

| Field | Value |
| --- | --- |
| **Status** | **Amended** (by master document four-outcome framing) |
| **Date** | 2026-09-24 |
| **Deciders** | Product + Engineering |
| **Supersedes** | ADR-024 (holistic plant / energy-hero framing), ADR-026 (prior framing; tag v2026.09.24) |
| **Amended by** | [`Stamped_Master_Document.md`](../../Stamped_Master_Document.md) (2026-09-26) |
| **Authority narrative** | Master document wins · historical: [`09-stamped-founder-vision.md`](../../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) |
| **Agent contract** | [`10-stamped-vision-agent-alignment.md`](../../research/plant-efficiency-exploration-2026-09/10-stamped-vision-agent-alignment.md) |
| **Related** | [ADR-008](../006-010/ADR-008-layer-repo-topology-and-interfaces.md) · [ADR-025](../024-026/ADR-025-improve-loop-step-06.md) · [STAMPED_ARCHITECTURE.md](../../technical/STAMPED_ARCHITECTURE.md) |

---

## Context

Prior framing (tag `v2026.09.24`) locked Stamped as an energy-first product (ADR-026) with energy-hero holistic co-benefits (ADR-024). Founder vision 2026-09-24 defines a different company: one decision card across five domains, recommend and assign by default, energy as entry wedge only. L0–L6 topology and contracts stay; identity and agent reading orders must change.

Snapshot of the prior product: git tag `v2026.09.24` on stamped-external and consumer repos.

---

## Decision summary

| # | Topic | Decision |
| --- | --- | --- |
| 1 | Product name | **Stamped** only — do not append Energy to the product name |
| 2 | One sentence | Stamped helps plant teams **choose, assign, and verify** the next operating action across energy, cost, time / throughput, continuity / flow, and short-horizon exceptions |
| 3 | Shape | **One** product; **five** decision domains on **one** card with **one** owner |
| 4 | Entry wedge | Energy opens the first conversation; it is not the category |
| 5 | Default autonomy | Recommend and assign; humans decide and execute |
| 6 | Hard stops | No automatic safety / critical remote command; no quality hold release; no maintenance authorization; no silent master-data or full dispatch change; no constraint override for a model benefit alone |
| 7 | Stack | L0–L6 layer-per-repo topology **unchanged** (ADR-008); product claim is the closed action, not the layer diagram |
| 8 | Process pillar | Deferred — not a current product pillar |
| 9 | Integration | Read / ingest default; may notify or create a task; write-back human-confirmed, narrow, allow-listed, auditable |
| 10 | MES / ERP / APS | Read context; never replace systems of record; never own dispatch or promise dates |
| 11 | Evidence | Measured / Confirmed / Modeled / Unknown; wallets separate; calculator owns money |
| 12 | Supersession | ADR-024 and ADR-026 are **withdrawn**; do not cite them for product identity |

---

## Mandatory thinking model

```text
One product — Stamped
 â”œâ”€â”€ Five domains (one primary tag per card): Energy · Cost · Time/throughput · Continuity/flow · Exception response
 â”œâ”€â”€ Loop: detect â†’ recommend â†’ assign â†’ act â†’ verify (optional propose learning)
 â””â”€â”€ Stack: L1 â†’ L2 â†’ L3 â†’ L4 â†’ L5 â†’ L6 (unchanged topology)
```

---

## Language lock

| Say | Do not say |
| --- | --- |
| Stamped | Product name with Energy appended |
| Five-domain decision loop | Withdrawn dual-pillar + shared-context framing |
| Choose / assign / verify | Dashboard-only / insight-only |
| Energy as entry wedge | Energy-only company |
| Recommend and assign by default | Autonomous plant / runs the plant |
| Closed action | 15–20% verified savings as identity |
| OpEx is the plant’s program | Operational-excellence suite |

---

## Enforcement

- Agent entry: `AGENT-START.md` â†’ `09` â†’ `10` â†’ this ADR â†’ layer specs.
- Consumer repos pin stamped-external after this ADR lands on default branch.
- Identity lint forbids live docs (outside `archive/` and historical `CHANGELOG.md` sections) from teaching the withdrawn framing.
