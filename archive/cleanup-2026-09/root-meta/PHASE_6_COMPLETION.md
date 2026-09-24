# Phase 6 completion: shared deck trust and accessibility

## Completed work

- Replaced AI-forward title labels with plant-facing outcomes.
- Replaced the universal 15% savings claim with explicit scenario arithmetic.
- Marked industry and machinery-OEM rupee impacts as illustrative.
- Removed client-facing model-confidence numbers and unsupported Lohia solar figures.
- Reframed work-order and ESG language around assigned actions and auditable evidence.
- Added 44px floor controls, keyboard focus styles, safer mobile wrapping, and coarse-pointer navigation behavior.
- Corrected stale hub builders so rebuilds retain prescription, client, explainer, and technical links.

## Files modified

- Shared Proof Run template and generated industry/client decks
- Industry and client content packs
- Industry and client hub builders
- Deck hub outputs and client deck index documentation

## Architectural changes

No presentation architecture changed. Canonical template and content-pack ownership remains intact. Hub content now lives in its builders instead of relying on manual edits that regeneration deletes.

## Validation performed

- Industry and client builders completed successfully.
- `git diff --check` passed.
- Static scans found none of the removed AI-forward labels, universal 15% claim, work-order headline, or model-confidence copy in generated decks.
- Browser checks were attempted but require Playwright, which is not installed in the current environment.

## Known issues

- Browser-level mobile checks remain pending.
- Standalone technical decks and deep-dives are handled in later phases.

## Next phase

Polish the generic, ITC, and Nestlé technical decks, then synchronize their deployment copies.

## What we learned

- The checked-in hubs had drifted ahead of their builders, so any rebuild silently removed valid deck links.
- One shared template change corrects six presentation surfaces while preserving deck-specific content.
- Scenario arithmetic communicates commercial scale without presenting an estimate as measured savings.
