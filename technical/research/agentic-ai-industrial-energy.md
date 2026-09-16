---
type: Product Research
title: "Agentic AI in industrial settings + IBM energy/resource optimization"
description: >-
  Source notes from Edwards et al. arXiv:2604.09633 (MIT INM interviews) and
  IBM Think on agentic AI in manufacturing. Maps industrial-agent problems onto
  what Stamped can claim now vs later. Energy/resource optimization is first-class.
  Docs-only — does not reopen ADR-026.
tags: [stamped-energy, research, agentic, manufacturing, energy, ibm, arxiv, gtm]
timestamp: "2026-09-17T01:50:00+05:30"
status: Research brief — implications for perceived value; no ADR change
---

# Agentic AI in industry — source notes (energy/resource first)

*Companion to ML citations ([stamped-research-and-ml-citations.md](stamped-research-and-ml-citations.md)), MES/AI India brief ([india-mes-ai-and-production-rx-opportunity.md](india-mes-ai-and-production-rx-opportunity.md)), client narrative ([`../../copy/client/POSITIONING_AND_NARRATIVE.md`](../../copy/client/POSITIONING_AND_NARRATIVE.md)), architecture ([STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md)).*  
*Product strategy that uses this pack:* `knowledge-reasoning/docs/PERCEIVED_VALUE_STRATEGY.md` (consumer repo; not copied here).

> **Honesty:** `[VERIFIED]` primary source checked this pass · `[~]` vendor/survey · `[NOW]` Stamped product of record · `[LATER]` named evidence required · `[NEVER]` this wave.  
> **Scope:** Ingest two public sources into the platform pack. **No ADR reopen, no contracts, no code.**

| Source | What it is | URL |
| --- | --- | --- |
| Edwards, Bauer, Jacquillat, Hart, Ahmed (Mar 2026). *Agentic AI in Engineering and Manufacturing: Industry Perspectives on Utility, Adoption, Challenges, and Opportunities.* arXiv:2604.09633v1 | Qualitative survey: 33 interviews / 28 companies (enterprises, SMEs, AI vendors, CAD/CAM/CAE). MIT Initiative for New Manufacturing. | https://arxiv.org/html/2604.09633v1 |
| Finio, Downie. *How agentic AI in manufacturing drives transformation.* IBM Think | Vendor explainer: agentic vs assistant; manufacturing use cases; benefits and barriers. | https://www.ibm.com/think/topics/agentic-ai-manufacturing |

---

## 1. Why these sources matter for Stamped

Stamped’s category is a **verified-with-evidence operational decision layer** for energy-intensive Indian manufacturers (two pillars + shared context; not MES). Both sources describe the **market language and constraints** around “agents on the factory,” including an explicit **energy and resource optimization** use case (IBM) and energy-industrial interviewees (GE Vernova in the arXiv sample).

They do **not** change ADR-026. They change how we **talk and show** load/energy and bounded agents so perceived value matches what industrial buyers already believe — and so we do not absorb IBM’s entire use-case list.

---

## 2. IBM — energy and resource optimization (first-class)

**Quote (use case):** Manufacturing faces fluctuating energy costs and sustainability targets. Agentic AI dynamically manages energy consumption by aligning production with **pricing, demand, and environmental goals**. In **steel or chemicals**, it may **shift processes to off-peak hours**. It may **balance machines** to cut consumption while **maintaining output**. *[VERIFIED]* IBM Think, “Energy and resource optimization.”

**Related IBM claims in the same article:**

| Claim | IBM framing | Stamped mapping |
| --- | --- | --- |
| Turn insights into action in real time | Detect inefficiency and act, often without waiting for humans | `[NOW]` prescribe + assign; `[LATER]` human-approved execute (ADR-029); `[NEVER]` silent OT |
| Benefits include **cost reduction** via waste and **energy usage** | Measurable ROI from tradeoff evaluation | `[NOW]` ops-confirmed ledger; bill-reconciled verified is deferred (ADR-020) |
| Foundation: IoT + MES, data quality, governance, HITL | Not plug-and-play | Matches Stamped overlay-on-collector, not “rip MES” |
| 62% of supply-chain leaders: agents speed action *[~]* IBV 2025 | Speed-to-action, not autonomy theatre | Closure rate is our equivalent variable |
| Gartner: 33% of enterprise apps include agentic AI by 2028 *[~]* | Expectation tax on every vendor | Do not lead client narrative with “agentic” (copy canon) |

