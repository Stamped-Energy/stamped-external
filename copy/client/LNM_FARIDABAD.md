# LNM Auto Faridabad — site value prop (internal)

**Audience:** agents and founders before LNM rooms. **Not** homepage / About. **Not** a third SKU.  
**Status:** Consumed 27 Aug 2026 from the live FANUC pack. Deck HTML is still the generic forge-HT brief until we retarget it.  
**SSOT for cards / fields / readiness:** `connectors-edge/packages/site-lnm-mtlinki/docs/prescriptions/` (`README.md`, `catalogue-client.md`, `catalogue.md`, `gaps-and-asks.md`, `rx-catalogue.json`). Do not fork the 100 cards here.

Plant study: [`../../pilot-research/lnm-plant-ee-me-sw.md`](../../pilot-research/lnm-plant-ee-me-sw.md). Claim-sheet stub: [`../decks/CLIENT_BRIEFS.md`](../decks/CLIENT_BRIEFS.md). Control language: [`../CONTROL_AND_ACTION.md`](../CONTROL_AND_ACTION.md).

---

## 1. What we actually have at LNM

LNM already paid for **FANUC MT-LINKi**. It already records machine state, alarms, a 24-hour Gantt, the product on the machine, program history, and a power-by-state split. Shop-floor people are not in that UI. IT downloads a report the next day.

26 Aug 2026 sample (`CNC_14_S2`, 31-machine fleet):

| Already true | Not true yet |
|---|---|
| Live OPERATE / STOP / ALARM / EMERGENCY / DISCONNECT on 31 machines | Alarm **codes** in the API (`2019` / `2029` seen in the UI only) |
| ~527 Gantt state cuts / 24 h on one machine | kWh and ₹ (power schema live, **every value is 0**) |
| Product `1774*P/M` on the Gantt (no ERP needed) | Plan vs actual (`Plans = 0`) |
| `CNC_14` cell split (S2 running, S1 stopped) | ERP due date, ForgeLink, SQF/SCADA, APFC / DHBVN bill |
| Induction `INDUCTION_01` / `02` already on FANUC | Named setter roster (paper map is enough to start) |

**Event volume (order of magnitude only, do not quote as a measured fleet total):** one machine ~863 state+alarm rows / day. Clustering is the product. ADR-021 caps business pushes at 3 per role per day.

---

## 2. Value proposition (after the “execution from data” conversation)

The buyer complaint was: industries have data; **monitoring screens are not worth anything**; they want **execution derived from the data**. That is LNM’s situation in one sentence.

They did not buy a missing dashboard. They bought a collector whose last mile is a CSV and a meeting.

**Commercial sentence for the room**

> You already collect machine data. We remove the delay between an abnormal event and the person who must act. We put rupees on the DHBVN bill when the electrical data is there. We use production information so the action respects the order. We do not replace FANUC, ForgeLink, or ERP.

**What that is not:** a second FANUC screen, an OEE hero, a MES, vibration PdM, or silent CNC write.

**Job, not category:** named action, owner on this shift, deadline, close when the **machine** returns to OPERATE. Energy cost, lost minutes, and maintenance inspect are three reasons the same card can exist. They are not three products.

### How to rank the four outcomes *in this plant*, this week

The FANUC pack labels **A Energy** as the primary commercial offer. That is the **platform** wedge (bill is measurable). It is the **wrong lead for this meeting**, because kWh is still zero.

| Outcome | Client question | Role at LNM now |
|---|---|---|
| **C Real-time action** | Who needs to do something, right now? | **What they can feel today.** Execution layer for A and B. Not a third product. |
| **B Equipment intelligence** | Which machines are starting to behave abnormally? | **Proof from the Gantt today.** Inspect / cluster / trend. Not RUL. |
| **A Energy intelligence** | Where is LNM losing ₹ in electricity? | **Finance story.** Timing (coincidence, induction × CNC) is honest **now**. Rupee quantum waits for power module, incomer, or bill. |
| **D Plant context** | Does this action matter to production? | **Shared context.** Product and cell are already on FANUC. Due date is an ERP join later. Not MES. |

