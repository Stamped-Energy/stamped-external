# Factory Intelligence: Global Market Map & Tech Study
**Prepared for:** Vinayak Raizada — Stamped (India industrial AI)  
**Context:** Advisor brief from Vaibhav (Together Fund) — study every serious factory-intelligence company and understand the tech  
**Date:** 2026-09-22 (IST)  
**Method:** WebSearch + WebFetch; vendor/press claims flagged; no invented stats  
**Scope:** ~30 named companies across 8 archetypes + teachable tech curriculum + Stamped implications

---

## 1. Executive briefing for Stamped

### What “factory intelligence” actually is
Factory intelligence is **not one product**. It is a stack of capabilities that turn plant OT/IT data into decisions that change cost, yield, energy, quality, or uptime. Serious players specialize in different layers:

| Layer | Question answered | Typical buyer |
|---|---|---|
| **Connect & contextualize** | Can we trust and join the data? | CIO / OT architect |
| **See** | What is happening / happened? | Plant / production manager |
| **Predict** | What will fail or drift? | Reliability / maintenance |
| **Prescribe** | What should we change? | Process / energy engineer |
| **Act (closed-loop)** | Can software write setpoints safely? | Controls / APC / ops |
| **Orchestrate (agents)** | Who/what executes across systems? | Digital / ops excellence |

Stamped’s two surfaces map cleanly onto this stack:
- **Stamped Energy** → energy/resource **decision layer** (prescribe + prove savings; adjacent to Greenovative, ZeroWatt, LTTS EnergiSensEI, Nanoprecise’s energy angle).
- **Stamped Process** → manufacturing **process engineering outcomes** (prescribe/optimize process, recipes, setpoints; adjacent to Fero Labs, Basetwo, Imubit, Sight Machine’s optimization layer).

### Naming clarification (important)
Vaibhav’s “Bright AI” almost certainly refers to **Bright Machines** (San Francisco; software-defined manufacturing + Factory Intelligence layer)—**not** a separate “Bright AI” world-model company. The closest public “world model for factories” stealth narrative in 2026 press is **Noetive** (emerged Sep 2026, $41M seed, “intelligence of record” / world models + sensing pods). Treat “Bright AI” as a spoken shorthand; in decks, say **Bright Machines** and **Noetive** separately.

### Market structure in one monologue
1. **Hyperscalers & industrial majors** (Siemens, Rockwell, ABB, Microsoft, Schneider/AVEVA+Cognite) own the installed base and are racing to agentic copilots. They win long, deep accounts; they are slow and often advisory-first.
2. **Industrial data platforms** (Cognite, C3 AI, Palantir Foundry, Databricks manufacturing patterns) sell the **data foundation**—contextualization, knowledge graphs, app platforms. Cognite’s agreed ~$3.1B acquisition by Schneider (Jun 2026, press) is a category-defining signal that **data fabric + industrial AI** is strategic M&A, not niche SaaS.
3. **Outcome specialists** win when they own a KPI: uptime (Augury, Infinite Uptime, Nanoprecise), OEE/visibility (Sight Machine, MachineMetrics, Tulip), process margin (Imubit, Fero, Basetwo), CNC programming (CloudNC, Lambda Function, Productive Machines), energy intensity (Greenovative, ZeroWatt, EnergiSensEI).
4. **Physical-AI / world-model startups** (Noetive, Bright Machines’ physical AI stack, PhysicsX for simulation, Arrakis as FDE-led industrial OS) are the 2024–2026 narrative shift: from dashboards → models that **observe, reason, and eventually act**.

### India / India-relevant reality check
- **Energy comps (known):** Greenovative (Pune; enterprise energy intelligence, vendor: 200+ facilities / 80+ industry leaders claims), ZeroWatt (IITM Research Park / Trivandrum roots; vendor: 100+ factories, ~120 MW connected load in earlier press).
- **PdM scale from India:** Infinite Uptime (TechCrunch Mar 2025: ~800 plants, ~30 countries, Series C $35M, ~$65M total reported).
- **OEM/group activity:** TVS / TVS Next talking “manufacturing intelligence orchestration”; Honda India digital manufacturing partnerships (Infosys and others in public case studies); Adani/Reliance-type accounts often go through **Honeywell / majors / SI** stacks rather than pure startups—treat as **deployment theaters**, not single-vendor wins.
- Comps “talking to Honda/TVS” is a common India GTM pattern: automotive discrete + tier-1s are high-signal design partners for Process; energy-intensive process (cement, metals, chemicals) for Energy.

### Stamped’s strategic frame (before you dive dossiers)
| Do | Don’t |
|---|---|
| Own a **verifiable KPI** (₹/unit energy, specific energy consumption, yield, first-pass quality, changeover loss) | Sell “AI platform for factories” without a vertical wedge |
| Lead with **physics + data hygiene + M&V** (see EnergiSensEI’s thesis) | Train models on unclean meters and claim savings |
| Stay **recommend → HITL → optional closed-loop** | Jump to autonomous setpoint writing without controls partnership |
| Study Imubit/Fero for Process closed-loop vs white-box; study Greenovative/ZeroWatt/LTTS for Energy GTM | Copy Bright Machines’ robotics stack (wrong capital intensity for Stamped’s wedge) |
| Treat Cognite/Palantir as **partners or “data layer above you”**, not as peer competitors for mid-market India plants | Pretend you will displace Siemens/Rockwell/SCADA |

