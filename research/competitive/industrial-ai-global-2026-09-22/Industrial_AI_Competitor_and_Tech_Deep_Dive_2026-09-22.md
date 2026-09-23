# Industrial AI Competitor & Tech Deep Dive
**Prepared for:** Vinayak Raizada — Stamped (India industrial AI)  
**Date:** 2026-09-22 (IST)  
**Method:** WebSearch + WebFetch of primary sources (company sites, product docs, SEC/EU/CN filings, Reuters/TechCrunch/company PR). Every funding/revenue/plant/savings figure cites a public URL or is marked `Not disclosed publicly`. Vendor marketing flagged **vendor-claimed**. No invented statistics.  
**Baseline expanded:** Deepens [`Factory_Intelligence_Global_Market_and_Tech_Study.md`](./Factory_Intelligence_Global_Market_and_Tech_Study.md) (~30 companies) into a multi-region dossier set.  
**Stamped positioning (vision v0.3):** Outcome specialists — **Stamped Energy** (energy/resource efficiency, verified ₹/SEC) + **Stamped Process** (manufacturing process engineering / methods decisions, HITL freezes). Not Cognite/Siemens replacements. Energy wedge; Process = PE decisions; HITL.

---

## Document map (read this first)

| File | Contents |
|---|---|
| **This master** | Exec briefing, market definition, 2024–26 tech movements summary, India dossiers, competitor matrix, “what’s new,” Stamped implications, master source index |
| [`Industrial_AI_Deep_Dive_Tech_Approaches.md`](./Industrial_AI_Deep_Dive_Tech_Approaches.md) | Plain-English curriculum: fabrics, FMs, hybrid twins, world models, agents, closed-loop, PdM, Energy M&V, CAM AI |
| [`Industrial_AI_Deep_Dive_USA.md`](./Industrial_AI_Deep_Dive_USA.md) | USA/NA competitor table + ~38 dossiers |
| [`Industrial_AI_Deep_Dive_Europe.md`](./Industrial_AI_Deep_Dive_Europe.md) | Europe majors + startups dossiers |
| [`Industrial_AI_Deep_Dive_China.md`](./Industrial_AI_Deep_Dive_China.md) | China industrial AI (thorough) |
| [`Industrial_AI_Deep_Dive_India.md`](./Industrial_AI_Deep_Dive_India.md) | India dossiers (Energy/Process home market) |
| [`README.md`](./README.md) | Pack index and Stamped mapping notes |

---

## 1. Executive briefing for Stamped (how to read this map)

### What “industrial AI / factory intelligence” is
Not one product. A **stack** that turns plant OT/IT data into decisions that change cost, yield, energy, quality, or uptime:

| Layer | Question | Typical buyer |
|---|---|---|
| Connect & contextualize | Can we trust and join the data? | CIO / OT architect |
| See | What is happening / happened? | Plant / production manager |
| Predict | What will fail or drift? | Reliability / maintenance |
| Prescribe | What should we change? | Process / energy engineer |
| Act (closed-loop) | Can software write setpoints safely? | Controls / APC |
| Orchestrate (agents) | Who/what executes across systems? | Digital / ops excellence |

**Stamped mapping:**
- **Energy** → prescribe + prove savings (M&V); HITL; no default DCS writeback; no vibration PdM product line.
- **Process** → manufacturing **process engineering / methods** outcomes (cycle time, cost per accepted part, tool life); AI reasoner + human freezes + implementation path.

### Market structure in one monologue
1. **Hyperscalers & industrial majors** (Siemens, Rockwell, ABB, Microsoft, Schneider/AVEVA+Cognite, Huawei in China) own installed base and race to agentic copilots. Slow; advisory-first; win deep accounts.
2. **Industrial data platforms** (Cognite, C3 AI, Palantir, Databricks patterns, Huawei iDME) sell the **data foundation**. Cognite’s agreed **$3.1B** acquisition by Schneider (Jun 30, 2026; closing pending) is category-defining M&A. Cognite 2025 revenue **>$170M** (Reuters/Schneider).
3. **Outcome specialists** win by owning a KPI: uptime (Augury, Infinite Uptime, Nanoprecise), OEE/visibility (Sight Machine, MachineMetrics, Tulip), process margin (Imubit, Fero, Basetwo, Oden, SUPCON TPT), CNC programming (CloudNC, Lambda Function), energy intensity (Greenovative, ZeroWatt, EnergiSensEI, EnOS).
4. **Physical-AI / world-model startups** (Noetive $41M seed Sep 2026; Bright Machines; Haier Tianzhi narratives; Foxconn×NVIDIA) shift story from dashboards → models that observe, reason, eventually act. **Study, don’t chase CapEx.**

