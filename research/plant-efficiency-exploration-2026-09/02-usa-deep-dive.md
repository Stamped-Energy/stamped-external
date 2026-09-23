# 02 — USA / North America — Industrial AI for Manufacturing Efficiency (Deep Dive)

**Status:** exploration — not a product lock  
**Promoted from:** agent enrichment draft 2026-09-24


**Prepared for:** Stamped Energy / Stamped Process strategy  
**Date:** 2026-09-24 (IST)  
**Scope:** Manufacturing and plant **efficiency** in the broad sense — throughput, OEE, yield, scrap, cycle time, labor productivity, programming/setup time, quality escape, maintenance-driven loss, and **co-benefit** utility intensity — **not** an energy-only market map.  
**Baseline expanded from:** `universal-repositary/external/research/competitive/industrial-ai-global-2026-09-22/Industrial_AI_Deep_Dive_USA.md` (deepened; not copied verbatim).  
**Method:** Company primary sites, press releases, SEC filings where public, and reputable trade press. Funding, revenue, plant counts, and ROI figures are **vendor-claimed** or **press-reported** unless tied to a filed public number; nothing is invented. Where unknown: *Not disclosed publicly*.

---

## 1. Why this document exists

North America is where industrial AI **GTM archetypes** are most visible: hyperscaler substrates, automation majors, data fabrics, outcome specialists (process margin, OEE, PdM), physical-AI narratives, and shop-floor execution layers. For Stamped’s **software-only** plant efficiency wedge (existing data → ranked actions → human freeze → optional writeback **without** selling new sensors or controls), the useful question is not “who raised the most?” but:

1. **Which KPI do they contractually own?** (OEE points, $/ton, yield %, programming hours, defect PPM, MTBF, margin/bbl — not “AI platform.”)
2. **Advisory vs closed-loop?** (Recommend → approve → write setpoints/DCS vs dashboard-only.)
3. **Hardware dependency?** (Can a plant with historians/MES/CSV-only still get value?)
4. **Who signs?** (Plant manager, process engineer, reliability, OT architect, CIO, PE sponsor.)
5. **What should Stamped steal vs avoid?** (Ontology patterns yes; CapEx robotics no.)

This draft catalogs **40+ named entities** with short dossiers aligned to those five questions.

---

## 2. Taxonomy — five layers (efficiency, not energy-only)

| Layer | Role in efficiency stack | Examples (this doc) |
|-------|--------------------------|---------------------|
| **L0 — Connect / contextualize** | Make OT data usable without owning outcomes | Litmus, HighByte, AWS SiteWise, Azure IoT |
| **L1 — Visibility / twin** | Production or asset model; often stops at analytics | Sight Machine, MachineMetrics, Guidewheel, Cognite, Palantir |
| **L2 — Engineer analytics** | Deep investigation; KPI ownership optional | Seeq, C3 apps, Honeywell Forge analytics |
| **L3 — Outcome AI (advisory)** | Prescribe setpoints, routes, maintenance, CAM | Fero, Basetwo, Green Factory AI, Landing AI, CloudNC |
| **L4 — Closed-loop control** | Write through DCS/APC/MES | Imubit, (optional writeback) Green Factory AI, Emerson hybrid |
| **L5 — Physical execution** | Robots, vision hardware, sensing pods | Bright Machines, Cognex, Elementary, Augury (sensors), BrightAI |

**Stamped target band:** L3 with a path to **selective** L4 writeback where the plant already has APC/DCS — **without** becoming L5.

---

## 3. Snapshot matrix (efficiency focus)