---

## 2. Market map by archetype

**Legend:** H = heavy hardware, S = software-primary, H+S = mixed. Funding/scale = **vendor or press-reported only**.

### A. Factory world models / plant digital brains / physical AI
| Company | What | H/S | Relevance to Stamped |
|---|---|---|---|
| **Bright Machines** | Software-defined manufacturing; Bright Factory = design twin + robotics + Factory Intelligence data layer; AI hardware assembly niche | H+S | Process-adjacent (execution/automation); **not** Energy. Study their data-feedback loop, not robots. |
| **Noetive** | “Intelligence of record” for physical economy; world models + agents + multimodal sensing pods; design partners in mfg/logistics/energy/DCs | H+S | Closest public “factory world model” narrative. Study architecture claims carefully—early. |
| **Zentio** | “Agentic twin” for high-mix manufacturing: live model + scheduling/planning agents | S | Process / scheduling; less Energy. |
| **PhysicsX** | Physics-informed AI + simulation for engineering/manufacturing/process | S | Process deep-tech; simulation hybrid methods. |
| **Prometheus** (prometheusenergy.ai) | First-principles global optimization for refining/chemicals/blending multi-period plans | S | Process / energy-in-process; heavy industry planning. |

### B. Industrial data platforms
| Company | What | H/S | Relevance |
|---|---|---|---|
| **Cognite (CDF)** | Industrial DataOps + knowledge graph; IT/OT/ET contextualization; agentic push (Atlas AI); Schneider agreed acquisition ~$3.1B (Jun 2026) | S | **Foundation layer.** Stamped apps may sit on or beside this in large accounts. |
| **C3 AI** | Enterprise AI applications (incl. manufacturing/process/APM suites) | S | Compete/partner on enterprise AI apps; heavy enterprise sales. |
| **Palantir Foundry** | Ontology + ops apps; manufacturing/battery plant deployments (e.g. Panasonic Energy press) | S | Enterprise “digital twin of the enterprise”; rare mid-market India fit alone. |
| **Databricks (mfg patterns)** | Lakehouse + governed ML for manufacturing analytics | S | Common data plane under custom industrial apps. |

### C. Predictive / prescriptive maintenance
| Company | What | H/S | Relevance |
|---|---|---|---|
| **Augury** | Machine health (vibration/acoustic/thermal) + Process Health (Seebo); industrial AI agents; large CPG references (e.g. PepsiCo success story) | H+S | Process + reliability; energy secondary. |
| **Infinite Uptime** | Sensors + edge AI PdM for heavy industry; India-origin scale play | H+S | Strong India peer; uptime KPI; energy co-benefit claims. |
| **Nanoprecise** | Multi-parameter sensors + AI; **Energy-Centered Maintenance** thesis; Series C $38M (Mar 2025 press) | H+S | **Energy + PdM overlap**—study carefully for Stamped Energy adjacency. |
| **Senseye** (Siemens) | Software PdM; acquired by Siemens (2022) | S | Embedded in Siemens industrial AI portfolio. |

### D. Manufacturing intelligence / OEE / visibility
| Company | What | H/S | Relevance |
|---|---|---|---|
| **Sight Machine** | Plant data model / digital twin of production; OEE + AI optimization | S | Process visibility → optimization path. |
| **Tulip** | No-code frontline ops / apps / connected worker; $100M Series C (press) | S | Shop-floor UX; not Energy core. |
| **MachineMetrics** | Machine connectivity, OEE, MES-ish analytics for discrete/CNC | H+S (connectors) | Discrete Process; CNC adjacency. |
| **TrendMiner** | Self-service process time-series analytics; acquired by Proemion (2024) | S | Process historian analytics; engineer self-serve. |

### E. Process / recipe optimization
| Company | What | H/S | Relevance |
|---|---|---|---|
| **Fero Labs** | White-box / explainable ML for process diagnostics, simulation, live production; steel/chem/cement/CPG | S | **Core Stamped Process peer.** |
| **Basetwo** | Low-code physics-informed AI / digital twins for pharma/chem; Series A ~$11.5M USD / ~C$16.5M press | S | Physics+ML hybrid—study method. |
| **Imubit** | Closed-loop Physical AI; RL controllers writing through DCS/APC; refining/cement/chemicals | S | **Gold standard closed-loop Process.** Study Map→Model→Control. |

### F. CNC / CAM process AI
| Company | What | H/S | Relevance |
|---|---|---|---|
| **CloudNC** | CAM Assist AI programming; 1,000+ shops claimed; Autodesk-linked Series B history; additional $20M (Sep 2026 press) | S | Discrete Process niche (programming time). |
| **Productive Machines** | SenseNC—physics-based chatter/feed/speed optimization | S | Process physics at machine tool. |
| **Lambda Function** | AI CAM + shop-floor sensing for autonomous precision machining | H+S | Closed-loop machining. |

### G. Energy industrial AI
| Company | What | H/S | Relevance |
|---|---|---|---|
| **Greenovative** | Prescriptive industrial energy intelligence; SCADA/PLC/BMS integrate; source mix, renewables, unit economics, multi-site | S (HW-agnostic claim) | **Direct India Energy comp.** |
| **ZeroWatt** | AI energy intelligence / “digital energy brain”; detect waste + prescribe; HW at cost + SaaS metering points | H+S | **Direct India Energy comp.** |
| **LTTS EnergiSensEI** | Engineering-verified energy & sustainability platform; **verify physics before AI**; agents for optimize/trends/insights/reports | S (+ services) | **Must-study** for M&V & trust thesis. |

