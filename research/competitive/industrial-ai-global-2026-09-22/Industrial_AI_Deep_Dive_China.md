# Industrial AI Deep Dive — China (中国工业AI)
**Prepared for:** Vinayak Raizada — Stamped (India)  
**Date:** 2026-09-22 (IST)  
**Parent:** `Industrial_AI_Competitor_and_Tech_Deep_Dive_2026-09-22.md`  
**Method:** Company IR/pages, Chinese press (36Kr-class, company sites), SCMP/Reuters where available, Huawei/Haier/SUPCON primary pages. Prefer English + Chinese names. **No invented stats.** Third-party funding databases flagged. Note **data localization / on-prem norms**.

**Why this section exists:** Chinese industrial AI is systematically under-covered in Western decks. China has parallel stacks: industrial internet platforms (RootCloud, COSMOPlat), process DCS majors with industrial large models (SUPCON TPT), hyperscaler industrial brains (Huawei, Alibaba legacy), vision/robotics AI (Mech-Mind, Aqrose, Orbbec), and MES/SaaS (黑湖 Hulu). Deployment culture often prefers **on-prem / private cloud / data stays in China**.

**Adjacency to Stamped:** Direct | Adjacent | Foundation | Irrelevant

---

## China snapshot table

| Company (EN / 中文) | Website | Archetype | Energy | Process |
|---|---|---|---|---|
| Huawei Industrial Intelligence / FusionPlant / iDME | huawei.com | Hyperscaler industrial stack | Foundation | Foundation |
| Alibaba Cloud Industrial Brain / 犀牛智造 Rhino | aliyun.com | Cloud industrial + flexible mfg | Adjacent | Adjacent |
| Tencent / Baidu industrial AI | cloud.tencent.com / baidu.com | Cloud / CV adjacency | Adjacent | Adjacent |
| Foxconn / Hon Hai AI factories | foxconn.com / honhai.com | Physical AI / twin factories | Adjacent | Adjacent |
| Haier COSMOPlat / 卡奥斯 / 天智 | cosmoplat.com | Industrial internet + world model | Adjacent | Adjacent |
| Sany / RootCloud 树根互联 | rootcloud.com | IIoT platform | Adjacent | Adjacent |
| SUPCON 中控 / TPT | global.supcon.com | Process control + industrial FM | **Direct** | **Direct** |
| HollySys 和利时 | hollysys.com | DCS / smart plant | Adjacent | Adjacent |
| Envision Digital / EnOS | envision-group.com / univers.com | Energy AIoT OS | **Direct** | Adjacent |
| SenseTime 商汤 / Megvii 旷视 | sensetime.com / megvii.com | Vision AI | Irrelevant | Adjacent |
| Mech-Mind 梅卡曼德 | mech-mind.com | 3D vision robotics | Irrelevant | Adjacent |
| Aqrose 埃科森 / 相关工业视觉 | aqrose.com | Industrial vision QC | Irrelevant | Adjacent |
| Orbbec 奥比中光 | orbbec.com | 3D sensing | Foundation | Adjacent |
| 黑湖科技 Hulu | blacklake.cn / hulu.com mirrors | MES / mfg SaaS + agents | Irrelevant | Adjacent |
| 用友 YonYou | yonyou.com | ERP / BIP / industrial AI | Adjacent | Adjacent |
| 金蝶 Kingdee | kingdee.com | ERP / manufacturing cloud | Adjacent | Adjacent |
| Cambricon 寒武纪 | cambricon.com | AI chips (edge context) | Foundation | Foundation |
| State Grid / Southern Power Grid AI | (SOE) | Energy AI | Adjacent | Irrelevant |
| BYD / CATL digital mfg (public only) | byd.com / catl.com | OEM digital factories | Adjacent | Adjacent |
| iFLYTEK 科大讯飞 industrial | iflytek.com | Speech/LLM adjacency | Irrelevant | Adjacent |

---

## Structural notes (read before dossiers)

