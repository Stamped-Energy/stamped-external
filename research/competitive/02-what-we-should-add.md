# What Stamped should add (from competitive review)

**As-of:** 2026-09-22 (Asia/Calcutta)  
**Inputs:** `00-stamped-capability-baseline.md`, `01-vendor-research-raw.md` (+ deepening pass), `gap-*.md`  
**Framing lock:** two pillars + shared context; software overlay; no invented ₹ savings.

## How to read this

Only items that are:

1. **Addable as Stamped software** (or light partner for sensors/meters), and  
2. Fit **energy + equipment** Findings → ₹ Prescriptions → closure → verify, and  
3. Are **not** “become a BESS EMS / meter OEM / ABB OPTIMAX.”

Prefer fewer strong bets over a laundry list. Competitor marketing % and ₹ figures are **not** targets.

---

## Priority 1 — build soon (software)

### 1. Live SEC / kWh-per-tonne desk views
- **Plain description:** Make “kWh per tonne (or per unit) by line / shift / machine” a first-class screen and Finding input — not a buried engine. Needs production totals (CSV/ERP soft-join is enough to start).
- **Which competitor surfaces it:** VolTwin (hero), Tech OVN (factory SEC), lightly LTTS intensity language.
- **Why it fits Stamped:** Same data path we already have (`sec` / `enpi` + `production_record`); turns India DC / CFO questions into Prescriptions (“Line 3 SEC drifted — owner, effort, ₹”).
- **Rough layer:** L2 features + L3 SEC/EnPI + L6 views; contracts already touch production_record.
- **Notes:** Never invent ₹ from SEC alone; join to tariff only where defendable.

### 2. PAT / ISO 50001 / BRSR **evidence export** packs
- **Plain description:** One-click (or guided) export packs: EnPI baseline/target/trend; PAT M&V-style consumption evidence; BRSR Scope 2 / energy intensity **evidence** for the customer’s filing team — we enable, we do not file or trade certificates.
- **Which competitor surfaces it:** VolTwin (strong), Tech OVN (exports), LTTS (ISO one-click), ABB (ISO reporting).
- **Why it fits Stamped:** Compliance register already says enable-not-register; RFPs lose to “audit-ready PDF” even when our Rx are better.
- **Rough layer:** L5 evidence + L6 export; L3 EnPI/SEC feeds; bill/metadata intake stays honest.
- **Notes:** Park ESCert trading UI and full ImpacTwin-class ESG suite.

### 3. Physics / residual “verify before you trust” gate (named product story)
- **Plain description:** Productize what we already believe: drifted meters, offline sensors, and bad joins must fail closed before a Finding becomes a money Prescription. Say it in founder/plant language (“we check the reading makes physical sense”).
- **Which competitor surfaces it:** LTTS EnergiSensEI (hero differentiator).
- **Why it fits Stamped:** Matches TOW-P baseline-of-record + Lab dual-lane + honesty bar; differentiates vs black-box “AI saved 12%” vendors.
- **Rough layer:** L3 detection gates + Lab vs L4 outbox; L6 trust/evidence flip copy.
- **Notes:** Do not rebrand as agent theatre; keep forecast models shadow-only.

### 4. Stronger MD / ToD **early-warning Prescriptions** (still human-owned)
- **Plain description:** Sharper rolling demand alerts and ToD exposure Findings that land as assigned Rx (stagger, shed, pre-cool, shift non-critical) **before** the billing window locks — without writing to batteries or PLCs.
- **Which competitor surfaces it:** EnerCog (executes via BESS), VolTwin (MD alerts), Tech OVN (demand alerts), ABB (closed-loop peaks).
- **Why it fits Stamped:** We already ship MD/ToD/load-management engines; competitors win attention on “we stop the spike.” We win on owner + verify.
- **Rough layer:** L3 load_management / incomer / tariff + L4 templates + L5 WhatsApp urgency.
- **Notes:** Execution via battery = partner EMS, not us.

---

## Priority 2 — build next

### 5. Human-guided soft writeback (Wave C) — beachhead only
- **Plain description:** Opt-in, human-approved soft actions (e.g. idle aux stop, approved setpoint, schedule release) via ActionIntent — never silent, never e-stop / FANUC cycle start / PCS charge commands.
- **Which competitor surfaces it:** LTTS “Act” ambiguity; EnerCog/ABB closed-loop (we refuse their depth).
- **Why it fits Stamped:** Already **specified** (ADR-029); closes “you only recommend” objections without becoming OPTIMAX.
- **Rough layer:** L5 ActionIntent + edge write path; contracts exist.
- **Notes:** Fail-closed; fatigue budget; audit trail.