### H. Hyperscalers / industrial majors
| Company | What | Relevance |
|---|---|---|
| **Siemens Industrial AI** | Edge, twins, copilots, agentic shopfloor (w/ partners); Senseye inside | Platform gravity; partner/compete |
| **Rockwell** | FactoryTalk + Microsoft agentic factory engineering narratives | Discrete automation stack |
| **Microsoft** | Azure industrial / factory agents / copilots; Bright Machines collab | Cloud + agent fabric |
| **ABB Genix** | OT/IT/ET analytics + Genix Copilot (Azure OpenAI narratives) | Process industries |
| **Schneider + AVEVA + Cognite** | Energy mgmt + industrial software + data fabric consolidation | Energy + data platform mega-stack |

### I. Stealth / notable 2024–2026 factory AI (verified in press)
| Company | Signal |
|---|---|
| **Noetive** | Sep 2026: $41M seed (Eclipse-led); world models / IoR for physical ops |
| **Arrakis** | 2026: ~$38M total (Accel seed + Blossom Series A); FDE-led industrial AI OS; London/Paris |
| **Zentio** | Agentic twin for high-mix mfg (public product site) |
| **PhysicsX** | Large 2025/26 funding narrative for physics AI simulation (press cites ~$300M / multi-B valuation—treat as press-reported) |

**Skipped / not confirmed as distinct “Bright AI” entity:** No credible separate company named exactly “Bright AI” matching Vaibhav’s description beyond Bright Machines. Stealth “world model for factories” → prioritize **Noetive** in reading list.

---

## 3. Company dossiers (compact)

*All $ / customer / % figures are vendor- or press-reported unless noted. Verify before investor use.*

### 3.1 Bright Machines
- **Sells:** Bright Factory—virtual product development (Bright Designer), AI robotics (Smart Skills), Factory Intelligence (Bright Data).
- **ICP:** Electronics / AI infrastructure hardware manufacturing (servers, racks, storage).
- **H/S:** Full-stack hardware + software.
- **Scale/funding:** Series C $126M (Jun 2024 press; BlackRock-led + NVIDIA, Microsoft, etc.); total raised >$400M (company PR).
- **Diff:** Software-defined assembly + design-for-automation + production data loop; NVIDIA Omniverse / Azure partnerships.
- **Stamped:** Study **data closed loop** (design↔build↔optimize). Avoid copying robotics CapEx model. Low Energy relevance.

### 3.2 Noetive
- **Sells:** “Intelligence of record”—self-improving AI + world models/agents + multimodal sensing pods.
- **ICP:** Physical economy design partners (mfg, logistics, energy, data centers, construction).
- **H/S:** Software brain + sensing hardware.
- **Funding:** $41M seed (Sep 2026; Eclipse-led) — press.
- **Diff:** Explicit **world-model** positioning vs copilots; sensing where data never hits MES/ERP.
- **Stamped:** Watch narrative & architecture; too early to copy. Relevant to both Energy and Process as long-horizon competitor archetype.

### 3.3 Cognite
- **Sells:** Cognite Data Fusion—industrial DataOps, knowledge graph, contextualized IT/OT/ET; industrial tools + agentic AI (Atlas AI).
- **ICP:** Asset-intensive (energy, process, manufacturing); named historical customers include bp, Saudi Aramco, Celanese, etc. (company materials).
- **Funding / M&A:** Unicorn round $150M / $1.6B val (2021); Schneider definitive agreement to acquire for **$3.1B** (Jun 30, 2026 press); ~$170M 2025 revenue cited in Reuters coverage.
- **Diff:** First-mile industrial contextualization at scale.
- **Stamped:** Not a peer for SMB India plants; in large accounts CDF may be the data plane your app plugs into.

### 3.4 C3 AI
- **Sells:** Enterprise AI application suite (APM, process, inventory, etc.).
- **ICP:** Large global industrials / materials / process.
- **Diff:** Packaged AI apps + enterprise sales motion.
- **Stamped:** Benchmark enterprise packaging; avoid competing on “platform” messaging.

### 3.5 Palantir Foundry (industrial)
- **Sells:** Ontology-centric operating system for data + decisions; manufacturing modules.
- **Customers:** Panasonic Energy NA multi-year agreement (press); other large industrials.
- **Stamped:** Learn ontology/contextualization ideas; GTM is out of band for early Stamped.

### 3.6 Augury
- **Sells:** Asset Health + Process Health; sensors + AI + agents.
- **ICP:** Large manufacturers / CPG (PepsiCo public story).
- **Funding:** Press/LinkedIn aggregates cite ~$369M total incl. $75M (2025) at $1B+ valuation—**vendor/press**.
- **Stamped:** Process + reliability peer; Energy only as side effect of healthier machines.

### 3.7 Infinite Uptime
- **Sells:** Proprietary sensors + analytics + AI diagnostics; outcomes-as-a-service narrative.
- **ICP:** Steel, cement, metals, mining, fertilizers, chemicals, paper.
- **Scale/funding:** TechCrunch (Mar 2025): Series C $35M; ~$65M total; **~800 plants / ~30 countries** (company via press).
- **Stamped:** India-origin scale proof for industrial AI; PdM wedge ≠ Stamped Energy wedge, but GTM lessons transfer.

