# Competitive research (Stamped Energy)

Docs in this folder are written for **founder readability** — plain English first, short paragraphs, concrete examples. Jargon (ToD, MD, BESS, BRSR, PAT, …) is defined in parentheses the first time it appears in each gap note.

## What to read

| File | What it is |
| --- | --- |
| [00-stamped-capability-baseline.md](00-stamped-capability-baseline.md) | What Stamped already does (plain-English loop at top; detailed cited inventory below) |
| [01-vendor-research-raw.md](01-vendor-research-raw.md) | Vendor-stated claims with source URLs (2026-09-21 + deepening pass 2026-09-22) |
| [02-what-we-should-add.md](02-what-we-should-add.md) | Ranked backlog of software we should add ourselves (and what not to build) |
| [gap-enercog.md](gap-enercog.md) | EnerCog vs Stamped — plain English |
| [gap-voltwin.md](gap-voltwin.md) | VolTwin / Wistwin vs Stamped — plain English |
| [gap-tech-ovn.md](gap-tech-ovn.md) | Tech OVN vs Stamped — plain English |
| [gap-ltts-energisensei.md](gap-ltts-energisensei.md) | LTTS EnergiSensEI vs Stamped — plain English |
| [gap-abb-optimax.md](gap-abb-optimax.md) | ABB OPTIMAX vs Stamped — plain English |

## Framing

- Product loop: Connect → Observe → Decide → Execute → Verify → Improve ([`technical/STAMPED_ARCHITECTURE.md`](../../technical/STAMPED_ARCHITECTURE.md) §3; pack map [`docs/PRODUCT_MAP_STAMPED_EXTERNAL.md`](../../docs/PRODUCT_MAP_STAMPED_EXTERNAL.md))
- Two pillars + shared context (not MES): [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md)
- Human-guided writeback: [ADR-029](../../decisions/028-032/ADR-029-human-guided-ot-command-path.md) = **specified, not shipped**
- Never invent plant ₹ savings; competitor marketing % are claims only

## How gap notes are structured

Each `gap-*.md` uses: one sentence → what they do → what we already do → real gaps (what / why plant cares / SW|HW / can we add / should we) → bottom line (threat / partner / ignore).