1. **工业互联网 (Industrial Internet)** was a national policy push (MIIT). Platforms connect equipment, build industrial apps, and increasingly add 工业大模型 (industrial large models).
2. **On-prem / localization:** Many plants and SOEs require data to remain in China, often on private cloud or air-gapped variants. Western SaaS GTM assumptions fail here.
3. **DCS majors matter:** Unlike US startup-led process AI narrative, China has strong domestic DCS vendors (SUPCON, HollySys) shipping **industrial FMs on top of control**.
4. **Stamped takeaway:** China’s closed-loop process AI (SUPCON TPT) and energy OS (EnOS) are method teachers; China’s IIoT platforms are Foundation-scale. Stamped will rarely compete head-to-head in China early; learning transfer matters for India plants owned by Chinese OEMs and for future product architecture.

---

## Dossiers — China priority

### 1. Huawei — Industrial Intelligent Manufacturing / FusionPlant / MindSpore / Ascend
- **Names:** 华为工业智能化；FusionPlant；工业数据平台 iDME.X；MindSpore 昇思；Ascend 昇腾
- **Website:** https://www.huawei.com/ · industrial news: https://www.huawei.com/en/news/2025/9/hc-act-industrial-intelligence
- **What they sell:** Full-stack ICT for industrial intelligence: compute (Ascend), AI framework (MindSpore), industrial data modeling (iDME.X / digital thread), FusionPlant industrial internet platform narratives, partner solutions for manufacturing R&D, steel blast furnace temperature prediction, oil & gas exploration, logistics, etc.
- **ACT pathway (Huawei CONNECT 2025):** Assess high-value scenarios → Calibrate industry models on vertical data → Transform with scaled AI agents. Claims framework helped identify **1,000+** core production scenarios (**vendor**). Ecosystem: 6,300+ Kunpeng partners, 2,700+ Ascend partners, 750 ISVs (**vendor**, Sep 2025).
- **Named industrial examples (vendor press):** China Southern Power Grid “MegaWatt” large model on Ascend/MindSpore for power line inspection (defect/risk ID efficiency ×5; image accuracy >90% — **vendor-claimed**). Steel blast furnace temperature prediction solution among nine launched solutions.
- **Tech approach (plain English):** Collect industrial data → build knowledge/models on Ascend → deploy industry-specific models and multi-agent workflows near production. Emphasize vertical data over generic LLMs.
- **Funding / revenue:** Huawei private; industrial AI revenue **Not disclosed publicly** as a separate line.
- **Pricing:** Enterprise + partner solutions; Not disclosed publicly.
- **Stamped adjacency:** **Foundation** (both). Not a peer for India mid-market SaaS, but defines Chinese OEM digital stack that Indian JV plants may inherit.
- **Risks / caveats:** Geopolitical export controls on Ascend; Western customers may avoid; vendor claims on scenario counts are marketing-scale.

### 2. Alibaba Cloud — ET Industrial Brain / 工业大脑 + 犀牛智造 (Rhino / Xiyin)
- **Names:** 阿里云工业大脑；犀牛智造
- **Websites:** Alibaba Cloud industrial docs; Rhino historical: Alibaba new manufacturing platform announcements (2020-era launch coverage). Industrial Brain open platform docs: https://help.aliyun.com/zh/industrial-intelligence/
- **What they sell historically / currently:**
  - **ET Industrial Brain:** industrial data + algorithms platform for modeling, optimization, quality (legacy “大脑” brand evolved into Alibaba Cloud industrial intelligence offerings).
  - **犀牛智造 (Rhino Smart Manufacturing):** Alibaba’s flexible apparel manufacturing platform connecting demand signals (Taobao/Tmall) to small-batch factory production with IoT/AI scheduling — more of an Alibaba-operated manufacturing network than a general industrial AI SaaS sold to arbitrary plants.
- **Buyer:** Cloud-adopting manufacturers; apparel SME factories in Rhino network.
- **Tech approach:** Cloud data platform + ML for process/quality; for Rhino, demand forecasting → flexible scheduling → short lead times (historical marketing: ~7-day delivery narratives — **vendor/press historical**).
- **Funding/revenue:** Alibaba Group IR; industrial line Not disclosed separately.
- **Stamped adjacency:** Process Adjacent (flexible mfg / scheduling lessons). Energy Adjacent if utility optimization modules used. Rhino itself **Irrelevant** as competitor to Stamped India Energy.
- **Risks:** Brand fragmentation (Brain vs Cloud products); Rhino is vertical-operated manufacturing, not a horizontal peer.