| Company | Primary efficiency KPI (claimed / implied) | Mode | H / S | Typical buyer | Stamped SW-only fit |
|---------|-----------------------------------------------|------|-------|---------------|---------------------|
| Fero Labs | Yield, quality variation, $/ton | Advisory → live recs | S | Process engineer | **Direct peer** — explainable prescribe |
| Imubit | Margin, NG/fuel, yield | **Closed-loop** | S | Controls / PE | Aspirational L4; India may stop at L3 |
| Basetwo | Batch cycle, spec, throughput | Advisory / AutoPilot path | S | Process dev | Hybrid-model reference |
| Green Factory AI | Chemicals/energy per ton, profit | Advisory → writeback | S | Mill engineer | Strong NA-EU process parallel |
| Sight Machine | OEE, throughput | Analytics → optimize | S | Ops / digital mfg | Data model patterns |
| MachineMetrics | OEE, cycle time | Analytics | H+S | Plant / CI leader | Connector + OEE, not PE AI |
| Guidewheel | Downtime, OEE | Analytics + AI tags | H+S | Plant manager | Non-invasive visibility |
| Jemba (TeepTrak) | OEE root cause, energy | Advisory | S (+ optional HW via TeepTrak) | Process engineer | ML-on-CSV/API playbook |
| Tulip | Cycle time, defect capture | Human-in-loop apps | S | Ops excellence | Complement for freeze UX |
| Parsable | Procedure compliance, MTTR | Connected worker | S | EHS / ops | Execution layer, not optimizer |
| UptimeAI | Reliability, anomaly | Advisory | S | Reliability engineer | Adjacent — loss from failures |
| Augury | Machine health, process health | Advisory (+ sensors) | H+S | Reliability / ops | Process Health messaging overlap |
| Tractian | MTBF, downtime | Advisory (+ sensors) | H+S | Maintenance mgr | GTM scale lesson, not core |
| Uptake | Fleet/asset availability | Analytics | S | Asset owner | Heavy industry APM |
| SparkCognition / Avathon | Uptime, optimization (vertical) | Mixed | S | Enterprise IT | Platform breadth |
| C3 AI | Inventory, reliability, process | App suite | S | CIO + line of business | Enterprise packaging benchmark |
| Seeq | Investigation time, loss understanding | Analytics | S | Process engineer | Complement in large accounts |
| Cognite | Time-to-insight (fabric) | Foundation | S | Digital twin lead | Partner / underlay |
| Palantir | OT/IT decision latency | Foundation + apps | S | CTO / plant digital | Ontology reference |
| HighByte | Data productization | Foundation | S | OT architect | UNS pattern for Stamped graph |
| Litmus | Edge ingest latency | Foundation | S | OT / SI | Edge optional for India |
| Landing AI | Visual defect rate | Model training / infer | S (+ camera) | Quality / data science | Vision lane adjacent |
| Cognex | Inspection throughput | Automated QC | H+S | Quality engineer | Not decision-layer peer |
| Instrumental | Yield, escape rate (electronics) | Analytics + vision | S | CM / OEM quality | Root-cause UX reference |
| Elementary | Inspection accuracy | Vision systems | H+S | Quality | Hardware-heavy |
| CloudNC | CAM programming hours | Advisory (toolpath) | S | CNC programmer | Discrete efficiency wedge |
| Toolpath | Setup/programming time | Advisory | S | Job shop owner | Same lane as CloudNC |
| Productive Machines / SenseNC | Chatter, cycle time | Advisory (FEA/speeds) | S | Machining engineer | Physics at spindle |
| Bright Machines | Assembly throughput | Physical automation | H+S | OEM automation | Irrelevant CapEx; study data loop |
| Noetive | Ops-wide “intelligence of record” | Agents + sensing | H+S | C-suite / innovation | Long-horizon archetype |
| BrightAI | Measurement accuracy, line stops | Physical AI + sensors | H+S | Ops / field services | Mostly infra; mfg is subset |
| MadeOS | Downtime, throughput | Prescribe to operator | S (+ gap-fill HW) | Plant manager | “Zero-loss ops” narrative |
| Microsoft / AWS / Google | Time-to-deploy apps | Substrate | S | Enterprise IT | Portable connectors rule |
| Rockwell | OEE, time-to-market | Automation + software | H+S | Controls engineer | Foundation in discrete |
| Emerson / Aspen | Yield, energy (process) | Hybrid models + APC adjacency | H+S | Process engineer | Incumbent in process |
| Honeywell Forge | Asset / site performance | Enterprise apps | S | VP operations | Large-account adjacent |
| GE Vernova | Generation availability | Energy equipment + software | H+S | Utility | Mostly irrelevant to factory |
| Aveva (Schneider) | Production + engineering | MES/historian + AI | S | Engineering IT | Post-Cognite Schneider stack |
| PTC | Service uptime, quality | PLM + IoT | S | Engineering | Digital thread, not shop KPI owner |

---

## 4. Entity dossiers (USA / NA and material NA GTM)

Each dossier: **KPI · Mode · HW/SW · Buyer · URLs · Stamped implication (software-only efficiency).**

---

### 4.1 Process optimization & closed-loop (continuous / batch)

#### Fero Labs
- **HQ:** New York, USA — https://www.ferolabs.com/
- **KPI owned:** Process margin proxies — scrap/yield, quality variation, $/ton savings (**vendor-claimed** in case studies).
- **Mode:** **Advisory / live production** recommendations with explainable models; engineer remains in control (not DCS write by default).
- **HW vs SW:** **Software** on historian/MES/LIMS-style data.
- **Buyer:** Process engineer, metallurgist/chemist, continuous improvement; steel, chemicals, cement, CPG.
- **URLs:** https://www.ferolabs.com/case-studies/gerdau · https://www.climateinvestment.com/news/fero-labs-secures-15m-to-reduce-manufacturing-emissions-with-ai
- **Vendor-claimed highlights:** Gerdau narrative — **$3/ton** and **15%** lower quality variation (**vendor case study**); cumulative funding **$30M** after **$15M** growth round (**investor/company press**).
- **Stamped (SW-only):** Closest **Process Direct** NA peer. Copy the **white-box + simulate + freeze** doctrine; compete on India mid-market packaging and faster time-to-first-prescription using CSV/historian-only onboarding.

#### Imubit
- **HQ:** Houston, USA — https://imubit.com/
- **KPI owned:** Economic margin ($/bbl class), natural gas / fuel intensity, average yield (**vendor-claimed** on website).
- **Mode:** **Closed-loop** — RL controllers writing through existing DCS/APC within certified envelopes.
- **HW vs SW:** **Software**; uses plant controls layer.
- **Buyer:** Advanced process control engineer, refinery/cement economics owner.
- **URLs:** https://imubit.com/ · Customer quotes on site (Citgo, Ash Grove, Monroe Energy, Preem, etc. — **vendor**).
- **Vendor-claimed:** **100+** closed-loop applications; **15–30%** NG reduction; **$0.25/bbl** margin; **1–3%** yield — all **vendor-claimed**.
- **Stamped (SW-only):** Gold standard for **L4** when customer trusts APC. Stamped should default to **L3 prescribe** in India mid-market; treat Imubit as proof that efficiency KPIs must be **economic**, not dashboard vanity.

#### Basetwo
- **HQ:** Toronto, Canada (NA GTM) — https://www.basetwo.ai/
- **KPI owned:** Batch cycle time, spec compliance, throughput in pharma/chemical/personal care.
- **Mode:** **Advisory** digital twin / copilot; AutoPilot narratives toward assisted control.
- **HW vs SW:** **Software** (low-code physics-informed AI).
- **Buyer:** Process development, manufacturing science.
- **URLs:** https://www.basetwo.ai/announcements/basetwo-raises-11-5m-series-a-to-transform-chemical-manufacturing-with-physics-ai-platform
- **Funding (press):** Series A **$11.5M USD** (**company announcement**).
- **Stamped (SW-only):** Method reference for **first-principles + data** without selling hardware; Stamped can offer narrower KPI modules vs full twin platform.

