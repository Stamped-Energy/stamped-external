# Phase 9 completion: validation and visual QA

## Completed work

- Fixed Playwright check roots so they serve the repo, not `scripts/decks/`.
- Broadened the floor-phone check to all six generated Proof Run decks and asserted 44px floor controls.
- Added a standalone check for prescriptions, technical briefs, tech pages, and hubs.
- Confirmed ITC flat and folder copies stay byte-identical.
- Raised the tech-page brand link to 44px after mobile QA caught a 24px target.

## Files modified

- `scripts/decks/checks/check-floor-phone.py`
- `scripts/decks/checks/check-pharma-deck.py`
- `scripts/decks/checks/check-standalone-decks.py`
- `demo-decks/tech/deep-dive.css`

## Architectural changes

None. Validation still uses the existing Playwright scripts. Playwright stays a local tool, not a repo dependency.

## Validation performed

- `python3 scripts/decks/checks/check-client-decks.py`
- `python3 scripts/decks/checks/check-pharma-deck.py`
- `python3 scripts/decks/checks/check-floor-phone.py`
- `python3 scripts/decks/checks/check-standalone-decks.py`
- Mobile and desktop screenshots under `/tmp/standalone-deck-audit`

## Known issues

- Snapshot `model conf` strings remain as builder replacement anchors, not buyer-facing copy.
- Slide dots stay visible under fine-pointer emulation; coarse-pointer CSS hides them.
- Prescriptions talk tracks still use em dashes. Named client Proof Runs do not.

## Next phase

Final consistency review, leftover copy close-out, and delivery docs.

## What we learned

- Check scripts that walk up the wrong number of parents fail with 404s that look like missing decks.
- A 44px rule on “controls” will miss a brand link unless the selector list includes it.
- Screenshot QA on a fine pointer does not prove the coarse-pointer hide-dots rule.
