# Stamped Energy — Capability Baseline (for competitive gap analysis)

**As-of workspace read:** 2026-09-21; plain-English rewrite 2026-09-22 (IST)  
**Sources of truth:** this repo (`contracts/`, ADRs, [PROGRESS.md](../../PROGRESS.md)), L1–L6 consumer READMEs ([REPOS.md](../../REPOS.md)), pilot tape `packages/data-analysis-package-1/` (consumer repo, not vendored here)  
**Framing lock:** two pillars + shared context — [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md); architecture SSOT [STAMPED_ARCHITECTURE.md](../../technical/STAMPED_ARCHITECTURE.md)

**Status vocabulary (this doc only):**

| Tag | Meaning |
| --- | --- |
| **shipped** | Code + contracts present in layer repos; Wave A/B completion noted in PROGRESS / PHASE_1_TO_5 |
| **specified** | ADR / contracts / handoff / layer SSOT written; consumer code deferred or partial |
| **research-only** | Memo / exploration / pilot analysis; not a production product claim |
| **not present** | Explicitly out of scope, parked, or absent from inventory |

**Honesty:** Never invent plant ₹ savings. Demo/catalog ₹ figures are labelled illustrative in source decks. LNM tape verified savings = ₹0 (see data-analysis package).

**Wave snapshot:** Positioning alignment Phases 0–5 **completed** (L1–L6 Wave A idle/compressor + Wave B tradeoff/holistic). Writeback = **spec completed, code Wave C later**. ([PROGRESS.md](../../PROGRESS.md), [PHASE_1_TO_5_COMPLETION.md](../../PHASE_1_TO_5_COMPLETION.md))

---

## Stamped in plain English

**What we sell:** software that sits on top of a factory’s existing meters, SCADA, and machine data. We do **not** sell meters, batteries, or a plant control system that silently writes to PLCs.

**Who buys:** plant heads, electrical heads, and maintenance heads at energy-heavy Indian factories (HT industrial bills). They care about the next concrete action, not another dashboard.

**The loop (Connect → Observe → Decide → Execute → Verify):**

1. **Connect** — Pull live and historical plant signals (meters, MQTT/OPC, files, CNC historians) and the actual DISCOM electricity bill into one place. Normalise tags so “incomer kW” means the same thing every time.
2. **Observe** — Spot money and reliability problems: Maximum Demand (MD) spikes, Time-of-Day (ToD) peak exposure, poor Power Factor (PF), idle/phantom loads, compressor waste, CNC idle, and similar. Emit a **Finding** (what’s wrong, with evidence).
3. **Decide** — Turn each Finding into a **Prescription**: what to do, who owns it, how hard it is, rough ₹ impact from the real tariff table (not invented %), and when it’s due. Humans can Discuss / negotiate the Rx.
4. **Execute** — Push the Prescription to the right person (including WhatsApp), track open → ack → done. Today we do **not** silently write to plant equipment. Human-guided soft writeback is specified for later (Wave C), not shipped.
5. **Verify** — Confirm the ops change happened on live tags (**ops-confirmed**). Full “this saved ₹X on the DISCOM bill” verification is reserved for a future bill path — we refuse to claim bill-verified savings we cannot defend. Pilot tape honesty: verified savings can be ₹0.

**Two pillars (what we optimise for):** energy cost / waste, and equipment health signals that drive energy waste — always with shared plant context (orders, shifts). We are **not** a MES, OEE hero product, BESS EMS, or ABB-style closed-loop plant optimiser.

**India money levers we already care about:** ToD windows, MD / contract demand, PF slabs, CMD rightsizing, idle and compressor waste — scored in ₹ from tariff tables and bills.

**Status tags below:** **shipped** = code+contracts in repos · **specified** = written design, code deferred/partial · **research-only** = pilot/analysis, not a product claim · **not present** = out of scope or absent.

## Connect / ingest