#### Green Factory AI
- **HQ:** Helsinki with **USA office** (**company**); NA-relevant process mills — https://greenfactory.ai/
- **KPI owned:** Raw material, chemical, water, and **energy per unit**; profit uplift (**vendor-claimed** ranges **5–10%** profit, **10–30%** CO₂/emission intensity reduction on marketing pages — **vendor-claimed**).
- **Mode:** Starts **advisory** (operator-approved recommendations); optional **writeback** when approved (**product page**).
- **HW vs SW:** **Software** on-prem containers; connectors OPC UA/DA, MQTT, PHD REST — no rip-and-replace controls.
- **Buyer:** Mill process engineer (pulp/paper first; chemicals/steel expansion narrative).
- **URLs:** https://greenfactory.ai/product/ · https://greenfactory.ai/about-us/
- **Stamped (SW-only):** Nearly ideal architectural cousin for Stamped Process — **on-prem, advisory-first, constraint-safe setpoints**. Differentiate on India verticals ( metals, FMCG process ) and PE-outcome commercial model.

#### Emerson / AspenTech
- **HQ:** USA global — https://www.emerson.com/ · https://www.aspentech.com/
- **KPI owned:** Yield, energy intensity in existing Aspen customers (**vendor case** — e.g., Dow **10%** yield improvement cited in Aspen Hybrid Models materials — **vendor-claimed**).
- **Mode:** **Advisory** simulation + hybrid models; APC ecosystem can become closed-loop via incumbent tools.
- **HW vs SW:** **Both** (Emerson instrumentation + Aspen software).
- **Buyer:** Process engineer already on Aspen stack.
- **URLs:** https://www.aspentech.com/en/solutions/aspen-hybrid-models/
- **Stamped (SW-only):** Compete **below** Aspen footprint — plants with historians but **no** Aspen license. Stamped sells outcomes without hybrid-model tooling tax.

#### Seeq
- **HQ:** Seattle area, USA — https://www.seeq.com/
- **KPI owned:** Indirect — engineer productivity and loss **understanding**; not typically a guaranteed OEE/yield contract.
- **Mode:** **Advisory** analytics workbench on time-series.
- **HW vs SW:** **Software**.
- **Buyer:** Process engineer, reliability engineer.
- **URLs:** https://www.seeq.com/ · Series D **$50M** (**PR Newswire**, 2024).
- **Stamped (SW-only):** Partner/complement: Stamped owns **ranked actions + freeze**; Seeq owns **investigation UI** in F500. Do not confuse analytics depth with outcome ownership.

#### C3 AI
- **HQ:** Redwood City, CA — https://www.c3.ai/
- **KPI owned:** App-dependent (inventory, reliability, production); enterprise SLAs vary.
- **Mode:** Mostly **advisory** apps; agentic platform expanding.
- **HW vs SW:** **Software**.
- **Buyer:** CIO + line-of-business SVP in large industrials.
- **URLs:** https://www.c3.ai/news/c3-ai-announces-fiscal-fourth-quarter-and-full-fiscal-year-2026-results — FY2026 revenue **$250.3M** (**SEC/company release**).
- **Stamped (SW-only):** Benchmark for **multi-app packaging**; Stamped should stay narrow (2–3 KPI modules) vs C3 breadth.

---

### 4.2 Production visibility, OEE, and discrete efficiency

#### Sight Machine
- **HQ:** San Francisco / Ann Arbor roots — https://www.sightmachine.com/
- **KPI owned:** OEE, throughput, loss categorization; path to optimization.
- **Mode:** **Advisory** analytics on a production data model.
- **HW vs SW:** **Software** (connectors to existing sources).
- **Buyer:** VP operations, digital manufacturing.
- **URLs:** https://www.sightmachine.com/
- **Stamped (SW-only):** Learn **production data model** normalization; Stamped must go one layer deeper to **prescriptive** ranked actions tied to rupee/ton KPIs.

#### MachineMetrics
- **HQ:** Massachusetts, USA — https://www.machinemetrics.com/
- **KPI owned:** Machine OEE, cycle time, downtime Pareto.
- **Mode:** **Advisory** dashboards and APIs.
- **HW vs SW:** **H+S** — edge connectivity to CNC/PLC common in GTM.
- **Buyer:** Discrete plant manager, CI leader.
- **URLs:** https://www.businesswire.com/news/home/20210616005165/en/MachineMetrics-Announces-%2420M-Series-B-Funding-Round
- **Stamped (SW-only):** If machine data already exists, Stamped adds **cross-line efficiency** (scrap energy, process) without selling connectors; if not, partner rather than sell hardware.

#### Guidewheel (FactoryOps)
- **HQ:** San Francisco, USA — https://www.guidewheel.com/
- **KPI owned:** Downtime reduction, OEE uplift via **power-signature** machine states (**vendor**).
- **Mode:** **Advisory** — visibility and AI-assisted categorization.
- **HW vs SW:** **H+S** — clamp-on power sensors emphasized in GTM (**vendor**).
- **Buyer:** Plant manager without PLC access.
- **URLs:** https://www.businesswire.com/news/home/20240813639025/en/Guidewheel-raises-%2431M-Series-B-to-scale-AI-powered-FactoryOps-across-factory-floors-globally
- **Funding (press):** Series B **$31M** (Aug 2024).
- **Stamped (SW-only):** Parallel to “use existing meters/signals” — Stamped should ingest Guidewheel-like data via API **if present**, not duplicate sensor GTM.

