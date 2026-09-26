# Stamped — Technical Context Pack

**Start here:** [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) — overall product + technical architecture (four outcomes; L3 signal / L4 brain; L5 live card).  
**Company policy:** [`../Stamped_Master_Document.md`](../Stamped_Master_Document.md) (wins on identity).  
**Layer pages:** [`layers/`](layers/) — L1 connect, L2 store, L5 closure, L6 experience.  
**L3 architecture (deep):** [`l3/`](l3/) — detection runtime, engines, rulepacks, Finding contract.  
**L4 architecture (normative + as-built):** [`l4/`](l4/) — kernel, runtime, PSM, discovery, seams, opportunity ledger · [`l4/30-as-built.md`](l4/30-as-built.md).  
**Supporting history:** [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md) (amended) · Vision [`../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md`](../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) · Coarse evolution [`../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md`](../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md)

This folder is the portable technical pack (submodule path `external/technical/`).

## Agent reading order

| # | Document | For |
| --- | --- | --- |
| 0 | [`../Stamped_Master_Document.md`](../Stamped_Master_Document.md) | Company identity |
| 1 | [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) | **SSOT** — overall product + technical architecture |
| 2 | [`layers/`](layers/) | Per-layer map (repos, contracts, must-nots) |
| 3a | [`l3/`](l3/) | **L3 deep** — Findings, dual-lane, engines |
| 3b | [`l4/`](l4/) · ADRs [033](../decisions/033-039/ADR-033-l4-decision-runtime.md)–[040](../decisions/040-044/ADR-040-l4-production-hardness.md) | **L4 contract + as-built** |
| 4 | [`../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md`](../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md) (+ `15`–`18`, `19`) | How L1–L6 evolve; L4 peer research |
| 5 | [L1-L2-DATA-PLANE.md](L1-L2-DATA-PLANE.md) | Configure meters, ERP exports, and context into L2; boot/trial proof |
| — | [`pointers/`](pointers/) | Legacy filenames → redirect to SSOT |

Pre-overhaul layer specs, cross-cutting notes, and citation packs were moved to [`../archive/cleanup-2026-09/technical/`](../archive/cleanup-2026-09/technical/). Prefer SSOT + `layers/` + `l3/` + `l4/` over archived layer markdown.

## Conventions

- Honesty: `[~]` approximate · `[!]` evolving
- Status labels: **as-built** · **contract** · **direction**
- Contracts: [`../contracts/`](../contracts/)
- ADRs: [`../decisions/`](../decisions/)
- Handoff: [`../handoff/`](../handoff/)
- Design / brand: [`../design/`](../design/)

## Thesis

> Value is engineered as **closed decision cards** with honest evidence tiers — not a single model output and not a fixed savings percentage as company identity.
