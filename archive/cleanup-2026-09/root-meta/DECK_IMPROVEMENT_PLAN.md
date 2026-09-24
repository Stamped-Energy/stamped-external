# Deck copy and design improvement plan

Approved: 2026-08-15

## Goal

Improve the credibility, clarity, visual hierarchy, accessibility, and mobile presentation of every deck and technical deep-dive under `demo-decks/`.

## Scope

- Industry and client Proof Run sources
- Prescription examples
- Generic, ITC, and Nestlé technical decks
- Technical deep-dives and deck hubs
- Generated deployment copies through their builders
- Relevant validation scripts and documentation

## Non-goals

- A new presentation framework or dependency
- A full migration of standalone decks into the shared builder
- Product features unrelated to the walkthroughs

## Phases

| Phase | Objective | Status |
| --- | --- | --- |
| 1 | Correct shared Proof Run copy, credibility, mobile, and accessibility issues | Complete |
| 2 | Polish standalone technical and account decks | Complete |
| 3 | Polish prescriptions, hubs, and technical deep-dives | Complete |
| 4 | Extend validation and complete visual QA | Complete |
| 5 | Final consistency review and delivery | Complete |

## Decisions

- Improve canonical sources and regenerate outputs; do not edit generated copies independently.
- Preserve the current presentation architecture instead of performing a high-risk template migration.
- Treat copied technical explainers as local publishing mirrors for this pass.
- Prefer qualified scenarios and illustrative labels over universal savings claims.

## Risks

- Named-client facts must remain sourced or be removed.
- Standalone deck forks can drift until they share a builder.
- Browser checks require Playwright in the validation environment.