#### Jemba (TeepTrak)
- **HQ:** Product by TeepTrak (Paris HQ, **Chicago US office**) — https://jemba.ai/
- **KPI owned:** OEE explanation, anomaly MTTR, quality correlation, energy monitoring (**vendor**).
- **Mode:** **Advisory** — ranked, costed recommendations in “operator language.”
- **HW vs SW:** **Software-first** (machines, sensors, CSV, API); TeepTrak often bundles IoT (**vendor**).
- **Buyer:** Factory manager, process engineer **without** data science team.
- **URLs:** https://jemba.ai/ · https://teeptrak.com/en/oee-monitoring-software-2/
- **Vendor-claimed:** **48h** setup; **450+** plants (**vendor**); TeepTrak cites **+29 OEE points** average and **99.7%** anomaly detection (**vendor-claimed** — treat as marketing until independently verified).
- **Stamped (SW-only):** Strong playbook for **mid-market ML on existing signals** — Stamped should match “no data scientist” UX while owning **process + energy** cross-KPI prescriptions.

#### Tulip Interfaces
- **HQ:** Somerville, MA — https://tulip.co/
- **KPI owned:** Frontline cycle time, defect logging, training time — via apps customers build.
- **Mode:** **Human-in-loop** execution apps (advisory/checklist).
- **HW vs SW:** **Software** (optional device ecosystem).
- **Buyer:** Operations excellence, manufacturing engineering.
- **URLs:** https://tulip.co/press/tulip-raises-100m-seriesc-led-by-insight-partners/
- **Stamped (SW-only):** **Freeze/approve UX** layer — Stamped prescriptions could surface as Tulip apps in enterprise deals.

#### Parsable
- **HQ:** San Francisco — https://parsable.com/
- **KPI owned:** Procedure adherence, mean time to repair, audit readiness — not yield optimization core.
- **Mode:** **Advisory** connected worker workflows.
- **HW vs SW:** **Software** (mobile).
- **Buyer:** EHS, operations, quality systems leader.
- **URLs:** https://parsable.com/blog/manufacturing/parsable-raises-20m-from-global-industrial-firms-to-eliminate-paper/
- **Stamped (SW-only):** Downstream **action delivery** for maintenance/ops tasks triggered by Stamped anomaly prescripts.

#### MadeOS
- **HQ:** GTM narrative global; Tracxn lists Mexico founding **2025** — https://madeos.ai/
- **KPI owned:** Uptime, throughput, quality drift — **vendor-claimed** up to **55%** unplanned downtime reduction (**vendor homepage** — **vendor-claimed**).
- **Mode:** **Prescriptive** operator/maintenance actions from operational digital twin; not replacing DCS (**vendor FAQ**).
- **HW vs SW:** **Software-first** with optional gap-fill instrumentation/vision (**vendor**).
- **Buyer:** Plant manager seeking brownfield start.
- **URLs:** https://madeos.ai/
- **Stamped (SW-only):** Competing narrative to Stamped “zero-loss ops” — differentiate with **proven India references** and strict **no new hardware default**.

---

### 4.3 Reliability, APM, and loss from failures (efficiency adjacency)

#### Augury
- **HQ:** NYC (US commercial) — https://www.augury.com/
- **KPI owned:** Machine health (PdM); **Process Health** expands to yield/waste (**vendor**).
- **Mode:** **Advisory** recommendations; sensors for Machine Health.
- **HW vs SW:** **H+S** (vibration/acoustic/thermal).
- **Buyer:** Reliability director; CPG innovation (e.g., **PepsiCo** story — **vendor**).
- **URLs:** https://www.augury.com/success-stories/pepsicos-manufacturing-innovation-leads-to-tangible-roi/ · https://techcrunch.com/2025/02/19/augury-raises-73m-on-a-1b-valuation-for-ai-to-detect-malfunctions-in-factory-machines/
- **Funding (press):** **$75M** (Feb 2025), **$1B+** valuation (**press/company**).
- **Stamped (SW-only):** PdM not core — but **Process Health** messaging collides with Stamped Process; position Stamped as **cross-system efficiency** (recipe + utility + rate) vs vibration-first.

#### UptimeAI
- **HQ:** US expansion focus — https://www.uptimeai.com/
- **KPI owned:** Plant reliability, process anomaly detection.
- **Mode:** **Advisory**.
- **HW vs SW:** **Software** on existing plant data.
- **Buyer:** Reliability / process engineer in process industries.
- **URLs:** https://www.prnewswire.com/news-releases/ai-innovator-uptimeai-raises-14m-to-drive-north-american-expansion-302219810.html
- **Funding (press):** **$14M** NA expansion (**PR Newswire**, 2024).
- **Stamped (SW-only):** Adjacent — Stamped should attribute downtime dollars to **process/energy** root causes when sensor PdM is absent.

#### Tractian
- **HQ:** Brazil with **US GTM** — https://tractian.com/
- **KPI owned:** Downtime, MTBF, maintenance cost.
- **Mode:** **Advisory** with sensor kit.
- **HW vs SW:** **H+S**.
- **Buyer:** Maintenance manager (SMB-to-mid market motion).
- **URLs:** https://tractian.com/
- **Funding (press):** Series C **$120M** cited in 2024 roundups — verify primary PR before investor decks.
- **Stamped (SW-only):** GTM velocity lesson; not a process-efficiency peer.

#### Uptake
- **HQ:** Chicago — https://www.uptake.com/
- **KPI owned:** Asset availability in rail, mining, heavy industry heritage.
- **Mode:** **Advisory** analytics.
- **HW vs SW:** **Software**.
- **Buyer:** Asset owner / OEM fleet operator.
- **URLs:** https://www.uptake.com/
- **Stamped (SW-only):** Limited overlap except **fleet-to-plant** spare parts latency — skip as core competitor.

#### SparkCognition / Avathon
- **HQ:** Austin, TX — https://www.sparkcognition.com/ (confirm **Avathon** branding on current SKUs — **rebrand in progress** in some materials)
- **KPI owned:** Vertical-specific (energy, manufacturing reliability, security).
- **Mode:** Mixed **advisory** and automation in defense/energy-heavy portfolios.
- **HW vs SW:** **Software**-led platform.
- **Buyer:** Enterprise digital + vertical VP.
- **URLs:** https://www.prnewswire.com/news-releases/sparkcognition-announces-123-million-series-d-funding-and-a-unicorn-valuation-to-accelerate-ai-adoption-across-industries-301467137.html
- **Funding (press):** Series D **$123M** (Jan 2022) (**PR**).
- **Stamped (SW-only):** Avoid platform sprawl; Stamped wins on **one plant, one KPI, 90-day proof**.