### Naming clarification
Vaibhav’s “Bright AI” ≈ **Bright Machines** + **Noetive** world-model narrative — not a separate confirmed “Bright AI” entity.

### How to use dossiers
For each company ask: (1) What KPI do they own? (2) Advisory vs closed-loop? (3) Hardware vs software? (4) Energy / Process / Foundation / Irrelevant to Stamped? (5) What can we absorb vs partner vs ignore?

---

## 2. Market definition & stack layers

See Tech Approaches annex §1 for the full connect→agentic table and autonomy ladder (Levels 0–5). **Stamped default live at Levels 2–3** (prescribe + HITL act); design for 4 without shipping 4 prematurely.

**Payment models observed:**
- Enterprise subscription + PS (Cognite, C3, Seeq, Braincube)
- Sensors + SaaS (Augury, Infinite Uptime, Nanoprecise, ZeroWatt)
- Outcomes / gainshare (Imubit-class; Stamped Process v0.3 lock)
- Seat/plugin (CloudNC, Tulip)
- Automation CapEx + software (Bright Machines, Siemens, Rockwell)

---

## 3. Latest tech movements 2024–2026 (summary + sources)

Full plain-English explanations: **Tech Approaches annex**. Headlines:

| Movement | What’s actually new | Key sources |
|---|---|---|
| Industrial data fabrics / KGs | Cognite→Schneider $3.1B agreement; Atlas AI; Palantir Foundry for mfg; HighByte UNS | Reuters 2026-06-30; cognite.com |
| Time-series / tabular FMs for OT | TimesFM-3; SUPCON TPT/TPT2 industrial transformer + agents | Google Research; global.supcon.com/digital/tpt |
| Physics-informed / hybrid twins | Aspen Hybrid Models; Basetwo Series A; PhysicsX $300M Series C press | aspentech.com; basetwo.ai; physicsx.ai |
| World models / physical AI | Noetive $41M; Bright Machines SDM; Haier industrial world model; Foxconn×NVIDIA | noetive.ai; brightmachines.com; NVIDIA case studies |
| Agentic industrial copilots | Siemens Copilot+Senseye; ABB Genix Copilot; Schneider×Microsoft; Rockwell×Microsoft | Siemens/ABB/Rockwell press |
| Closed-loop APC / RL | Imubit Map→Model→Control; SUPCON autonomous chlor-alkali claims | imubit.com; SUPCON TPT page |
| Edge AI + PdM | Augury $75M @ $1B+ (Feb 2025); Infinite Uptime Series C $35M; Nanoprecise $38M | TechCrunch; company PRs |
| Energy intensity / M&V AI | Greenovative / ZeroWatt / EnergiSensEI; EnOS; IPMVP discipline | Company sites; evo-world.org |
| CAM / CNC AI | CloudNC +$20M (Sep 2026); 1,000+ shops; Lambda Function; SenseNC | TechCrunch; company sites |

---

## 4. Regional deep dives

- **USA:** [`Industrial_AI_Deep_Dive_USA.md`](./Industrial_AI_Deep_Dive_USA.md) — Bright Machines, Noetive, Cognite, C3 AI, Palantir, Augury, Seeq, Fero, Imubit, Basetwo, Sight Machine, MachineMetrics, Tulip, Litmus, HighByte, Uptake, SparkCognition, Landing AI, Cognex, Instrumental, Elementary, Samsara, CloudNC, Toolpath, Microsoft, AWS, Rockwell, Emerson/Aspen, Honeywell Forge, GE Vernova, etc.
- **Europe:** [`Industrial_AI_Deep_Dive_Europe.md`](./Industrial_AI_Deep_Dive_Europe.md) — Siemens, ABB, Schneider+AVEVA+Cognite, Bosch Rexroth, Celonis, Cumulocity, Oden, Braincube, Cosmo Tech, Neural Concept, Dassault, SAP DM, Arrakis, PhysicsX, Zentio, TrendMiner, Senseye.
- **China:** [`Industrial_AI_Deep_Dive_China.md`](./Industrial_AI_Deep_Dive_China.md) — Huawei, Alibaba/Rhino, Foxconn, COSMOPlat, RootCloud, SUPCON TPT, HollySys, EnOS, SenseTime/Megvii, Mech-Mind, Aqrose, Orbbec, Hulu, YonYou, Kingdee, Cambricon, State Grid AI, BYD/CATL (public only).
- **India:** [`Industrial_AI_Deep_Dive_India.md`](./Industrial_AI_Deep_Dive_India.md) + Section 4.4 summary below.