### 3. Tencent / Baidu industrial AI (compact)
- **Tencent Cloud:** Industrial internet / IoT / vision solutions for manufacturing; less iconic “industrial brain” brand than Alibaba/Huawei. Website: https://cloud.tencent.com/
- **Baidu:** Apollo/industrial vision and large model applications; Baidu AI Cloud manufacturing solutions. https://cloud.baidu.com/
- **Assessment:** Material as cloud AI suppliers; **not** primary factory-intelligence specialists in the Cognite/SUPCON sense.
- **Stamped adjacency:** Foundation/Adjacent. Specific ARR for industrial SKUs **Not disclosed publicly**.

### 4. Foxconn / Hon Hai — AI factories / physical AI
- **Names:** 鸿海 / 富士康；Fii / Foxconn Industrial Internet
- **Website:** https://www.foxconn.com/ · https://www.honhai.com/
- **What they sell / operate:** AI-enabled smart factories with digital twins (Fii Omniverse Digital Twin narratives with NVIDIA), FoxBrain analysis, NVIDIA Cloud Partner AI factories, robotics JV with Intrinsic (Alphabet) for AI factory of the future (**Hon Hai press**).
- **Sources:** NVIDIA case study: https://www.nvidia.com/en-in/case-studies/foxconn-develops-physical-ai-enabled-smart-factories-with-digital-twins/ · Hon Hai COMPUTEX / AI factory PRs.
- **Tech approach:** Simulate factory in digital twin → optimize layout/flow → AI for inspection/robotics → multi-agent orchestration experiments (NVIDIA FOX blueprint narratives).
- **Revenue:** Hon Hai group IR (electronics manufacturing giant); AI factory software Not disclosed separately.
- **Stamped adjacency:** Process Adjacent (discrete electronics methods). Energy Adjacent in facility ops. Mostly **operator**, not SaaS peer.
- **Risks:** Captive tech; hard to buy as a product if you’re not in Foxconn ecosystem.

### 5. Haier COSMOPlat / 卡奥斯 / 天智工业大模型
- **Names:** 海尔卡奥斯 COSMOPlat；天智工业大模型
- **Website:** https://www.cosmoplat.com/ · Haier group: https://www.haier.com/
- **What they sell:** Industrial internet platform for mass customization / flexible manufacturing; evolving AI-native stack with **Tianzhi industrial large model** and agent clusters (COSMO-Sphere, COSMO-iMOM, COSMO-iEMS energy management narratives in Chinese press 2025–2026). WAIC showcases of industrial world model + agents (**vendor/Chinese press**).
- **Buyer:** Appliance and multi-industry manufacturers; lighthouse factory network claims (**vendor**).
- **Tech approach:** Platform connects users-factories-resources; industrial LLM + agents for production, maintenance, energy management via natural language (**vendor**).
- **Funding/revenue:** Haier group / COSMOPlat entity figures vary by listing structure — **Not disclosed cleanly as SaaS ARR** in English sources reviewed; use Haier IR cautiously.
- **Stamped adjacency:** Process Adjacent; Energy **Adjacent** (iEMS). Method interest: industrial LLM + energy agent packaging.
- **Risks:** Platform marketing breadth; world-model claims need independent verification.

### 6. Sany / RootCloud 树根互联 (RootCloud / IROOTECH)
- **Names:** 三一；树根互联；根云 RootCloud
- **Website:** https://www.rootcloud.com/ (confirm live domain) · company historically rootcloud / irootech branding
- **What they sell:** Industrial internet platform (edge + OS + industrial apps): equipment connection, predictive maintenance, fleet/remote service, smart manufacturing, industrial chain platforms. Originated from Sany construction machinery IoT.
- **Scale claims:** Baidu Baike / company materials cite **2.5M+** connected industrial devices as of Apr 2025 — **vendor/encyclopedia**. Earlier 2019 Sany posts cited 471k+ machines.
- **Funding:** Series B ~¥500M (2019); Series C ~¥800–860M (2020) with Tencent/IDG etc. Tracxn-style aggregates ~$195M — **databases**. Primary SSE IPO filing materials (2022 attempt) disclosed revenue:
  - 2019 / 2020 / 2021 main business revenue approx **¥149.5M / ¥267.2M / ¥492.3M** (SSE disclosure PDFs) — use audited figures from filing.
  - Heavy Sany-related customer concentration historically (filing notes).