---

### 4.4 Quality, vision, and programming-time efficiency (discrete)

#### Landing AI
- **HQ:** Palo Alto — https://landing.ai/
- **KPI owned:** Visual defect detection accuracy, model deployment time.
- **Mode:** **Advisory** inference / MLOps for vision.
- **HW vs SW:** **Software** (+ customer cameras).
- **Buyer:** Quality engineer, central data science.
- **URLs:** https://landing.ai/
- **Stamped (SW-only):** Integrate vision **scores as features** in plant efficiency model; do not become a vision company.

#### Cognex
- **HQ:** Natick, MA (NASDAQ: CGNX) — https://www.cognex.com/
- **KPI owned:** Inspection throughput, false reject rate.
- **Mode:** **Closed-loop** at station level (reject/accept hardware).
- **HW vs SW:** **H+S** machine vision leader.
- **Buyer:** Quality / automation engineer.
- **URLs:** https://www.cognex.com/en-us/company/investor-information — confirm latest 10-K for revenue (**~$994M** cited in 2025 roundups — **verify against IR**).
- **Stamped (SW-only):** Not a peer — consume pass/fail streams if available.

#### Instrumental
- **HQ:** Palo Alto — https://www.instrumental.com/
- **KPI owned:** Electronics yield, escape rate, root-cause time.
- **Mode:** **Advisory** analytics combining images + process data.
- **HW vs SW:** **Software**-centric with line cameras.
- **Buyer:** CM/OEM quality leader.
- **URLs:** https://www.instrumental.com/
- **Stamped (SW-only):** UX reference for **correlating visual + parametric** data without Stamped selling cameras.

#### Elementary
- **HQ:** USA — https://www.elementaryml.com/
- **KPI owned:** Inspection accuracy on line.
- **Mode:** Automated vision decisions at edge.
- **HW vs SW:** **H+S**.
- **Buyer:** Quality / automation.
- **URLs:** https://www.elementaryml.com/
- **Stamped (SW-only):** Same as Cognex — feature input only.

#### CloudNC
- **HQ:** UK with **US market** — https://www.cloudnc.com/
- **KPI owned:** CAM programming hours, quoting cycle time.
- **Mode:** **Advisory** inside CAM (Fusion/Mastercam/NX plugins).
- **HW vs SW:** **Software**.
- **Buyer:** CNC programmer, job shop owner.
- **URLs:** https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/
- **Vendor-claimed scale:** **1,000+** machine shops (**vendor**); **$20M** raise Sep 2026 (**press**).
- **Stamped (SW-only):** Discrete **setup/programming** wedge is orthogonal — partner for machining vertical bundles.

#### Toolpath
- **HQ:** USA — https://www.toolpath.com/
- **KPI owned:** Programming and machining strategy time.
- **Mode:** **Advisory** CAM assistance.
- **HW vs SW:** **Software**.
- **Buyer:** Job shop / programming lead.
- **URLs:** https://www.toolpath.com/
- **Stamped (SW-only):** Optional alliance — Stamped focuses shop **OEE + energy** per part, not toolpath geometry.

#### Productive Machines / SenseNC
- **HQ:** UK deeptech; **US-relevant** for aerospace/defense supply chain — https://solutions.productivemachines.co.uk/
- **KPI owned:** Cycle time, surface quality via chatter avoidance.
- **Mode:** **Advisory** feed/speed optimization from physics models.
- **HW vs SW:** **Software** (SenseNC).
- **Buyer:** Machining process engineer.
- **URLs:** https://solutions.productivemachines.co.uk/
- **Stamped (SW-only):** Physics-at-tool complements Stamped **line-level** efficiency; integrate as optional module.

---

### 4.5 Data foundation, ontology, and enterprise industrial AI

#### Cognite
- **HQ:** Oslo; **heavy US enterprise sales** — https://www.cognite.com/
- **KPI owned:** Fabric KPI — time-to-trustworthy context, not line yield guarantee.
- **Mode:** **Foundation** + Atlas AI agents (**advisory**).
- **HW vs SW:** **Software**.
- **Buyer:** Chief digital officer, asset owner IT/OT.
- **URLs:** https://www.cognite.com/en/company/newsroom/schneider-electric-announces-agreement-to-acquire-cognite · https://www.reuters.com/business/schneider-electric-buy-ai-software-firm-cognite-31-billion-2026-06-30/
- **Deal (press):** Schneider agreement **$3.1B** (Jun 2026); **>$170M** 2025 revenue cited (**Reuters/Schneider** — not closed as of study notes).
- **Stamped (SW-only):** Build **minimal asset graph** in-product; partner with CDF in F500, don’t sell fabric alone in India mid-market.

#### Palantir Technologies (Foundry for Manufacturing)
- **HQ:** Denver / US — https://www.palantir.com/explore/foundry-for-manufacturing/
- **KPI owned:** Decision latency, quality/supply exceptions — customer-defined.
- **Mode:** **Advisory** apps + AIP agents on ontology.
- **HW vs SW:** **Software**.
- **Buyer:** CTO, manufacturing COO (large programs).
- **URLs:** https://na.panasonic.com/news/palantir-and-panasonic-energy-of-north-america-sign-multi-year-agreement
- **Public finances:** Company-wide FY2025 revenue **$4.475B** (**SEC earnings release**) — not manufacturing-only.
- **Stamped (SW-only):** Ontology + **human-governed** action audit trail is the steal; services-heavy GTM is not.

