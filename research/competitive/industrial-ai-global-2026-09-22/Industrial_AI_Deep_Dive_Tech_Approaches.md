# Industrial AI Deep Dive — Tech Approaches (2024–2026)
**Prepared for:** Vinayak Raizada — Stamped (India)  
**Date:** 2026-09-22 (IST)  
**Parent study:** `Industrial_AI_Competitor_and_Tech_Deep_Dive_2026-09-22.md`  
**Method:** WebSearch + WebFetch of primary vendor docs, research blogs, standards bodies; marketing claims flagged as **vendor-claimed**; no invented statistics.

---

## How to read this annex

This annex explains *how* industrial AI systems actually work in plain English: what data goes in, what method is applied, what comes out, who buys it, and how vendors get paid. It is written so Vinayak can monologue without slides. Pair each section with the regional dossiers when citing a company.

Stamped mapping reminder:
- **Stamped Energy** cares most about: energy intensity / M&V, bill defence, soft sensors for utilities, HITL prescribe, IPMVP.
- **Stamped Process** cares most about: methods/PE decisions, hybrid twins, CAM/CNC AI as adjacent, open-loop → supervised closed-loop ladder.

---

## 1. Stack layers: connect → see → predict → prescribe → act → agentic

| Layer | Plain-English question | Typical data in | Typical method | Typical output | Who buys |
|---|---|---|---|---|---|
| **Connect** | Can we get trustworthy tags out of PLCs/DCS/historians? | OPC UA, MQTT Sparkplug, Modbus, proprietary drivers | Protocol gateways, Unified Namespace, edge buffers | Contextualized streams + asset IDs | OT architect / CIO |
| **See** | What is happening / happened? | Time series, events, quality, energy meters | Dashboards, OEE, self-serve analytics | Trends, alarms, reports | Plant / production manager |
| **Predict** | What will fail or drift? | Vibration, process tags, quality labs | Classical ML, anomaly detection, FMs for TS | Remaining useful life, drift alerts | Reliability / maintenance |
| **Prescribe** | What should we change? | Same + costs, constraints, recipes | Explainable ML, optimization, hybrid models | Setpoint / recipe / work-order recommendations | Process / energy engineer |
| **Act** | Can software write safely? | DCS/APC interfaces, safety envelopes | RL / MPC / supervised closed-loop | Setpoint writes within limits | Controls / APC |
| **Agentic** | Who/what executes across systems? | Tools (CMMS, MES, OPC write, email) + policies | LLM agents + planners + HITL gates | Multi-step workflows with audit | Digital / ops excellence |

**Stamped rule:** Sell Level 2–3 (prescribe + HITL act) first. Climb to Level 4 only with controls partners and envelopes.

---

## 2. Industrial data fabrics / knowledge graphs

### What problem they solve
Raw tags (`TI-401.PV`) are meaningless until joined to a heat exchanger on a P&ID, a pump, a work order in SAP, and a tariff schedule. **Contextualization** builds that join graph once so every app reuses it.

### How it works (plain English)
1. Ingest OT time series (historians), documents (P&IDs, manuals), engineering models (3D, ISA-95), and IT transactions (ERP/CMMS/LIMS).
2. Extract entities and relationships into a **knowledge graph** or **ontology**.
3. Serve contextualized views and APIs to analytics, ML, and agents.
4. Optionally add generative search / copilots over the graph (Cognite Atlas AI narrative; Palantir AIP).

### Who sells this
- **Cognite Data Fusion** — industrial DataOps + knowledge graph; Schneider agreed ~$3.1B acquisition (Jun 2026, not closed as of late Sep 2026 press tracking). ~$170M 2025 revenue cited by Reuters/Schneider. https://www.cognite.com/ · https://www.reuters.com/business/schneider-electric-buy-ai-software-firm-cognite-31-billion-2026-06-30/
- **Palantir Foundry** — ontology + ops apps; manufacturing module; Panasonic Energy NA multi-year agreement. https://www.palantir.com/explore/foundry-for-manufacturing/
- **C3 AI** — enterprise AI apps on a model-driven platform; FY2026 revenue $250.3M (company PR, year ended Apr 30, 2026). https://www.c3.ai/
- **HighByte Intelligence Hub** — industrial DataOps / Unified Namespace for edge contextualization. https://www.highbyte.com/
- **Huawei iDME.X** — industrial data modeling + digital thread (China stack). Huawei Industrial Intelligence materials 2025.