| Capability | Status | Notes / cite |
| --- | --- | --- |
| Modbus TCP/RTU meter poll (incomer / feeder kW, kWh, PF) | **shipped** | Path B production; YAML profiles (Schneider, Secure, L&T, HPL, Elmeasure, …). `l1/connectors-edge/README.md` |
| MQTT plant EMS JSON + Sparkplug B decode | **shipped** | Edge adapters production-capable. Same README |
| OPC UA poll (Kepware-class) | **shipped** (field in `p1` flavour) | Sim if endpoint empty. README |
| Filewatch CSV drops (EMS / site packs) | **shipped** | Production-capable. README |
| REST JSON poller | **shipped** | Production-capable. README |
| Historian SQL watermark backfill | **shipped** (wedge) | Incremental query; sqlite open noted. README |
| DLMS/COSEM Indian HT OBIS | **specified** / sim-first | Field returns pilot-gate error. README; compliance IS 15959 |
| BACnet/IP HVAC | **specified** / sim-first | README |
| MTConnect CNC agent | **specified** / sim-first | README; **no FOCAS** in Go agent |
| FANUC MT-LINKi (LNM) via Socket.IO → CSV → filewatch | **shipped** (site pack) | `l1/connectors-edge/packages/site-lnm-mtlinki/` — read-only; no FOCAS, no CNC writes |
| Fake / plant-sim lab connectors | **shipped** | Dev + Wave A idle/compressor scenarios |
| MES-lite Path B: CSV → `production_order` + `production_record` | **shipped** | Edge `plant_sim.mes_lite`; posts L2 ingest. Edge README |
| Tag mapping UI + OTA signed mapping manifests | **shipped** | `tag-mapping-api` / `tag-mapping-ui`; edge README |
| Edge local buffer (~72h SQLite) + MQTT uplink QoS1 | **shipped** | Edge README |
| Cloud ingest + Postgres outbox + L2 relay | **shipped** | Record types: measurement, event, production_record, production_order, bill_line. `l1/connectors-cloud/README.md` |
| HTTP backfill measurements / production-orders | **shipped** | Cloud README |
| DISCOM HT bill PWA + OCR + ₹1 recompute gate | **shipped** | Templates: UPPCL, MSEDCL, DVVNL, … `l1/connectors-bill/README.md` |
| Other utility bills (LT, water, PNG) | **shipped** (extract) | Same README doc_types |
| Plant docs: EMS CSV, production export, shift calendar, load profile, PM/PAT proforma | **shipped** (extract lanes) | Bill README |
| Tariff-order analyst queue → YAML | **shipped** (analyst path) | Not MQTT bill line |
| Metadata-only docs (BRSR, thermography, energy audit, …) | **specified** (P2 events) | Arrival events only |
| L2 Timescale seven schemas + HTTP ingest/query | **shipped** | ingest, telemetry, graph, commercial, features, baselines, ledger. `l2/universal-repositary/README.md` |
| Historian backfill API (`late=true`) | **shipped** | L2 README |
| LNM site seed (CNC-aligned orders) | **shipped** (site pack) | `packages/site-lnm-faridabad` referenced in L2 README |
| Native S7 / EtherNet/IP PLC connector | **not present** | Reach via OPC UA / Modbus gateway only. Edge README |
| Direct FOCAS CNC driver | **not present** | Explicit forbid. Edge README; `docs/research/FANUC_CONNECTIVITY.md` |
| Camera / CCTV as L1 source | **research-only** | `research/concepts/06-plant-camera-perception.md` — not L1 P0 |

---

## Observe / analytics

