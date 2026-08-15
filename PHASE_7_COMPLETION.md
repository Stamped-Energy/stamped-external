# Phase 7 completion: standalone technical decks

## Completed work

- Replaced AI-led headings with outcome-led language in the generic and ITC explainers.
- Rewrote the Nestlé opening around warehouse HVAC, tariffs, owners, and evidence.
- Restored canonical two-pillar terminology across the Nestlé brief.
- Removed internal Gurugram procurement language and made bill access optional.
- Softened predictive-maintenance language to claims supported by fixed-alarm comparisons.
- Added consistent focus states, 44px floor controls, readable mobile wrapping, and coarse-pointer navigation across all three deck families.
- Kept the ITC flat file and deploy copy byte-for-byte synchronized.

## Files modified

- `demo-decks/clients/technical-explainer.html`
- `demo-decks/clients/itc-nadiad-technical.html`
- `demo-decks/clients/itc-nadiad-technical/index.html`
- `demo-decks/clients/nestle-pantnagar-technical/index.html`

## Architectural changes

None. These publishing mirrors remain standalone HTML decks.

## Validation performed

- `git diff --check` passed.
- ITC source and deploy files are byte-identical.
- Static scans found no deprecated Nestlé pillar names, urgency headline, Gurugram reference, or required-bill language.

## Known issues

- These standalone files still duplicate their deck shell.
- Browser-level validation remains pending Playwright setup.

## Next phase

Polish the prescriptions deck, hubs, and shared technical deep-dives.

## What we learned

- Nestlé already had the strongest mobile prescription behavior; the copy taxonomy, not the interaction design, had drifted.
- Account specificity is strongest when it names the operating boundary, not internal procurement context.
- Technical depth can remain in the body while titles lead with the decision a plant team needs to make.
