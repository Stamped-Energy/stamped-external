# Stamped — vision alignment for AI agents

**Date:** 2026-09-24  
**Audience:** AI systems and agents updating docs, product copy, architecture notes, research memos, prompts, and plans.  
**Authority:** Derived from [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md). If this file and `09` conflict, **`09` wins**.  
**Job of this file:** Give agents a machine-consumable contract so they can realign older **internal** Stamped material (including Energy-suffixed branding) to the current company vision without inventing a new company. External marketing is out of scope.

---

## 0. How to use this file

When you are asked to update prior work, or to write anything “about Stamped”:

1. Load this file and treat §1–§4 as **hard constraints**.
2. Run the **alignment check** in §9 on the target document or change.
3. Prefer **surgical edits** that restore invariants over rewriting whole files.
4. Do **not** invent revenue, customers, savings %, ship status, or competitor implementation claims.
5. Do **not** append Energy to the product name. Product name is **Stamped**. Energy is a domain and an entry wedge.
6. Do **not** update external marketing (website, decks, LinkedIn, ads, client brochures) from this contract.
7. If a prior **internal** doc claims Stamped is energy-only, an OpEx suite, an MES/APS replacement, a dashboard, a logistics SKU, or a system that runs the plant — **correct it** to match this contract.
8. For long prose or founder-facing narrative, prefer lifting from `09`. This file is the **operating contract** for alignment work.

### Output contract when you finish an update

State briefly:

- **Aligned:** what now matches the vision
- **Changed:** what old framing you removed or rewrote
- **Open:** anything that still conflicts and needs a human (pricing, legal entity, unpublished metrics)

---

## 1. North star (lock this first)

### One sentence (do not paraphrase away)

**Stamped helps plant teams choose, assign, and verify the next operating action across energy, cost, time / throughput, continuity / flow, and short-horizon exceptions.**

### Company in three lines

1. Stamped turns plant signals into a **specific next step** for a person, **records** the choice, and **checks** what happened.
2. Coverage is **five decision domains** on **one card** with **one owner**. Wide coverage, narrow authority.
3. The plant stays accountable for the operating choice. Stamped owns the **workflow**, not safety, quality release, maintenance authority, or customer commitments.

### Outcomes agents must drive toward

When updating prior work, the outcome of the product story must be:

| Outcome domain | What “good” means in text and design |
|---|---|
| **Energy** | Avoidable load / intensity decisions with production constraints visible; bill alone is not proof |
| **Cost** | Visible operating-cost tradeoffs (overtime, wait, alternate capacity); calculator / finance owns ₹ |
| **Time / throughput** | Productive machine-minutes, idle/alarm dwell, constraint-cell response — not a full schedule |
| **Continuity / flow** | One handoff / batch / queue decision at a time — not a new dispatch list |
| **Exception response** | Next-hours choice after a stop or slip — not APS / MRP replacement |

These can overlap on one card. They must **not** be summed into one hero savings number.

### What success looks like (for product, and for doc alignment)

- A real **decision family** repeats.
- **One owner** per card.
- Closure states are honest: verified, no change, rejected, deferred, blocked.
- Measured / confirmed evidence is not mixed with modeled value.
- Energy may open the conversation; the company identity remains the **five-domain loop**.

---

## 2. Invariants (MUST)

Agents must preserve these. If a prior doc violates them, fix the doc.

### 2.1 Name and identity

- Product name: **Stamped**
- Never present the product with an Energy suffix on the name
- Energy = entry wedge + one owned domain, **not** the category label
- Company is **not** an operational-excellence suite (OpEx is the plant’s program)

### 2.2 Decision loop

Every product-shaped claim must map to:

`detect → recommend → assign → act → verify`  
(with optional `propose learning` after close)

Missing owner, missing verification, or “insight only” is **outside** the product center.

### 2.3 One card