| Capability | Status | Notes / cite |
| --- | --- | --- |
| Two-pillar Finding emit (energy + equipment) | **shipped** | L3 core; Wave A. PROGRESS phase 2; `l3/intelligence-core/README.md` |
| Hot path: incomer MD (+ PF / ToD) | **shipped** | Engines `md.py`, `pf.py`, `tod.py`; rulepacks `domain/incomer`, `domain/tariff` |
| Idle load / phantom nonprod / offshift baseload | **shipped** | Engine `idle_load` + pack `domain/idle` 1.1.0; Wave A commit |
| Compressor SP drift (+ unload / leak rules in pack) | **shipped** | Engine + `domain/compressor` 1.1.0; Wave A |
| Load management: stagger, peak shed, CMD rightsizing, demand floor | **shipped** (rules + engines) | `domain/load_management` 1.1.0; electrical_demand / MD overlap rules |
| CNC pack under `ENABLE_CNC` (state energy split, spindle signature, SEC/part, aux-on-idle, alarm dwell, abandoned e-stop, unattended long stop, …) | **shipped** (flag-gated) | Engines under `engines/cnc_*`, `idle_cnc_spindle`, etc.; pack `domain/machining` 0.1.0 |
| Furnace / HVAC / source-mix / equipment-health / baseload / alarm-hygiene packs | **shipped** (catalog) | 14 domain packs, 46 rules, 9 verticals — `l3/intelligence-rulepacks/README.md` |
| TOW-P baseline of record + EWMA/CUSUM residual warm path | **shipped** | Core README; challengers TimesFM/TabPFN/LGBM **shadow only** |
| EnPI / SEC feature path | **shipped** (engine + L2 `sec_feature`) | `engines/enpi.py`, `sec.py`; L2 features schema |
| Tradeoff TOD/preheat ranking (mgmt Findings) | **shipped** | Wave B `TradeoffEngine`; PROGRESS phase 5; `engines/tradeoff.py` |
| Dual-mode live vs historian detection windows | **shipped** | Core README `run_detection_window` |
| Dual-lane Lab vs L4 outbox (suppress/shadow stay Lab) | **shipped** | ADR-015; core README |
| Rulepack DISCOM HT tables (UPCL, JVVNL, … provisional) | **shipped** (catalog) | `intelligence-rulepacks/tariffs/` |
| LNM 93-day MT-LINKi historian analysis (fleet hours, bills, ranked Rx goldens) | **research-only** / pilot pack | `packages/data-analysis-package-1/` — **not** production L3; verified savings on tape **₹0** |
| kWh/MT or SEC-by-SKU soft join via ERP | **shipped** (soft-join engines) | Core README ERP soft-joins; needs production_record |
| Plant camera occupancy covariate | **research-only** | Camera perception note |
| Black-box autonomous forecasting as money of record | **not present** | TOW-P is baseline of record; FM shadow only. Core README |

---

## Decide

| Capability | Status | Notes / cite |
| --- | --- | --- |
| Finding → Prescription compiler (quality path) | **shipped** | L4 graphs A/B, delta facts, playbooks, veto/judge. `l4/knowledge-reasoning/README.md` |
| Template fast path (0 LLM) for money-pack / Proof Run | **shipped** | L4 README; Wave A AD-5 templates |
| Prescription card: what / why / owner / effort / impact ₹ / due / evidence flip | **shipped** | Architecture §8; L6 flip cards Wave A `42cb105` |
| ₹ scoring via tariff-true decomposition (`inr_decomposition`) | **shipped** | L3 must not invent; L2 `get_active_tariff`. Core README |
| Management Rx trade-off block (energy hero + effectiveness co-benefits) | **shipped** (contracts + engine) | ADR-024; Finding/Rx `decision_class` / `tradeoff`; Wave B |
| Bounded prescription negotiation (“Discuss”) | **shipped** (workflow events + L6 panel) | ADR-024; contracts `prescription-revision`; L6 README Discuss panel |
| Dual plant graphs + Path D delta pack | **specified** / shipped in L4 modules | ADR-028; L4 plant_context modules |
| CapexProposal sidecar (ROI / payback) | **specified** (contract) | `contracts/schemas/intelligence/capex-proposal.json` — human approval required |
| Ask Analyst (read-only tool allowlist) | **shipped** (L4 + L6 `/analyst`) | L4/L6 READMEs; no OT/SQL/open crawl |
| Free-form LLM invents owners / ₹ / OT writes | **not present** | Explicit non-goal; quality gates abstain |

---

## Execute / closure

| Capability | Status | Notes / cite |
| --- | --- | --- |
| Prescription ingest → alarm → workflow (open → ack → done → verified) | **shipped** | `l5/closure-verification/README.md` |
| WhatsApp notify (Meta Cloud API templates + quick replies) | **shipped** (code; live behind `L5_META_ENABLED` default false) | ADR-021; L5 README |
| SMS fallback (MSG91 + TRAI DLT) | **specified** / implemented path | ADR-021: register P0, send live P1; L5 SMS on Meta failure / budget |
| Fatigue budget ≤3 pushes/role/day | **shipped** (policy in code) | ADR-021; `DAILY_PUSH_BUDGET=3` |
| L5 internal stamped-gate console | **shipped** | Wave A gate+console; L5 `:8095` |
| Delivery judge (LLM-as-judge) when stamped gate off | **shipped** (fail-closed without keys) | L5 README |
| L6 Forge: alarms, prescriptions lanes, live plant, equipment/CNC | **shipped** | `l6/experience-integration/README.md`; Wave A live Rx flip |
| Human-guided OT writeback (`ActionIntent`) | **specified** | ADR-029; contracts `action-intent.json`; handoff `handoff/l5/stamped-l5-action-intent.md`; **code Wave C later** (PROGRESS) |
| Soft OT beachhead commands (idle aux stop, approved setpoint, schedule release) | **specified** | ADR-029 — not FANUC cycle start / e-stop |
| Wave B desk assign/confirm without OT write | **shipped** | ADR-029 staging; PROGRESS writeback-spec |
| Autonomous / silent PLC write | **not present** | Hard non-goal. ADR-029; CONTROL_AND_ACTION.md |

