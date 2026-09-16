# Product map — Stamped External (`stamped-external`)

*Read-only discovery snapshot for baseline discussions. Sources: repo docs as of platform tag lineage in [REPOS.md](../REPOS.md) (contracts **0.11.2**).*

---

## Terminology disambiguation (read this first)

| Term | What it is **not** | What it **is** |
| --- | --- | --- |
| **Stamped External** / `stamped-external` | A customer-facing product pillar | The **platform pack** (also `stamped-platform`): contracts, ADRs, handoff, technical SSOT, copy canon, compliance, design tokens |
| **`external/` folder** in layer repos | A second product | Git submodule mount pointing at `stamped-external` ([ADR-011](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md)) |
| **Two pillars** | External vs internal repos | **Outcome pillars inside one product** — Load & Energy vs Prescriptive Equipment ([ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md)) |
| **Stamped-Energy** | The platform pack | Company / product brand; **Stamped Intelligence** is the product name; layer repos hold runnable application code |

If the question is “how does External fit alongside the main product?”, the documented answer is: **External is the shared specification layer; the main product is implemented across L1–L6 consumer repositories that submodule this pack.**

---

## What Stamped External is

**Stamped External** (`vinayak-rz/stamped-external`, org mirror `Stamped-Energy/stamped-external`) is the **single source of truth for cross-repo platform concerns** — not application code, not deploy compose, not customer telemetry.

From [README.md](../README.md) §1.2:

- **Name:** `stamped-external` (platform pack; also **stamped-platform**)
- **Role:** Shared contracts, ADRs, specs, handoff docs, compliance register, design tokens, agent-facing **public marketing voice** (`copy/`)
- **Distribution:** Git submodule at `external/` in every layer consumer ([ADR-011](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md))
- **Primary interface:** Versioned git tags (`vYYYY.MM.DD`); consumers pin tags and run `contract-check.sh`

**What it is not** ([README.md](../README.md) §1.3): runnable services, production secrets, live website (that is **Main_Website** when present), or a monitoring/ESG-only product.

The **product vision** lives here as architecture and copy canon; **implementation** lives in per-layer repos listed in [REPOS.md](../REPOS.md).

---

## Role as a pillar (name + citation)

**Stamped External is not one of the two product pillars.**

Product framing lock ([ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md), echoed in [technical/STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md) §1):

```text
One product — Stamped Intelligence
 ├── Pillar 1 — Load & Energy Efficiency Intelligence   (hero ₹ / SEC / bill)
 ├── Pillar 2 — Prescriptive Equipment Intelligence     (equipment early warnings)
 └── Shared context — orders, departments, tradeoffs, negotiation, Improve
```

Client-facing pillar labels ([copy/README.md](../copy/README.md)): **Industry Energy Management** · **Asset Health Intelligence**.

**Stamped External’s architectural role** is the **platform pillar in the engineering sense** — the pack that keeps one L0–L6 product coherent across repos:

> “One product, two pillars + shared context” — framing lock [ADR-026]; SSOT [STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md)  
> — [README.md](../README.md) TL;DR

Layer repos communicate **only** through versioned contracts in this pack ([ADR-008](../decisions/006-010/ADR-008-layer-repo-topology-and-interfaces.md)).

---

## Key capabilities / modules

Top-level modules (confirmed by directory layout + [README.md](../README.md) §3):