### 3.8 Nanoprecise
- **Sells:** IoT sensors + AI diagnostics; Energy-Centered Maintenance.
- **ICP:** O&G, chemicals, automotive, CPG, manufacturing (Fortune 500 claims).
- **Funding:** Series C $38M USD equity+debt (Mar 2025 PR).
- **Stamped:** Closest PdM player to **Energy thesis**—study ECM framing.

### 3.9 Senseye (Siemens)
- **Sells:** Software PdM; now Siemens Industrial AI portfolio piece.
- **Stamped:** Example of startup → major absorption path.

### 3.10 Sight Machine
- **Sells:** Manufacturing data platform / production digital twin; OEE + optimization.
- **Funding:** PitchBook/Tracxn aggregates vary (~$85M–$148M)—**databases disagree; flag as unverified to exact**.
- **Stamped:** Process visibility → AI optimization path.

### 3.11 Tulip Interfaces
- **Sells:** No-code frontline manufacturing apps / connected worker.
- **Funding:** $100M Series C led by Insight (company press).
- **Stamped:** UX for operators; complement not Energy/Process core AI.

### 3.12 MachineMetrics
- **Sells:** Machine data platform, OEE, production analytics for discrete.
- **Funding:** Series A $11.3M; Series B $20M (2021 BusinessWire).
- **Customers (historical press):** Fastenal, Snap-on, Continental, etc.
- **Stamped:** Discrete machine connectivity patterns.

### 3.13 TrendMiner
- **Sells:** Self-service advanced analytics on process time-series.
- **M&A:** Acquired by Proemion Holding (Apr 2024 press).
- **Stamped:** How process engineers want to explore historian data.

### 3.14 Fero Labs
- **Sells:** Diagnostics, Simulator, Production, Foundation—explainable process ML.
- **ICP:** Steel, chemicals, O&G, cement, CPG; named references in press include Gerdau, Covestro, Volvo, CELSA (earlier PR narratives).
- **Funding:** Climate Investment / PR: $15M round; CB Insights-style aggregates ~$30M total—**press**.
- **Stamped:** **Primary Process study object**—white-box, engineer-in-control.

### 3.15 Basetwo
- **Sells:** Low-code physics AI / digital twins / copilots for process industries.
- **ICP:** Pharma, chemical, personal care (company).
- **Funding:** Series A $11.5M USD / C$16.5M (company/BetaKit).
- **Stamped:** Physics-informed modeling curriculum.

### 3.16 Imubit
- **Sells:** Closed-Loop Physical AI—Map → Model → Control; RL through existing DCS/APC.
- **ICP:** Refining, cement, chemicals; named logos/quotes: Citgo, Ash Grove, Monroe Energy, Preem, etc. (site).
- **Claims (vendor):** 100+ closed-loop apps; 15–30% NG usage reduction; yield/margin stats on site.
- **Funding:** Earlier press cited ~$50M raised—**verify if citing externally**.
- **Stamped:** **How closed-loop Process is done safely.** Energy relevance via fuel/utility intensity in process units.

### 3.17 CloudNC
- **Sells:** CAM Assist (AI toolpaths inside Fusion/Mastercam/NX); expanding quoting agents.
- **Scale:** 1,000+ machine shops (company); Lockheed etc. in press.
- **Funding:** Series B $45M (2022 Autodesk-led); additional $20M (Sep 2026 TechCrunch/TNW).
- **Stamped:** Discrete Process AI wedge example (time-to-program KPI).

### 3.18 Productive Machines
- **Sells:** SenseNC—physics-based CNC stability / feed-speed optimization.
- **Funding:** Small UK deeptech rounds (Catapult / Innovate UK press)—early stage.
- **Stamped:** Physics-first machine process optimization.

### 3.19 Lambda Function
- **Sells:** Autonomous precision machining—AI CAM + load/vibration/tool-life closed loop.
- **Stamped:** Closed-loop discrete Process.

### 3.20 Greenovative
- **Sells:** Prescriptive energy intelligence—source cost mix, renewables, capex utilization, production unit economics, enterprise benchmarking.
- **ICP:** Multi-plant industrials; testimonials cite automotive conglomerate, Jotun, cement, LG plant, textiles.
- **Claims (vendor site):** 200+ deployments / 80+ industry leaders; 2–3 week go-live; 12–15% energy cost reduction; <12 month ROI—**vendor**.
- **H/S:** Hardware-agnostic; SCADA/PLC/BMS/IoT.
- **Stamped:** **Closest India Energy competitor to study weekly.**

### 3.21 ZeroWatt
- **Sells:** AI energy & ops intelligence—“digital energy brain”; waste detection + root cause + prescribe; equipment health angle.
- **ICP:** Indian manufacturing groups; energy-intensive facilities.
- **Claims:** YourStory (Jun 2025): bootstrapped by NTPC veterans; **100+ factories**, **120 MW+** load, ~10% average energy reduction, ~78,800 tCO₂/yr avoided—**press/vendor**. Site: 20–30% average annual energy cost reduction; 3–6 month payback—**vendor**.
- **Commercial model (press):** Subscription per metering point; hardware at cost.
- **Stamped:** Alternate India Energy GTM (hardware-assisted, expert-as-software).

