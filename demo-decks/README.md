# Demo decks

Client-facing HTML presentation decks for Stamped Energy: one walkthrough per industry, plus private client packs.

| Path | Use |
|------|-----|
| [index.html](./index.html) | Industry picker (hub) |
| [cement.html](./cement.html) | Cement: kiln, mills, WHR |
| [steel.html](./steel.html) | Steel: furnace, rolling mill |
| [pharma.html](./pharma.html) | Pharma: load management, HVAC, chillers |
| [pharma/](./pharma/) | Pharma Vercel deploy root (`index.html`; `vercel --prod`) |
| [clients/](./clients/) | Client deck picker + OEM / Lohia walkthroughs (linked from hub) |
| [tech/](./tech/) | Tech deep-dives linked from the Technology slide |
| [assets/](./assets/) | Industry and client hero photos |
| [/index.html](../index.html) | Same hub at repo root for GitHub Pages |

### Client decks

From the industry hub, open **Clients** → [`clients/index.html`](./clients/index.html). Rebuild with `python3 scripts/build-client-decks.py`.

| Path | Use |
|------|-----|
| [clients/index.html](./clients/index.html) | Client deck picker |
| [clients/machinery-oem.html](./clients/machinery-oem.html) | Anonymous full Proof Run for a packaging-machinery OEM (real-time decisions, early warnings, 60-day as needed) |
| [clients/machinery-oem/](./clients/machinery-oem/) | Optional standalone deploy root for the OEM demo |
| [clients/lohia-corp-brief.html](./clients/lohia-corp-brief.html) | Short Lohia Corp meeting walkthrough (named; on-site Chaubepur ask) |

Meeting default: open the Lohia brief. Keep the anonymous OEM demo ready if the room wants a full product walkthrough without account research on-screen.

**Tech deep-dives** (shared across industries; open from `#scene-tech` cards):

| Page | Pillar |
|------|--------|
| [tech/physics.html](./tech/physics.html) | Versioned industrial physics & rulepacks |
| [tech/models.html](./tech/models.html) | Plant-calibrated industrial ML |
| [tech/agents.html](./tech/agents.html) | Bounded prescription agents |
| [tech/evidence.html](./tech/evidence.html) | Verified with evidence (calculation engine) |

Back-links use `?from={cement|steel|pharma|machinery-oem}` → deck `#scene-tech` (client decks resolve under `clients/`). Citation SSOT: [`../technical/stamped-research-and-ml-citations.md`](../technical/stamped-research-and-ml-citations.md).

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

**GitHub Pages:** enable Pages from the repo root so `/` serves the hub and `/demo-decks/*.html` serves each deck.

**Vercel (pharma only):** deploy the standalone folder:

```bash
cd demo-decks/pharma && vercel --prod
```

**Floor / verify check:**

```bash
python3 scripts/check-floor-phone.py
```
