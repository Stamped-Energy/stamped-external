# Demo decks

Client-facing HTML presentation decks for Stamped Energy: one walkthrough per industry, plus private client packs.

| Path | Use |
|------|-----|
| [/index.html](../index.html) | **GitHub Pages entry** — demo hub (industry + prescriptions + clients + tech) |
| [index.html](./index.html) | Industry picker (same links, relative) |
| [cement.html](./cement.html) | Cement: kiln, mills, WHR |
| [steel.html](./steel.html) | Steel: furnace, rolling mill |
| [pharma.html](./pharma.html) | Pharma: load management, HVAC, chillers |
| [prescriptions-examples.html](./prescriptions-examples.html) | **Cold-call / discovery:** 10 practical prescriptions (flip cards + negotiation vignette) |
| [prescriptions-examples.md](./prescriptions-examples.md) | Markdown twin — talk tracks, plain-language cards, evidence on flip |
| [technical/product/Stamped_Client_Positioning_and_Narrative_v1.md](../technical/product/Stamped_Client_Positioning_and_Narrative_v1.md) | Canonical client narrative (WhatsApp, decks, I4.0) |
| [pharma/](./pharma/) | Pharma Vercel deploy root (`index.html`; `vercel --prod`) |
| [clients/](./clients/) | Client deck picker: 11-scene technical briefs (Nestlé, ITC, LNM, Lohia, OEM, forge-HT, explainer) |
| [tech/](./tech/) | Tech deep-dives linked from the Technology slide |
| [assets/](./assets/) | Industry and client hero photos |

**GitHub Pages:** public SSOT is [`Stamped-Energy/decks-stamped`](https://github.com/Stamped-Energy/decks-stamped) → https://stamped-energy.github.io/decks-stamped/ . This private repo keeps a **mirror** of decks/brand/design for submodule consumers — **edit in `decks-stamped` first**, then sync here if needed.

### Client decks

From the industry hub, open **Clients** → [`clients/index.html`](./clients/index.html). HTML is hand-authored 11-scene briefs. `python scripts/decks/build/build-client-decks.py` only syncs `clients/assets/`.

| Path | Use |
|------|-----|
| [clients/index.html](./clients/index.html) | Client deck picker |
| [clients/nestle-pantnagar-technical/](./clients/nestle-pantnagar-technical/) | Nestlé Pantnagar Maggi leave-behind (quality bar; uses "rupee(s)") |
| [clients/itc-nadiad-technical/](./clients/itc-nadiad-technical/) | ITC Nadiad technical brief (deploy folder) |
| [clients/itc-nadiad-technical.html](./clients/itc-nadiad-technical.html) | Flat twin of the ITC folder index |
| [clients/lnm-auto-faridabad-technical/](./clients/lnm-auto-faridabad-technical/) | LNM Auto Faridabad Sector 59 leave-behind (precision forge / machine / HT / surface) |
| [clients/lohia-corp-brief.html](./clients/lohia-corp-brief.html) | Named Lohia brief (DIC, not a second audit, Chaubepur visit) |
| [clients/auto-forge-ht.html](./clients/auto-forge-ht.html) | Anonymous forge / HT / die-cast brief |
| [clients/machinery-oem.html](./clients/machinery-oem.html) | Anonymous packaging-machinery OEM brief (60-day if justified) |
| [clients/machinery-oem/](./clients/machinery-oem/) | Optional standalone deploy root |
| [clients/technical-explainer.html](./clients/technical-explainer.html) | Generic technical explainer (11 scenes; 60-day close) |

Named-account default: Nestlé or ITC. Keep OEM / forge-HT ready when the room should stay anonymous.

**Technical explainers** (also linked from the root hub): generic product explainer plus named-account briefs.

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

**Rebuild industry decks from base:** edit `demo-decks/_base.snapshot.html` and/or `scripts/decks/build/build-industry-decks.py`, then:

```bash
python scripts/decks/build/build-industry-decks.py
python scripts/decks/build/build-client-decks.py   # assets only; does not rewrite briefs
```

**Client deck gate:**

```bash
python scripts/decks/checks/check-client-decks.py
```

**GitHub Pages** (**live SSOT:** `Stamped-Energy/decks-stamped`):

| URL | Serves |
|-----|--------|
| https://stamped-energy.github.io/decks-stamped/ | Demo hub |
| https://stamped-energy.github.io/decks-stamped/demo-decks/ | Industry hub (picker) |
| https://stamped-energy.github.io/decks-stamped/demo-decks/prescriptions-examples.html | Sample prescriptions deck |
| https://stamped-energy.github.io/decks-stamped/demo-decks/clients/ | Client briefs |
| https://stamped-energy.github.io/decks-stamped/project/ | Hub via `project/index.html` |

Edit decks in **`decks-stamped`**. Mirror under this repo is for private platform consumers only. Pages is **not** deployed from `stamped-external` (private + Free org).

**Vercel (pharma only):** deploy the standalone folder:

```bash
cd demo-decks/pharma && vercel --prod
```

**Floor / verify check:**

```bash
python scripts/decks/checks/check-floor-phone.py
```