#### HighByte
- **HQ:** Portland, ME — https://www.highbyte.com/
- **KPI owned:** Data product readiness (UNS), not OEE.
- **Mode:** **Foundation** — edge contextualization.
- **HW vs SW:** **Software** (edge hub software).
- **Buyer:** OT architect, Industry 4.0 lead.
- **URLs:** https://www.highbyte.com/
- **Stamped (SW-only):** Mirror **small UNS** internally; 3–5 canonical objects (line, meter, batch, SKU) for prescribe engine.

#### Litmus Automation
- **HQ:** San Jose — https://litmus.io/
- **KPI owned:** Edge collection reliability.
- **Mode:** **Foundation**.
- **HW vs SW:** **Software** edge platform.
- **Buyer:** OT / SI partner.
- **URLs:** https://litmus.io/
- **Stamped (SW-only):** Optional edge — prefer plant’s existing gateway; Litmus as integrate-not-compete.

#### Microsoft (Azure industrial)
- **HQ:** Redmond — https://www.microsoft.com/
- **KPI owned:** N/A (substrate).
- **Mode:** Partner solutions + Copilot industrial narratives.
- **HW vs SW:** **Software** cloud; partners bring OT.
- **Buyer:** Enterprise IT.
- **URLs:** https://www.rockwellautomation.com/en-us/company/news/press-releases/Rockwell-Automation-and-Microsoft-Expand-Partnership-to-Leverage-Generative-AI-Capabilities-for-Enhanced-Productivity-and-Faster-Time-to-Market.html
- **Stamped (SW-only):** Stay cloud-portable; use Azure OpenAI only where customer already standardized.

#### AWS IoT SiteWise
- **HQ:** Seattle — https://aws.amazon.com/iot-sitewise/
- **KPI owned:** N/A (ingest/model/monitor).
- **Mode:** **Foundation**.
- **HW vs SW:** **Software** + Greengrass edge option.
- **Buyer:** Cloud architect.
- **URLs:** https://aws.amazon.com/iot-sitewise/
- **Stamped (SW-only):** SiteWise as **sink/source** connector in multi-cloud Stamped deployments.

#### Google Cloud (Manufacturing Data Engine patterns)
- **HQ:** Mountain View — https://cloud.google.com/solutions/manufacturing
- **KPI owned:** N/A (patterns on BigQuery/Vertex).
- **Mode:** **Foundation**.
- **HW vs SW:** **Software**.
- **Buyer:** Analytics-forward manufacturers.
- **URLs:** https://cloud.google.com/solutions/manufacturing
- **Stamped (SW-only):** Lower default priority in India vs Azure; support if customer already on GCP.

#### Rockwell Automation
- **HQ:** Milwaukee — https://www.rockwellautomation.com/
- **KPI owned:** Automation productivity, OEE via FactoryTalk/Plex ecosystems.
- **Mode:** Mix of **closed-loop** control (PLCs) and **advisory** software.
- **HW vs SW:** **H+S**.
- **Buyer:** Controls engineer, plant automation lead.
- **URLs:** Rockwell–Microsoft GenAI partnership (link above).
- **Stamped (SW-only):** Sit **above** Rockwell stack — ingest tags/historian, prescribe without PLC programming services.

#### Honeywell Forge
- **HQ:** Charlotte / US — https://www.honeywell.com/us/en/honeywell-forge
- **KPI owned:** Site/asset performance, cyber, worker productivity (portfolio).
- **Mode:** **Advisory** enterprise apps.
- **HW vs SW:** **Software**-forward brand on Honeywell install base.
- **Buyer:** VP operations in process and buildings-adjacent plants.
- **URLs:** https://www.honeywell.com/us/en/honeywell-forge
- **Stamped (SW-only):** Compete on **narrow KPI guarantees** vs Forge suite breadth.

#### GE Vernova
- **HQ:** US — https://www.gevernova.com/
- **KPI owned:** Power generation availability — not general factory OEE.
- **Mode:** Equipment + legacy Predix-era services (restructured).
- **HW vs SW:** **H+S** (energy equipment).
- **Buyer:** Utility / generation owner.
- **URLs:** https://www.gevernova.com/
- **Stamped (SW-only):** **Irrelevant** as factory peer except co-located industrial sites with GE power assets.

#### Aveva (Schneider Electric portfolio)
- **Extra (material):** Engineering + operations software widely deployed in NA process/discrete — https://www.aveva.com/
- **KPI owned:** Engineering change cycle, MES throughput — varies by module.
- **Mode:** **Advisory** + MES execution.
- **HW vs SW:** **Software**.
- **Buyer:** Engineering IT + plant systems owner.
- **Stamped (SW-only):** Post-Cognite acquisition, Schneider stack is **partner channel** — Stamped as AI outcome layer on Aveva/historian data.

---

### 4.6 Physical AI, software-defined manufacturing, and multimodal ops

#### Bright Machines
- **HQ:** San Francisco — https://www.brightmachines.com/
- **KPI owned:** Assembly throughput, ramp time for electronics/AI hardware builds.
- **Mode:** **Closed-loop** robotics + software-defined assembly.
- **HW vs SW:** **H+S** (robotics + Bright Factory software).
- **Buyer:** OEM/ODM automation VP.
- **URLs:** https://www.prnewswire.com/news-releases/bright-machines-raises-126m-series-c-funding-to-propel-manufacturing-into-software-defined-era-302181151.html
- **Funding (press):** Series C **$126M**; total **>$400M** (**vendor PR**).
- **Stamped (SW-only):** **Irrelevant** CapEx path — study **data feedback to design**, do not copy robotics GTM.

