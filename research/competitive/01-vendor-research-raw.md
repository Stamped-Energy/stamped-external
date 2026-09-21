# Vendor research dump — energy / industrial competitors

**Purpose:** Factual, source-cited capability notes for gap analysis. Claims below are vendor-stated only; outcomes (e.g. % savings) are marketing claims, not independently verified here.  
**Research date:** 2026-09-21 (Asia/Calcutta)  
**Method:** WebSearch + WebFetch of vendor product pages, datasheets/brochures, India-market pages. Preference for primary sources.

---

## 1. EnerCog (Enercog)

### Official name / positioning
- **Company / brand:** Enercog / EnerCog (Pune, India)
- **Core products:** BESS EMS; industrial Energy Management System (EMS); Synapse industrial edge controllers; Cortex (AI / tariff scheduler / cloud analytics); Clarity UI; Solar SCADA/RMS; Solar Power Plant Controller (PPC); PM-KUSUM RMS; zero-export & DG-PV sync
- **Positioning:** India-focused grid-compliant renewable + C&I energy software/hardware for solar, BESS, hybrid plants and HT industrial consumers — ToD/MD optimisation with autonomous BESS dispatch under DISCOM tariff structures

### URLs used
- https://enercog.com/enercog-bess-ems/
- https://enercog.com/solutions/ems/
- https://enercog.com/solutions/industrial/
- https://enercog.com/solutions/

### Capability bullets (vendor claims)
- **BESS EMS supervisory control** with six configurable modes: (1) peak shaving / demand limiting, (2) ToD arbitrage & scheduling, (3) solar-plus-storage grid firming / ramp limiting, (4) reactive power & POI voltage support, (5) reserve capacity / resilience / islanding support, (6) multi-asset & cluster dispatch allocation
- **MD / demand charge management:** 1-second demand monitoring; predictive peak shaving via load-pattern learning; auto BESS discharge near MD setpoint; claimed MD charge reductions of ~20–40% (well-sized systems) / 20–35% first billing cycle (marketing)
- **ToD / DISCOM tariff engine:** Cortex scheduler with DISCOM-specific windows; named coverage includes MSEDCL, BESCOM, TANGEDCO, GUVNL, KSEB and “all major DISCOMs”; off-peak charge / peak discharge; weekday/weekend calendars; weather-adjusted solar; multi-day tariff calendars
- **Autonomy / writeback:** Issues autonomous charge/discharge and active/reactive setpoints to PCS; coordinates with Solar PPC; does **not** replace BMS/PCS safety — supervisory layer only; local execution on Synapse (cloud not required for core dispatch); fallback on stale telemetry / comms loss
- **Solar–BESS–DG–grid coordination:** Solar surplus → BESS; MD/ToD discharge; DG reverse-power protection; zero-export throttling; DG-PV sync with Woodward / Deep Sea / ComAp / DEIF controllers
- **Protocols:** Modbus TCP/RTU, SunSpec, IEC 60870-5-104, DNP3, IEC 61850 (utility tier), CAN 2.0B / CANopen for BMS, Ethernet/IP, REST API
- **Hardware:** Synapse DIN-rail edge RTU (C&I / &lt;~25 MW); utility 1+1 rackmount server clusters (&gt;~50 MW / 100 MWh); India-built/assembled in Pune for DCR / SECI / NTPC / DISCOM tenders
- **Other pillars:** Utility solar SCADA/RMS; sub-second Solar PPC (P/Q/PF/V at PCC); PM-KUSUM Component A & C RMS; Clarity UI reporting (incl. WhatsApp/email savings reports)

### Software / hardware / services mix
- **Software:** BESS EMS / EMS runtime, Cortex AI/cloud, Clarity UI
- **Hardware:** Synapse edge controllers; optional rackmount utility servers; panel build
- **Services:** SLD scoping, FAT/SAT, SLDC telemetry handshake, commissioning, operator training, long-term support

### Geography / focus
- Strong **India** focus: DISCOM ToD/MD billing, CEA/SLDC grid codes, state DISCOM interconnection, PM-KUSUM, domestic content for PSU tenders
- C&I manufacturing, commercial RE, utility solar + BESS

### Compliance claims
- CEA Technical Standards / state grid connectivity; IEC 60870-5-104 / IEC 61850 for SLDC; ABT metering at POI (visibility layer)
- **Not primarily positioned** as PAT / ISO 50001 / BRSR reporting product (no strong public PAT/BRSR claims found on fetched pages)

