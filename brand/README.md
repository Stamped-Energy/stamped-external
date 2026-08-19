# Stamped public copy (portable)

Customer-facing origin, problem, and solution for agents that do **not** have the Main_Website repo. Technical architecture stays in [`technical/STAMPED_ARCHITECTURE.md`](../technical/STAMPED_ARCHITECTURE.md).

## Agent read-order (mandatory for copy)

1. [`COPY_CANON.md`](COPY_CANON.md) — why we exist, how the site frames problem and solution, rupee compounds, what not to use
2. [`WEBSITE_COPY.md`](WEBSITE_COPY.md) — snapshot of homepage, solutions, and About
3. Then write. Prefer verbatim strings or close paraphrases.

If this pack is mounted inside **Main_Website**, live SSOT is `lib/content/` (`about.ts`, `landing.ts`, `solutions.ts`, `site.ts`). Update this folder when those pages change.

## Sync rule

When homepage, solutions hub/pillars, or About copy changes on stamped.work / Main_Website, update `COPY_CANON.md` and `WEBSITE_COPY.md` in the same change set (or immediately after).

## Not this folder

- Master Document, ICP tables, four-step Client Positioning narrative — GTM/decks, not public About or homepage
- Layer contracts, ADRs, handoff specs — engineering