- One meaningful condition → **one decision card**
- One **primary** domain tag; optional secondary tags
- **One** accountable owner until explicit reassignment
- Not five queues, five tickets, or five products

### 2.4 Evidence tiers

Label evidence as exactly one of:

- **Measured** — agreed meter / machine / production / timestamp source
- **Confirmed** — authorized plant person when system data is incomplete
- **Modeled** — approved assumptions; useful for a decision; **not** proof of realized impact
- **Unknown** — not enough evidence to claim an effect

**Modeled ≠ measured.** Dual effect wallets (e.g. energy + machine-minutes) stay **separate**. The **calculator** (or plant-approved tariff / costing path) owns money.

### 2.5 Closure states

Minimum states: Open; Assigned; In progress; Closed — verified; Closed — no change; Rejected; Deferred / expired; Blocked / disputed.

**Closed ≠ successful.** Rejection and no-change stay visible. They are learning events.

### 2.6 Integration posture

- Default: **read / ingest**
- Allowed: notify or create a task when destination and owner are clear
- Write-back: human-confirmed, narrow, allow-listed, auditable — unless an **earned run** applies (§4)

### 2.7 Horizon

- Next hours or one shift for operating choices
- Not month-ahead planning, not full dispatch rewrite, not promise-date ownership

### 2.8 Intelligence split (presentation)

- **ML models and ML methods:** find conditions; estimate effects; do **not** invent ₹
- **Self-improving agent stack:** bounded recommendation (options, constraints, uncertainty, owner); learns from closed cards; this is the **latest-tech** line
- Agent stack is **not** the company and **not** the only innovation
- A production rule / threshold still needs **named-owner acceptance**

---

## 3. Hard stops (MUST NOT)

These are absolute. Do not soften in marketing, architecture, or agent prompts.

Stamped must never:

1. Make an automatic **safety** decision or send a **remote command** to critical equipment  
2. **Release a quality hold**, sign off conformance, or give metallurgical / process acceptance  
3. **Authorize maintenance** or bypass a maintenance lockout  
4. **Silently change** customer priority, promise date, routing, master data, or the full dispatch sequence  
5. Issue a recommendation that **outranks a known plant constraint** only because a model predicts a benefit  

Also refuse product claims that imply:

- Replacement of **MES / APS / ERP / QMS / CMMS** as system of record  
- A **plant-wide digital twin** or “model everything first” program as the product  
- **Silent control** of the plant  

---

## 4. Earned run (narrow exception)

**Default:** recommend and assign. Humans decide and execute.

**Earned run:** a plant-accepted, reversible, low-risk workflow with named owner, audit, watch mode, and rollback.

**May include (examples):**

- Suppress a duplicate notification  
- Open a review task after a repeated, agreed condition  

**Must never include:**

- Reroute a job  
- Switch critical equipment  
- Release quality  
- Change a customer commitment  

If an earned run is wrong: stop it, see what it did, revert, mark disputed.

---

## 5. Product model (compact)

### 5.1 Five domains

| Domain | Owns | Does not own |
|---|---|---|
| Energy | When/how loads run; avoidable use / intensity where data supports | Retail energy, bill-audit firm, meter hardware, critical remote control |
| Cost | Visible operating-cost levers (idle, overtime, wait, alternate) | Plant ledger / FP&A |
| Time / throughput | Machine-minutes, dwell, constraint-cell next choice | Full plant schedule publish |
| Continuity / flow | One handoff / batch / queue decision | New dispatch list / month-ahead plan |
| Exception response | Next choice after stop / slip under visible constraints | Removing the exception; owning plant risk acceptance; APS |

### 5.2 Action kernel

1. Ingest signals (meters, machine state, production, maintenance context, calendars, structured human input)  
2. Normalize enough to join **one** condition  
3. Detect (ML / methods / rules)  
4. Recommend (agent stack: options, constraints, uncertainty, one owner)  
5. Assign  
6. Record response  
7. Verify against named evidence  
8. Propose learning (named-owner gate for production changes)  