### Autonomy / control notes
- Explicit **closed-loop / autonomous** BESS and hybrid dispatch with PCS setpoint write; local deterministic fallback
- Grid-forming / synthetic inertia / sub-second primary frequency response called out as **project-specific** (needs PCS capability + FAT/SAT gates) — not baseline claim

### Confidence
- **Strong** — detailed official product architecture, modes, protocols, hardware tiers, and India tariff positioning on vendor site

---

## 2. VolTwin™ (Wistwin® / Group VB)

### Official name / positioning
- **Product:** VolTwin™ — energy intelligence module of the **Wistwin®** digital twin platform
- **Company context:** Wistwin / Group VB (Hyderabad HQ stated on site)
- **Positioning:** Live kWh/MT (or GJ/T) attribution, DISCOM-aware tariff intelligence, peak-demand (MD) alerts, ISO 50001 EnPI, BRSR Core–ready energy disclosures for Indian manufacturers — especially energy-intensive steel/cement/aluminum

### URLs used
- https://wistwin.in/platform/voltwin.html
- https://wistwin.in/industries/steel-cement.html
- https://wistwin.in/compliance/brsr-core.html
- https://wistwin.in/platform/impactwin.html (ImpacTwin companion for BRSR)

### Capability bullets (vendor claims)
- Connects DISCOM, captive, solar, diesel meters; attributes kWh to machine / line / shift / product via AssetTwin
- **Live SEC:** kWh/MT, GJ/T per furnace/kiln/line; shift and plant benchmarking
- **DISCOM tariff intelligence** for 9 named DISCOMs: MSEDCL, TANGEDCO, GUVNL/UGVCL, BESCOM, TSSPDCL, UPPCL, MPPKVVCL, PSPCL, HVPNL — slabs, ToD, contract demand, PF incentives, FAC/CAPF (updated quarterly per site)
- **Peak demand / MD alerts:** rolling 15-min kVA tracking; pre-emptive alarms before contract MD breach; recommends load-shifting (claimed ~18% peak demand reduction in marketing benchmarks)
- **ToD optimisation:** peak/off-peak/night awareness; “shift non-critical loads to off-peak windows automatically” (wording implies automation — depth of closed-loop writeback not detailed as PCS/BESS control suite)
- Power factor monitoring; grid + captive + solar mix recommendations; “battery storage dispatch logic where applicable” (high-level claim)
- **ISO 50001 EnPI** baselines, targets, trends
- **BRSR Core** energy intensity / renewable vs non-renewable / GHG Scope 1–2 (Scope 3 planned) via ImpacTwin; SEBI BRSR Core XML/PDF
- **PAT:** live SEC vs BEE PAT-cycle target; ESCert long/short/neutral position; M&V audit-readiness; audit export / BEE compliance packs
- Anomaly detection on consumption spikes; PLI claim energy-intensity documentation support
- Integrations: Modbus/MQTT meters (Schneider, Siemens, ABB, L&T, Secure, Genus, HPL, etc.); split-core CTs for non-digital meters; ERP (SAP ECC/S4, Oracle, Dynamics, Tally) and SCADA/MES/LIMS for ImpacTwin stacking
- Data residency: AWS Mumbai default; on-prem available; DPDP-compliant; ISO 27001 “in progress (Q3 2026)” per site

### Software / hardware / services mix
- **Software platform** (digital twin modules: AssetTwin, VolTwin, ImpacTwin, TrusTwin, PredicTwin, AviraTwin, SmarTwin)
- **Hardware:** primarily meter-agnostic / CT retrofit — not a meter OEM
- **Services:** multi-plant hub-and-spoke rollout; compliance/ESG aggregation

### Geography / focus
- **India manufacturing**, especially steel / cement / aluminum Designated Consumers; listed-company BRSR; EU CBAM export evidence (via ImpacTwin)

### Compliance claims
- ISO 50001 EnPI; BEE PAT (SEC / ESCert); SEBI BRSR Core; GRI/CDP/SBTi-aligned carbon accounting language; CPCB CEMS / CBAM via sibling modules

### Autonomy / control notes
- Strong on **monitor / attribute / alert / recommend / report**
- Mentions automatic load-shifting recommendations and “battery storage dispatch logic where applicable” — **public detail thin** vs EnerCog/ABB-style PCS setpoint architecture; no clear public claim of BESS EMS / writeback stack comparable to EnerCog