- **SSE filing PDF examples:** http://static.sse.com.cn/stock/disclosure/announcement/c/202206/001164_20220602_05XK.pdf
- **Tech approach:** Connect machines → RootCloud OS → industrial apps (PdM, remote ops, manufacturing IIoT) → increasingly AI analytics.
- **Stamped adjacency:** Foundation/Adjacent (IIoT). Energy Adjacent via machine energy/ops. Process Adjacent for equipment OEMs.
- **Risks:** Customer concentration with Sany historically; IPO path uncertain; English GTM limited.

### 7. SUPCON 中控 — TPT / TPT2 industrial large model
- **Legal:** Zhejiang Supcon Technology Co., Ltd. (SH: 688777); Hangzhou
- **Website:** https://global.supcon.com/ · TPT: https://global.supcon.com/digital/tpt · Chinese: 浙江中控
- **What they sell:** DCS/PLC/APC process automation + digital/AI: **TPT (Time-series Pre-trained Transformer)** and **TPT2** agentic industrial AI platform integrating time-series learning, simulation, first principles, multi-expert models, natural language access.
- **Tech approach (plain English):** Train transformer-style models on industrial time series with semantic tags and process logic → predict, control, optimize → agent orchestrates tools. Hybrid **AI + first principles**. Aimed at autonomous operations in process plants.
- **Public company revenue:** Total company revenue ~**RMB 9.14B** in 2024 and ~**RMB 8.05–8.07B** in 2025 per market reports — **confirm on latest 688777 filings**. TPT-specific: ~**RMB 116–120M** in 1H 2025 (~3% of operating revenue per analyst notes); management expected FY2025 TPT revenue RMB 200–300M — **analyst/press**, not a substitute for filing.
- **Vendor case claims (product page — vendor-claimed):**
  - Chlor-alkali autonomous ops: ≈1,000 t/yr soda ash reduction; ≈5% electrolyzer specific energy cut; 95% membrane life prediction accuracy.
  - Yulin Chemical ethane-to-ethylene: 99.79% abnormal event prediction accuracy; furnace start-up −4–5 hours; +0.373% ethylene yield.
  Source: https://global.supcon.com/digital/tpt
- **Hannover Messe 2026:** Software-defined controls + large industrial AI models + agentic platforms narratives (**press**).
- **Stamped adjacency:** Energy **Direct** (specific energy in process units) + Process **Direct** (closed-loop process AI). **Highest-priority China study object** for Stamped Process/Energy method transfer.
- **Risks:** Domestic China GTM; export/politics; vendor case metrics need independent audit before copying into Stamped claims.

### 8. HollySys 和利时
- **Website:** https://www.hollysys.com/ · https://www.hollysys.com.cn/
- **What they sell:** DCS/SIS/PLC, smart plant solutions, APC, predictive maintenance/asset management, simulation, virtualized control (HiaVDCS). Strong in power, chemicals, metals, rail.
- **Named public projects (company news):** Sinopec Tianjin Nangang ethylene cluster; Ansteel pellet line; Datang power plants; China Coal Xinji smart power plant with virtualized DCS — **company news**.
- **Tech approach:** Classic Chinese automation major adding smart/AI layers on HOLLiAS stack — less “startup FM brand” than SUPCON TPT, more installed-base digitalization.
- **Revenue:** HollySys listed historically (SGX/other structures evolved) — use current IR entity carefully; exact 2025 AI revenue **Not disclosed publicly** as separate line.
- **Stamped adjacency:** Process Adjacent; Energy Adjacent in power/process utilities. Foundation in plants on HollySys DCS.
- **Risks:** Competing with SUPCON for domestic DCS; AI storytelling less globalized.

### 9. Envision Digital / EnOS (远景)
- **Names:** 远景智能；EnOS
- **Websites:** Envision Group; EnOS product pages e.g. https://univers.com/products/enos/ (partner mirrors) · Microsoft Marketplace listings for EnOS
- **What they sell:** AIoT operating system for energy and industrial assets — monitor, forecast, optimize, decarbonize renewables, buildings, factories, transport, grids.
- **Scale claims:** Marketing materials cite hundreds to **1,200+** enterprise customers across years — figures **conflict across third-party pages**; treat as **vendor-claimed**, do not lock a single number without primary IR.
- **Partners:** Microsoft Net Zero / Azure narratives; various energy majors in historical PRs.
- **Revenue:** Third-party databases disagree wildly — **Not disclosed reliably publicly**; do not cite PrivCo/RocketReach estimates as fact.
- **Stamped adjacency:** Energy **Direct** (closest China energy OS peer shape). Process Adjacent when factory energy is optimized.
- **Risks:** Energy-transition positioning vs plant Energy intensity M&V; data residency deployments vary by market.