### 5.3 Exception response ≠ APS

- May recommend next operating choice for next hours / one shift  
- Must not publish a new plant schedule, reorder full dispatch, rewrite MRP, or change promise dates  
- **Hold** = short operating pause for one batch/step when authorized — **never** quality hold release  

### 5.4 Who it is for

- Champion: plant / ops / energy / CI / mfg engineer who will own responses  
- Beachhead hypothesis: India mid-market discrete plant with accessible data — **not** a geography lock  
- Pricing: TBD; no outcome-pricing claim without a real measurement basis  
- Energy wins the **first conversation**; expansion requires a closed **non-energy** decision  

---

## 6. Anti-vision (tight)

Use this short list when aligning docs. Do not expand into a brochure of competitors.

Stamped is **not**:

1. An **energy dashboard / EMS / savings-report** tool (charts without owned action + verification)  
2. A **generic OEE / analytics** vendor (metrics without one decision + one owner)  
3. A replacement **MES / APS / ERP / QMS / CMMS** or other system of record  
4. A **plant OS**, plant-wide AI that owns judgment/control, or silent-control product  
5. An **operational-excellence suite**, agent operating system, sensing-pod company, or logistics-only SKU  
6. A **default CapEx sensor** play or digital-twin services firm that must model everything before one loop repeats  

Hardware, sensors, and analytics may **support** a decision family. They are not the product center.

---

## 7. Delta map — old framing → current vision

Use this when scanning older Stamped docs (including Energy-suffixed branding), READMEs, decks, research notes, and prompts.

| If prior material says… | Rewrite toward… |
|---|---|
| Energy-suffixed product name | **Stamped**; energy is wedge + domain |
| Energy company / energy-only AI | Five-domain decision loop; energy opens the door |
| Dashboard, findings, rankings | Decision card → owner → verify → honest close |
| Savings % / ₹ hero / additive wallets | Separate wallets; calculator owns money; no fake proof |
| Autonomous plant / runs the plant / FSD metaphor | Recommend/assign default; earned run only if fenced |
| Agent stack = the company | Agent stack = latest-tech **presentation**; company = closed decision loop |
| OpEx platform / digital transformation | Bounded decision + closure inside the plant’s own program |
| Replace MES/APS | Read context; respond; do not replace systems of record |
| Logistics / dispatch product | Continuity/exception may appear; not a logistics SKU |
| “Not built yet” status inventory as identity | Vision language; pilots as sequence, not confession |
| Mill models | **ML models** / **ML methods** |
| Intelligence of record / factory brain / NeoLab copy | Do not paste; use choose / assign / verify language |
| Process as second product | Deferred; not a current pillar |

### Stack language (when architecture docs appear)

Plain map only — do not turn layer codes into marketing:

- L1 connectors → L2 store → L3 findings (ML/methods + rules) → L4 reasoning → L5 closure → L6 experience  
- Product claim stays the **closed action**, not the layer diagram  

---

## 8. Agent playbook — how to realign a document

### Step A — Classify the target

- **Product identity** (what we are)  
- **Architecture** (how it works)  
- **GTM / client** (how we sell)  
- **Research / exploration** (hypotheses)  
- **Internal status** (honest build state — keep honest; do not inject into public vision claims)

### Step B — Scan for violations

Search for: Energy-suffixed product name, `energy-only`, `dashboard`, `savings`, `%`, `autonomous`, `run the plant`, `replace MES`, `APS`, `OpEx platform`, `digital twin`, `copilot`, `intelligence of record`, `factory brain`, `mill model`, fake customer counts, prior framing (tag `v2026.09.24`).

### Step C — Apply fixes in this order

1. Name + one-sentence identity  
2. Hard stops / HITL / earned-run fence  
3. Evidence tiers + dual wallets  
4. Domains + one card + one owner  
5. Tech split (ML methods vs agent stack)  
6. Anti-vision collisions (use §6 only)  
7. Pilot / entry sequence if the doc discusses sequencing  