### 3.22 LTTS EnergiSensEI
- **Sells:** Energy & sustainability platform with **physics verification before AI**; Assess→Build→Operate→Sustain; five agents (Optimizer, Trends, Insights, Reports, Dashboard).
- **ICP:** Manufacturing, process, utilities; multi-site ESG.
- **Claims (LTTS):** 5–15% energy & water reduction; payback figures vary on page (2–4 yrs / <3.5 yrs); “20+ clients” / “50+ sites” in one block and “1000+ sites” in another—**treat carefully; SI scale may include broader ESG metering programs**.
- **Diff:** Trust / M&V / engineering verification narrative.
- **Stamped:** **Steal the “verify first” doctrine** for Energy credibility with CFOs and plant heads.

### 3.23 Siemens / Rockwell / Microsoft / ABB
- **Siemens:** Industrial Edge, digital twins, Industrial Copilot, agentic shopfloor initiatives; Senseye.
- **Rockwell + Microsoft:** Agentic factory engineering linking twins, automation logic, validation (joint narratives).
- **Microsoft:** Factory operations / safety agents; Azure as industrial AI substrate (Bright Machines collab).
- **ABB Genix:** Unified industrial data + Genix Copilot.
- **Stamped:** These define **procurement reality** in large plants. Position as complementary decision layer, not replacement PLC/DCS/MES.

### 3.24 Arrakis
- **Sells:** AI operating system for industrial companies via forward-deployed engineers; model-agnostic.
- **Funding:** ~$7.5M seed (Accel) + $30M Series A (Blossom, Jul 2026 press); ~$140M post reported.
- **Stamped:** GTM pattern (FDE) vs productized SaaS—decide consciously.

### 3.25 Zentio
- **Sells:** Agentic Twin—live factory model + scheduling/planning/analytics agents.
- **ICP:** High-mix manufacturing; EU data residency emphasis.
- **Stamped:** Process orchestration / scheduling archetype.

### 3.26 PhysicsX
- **Sells:** Physics AI platform for simulation-heavy engineering and process.
- **Stamped:** Method reference for hybrid physics+ML (Process).

### 3.27 Prometheus (AI for manufacturing optimization / energy process planning)
- **Sells:** Globally optimized multi-period plans with first-principles models (refining/chemicals/blending).
- **Stamped:** Planning-layer Process/Energy hybrid.

---

## 4. Tech stack curriculum (study guide)

*Read aloud sections A–H. Goal: Vinayak can teach these without slides.*

### A. OT data path (PLC → SCADA → OPC-UA / MQTT → historians)

**Monologue:**  
“On a plant floor, the truth starts in **PLCs and DCS controllers**—they run real-time loops. Operators see aggregated views in **SCADA/HMI**. To get data out without custom hell, modern plants expose tags via **OPC UA** (rich information model, security, browsing) and/or **MQTT** (often Sparkplug B) into a **Unified Namespace**. Long-lived process data lands in a **historian** (AVEVA PI, Aspen IP.21, Honeywell PHD, open TSDB stacks). IT systems (MES, ERP, CMMS, LIMS) sit beside OT—not instead of it. Factory AI that skips OT literacy fails in week two.”

**Study checklist:**
1. Tag vs asset vs event vs batch genealogy.
2. Sampling: 1 Hz utilities vs 100 ms vibration vs slow lab assays.
3. Clock sync / late data / sensor freeze (EnergiSensEI’s point: meters lie).
4. Air-gapped historians vs cloud brokers (see G).

**Founder exercise:** Draw Stamped Energy’s ingestion for one cement mill: electrical meters → PLC → SCADA → OPC UA → edge buffer → cloud feature store → prescription → HITL ticket in CMMS.

### B. Industrial data fabric / contextualization

**Monologue:**  
“Raw tags are useless. `TI-401.PV` means nothing until linked to a heat exchanger on P&ID line 12, served by pump P-12A, with work orders in SAP and a 3D model. That’s **contextualization**. Cognite-style platforms build an **industrial knowledge graph** joining time series, documents, engineering (ET), and transactions (IT). Palantir calls the governed object model an **ontology**. Without this, every ML project reinvents joins and dies at scale-out to plant 2.”

**Stamped choice:** For India mid-market, you may not sell a Cognite. You still need a **lightweight asset graph**: site → area → line → asset → meter → product SKU → tariff → shift. That graph is your moat.

### C. Classical ML vs foundation models for tabular / time-series

**Classical (still wins often):**
- Gradient boosting (XGBoost/LightGBM) on engineered features for fault codes, energy drivers, yield predictors.
- ARIMA/Prophet-class or state-space for simple forecasts.
- Clustering for regime detection (grade changes, campaign modes).

**Foundation / FM-class (study, don’t worship):**
- **TimesFM** (Google): pretrained time-series FM; TimesFM-3 pushes multivariate / covariate-aware zero-shot forecasting (Google Research blog). Useful as a **strong baseline** for demand, load, sensor forecasts—then fine-tune or feature-condition with plant covariates.
- **TabPFN / TabFM-class:** Strong on **small tabular** datasets (common in industrial failure labels). Research shows TabPFN-v2 variants can compete on some time-series tasks—**task-dependent**, not automatic replacement (arxiv literature).

**Founder rule:** FMs reduce cold-start pain; **physics + regimes + labels** still decide industrial ROI. Always bake-off: LightGBM vs TimesFM vs hybrid on *your* KPI with M&V.

### D. Physics-informed / hybrid models

