# VolTwin (Wistwin) vs Stamped — plain English

## In one sentence
VolTwin is Wistwin’s energy module for Indian factories: it attributes every kWh to machines/lines, applies DISCOM tariffs, alerts on peak demand, and produces ISO 50001 / PAT / BRSR-ready energy reports — especially for steel, cement, aluminum, and listed companies.

## What they actually do (no jargon)
- Connect DISCOM, captive, solar, and diesel meters; tag kWh to machine / line / shift / product via their asset register (**AssetTwin**).
- Show live **Specific Energy Consumption (SEC)** — e.g. kWh per tonne of product (kWh/MT) — so the CFO can see where the bill goes.
- Know tariff structures for **nine named Indian DISCOMs** (slabs, ToD, contract demand, Power Factor incentives, fuel adjustment charges), updated quarterly on their side.
- Alert before **Maximum Demand (MD)** — the peak 15‑minute spike that can trigger penalties — and recommend load shifting (they say “automatically” in places; public detail on real plant writeback is thin).
- Track **ISO 50001 Energy Performance Indicators (EnPIs)** — baselines, targets, trends for energy audits.
- For **Perform, Achieve, Trade (PAT)** plants: live SEC vs BEE target and an **ESCert** (energy certificate) long/short/neutral position for trading readiness.
- Feed **BRSR Core** (SEBI listed-company ESG disclosure) energy and Scope 1/2 numbers into sibling **ImpacTwin** (XML/PDF for portal upload).
- Meter-agnostic software; split-core current sensors for old meters; not a meter manufacturer. Hyderabad / India brownfield focus.

## What Stamped already does in the same area
- We already do DISCOM ToD / MD / PF Findings and ₹ Prescriptions from tariff tables + HT bill ingest.
- We already recommend load stagger / peak shed / contract demand rightsizing as assigned work — and we are explicit that silent OT write is **not** what we ship.
- We already have SEC / EnPI engines and soft-join to production records (when production data exists).
- We already connect Modbus/MQTT-class meters without owning the hardware.
- We already treat PAT / ISO / BRSR as **evidence we help the customer export**, not as “we file / we trade certificates for you.”
- We differentiate on **owner + effort + ₹ + evidence flip + WhatsApp closure + ops-cleared ledger**, not twin dashboards alone.

## What they can do that we cannot (the real gaps)

### Live kWh/MT as the hero daily desk object
- **What it is:** Per furnace/kiln/line SEC on the main screen, with shift and plant benchmarks.
- **Why a plant would care:** Energy-intensive Designated Consumers live and die by tonnes vs kWh; “where did the bill go?” is a board question.
- **Software, hardware, or both?** Software (needs production tonnes + meter data).
- **Can Stamped add this?** Yes software — we already have SEC/EnPI and production soft-join; productize the UX.
- **Should we?** Yes — Priority for energy-intensive ICP; never invent ₹ from SEC alone.

### BRSR Core auto XML/PDF filing pack (via ImpacTwin)
- **What it is:** Auto-build SEBI BRSR Core energy/GHG disclosures from live meters for top-1000 listed companies.
- **Why a plant would care:** Listed cos have disclosure deadlines; spreadsheet reconstruction fails audits.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** Yes software for **Scope 2 / energy evidence export**; No for becoming a full ESG filing platform.
- **Should we?** Build evidence packs; do not become ImpacTwin.

### PAT live target + ESCert long/short position + M&V audit packs
- **What it is:** Dashboard of SEC vs BEE PAT-cycle target and whether you are generating or burning tradable certificates; audit export packs.
- **Why a plant would care:** Missing PAT targets costs real money in certificate purchases.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** Yes software for evidence / M&V export; park certificate-trading desk UI.
- **Should we?** Yes for evidence packs on DC deals; no ESCert exchange product.

### ISO 50001 EnPI as a polished compliance product
- **What it is:** Baseline / target / trend packs ready for management review and certification audits.
- **Why a plant would care:** Certification and customer audits ask for EnPIs, not just charts.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** Yes software — deepen exports; we do not certify plants.
- **Should we?** Yes as evidence packs next to Rx.

### “Automatic” load-shift / battery dispatch logic
- **What it is:** Wording that implies loads or batteries move themselves off-peak.
- **Why a plant would care:** Same as wanting MD/ToD relief without manual hustle.
- **Software, hardware, or both?** Unclear publicly (software ± write).
- **Can Stamped add this?** Unclear until validated. If recommend-only → we largely cover it. If autonomous BESS → No (strategic).
- **Should we?** Validate in deals; default to recommend + partner EMS.

### Split-core CT retrofit programme
- **What it is:** Clamp sensors so plants without digital meters can still feed data.
- **Why a plant would care:** Brownfield India still has dumb meters.
- **Software, hardware, or both?** Hardware / services.
- **Can Stamped add this?** Yes with partners — we stay meter-agnostic ingest.
- **Should we?** Partner ESCOs / CT installers; do not OEM sensors.

### Deep ERP + MES stacking for disclosure
- **What it is:** Pull SAP/Oracle/Dynamics/Tally (and MES/LIMS) into ESG and energy intensity joins.
- **Why a plant would care:** BRSR and SEC need finance and production truth, not only meters.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** Yes software for soft-joins that serve energy Rx — without becoming a MES.
- **Should we?** Deepen soft-joins where deals need them; never a third MES pillar.

## Bottom line for Stamped
VolTwin is the **closest peer threat** among the five on the India manufacturing energy + compliance desk — especially Designated Consumers and listed buyers. They win when the RFP is “live kWh/MT + BRSR XML + PAT position.” We win when the buyer wants assigned ₹ Prescriptions, equipment+energy Findings, WhatsApp closure, and honest ops/bill verification. Copy their **evidence packaging** (SEC hero views, PAT/ISO/BRSR exports); do not copy ESG-as-platform, ESCert trading, or CT OEM. Never quote their 14% / 18% / ₹2.4 Cr marketing as our proof.