---

## 4.4 India (compact but accurate)

| Company | Website | Archetype | Energy | Process |
|---|---|---|---|---|
| Greenovative | greenovative.com | Prescriptive energy intelligence | **Direct** | Adjacent |
| ZeroWatt | zerowatt.energy | AI energy brain + metering | **Direct** | Adjacent |
| LTTS EnergiSensEI | ltts.com/solutions/EnergiSensEI | Engineering-verified energy/ESG | **Direct** | Adjacent |
| Infinite Uptime | infiniteuptime.com | Sensors + PdM / PlantOS | Adjacent | Adjacent |
| Nanoprecise | nanoprecise.io | PdM + Energy-Centered Maintenance | **Adjacent→Direct angle** | Adjacent |
| Lambda Function | lambdafunction.ai | AI CAM + machining autonomy | Irrelevant | **Direct adjacent** |
| Dashnode | (dashnode.in / confirm) | Costing / manufacturing intelligence | Irrelevant | Adjacent |
| Emithran | emithran.com | Planning/costing/sourcing AI | Irrelevant | Adjacent |
| Ethereal Machines | etherealmachines.com | CNC / advanced manufacturing OEM | Irrelevant | Adjacent |
| Intellithink | intellithink.com | Industrial IoT / PdM adjacency | Adjacent | Adjacent |
| TVS Next (context) | — | Mfg intelligence orchestration narratives | Foundation | Foundation |

### India dossiers

#### Greenovative
- **HQ:** Pune, India; https://greenovative.com/
- **Sells:** Prescriptive industrial energy intelligence — source cost mix, renewables, capex utilization, production unit economics, multi-site benchmarking; SCADA/PLC/BMS integrate; HW-agnostic claim.
- **Claims (vendor):** 200+ deployments / 80+ industry leaders; 2–3 week go-live; 12–15% energy cost reduction; <12 month ROI — **vendor-claimed**.
- **Funding:** Strategic investment from European sustainability fund (company news; amount often **Not disclosed publicly**). https://greenovative.com/news-events/greenovative-secures-european-strategic-investment/
- **Stamped:** **Closest India Energy competitor** — study weekly.
- **Risks:** Enterprise multi-site bar; savings claims need M&V discipline to counter.

#### ZeroWatt
- **HQ:** IITM Research Park / Trivandrum roots; https://zerowatt.energy/
- **Sells:** AI energy & ops intelligence (“digital energy brain”); waste detection + root cause + prescribe; equipment health angle; HW at cost + SaaS per metering point (press).
- **Claims:** YourStory (Jun 2025): bootstrapped by NTPC veterans; **100+ factories**, **120 MW+** load, ~10% average energy reduction — **press/vendor**. Site may claim 20–30% cost reduction / 3–6 month payback — **vendor**.
- **Stamped:** **Direct Energy comp** — alternate GTM (hardware-assisted).
- **Source:** https://yourstory.com/2025/06/zerowatt-energy-ai-efficiency-platform

#### LTTS EnergiSensEI
- **Website:** https://www.ltts.com/solutions/EnergiSensEI
- **Sells:** Energy & sustainability platform with **physics verification before AI**; Assess→Build→Operate→Sustain; agents (Optimizer, Trends, Insights, Reports, Dashboard).
- **Claims (LTTS):** 5–15% energy & water reduction; site counts inconsistently stated (50+ vs 1000+ blocks) — **treat carefully; SI scale may blend programs**.
- **Stamped:** **Steal verify-first / M&V doctrine**.
- **Risks:** SI packaging vs pure product; metric inconsistency on site.

#### Infinite Uptime
- **Website:** https://www.infiniteuptime.com/
- **Sells:** Proprietary sensors + analytics + AI diagnostics; predictive/prescriptive maintenance; energy-per-ton commentary in founder interviews.
- **Scale/funding:** TechCrunch Mar 10, 2025: Series C **$35M** (Avataar-led); ~**$65M** total; **~800 plants / ~30 countries**; ~350 employees; cash-flow positive claim (**founder via press**). https://techcrunch.com/2025/03/10/infinite-uptime-bags-35m-to-help-factories-optimize-equipment-usage/
- **Verticals:** Steel, cement, metals, mining, fertilizers, chemicals, paper.
- **Stamped:** India-origin scale proof; PdM ≠ Energy product, but GTM + energy co-benefit lessons transfer. **Adjacent**.