**Monologue:**  
“Pure black-box ML will happily learn a drifting meter. Hybrid approaches constrain learning with **mass/energy balances, thermodynamics, machine tool dynamics, compressor curves**. Basetwo and PhysicsX productize physics AI; EnergiSensEI verifies readings against engineering physics *before* learning; Productive Machines predicts chatter from physics; Imubit guides nonlinear models with first principles then RL control.”

**Patterns:**
1. Soft sensors (infer hard-to-measure quality from easy sensors + physics).
2. Residual learning (physics baseline + ML residual).
3. PINNs / constrained optimization (research → selective production use).
4. Digital twin simulation for counterfactuals (Fero Simulator class).

### E. Digital twins vs world models (terminology discipline)

| Term | Careful meaning | Abuse to avoid |
|---|---|---|
| **Digital twin** | Synchronized digital representation of a specific asset/process/plant for monitor, simulate, optimize—fidelity varies from dashboard twin → physics twin → control twin | Calling any dashboard a twin |
| **Process digital twin** | Model of unit operations / recipes / material flows | — |
| **Agentic twin** (Zentio usage) | Live ops model **plus** agents that schedule/act | Marketing synonym for “AI” |
| **World model** (Noetive / research sense) | Learned model of environment dynamics enabling prediction & planning from multimodal observation—closer to robotics/RL research than classic CAD twin | Equating world model = 3D factory CAD |

**Monologue:**  
“A digital twin is usually **engineered structure + live data**. A world model is usually **learned dynamics** that let an agent imagine futures. Plants will have both: graphs/twins for truth and audit; learned world models for planning under uncertainty. Don’t sell ‘world model’ until you can show prediction of plant state transitions that beat a twin+optimizer baseline.”

### F. Agentic layers (recommend vs act; HITL; orchestration)

**Autonomy ladder (use this in every customer conversation):**
0. **Describe** — dashboards, search over tags.  
1. **Diagnose** — root cause suggestions (Fero Diagnostics).  
2. **Prescribe** — concrete setpoint / work-order recommendations (Greenovative, EnergiSensEI agents).  
3. **HITL act** — human approves; system writes to CMMS/MES or operator checklist.  
4. **Supervised closed-loop** — writes setpoints within envelopes through APC/DCS (Imubit).  
5. **Broad autonomy** — multi-system agents rescheduling labor/materials/machines (Zentio aspiration; majors’ agentic factory narratives).

**Orchestration:** Agents need tools (OPC write, SAP BAPI, email, CMMS API), memory (asset graph), and **policy** (safety interlocks never bypassed). Microsoft/Siemens/Rockwell are defining enterprise agent runtimes—Stamped should expose **actions as tools**, not rebuild the OS.

### G. Edge vs cloud / air-gap patterns

| Pattern | When | Notes |
|---|---|---|
| **Cloud SaaS** | Multi-site analytics, model training, benchmarking | India plants often OK for Energy with IT approval |
| **Edge gateway** | Protocol translation, buffering, local inference | Mandatory for flaky WAN / high-rate vibration |
| **On-prem / private cloud** | Defense, pharma, some PSU | Longer sales; same product, different deploy |
| **Air-gap** | No outbound; USB/update rituals | Rare for Energy SaaS; possible for Process on DCS DMZ |

**Rule:** Inference for safety-critical closed-loop stays near control network; heavy training and cross-site learning can be cloud if data governance allows.

### H. Verification / M&V for savings claims

**Monologue:**  
“If your Energy product cannot survive an audit, it is a demo. **IPMVP** (Efficiency Valuation Organization) is the global language of energy savings verification: define boundary, baseline, adjustments for production/weather/non-routine events, then Options A–D. AI can help build baselines and detect non-routine events, but **does not replace** an M&V plan.”

**Stamped Energy non-negotiables:**
1. Meter hierarchy + reconciliation (sum of children ≈ parent).
2. Production-normalized SEC (kWh/ton, ₹/unit)—not raw kWh alone.
3. Baseline period vs reporting period with explicit adjustments.
4. Separate **avoided cost** (tariff, ToD, DG vs grid) from **technical efficiency**.
5. Customer-signable M&V one-pager each quarter.

**Why EnergiSensEI’s “verify before AI” matters:** CFOs have been burned by dashboards that “saved 12%” while production mix changed. Your differentiation in India can be **board-defendable savings**, not prettier charts.

---

## 5. What to learn this week (prioritized)

### Day 1–2 — Energy wedge (Stamped Energy)
1. Greenovative site + FAQ (go-live, prescriptions, multi-site): https://greenovative.com/  
2. ZeroWatt site + YourStory profile: https://zerowatt.energy/ · https://yourstory.com/2025/06/zerowatt-energy-ai-efficiency-platform  
3. LTTS EnergiSensEI (verify-first doctrine): https://www.ltts.com/solutions/EnergiSensEI  
4. Skim Nanoprecise ECM / Series C PR (energy×maintenance): https://nanoprecise.io/  

**Monologue goal:** Compare three India/India-relevant Energy approaches—HW-agnostic SaaS (Greenovative), metering-point SaaS+HW (ZeroWatt), SI/engineering-verified platform (LTTS).

### Day 3–4 — Process wedge (Stamped Process)
1. Fero Labs product/method (white-box, engineer control): https://www.ferolabs.com/  
2. Imubit Map→Model→Control (closed-loop): https://imubit.com/  
3. Basetwo physics AI Series A narrative: https://www.basetwo.ai/  
4. Sight Machine (production twin → optimization): https://www.sightmachine.com/  