### 10. SenseTime 商汤 / Megvii 旷视 — industrial vision
- **SenseTime:** https://www.sensetime.com/ — computer vision / generative AI; smart city heritage; industrial inspection solutions exist but company is broader AI.
- **Megvii:** https://www.megvii.com/ — vision AI; manufacturing QC among verticals.
- **Funding:** Historical mega-rounds (SenseTime IPO HK; Megvii historical ~$1B+ cumulative in older press) — use latest IR, not 2018 headlines.
- **Stamped adjacency:** Process Adjacent (vision QC). Energy Irrelevant. Not PE-methods peers.
- **Risks:** Geopolitical sanctions history; pivoting narratives.

### 11. Mech-Mind Robotics 梅卡曼德
- **Website:** https://www.mech-mind.com/
- **What they sell:** 3D vision + AI for industrial robots (bin picking, depalletizing, inspection guidance).
- **Funding:** Aug 2025 round **CNY 500M (~$70M)** reported (China Growth Capital, CICC Capital, etc.; databases label Series D/E inconsistently). https://in.marketscreener.com/news/mech-mind-robotics-technologies-ltd-announced-that-it-has-received-cny-500-million-in-funding-from-ce7c50dedf8bf620
- **Stamped adjacency:** Process Adjacent (robotic vision). Energy Irrelevant.
- **Risks:** Hardware+software CapEx; not decision-layer Energy/Process.

### 12. Aqrose Technology (埃科森 / Aqrose)
- **Website:** https://www.aqrose.com/ (confirm)
- **What they sell:** Industrial AI vision for defect detection / QC.
- **Funding:** Historical totals ~$38M through 2021 in LinkedIn-class aggregates — **outdated**; 2024–25 rounds Not confirmed in this pass.
- **Stamped adjacency:** Process Adjacent (QC).

### 13. Orbbec 奥比中光
- **Website:** https://www.orbbec.com/
- **What they sell:** 3D cameras / sensing for robots, volume measurement, industrial perception.
- **Public:** Listed/China capital markets history — use IR for revenue.
- **Stamped adjacency:** Foundation (sensing). Process Adjacent.

### 14. 黑湖科技 (Hulu / Black Lake)
- **Names:** 黑湖智造；Black Lake
- **Website:** https://www.blacklake.cn/ (primary CN)
- **What they sell:** Manufacturing SaaS / MES-class platform for discrete factories — order split, quoting, scheduling, production, QC; 2024–25 messaging adds industrial AI agents.
- **Funding:** Near **¥500M Series C** (2024 Chinese press: “近5亿元C轮”). https://www.3ctvn.net/kejifunen/338433.html (secondary); 21jingji coverage 2025.
- **Scale claims:** Chinese press cites **30,000+** customers — **vendor/press**; treat cautiously.
- **Stamped adjacency:** Process Adjacent (MES/ops). Energy Irrelevant. Different GTM (high-volume SMB SaaS) vs Stamped outcomes.
- **Risks:** SMB churn; “agents” marketing vs engineering depth.

### 15. 用友 YonYou / 金蝶 Kingdee — manufacturing AI angles
- **YonYou:** https://www.yonyou.com/ — BIP / YonGPT / industrial internet & smart manufacturing modules for ERP-centric manufacturers.
- **Kingdee:** https://www.kingdee.com/ — Cosmic / manufacturing cloud / AI assistant features.
- **Assessment:** Dominant China enterprise software; manufacturing AI is an **add-on narrative** to ERP/MES, not a Cognite/SUPCON peer.
- **Stamped adjacency:** Foundation/Adjacent in China-owned India plants using these ERPs (less common than SAP, but growing in Chinese OEM supply chains).
- **Revenue:** Public CN listings — use IR; AI SKU Not broken out cleanly.