#### Nanoprecise
- **Website:** https://nanoprecise.io/
- **Sells:** Multi-parameter IoT sensors + AI; **Energy-Centered Maintenance** thesis.
- **Funding:** Series C **$38M USD** equity+debt (Mar 2025 company PR). https://nanoprecise.io/blog/nanoprecise-closes-38m-usd-series-c-fundraise/
- **Stamped:** Closest PdM player to **Energy thesis** — study ECM framing. Adjacent/angle-Direct.

#### Lambda Function
- **Website:** https://www.lambdafunction.ai/
- **Sells:** Autonomous precision machining — AI CAM + load/vibration/tool-life closed loop.
- **Funding/revenue:** Not disclosed publicly in sources reviewed this pass.
- **Stamped:** Process **Direct adjacent** (CNC autonomy). Different GTM if Stamped sells outcomes not seats.

#### Dashnode / Emithran / Ethereal / Intellithink
- **Dashnode:** Manufacturing costing / intelligence adjacency — Process Adjacent; confirm live domain before deck use.
- **Emithran:** Planning/costing/sourcing — Adjacent to Process but **not** methods engineering core (vision v0.3 out-of-scope for supply-chain).
- **Ethereal Machines:** Advanced CNC OEM — Adjacent as beachhead customer archetype, not software peer.
- **Intellithink:** IIoT/PdM adjacency — Adjacent; not Energy core.

#### India deployment theaters (not single-vendor comps)
- TVS / TVS Next manufacturing intelligence orchestration (Express Computer coverage).
- Honda India digital manufacturing partnerships (Infosys case studies).
- Adani/Reliance-class plants often buy via Honeywell/majors/SI — treat as **accounts**, not one competitor.

---

## 5. Cross-company competitor matrix (selected)

| Company | Primary KPI owned | Closed-loop vs advisory | HW vs SW | Region strength | vs Stamped Energy | vs Stamped Process |
|---|---|---|---|---|---|---|
| Greenovative | Energy cost / SEC | Advisory→prescribe | SW | India | Direct | Adjacent |
| ZeroWatt | Energy cost | Prescribe | H+S | India | Direct | Adjacent |
| EnergiSensEI | Verified energy/ESG | Prescribe | SW+services | India/global SI | Direct | Adjacent |
| EnOS | Energy asset opt | Advisory→opt | SW | CN/global | Direct | Adjacent |
| SUPCON TPT | Yield / specific energy | Closed-loop capable | SW on DCS | China | Direct | Direct |
| Imubit | Margin / fuel intensity | Closed-loop | SW | US | Adjacent | Direct |
| Fero Labs | Process quality/yield | Advisory→live | SW | US | Adjacent | Direct |
| Basetwo | Process twin outcomes | Assist→auto | SW | NA | Adjacent | Direct |
| Oden | Production optimization | Advisory→AI suite | SW | EU/US | Adjacent | Direct |
| Augury | Uptime / process health | Advisory | H+S | US | Adjacent | Adjacent |
| Infinite Uptime | Uptime | Prescribe | H+S | India→global | Adjacent | Adjacent |
| Nanoprecise | Uptime + ECM | Prescribe | H+S | Global | Adjacent | Adjacent |
| Cognite | Contextualized data | Foundation + agents | SW | Global | Foundation | Foundation |
| C3 AI | Enterprise AI apps | Advisory apps | SW | US | Adjacent | Adjacent |
| Palantir | Ontology ops | Ops apps | SW | US | Foundation | Foundation |
| Siemens Copilot | Eng/maint productivity | Advisory agents | H+S | Global | Foundation | Foundation |
| Schneider+AVEVA | Energy+industrial SW | Mixed | H+S | Global | Foundation | Foundation |
| Bright Machines | Assembly throughput | Execution | H+S | US | Irrelevant | Adjacent |
| Noetive | Ops intelligence | Aspire act | H+S | US | Adjacent | Adjacent |
| CloudNC | Programming time | Advisory CAM | SW | UK/US | Irrelevant | Adjacent |
| Lambda Function | Machining autonomy | Closed-loop | H+S | India | Irrelevant | Direct adj. |
| Sight Machine | OEE / production twin | Advisory→opt | SW | US | Adjacent | Adjacent |
| Tulip | Frontline execution | Apps | SW | US | Irrelevant | Adjacent |
| MachineMetrics | Machine OEE | See | H+S | US | Irrelevant | Adjacent |
| PhysicsX | Sim fidelity / eng speed | Sim | SW | UK | Adjacent | Direct |
| Arrakis | Industrial AI OS | FDE agents | SW | EU | Adjacent | Adjacent |
| Braincube | Production KPIs | Advisory | SW | FR | Adjacent | Adjacent |
| RootCloud | Connected assets | IIoT apps | SW | CN | Adjacent | Adjacent |
| COSMOPlat | Flexible mfg / agents | Platform | SW | CN | Adjacent | Adjacent |
| Huawei industrial | Industry models/agents | Full stack | H+S | CN | Foundation | Foundation |
| Hulu 黑湖 | MES execution | SaaS | SW | CN | Irrelevant | Adjacent |
| Celonis | IT process mining | Advisory | SW | DE | Adjacent | Adjacent* |
| Cognex | Vision quality | Inspection | H+S | US | Irrelevant | Adjacent |