**Monologue goal:** Explain open-loop prescribe vs closed-loop DCS write; when India plants will accept each.

### Day 5 — Data foundation & agents
1. Cognite Data Fusion + Schneider acquisition signal: https://www.cognite.com/ · Reuters/SE Jun 2026 coverage  
2. Noetive stealth thesis (world model narrative): https://noetive.ai/news/noetive-emerges-from-stealth-with-41-million-seed  
3. Bright Machines platform (Factory Intelligence layer): https://www.brightmachines.com/platform/  

### Day 6 — Tech drills ( Curriculum A, C, H )
1. OPC UA vs MQTT Sparkplug (pick one explainer + draw your plant path).  
2. TimesFM-3 Google Research blog (zero-shot multivariate).  
3. IPMVP overview (EVO): https://www.evo-world.org/en/products-services-mainmenu-en/protocols/ipmvp  

### Day 7 — Synthesis for Vaibhav
Prepare a 10-minute monologue:
1. Market map by archetype (30 seconds each).  
2. Where Stamped Energy and Process sit.  
3. Three companies we’d study weekly for 90 days.  
4. One thing we will **not** build (e.g., robotics stack / full DataOps platform).  
5. Our M&V trust thesis.

---

## 6. Stamped gap analysis vs category leaders

### Relative to Energy leaders (Greenovative, ZeroWatt, EnergiSensEI, Nanoprecise ECM)
| Gap / strength | Implication |
|---|---|
| Leaders already claim fast go-live on existing SCADA/meters | Stamped must match **time-to-first-prescription** (weeks, not months) |
| EnergiSensEI owns **trust/verification** narrative | Copy doctrine; productize meter reconciliation + IPMVP packs |
| ZeroWatt mixes HW + SaaS economics | Decide HW strategy explicitly (agnostic vs selective) |
| Greenovative pushes **enterprise multi-site benchmarking** | Single-plant wizardry won’t win group accounts (Adani-class) |
| Stamped Energy can differentiate on **decision quality tied to process state** (not only utilities) | Energy×Process join is a real wedge if Process product feeds regimes |

### Relative to Process leaders (Fero, Imubit, Basetwo, Sight Machine)
| Gap / strength | Implication |
|---|---|
| Fero: explainability + engineer workflow | Build white-box / constraint-visible recommendations |
| Imubit: closed-loop through APC/DCS | Partner with controls integrators; don’t fake autonomy |
| Basetwo: physics+low-code | Invest in hybrid models for 1–2 processes (e.g., furnace, kiln, curing) before horizontal claims |
| Sight Machine: production data model | You need a clean production event model even if you don’t sell OEE |

### Relative to platforms / majors (Cognite, Siemens, Microsoft, Palantir)
| Gap / strength | Implication |
|---|---|
| They own data planes & control stacks | Stamped = **outcome app** with clean APIs into their fabrics |
| Agentic narratives are noisy | Ship Level 2–3 autonomy with audit trails before “agents run the plant” |
| M&A consolidating (Cognite→Schneider) | Window for independent outcome specialists remains if KPI-owned |

### Relative to world-model / physical-AI narrative (Noetive, Bright Machines)
| Gap / strength | Implication |
|---|---|
| Capital & research intensity high | **Study, don’t chase** until Energy/Process KPI engine works |
| Sensing pods / robotics change CapEx | Stamped’s India GTM prefers software on existing instrumentation first |

### Copy vs avoid (blunt)
**Copy:**
- Verify-before-AI (LTTS).  
- Prescriptive, role-based actions with ₹ impact (Greenovative/ZeroWatt).  
- White-box process diagnostics (Fero).  
- Map→Model→Control discipline (Imubit)—even if you stop at Model+Prescribe initially.  
- Asset graph / contextualization lite (Cognite ideas, smaller scope).  
- M&V / IPMVP packaging.

**Avoid:**
- “Platform for all factory AI” positioning.  
- Robotics / full software-defined factory CapEx (Bright Machines path).  
- Claiming world models without predictive eval harness.  
- Closed-loop writes without safety envelopes and customer control ownership.  
- Unverified % savings in investor materials.

### Suggested 90-day study/build bias
1. **Energy:** one vertical (e.g., automotive discrete utilities **or** cement/metals SEC) + M&V pack + multi-meter reconciliation.  
2. **Process:** one unit operation with explainable setpoint recommendations (open-loop).  
3. **Shared:** plant asset graph + OT connectors (OPC UA/MQTT) + regime detection.  
4. **Park:** agents that write to DCS; world-model research; multi-industry horizontal FM marketing.

---

## 7. Source appendix