### Confidence
- **Strong** for energy intelligence, kWh/MT, MD alerts, DISCOM list, ISO 50001, BRSR/PAT positioning  
- **Thin** on closed-loop plant control / BESS autonomy depth

---

## 3. Tech OVN (Tech OVN Pvt Ltd)

### Official name / positioning
- **Company:** Tech OVN Pvt Ltd (Gurugram / Delhi–Jaipur Highway, Haryana, India)
- **Hardware:** Titan family — Titan 3-phase DIN-rail Class 0.5S smart meter; Titan Audit (clamp-on portable logger); roadmap: Titan PQ, BTU, Asset, EV, etc.
- **Software:** **Tech OVN Energy Intelligence Platform (EIP)** — cloud multi-site EMS / monitoring SaaS
- **Positioning:** India-manufactured meters + native MQTT cloud EMS for factories, buildings, data centres, hospitals — BEE PAT / ISO 50001 / BRSR-ready measurement and reporting

### URLs used
- https://www.techovn.com/energy-management-system
- https://www.techovn.com/energy-management-system/factory
- https://www.techovn.com/products/titan
- https://www.techovn.com/products/titan-audit
- https://www.techovn.com/solutions/energy-audit

### Capability bullets (vendor claims)
- **Titan meter:** Class 0.5S active (IEC 62053-22), Class 1 reactive; V/I/P/PF/f/kWh/kVARh/kVAh; harmonics to 31st; MD (block/sliding); up to 8 TOD zones; dual-source grid/DG; on-device CO₂ with configurable emission factors
- **Connectivity:** WiFi + Ethernet + RS485; Modbus RTU/TCP + MQTT simultaneous; HTTP/HTTPS push; no gateway required to EIP
- **Titan Audit:** split-core clamp-on; rapid deploy; PDF audit reports from phone app; BEE PAT / ISO 50001 / ASHRAE Level 2–3 audit use cases; leave-in-place for ongoing M&V
- **EIP EMS:** real-time multi-site dashboards; submetering by line/floor/tenant/asset; TOU tariff & demand cost allocation; alerts (demand, PF, voltage, consumption); AI anomaly / baseline analytics; mobile app
- **Factory EMS:** per-line / per-shift / per-machine attribution; automatic SEC & EnPI vs baseline; compressed air / HVAC / motor waste visibility
- **Compliance exports:** ISO 50001 EnMS-ready; BEE PAT; BRSR / ESG exports (platform FAQ/specs)
- **Edge features on meter:** TOU registers, MD monitoring, threshold alerts; “autonomous alerts and power disconnection when thresholds are exceeded” (relay control mentioned in integration guide context)
- Runs **alongside** BMS/SCADA (does not replace them); cloud-only SaaS for EIP
- Geographic reach: manufactured in India; deployments claimed across India, Middle East, Europe, Southeast Asia, Africa

### Software / hardware / services mix
- **Hardware-first OEM** (meters designed/manufactured in-house) + **cloud SaaS** EIP
- Optional white-label / OEM meter programme
- Audit → permanent monitoring path for ESCOs / BEE-empanelled auditors

### Geography / focus
- India C&I + buildings + multi-country export of meters/platform; Indian ToD/DG/grid operating patterns called out

### Compliance claims
- BEE PAT measurement requirements (accuracy, TOU, harmonics) — **measurement/M&V support**, not a full ESCert trading desk
- ISO 50001 EnPI / M&V / audit-ready reports
- BRSR / ESG export claims on EMS specs page
- Meter standards: IEC 62052-11, 62053-21/22, 61010, 61000

### Autonomy / control notes
- Primarily **metering + monitoring + alerting + reporting**
- Limited autonomy: threshold alerts; relay/disconnection claim on meter; **no public BESS EMS / plant APC / ToD arbitrage closed-loop stack** comparable to EnerCog or ABB OPTIMAX
- Explicitly positioned as EMS measurement layer next to BMS/SCADA, not process control replacement

### Confidence
- **Strong** for meter specs, MQTT stack, EIP monitoring/reporting, PAT/ISO audit tooling  
- **Moderate** for depth of BRSR (listed as export capability; ImpacTwin-level ESG workflow not evidenced)  
- **Thin** on plant energy optimisation / writeback autonomy

---

## 4. LTTS EnergiSensEI (L&T Technology Services)