\*Celonis “process” ≠ manufacturing process engineering — messaging hazard.

---

## 6. Latest “what’s actually new” narrative (2025–2026)

1. **Data fabric became strategic M&A.** Schneider’s $3.1B Cognite agreement (Jun 2026; closing pending) prices industrial contextualization as core infrastructure, not niche SaaS. https://www.reuters.com/business/schneider-electric-buy-ai-software-firm-cognite-31-billion-2026-06-30/
2. **Majors productized copilots.** Siemens (maintenance Copilot + Senseye), ABB Genix Copilot, Rockwell×Microsoft, Schneider×Microsoft — mostly Level 1–2 autonomy with HITL.
3. **Industrial foundation models left the lab.** SUPCON TPT/TPT2 ships process-industry FM + agents with vendor plant case metrics; Google TimesFM-3 strengthens zero-shot TS baselines.
4. **Physical AI / world-model capital wave.** Noetive $41M seed (Sep 2026); PhysicsX $300M Series C press; Bright Machines continuing SDM; Foxconn×NVIDIA factory twins.
5. **PdM unicorns & India scale.** Augury $75M @ $1B+ (Feb 2025); Infinite Uptime 800 plants / Series C $35M; Nanoprecise Series C $38M — PdM is crowded; Energy-Centered angles matter.
6. **CNC AI commercializes.** CloudNC 1,000+ shops + $20M (Sep 2026); Lockheed-adjacent capital signal.
7. **China DCS + 工业大模型.** SUPCON and Huawei ACT pathway show China stacking agents on domestic compute and control — under-covered in Western decks.
8. **C3 AI public reality check.** FY2026 revenue $250.3M with restructuring / CEO return narrative — enterprise AI apps are hard; packaging ≠ automatic growth. https://www.c3.ai/news/c3-ai-announces-fiscal-fourth-quarter-and-full-fiscal-year-2026-results

---

## 7. Stamped implications

### Absorb (copy doctrine, not logos)
- **Verify-before-AI / IPMVP packs** (EnergiSensEI, IPMVP).
- **Prescriptive actions with ₹ impact + role owner** (Greenovative, ZeroWatt).
- **White-box process diagnostics** (Fero).
- **Map→Model→Control discipline** (Imubit) — stop at Model+Prescribe initially.
- **Lightweight asset graph** (Cognite ideas, smaller scope).
- **Energy-Centered framing** where maintenance meets kWh (Nanoprecise) — as narrative, not PdM product.
- **SUPCON lesson:** industrial FM + first principles + semantic tags for process units.

### Partner
- Data fabrics in large accounts (Cognite/AVEVA post-close, Palantir, Databricks, Azure).
- Automation majors’ agent runtimes (expose Stamped actions as tools).
- Controls integrators for any future Level 4 writeback.
- CAM vendors as beachhead data sources for Process — not as the product.

### Ignore / do not build
- Robotics / software-defined factory CapEx (Bright Machines path).
- Full industrial DataOps platform as the company.
- Vibration PdM as a customer pillar (vision v0.3 exit).
- “World model” marketing without predictive eval harness.
- Unqualified “process optimisation” that sounds like supply chain or Celonis.

### Vertical niche hypotheses (test, don’t declare)
| Hypothesis | Product | Why |
|---|---|---|
| Automotive discrete utilities + paint/HVAC energy | Energy | India auto groups; multi-site; known Energy comps already hunting |
| Cement / metals SEC (kWh/ton) | Energy | Infinite Uptime/Nanoprecise already in vertical; Energy wedge can co-exist if M&V-owned |
| Precision machining methods + tooling freeze | Process | Lambda/CloudNC adjacent; Stamped outcomes differentiation |
| Process heat / furnace / kiln setpoint prescribe (open-loop) | Process→Energy join | Imubit/SUPCON/Fero method transfer without closed-loop risk |