### Company / product pages
- Bright Machines platform: https://www.brightmachines.com/platform/  
- Bright Machines home: https://www.brightmachines.com/  
- Cognite Data Fusion: https://www.cognite.com/en/product/cognite_data_fusion_industrial_dataops_platform  
- Cognite TCV round (2021): https://www.cognite.com/en/company/newsroom/cognite-secures-150-million-investment-from-tcv-to-acceleratedigitalization-of-global-industries  
- Schneider–Cognite agreement: https://www.cognite.com/en/company/newsroom/schneider-electric-announces-agreement-to-acquire-cognite · https://www.reuters.com/business/schneider-electric-buy-ai-software-firm-cognite-31-billion-2026-06-30/  
- Greenovative: https://greenovative.com/  
- ZeroWatt: https://zerowatt.energy/  
- ZeroWatt YourStory: https://yourstory.com/2025/06/zerowatt-energy-ai-efficiency-platform  
- LTTS EnergiSensEI: https://www.ltts.com/solutions/EnergiSensEI  
- Imubit: https://imubit.com/  
- Fero Labs: https://www.ferolabs.com/  
- Basetwo: https://www.basetwo.ai/ · Series A: https://www.basetwo.ai/announcements/basetwo-raises-11-5m-series-a-to-transform-chemical-manufacturing-with-physics-ai-platform  
- Sight Machine: https://www.sightmachine.com/  
- Tulip Series C: https://tulip.co/press/tulip-raises-100m-seriesc-led-by-insight-partners/  
- MachineMetrics Series B: https://www.businesswire.com/news/home/20210616005165/en/MachineMetrics-Announces-%2420M-Series-B-Funding-Round  
- CloudNC: https://www.cloudnc.com/ · $20M 2026: https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/  
- Productive Machines: https://solutions.productivemachines.co.uk/  
- Lambda Function: https://www.lambdafunction.ai/  
- Nanoprecise Series C: https://nanoprecise.io/blog/nanoprecise-closes-38m-usd-series-c-fundraise/  
- Infinite Uptime TechCrunch: https://techcrunch.com/2025/03/10/infinite-uptime-bags-35m-to-help-factories-optimize-equipment-usage/  
- Augury PepsiCo story: https://www.augury.com/success-stories/pepsicos-manufacturing-innovation-leads-to-tangible-roi/  
- Noetive seed: https://noetive.ai/news/noetive-emerges-from-stealth-with-41-million-seed · https://runtimewire.com/article/noetive-41m-seed-industrial-world-models  
- Zentio: https://zentio.ai/  
- Arrakis: https://thenextweb.com/news/arrakis-ai-startup-38-million-stealth-industrial  
- PhysicsX: https://www.physicsx.ai/platform  
- Prometheus: https://www.prometheusenergy.ai/  
- Siemens Industrial AI: https://www.siemens.com/global/en/products/automation/topic-areas/industrial-ai.html  
- Palantir manufacturing: https://www.palantir.com/explore/foundry-for-manufacturing/  
- Bright Machines Series C PR: https://www.prnewswire.com/news-releases/bright-machines-raises-126m-series-c-funding-to-propel-manufacturing-into-software-defined-era-302181151.html  
- TrendMiner acquisition: https://www.finsmes.com/2024/04/proemion-holding-acquires-trendminer.html  

### Tech / standards
- TimesFM-3 (Google Research): https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/  
- TabPFN time-series discussion (arxiv): https://arxiv.org/html/2501.02945v3  
- IPMVP (EVO): https://www.evo-world.org/en/products-services-mainmenu-en/protocols/ipmvp  
- Cognite agentic / knowledge graph commentary: https://www.arcweb.com/blog/data-fabric-digital-teammates-agentic-ai-vision-cognite-impact-2025  

### India deployment context (illustrative, not exhaustive)
- TVS Next manufacturing intelligence orchestration: https://www.expresscomputer.in/news/beyond-dashboards-why-tvs-next-is-betting-on-manufacturing-intelligence-orchestration/138086/  
- Honda Car India digital manufacturing (Infosys case): https://www.infosys.com/industries/industrial-manufacturing/case-studies/digital-partnership.html  

### Fetch notes / confidence flags
- **Noetive press page:** one WebFetch attempt timed out; content corroborated via WebSearch summaries + alternate Runtime Wire / Ctech coverage.  
- **Sight Machine exact funding:** databases disagree—do not cite a single total without primary filing.  
- **LTTS site metrics:** internal inconsistencies on site count (50+ vs 1000+)—likely product vs broader practice; verify in sales conversations.  
- **“Bright AI”:** no separate confirmed entity; mapped to Bright Machines + Noetive world-model narrative.  
- **Johnson Controls:** stronger in buildings/HVAC/data centers than factory process AI; Adani/Reliance factory AI often involves process automation majors (Honeywell et al.)—treat as account context, not a single “comp.”  
- All percentage savings and plant counts are **vendor/press-reported** until independently audited.

---

## Appendix: One-page cheat sheet (memorize)

**Energy peers:** Greenovative · ZeroWatt · EnergiSensEI · Nanoprecise (ECM)  
**Process peers:** Fero · Imubit · Basetwo · Sight Machine  
**PdM (adjacent):** Augury · Infinite Uptime · Senseye/Siemens  
**Data fabric:** Cognite · Palantir · C3 · Databricks  
**Physical AI / narrative:** Bright Machines · Noetive · PhysicsX · Arrakis · Zentio  
**Discrete CNC:** CloudNC · Productive Machines · Lambda Function  
**Majors:** Siemens · Rockwell · Microsoft · ABB · Schneider/AVEVA  

**Stamped sentence:**  
“We sell a **verified decision layer**—Energy for resource cost and intensity, Process for engineering outcomes—sitting on the customer’s existing OT, with physics hygiene and M&V, climbing the autonomy ladder only as fast as plant trust allows.”

---
*End of study document. For Vinayak / Stamped internal use. Update quarterly as funding and M&A move.*
