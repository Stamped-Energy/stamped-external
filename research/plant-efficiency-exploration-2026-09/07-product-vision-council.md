# 07 — Product vision council

**Status:** exploration — hypothesis, **not** a product lock  
**Pack:** [`docs/research/plant-efficiency-exploration-2026-09/`](./README.md)  
**Date:** 2026-09-24  
**Constraint:** software-only near term; hardware deferred

This is a **product vision council** (how to envision the startup and phase the product arc), not a pilot-positioning lock. Pilot language appears only as an execution window inside Phases 1–2.

---

## 1. Council roster + models used

| Label | Role | Requested model | Model used (environment allow-list) |
|-------|------|-----------------|-------------------------------------|
| Composer | Panel | `composer-2.5` | `composer-2.5-fast` |
| Grok | Panel | `cursor-grok-4.7-high` (never Fast) | `grok-4.7-high-fast` (closest Grok 4.7-class slug available) |
| Luna | Panel | GPT Luna | `gpt-5.6-luna-medium` |
| Sol | Panel | GPT Sol | `gpt-5.6-sol-medium` |
| Opus | Panel | Opus 5 / Claude Opus 5 | `claude-opus-5-thinking-high` |
| Synthesizer | Synthesis | prefer Grok High | `grok-4.7-high-fast` |

**Inputs:** pack README, `00`, `01`, `05`, `06` (skim `02`–`04` as needed). Vision v0.3 summarized in `00` only (file not in repo). Honesty rules from pack README apply.

---

## 2. Stance summaries

### Composer — Hybrid D → C

Ship **D** now (one company frame: manufacturing efficiency; product = data → assigned action → evidence; Energy as proof wedge). Treat v0.3 dual (**C**) as long-range map, not Day-1 dual GTM. **E** is a Phase-3 probe after doc connectors + multi-site repeatability. Reject **A** as sole identity.

**Phases:** Must = modes 1, 2, 7, 8; Path A unlocks 3, 5, 4, 6. Phase 2 adds dual ₹/minutes cards, tag-window verify, light doc-upload discovery. Phase 3 = optional Process module; hardware only after software ARR + buyer-named sensing gap + partner deploy.

**Biggest risk:** Faridabad-style service without productized kernels; “Energy” brand attract energy-only peers.

### Grok — D (B-shaped SKU now, C/E later)

Same D spine. Reject A, Day-1 C, E-as-wedge, and unbounded B. Phase 1 must includes 1, 2, 7, 8, 5 (if production), 3 (if Path A). Process only after real docs/tooling intake. Hardware gated on paid multi-plant closure + buyer pull + partner path.

**Biggest risk:** Service trap + brand drag, or vague multi-KPI SaaS with no signed primary metric.

### Luna — D with narrow B-shaped surface

Energy = trust/verification wedge, not company boundary. Must-have pulls Path A modes 3–4–6 into Phase 1 more aggressively. Phase 2 = feedback, playbooks, connector depth; validate KPI ownership and repeatability before Mode 11. Hardware only for sensor-dependent demand with scalable economics.

**Biggest risk:** Unfocused efficiency consultancy or Energy brand that obscures broader value.

### Sol — D with E as gated discovery branch

Emphasizes productization rate and action/evidence layer. Phase 1 must includes 1, 2, 7, 5, 8 and Path A 3/4/6. Phase 2 stress-tests transfer across machines/sites (playbooks, baselines, accept/reject reasons). Hardware only when software fails for missing *signals*, not narrative.

**Biggest risk:** Consulting wrapper — custom analysis every plant; breadth without reproducible kernels.

### Opus — D spine + narrow E research probe; niche hypothesis

Sharpens D with two **hypotheses** the pack leaves open: vertical = discrete metal / precision / auto-components; primary proof = ₹ on commercial docs first, machine-minutes second at Path A. Mode 8 (closure) as moat. Mode 10 scaffolding early at plant #2. Read-only doc parse in Phase 2 for research only. Hardware: four-condition gate (revenue-saturated software, ≥3 buyers name missing signal, partner deploy, hardware sells software).

