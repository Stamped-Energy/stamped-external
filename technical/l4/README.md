# L4 — Decision runtime architecture

**Status:** Architecture contract (docs). Implementation lives in `stamped-l4`.  
**Date:** 2026-09-25  
**Product framing:** [ADR-030](../../decisions/028-032/ADR-030-five-domain-decision-loop.md)  
**Normative kernel:** [`00-kernel.md`](00-kernel.md) — other docs link here; they do not restate it.

L4 turns plant conditions into **at most one owned card proposal** — or withholds / abstains with a full trace. Humans decide and execute. L5 owns the live card. L3 owns detection methods and money calculation. L2 owns plant source-of-truth records. L4 owns the decision runtime, the derived Plant Situation Model, and the opportunity ledger.

## Eight ideas this set leads with

1. **A small kernel of rules; everything else is replaceable.** Code owns terminals, hard stops, money references, constraint checks, and the one-card rule. Models, prompts, and registries live inside and swap by release.
2. **See the whole plant, decide about one thing.** The Plant Situation Model holds structure, history, and state. Each run gets a focused, provenance-tagged slice.
3. **Constraints are code, not prose.** Typed predicates return satisfied, violated, or unknown. A model may explain; it never evaluates a gate.
4. **Evidence before words.** Every claim cites a ledger row. Uncited claims are dropped. Models never assign an evidence tier or a rupee.
5. **Two ways in, one way out.** Findings and discoveries meet the same floor, the same constraint check, and the same portfolio.
6. **The plant is a portfolio.** Cards carry footprints; overlapping footprints conflict; owners have a per-shift budget (exceptions exempt via registry).
7. **Built to change, including at the core.** Domains, families, workflows, stages, analyses, patterns, constraint kinds, tools, prompts, memory missions, and model pins are versioned registry entries under one release lockfile. The kernel never names a specific domain.
8. **Nothing is silently lost, and every block teaches.** Soft-gate blocks reach the opportunity ledger and the owner's backlog. Exploration measures whether blocked items would have helped. Soft gates then move on evidence.

## Reading order

| Order | Doc | Role |
| --- | --- | --- |
| 0 | [`00-kernel.md`](00-kernel.md) | Normative frozen surface |
| 1 | [`01-system-overview.md`](01-system-overview.md) | End-to-end picture + Mermaid |
| 2 | [`02-plant-structure.md`](02-plant-structure.md) | Site-pack topology |
| 3 | [`03-plant-situation-model.md`](03-plant-situation-model.md) | PSM |
| 4 | [`04-constraints.md`](04-constraints.md) | Typed constraints |
| 5 | [`05-context-engineering.md`](05-context-engineering.md) | Ledgers and zoom |
| 6 | [`06-memory.md`](06-memory.md) | Hindsight, case library |
| 7 | [`07-finding-runtime.md`](07-finding-runtime.md) | Finding → terminal |
| 8 | [`08-discovery.md`](08-discovery.md) | Scanners, patterns, hypothesis lane |
| 9 | [`09-portfolio.md`](09-portfolio.md) | Dedupe, conflict, attention |
| 10 | [`10-domain-analyses.md`](10-domain-analyses.md) | Domain plug-ins |
| 11 | [`11-models-and-seams.md`](11-models-and-seams.md) | Dual family, Jev seams |
| 12 | [`12-trace-and-eval.md`](12-trace-and-eval.md) | Trace and pass^k |
| 13 | [`13-improvement.md`](13-improvement.md) | Offline council |
| 14 | [`14-ask.md`](14-ask.md) | Ask over L4 |
| 15 | [`15-l3-l4-interface.md`](15-l3-l4-interface.md) | Contract with L3 |
| 16 | [`16-operations.md`](16-operations.md) | Deploy and monitor |
| 17 | [`17-change-guide.md`](17-change-guide.md) | How to expand |
| 18 | [`18-contract-deltas.md`](18-contract-deltas.md) | Cross-layer deltas |
| 19 | [`19-failure-modes.md`](19-failure-modes.md) | Named failure modes |
| 20 | [`20-benchmark.md`](20-benchmark.md) | How we know it works |
| 21 | [`21-registries-and-stage-graph.md`](21-registries-and-stage-graph.md) | Registries |
| 22 | [`22-missed-opportunities.md`](22-missed-opportunities.md) | Opportunity ledger |
| 23 | [`23-oe-knowledge-corpus.md`](23-oe-knowledge-corpus.md) | OE literature RAG (advisory) |
| 24 | [`24-architecture-gaps.md`](24-architecture-gaps.md) | Gap audit (historical + pointers) |
| 25 | [`25-work-queue-and-concurrency.md`](25-work-queue-and-concurrency.md) | Plant work queue |
| 26 | [`26-decision-case-lifecycle.md`](26-decision-case-lifecycle.md) | Case states, leases, resume |
| 27 | [`27-ports-and-reliability.md`](27-ports-and-reliability.md) | Timeouts, retries, breakers, idempotency |
| 28 | [`28-commissioning-and-controls.md`](28-commissioning-and-controls.md) | Safe-start, kill switch |
| 29 | [`29-software-quality-and-release.md`](29-software-quality-and-release.md) | Tests, CI, SLOs, durability |
| — | [`glossary.md`](glossary.md) | Terms |

## ADRs

| ADR | Title |
| --- | --- |
| [033](../../decisions/033-039/ADR-033-l4-decision-runtime.md) | Decision runtime |
| [034](../../decisions/033-039/ADR-034-plant-situation-model-and-memory.md) | PSM and memory |
| [035](../../decisions/033-039/ADR-035-l4-discovery.md) | Discovery |
| [036](../../decisions/033-039/ADR-036-dual-family-models.md) | Dual-family models |
| [037](../../decisions/033-039/ADR-037-site-pack-topology.md) | Site-pack topology |
| [038](../../decisions/033-039/ADR-038-soft-gates-opportunity-ledger.md) | Soft gates / opportunity ledger |
| [040](../../decisions/040-044/ADR-040-l4-production-hardness.md) | Production hardness |

## Research

- Peers and literature: [`../../research/plant-efficiency-exploration-2026-09/19-l4-agent-peer-systems.md`](../../research/plant-efficiency-exploration-2026-09/19-l4-agent-peer-systems.md)
- Vision wins on conflict: [`../../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md`](../../research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md)

## What this is not

Not code. Not a schedule optimizer. Not equipment write. Not a second plant UI. Not a graph product in L2.

---

## v1 slice vs later

| v1 | Later |
| --- | --- |
| Architecture docs + Finding runtime + PSM + dual-family seams + soft-gate ledger + OE corpus + **production hardness (`25`–`29`)** | stamped-l4 implementation of kernel **and** queue/lifecycle/ports/controls |
| Five **seeded** domain registry ids (ADR-030 framing); Pilot activates families when commissioned | Additional domains by registration |
| Cross-plant memory / priors | Not in v1 (designed seam only) |
| OE corpus Tier A public ingest | Broader Tier B/C under license / owner packs |