### Official name confirmation
- **Confirmed product name on LTTS site:** **EnergiSensEI**  
  - Primary: https://www.ltts.com/solutions/EnergiSensEI  
  - Brochure slug uses lowercase: https://www.ltts.com/brochure/energisensei (“Energy Savings You Can Trust”) — still titles the product **EnergiSensEI**
- **Alternatives checked:**
  - “EnergiSense” / “Energi Sense” — appear in informal/third-party paraphrases; **not** the primary LTTS product URL title
  - Related but **distinct** LTTS offering: **Energy and Sustainability Manager / utility monitoring system** (https://www.ltts.com/solutions/utility-monitoring-system) — WAGES-style utility dashboards, ISO 50001/50000, GHG Scope 1–3, SBTi language
  - Broader LTTS sustainability / Engineering Intelligence portfolio materials also exist; EnergiSensEI is the named energy & sustainability **platform** on the Solutions catalog

### Positioning
- Engineering-physics–verified AI energy & sustainability platform for industrial plants: verify meter/sensor data against physics **before** AI learns/recommends; visibility across energy, water, emissions, ESG

### URLs used
- https://www.ltts.com/solutions/EnergiSensEI
- https://www.ltts.com/brochure/energisensei
- https://www.ltts.com/solutions/utility-monitoring-system (related sibling)
- https://www.ltts.com/solutions (catalog listing)

### Capability bullets (vendor claims)
- Four-stage journey: **Assess → Build → Operate → Sustain**
- Pipeline: **Verify → Learn → Recommend → Act** (Act = supports decision; “your plant manager and team make the call” — human-in-the-loop emphasis)
- **Five agents:** Optimizer (live waste flags), Trends (demand forecast / early problems), Insights (plain-language Q&A), Reports (audit-ready D/W/M), Dashboard (exec/shop-floor, no developer)
- Use cases: compressed air leak detection; HVAC/thermal **set-point tuning** recommendations; motors/rotating equipment diagnosis; boilers & steam loss; multi-site demand forecast / loss flags; ESG & compliance
- **ISO 50001** one-click / automated cycles; emissions tracking; up to ~70% reporting effort cut (claim)
- Works with **any meter/vendor**; integrates SAP, Power BI, SCADA/IoT; edge or cloud
- Marketing scale claims: 5–15% energy & water reduction; payback ~&lt;3.5–4 years; deployments referenced as 50+ sites live / 20+ clients / also “1000+ sites” language in places (treat as vendor marketing; numbers inconsistent across page sections)
- Case vignettes on page: upstream O&G, global CPG/FMCG, paint manufacturer, large EPC ESG consolidation, green financing enablement

### Software / hardware / services mix
- **Software platform + engineering services** (metering assessment, OT integration, managed services / operate)
- **Not a meter OEM** — meter-agnostic; consulting/build/operate under one roof
- No public claim of shipping Synapse-like edge RTU as a branded product line (edge runtime mentioned)

### Geography / focus
- Global industrial / manufacturing / process / utilities clients (LTTS global ER&D positioning); not DISCOM-ToD/BESS-India-specific in public EnergiSensEI materials

### Compliance claims
- ISO 50001 automation; emissions / ESG reporting; GRI-compliant reporting mentioned in case language
- Sibling utility-monitoring page: ISO 50000/50001, GHG Scope 1–3, SBTi, water management PDCA
- **No strong public India PAT / BRSR Core / DISCOM ToD** claims on EnergiSensEI pages fetched

### Autonomy / control notes
- AI **recommends**; HVAC “tunes set points to real conditions” is claimed as what the product does in use-case cards — but Act stage states plant team makes the call
- **Not clearly marketed** as autonomous BESS EMS or closed-loop PCS writeback platform
- Stronger as verified analytics / optimisation advisory + reporting than as grid/BESS controller

### Confidence
- **Strong** on product name (EnergiSensEI), positioning (physics-verify-then-AI), ISO 50001/ESG reporting, integrations, agent list  
- **Moderate** on exact closed-loop control depth (recommend vs writeback ambiguous)  
- **Thin** on India DISCOM/PAT/BRSR-specific features

---

## 5. ABB Ability™ OPTIMAX®

### Official name / positioning
- **Full name:** ABB Ability™ OPTIMAX® — Energy Management and Optimization  
- **Suite / variants:** OPTIMAX for Industrial Sites (EMOS); Steam & Power; Oil & Gas; Petrochemicals & Refining; Virtual Power Plants (VPP); Water & Wastewater; Hydrogen; Data Centers; Cloud for Smart Charging; historically power-plant OPTIMAX APC tools (PowerCycle, Combustion Optimizer, BoilerMax / NMPC, etc.)
- **Positioning:** Scalable industrial energy management & optimisation — monitoring, AI forecasting, real-time and predictive (day-ahead / intraday) optimisation, open- or closed-loop setpoint distribution to controllable assets; pairs with ABB Ability™ Advanced Process Control (APC)

### URLs used
- https://new.abb.com/process-automation/energy-industries/digital/solutions/abb-ability-energy-management-and-optimization-optimax
- https://library.e.abb.com/public/69633d53b57e461bb0421d5afa42b400/7PAA014954_en_C_OPTIMAX%20for%20Industrial%20Sites.pdf (OPTIMAX for Industrial Sites brochure)
- https://new.abb.com/power-generation/solutions/power-plant-optimization/plant-optimization
- Supporting library/brochure hits for Combustion Optimizer / BoilerMax / energy-efficiency (historical OPTIMAX portfolio)

### Capability bullets (vendor claims)
- Orchestrate energy sources and loads in real time; up to **~10% energy cost reduction** (marketing)
- **AI-enabled forecasting** (incl. AutoML in v6.4 brochure language): load demand, generation, energy pricing; reduce day-ahead/intraday nomination errors
- **Step approach:** (1) monitoring & reporting → (2) real-time control & predictive optimisation
- **Real-time control:** optimal setpoints distributed directly to controllable systems; **open- or closed-loop**; demand response / ancillary / network services
- **Predictive optimisation:** intraday & day-ahead schedules from forecasts, loads, prices; peak shaving; stay within load bands; trading / flexibility support
- **Industrial Sites EMOS:** multi-asset coordination (generation, storage, consumption, EV charging, renewables); minimise peaks; maximise self-generation; market participation
- **Steam & Power:** boilers, turbines, steam networks; MPC; automated power import/export vs price; claimed ~5% steam / fuel savings class benefits on niche pages
- **VPP:** aggregate DERs; automatic asset dispatch; ancillary services; schedule disaggregation; trading decision support
- **ISO 50001-compliant** monitoring/reporting; PDF/Excel; claimed up to ~50% reporting time reduction
- Deployment: **SaaS, cloud, edge, on-prem, hybrid**; Kubernetes-based; works with APC
- Example: Busch-Jaeger Lüdenscheid Mission to Zero — OPTIMAX coordinating PV, **BESS (200 kW / 275 kWh)**, EV charging, largely autonomous energy flow
- Broader suite history: APC/MPC (Combustion Optimizer, BoilerMax NMPC boiler start-up), PowerCycle simulation, lifecycle/performance tools — plant optimisation heritage from power gen

### Software / hardware / services mix
- **Industrial software** (OPTIMAX + APC) within ABB Ability ecosystem
- Integrates with ABB and third-party plant/automation hardware (PMS, PCS, chargers, etc.) — manufacturer-independent energy management claimed for Industrial Sites
- Global engineering/services footprint; 200+ installations / 5 continents claimed in Industrial Sites brochure

### Geography / focus
- **Global** industrial, utility, oil & gas, chemicals, water, hydrogen, data centres, e-mobility — not India-DISCOM-specific in primary pages
- Deep process/plant energy & market optimisation vs India HT tariff niche products

### Compliance claims
- ISO 50001 reporting/compliance support; emissions reduction / sustainability frameworks; market/regulatory nomination and emissions reporting (sector-dependent)

### Autonomy / control notes
- Explicit **closed-loop** setpoint write to controllable assets; real-time EMS regulation of generation/storage/consumption
- Combined with APC/MPC for process variables
- VPP automatic dispatch
- Strongest public **autonomy / writeback** story among the five for plant-scale energy optimisation (alongside EnerCog for India BESS/PPC)

### Confidence
- **Strong** — official product family pages + Industrial Sites PDF with clear monitoring → closed-loop optimisation claims  
- Note: OPTIMAX is a **broad suite**; feature set varies by vertical package (Industrial Sites vs Steam & Power vs VPP). India DISCOM ToD/MD-specific packaging not prominent on fetched pages.

---

## Deepening pass 2026-09-22

Additional primary-source fetches after the 2026-09-21 dump. Existing sections above are unchanged. Marketing ₹/% savings remain **vendor claims**, not verified.

### 1. EnerCog — deepening

**New / reconfirmed URLs**
- https://enercog.com/solutions/industrial/ (HT bill structure + four-asset stack)
- https://enercog.com/products/synapse/ (RTU specs, SLDC protocols, 3-month buffer)
- https://enercog.com/enercog-bess-ems/
- https://enercog.com/bess-integrated-power-plant-control-under-msedcl-and-guvnl-tod-tariffs-algorithmic-co-optimization-for-indian-ci-solar-assets/

**Buyer / who they sell to (vendor language)**
- HT / LT industrial and commercial facilities in India that already have or are buying **solar + BESS (+ often DG)** and want the electricity bill’s three levers attacked together: energy (kWh), Maximum Demand (MD), and Time-of-Day (ToD).
- Also EPCs / RE developers needing Solar PPC, SLDC telemetry, PM-KUSUM RMS — different buyer than a plant “prescription desk.”

**What they control vs recommend**
- **Control (closed-loop):** Cortex/Synapse issue autonomous charge/discharge and active/reactive setpoints to PCS/inverters; Solar PPC at Point of Common Coupling (PCC); DG-PV sync (Woodward / Deep Sea / ComAp / DEIF class); zero-export throttling. Local Synapse keeps dispatching when cloud is down.
- **Recommend / report:** Clarity UI live cost dashboard; automated WhatsApp/email monthly savings reports. Pre-deployment savings *model* using customer tariff + load (still a sales tool, not independent M&V).

**Concrete feature deltas vs prior dump**
- Industrial page frames MD as typically **20–35% of the HT bill** and ToD peak windows typically **6–10 AM and 6–10 PM** in named states (MERC/KERC/RERC/GERC/TNERC/APERC) — vendor education copy.
- Four-asset stack explicit: **Solar + BESS + DG + Grid** coordinated at 1-second resolution.
- Synapse hardware: DIN-rail ARM edge; protocols IEC 60870-5-101/104, DNP3, IEC 61850, Modbus, CAN, SunSpec; IEC 61131-3 logic; **up to ~3 months** local buffer for MNRE/PM-KUSUM-class retention; FOTA; India-built/assembled Pune for DCR tenders.
- Blog claim: from **1 Apr 2026**, MSEDCL requires new rooftop/captive/open-access solar **>100 kW** to integrate BESS ≥50% of solar kW with ≥2-hour discharge — **vendor regulatory claim; verify with tariff order before product use**.
- Automatic DISCOM tariff-order push into EMS configs claimed (no manual reconfig) — **software claim, confidence Strong on existence of claim, Moderate on coverage of “all major DISCOMs.”**

**India vs global:** India-first (DISCOM ToD/MD, CEA/SLDC, PM-KUSUM). Not a global APC brand.

**Confidence:** **Strong** on BESS EMS autonomy + Synapse specs + India HT positioning. Treat all ₹ lakh savings as marketing.

---

### 2. VolTwin / Wistwin — deepening

**New / reconfirmed URLs**
- https://wistwin.in/platform/voltwin.html
- https://wistwin.in/industries/steel-cement.html
- https://wistwin.in/platform/ (five layers / ten modules)
- https://wistwin.in/compliance/brsr-core.html
- https://wistwin.in/platform/impactwin.html

**Buyer / who they sell to**
- Indian manufacturers — especially **steel / cement / aluminum Designated Consumers** and **SEBI top-1000 listed** plants needing BRSR Core.
- Personas called out: EHS Head, CFO, Sustainability Head (not primarily the electrical head’s WhatsApp Rx desk).
- Brownfield India positioning vs Western IIoT platforms; Hyderabad HQ (Group VB).

**What they control vs recommend**
- **Strong recommend / attribute / report:** live kWh/MT (or GJ/T), DISCOM tariff intelligence, MD alerts, EnPI, PAT SEC vs target, BRSR XML/PDF via ImpacTwin.
- **Ambiguous automation:** “Shift non-critical loads to off-peak windows automatically”; “battery storage dispatch logic where applicable” — **no public PCS/BESS EMS architecture comparable to EnerCog**. Treat as recommend-first until validated.
- **Not** a meter OEM; split-core CT retrofit for non-digital meters; AssetTwin required for per-machine attribution.

**Concrete feature deltas**
- Nine DISCOMs named unchanged; quarterly tariff updates by Wistwin team.
- Hub-and-spoke multi-plant; AWS Mumbai default; DPDP; ISO 27001 “in progress (Q3 2026)” per site.
- PAT: live ESCert **long / short / neutral** position + M&V audit-readiness (steel-cement page).
- ImpacTwin: 9 BRSR Core indicators + 67 sub-questions; Scope 3 expansion language for FY25-26; ERP pulls SAP/Oracle/Dynamics/Tally.
- Platform is a **digital twin suite** (AssetTwin, VolTwin, ImpacTwin, SmarTwin/OEE, …) — energy is one module, not the whole company.

**India vs global:** India manufacturing + Indian regulators (PAT, BRSR, DISCOM, CBAM export evidence). Not global EMS.

**Confidence:** **Strong** on kWh/MT, DISCOM list, PAT/BRSR productization. **Thin** on closed-loop control depth. Marketing benchmarks (14% kWh/MT, 18% peak, ₹2.4 Cr) = claims only.

---

### 3. Tech OVN — deepening

**New / reconfirmed URLs**
- https://www.techovn.com/energy-management-system/factory
- https://www.techovn.com/energy-management-system
- https://www.techovn.com/products/titan
- https://www.techovn.com/industries/factories

**Buyer / who they sell to**
- Factories needing **sub-metering + cloud charts** (cement, textile, pharma, food, auto); also buildings, data centres, hospitals, hotels — broader than HT manufacturing ICP.
- BEE-empanelled auditors / ESCOs (Titan Audit → leave-in-place path).
- Facility managers, energy heads, ESG teams who buy **meter + dashboard as one SKU**.

**What they control vs recommend**
- **Measure + monitor + alert + report.** EIP is cloud SaaS (cloud-only; no on-prem claim on fetched EMS FAQ).
- Limited on-meter autonomy: threshold alerts; “autonomous alerts and power disconnection when thresholds are exceeded” (relay) — **meter relay, not plant APC**.
- Explicitly **alongside** BMS/SCADA, not a replacement.
- Titan works **standalone** to any BMS/SCADA via Modbus/MQTT — EIP optional.
- Platform adds: multi-site, BESS **sizing/ROI** (sizing tool language — not BESS EMS dispatch), baselines, condition monitoring dashboards.

**Concrete feature deltas**
- Titan Class 0.5S; harmonics to 31st; up to 8 TOD zones; dual-source grid/DG; on-device CO₂; WiFi+Ethernet+RS485; MQTT+Modbus simultaneous; no gateway to EIP.
- Factory path: production totals via **manual entry or CSV** for SEC — “No SCADA/MES integration required to get SEC working.”
- Roadmap family: Titan PQ, Asset, BTU, EV, Pump, etc. (many “Coming Soon”).
- White-label / OEM meter programme for export.
- India operating patterns called out (DG/grid, ToD, PAT) but also multi-country ship from Delhi NCR.

**India vs global:** India-manufactured meters; India PAT/ToD language; export Middle East / Europe / SE Asia / Africa.

**Confidence:** **Strong** on meter + EIP monitoring/reporting. **Moderate** on BRSR depth (export claim, not ImpacTwin-class workflow). **Thin** on plant optimisation / writeback.

---

### 4. LTTS EnergiSensEI — deepening

**New / reconfirmed URLs**
- https://www.ltts.com/solutions/EnergiSensEI
- https://www.ltts.com/brochure/energisensei
- https://www.ltts.com/EngineeringIntelligence (portfolio context; “EnergiSense” appears as short label in EI catalog — product page title remains **EnergiSensEI**)

**Buyer / who they sell to**
- Global industrial / process / manufacturing / utilities plants that want **ER&D + platform + managed operate** under one LTTS roof.
- Not sold as an India-DISCOM ToD/BESS controller on public pages.

**What they control vs recommend**
- Pipeline: **Verify → Learn → Recommend → Act** with explicit “your plant manager and team make the call.”
- Use-case cards say HVAC “tunes set points to real conditions” — **ambiguous** vs Act stage; treat writeback depth as **unclear** without deal validation.
- Five agents: Optimizer, Trends, Insights, Reports, Dashboard.
- Services journey: Assess → Build → Operate → Sustain (global managed-services team).

**Concrete feature deltas**
- Physics-verify-before-AI is the hero differentiator vs “black-box energy AI.”
- Meter-agnostic; SAP / Power BI / SCADA/IoT; edge or cloud.
- Strong ISO 50001 one-click + emissions / ESG reporting; up to ~70% reporting effort cut (claim).
- Site-count language inconsistent across page (20+ clients / 50+ sites / also “1000+ sites”) — **marketing inconsistency noted; do not treat as fact**.
- Public materials still **thin** on India PAT / BRSR Core / DISCOM ToD specifics.

**India vs global:** Global LTTS footprint; India presence via LTTS but product story is not DISCOM-first.

**Confidence:** **Strong** on name, Verify-first story, agents, ISO/ESG packaging, human-in-the-loop Act. **Moderate** on closed-loop depth. **Thin** on India tariff/PAT/BRSR.

---

### 5. ABB Ability™ OPTIMAX® — deepening

**New / reconfirmed URLs**
- https://new.abb.com/process-automation/energy-industries/digital/solutions/abb-ability-energy-management-and-optimization-optimax/optimax-for-industrial-sites
- https://new.abb.com/process-automation/energy-industries/digital/solutions/abb-ability-energy-management-and-optimization-optimax
- https://library.e.abb.com/public/69633d53b57e461bb0421d5afa42b400/7PAA014954_en_C_OPTIMAX%20for%20Industrial%20Sites.pdf
- https://new.abb.com/news/detail/133171/abb-introduces-saas-option-for-industrial-energy-optimization-software (OPTIMAX 7.0 SaaS / Kubernetes / APC 7.0 — news dated ~Mar 2026 in third-party coverage)

**Buyer / who they sell to**
- Global industrial sites, microgrids, smart cities needing **Energy Management and Optimization System (EMOS)** — monitoring then **control & optimisation**.
- Process industries pairing OPTIMAX with **Advanced Process Control (APC)** / MPC.
- Procurement comfort for majors needing SaaS / edge / on-prem / hybrid.

**What they control vs recommend**
- Step 1: Monitoring & Reporting (ISO 50001, one-click reports).
- Step 2: Control & Optimization — **open- or closed-loop** setpoint distribution to controllable assets; day-ahead / intraday schedules; real-time deviation compensation; market / demand-response participation.
- AI/AutoML forecasting of load, generation, prices as optimiser input.
- Strongest **autonomy / writeback** story among the five at plant EMOS scale (alongside EnerCog for India BESS/PPC niche).

**Concrete feature deltas**
- OPTIMAX **7.0** adds managed **SaaS** option; Kubernetes for edge/cloud/hybrid; tighter packaging with APC 7.0 (ABB news).
- Industrial Sites still claims up to ~10% energy cost reduction (marketing).
- India DISCOM ToD/MD packaging still **not prominent** on primary pages.

**India vs global:** Global. Not an India HT tariff niche product in public materials.

**Confidence:** **Strong** on closed-loop EMOS + forecasting + ISO reporting + deploy flexibility. Feature set varies by vertical package.

---

## Cross-vendor snapshot (for gap analysis)

| Dimension | EnerCog | VolTwin (Wistwin) | Tech OVN | LTTS EnergiSensEI | ABB OPTIMAX |
| --- | --- | --- | --- | --- | --- |
| India DISCOM ToD/MD | Core | Strong (alerts + tariff intel) | Monitoring/alerts | Thin public | Thin public (global markets) |
| kWh/MT / SEC | Thin | Core | SEC/EnPI via meters | Intensity/savings analytics | Energy flow opt (not kWh/MT-first) |
| BESS autonomy | Core closed-loop | Thin (“dispatch logic”) | Thin | Recommend-oriented | Strong closed-loop / examples |
| Meters hardware | Edge RTU (not tariff meter OEM) | Agnostic | Core OEM (Titan) | Agnostic | Agnostic / ABB ecosystem |
| PAT | Thin | Strong (live ESCert position) | Strong M&V/audit | Thin | Thin |
| ISO 50001 | Thin | Strong EnPI | Strong | Strong one-click | Strong reporting |
| BRSR | Thin | Strong (via ImpacTwin) | Export claim | ESG/emissions (global) | Sustainability/ISO focus |
| Plant APC/MPC | PPC/BESS EMS | Soft | No | AI recommend | Core (APC/MPC) |

---

## Source quality notes
- All capability bullets above are grounded in fetched vendor pages/PDFs dated access 2026-09-21.
- Savings percentages, pilot averages, and site counts are **vendor marketing** — retained as claims, not facts.
- Where autonomy vs recommendation is ambiguous (VolTwin load-shift “automatically”; LTTS HVAC set-point “tunes”), ambiguity is noted rather than inferred as full writeback.