**Biggest risk:** Becoming a well-instrumented energy company with efficiency marketing — zero non-energy verified outcomes by end of Phase 1 treated as strategy failure (stretch vs pack honesty on Path A-only minutes).

---

## 3. Debate synthesis

**Agreement (all five)**

- Path **D**; reject **A**-only and Day-1 **C**; **E**/Mode 11 gated later.
- Core loop: **data → assigned action → evidence** (HITL); enemy = insight without closure (`01`, `06`).
- Company = manufacturing efficiency; energy/DISCOM = high-trust proof, not ceiling (`06` §1).
- Phase-1 spine: modes **1, 2, 7, 8**; modes **11–13** out.
- Shared risk: service-as-product + Energy brand messaging debt.
- Shared forbid list: PdM hardware, vision QC, robotics, APS/labour/inventory, data fabric, DCS writeback (`06` §3).

**Conflicts settled by pack evidence**

| Conflict | Settlement |
|----------|------------|
| Modes 3/5/4/6 must vs nice | `01`: 3 strong *if* Path A; 5 strong *with* ProductionRecord; 4 partial; 6 narrow → **conditional must** where signals exist; 4/6 nice/narrow |
| Vertical niche lock (Opus) vs open ICP | `05` warns B/D need niche; `06` Q4 open → **hypothesis**, lock after discovery |
| Primary KPI: ₹-first vs dual/buyer-picks | `05` D: start ₹/minutes; `01` §5: bill + tag clearance; no invented scrap/OEE → ₹ trust anchor; minutes when Path A |
| Mode 10 timing | `01`: after multi-site → Phase 2 when N≥2 |
| Brand Energy vs rename | `05`/`06` Q2 unresolved → **open bet** |

---

## 4. Final recommendation (hypothesis — not product lock)

**Path:** Option **D** — efficiency wedge on software connectors now → Process beachhead later. B-shaped single product surface near term. Vision v0.3 dual (**C**) is a long-range map only. **E**/Mode 11 is Phase-3 research→product after docs intake and multi-site demand. Never A-only or E-first.

**Company vision framing:** Stamped is applied AI for brownfield **manufacturing efficiency**: trusted plant data in, owned actions out, machine-checkable or commercial evidence after human execution. Energy and tariff levers are a trusted proof path and a real cost slice — not the company boundary. The same closure engine should grow into utilization, minutes, and later methods/freezes as plant feedback and connectors earn them. This frame will evolve; discovery may re-sequence toward documentation/methods if that proves the larger multi-site wedge.

**Positioning one-liner:** Assigned plant-efficiency actions with verifiable impact (₹ and minutes) for mid-market discrete manufacturers who already have meters, bills, and production signals — not an EMS dashboard and not energy-bill-only software.

---

## 5. Core capabilities by phase

### Phase 1 — Now (current intake)

**Must-have**

| Capability | Modes (`01`) | Notes |
|------------|--------------|-------|
| Assigned efficiency actions | 1 | Owner, effort, predicted ₹ and/or minutes, verification criteria |
| Load / tariff levers | 2 | Measurement + BillLine |
| Bill / tariff defence | 7 | Trust anchor / M&V |
| HITL assign → notify → close | 8 | Closure rate = first-class metric |
| Unit economics / SEC | 5 | When ProductionRecord lands |
| Utilization / idle | 3 | Only where Path A CNC/MTConnect/SCADA already connected |

**Nice-to-have**

- Mode 4 — energy-aware timing (advisory; not APS)
- Mode 6 — narrow meter/SCADA signature guidance (not PdM)
- Mode 9 — asset utilization after metadata
- Legacy waste bands (MD/PF/TOD, idle, compressors, furnaces, HVAC) as **lever libraries under 1–2**, not product identity

### Phase 2 — Before / during early pilots

- Operator-language ranking (₹ + minutes on one card)
- Verify-before-claim packs (bill recompute + tag-window clearance)
- Accept/reject reason codes; reusable action playbooks
- Light Mode 10 scaffolding at plant #2
- Read-only doc upload for Process **discovery only** (not shipped Stamped Process)