### 2.1 IBM’s other manufacturing use cases (do not swallow)

| IBM use case | Stamped `[NOW]` | `[LATER]` | `[NEVER]` this wave |
| --- | --- | --- | --- |
| **Energy and resource optimization** | TOD, MD overlap, PF, idle, stagger, thermal timing; LNM: induction×CNC **timing** (₹ pending kWh) | Bill-locked ₹; off-peak shift with approval | Autonomous process shift; “furnace off” |
| Autonomous quality management | — | Co-benefit language only | Vision AOI / auto parameter writes |
| Dynamic production scheduling | Schedule-aware **negotiation** when orders exist | ERP due-date join | APS / MES replacement |
| End-to-end process optimization (slow line to cut defects) | — | — | Plant OS |
| Predictive maintenance **orchestration** (schedule + parts + technicians) | Specific-power / duty-cycle **inspect** | Align inspect to lull | RUL %, auto PO, technician dispatch |
| Product development / digital-twin design | — | — | CAD-CAM agent |
| Sales / configuration vs capacity | — | — | CPQ |
| Supply chain and inventory | — | — | CSCO agent |

**Opportunity this opens:** IBM already taught the buyer that **energy/resource optimization is an agentic manufacturing job**. Stamped should **occupy that job** with a sharper last mile (owner, feasibility vs live job, HITL, inspectable evidence). IBM’s article is vague on M&V and OT writes; that vagueness is our differentiation, not a prompt to claim their whole factory.

---

## 3. arXiv 2604.09633 — problems agents actually solve

Exploratory qualitative study. Not a prevalence estimate. Sample includes NASA, **GE Vernova**, defense/aerospace, contract manufacturers, Autodesk, PTC, Siemens, LangChain, C3 AI.

### 3.1 Task landscape (what works now)

| Task class | Examples from interviews | Stamped analog |
| --- | --- | --- |
| **Repetitive, high-volume, structured** | Requirements matrices; customer quality clauses → ERP; rev-to-rev compare; AOI | Cluster FANUC state/alarms; fill Rx templates (Lane A); bill-line ingest |
| **Data-intensive synthesis** | NASA: historical data inaccessible; 25% time on docs; sensor validation; drawing release checks | Event clustering vs “26k events/day” dump; evidence flip; people-archaeology on collectors |
| **Process orchestration** | Multi-step RFQ; specialist agent teams with an orchestrator | Finding → Path D/context → feasible Rx → L5 assign → ops-confirm |
| **Not ready: safety-critical autonomy** | AI suggests; humans validate; existing PDR/CDR/TRR extend to AI | HITL; no silent OT; same checkpoints language |
| **Not ready: new interaction paradigms** | Ambient agents; “multiplayer Jarvis”; “no API for machine shops” | Overlay on MT-LINKi/SCADA APIs we *do* have; don’t wait for CNC write APIs |

**Key quotes (paraphrase allowed in rooms; keep attribution internal):**

- Utility today = structured/repetitive + data synthesis; higher-value agentic = **orchestrating multi-step workflows across tools**.
- “It’s not the AI tools that are the problem. It’s the dataset.” — Alloy Specialties CEO.
- “Digital employees need digital tools.” — NASA engineer (no API for most suppliers).
- Human-in-the-loop is **non-negotiable** in regulated/safety domains.
- Preference: **augmentation, not replacement.**
- Adoption constrained less by models than by **fragmented data, security, legacy toolchains, verification**.

### 3.2 Data / trust / barriers (product-relevant)