---

## Verify

| Capability | Status | Notes / cite |
| --- | --- | --- |
| Ops-clearance on Finding → L5 clearance poll on L2 tags | **shipped** | ADR-020; L5 verification worker |
| Dual claim labels: `ops_confirmed` ≠ bill-verified | **shipped** | ADR-020; L5/L6 sanitizers |
| Ledger intents: potential → ops_confirmed realised | **shipped** | ADR-013/020; L2 `ledger` schema; L5 ledger module |
| Counterfactual / opportunity_cost always `modeled` | **shipped** (policy) | ADR-020 |
| Bill / IPMVP Option C reconciliation as P0 gate | **not present** (deferred) | ADR-020: `verification_status=verified` reserved for future bill path |
| Evidence archive / content-addressed refs | **shipped** / **specified** retention | L2 `evidence_window_archive`; ADR-021 evidence in ap-south-1 |
| ASHRAE G14 / M&V-grade baseline gates for credit | **specified** | L3 SSOT / eval docs; uncertified baseline → no bill-`verified` |
| LNM claim_check / honesty bar on analysis claims | **research-only** (pilot tooling) | `data-analysis-package-1/analysis/tools/claim_check.py` |

---

## Compliance / reporting

| Capability | Status | Notes / cite |
| --- | --- | --- |
| India compliance register (CERT-In, DPDP, OT read-only, ap-south-1) | **specified** / design baseline | `compliance/india-compliance-register.md`; ADR-004 |
| BEE PAT — SEC/M&V evidence **export** for Designated Consumers | **specified** (enable, not register) | Compliance register §4.5 — Stamped is not a PAT registrant |
| ISO 50001 support (data for customer audits) | **specified** (indirect) | Compliance §6.2 — we don’t certify plants |
| SEBI BRSR Scope 2 evidence export | **specified** (future L5/L6 packs) | Compliance §6.1 — not BRSR filing |
| PAT / BRSR / energy-audit doc intake as structured bill lines | **not present** | Bill PWA: PAT proforma / BRSR → metadata events only (P2) |
| ISO 27001 org certification | **not present** (controls now; certify when deal requires) | Compliance §2.4 |

---

## Hardware / OT control

| Capability | Status | Notes / cite |
| --- | --- | --- |
| Software overlay on customer meters / SCADA / CNC IIoT | **shipped** (connect posture) | Architecture §1 — read-only default |
| Own meter hardware / retrofit program | **not present** | Architecture: not a hardware retrofit program; compliance: not a meter manufacturer |
| BESS autonomy / battery dispatch optimizer | **not present** | Website copy: “No battery-storage claim”; rulepack research notes peer EMS do ToD+BESS — Stamped catalog is threshold `dispatch_gap` only (`intelligence-rulepacks` research note) |
| ABB-like plant optimizer / EMS closed-loop control | **not present** | Category: decision layer, not EMS. Battlecard in `technical/research/india-mes-ai-and-production-rx-opportunity.md` Appendix A |
| Human-guided write to plant command tags (opt-in) | **specified** | ADR-029 Wave C — not autonomous EMS |
| Universal machine control plane | **not present** | ADR-029 rejected alternative |

---

## Explicit NON-goals / parked

| Item | Status | Cite |
| --- | --- | --- |
| Third pillar / MES / plant OS / OEE-hero product | **not present** (forbidden) | ADR-026 |
| Production-efficiency prescriptions (prod_* decision class) | **parked** | `future/later/production-efficiency-prescriptions.md`; PROGRESS `future/` |
| Plant margin optimization (contribution-margin scorecard) | **parked** | `future/near-term/plant-margin-optimization.md` |
| Replace EMS / CMMS / vibration PdM company | **not present** | Architecture anti-confusion; EMS battlecard |
| Silent/autonomous OT write; e-stop / FANUC cycle start via Stamped | **not present** | ADR-029 |
| Cameras as WM / VMS product | **research-only** / not P0 | Camera perception note; PROGRESS research row |
| Split core into Energy / Maintenance / MES products | **not present** | ADR-026 |
| Customer-facing gate / stamped-review controls on L6 | **not present** | IMPLEMENTATION_PLAN non-goals; L5 console is internal |
| Invent undefendable savings % / fake live KPIs | **not present** | PRODUCT.md anti-references; data-analysis honesty bar |