### 90-day bias (unchanged in spirit from baseline study)
1. Energy: one vertical + M&V pack + meter reconciliation.  
2. Process: one engineering decision class with explainable freeze package.  
3. Shared: asset graph + OT connectors + regime detection.  
4. Park: DCS write agents; world-model research marketing; horizontal FM claims.

---

## 8. Company count & coverage checklist

**Named with websites in this study set (master + annexes): 55+** including:

USA/NA: Bright Machines, Noetive, Cognite, C3 AI, Palantir, Augury, Seeq, Fero Labs, Imubit, Basetwo, Sight Machine, MachineMetrics, Tulip, Litmus, HighByte, Uptake, SparkCognition, Parsable, Landing AI, Cognex, Instrumental, Elementary, Samsara, CloudNC, Toolpath, Productive Machines, Microsoft, AWS, Google (MDE), Rockwell, Emerson/AspenTech, Honeywell Forge, GE Vernova  

Europe: Siemens, Senseye, ABB, Schneider, AVEVA, Bosch Rexroth, Celonis, Software AG/Cumulocity, Oden, Braincube, Cosmo Tech, Neural Concept, Imagimob, Dassault, SAP, Arrakis, PhysicsX, Zentio, TrendMiner  

China: Huawei, Alibaba (Industrial Brain/Rhino), Tencent Cloud, Baidu Cloud, Foxconn/Hon Hai, Haier COSMOPlat, RootCloud/Sany, SUPCON, HollySys, Envision/EnOS, SenseTime, Megvii, Mech-Mind, Aqrose, Orbbec, Hulu/黑湖, YonYou, Kingdee, Cambricon, State Grid/CSG (context), BYD, CATL  

India: Greenovative, ZeroWatt, LTTS EnergiSensEI, Infinite Uptime, Nanoprecise, Lambda Function, Dashnode, Emithran, Ethereal Machines, Intellithink  

---

## 9. Source appendix (master index — see also annex appendices)

### M&A / public company
- Schneider–Cognite: https://www.reuters.com/business/schneider-electric-buy-ai-software-firm-cognite-31-billion-2026-06-30/
- Cognite PR: https://www.cognite.com/en/company/newsroom/schneider-electric-announces-agreement-to-acquire-cognite
- C3 AI FY2026: https://www.c3.ai/news/c3-ai-announces-fiscal-fourth-quarter-and-full-fiscal-year-2026-results
- Palantir earnings ex: https://www.sec.gov/Archives/edgar/data/1321655/000132165526000004/a2025q4ex991earningsrelease.htm

### Funding / launches 2025–26
- Noetive $41M: https://noetive.ai/news/noetive-emerges-from-stealth-with-41-million-seed
- Bright Machines Series C: https://www.prnewswire.com/news-releases/bright-machines-raises-126m-series-c-funding-to-propel-manufacturing-into-software-defined-era-302181151.html
- Augury $75M: https://techcrunch.com/2025/02/19/augury-raises-73m-on-a-1b-valuation-for-ai-to-detect-malfunctions-in-factory-machines/
- Infinite Uptime: https://techcrunch.com/2025/03/10/infinite-uptime-bags-35m-to-help-factories-optimize-equipment-usage/
- Nanoprecise: https://nanoprecise.io/blog/nanoprecise-closes-38m-usd-series-c-fundraise/
- Arrakis: https://fortune.com/2026/07/22/arrakis-a-startup-betting-ais-biggest-payoff-is-in-industrial-sectors-not-office-work-emerges-from-stealth-with-38-million-in-venture-funding/
- PhysicsX Series C: https://www.physicsx.ai/newsroom/physicsx-announces-300m-series-c-to-accelerate-physics-ai-for-industrial-engineering
- CloudNC $20M: https://techcrunch.com/2026/09/08/cloudnc-raises-20m-to-automate-manufacturings-most-pressing-bottlenecks/
- Basetwo Series A: https://www.basetwo.ai/announcements/basetwo-raises-11-5m-series-a-to-transform-chemical-manufacturing-with-physics-ai-platform
- Seeq Series D: https://www.prnewswire.com/news-releases/seeq-announces-50-million-series-d-funding-round-led-by-sixth-street-growth-302215495.html
- Oden Series B: https://siliconangle.com/2024/04/11/oden-technologies-raises-28-5m-launch-ai-driven-products-manufacturing/
- Braincube €83M: https://tech.eu/2023/11/29/french-iiot-platform-braincube-secures-eur83-million-investment/
- Mech-Mind CNY500M: https://in.marketscreener.com/news/mech-mind-robotics-technologies-ltd-announced-that-it-has-received-cny-500-million-in-funding-from-ce7c50dedf8bf620