#### Noetive
- **HQ:** San Francisco; founded **2026** — https://noetive.ai/
- **KPI owned:** “Intelligence of record” — economy-wide ops KPI (early).
- **Mode:** **Agents** + world models; multimodal **sensing pods** in narrative.
- **HW vs SW:** **H+S** positioning.
- **Buyer:** Innovation office / C-suite design partners.
- **URLs:** https://noetive.ai/news/noetive-emerges-from-stealth-with-41-million-seed
- **Funding (press):** **$41M** seed (Sep 2026) (**company/PR**).
- **Stamped (SW-only):** Long-horizon **architecture watch** — Stamped stays pragmatic L3 on existing data.

#### BrightAI (bright.ai)
- **HQ:** USA — https://www.bright.ai/
- **KPI owned:** Infrastructure uptime; in manufacturing — measurement accuracy (Latham Pools partnership), acoustic early friction (**vendor**).
- **Mode:** **Advisory** to field/line teams; Stateful OS for multimodal data.
- **HW vs SW:** **H+S** — **250,000+** sensors deployed cited in press (**SiliconANGLE**, **vendor/press**); edge AI hubs.
- **Buyer:** Asset-heavy operators (utilities, HVAC, manufacturing partners).
- **URLs:** https://siliconangle.com/2024/11/19/brightai-raises-15m-ai-powered-infrastructure-optimization-platform/ · https://bright.ai/industries/
- **Funding (press):** **$15M** seed (2024); **>$80M** revenue from six enterprises cited (**press** — **verify**).
- **Stamped (SW-only):** Mostly **not** Stamped peer — unless Stamped adds optional acoustic **features** from existing microphones (software-only path only).

---

### 4.7 Connected operations (adjacent, not core factory AI)

#### Samsara (NYSE: IOT)
- **HQ:** San Francisco — https://www.samsara.com/
- **KPI owned:** Fleet/equipment utilization, site safety — industrial overlap at **site** level.
- **Mode:** **Advisory** dashboards.
- **HW vs SW:** **H+S** telematics.
- **Buyer:** Operations director (logistics/construction/industrial sites).
- **URLs:** https://www.samsara.com/
- **Stamped (SW-only):** Irrelevant inside four walls except **shared energy telemetry** on mobile assets.

---

## 5. Cross-cutting patterns (software-only efficiency)

### 5.1 What wins NA efficiency budgets in 2025–2026

1. **Named KPI in the first sales call** — margin, OEE points, programming hours, scrap rate — not “digital transformation.”
2. **Brownfield onboarding** — OPC/MQTT/historian/CSV/API (Green Factory AI, Jemba, MadeOS, Fero) beats greenfield MES rip-and-replace.
3. **Advisory-first trust ladder** — explicit operator approval before writeback (Green Factory AI product doctrine; Fero “engineer in control”; Stamped “freeze”).
4. **Explainability for audit** — process industries require white-box drivers (Fero, Basetwo, Aspen hybrid narrative).
5. **Closed-loop as upsell** — Imubit proves plants pay for L4 when economics are modeled; most mid-market stops at L3.

### 5.2 What Stamped should not copy from NA

- Sensor-first GTM as default (Augury, Tractian, Guidewheel hardware story).
- Robotics / SDM CapEx (Bright Machines).
- Enterprise fabric-only sales (Cognite/Palantir without KPI app).
- General-purpose vision platforms (Landing AI, Cognex) as core identity.

### 5.3 Minimal data graph ( steal from Cognite / Palantir / HighByte )

| Object | Why it matters for efficiency |
|--------|-------------------------------|
| **Production line / unit** | OEE, rate, scrap attribution |
| **Batch / grade / SKU** | Yield and spec efficiency |
| **Meter / utility tag** | Co-benefit intensity, not primary story |
| **Asset / machine** | Downtime correlation |
| **Prescription / freeze record** | Audit and M&V for outcomes |

---

## 6. Competitive density by efficiency KPI (qualitative)

| KPI cluster | Crowded NA players | White space for Stamped (India mid-market, SW-only) |
|-------------|-------------------|-----------------------------------------------------|
| Process yield / $/ton | Fero, Imubit, Basetwo, Green Factory AI, Aspen | Bundled **energy + rate** prescribe with 90-day proof |
| OEE / downtime | Sight Machine, MachineMetrics, Guidewheel, Jemba, Tulip | Root-cause **prescriptions** without selling sensors |
| CAM / setup time | CloudNC, Toolpath, SenseNC | Line-level efficiency linking **setup to kWh/part** |
| Quality escape | Landing AI, Cognex, Instrumental | Parametric + optional vision **features**, not cameras |
| Reliability | Augury, UptimeAI, Tractian | Only where free CMMS/historian signals exist |

---

## 7. USA narrative for Stamped

North American industrial AI is **bifurcated**. At the top, **data fabrics and ontologies** (Cognite heading into Schneider, Palantir Foundry, C3’s app suite, HighByte/Litmus UNS/edge patterns) absorb years of budget and SI hours — they rarely **guarantee** a line-level efficiency KPI without a specialist sitting on top. **Automation majors** (Rockwell with Microsoft, Emerson/Aspen hybrid models, Honeywell Forge) own trust in controls and historians but sell breadth, not a mid-market outcome contract.

The **outcome layer** is fragmented but instructive. **Process margin** specialists (Fero Labs, Imubit, Basetwo, Green Factory AI) prove plants pay when AI touches **$/ton, yield, or fuel intensity** — with Imubit at the **closed-loop** extreme and Fero/Green Factory at the **explainable advisory** extreme Stamped should mirror. **Visibility players** (Sight Machine, MachineMetrics, Guidewheel, Jemba/TeepTrak) own OEE and downtime language; many stop before **ranked, costed actions** in the operator’s vocabulary. **Discrete programming** tools (CloudNC, Toolpath, Productive Machines) attack a different bottleneck — CAM hours — that Stamped can partner with rather than fight. **Physical AI** fundraisers (Bright Machines, Noetive, BrightAI) chase world models, robotics, and multimodal sensing — valuable as **architecture R&D**, wrong GTM for a software-only India wedge.