A live card always uses at least two. Example that *is* the product:

> **CNC_14_S2** · product `1774*P/M` · repeated clamp / micro-stop cluster · setter on this shift · check fixture · 10 minutes · machine returns to OPERATE → closed.

That is B + C + D. If STOP kWh is non-zero, A sits on the same card.

Map to platform (ADR-026): A = Industry Energy Management. B = Asset Health Intelligence. C = assign / verify (how A and B close). D = shared context. Do **not** sell availability / OEE as a third pillar.

---

## 3. Comments on the FANUC pack (keep, tighten, do not dump)

**Keep.** Four outcomes, not twenty capabilities. Honesty on ready vs FANUC-config vs plant-system. Worked card. Demo shortlist of eight items that need no new plant access. ERP used in four D places only. Compression vs notification budget. Never “turn the furnace off.” Never autowrite FOCAS.

**Tighten for the room.**

1. **Lead C, prove with B, sell A when kWh lands.** Do not open with “where is LNM losing ₹” while every power bucket is 0.
2. **Drop “read-only” as the identity line.** Say operators stay in control; recommendation, not automatic furnace or CNC control. Optional human-approved desk execution is platform language, not a LNM week-1 promise. No FOCAS writes.
3. **One card in the room, not 100.** `catalogue-client.md` is the show file. `rx-catalogue.json` is ammunition.
4. **Do not quote 26,750 events / day** as measured. One-machine 24 h × 31 is `[~]`.
5. **Clamp vs lube owner-split is still blocked (G1).** Talk the *shape* (cluster → setter vs maintenance). Do not claim we already route `2019` / `2029` from the API.
6. **Recover-now / lost minutes** are production-efficiency co-benefits on the same card, not a new SKU. Finding.category enum still lacks an honest availability member (`abnormal_duty` is nearest). Do not wait on that PR to tell the story.
7. **IT’s job becomes exception reviewer**, not daily CSV ETL. That sentence is as important as any Rx.

**First two asks (not ten):** alarm columns in the API so clamp vs lube go to the right person; turn on the FANUC power module they already paid for (A26). Owner map for a 3–5 machine pilot cell is the third if the room is warm.

---

## 4. Delta vs the current leave-behind

Live brief: [`../../demo-decks/clients/lnm-auto-faridabad-technical/`](../../demo-decks/clients/lnm-auto-faridabad-technical/). It is still the **anonymous forge-HT** spine with LNM chrome.

| Current slide | Problem for this meeting |
|---|---|
| H1 *Act on energy opportunities before the window closes* | Energy-first. The client’s job is execution from data they already bought. |
| Lead *meters, SCADA, DHBVN bills* | The evidence we have is **MT-LINKi**, not a locked incomer/bill. |
| Sample Rx *Press Line 1 vs SQF preheat* · *Inspect Compressor 2* | Generic. We have `CNC_14_S2`, `1774*P/M`, cell split, induction on FANUC, micro-stop volume. |
| Gap list *Incomer meters and EMS / SCADA* | Overclaims electrical digital. Field note was weak energy monitoring. |
| Equipment *compressors, SQF / quench, press startups* | Wrong asset class for the collector we actually read. |
| Footer *Read-only on meters and SCADA* | Fights the execution story. |

Retarget later (not this file): title and gap to last-mile action; load Rx to induction × CNC stagger (timing, no fake ₹); equipment Rx to Gantt micro-stop / cell-partner idle (clamp cluster as *shape* until G1); floor card to CNC_14_S2; integration names FANUC + ForgeLink, not a second screen.

**Do not demo:** vibration PdM, OEE%, plan-vs-actual, camera as brain, furnace off, guaranteed ₹, FOCAS write, 336 WhatsApps.

---

## 5. Room sequence (when the deck is retargeted)

1. They already collect. The last mile to the setter is missing.
2. Worked card (B + C + D). One cluster, one message, close on OPERATE.
3. What is true **today** from their collector (demo shortlist 1–8 in `gaps-and-asks.md`).
4. Energy: stagger / overlap **timing** now; ₹ after A26 or a bill.
5. Two asks. Working session. No commitment required.

People names stay off slides.