### Step D — Do-not-invent list

Never add:

- Revenue, ARR, customer count, retention  
- Unmeasured kWh / ₹ / % savings as fact  
- Claims that the whole five-domain product is already proven everywhere  
- Competitor implementation details beyond category contrast already in `09`  

### Step E — Self-check before returning work

Answer yes to all:

- [ ] Product named Stamped?  
- [ ] Choose / assign / verify still true?  
- [ ] One owner + verification path present for product claims?  
- [ ] Hard stops intact?  
- [ ] ML + agent stack both present if discussing intelligence; latest-tech points at agent stack only?  
- [ ] No additive wallet math?  
- [ ] No OpEx / MES-replacement / run-the-plant identity?  
- [ ] Plant cut and funding cut (if used) describe the **same** company?  

---

## 9. Alignment check (paste into agent prompts)

```text
ALIGNMENT CHECK — Stamped vision
Authority: 09-stamped-founder-vision.md + this agent alignment file (09 wins on conflict)

1. Name: Is the product called Stamped (no Energy suffix)?
2. Sentence: Does it still mean choose, assign, verify across five domains?
3. Card: One condition → one card → one owner → closure?
4. Evidence: Measured / Confirmed / Modeled / Unknown respected? Wallets separate? Calculator owns money?
5. Stops: Any claim that violates safety / quality / maintenance / silent master-data or dispatch / constraint override?
6. Autonomy: Recommend/assign default? Earned run only if fenced?
7. Tech: ML models/methods + agent stack both fair? Latest-tech line on agent stack only?
8. Category: Not OpEx suite, not MES/APS replacement, not logistics-only, not energy-only identity?
9. Proof: No invented savings, customers, or revenue?
10. Outcome: Does this change drive a clearer next operating action and honest close?

If any fail: fix before ship. Report Aligned / Changed / Open.
```

---

## 10. Build / do-not-build test (for agents proposing features)

Before proposing a feature, doc section, or roadmap item, require answers:

1. What **operational decision** does this help a plant make?  
2. Which domain is **primary**, and what are secondary tags?  
3. Who is the **one** accountable owner?  
4. Evidence source, horizon, constraint, closure state?  
5. Next-hours choice rather than a new schedule?  
6. Hard stops preserved?  
7. Reusable decision family vs custom consulting?  
8. Works with existing systems without silently replacing them?  
9. Will the closed result make the next recommendation sharper **inside** the hard stops?  

**Do not build / do not write** when the idea is only: a dashboard, a generic alert, an unsupported savings claim, an autonomous critical action, full planning, a new pillar, or a request with no owner and no verification path.

**Founder test:**  
**What decision is Stamped helping the plant make, who acts, what evidence closes it, and what will Stamped refuse to change?**

---

## 11. Worked examples (for rewrite grounding)

### 11.1 Canonical card — idle with extra loads

- **Detect:** machine idle; extra loads still on  
- **Recommend:** safe idle response allowed by plant practice (no remote critical command)  
- **Assign:** responsible operator or supervisor  
- **Verify:** machine state + measured load after agreed interval  
- **Evidence:** may show energy effect and recovered machine-minute **separately**  
- **Close:** verified / no change / rejected / blocked — never “success because we notified”

### 11.2 Exception — bottleneck alarm (illustrative)

- Show state, WIP, due work, known alternate — do not invent repair duration  
- Recommend: stop feeding unavailable cell; check one alternate; escalate maintenance  
- Supervisor chooses; singular ownership for next action  
- Verify: alternate started? cell recovered? rule still apply?  
- Honest result may be no measurable change or rejection  

### 11.3 Wrong rewrite (reject)

“Stamped’s autonomous AI runs your plant and delivers invented savings.”

**Corrected:**  
“Stamped recommends, assigns, and verifies the next operating action across five domains. Humans decide by default. Money claims need measured or confirmed evidence and calculator-owned ₹ — not a modeled hero number.”