**Stamped’s NA-informed strategy:** Enter as an **outcome specialist** for **software-only plant efficiency** — existing historians, meters, MES exports, and CSVs → **prescriptions with human freeze** → optional writeback where APC exists. Treat US platforms as **integration partners or future channels**, not as peers for the mid-market plant manager. Lead with **two efficiency wedges** (process rate/yield/scrap and co-benefit intensity) under one action layer, prove economics in **90 days**, and resist becoming a sensor company, a fabric company, or a robotics company. NA proves the buyer pays for **KPI ownership**; Stamped’s differentiation is doing that **without new hardware** in markets the NA stack has ignored.

---

## 8. Source URL appendix

### Process / optimization
- Fero Labs: https://www.ferolabs.com/
- Fero Gerdau case: https://www.ferolabs.com/case-studies/gerdau
- Fero funding: https://www.climateinvestment.com/news/fero-labs-secures-15m-to-reduce-manufacturing-emissions-with-ai
- Imubit: https://imubit.com/
- Basetwo Series A: https://www.basetwo.ai/announcements/basetwo-raises-11-5m-series-a-to-transform-chemical-manufacturing-with-physics-ai-platform
- Green Factory AI product: https://greenfactory.ai/product/
- Green Factory AI home: https://greenfactory.ai/
- Seeq Series D: https://www.prnewswire.com/news-releases/seeq-announces-50-million-series-d-funding-round-led-by-sixth-street-growth-302215495.html
- Aspen Hybrid Models: https://www.aspentech.com/en/solutions/aspen-hybrid-models/
- C3 AI FY2026 results: https://www.c3.ai/news/c3-ai-announces-fiscal-fourth-quarter-and-full-fiscal-year-2026-results

### Production / OEE / frontline
- Sight Machine: https://www.sightmachine.com/
- MachineMetrics Series B: https://www.businesswire.com/news/home/20210616005165/en/MachineMetrics-Announces-%2420M-Series-B-Funding-Round
- Guidewheel: https://www.guidewheel.com/
- Guidewheel Series B: https://www.businesswire.com/news/home/20240813639025/en/Guidewheel-raises-%2431M-Series-B-to-scale-AI-powered-FactoryOps-across-factory-floors-globally
- Jemba: https://jemba.ai/
- TeepTrak + Jemba: https://teeptrak.com/en/oee-monitoring-software-2/
- Tulip Series C: https://tulip.co/press/tulip-raises-100m-seriesc-led-by-insight-partners/
- Parsable funding blog: https://parsable.com/blog/manufacturing/parsable-raises-20m-from-global-industrial-firms-to-eliminate-paper/
- MadeOS: https://madeos.ai/

### Reliability / industrial AI platforms
- Augury / PepsiCo: https://www.augury.com/success-stories/pepsicos-manufacturing-innovation-leads-to-tangible-roi/
- Augury funding: https://techcrunch.com/2025/02/19/augury-raises-73m-on-a-1b-valuation-for-ai-to-detect-malfunctions-in-factory-machines/
- UptimeAI: https://www.uptimeai.com/
- UptimeAI $14M: https://www.prnewswire.com/news-releases/ai-innovator-uptimeai-raises-14m-to-drive-north-american-expansion-302219810.html
- Tractian: https://tractian.com/
- Uptake: https://www.uptake.com/
- SparkCognition Series D: https://www.prnewswire.com/news-releases/sparkcognition-announces-123-million-series-d-funding-and-a-unicorn-valuation-to-accelerate-ai-adoption-across-industries-301467137.html

### Quality / CAM / machining
- Landing AI: https://landing.ai/
- Cognex IR: https://www.cognex.com/en-us/company/investor-information
- Instrumental: https://www.instrumental.com/
- Elementary: https://www.elementaryml.com/
- CloudNC: https://www.cloudnc.com/
- CloudNC funding: https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/
- Toolpath: https://www.toolpath.com/
- Productive Machines / SenseNC: https://solutions.productivemachines.co.uk/

### Data foundation / enterprise / automation
- Cognite / Schneider: https://www.reuters.com/business/schneider-electric-buy-ai-software-firm-cognite-31-billion-2026-06-30/
- Palantir manufacturing: https://www.palantir.com/explore/foundry-for-manufacturing/
- Panasonic–Palantir: https://na.panasonic.com/news/palantir-and-panasonic-energy-of-north-america-sign-multi-year-agreement
- HighByte: https://www.highbyte.com/
- Litmus: https://litmus.io/
- AWS IoT SiteWise: https://aws.amazon.com/iot-sitewise/
- Google manufacturing: https://cloud.google.com/solutions/manufacturing
- Rockwell–Microsoft: https://www.rockwellautomation.com/en-us/company/news/press-releases/Rockwell-Automation-and-Microsoft-Expand-Partnership-to-Leverage-Generative-AI-Capabilities-for-Enhanced-Productivity-and-Faster-Time-to-Market.html
- Honeywell Forge: https://www.honeywell.com/us/en/honeywell-forge
- Emerson: https://www.emerson.com/
- GE Vernova: https://www.gevernova.com/
- Aveva: https://www.aveva.com/

### Physical AI / emerging narratives
- Bright Machines Series C: https://www.prnewswire.com/news-releases/bright-machines-raises-126m-series-c-funding-to-propel-manufacturing-into-software-defined-era-302181151.html
- Noetive seed: https://noetive.ai/news/noetive-emerges-from-stealth-with-41-million-seed
- BrightAI: https://www.bright.ai/
- BrightAI funding (SiliconANGLE): https://siliconangle.com/2024/11/19/brightai-raises-15m-ai-powered-infrastructure-optimization-platform/
- BrightAI manufacturing: https://bright.ai/industries/

### Adjacent
- Samsara: https://www.samsara.com/

---

*End of exploration draft — not product lock.*
