# Demo decks

Client-facing HTML presentation decks for Stamped Energy: one walkthrough per industry, plus private client packs.

| Path | Use |
|------|-----|
| [/index.html](../index.html) | **GitHub Pages entry** — demo hub (industry + prescriptions + clients + tech) |
| [index.html](./index.html) | Industry picker (same links, relative) |
| [cement.html](./cement.html) | Cement: kiln, mills, WHR |
| [steel.html](./steel.html) | Steel: furnace, rolling mill |
| [pharma.html](./pharma.html) | Pharma: load management, HVAC, chillers |
| [prescriptions-examples.html](./prescriptions-examples.html) | 10 sample prescriptions (flip cards; client pack) |
| [prescriptions-examples.md](./prescriptions-examples.md) | Markdown twin — **floor-tied illustrations** + constraint rules |
| [technical/product/Stamped_Client_Positioning_and_Narrative_v1.md](../technical/product/Stamped_Client_Positioning_and_Narrative_v1.md) | Canonical client narrative (WhatsApp, decks, I4.0) |
| [pharma/](./pharma/) | Pharma Vercel deploy root (`index.html`; `vercel --prod`) |
| [clients/](./clients/) | Client deck picker + OEM / Lohia walkthroughs (linked from hub) |
| [tech/](./tech/) | Tech deep-dives linked from the Technology slide |
| [assets/](./assets/) | Industry and client hero photos |

**GitHub Pages:** workflow [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) deploys root `index.html` + `demo-decks/` from `main`. Enable Pages → Source: **GitHub Actions** once in repo Settings.

### Client decks

From the industry hub, open **Clients** → [`clients/index.html`](./clients/index.html). Rebuild with `python3 scripts/build-client-decks.py`.

| Path | Use |
|------|-----|
| [clients/index.html](./clients/index.html) | Client deck picker |
| [clients/machinery-oem.html](./clients/machinery-oem.html) | Anonymous full Proof Run for a packaging-machinery OEM (real-time decisions, early warnings, 60-day as needed) |
| [clients/machinery-oem/](./clients/machinery-oem/) | Optional standalone deploy root for the OEM demo |
| [clients/lohia-corp-brief.html](./clients/lohia-corp-brief.html) | Short Lohia Corp meeting walkthrough (named; on-site Chaubepur ask) |
| [clients/technical-explainer.html](./clients/technical-explainer.html) | Generic Stamped Intelligence technical explainer (11 slides; sales collateral) |
| [clients/itc-nadiad-technical.html](./clients/itc-nadiad-technical.html) | ITC Nadiad account technical brief (named; packaging &amp; printing) |
| [clients/itc-nadiad-technical/](./clients/itc-nadiad-technical/) | GitHub Pages deploy root for ITC brief (hero `nadiad-plant.jpg`) |

Meeting default: open the Lohia brief. Keep the anonymous OEM demo ready if the room wants a full product walkthrough without account research on-screen.

**Technical explainers** (also linked from the root hub): generic product explainer plus named-account briefs. Source HTML is authored in `Stamped-Energy` and copied here for GitHub Pages.

**Tech deep-dives** (shared across industries; open from `#scene-tech` cards):

| Page | Pillar |
|------|--------|
| [tech/physics.html](./tech/physics.html) | Versioned industrial physics & rulepacks |
| [tech/models.html](./tech/models.html) | Plant-calibrated industrial ML |
| [tech/agents.html](./tech/agents.html) | Bounded prescription agents |
| [tech/evidence.html](./tech/evidence.html) | Verified with evidence (calculation engine) |

Back-links use `?from={cement|steel|pharma|machinery-oem}` → deck `#scene-tech` (client decks resolve under `clients/`). Citation SSOT: [`../technical/research/stamped-research-and-ml-citations.md`](../technical/research/stamped-research-and-ml-citations.md).

Each industry deck keeps the same Proof Run structure. What changes:

- **Prescriptions** (short, readable actions + evidence tags)
- **Data sources** called out in the hook / gap / “what we read” slides
- **Optimisation targets** on the savings map (what we check first)
- **Hero photo** matched to the industry

Open an industry file in a browser. Arrow keys, space, or on-screen controls navigate. On phones, the title slide is **text → Begin → plant photo**; the simulated Sample workspace slide is skipped. On the **floor** slide, Snooze / Acknowledge cycle three prescriptions on the phone, then show **Stamped Energy**.

**Rebuild from base:** edit `demo-decks/_base.snapshot.html` (generic template) and/or `scripts/build-industry-decks.py`, then:

```bash
python3 scripts/build-industry-decks.py
python3 scripts/build-client-decks.py   # private OEM + Lohia brief
```

**Client deck gate:**

```bash
python3 scripts/check-client-decks.py
```

**GitHub Pages** (`Stamped-Energy/stamped-external`, branch `main`, path `/`):

| URL | Serves |
|-----|--------|
| https://stamped-energy.github.io/stamped-external/demo-decks/ | Industry hub (picker) |
| https://stamped-energy.github.io/stamped-external/demo-decks/prescriptions-examples.html | Sample prescriptions deck |
| https://stamped-energy.github.io/stamped-external/project/ | Same hub via `project/index.html` |

Static HTML under `demo-decks/` and `project/` deploys automatically when merged to `main`. No extra workflow step.

**Vercel (pharma only):** deploy the standalone folder:

```bash
cd demo-decks/pharma && vercel --prod
```

**Floor / verify check:**

```bash
python3 scripts/check-floor-phone.py
```
