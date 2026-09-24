# Product lock — vision doc overhaul (P0)

**Date:** 2026-09-24  
**Audience:** AI agents and engineers updating internal Stamped docs.  
**Authority:** [`research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md`](../../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) (wins on conflict).

## Primary user

An AI coding agent (or engineer) opening stamped-external or any L1–L6 consumer repo to write architecture, ADRs, prompts, or product contracts.

## Job

Make the live documentation tree teach only the current company: **Stamped helps plant teams choose, assign, and verify the next operating action across energy, cost, time / throughput, continuity / flow, and short-horizon exceptions.**

## Done when

- Snapshot tag `v2026.09.24` preserves the prior product.
- Live tree has no prior-framing identity, Energy-suffixed product name, invented savings bands, or energy-only company.
- ADR-030 is the framing lock; ADR-024 and ADR-026 are gone.
- stamped-external PR is green and merged first; every consumer pins that SHA and has a green PR.

## Out of scope (non-goals)

- Contract schema or runtime code changes
- L0–L6 topology redesign
- External marketing rewrite (archived, not rewritten)
- Invented savings, customers, or revenue
- Submodule pin moves before stamped-external merge

## P0 vs later

| P0 this run | Later |
|-------------|-------|
| Tags, doc cut, ADR-030, agent entry rewrite, consumer pins + PRs + CI | Architecture revisit of OT command path; public marketing rewrite |
