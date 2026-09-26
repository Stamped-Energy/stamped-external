# Stamped Platform — shared architecture, contracts, and handoff

> **What it is:** The single source of truth for Stamped’s cross-repo platform layer — JSON schemas, ADRs, technical specs, design system, and handoff playbooks.  
> **What it is not:** Application code, deploy compose, or a runnable service. Consumer repos mount this pack as a git submodule and implement layers L1–L6.  
> **Product:** Stamped helps a plant team choose, assign, and verify the next operating action across quality and yield, energy and waste, uptime, and dynamic scheduling.  
> **Company policy:** [`Stamped_Master_Document.md`](Stamped_Master_Document.md) (wins on identity) · Architecture: [`technical/STAMPED_ARCHITECTURE.md`](technical/STAMPED_ARCHITECTURE.md)  
> **GitHub:** [Stamped-Energy/stamped-external](https://github.com/Stamped-Energy/stamped-external) · **Prior product snapshot:** tag `v2026.09.24`

---

**TL;DR**

- **One product, four outcomes, one card, one owner** — [`Stamped_Master_Document.md`](Stamped_Master_Document.md)
- **L3 signal + L4 brain are the core** — detect → decide/answer → close → show
- **One repo per layer** communicates only through **versioned contracts** ([ADR-008](decisions/006-010/ADR-008-layer-repo-topology-and-interfaces.md))
- **SSOT:** [`technical/STAMPED_ARCHITECTURE.md`](technical/STAMPED_ARCHITECTURE.md) · layers [`technical/layers/`](technical/layers/) · L3 [`technical/l3/`](technical/l3/) · L4 [`technical/l4/`](technical/l4/)
- **Coarse evolution:** [`research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md`](research/plant-efficiency-exploration-2026-09/14-coarse-architecture.md)
- **Agent entry:** [`Stamped_Master_Document.md`](Stamped_Master_Document.md) → architecture SSOT → layer pages → L3/L4 depth
- **Design / brand:** [`design/`](design/) (website + [Bhatia pilot deck](https://bhatia-stamped-pilot.vercel.app/#s6))
- **Demo decks:** [`demo-decks/`](demo-decks/)
- Pin consumers to a **specific SHA or semver tag**; never float on `main` in production branches
- **L1–L2 context plane:** [`technical/L1-L2-DATA-PLANE.md`](technical/L1-L2-DATA-PLANE.md) · [ADR-031](decisions/028-032/ADR-031-l1-l2-context-records.md)

---

## 1. Vision

### 1.1 What Stamped is

Stamped is software that turns plant signals into a **specific next step** for a person, **records** the choice, and **checks** what happened across quality and yield, energy and waste, uptime, and dynamic scheduling. Energy and waste often opens the first conversation. It is not the company name and not the product category.

Full policy: [`Stamped_Master_Document.md`](Stamped_Master_Document.md). Stack summary: [`technical/STAMPED_ARCHITECTURE.md`](technical/STAMPED_ARCHITECTURE.md).

### 1.2 What this repository is

| Aspect | Description |
|--------|-------------|
| **Name** | `stamped-external` (platform pack) |
| **Role** | Shared contracts, ADRs, specs, design system, handoff docs |
| **Distribution** | Git submodule at `external/` in every consumer repo ([ADR-011](decisions/011-015/ADR-011-stamped-platform-submodule-distribution.md)) |

### 1.3 What this repository is not

- Not application code
- Not deploy compose files
- Not customer data or secrets
- Not the live website (site lives in Stamped-Energy-Website / local `Main_Website`)

### 1.4 Who it is for

| Audience | Use |
|----------|-----|
| **Layer repo engineers** | Implement against contracts and ADRs |
| **Platform maintainers** | Evolve schemas, ADRs, handoff, design tokens |
| **AI coding agents** | Onboard via [`AGENTS.md`](AGENTS.md) + vision pack |

---

## 2. Architecture

Start at [`technical/STAMPED_ARCHITECTURE.md`](technical/STAMPED_ARCHITECTURE.md) for the L0–L6 map, then:

| Depth | Path |
| --- | --- |
| Layer pages | [`technical/layers/`](technical/layers/) — L1, L2, L5, L6 |
| L3 deep | [`technical/l3/`](technical/l3/) — Findings, dual-lane, engines |
| L4 deep | [`technical/l4/`](technical/l4/) — decision runtime contract + [`30-as-built.md`](technical/l4/30-as-built.md) |
| L1–L2 configure | [`technical/L1-L2-DATA-PLANE.md`](technical/L1-L2-DATA-PLANE.md) |

---

## 3. Reading order for engineers and agents

1. [`Stamped_Master_Document.md`](Stamped_Master_Document.md) — company policy  
2. [`AGENTS.md`](AGENTS.md)  
3. [`technical/STAMPED_ARCHITECTURE.md`](technical/STAMPED_ARCHITECTURE.md)  
4. [`technical/layers/`](technical/layers/) for your layer  
5. Depth: [`technical/l3/`](technical/l3/) or [`technical/l4/`](technical/l4/) when changing detection or the decision runtime  
6. Supporting history (do not override master): [`AGENT-START.md`](research/plant-efficiency-exploration-2026-09/AGENT-START.md) → [`09`](research/plant-efficiency-exploration-2026-09/09-stamped-founder-vision.md) → [`10`](research/plant-efficiency-exploration-2026-09/10-stamped-vision-agent-alignment.md) · [ADR-030](decisions/028-032/ADR-030-five-domain-decision-loop.md) (amended)  
7. [`handoff/README.md`](handoff/README.md) → integration playbooks for your repo  
8. [`decisions/README.md`](decisions/README.md) · [`contracts/`](contracts/) + `./scripts/contracts/contract-check.sh`  
9. [`design/`](design/) when touching UI or decks

You can stay inside this repository for the full technical picture; consumer repos add implementation detail, not a second architecture story.

---

## 4. Platform pack contents

| Path | Purpose |
|------|---------|
| `contracts/` | Versioned JSON schemas + fixtures |
| `decisions/` | Active ADRs |
| `technical/` | Architecture SSOT + pointers |
| `handoff/` | Cross-repo integration docs |
| `design/` | Brand + design system + tokens |
| `demo-decks/` | Client / industry HTML decks (incl. Bhatia pilot snapshot) |
| `future/` | Open tech directions (not live product) |
| `pilot-research/` | Pilot plant notes |
| `research/plant-efficiency-exploration-2026-09/` | Vision + coarse architecture authority |
| `archive/` | Pre-overhaul marketing + 2026-09 cleanup |

---

## 5. Consumer repositories

See [REPOS.md](REPOS.md) and [SUBMODULE.md](SUBMODULE.md). After this pack lands on default branch, consumers pin the merge SHA and update their `AGENTS.md` reading order.

---

## 6. Contributing & release

- Conventional commits; tag platform releases as needed after this overhaul.
- Contract changes: run `./scripts/contracts/contract-check.sh`
- Identity: run `./scripts/vision-identity-lint.ps1` before merge on vision-sensitive PRs

## Changelog

Historical entries in [CHANGELOG.md](CHANGELOG.md) describe the prior product. Do not take company identity from those sections. Prior snapshot: `v2026.09.24`.
