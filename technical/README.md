# Stamped Energy — Technical Context Pack

**Start here:** [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) — single latest product + technical architecture (two pillars + shared context).

This folder is the portable technical pack (submodule path `external/technical/`).

## Agent reading order

| # | Document | For |
| --- | --- | --- |
| 1 | [STAMPED_ARCHITECTURE.md](STAMPED_ARCHITECTURE.md) | Product framing, loop, L0–L6, shared context, savings thesis |
| 2 | [ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md) · [ADR-024](../decisions/024-026/ADR-024-holistic-plant-decisions.md) · [ADR-025](../decisions/024-026/ADR-025-improve-loop-step-06.md) | Framing + holistic + Improve |
| 3 | [`layers/`](layers/) | Per-layer deep dives |
| 4 | [`cross-cutting/`](cross-cutting/) | Production engineering + evaluation |
| 5 | [research/stamped-research-and-ml-citations.md](research/stamped-research-and-ml-citations.md) | CORE vs FRONTIER bibliography |
| — | [`pointers/`](pointers/) | Legacy filenames → redirect to SSOT |

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

> 15–20% verified savings is engineered as the **sum of closed prescriptions**, multiplied by **closure rate**, defended by **evidence-backed M&V** — not a single model output.