### 6. Deeper production / ERP soft-joins (read-only)
- **Plain description:** Richer joins from SAP/Oracle/Dynamics/Tally-class exports or APIs so SEC and idle Rx know the real order/SKU — still **read orders for energy Rx**, not schedule production.
- **Which competitor surfaces it:** VolTwin / ImpacTwin ERP stacking; Tech OVN CSV production for SEC.
- **Why it fits Stamped:** Unlocks Priority 1 SEC without a MES pillar.
- **Rough layer:** L1 ingest + L2 production_record + L3 soft-join engines.
- **Notes:** ADR-026 forbid third pillar / OEE hero.

### 7. Ask Analyst + report agents as thin packaging (not a new platform)
- **Plain description:** Package existing Ask Analyst + evidence exports as clear “ask / report” surfaces so buyers who saw LTTS agents still recognise the desk — without five-agent hype.
- **Which competitor surfaces it:** LTTS five agents.
- **Why it fits Stamped:** UX clarity over new intelligence claims.
- **Rough layer:** L4 + L6.
- **Notes:** Secondary to Prescription flip cards.

### 8. Advisory demand forecast in Lab (shadow)
- **Plain description:** Show Trends-like early warning in Lab/shadow; never let it become ₹-of-record.
- **Which competitor surfaces it:** LTTS Trends; ABB AutoML forecasting.
- **Why it fits Stamped:** Challenger models already shadow-only — expose carefully.
- **Rough layer:** L3 Lab + L6 Lab views.
- **Notes:** Hard rule: no autonomous forecast money claims.

---

## Priority 3 — nice later / evidence packs

- **Multi-plant hub rollup** of energy Findings and evidence exports (VolTwin hub-and-spoke) — after single-site Rx quality is boringly good.
- **PLI / incentive documentation exports** if a deal asks (VolTwin mentions; thin public depth) — report-only.
- **Read-only utility protocol connectors** (IEC 104 / DNP3 class) where a hybrid site already has EnerCog/ABB and we only need telemetry — ingest, not control.
- **Camera occupancy as covariate** — remains research-only; not P0.

---

## Explicitly do NOT build (and why)

| Do not build | Why |
| --- | --- |
| **BESS autonomy / PCS charge-discharge writer** | EnerCog’s core; conflicts with overlay + “no battery-storage claim.” |
| **Solar PPC / DG-PV sync / zero-export controller** | Control product; partner. |
| **Meter OEM / Titan-class DIN-rail / white-label meters** | Tech OVN’s core; we are meter-agnostic by ADR. |
| **On-meter relay disconnect product** | Autonomous OT write non-goal. |
| **Closed-loop OPTIMAX-style EMOS / VPP / APC-MPC** | Different category; “do not build ABB.” |
| **ESCert trading desk / full BRSR filing platform** | Compliance product creep; enable evidence only. |
| **WAGES / water-first / full Scope 3 ESG suite** | Outside two pillars. |
| **MES / OEE hero / production-efficiency third pillar** | ADR-026 forbidden. |
| **Forecast or marketing % as bill-verified savings** | Honesty bar; LNM tape can be ₹0. |

---

## Partner instead of build

- **EnerCog-class BESS EMS / Solar PPC** at hybrid solar+storage sites — they dispatch; we Prescribe and verify around their telemetry.
- **Tech OVN Titan / Titan Audit or any Class 0.5S + ESCO audit path** — they meter; we are the intelligence overlay on MQTT/Modbus.
- **CT / clamp retrofit installers** for non-digital meters (VolTwin-style brownfield).
- **ABB OPTIMAX / any plant EMS** — coexist; ingest tags; never claim we replace closed-loop.
- **LTTS-class SI / build-operate** when the buyer needs Assess–Operate delivery — Stamped remains the product.

---

## Opinionated summary (for Vinayak)

Build the things that make Stamped obviously better at **India HT money truth + assigned next steps + honest evidence**: live SEC desk, compliance **evidence** packs, named verify-before-trust, sharper MD/ToD Rx. Ship Wave C soft writeback only as a controlled beachhead. Partner everything that smells like **battery control, meters, or ABB**. If a slide needs a savings %, it is not ready.