---

## Contracts inventory (domains present)

Under `contracts/schemas/` (pin ~0.13.0 writeback era per L4 README / PROGRESS):

| Domain | Schemas (representative) |
| --- | --- |
| **Envelope** | `stamped-record-envelope`, `event`, `workflow-event` |
| **Telemetry** | `measurement`, `bill-line`, `production-record`, `tag-inventory` |
| **Intelligence** | `finding`, `prescription`, `prescription-revision`, `l4-compile-trace`, `plant-intelligence-score`, `capex-proposal` |
| **Closure** | `ledger-entry`, `action-intent`, `improvement-signal`, `improve-cycle`, `calibration-patch`, `model-run` |
| **Plant / shared context** | `production-order`, `plant-department-graph`, `plant-knowledge-graph`, `plant-live-index`, `plant-preference-profile`, `plant-admin-settings`, `shift-roster`, `machine-capability` |
| **Config** | `site-config`, `modbus-profile`, `mapping-config` |

Topics: `contracts/TOPICS.md`.

---

## data-analysis-package-1 (pilot analytics — not an L-layer)

| Capability | Status | Cite |
| --- | --- | --- |
| 93-day Line_1 MT-LINKi dump + DHBVN Jun–Aug bills | **research-only** | Package README |
| Fleet hours / long STOP / abandoned e-stop analytics | **research-only** | `docs/handoff/04-*.md` |
| Five ranked human-executed prescriptions (goldens feeding L3 CNC path) | **research-only** → product lift | `docs/handoff/05-ranked-prescriptions.md`; engines under `ENABLE_CNC` |
| Meet pack / HTML briefing / claim_check | **research-only** (shipped as static pack) | PROGRESS meet-pack waves done |
| Verified energy savings on tape | **₹0** (explicit) | Package README — do not invent |

---

## Competitive differentiation cues (from own research — not competitor claims)

- **vs EMS monitoring:** assigned owner + ops-cleared ledger, not charts. Battlecard Appendix A — [`technical/research/india-mes-ai-and-production-rx-opportunity.md`](../../technical/research/india-mes-ai-and-production-rx-opportunity.md)
- **vs MES:** read orders for practical energy Rx; do not schedule. [ADR-026](../../decisions/024-026/ADR-026-two-pillars-shared-context.md)
- **India-specific money levers present in catalog:** ToD exposure, MD coincidence/stagger, PF slabs, CMD rightsizing, idle/phantom — rulepacks `incomer` / `tariff` / `load_management` / `idle`

---

## Source index (primary)

1. [`docs/PRODUCT_MAP_STAMPED_EXTERNAL.md`](../../docs/PRODUCT_MAP_STAMPED_EXTERNAL.md) (operating loop + pack map; no separate `ORIENTATION.md` in this repo)  
2. [`PROGRESS.md`](../../PROGRESS.md), [`IMPLEMENTATION_PLAN.md`](../../IMPLEMENTATION_PLAN.md), [`PHASE_1_TO_5_COMPLETION.md`](../../PHASE_1_TO_5_COMPLETION.md)  
3. [`technical/STAMPED_ARCHITECTURE.md`](../../technical/STAMPED_ARCHITECTURE.md)  
4. ADRs: 020, 021, 024, 026, 028, 029 (+ 013 ledger) — [`decisions/`](../../decisions/)  
5. [`contracts/`](../../contracts/)  
6. Layer READMEs in consumer repos (`l1/`–`l6/` per [REPOS.md](../../REPOS.md))  
7. `l3/intelligence-rulepacks/` catalog (consumer repo)  
8. `packages/data-analysis-package-1/` (consumer / pilot package)  
9. [`future/`](../../future/), [`research/concepts/06-plant-camera-perception.md`](../../research/concepts/06-plant-camera-perception.md), [`technical/research/india-mes-ai-and-production-rx-opportunity.md`](../../technical/research/india-mes-ai-and-production-rx-opportunity.md)  
10. [`compliance/india-compliance-register.md`](../../compliance/india-compliance-register.md)