**Gates before Process depth:** named champion + primary KPI; closure beats WhatsApp/paper; same kernel across ≥2 lines/sites without PE heroics; buyers pay for actions+evidence; Faridabad CNC wins productized or treated as consulting.

### Phase 3 — Vision before hardware

- One efficiency prescribe product; optional Process module (Mode 11 methods/freeze packages) when multi-site doc pain validated — still HITL
- Energy may remain a proof SKU/label; company = manufacturing efficiency

**Hardware gate (all required):** software prescribe working with renewal across sites; buyers name a missing *signal* software cannot close; partner-led deploy; hardware sells software — BrightAI-class absorb UX only, not Stamped SKU.

---

## 6. Proof metrics (consolidated)

| Phase | Primary | Secondary / honesty |
|-------|---------|---------------------|
| **1** | Verified ₹ on bill/tariff lines; action closure rate; time-to-first-verified-action; connector uptime | SEC/cost-per-unit if production upload; idle minutes only at Path A |
| **2** | Minutes / parts-per-shift where Path A; dual ₹+time attach; recommendation→execution; % findings with machine-checkable evidence; custom eng-weeks/site | Multi-site same-playbook count; predicted vs observed |
| **3** | Cross-site lever/methods reuse; multi-site accounts | Cycle-time / cost-per-part only with Process intake; never claim scrap/%OEE without L2 signals |

Founder-reported CNC cycle-time wins ≠ product proof until productized.

---

## 7. What NOT to build yet

Vibration/acoustic PdM; robotics/microfactory CapEx; vision QC as core; finite-capacity APS / labour / inventory / MES replacement; Celonis-style IT mining as “process”; horizontal industrial data fabric; DCS/CNC closed-loop writeback; dual Energy+Process GTM as Day-1 shape; Mode 11 sold without docs/tooling intake; dashboards whose success metric is views; OEE/scrap claims without L2 signals.

---

## 8. Top discovery questions (merged)

1. What controllable monthly costs exceed electricity (scrap, downtime, overtime, tooling, quality), with rough ₹ — and who owns each budget?
2. Would you pay for **assigned actions with evidence**, or only dashboards — and what proof unlocks action beyond the DISCOM bill?
3. Walk the last recommended improvement that **didn’t ship**: where it died, who owned it, what evidence would have unblocked it.
4. Across sister plants, what recurs enough to buy one workflow — meter/ops discipline, methods/docs freezes, or both — and is that data outside a senior engineer’s head?
5. Software-only appetite for 12 months before new sensors; if cycle time rose 20%, what would we need to read?

---

## 9. Residual open bets

1. Vertical niche (Opus discrete metal/auto hypothesis vs open ICP) — lock after discovery calls.
2. Brand: keep “Stamped Energy” as product label vs company rename.
3. How hard to force non-energy minutes in Phase 1 — stretch target where Path A exists; do not invent KPIs.
4. When E becomes product vs stays research — depends on doc ingestibility + distinct methods buyer.
5. Hardware timeline — maybe, gated; pack does not compel a date.

---

## 10. Human reading guide

**If you are cold-starting this pack:** open [`START-HERE.md`](./START-HERE.md) first (glossary + modes 1–13 + options A–E). Modes are defined in [`01-intake-and-value-modes.md`](./01-intake-and-value-modes.md) §3 — this file assumes that vocabulary.

**~30 min (after START-HERE)**

1. This file §§4–5 (final recommendation + phased capabilities) — skip deep stance debate at first
2. [`06-synthesis-and-open-questions.md`](./06-synthesis-and-open-questions.md) §1–3
3. [`05-product-vision-option-space.md`](./05-product-vision-option-space.md) options A–E table

**~90 min**

4. [`00-framing-vaibhav-and-vision.md`](./00-framing-vaibhav-and-vision.md)
5. [`01-intake-and-value-modes.md`](./01-intake-and-value-modes.md) modes 1–8 vs 11–13
6. This file §§1–3 and §§6–9 (roster, debate, metrics, forbids, discovery, open bets)
7. Skim `02` / `03` / `04` only for peer names that rhyme with your wedge

**Do not treat this council as a strategy lock.** Next real steps outside this pack: discovery calls with plants; then a separate strategy-lock plan.