### Pricing (when public)
Usually enterprise subscription + professional services. Exact list prices **Not disclosed publicly** for Cognite/Palantir/C3.

### Stamped implication
Do **not** build a Cognite. Build a **lightweight asset graph**: Site → Area → Line → Asset → Meter → Product → Tariff → Shift. That graph is the Energy/Process join key.

---

## 3. Time-series & tabular foundation models for OT

### Classical methods that still win
- Gradient boosting (XGBoost/LightGBM) on engineered features for energy drivers, yield, fault codes.
- Regime detection (clustering / HMMs) for grade changes and campaign modes.
- Soft sensors: infer hard-to-measure quality from easy tags.

### Foundation-model class (study carefully)
- **TimesFM** (Google Research): pretrained time-series FM; TimesFM-3 pushes multivariate / covariate-aware zero-shot forecasting. Useful as a strong baseline for load/demand/sensor forecasts—then condition with plant covariates. https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/
- **TabPFN-class**: strong on small tabular datasets (common when failure labels are scarce). Literature discusses time-series adaptations; **task-dependent**, not automatic replacement. arXiv discussions e.g. https://arxiv.org/html/2501.02945v3
- **SUPCON TPT / TPT2**: industrial time-series pretrained transformer + agentic orchestration for process industries; vendor case claims on chlor-alkali energy intensity and ethylene optimization. https://global.supcon.com/digital/tpt

### Founder bake-off rule
Always compare: LightGBM vs TimesFM (or vendor FM) vs hybrid on *your* KPI with an M&V plan. FMs reduce cold-start; physics + regimes + labels decide ROI.

### Stamped Energy use
- Forecast plant load / ToD cost exposure.
- Detect non-routine events that invalidate baselines (IPMVP).
- Soft-sense missing submeter streams.

### Stamped Process use
- Predict cycle-time / tool-wear drivers from machine + process features.
- Regime-aware recommendations (don’t optimize across a tool change as if continuous).

---

## 4. Physics-informed ML / hybrid twins

### Plain English
Pure black-box ML will happily learn a drifting meter or an instrument bias. Hybrid methods constrain learning with **mass/energy balances, thermodynamics, machine-tool dynamics, compressor maps**.

### Patterns
1. **Residual learning:** physics baseline + ML residual.
2. **Soft sensors:** infer quality from easy sensors + first principles.
3. **Hybrid process models:** Aspen Hybrid Models (first principles + data + expertise) inside Aspen Plus/HYSYS class tools. https://www.aspentech.com/en/solutions/aspen-hybrid-models/
4. **PINNs / constrained opt:** research → selective production use.
5. **Digital twin simulation for counterfactuals:** Fero Simulator class; PhysicsX simulation AI.

### Who productizes this
- **Basetwo** — low-code physics AI / digital twins for pharma/chem; Series A $11.5M USD. https://www.basetwo.ai/
- **PhysicsX** — physics AI for engineering/manufacturing simulation; press: $300M Series C (Temasek-led) — **press-reported**. https://www.physicsx.ai/
- **AspenTech / Emerson** — Hybrid Models in process engineering suite; Emerson Software & Control sales disclosed at group level (Aspen inside Emerson).
- **LTTS EnergiSensEI** — “verify physics before AI” for energy/sustainability. https://www.ltts.com/solutions/EnergiSensEI

### Stamped implication
For Energy: meter reconciliation + energy balance before learning. For Process: one unit operation with visible constraints before horizontal claims.

---

## 5. World models / physical AI for factories

### Terminology discipline
| Term | Careful meaning | Abuse |
|---|---|---|
| Digital twin | Engineered structure + live data for a specific asset/process | Calling any dashboard a twin |
| World model | Learned dynamics enabling prediction & planning from multimodal observation | Equating world model = 3D CAD |
| Physical AI | AI coupled to sensing/actuation in the physical world (NVIDIA/Foxconn narratives) | Marketing synonym for “AI” |

