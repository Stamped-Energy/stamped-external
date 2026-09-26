# stamped-external (platform SSOT) — architecture diagrams (Archify)

Layer **Contracts (SSOT)** · `Stamped-Energy/stamped-external` @ `a4c91bc` · generated 2026-09-25 with Archify (pinned `9e35d2b`) · [Master index](https://github.com/Stamped-Energy/stamped-external/blob/main/technical/archify/index.html)

> **Honesty:** No integration is live at any customer plant. Verified savings to date: ₹0. "BUILT" means code on `main` with tests, not production.

## How to view
Clone or download this folder and open `index.html` in a browser; offline OK. Zoom: **MAP** / **READ** / **FULL**. Use guided views, Route Probe, Node Finder.

Status tags: **BUILT** · **PARTIAL** · **DESIGNED** (dashed) · **DEFERRED** (dashed).

## What this repo does at runtime
No server runs in this repo: layer repos mount `external/` and run `contract-check.sh` on PRs. Platform merges update schemas, ADRs, and handoffs; tags drive submodule bumps (ADR-011). Vision/ADR markdown sets product law; `contracts/` sets wire bytes.

## Reading order
| # | Diagram | Type | Question | B/P/D/X |
|---|---|---|---|---|
| 1 | [EXT-01 — SSOT pack](EXT-01-stamped-external-ssot.html) | architecture | Where is authority for vision, ADRs, contracts, handoffs? | 8/0/0/0 |
| 2 | [EXT-04 — Authority order](EXT-04-authority-order-workflow.html) | workflow | Which doc wins on conflict? | 9/0/0/0 |
| 3 | [EXT-02 — Contract change](EXT-02-contract-change-workflow.html) | workflow | How does a schema change roll out? | 8/0/0/0 |
| 4 | [EXT-03 — Catalog dataflow](EXT-03-contract-catalog-dataflow.html) | dataflow | Who produces/consumes each family? | 6/0/0/0 |
| 5 | [EXT-05 — Version lifecycle](EXT-05-contract-version-lifecycle.html) | lifecycle | What states can a version be in? | 4/0/0/0 |

## Doc ↔ code gaps
| ID | Docs say | Main does | Evidence | Diagram |
|---|---|---|---|---|
| G9 | L4 compiler-only in archived layer notes | Agentic L4 in `technical/l4/` | `technical/STAMPED_ARCHITECTURE.md:9` | EXT-04 |
| new | “Removed” as CI enum | CHANGELOG policy only | `contracts/CHANGELOG.md:14` | EXT-05 |

## Files
`src/*.json` specs · `*.html` diagrams · `receipts/` · `TRACE_NOTES.md` · `manifest.json`

See `index.html` for full narratives and glossary.
