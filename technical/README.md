# Stamped — Technical Context Pack

**Start here:** [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) — overall product + technical architecture (five-domain decision loop; L4 agent / L5 live card).  
**Framing lock:** [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md) · Vision [`../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md`](../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) · Coarse evolution [`../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md`](../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md)

This folder is the portable technical pack (submodule path `external/technical/`).

## Agent reading order

| # | Document | For |
| --- | --- | --- |
| 0 | [`../research/plant-efficiency-exploration-2026-09/AGENT-START.md`](../research/plant-efficiency-exploration-2026-09/AGENT-START.md) → `09` → `10` | Company identity |
| 1 | [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) | **SSOT** — overall product + technical architecture |
| 2 | [`../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md`](../research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md) (+ `15`–`18`) | How L1–L6 evolve (contracts, pilot, exclusions, sequence) |
| 3 | [`layers/`](layers/) | Per-layer deep dives — update later; prefer SSOT + `14` if wording lags |
| 4 | [`cross-cutting/`](cross-cutting/) | Production engineering + evaluation |
| 5 | [research/stamped-research-and-ml-citations.md](research/stamped-research-and-ml-citations.md) | CORE vs FRONTIER bibliography |
| 6 | [research/stamped-context-graphs-and-practical-prescriptions.md](research/stamped-context-graphs-and-practical-prescriptions.md) | Dual graphs / Path D research (ADR-028) |
| — | [`pointers/`](pointers/) | Legacy filenames → redirect to SSOT |

Client positioning and website copy are **archived** under [`../archive/external-marketing-2026-09/`](../archive/external-marketing-2026-09/). Do not treat them as identity.

## Layer specs

| Layer | Path |
| --- | --- |
| L1 · L2 | [layers/l1-l2/](layers/l1-l2/) |
| L3 | [layers/l3/](layers/l3/) |
| L4 · L5 · L6 | [layers/l4-l6/](layers/l4-l6/) |

## Conventions

- Honesty: `[~]` approximate · `[!]` evolving
- Contracts: [`../contracts/`](../contracts/)
- ADRs: [`../decisions/`](../decisions/)
- Handoff: [`../handoff/`](../handoff/)

## Thesis

> Value is engineered as **closed decision cards** with honest evidence tiers — not a single model output and not a fixed savings percentage as company identity.