### 16. Cambricon 寒武纪 — edge chips context
- **Website:** https://www.cambricon.com/
- **What they sell:** AI accelerator chips for cloud/edge inference.
- **Stamped adjacency:** **Foundation** (compute). Irrelevant as software peer. Brief context only: Chinese industrial edge AI often assumes domestic accelerators under localization policy.

### 17. State Grid / China Southern Power Grid — energy AI adjacent
- **Examples:** Southern Power Grid “MegaWatt” model with Huawei (above). State Grid has extensive AI for grid inspection, load forecasting, defect detection (numerous Chinese technical papers/PRs).
- **Stamped adjacency:** Energy Adjacent (grid/utility AI methods). Not factory Energy peer directly — but India plants’ open-access / ToD interactions with grid AI will grow.
- **Revenue:** SOE; Not relevant as SaaS ARR.

### 18. BYD / CATL digital manufacturing (public only)
- **BYD 比亚迪:** https://www.byd.com/ — vertically integrated EV/battery manufacturing; public narratives on automation and digital factories; **no reliable public disclosure of a sellable industrial AI platform** as primary product.
- **CATL 宁德时代:** https://www.catl.com/ — battery manufacturing digitalization / lighthouse narratives; primarily operator.
- **Stamped adjacency:** Adjacent as **deployment theaters** and method sources; Irrelevant as software competitors unless a named product SKU appears.
- **Rule:** Only cite public IR/press; never invent internal AI metrics.

### 19. iFLYTEK 科大讯飞 — industrial?
- **Website:** https://www.iflytek.com/
- **Assessment:** Speech / education / LLM leader; industrial vertical assistants exist in Chinese market materials but **not** a core factory intelligence peer comparable to SUPCON/RootCloud. Treat as **low relevance** unless a named industrial control product is scoped.

### 20. CloudWalk 云从 — industrial?
- Smart city / vision heritage; industrial QC possible. **Not prioritized** without a clear manufacturing product line in English/primary sources this pass.

---

## China vs Western stack (comparison for monologue)

| Layer | West (typical) | China (typical) |
|---|---|---|
| Connect | HighByte, Litmus, Ignition, PI | Huawei iDME, RootCloud edge, domestic gateways |
| Data fabric | Cognite, Palantir | Huawei / Alibaba industrial data platforms; COSMOPlat |
| Process AI | Fero, Imubit, Aspen Hybrid | **SUPCON TPT**, HollySys smart plant, Aspen where licensed |
| Energy AI | Schneider, EnOS, startups | **EnOS**, COSMO-iEMS, State Grid AI, plant energy modules |
| Vision | Cognex, Landing, Instrumental | Mech-Mind, Aqrose, Orbbec, SenseTime/Megvii |
| MES SaaS | Tulip, Plex | 黑湖 Hulu, YonYou/Kingdee manufacturing |
| Deploy norm | Cloud SaaS OK often | **On-prem / private cloud / localization** default for many |

---

## China monologue for Stamped

“Don’t treat China as a footnote. They have **policy-scale industrial internet platforms** (RootCloud, COSMOPlat), **hyperscaler industrial stacks** (Huawei ACT pathway, Alibaba industrial cloud), and—critically—**DCS majors shipping industrial foundation models** (SUPCON TPT) with vendor case studies on specific energy and yield. Energy OS players like Envision EnOS parallel Western energy platforms. Vision/robotics AI (Mech-Mind) is world-class. For Stamped: (1) study SUPCON’s Map of time-series FM + first principles + agents as a Process/Energy method teacher; (2) assume Chinese OEM plants in India may demand localization patterns; (3) do not confuse Rhino or Foxconn captive factories with sellable SaaS peers; (4) never invent Chinese funding or plant counts—cite filings and vendor pages.”

---

## Source appendix (China)