### Who pushes the narrative (2025–2026)
- **Noetive** — “Intelligence of Record”; world models + agents + multimodal sensing pods; $41M seed (Eclipse-led, Sep 2026). Early; design partners claimed in mfg/logistics/energy/DCs. https://noetive.ai/news/noetive-emerges-from-stealth-with-41-million-seed
- **Bright Machines** — software-defined electronics manufacturing; Factory Intelligence data loop; $126M Series C (Jun 2024); >$400M total raised (**vendor PR**). https://www.brightmachines.com/
- **Haier COSMOPlat / Tianzhi** — industrial large model + world-model / agent cluster narratives at WAIC (Chinese press 2025–2026). https://www.cosmoplat.com/
- **Foxconn + NVIDIA** — digital twins / physical AI factory blueprints (NVIDIA case studies; Hon Hai press). 

### Stamped implication
**Study, don’t chase.** Capital intensity (sensing pods, robotics) is wrong for Stamped’s India wedge until Energy/Process KPI engines work.

---

## 6. Agentic industrial copilots (majors)

### What they actually are
LLM-powered assistants that sit on engineering tools, APM systems, or shopfloor apps. Typical skills: explain alarms, draft work orders, generate PLC/HMI snippets, summarize manuals, suggest maintenance actions. **Most are advisory (Level 1–2)** with HITL; “agentic factory” narratives (Rockwell×Microsoft, Siemens) are climbing toward multi-step tool use.

### Named programs (public)
- **Siemens Industrial Copilot** — engineering/ops/maintenance; Senseye-linked maintenance offering (Siemens press Mar 2025 narrative). https://press.siemens.com/
- **ABB Genix Copilot** — GenAI on Genix APM; alert prioritization, RCA, NL interaction. https://new.abb.com/process-automation/genix/abb-genix-copilot
- **Schneider + Microsoft Industrial Copilot** — EcoStruxure Automation Expert integration narratives (Automate 2025 PR).
- **Rockwell + Microsoft** — FactoryTalk Design Studio Copilot; shared agentic factory engineering vision (Rockwell press).
- **Microsoft Azure** — industrial copilots / factory agents as substrate; Bright Machines collab.

### Stamped implication
Majors own the agent *runtime* in large accounts. Stamped should expose **actions as tools** (CMMS ticket, energy prescription, PE freeze package) rather than rebuild the OS.

---

## 7. Closed-loop APC / RL / optimization on process units

### Map → Model → Control (Imubit pattern)
1. **Map:** understand unit constraints, existing APC/DCS, economic objective.
2. **Model:** nonlinear plant model (guided by first principles + data).
3. **Control:** RL / optimization writes setpoints **through** existing DCS/APC within safety envelopes.

Imubit markets this as Closed-Loop Physical AI for refining, cement, chemicals; vendor claims include energy/fuel intensity reductions — **vendor-claimed**. https://imubit.com/

### Classical APC still matters
MPC (Aspen DMC, Honeywell Profit Controller class) remains the installed-base control layer. New AI often rides on top rather than replacing DCS.

### SUPCON TPT2 vendor case claims (process AI)
From SUPCON global product page (vendor-claimed):
- Chlor-alkali: ≈5% electrolyzer specific energy reduction; membrane life prediction accuracy 95%.
- Ethane-to-ethylene: abnormal event prediction 99.79% accuracy; furnace start-up heating time −4–5 hours.
Source: https://global.supcon.com/digital/tpt

### Stamped implication
Process product should stop at **Model + Prescribe + HITL** until a controls partner owns writeback. Energy product should almost never write DCS setpoints by default.

---

## 8. Edge AI + sensors for PdM

### Data path
Piezo / MEMS vibration + temperature (+ sometimes ultrasonic/oil) → edge inference → cloud fleet models → work orders.

### Players
- **Augury** — Machine Health + Process Health; $75M funding Feb 2025 at $1B+ valuation (**company/TechCrunch**). https://www.augury.com/
- **Infinite Uptime** — India-origin; ~800 plants / ~30 countries; Series C $35M; ~$65M total (**TechCrunch Mar 2025**). https://techcrunch.com/2025/03/10/infinite-uptime-bags-35m-to-help-factories-optimize-equipment-usage/
- **Nanoprecise** — Energy-Centered Maintenance; Series C $38M USD equity+debt (**company PR Mar 2025**). https://nanoprecise.io/
- **Senseye** — software PdM; Siemens-owned since 2022.

### Stamped implication
**Out of product scope** (vision v0.3). Study only for GTM lessons and energy co-benefit narratives (Nanoprecise ECM, Infinite Uptime energy-per-ton comments).