### Tech / standards
- TimesFM-3: https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/
- SUPCON TPT2: https://global.supcon.com/digital/tpt
- IPMVP: https://www.evo-world.org/en/products-services-mainmenu-en/protocols/ipmvp
- Aspen Hybrid Models: https://www.aspentech.com/en/solutions/aspen-hybrid-models/
- Huawei ACT: https://www.huawei.com/en/news/2025/9/hc-act-industrial-intelligence

### India Energy
- Greenovative: https://greenovative.com/
- ZeroWatt: https://zerowatt.energy/ · https://yourstory.com/2025/06/zerowatt-energy-ai-efficiency-platform
- EnergiSensEI: https://www.ltts.com/solutions/EnergiSensEI

### Fetch failures / gaps
- Some Chinese English product pages redirect or vary by region; used filings + Chinese press + global.supcon.com successfully.
- Sight Machine exact funding: databases disagree — flagged unverified.
- EnOS customer counts conflict across marketing mirrors — not frozen.
- LTTS site metric inconsistency (50+ vs 1000+ sites) — flagged.
- Element Analytics / Limitless Labs / “Amplitude industrial” / Scale AI industrial SKU: not confirmed as material peers.
- Cognex 2025 revenue: confirm on Cognex IR before investor reuse.
- ZeroWatt “₹116 crore investment” appeared in some search snippets — **not verified against primary** in this pass; do not cite until primary PR found.
- Dealroom note: Cognite acquisition **announced not closed** as of ~20 Sep 2026 tracking.

---

## 10. One-page cheat sheet (memorize)

**Energy peers:** Greenovative · ZeroWatt · EnergiSensEI · EnOS · Nanoprecise (ECM) · SUPCON (specific energy)  
**Process peers:** Fero · Imubit · Basetwo · Oden · SUPCON TPT · PhysicsX (method) · Lambda/CloudNC (CNC adjacent)  
**PdM (out of Stamped product scope):** Augury · Infinite Uptime · Senseye/Siemens  
**Data fabric:** Cognite · Palantir · C3 · Huawei iDME · HighByte  
**Physical AI narrative:** Bright Machines · Noetive · Foxconn×NVIDIA · Haier Tianzhi  
**Majors:** Siemens · Rockwell · Microsoft · ABB · Schneider/AVEVA  

**Stamped sentence:**  
“We sell a **verified decision layer**—Energy for resource cost and intensity, Process for manufacturing engineering outcomes—on the customer’s existing OT, with physics hygiene and M&V, climbing the autonomy ladder only as fast as plant trust allows.”

---

*End of master document. Update quarterly. Annexes carry full dossiers.*


---

## Appendix M — Greenovative primary-site snapshot (fetched 2026-09-22)

Source: https://greenovative.com/

**Positioning (vendor):** Prescriptive industrial energy intelligence — “pinpoints exactly where you’re losing energy and delivers specific actions.”

**Scale claims (vendor UI):** Trusted by **80+** industry leaders; industrial deployments across **7 countries**; enterprise retention and ROI claims rendered as animated counters on site (treat numerical counters as **vendor-claimed**; FAQ states most plants go live in **2–3 weeks** without hardware retrofit).

**Capability modules named:** Source Cost Optimisation; Renewable Optimisation; Capacity/Capex Utilisation; Production Unit Economics; Enterprise Baseline & Benchmarking.

**Impact claims (vendor):** 12–15% energy cost reduction; <12-month ROI; 10–15% capex utilization increase; 15–20% CO₂ reduction; 10–12% resource efficiency — **all vendor-claimed**.

**Named testimonial roles/org cues on site:** Automotive conglomerate digital head; Jotun regional maintenance (ME expansion); cement AGM-IT; LG Ranjangaon CIO; textile HOD E&I — use as **reference categories**, verify before public Stamped competitive claims.

**Security claims (vendor FAQ):** Zero-trust, encryption, RBAC, ISO 27001 and CREST/CERT-IN alignment, VAPT — **vendor**.

**Stamped Energy competitive read:** Greenovative already owns the India enterprise Energy narrative Stamped must beat on **decision closure + M&V evidence**, not on “AI for energy” slogan overlap.

---

## Appendix N — Imubit vendor metrics (fetched 2026-09-22)

Source: https://imubit.com/

