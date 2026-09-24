# Stamped — Technical Context Pack

**Start here:** [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) — overall product + technical architecture (five-domain decision loop; L4 agentic system / L5 live card).  
**L4 architecture (normative detail):** [`l4/`](l4/) — kernel, runtime, PSM, discovery, seams, opportunity ledger.  
**Framing lock:** [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md) · Vision [`../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md`](../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) · Coarse evolution [`../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md`](../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md)

This folder is the portable technical pack (submodule path `external/technical/`).

## Agent reading order

| # | Document | For |
| --- | --- | --- |
| 0 | [`../research/plant-efficiency-exploration-2026-09/AGENT-START.md`](../research/plant-efficiency-exploration-2026-09/AGENT-START.md) → `09` → `10` | Company identity |
| 1 | [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) | **SSOT** — overall product + technical architecture |
| 1b | [`l4/`](l4/) · ADRs [033](../decisions/033-039/ADR-033-l4-decision-runtime.md)–[039](../decisions/033-039/ADR-039-registries-and-stage-graph.md) | **L4 contract** — implement from here |
| 2 | [`../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md`](../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md) (+ `15`–`18`, `19`) | How L1–L6 evolve; L4 peer research |
| 2b | [L1-L2-DATA-PLANE.md](L1-L2-DATA-PLANE.md) | Configure meters, ERP exports, and context into L2; boot/trial proof |
| — | [`pointers/`](pointers/) | Legacy filenames → redirect to SSOT |

Pre-overhaul layer specs, cross-cutting notes, and citation packs were moved to [`../archive/cleanup-2026-09/technical/`](../archive/cleanup-2026-09/technical/). Prefer SSOT + `14` over archived layer markdown.

## Conventions

- Honesty: `[~]` approximate · `[!]` evolving
- Contracts: [`../contracts/`](../contracts/)
- ADRs: [`../decisions/`](../decisions/)
- Handoff: [`../handoff/`](../handoff/)
- Design / brand: [`../design/`](../design/)

## Thesis

> Value is engineered as **closed decision cards** with honest evidence tiers — not a single model output and not a fixed savings percentage as company identity.