- Huawei CONNECT industrial intelligence: https://www.huawei.com/en/news/2025/9/hc-act-industrial-intelligence
- SUPCON TPT2: https://global.supcon.com/digital/tpt
- SUPCON PR TPT launch (2024): https://www.prnewswire.com/news-releases/building-industrial-intelligent-engine-reshaping-a-new-paradigm-of-industrial-applications-supcon-unveils-groundbreaking-time-series-pre-trained-transformer-tpt-302166886.html
- COSMOPlat: https://www.cosmoplat.com/
- Haier WAIC industrial AI press (example): https://www.haier.com/press-events/news/20260721_293355.shtml
- RootCloud Baike: https://baike.baidu.com/en/item/RootCloud/3452078
- RootCloud SSE filing: http://static.sse.com.cn/stock/disclosure/announcement/c/202206/001164_20220602_05XK.pdf
- Mech-Mind funding: https://in.marketscreener.com/news/mech-mind-robotics-technologies-ltd-announced-that-it-has-received-cny-500-million-in-funding-from-ce7c50dedf8bf620
- Foxconn NVIDIA case: https://www.nvidia.com/en-in/case-studies/foxconn-develops-physical-ai-enabled-smart-factories-with-digital-twins/
- Alibaba Industrial Brain docs: https://help.aliyun.com/zh/industrial-intelligence/
- HollySys: https://www.hollysys.com/
- EnOS product mirror: https://univers.com/products/enos/
- 黑湖 Series C secondary: https://www.3ctvn.net/kejifunen/338433.html
- YonYou: https://www.yonyou.com/
- Kingdee: https://www.kingdee.com/
- Orbbec: https://www.orbbec.com/
- Mech-Mind: https://www.mech-mind.com/
- SenseTime: https://www.sensetime.com/
- Cambricon: https://www.cambricon.com/
- BYD: https://www.byd.com/
- CATL: https://www.catl.com/

### Fetch / confidence flags (China)
- RootCloud English site availability varies; prefer filing + Baike + 36Kr-class for financing history.
- EnOS customer counts conflict across marketing mirrors — do not freeze a single number.
- TPT revenue split relies on analyst notes + company revenue filings — cite 688777 primary when updating.
- Hulu 30k customers is press/vendor scale — unverified independently.
- iFLYTEK / CloudWalk industrial depth intentionally deprioritized pending clearer product evidence.

---
*End of China annex.*


---

## Enrichment — How Chinese industrial AI actually deploys (for India plants owned by Chinese OEMs)

### Typical architecture pattern (composite from Huawei / SUPCON / RootCloud public materials)
1. **Edge gateways** collect PLC/DCS/CNC data on-prem.
2. **Private cloud or on-prem cluster** (often Ascend or domestic GPU) hosts industrial models — data may never leave the province/group.
3. **Industrial apps** (PdM, scheduling, energy, quality) sit on a platform (RootCloud / COSMOPlat / FusionPlant / vendor DCS digital layer).
4. **Agents / copilots** (2025–26 wave) wrap natural language on top of those apps — Huawei Versatile platform claims workflows with 100+ steps (**vendor**).
5. **Human accountability** remains explicit in SOE plants; “autonomous” usually means supervised optimization inside envelopes (SUPCON TPT framing).

### What Stamped should learn without entering China GTM early
| Lesson | Source archetype | Stamped action |
|---|---|---|
| Industrial FM on time series + first principles | SUPCON TPT | Prototype semantic tags + hybrid constraints for one process unit |
| Energy as first-class industrial agent | COSMO-iEMS / EnOS | Package Energy agents with M&V, not chat only |
| Device connection at millions scale | RootCloud | Don’t chase device count; chase verified KPI |
| Captive OEM digital twins | Foxconn×NVIDIA | Ignore as product; watch as customer sophistication rises |
| MES SaaS agents for SMB discrete | 黑湖 Hulu | Process GTM for India SMBs may need lighter UX — but Stamped stays outcomes not seats |

### Policy context (non-exhaustive)
- MIIT industrial internet + smart manufacturing demonstation factories created demand for platforms.
- Data security / CSL / localization norms push on-prem.
- Domestic DCS substitution (SUPCON, HollySys) creates a control-layer AI beachhead Western startups lack.

### Additional China sources
- SUPCON TPT PR 2024: https://www.prnewswire.com/news-releases/building-industrial-intelligent-engine-reshaping-a-new-paradigm-of-industrial-applications-supcon-unveils-groundbreaking-time-series-pre-trained-transformer-tpt-302166886.html
- Huawei CONNECT 2025: https://www.huawei.com/en/news/2025/9/hc-act-industrial-intelligence
- 36Kr-class SUPCON AI commentary: https://eu.36kr.com/en/p/3978416117464071