---

## 12. Glossary (agent-stable terms)

| Term | Meaning |
|---|---|
| **Stamped** | Product name |
| **Operational decision** | Bounded choice with trigger, options, human owner, evidence, horizon, closure |
| **Own (decision)** | Own the workflow (detect→…→verify); plant owns the operating choice |
| **Decision card** | One condition, one primary domain, one owner, evidence, options, closure |
| **Action kernel** | Smallest reusable product loop |
| **Self-improving** | Closed cards (incl. reject / no-change) sharpen next recommendation; production change needs named owner |
| **Earned run** | Plant-accepted reversible low-risk workflow with audit/watch/rollback |
| **ML models / ML methods** | Find conditions; estimate effects; no invented ₹ |
| **Agent stack** | Bounded recommend + learning from closed cards; latest-tech presentation |
| **Entry wedge** | Energy-led first conversation — not company identity |
| **Process (pillar)** | Deferred; not current product |

---

## 13. Lift paragraphs (same company, two cuts)

Use when an agent must produce short external text. Do not let the two cuts diverge.

**Plant cut.**  
Stamped puts the next operating action in front of one named owner. One card covers Energy, Cost, Time / throughput, Continuity / flow, or a short-horizon exception. The card shows condition, choice, constraints, uncertainty, and closing evidence. The plant can accept, edit, reject, defer, or verify. An idle-load card recommends a safe idle response, assigns the operator or supervisor, and checks machine state and load afterward; it does not add energy and machine-minutes into one savings number. Hard stops in §3 remain in force.

**Funding cut.**  
Stamped turns plant signals into one next operating action with one named owner and a reading that closes it. ML models and ML methods find conditions and estimate effects; they do not own money. The self-improving agent stack is how we present the current generation of the tech; it sharpens recommendations from closed cards, including rejection and no measurable change. The loop is scored by honest closure, not by recommendations issued. Stamped sits on systems the plant already runs. It does not run the plant. Production rules change only with named-owner acceptance.

---

## 14. Pilot 1 (sequence, not status confession)

**First decision family:** confirmed machine idle with extra loads still running; one owner; measured or confirmed verification.

**Includes:** one card, one owner, recommendation with visible constraint, assignment, accept/edit/reject, review time, closure states, evidence classification.

**Excludes:** automatic equipment control; quality/maintenance release; full scheduling; APS/MRP replacement; plant-wide energy optimization; new sensor fleet; Stamped Process; total plant savings claims.

**Exit bar:** cards repeat; named role closes assign→act→verify loops; peers accept evidence format; rejection and no-change recorded; team can label measured/confirmed/modeled/unknown.

After Pilot 1, expand domains only when data, frequency, owner access, and verified evidence justify it.

---

## 15. FAQ for agents (short answers)

| Question | Answer |
|---|---|
| Is the agent stack the company? | No. Closed five-domain decision loop is the company. Agent stack is latest-tech presentation. |
| Are we energy-only? | No. Energy is wedge + domain. |
| Are we an OpEx platform? | No. OpEx is the plant’s program. |
| Do we run the plant? | No. Recommend/assign default; earned run fenced. |
| Do we replace MES/APS? | No. Integrate; do not replace SoR. |
| Are we logistics? | No. Continuity/exceptions may appear; not a logistics product. |
| Can automation ever run? | Only earned run inside plant-accepted boundary. |
| Is Process in scope? | Deferred. Not a current pillar. |
| Pricing? | TBD. No outcome share without measurement basis. |

---

## 16. Source and maintenance

- **Canonical narrative:** `09-stamped-founder-vision.md`  
- **This file:** agent alignment contract derived from `09`  
- **Folder entry for agents:** `AGENT-START.md`  
- When `09` changes: update §1–§7 and §13–§15 here in the same change set  
- Prefer keeping **anti-vision short** (this file’s §6). Long competitor lists belong in research notes, not in agent context  
- **Internal only.** Do not use this file to rewrite website, decks, LinkedIn, ads, or client brochures.