| Module | Purpose |
| --- | --- |
| [`contracts/`](../contracts/) | JSON schemas (telemetry, plant, intelligence, closure), MQTT topics ([TOPICS.md](../contracts/TOPICS.md)), dedupe golden fixtures, semver changelog |
| [`decisions/`](../decisions/) | ADRs (topology, compliance, L3–L6, holistic plant, two-pillar lock, human-guided writeback, etc.) |
| [`technical/`](../technical/) | Product + engineering SSOT ([STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md)), per-layer specs L1–L6, cross-cutting production/eval/Rx practicality |
| [`architecture/`](../architecture/) | Implementation authority for layer boundaries (e.g. [layer-interfaces-l2.md](../architecture/layer-interfaces-l2.md)) |
| [`handoff/`](../handoff/) | Bootstrap playbooks per repo (connectors, L2–L6, deployment profiles, holistic/MES-lite context, agent prompts) |
| [`copy/`](../copy/) | Agent-facing selling copy (website canon mirror, client narrative, Rx catalog, deck claim sheets) |
| [`compliance/`](../compliance/) | India regulatory register (CERT-In, DPDP, OT read-only, metering) |
| [`design/`](../design/) | Forge Industrial design system tokens |
| [`consumers/`](../consumers/) | Mirrored consumer READMEs + seeds (e.g. stamped-l6) |
| [`demo-decks/`](../demo-decks/) | Mirror of public deck hub — edit SSOT in [`decks-stamped`](https://github.com/Stamped-Energy/decks-stamped) |
| [`scripts/contracts/`](../scripts/contracts/) | CI contract validation |
| [`.cursor/`](../.cursor/) | Vendored Cursor rules/skills for agents working across repos |

**Seven-layer product stack** (implemented in consumer repos, specified here):

| Layer | Consumer repos (examples) | Pack-owned artifacts |
| --- | --- | --- |
| L0 | Customer plant | — |
| L1 | connectors-edge, connectors-cloud, connectors-bill | L1 schemas, MQTT, portability handoffs |
| L2 | universal-repositary (stamped-l2) | Envelope ingest, six-store model spec |
| L3 | intelligence-core, intelligence-rulepacks, intelligence-evals | Finding engines, rulepacks, eval gates |
| L4 | knowledge-reasoning | Rx drafting, RAG, plant context graphs |
| L5 | closure-verification | Workflow, M&V, WhatsApp, ledger, Improve |
| L6 | experience-integration / stamped-l6 seed | Dashboard, BFF, EMS console, analyst |

**Deployment modes** (same contracts everywhere): `local`, `local-dashboard`, `cloud` — [ADR-010](../decisions/006-010/ADR-010-deployment-profiles-and-portability.md).

**Operating loop** (product, not pack-specific): Connect → Observe → Decide → Execute → Verify → Improve — [STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md) §3.

---

## Target user / buyer / problem

**Platform pack audiences** ([README.md](../README.md) §1.4): layer engineers, platform maintainers, AI agents, architects/product — people who need one coherent contract and decision set.

**End customer / buyer** (product, documented in pack):

| Dimension | Definition |
| --- | --- |
| **Who** | Plant heads, maintenance heads, electrical heads at large Indian energy-intensive manufacturers ([PRODUCT.md](../PRODUCT.md), [copy/client/POSITIONING_AND_NARRATIVE.md](../copy/client/POSITIONING_AND_NARRATIVE.md)) |
| **Category** | Verified-with-evidence **operational decision layer** — not EMS/MES/CMMS replacement |
| **Hero outcome** | ₹ energy / bill efficiency with **assigned prescriptions** and **evidence-backed verification** |
| **Co-benefit** | Plant effectiveness (OEE, order risk) on Rx when order context exists — **not** a third pillar |
| **Enemy** | Insight without closure — dashboards and alerts that never become owned, verified actions |
| **Integration posture** | Read-only OT by default; optional human-approved desk execution where configured ([copy/CONTROL_AND_ACTION.md](../copy/CONTROL_AND_ACTION.md), [ADR-029](../decisions/028-032/ADR-029-human-guided-ot-command-path.md)) |

**Savings model** (product claim architecture): closed prescriptions across six waste categories × closure rate × M&V — not a single model score ([STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md) §6, [README.md](../README.md) §2.4).

---

## Relationship to Stamped-Energy

| Artifact | Relationship |
| --- | --- |
| **Stamped-Energy (company)** | Builds **Stamped Intelligence**; public framing “intelligence layer for the industrial world” — [copy/website/COPY_CANON.md](../copy/website/COPY_CANON.md) |
| **`Stamped-Energy/stamped-external`** | Canonical org home for this platform pack per [REPOS.md](../REPOS.md); consumers still often reference `Vinayak-RZ/*` clones |
| **Layer consumer repos** | Application code; mount this repo at `external/`; implement L1–L6 per handoff docs |
| **Main_Website** | Live public website SSOT (`lib/content/`) when present; this repo holds **mirror** website copy under `copy/website/` |
| **`decks-stamped`** | Public deck HTML SSOT; `demo-decks/` here is mirror-only |
| **ADR-001 reference** | `external/technical/` described as reference specs “from Stamped-Energy” — pack centralizes what was previously copied |

**`stamped-external-world`:** Not referenced anywhere in this repository. Treat as unknown/out-of-pack unless defined elsewhere.

**Internal vs external naming:** “External” means **externally versioned platform submodule**, not “external customer product” or “pillar B.” Application repos are “internal” in the sense of **shipping runtime code**, but they are still one product under ADR-026.

---

## Gaps / product-strategic TODOs

Documented in-repo (not invented):

| Area | Status / gap | Source |
| --- | --- | --- |
| Submodule migration | Phase 1: all consumers pinned to same platform tag — **planned / in progress** | [README.md](../README.md) §16.1, [PROGRESS.md](../PROGRESS.md) |
| Consumer pin drift | REPOS table may lag latest platform tag | [REPOS.md](../REPOS.md) note on `v2026.08.21` vs older pins |
| L5/L6 maturity | Handoff + ADRs exist; README history still marks some as “planned” while REPOS lists `closure-verification` and `experience-integration` | [REPOS.md](../REPOS.md) vs [README.md](../README.md) §4 |
| Published `stamped-l1-contracts` package | Optional P1; submodule is P0 | [ADR-011](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md) |
| Third pillar / MES product | **Forbidden** for now; research says deepen co-benefits, not production hero | [ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md), [technical/research/india-mes-ai-and-production-rx-opportunity.md](../technical/research/india-mes-ai-and-production-rx-opportunity.md) |
| Parked futures | Plant margin optimization; production-efficiency Rx — require founder + new ADR | [future/README.md](../future/README.md) |
| Human-guided OT writeback | ADR-029 + contracts wave specified; **code Wave C later** | [PROGRESS.md](../PROGRESS.md) |
| Research canon sync | `Stamped_Two_Pillar_Technical_Framing_v1.md` in research repo — sync called out in ADR-026 | [ADR-026](../decisions/024-026/ADR-026-two-pillars-shared-context.md) |
| Deck/design vs platform | [PRODUCT.md](../PRODUCT.md) scopes impeccable/deck trust work in this repo separately from contract SSOT |
| Org/repo naming | Mix of `Vinayak-RZ/*` and `Stamped-Energy/*` URLs — operational clarity for Vinayak | [REPOS.md](../REPOS.md), [README.md](../README.md) |

---

## Quick reference — “two of what?”

| Question | Answer |
| --- | --- |
| Two **product** pillars? | (1) Load & Energy Efficiency Intelligence (2) Prescriptive Equipment Intelligence + shared context |
| Two **repos** at company level? | **Platform pack** (`stamped-external`) + **many layer implementation repos** (not a strict duo) |
| Two **deployment** postures? | Three modes: `local`, `local-dashboard`, `cloud` — same contracts |

---

## Citations index (authoritative reads)

1. [README.md](../README.md) — pack role, L0–L6, consumers  
2. [technical/STAMPED_ARCHITECTURE.md](../technical/STAMPED_ARCHITECTURE.md) — product + technical SSOT  
3. [decisions/024-026/ADR-026-two-pillars-shared-context.md](../decisions/024-026/ADR-026-two-pillars-shared-context.md) — pillar lock  
4. [decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md](../decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md) — why External exists  
5. [REPOS.md](../REPOS.md) — consumer repo map  
6. [copy/README.md](../copy/README.md) — what we sell (client language)  
7. [handoff/README.md](../handoff/README.md) — agent/engineer navigation  