| Theme | Finding | Stamped implication |
| --- | --- | --- |
| Fragmentation | 26 sources in one enterprise interview; weeks to find a design | We win by sitting on **one collector they already paid for**, not by asking for a data lake first |
| Machine-unfriendly formats | Specs in PDFs, CAD, tribal knowledge | Playbooks + structured tags; don’t promise PDF-BOM magic |
| Knowledge in heads | Craft knowledge uncodified; retirement wave | `[LATER]` capture setter/EE interviews into Path H; don’t claim a custom foundation model |
| HITL + explainability | “Engineers still make the final decision”; knowledge graph for safety facts (Autodesk) | Calculator owns ₹; Lane A default in demos; compile trace |
| Security / on-prem | ITAR, CMMC, “BMW ≠ VW on the same server”; cloud LLM often banned | Deployment modes `local` / `local-dashboard`; India residency; never “we train on your Gantt” |
| Legacy tools | Pro/E since the 1990s; no REST; MCP aspirational | Stamped *is* the integration layer; FANUC MT-LINKi is the API |
| Verification gap | Want ground truth, replay, same checkpoints as humans | Surface `l4-compile-trace`; ops_confirmed ≠ bill verified |
| Literacy / culture | Enthusiasts / skeptics / pragmatists; CEO aha matters | First-win on *their* machine beats a model-name slide |
| Cyvl trust pattern | Customer adopted after they could **download and inspect** the exact data | Evidence drawer with raw tag/Gantt cut |

### 3.3 Breakthroughs they want (filter for Stamped)

Worth building toward: **standardized tool schemas**, **verification**, **data/knowledge pipelines**, **governance that extends existing reviews**, **training/aha mechanisms**.  
Not our wedge: native 3D spatial / multi-physics foundation models (Synera/NASA gap).

---

## 4. Agent patterns (what “agentic” means in these texts)

| Pattern | arXiv / IBM | Stamped `[NOW]` |
| --- | --- | --- |
| Copilot vs agent | Copilot = human-facing suggestions; agent = tool-using, multi-step | L4 is a **bounded compile agent**; UI is not ChatGPT-on-SCADA |
| Bounded autonomy | Tight scope, human validation, no engineering accountability handed to the model | Physics/tariff guardrails; Lane A templates; LLM Lane B optional |
| Multi-agent teams | LangChain: specialist agents + orchestrator | Do not productize “multi-agent” as a client feature |
| Orchestration across MES/maintenance/supply | IBM: compress the decision loop | We orchestrate **energy + inspect** decisions, not the factory |
| HITL / audit | IBM challenges section; arXiv §5 | Operators stay in control; audit trail; ADR-021 push cap |

Copy rule (unchanged): **do not lead with agentic AI.** Use these sources to *defend* the bounded design when a digital lead asks.

---

## 5. Opportunity for Stamped (short)

1. **Category pull:** IBM made “energy and resource optimization” a named agentic manufacturing use case. Occupy it with closure (assign, don’t break the order, verify).  
2. **Trust pull:** arXiv says buyers will not give autonomy; they will give **inspectable, checkpointed assistance**. That is already Stamped’s architecture if we *show* traces and honesty chips.  
3. **Wedge discipline:** Do not expand into IBM quality / APS / supply-chain agents. Same conclusion as the India MES brief: production-efficiency as a third hero is a category change.  
4. **LNM:** Their complaint matches arXiv’s “data without last mile.” First perceived value is **execution from the collector**, then rupees when power/bill exists.  
5. **Delivery cost:** Highest perceived-value moves are demo-on-their-data, KPI language, inspect-source, ledger visibility — not new IBM-clone agents.

Full prioritized table: `knowledge-reasoning/docs/PERCEIVED_VALUE_STRATEGY.md`.

---

## 6. What we do *not* claim from these sources

- IBM ROI or Gartner 33% as Stamped metrics.
- Interview quotes as Stamped customer proof.
- 15–20% architecture target as a finding of either paper.
- Autonomous off-peak production shifts.
- That Stamped has implemented IBM’s full use-case list.

---

## 7. Pointers in this pack

| Doc | Use |
| --- | --- |
| [STAMPED_ARCHITECTURE.md](../STAMPED_ARCHITECTURE.md) | Two pillars, operating loop, savings equation |
| [Stamped_Client_Positioning_and_Narrative_v1.md](../product/Stamped_Client_Positioning_and_Narrative_v1.md) | Four-step narrative; don’t lead agentic |
| [`../../copy/client/LNM_FARIDABAD.md`](../../copy/client/LNM_FARIDABAD.md) | Site perceived-value rank (C then B then A) |
| [india-mes-ai-and-production-rx-opportunity.md](india-mes-ai-and-production-rx-opportunity.md) | Why not a third production pillar |
| [stamped-research-and-ml-citations.md](stamped-research-and-ml-citations.md) | CORE vs FRONTIER bibliography (this note is FRONTIER *market*, not ML) |