---

## 17. This folder — what agents may edit

| May edit | Leave alone unless asked |
|----------|---------------------------|
| `AGENT-START.md`, `README.md`, `START-HERE.md` | Peer survey **bodies** and vendor numbers in `02`–`04` |
| Authority banners + recommendation / conclusion sections in `00`–`08` and `08a` | Mode tables as data inventory in `01` |
| This file (`10`) | Action-catalog **rows** as research inventory in `08` |

**Rules**

1. Do not turn `00`–`08` into a second copy of `09`.  
2. Do not invent savings, customers, or revenue.  
3. Do not update **external marketing**.  
4. Prefer surgical recommendation fixes over full rewrites.

---

## 18. Other projects — internal change queue

Only run this queue when the human asks you to realign other repos. Skip sites, decks, LinkedIn, ads, and outbound copy.

| Priority | Path (as known in `08a`) | Old framing to fix | Delta toward `09` |
|----------|--------------------------|--------------------|-------------------|
| P0 | `universal-repositary/external/research/strategy/INSIGHTS_FOR_STAMPED.md` | Energy-as-identity / vague industrial intelligence | Stamped; five domains; closed decision loop |
| P0 | `universal-repositary/external/research/strategy/PATHS_FOR_STAMPED_V2.md` | Expansive paths that blur product | Filter to HITL choose/assign/verify; hard stops |
| P0 | `knowledge-reasoning/docs/STAMPED_ENERGY_VALUE_ARCHITECTURE.md` | Title/brand energy-primary | Product **Stamped**; dual wallets; five domains |
| P0 | `knowledge-reasoning/docs/COMPETITOR_VALUE_PRESSURE_TEST.md` | Energy-primary overlay | Same delta as value architecture |
| P1 | `universal-repositary/external/technical/research/agentic-ai-industrial-energy.md` | Agent = company / energy-only agents | Agent stack = latest-tech presentation; ML methods also innovation |
| P1 | Withdrawn ADR-024 (prior framing; tag `v2026.09.24`) | Holistic decisions without five-domain card language | Map to five domains; one card; one owner · cite ADR-030 |
| P1 | Withdrawn ADR-026 (prior framing; tag `v2026.09.24`) | Dual Energy+Process product surface | Process deferred; Stamped single product surface · cite ADR-030 |
| P1 | `knowledge-reasoning/docs/client/bhatia-alloy/research/VALUE_LEVERS_AND_REFERENCES.md` | Lever list without company lock | Keep levers; frame as domain tags under `09` |
| P2 | `universal-repositary/external/research/competitive/industrial-ai-global-2026-09-22/` | Survey conclusions that set company | Keep peer facts; conclusions → `09` |
| P2 | Zerowatt / energy conservation catalogs under `docs/` | Energy-only product story | Contrast peers; Stamped = five-domain loop |
| P2 | Agent prompts / system prompts with Energy-suffixed product name | Product name | Rename to Stamped; energy = domain |

**Stop rules**

- Do not edit those paths unless the human asked in this session.  
- Do not invent proof.  
- Do not touch external marketing.  
- Return **Aligned / Changed / Open**.

---

### Agent start prompt (copy/paste)

```text
You are aligning Stamped INTERNAL materials to the current company vision.
Open: AGENT-START.md → 09-stamped-founder-vision.md → 10-stamped-vision-agent-alignment.md
Authority conflict: prefer 09.
Product name: Stamped (never append Energy to the product name).
North star: choose, assign, and verify the next operating action across five domains.
Hard stops and earned-run rules are absolute.
Do NOT update external marketing (website, decks, LinkedIn, ads).
Do not invent savings, customers, or revenue.
Run the ALIGNMENT CHECK before finishing. Return Aligned / Changed / Open.
```
