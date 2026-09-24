# Design system — Stamped

**Synced:** 2026-09-24  
**Sources:** Main website (`Main_Website/DESIGN.md` + `styles/theme.css`) · [Bhatia Alloy × Stamped pilot deck](https://bhatia-stamped-pilot.vercel.app/#s6) · tokens [`stamped-tokens.yaml`](stamped-tokens.yaml)

Product name is **Stamped**. Never append Energy. Claims follow [ADR-030](../decisions/028-032/ADR-030-five-domain-decision-loop.md).

---

## 1. Creative north star

**Plant-office decision layer.** Bright industrial office at mid-morning: a director scanning cost and next actions — not a SaaS landing page performing “innovation.”

- Coral on near-black green against paper beige (`#f7faf5`)
- Grotesk display + Inter body + mono labels
- One job per section; real plant photography where imagery matters
- Motion is progressive (ease-out), not bounce / elastic / purple glow

**Rejects:** purple SaaS gradients, glassmorphism default, hero-metric strips, identical icon-card grids, thick colored side-stripes, MES/plant-OS claims, Plus Jakarta / Public Sans as display.

---

## 2. Colors

### Chrome (site + product UI)

| Token | Hex | Use |
|-------|-----|-----|
| **Forge Coral** (primary) | `#F75440` | CTAs, active nav, metrics, focus, 1px accent rules |
| On-primary | `#ffffff` | Text on coral |
| Primary soft | `#ffdad4` / `#fff4f1` | Tints, soft tags (deck: `--coral-soft`) |
| **Obsidian Green** (secondary) | `#000a07` | Dark contrast bands, footer gravity |
| **Process Teal** | `#00666b` | Optional support; prefer coral for interactive chrome |
| **Paper / surface** | `#f7faf5` | Default page + deck background |
| Surface ladder | `#f1f4f0` → `#e0e3df` → `#d8dbd6` | Soft bands |
| On-surface | `#191c1a` | Primary text (site) |
| Deck ink | `#051F13` | Deck headlines (Bhatia) |
| Body / muted | `#3f4a44` / `#6b716d` | Supporting copy |
| Outline | `#8f706b` / `#e3beb8` / `#e6d6d2` | Hairlines |

**One Coral Rule.** Primary = identity + action. Do not drench large chrome fills in coral; prefer text, borders, pills, metrics. Dark fills use secondary.

**Light Office Rule.** Default canvas stays light. Dark is a deliberate band, not a site theme.

### Motion scene fills (website MotionSlots only)

Forest `#4a634d`, acid `#eef981`, ember `#e35f3f`, wine `#761438`, lime `#e8f07a`, cream `#fbfcf9` — **chapter backgrounds**, never navbar/button/footer colors. Full list in Main_Website `DESIGN.md` §8.

---

## 3. Typography

| Role | Family | Use |
|------|--------|-----|
| Display / headlines / nav | **Space Grotesk** 500–700 | H1–H4, wordmark, KPI figures |
| Body / UI | **Inter** 400–700 | Paragraphs, buttons, forms |
| Labels / chips | **IBM Plex Mono** 500 | Section badges, deck chrome meta (`BHATIA ALLOY · PILOT 06 / 07`) |

Deck Google Fonts load (Bhatia): `Space+Grotesk:wght@500;600;700` · `Inter:wght@400;500;600;700` · `IBM+Plex+Mono:wght@500`.

---

## 4. Elevation & layout

- **Flat / tonal.** Depth from surface steps and 1px borders — not stacked shadows.
- Cards (decks): white fill, thin line (`#e6d6d2`), ~12px radius; coral border only for emphasis cards (e.g. indicative price).
- Primary button may use a soft coral shadow; do not generalize to every card.
- Site section rhythm: `.section-y` 4 / 5.5 / 7.5 rem.
- **Decks:** fixed **1600×900** stage, scaled with `--s`; chrome top bar + slide index; pagination dots with active coral.

---

## 5. Deck grammar (Bhatia as reference)

From [bhatia-stamped-pilot.vercel.app](https://bhatia-stamped-pilot.vercel.app/#s6):

1. Paper background; coral eyebrow label (uppercase mono/small).
2. One large Space Grotesk headline; short Inter support.
3. At most one primary composition per slide (cost table + one accent card, or flow diagram — not both plus a stats strip).
4. Numbers that matter go coral; fine print stays muted.
5. Slide meta top-right: `CLIENT · PILOT nn / nn`.
6. Ease: `cubic-bezier(0.22, 1, 0.36, 1)`; rise-in on active slide children.

Local snapshot: [`../demo-decks/clients/bhatia-alloy-pilot/index.html`](../demo-decks/clients/bhatia-alloy-pilot/index.html).

---

## 6. Do / don’t

**Do**

- Change site chrome colors only via the token set (mirror `theme.css`).
- Keep decks on the same coral / paper / Space Grotesk stack.
- Prefer hairline borders and tonal bands over card grids in heroes.
- Lead with choose → assign → verify language where product truth allows.

**Don’t**

- Second coral or second near-black for buttons/nav.
- Purple gradients, glassmorphism, thick left stripes.
- Mono on the whole navbar (badges only).
- Forest / wine / acid as chrome colors.
- “Stamped Energy” as the product name in UI.

---

## 7. Where to edit

| Surface | Edit here |
|---------|-----------|
| Tokens in this pack | `stamped-tokens.yaml` |
| Main website runtime | `Main_Website/styles/theme.css` + `DESIGN.md` |
| New / updated decks | `demo-decks/` (prefer Bhatia `:root` vars) |
| Product claims | Vision pack + ADR-030 — not this file |