---

## 9. Energy intensity / M&V / bill defence AI

### Plain English KPI stack
1. **Technical efficiency:** kWh/ton, Nm³/ton, specific steam (SEC / EnPI).
2. **Cost efficiency:** ₹/unit after ToD, demand charges, DG vs grid, open access.
3. **Verified savings:** IPMVP Options A–D with baseline, adjustments, non-routine events. https://www.evo-world.org/en/products-services-mainmenu-en/protocols/ipmvp

### What good Energy AI does
- Reconcile meter hierarchy (children sum ≈ parent).
- Detect waste regimes (idle load, simultaneous heating/cooling, compressed-air leaks as energy signatures).
- Prescribe actions with ₹ impact and owner role.
- Produce CFO-signable M&V packs quarterly.
- Optionally optimize source mix / renewables / demand charges (**bill defence**).

### Peers
- **Greenovative** — prescriptive industrial energy intelligence; HW-agnostic claim; vendor: 200+ facilities. https://greenovative.com/
- **ZeroWatt** — AI energy brain; HW at cost + SaaS metering points; press: 100+ factories / 120 MW+ load. https://zerowatt.energy/
- **LTTS EnergiSensEI** — verify physics before AI. https://www.ltts.com/solutions/EnergiSensEI
- **Schneider / AVEVA energy mgmt** — enterprise energy + industrial software mega-stack (with Cognite deal).

### Stamped Energy non-negotiables
1. Meter reconciliation.
2. Production-normalized SEC.
3. Explicit baseline adjustments.
4. Separate avoided cost vs technical efficiency.
5. Customer-signable M&V one-pager.

---

## 10. CAM / CNC programming AI (discrete Process adjacent)

### What they sell
AI that reduces programming time or improves feeds/speeds/toolpaths inside CAM suites (Fusion, Mastercam, NX) or via shop-floor closed loop.

### Players
- **CloudNC** — CAM Assist; 1,000+ shops claimed; Series B history + $20M (Sep 2026 press). https://www.cloudnc.com/ · https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/
- **Productive Machines / SenseNC** — physics-based chatter / feed-speed optimization. https://solutions.productivemachines.co.uk/
- **Lambda Function** (India) — AI CAM + shop-floor sensing for autonomous precision machining. https://www.lambdafunction.ai/
- **Toolpath** — AI CAM assist (US). https://www.toolpath.com/

### Stamped Process mapping
These are **adjacent**, not the core offer. Stamped Process sells **manufacturing engineering outcomes + freeze + implementation path** (tooling where needed), not a CAM seat. Learn their data objects (features, tools, stock, machine capability) for the PE reasoning kernel.

---

## 11. Hyperscaler industrial data planes (brief)

| Vendor | Offer | Role vs Stamped |
|---|---|---|
| **Microsoft Fabric + Azure IoT** | Lakehouse + IoT Ops + copilots | Common substrate; partner |
| **AWS IoT SiteWise** | Industrial data collection / modeling | Data plane option |
| **Google Manufacturing Data Engine** | Manufacturing data unification patterns | Less India default than Azure |
| **Databricks** | Lakehouse + ML for mfg analytics | Common custom-app plane |

Stamped apps should be **portable** across customer-chosen clouds where possible; do not bet the company on one hyperscaler.

---

## 12. Autonomy ladder (use in every customer conversation)

0. Describe — dashboards, search over tags.  
1. Diagnose — root-cause suggestions.  
2. Prescribe — concrete setpoint / work-order recommendations with evidence.  
3. HITL act — human approves; system writes to CMMS/MES or checklist.  
4. Supervised closed-loop — writes within envelopes via APC/DCS.  
5. Broad autonomy — multi-system agents (majors’ aspiration).

**Stamped default:** live at 2–3; design for 4 without shipping 4 prematurely.

---

## 13. Edge vs cloud / air-gap / China on-prem norms

| Pattern | When | Notes |
|---|---|---|
| Cloud SaaS | Multi-site Energy analytics | Common India mid-market with IT approval |
| Edge gateway | Protocol translation, buffering, local inference | Required for flaky WAN / high-rate sensors |
| On-prem / private cloud | Pharma, defense, many China plants | Longer sales; same product, different deploy |
| Air-gap | No outbound | Rare for Energy SaaS; possible for Process on DCS DMZ |