| Metric | Value on site | Flag |
|---|---|---|
| Closed-loop apps | 100+ | vendor-claimed |
| Model engagement | 7+ years | vendor-claimed |
| NG usage reduction | 15–30% | vendor-claimed |
| Margin improvement | $0.25/bbl | vendor-claimed |
| Yield improvement | 1–3% avg | vendor-claimed |

Named customer organizations with quotes: Citgo, Ash Grove, Oxbow, Monroe Energy, Big West Oil, Preem.

---

## Appendix O — Suggested weekly reading list (90 days)

**Week A (Energy):** Greenovative site+FAQ · ZeroWatt+YourStory · EnergiSensEI · IPMVP overview · Nanoprecise ECM PR  
**Week B (Process):** Fero Gerdau case · Imubit Map/Model/Control · Basetwo Series A · Oden Series B post  
**Week C (Foundation):** Cognite+Schneider Reuters · HighByte UNS primer · Palantir Panasonic  
**Week D (China method):** SUPCON TPT page · Huawei ACT press · EnOS overview  
**Week E (Narrative discipline):** Noetive seed · Bright Machines platform · PhysicsX Series C — write “what we will not claim” memo  
**Week F (Discrete Process):** CloudNC · Lambda Function · SenseNC · Toolpath — map objects into Stamped Process freeze package  
**Week G:** Synthesis monologue for investors (master §1 + §7)

---

## Appendix P — Glossary (quick)

| Term | Meaning here |
|---|---|
| SEC / EnPI | Specific energy consumption / energy performance indicator |
| M&V | Measurement & verification (IPMVP language) |
| HITL | Human-in-the-loop |
| APC | Advanced process control |
| DCS / PLC | Distributed control system / programmable logic controller |
| UNS | Unified Namespace |
| OT / IT / ET | Operations / information / engineering technology |
| FM | Foundation model |
| ECM | Energy-Centered Maintenance (Nanoprecise framing) |
| SDM | Software-defined manufacturing |
| IoR | Intelligence of Record (Noetive) |
| TPT | Time-series Pre-trained Transformer (SUPCON) |
| DfM / DFAA | Design for manufacturability / automated assembly |


---

## Appendix Q — Competitive war-gaming (Stamped vs named peers)

### vs Greenovative (Energy Direct)
| Dimension | Greenovative signal | Stamped response |
|---|---|---|
| Speed | 2–3 week go-live claim | Match or beat with connector kit |
| Proof | % savings on site | IPMVP packs + customer-signable quarterly |
| Multi-site | Enterprise benchmarking | Same; start one vertical deeply |
| Process join | Production unit economics module | Unique: PE regimes from Process product |

### vs ZeroWatt (Energy Direct)
| Dimension | ZeroWatt signal | Stamped response |
|---|---|---|
| HW | Metering points + HW at cost | Explicit HW-agnostic first; selective sensors only if gap |
| Heritage | NTPC veteran trust | Partner energy auditors; show M&V rigor |
| Scale claim | 100+ factories press | Don’t chase count; chase verified ₹ |

### vs Fero / Imubit (Process Direct)
| Dimension | Peer | Stamped response |
|---|---|---|
| Explainability | Fero white-box | Keep constraints visible in freeze UI |
| Closed-loop | Imubit RL→DCS | Stop at HITL prescribe until controls partner |
| Vertical | Steel/chem/refining | India discrete PE beachhead first |
| Commercial | Software seat / enterprise | Outcomes + implementation path (vision lock) |

### vs Lambda / CloudNC (CNC Adjacent)
| Dimension | Peer | Stamped response |
|---|---|---|
| KPI | Program time / autonomy | Cycle time / cost per good part / tool life |
| Offer | CAM seat/plugin | Freeze package + tooling path |
| Buyer | CAM programmer | Methods / PE + production leadership |

### vs Cognite / Siemens (Foundation)
| Dimension | Peer | Stamped response |
|---|---|---|
| Pitch | Platform / copilot | Outcome KPI app |
| Deal size | Multi-year enterprise | Land with Energy wedge weeks-not-years |
| Integration | They are the fabric | API into them later |

---

## Appendix R — Stats hygiene rules (for anyone updating this pack)

1. Every number needs a URL or `Not disclosed publicly`.
2. Prefer primary (company PR, SEC, exchange filing) over Crunchbase aggregates.
3. If two databases disagree (Sight Machine funding), say so — do not average.
4. Vendor % savings always tagged **vendor-claimed**.
5. M&A: distinguish **announced** vs **closed** (Cognite).
6. Chinese encyclopedia (Baike) is useful context, not audited IR.
7. Animated website counters (Greenovative “0+” placeholders in static fetch) — use FAQ/prose claims, not scraped zeros.