**China note:** Industrial AI often assumes **data localization / on-prem or private cloud**. Western SaaS narratives undersell this. See China annex.

---

## Source appendix (this annex)

- Cognite / Schneider Reuters: https://www.reuters.com/business/schneider-electric-buy-ai-software-firm-cognite-31-billion-2026-06-30/
- Cognite PR: https://www.cognite.com/en/company/newsroom/schneider-electric-announces-agreement-to-acquire-cognite
- C3 AI FY2026 results: https://www.c3.ai/news/c3-ai-announces-fiscal-fourth-quarter-and-full-fiscal-year-2026-results
- TimesFM-3: https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/
- SUPCON TPT2: https://global.supcon.com/digital/tpt
- Noetive seed: https://noetive.ai/news/noetive-emerges-from-stealth-with-41-million-seed
- Bright Machines Series C: https://www.prnewswire.com/news-releases/bright-machines-raises-126m-series-c-funding-to-propel-manufacturing-into-software-defined-era-302181151.html
- Augury $75M: https://techcrunch.com/2025/02/19/augury-raises-73m-on-a-1b-valuation-for-ai-to-detect-malfunctions-in-factory-machines/
- Infinite Uptime: https://techcrunch.com/2025/03/10/infinite-uptime-bags-35m-to-help-factories-optimize-equipment-usage/
- Nanoprecise Series C: https://nanoprecise.io/blog/nanoprecise-closes-38m-usd-series-c-fundraise/
- Basetwo Series A: https://www.basetwo.ai/announcements/basetwo-raises-11-5m-series-a-to-transform-chemical-manufacturing-with-physics-ai-platform
- CloudNC $20M: https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/
- IPMVP: https://www.evo-world.org/en/products-services-mainmenu-en/protocols/ipmvp
- Aspen Hybrid Models: https://www.aspentech.com/en/solutions/aspen-hybrid-models/
- ABB Genix Copilot: https://new.abb.com/process-automation/genix/abb-genix-copilot
- Palantir mfg: https://www.palantir.com/explore/foundry-for-manufacturing/
- Panasonic–Palantir: https://na.panasonic.com/news/palantir-and-panasonic-energy-of-north-america-sign-multi-year-agreement

---
*End of Tech Approaches annex.*


---

## 14. Worked example — Stamped Energy data path (cement mill sketch)

1. **Meters:** HT feeder, mill motor kWh, separator fan, baghouse, compressor house.  
2. **Production:** tons/hour from weigh feeder / MES.  
3. **Context graph:** Site→Kiln line→Cement mill CM-1→Motors→Meters→Tariff (ToD)→Product grade.  
4. **Hygiene:** Sum of sub-meters ≈ feeder (±tolerance); flag frozen meters; weather/production adjust.  
5. **Model:** Regime detect (empty running vs grinding); LightGBM/TimesFM hybrid for expected kWh/ton.  
6. **Prescribe:** “Reduce idle run 14 min/shift on CM-1 → est. ₹X/month”; owner = electrical + production.  
7. **HITL:** Ticket in CMMS / WhatsApp approve → operator checklist.  
8. **M&V:** IPMVP Option B/C style pack quarterly — baseline vs reporting, adjustments explicit.

## 15. Worked example — Stamped Process freeze package (precision part sketch)

1. **Inputs:** Drawing + tolerance stack; machine capability; current tooling list; historical cycle/scrap.  
2. **Reasoning:** Feature→operation sequence hypotheses; tool choice; speeds/feeds envelopes; fixturing notes.  
3. **Evidence:** Comparable past jobs; chatter risk flags (physics if available); cost per accepted part estimate.  
4. **Human freeze:** PE approves operations + tooling list.  
5. **Implementation path:** Tooling lead times / suppliers; CAM handoff (may use CloudNC-class assist as tool, not as product).  
6. **Measure:** Cycle time, scrap, tool life vs baseline job.

## 16. Anti-patterns (say out loud in sales training)

- “We’ll replace your SCADA.”  
- “Our AI saved 20%” without M&V boundary.  
- “World model” without state-transition eval.  
- “Process optimisation” that means inventory or labour.  
- Closed-loop demo on a customer DCS without envelopes and customer control ownership.
