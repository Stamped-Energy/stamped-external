# Stamped — founder vision

**Date:** 2026-09-24  
**Status:** Working company vision. The same note is cut into a plant conversation and a funding conversation. Both describe the same company.

## 1. Why this note exists

We need one answer to: what company are we building?

Stamped is software that turns plant signals into a specific next step for a person, records the choice, and checks what happened. It covers five decision domains: Energy, Cost, Time / throughput, Continuity / flow, and Exception response. Energy is how the first conversation often opens. It is not the company name and not the product category.

We are not building a full plant operating system, a replacement for MES or APS, or an autonomous controller. We are building a repeatable decision loop: one card, one owner, an honest close. The first loop is narrow by design. A pilot is the intended first sequence into wider plant coverage, not a vote to become energy-only.

This note is the source. A plant brief and a funding brief are cut from it. They must not invent a different company.

## 2. Stamped in one sentence

**Stamped helps plant teams choose, assign, and verify the next operating action across energy, cost, time / throughput, continuity / flow, and short-horizon exceptions.**

For example, it can show that a machine is idle while its extra loads remain on, recommend a safe idle response, assign it to the responsible operator or supervisor, and check the machine state and measured load afterward. The same card can show an energy effect and a recovered machine-minute without pretending they are one savings number. The calculator owns money. Evidence is labeled Measured, Confirmed, Modeled, or Unknown. Modeled does not mean measured.

**Extent.** One card format covers the five domains across the plant, with one primary tag, optional secondary tags, and one owner. Wide coverage, narrow authority. Not five products, not a logistics tool, and not a plant-wide dashboard or operating system.

**Rhythm.** See the operation through systems the plant already runs. Learn how this plant actually works. Put a bounded action with an owner in front of a person. Close the result so it sharpens the next one.

**Intelligence.** ML models and ML methods find conditions and estimate effects. They do not invent a rupee figure. A self-improving agent stack turns a condition into a bounded recommendation — options, constraints, uncertainty, one owner — and gets sharper from closed cards, including rejection and no measurable change. That self-improving agent stack is the latest tech we point to. A production rule still changes only with a named owner’s acceptance.

## 3. Definitions we will use consistently

### Operational decision
An **operational decision** is a bounded choice triggered by a current plant condition. It has: a trigger, a short list of feasible options, a responsible human, evidence and constraints, a time horizon, and a closure state. A chart or finding becomes a decision only when someone can choose what happens next.

### Own
When Stamped **owns** a decision, Stamped owns the product workflow for detecting the condition, explaining options, routing the choice, recording the response, and checking the result. It does not mean Stamped owns plant safety, quality release, maintenance authorization, customer commitments, or autonomous control. The plant remains accountable for the operating choice.

### Recommendation
A **recommendation** is a bounded proposed next step with its evidence, assumptions, constraints, expected effect, and uncertainty. It can be accepted, edited, rejected, or deferred. It is not an instruction to bypass the responsible plant role.

### Assignment
An **assignment** routes an accepted or requested action to the person or team that can do it, with a due or review time and the relevant context. It may be a Stamped task, a notification, or a human-confirmed ticket through an approved integration. It is not a silent work-order or dispatch rewrite.

### Verification
**Verification** compares what happened with a named signal or human confirmation: machine state, meter interval, production timestamp, batch status, queue age, or another agreed source. Verification may show improvement, no measurable change, failure, or insufficient data. It must not turn a modeled estimate into a measured result.

### Closure and closure states
**Closure** is the recorded end of the decision loop. The minimum states are:

- **Open:** condition detected; no response chosen yet.
- **Assigned:** a person or team owns the next action.
- **In progress:** the action is being carried out.
- **Closed — verified:** the action happened and the agreed evidence was checked.
- **Closed — no change:** the action happened, but the expected measurable change did not appear.
- **Rejected:** the responsible person declined it, with a reason where possible.
- **Deferred / expired:** the decision was postponed or the operating window passed.
- **Blocked / disputed:** data, authority, or constraints prevented a trustworthy close.

A closed action is not automatically a successful action. Zero measured change stays zero; a rejection stays visible.

### Action kernel
The **action kernel** is the smallest reusable product loop: ingest the relevant signals, detect a condition, create a decision card, recommend a bounded choice, assign an owner, record the response, and verify closure. Decision templates, evidence rules, role routing, and closure states are part of the kernel. A one-off analysis without that loop is not the product.

### Self-improving
**Self-improving** means that closed cards sharpen the next recommendation. Verified, no-change, and rejected cards all count as learning events. A production threshold still requires review and acceptance by a named owner.

### Earned run
An **earned run** is a plant-accepted, reversible, low-risk workflow with a named owner, audit record, watch mode, and rollback. It is an accepted exception to the default of recommendation and assignment.

Allowed examples include suppressing a duplicate notification or opening a review task after a repeated, agreed condition. An earned run cannot reroute a job, switch critical equipment, release quality, or change a customer commitment.

## 4. The problem

Plants already have meters, machine states, alarms, production counts, shift calendars, work orders, ERP records, spreadsheets, logbooks, and experienced people. The recurring problem is that these signals are not joined to a decision when the decision matters.

An energy team may see a demand spike but not know which operating change is possible. An MES may show production events without showing that the next furnace load should wait for a practical batch. A maintenance system may contain a work order while operations continues feeding work into a stopped cell. A plant manager may know that handoffs are slow without evidence of where the time went.

The result is familiar:

- Findings are ranked, but no one owns the response.
- Actions are assigned, but nobody checks the result.
- A machine appears to be running while it produces nothing.
- Local optimization starves or blocks the next cell.
- Teams debate dashboards instead of choosing a short, practical action.
- Improvement work depends on one person’s memory or spreadsheet.

Energy matters, but it is not the company’s identity and a monthly utility bill is not sufficient proof. The outcome types we care about are: energy use and intensity, operating cost, productive machine time, throughput, continuity across handoffs and batches, and response to short-horizon exceptions. They can overlap in one decision, but they are not automatically added into one savings line.

## 5. What we own: five decision domains

This is the width of the product: one decision card, one primary tag, optional secondary tags, and one owner.

The five domains are product boundaries, not five separate products. They overlap in plant life. They should not create five duplicate queues.

### 5.1 One decision card across five domains

Every meaningful condition creates **one decision card**. It has:

- one primary domain tag—the domain that best describes the decision being made;
- optional secondary tags, such as `energy`, `cost`, `time`, `continuity`, or `exception`;
- one accountable owner for the next action;
- evidence, constraints, options, expected effect, horizon, and closure state.

For example, a stopped bottleneck machine with idle auxiliaries might carry `exception` as the primary tag and `energy` and `time` as secondary tags. It gets one supervisor-owned response, not three tickets. A card may be seen by several roles, but ownership is singular until it is explicitly reassigned.

### 5.2 Energy

Energy covers operating choices about when and how loads run, including avoidable utility use and intensity where the data supports it. It is the entry wedge, not the category label.

Examples include staggering several large machines starting together when the next shift permits, switching off extra machine loads after a confirmed idle period, or avoiding an under-filled thermal cycle when the production window allows. The card must show the production constraint and the human override.

Energy data may include meters, tariffs, utility tags, machine state, production calendar, shift schedule, and process state. A bill can support the cost calculation; machine and production evidence are still needed to verify an operating action. The calculator or customer-approved tariff owner owns currency math. Stamped does not invent a precise saving from a bill alone.

We do not become an energy retailer, bill-audit firm, meter hardware company, or remote controller for a critical process.

### 5.3 Cost

Cost covers operating-cost choices tied to observable levers such as energy, idle time, overtime, avoidable waits, partial loads, and capacity tradeoffs. It is not a plant-wide accounting or FP&A product.

A card may compare waiting, an extra shift, an alternate machine, or deferment for the next few hours when a constraint cell is short on capacity. The recommendation names the tradeoff and the uncertain cost basis. Standard costs and tariffs remain governed by the plant’s finance and costing rules.

Currency impact and operating impact remain separate evidence fields. We do not stack a modeled tariff saving, a measured machine-minute gain, and a speculative output value into one headline.

### 5.4 Time / throughput

Time / throughput covers productive machine-minutes, idle or alarm time, constraint-cell output, and practical capacity for near-term commitments. A constraint cell means the bottleneck machine or line that limits useful output.

Examples include clearing a persistent alarm dwell, preparing tooling before a changeover, or choosing the next feasible operating response when an alternate machine is available. Stamped may recommend the next choice for a known constraint; it does not re-optimize or publish the full plant schedule.

The product should distinguish running, waiting, blocked, starved, alarmed, and genuinely productive states. It should not turn every state signal into an alert.

### 5.5 Continuity / flow

Continuity / flow covers work moving across handoffs, batches, racks, furnaces, and cells. It focuses on one visible wait or batch decision at a time.

Examples include reducing a handoff wait, holding a batch until a practical rack fill when the approved operating window allows it, or preventing more work from entering a downstream blockage. These are short-horizon operating choices with an owner and a verification signal. They are not a new dispatch list or a month-ahead plan.

### 5.6 Exception response

Exception response is the short-horizon choice after equipment failure, cell unavailability, or a sequence slip. Stamped helps the plant choose what to do next under the constraints it can see. It does not remove the exception or own the plant’s authority to accept risk.

A response might stop feeding work into an unavailable cell, identify an alternate that meets routing, tooling, material, quality, and operator constraints, and escalate maintenance with the affected work list. The supervisor or other authorized role chooses the response.

## 6. Exception response is not APS

APS is a broad planning system for demand, orders, capacity, routings, and constraints. Stamped responds when actual operations have departed from the assumed plan.

Stamped may recommend the next operating choice for the next few hours or one shift. It does not publish a new plant schedule, reorder the full dispatch list, rewrite MRP, change customer promise dates, or replace APS output. The plan may remain in APS. Any approved write-back must be human-confirmed, limited to an allow-listed object, and recorded.

**Hold-release is also not planning.** Stamped may recommend holding the release of one batch or job from an operating step when the evidence and authorized rule say the action is needed—for example, waiting for a practical rack fill. It does not release a quality hold, sign off conformance, or make a broad production-plan decision. “Hold” in this memo means a short operating pause; quality release remains with the quality owner.

### Illustrative sequence, not site data

At 9:10, a bottleneck machine stops and remains in alarm. Stamped shows the current state, work already started but not finished, due work, and known alternate capability. It does not assume a repair duration. The supervisor confirms the likely operating window.

The card recommends stopping new work into the unavailable cell, checking one suitable alternate, and escalating maintenance with the alarm history. The supervisor chooses or edits the response. One owner is assigned to alternate preparation; maintenance owns its escalation. At review time, Stamped checks whether the alternate started, whether the original cell recovered, and whether the short operating rule still applies.

The honest result may be protected output, a shorter queue, no measurable change, a rejection because a constraint was missing, or insufficient data. Stamped records which one occurred.

## 7. Closure loop across all domains

Closure rules apply to every domain: a condition has an owner, a due or review time, a response, a named verification source, and an honest state at the end.

Example: Stamped detects extra machine loads running during a confirmed idle period. It recommends an operator check, assigns the operator, and records the expected state change. After the agreed interval, it checks machine state and the relevant load signal. The card becomes `closed — verified`, `closed — no change`, `rejected`, or `blocked / disputed`; it does not claim success merely because the recommendation was sent.

The normal loop is **detect → recommend → assign → act → verify**. Humans decide and execute by default. A closed state is also a learning event: verified, no-change, and rejected cards all sharpen the next recommendation. A production threshold still needs a named owner. An earned run is the exception defined in §8; it is not smuggled into the default loop.

## 8. Sacred constraints and automation boundary

These are hard stops, not ranking preferences:

- no automatic safety decision or remote command to critical equipment;
- no quality hold release, conformance sign-off, or metallurgical/process acceptance;
- no maintenance authorization or bypass of a maintenance lockout;
- no silent change to customer priority, promise date, routing, master data, or full dispatch sequence;
- no recommendation that outranks a known plant constraint merely because a model predicts a benefit.

Recommendation and assignment are the default. A plant may accept a boundary for a reversible, low-risk workflow. Inside that boundary, an **earned run** can operate with a named owner, audit record, watch mode, and rollback.

Allowed examples include suppressing a duplicate notification or opening a review task after a repeated, agreed condition. Forbidden examples include rerouting a job, switching critical equipment, releasing quality, or changing customer commitments.

If an earned run is wrong, the plant can stop it, see what it did, revert it, and mark the decision disputed. The default remains recommend and assign; earned run is the accepted exception. Earned run never reaches a hard stop.

## 9. Evidence and proof

Each card labels its evidence:

- **Measured:** directly observed from an agreed meter, machine, production, or timestamp source.
- **Confirmed:** recorded by an authorized plant person when system data is incomplete.
- **Modeled:** calculated from approved assumptions; useful for a decision, not proof of realized impact.
- **Unknown:** not enough evidence to claim an effect.

A worked loop might show: idle auxiliary condition measured; operator action confirmed; machine state changed; load signal measured afterward; result was a verified reduction, no measurable change, or rejected because the operator had a legitimate constraint. Metrics we may observe, if data supports them, include idle minutes, alarm dwell, handoff wait, queue age, batch fill, protected output, intensity, operating cost, and time to closure.

The product should show the evidence source beside the result. It should not use modeled and measured values interchangeably.

## 10. How the product works

The first screen should help a role answer: what changed, what choice is available, who owns it, and what evidence will close it.

Stamped reads or ingests signals from meters, machine states, plant automation logs, production systems, maintenance context, calendars, spreadsheets, or structured operator input. The default is read and ingest. Those inputs are joined around one condition — enough to name the asset, the state, the shift, and the owner.

ML models and ML methods, with rules where a rule is the right tool, decide whether the condition is worth a card and what kind of effect is estimated. They do not invent a rupee figure. Evidence stays Measured, Confirmed, Modeled, or Unknown.

The self-improving agent stack turns that condition into a bounded recommendation: options, constraints, uncertainty, and one owner. It learns from closed cards — verified, no change, and rejected. That stack is how we present the current generation of the tech. A production rule still needs named-owner acceptance.

Assignment, the person’s response, and verification close the card. Notification or task creation is allowed when the destination and owner are clear. Write-back is human-confirmed, narrow, allow-listed, and auditable by default. An earned run (§8) is the only exception: one named low-risk action type inside a plant-accepted boundary. It is not general control of the plant.

The action kernel is:

1. **Ingest** relevant signals.
2. **Normalize** assets, states, jobs, batches, shifts, and owners enough to connect one operating condition.
3. **Detect** a condition that may justify action (ML models, ML methods, and rules where they fit).
4. **Recommend** a bounded choice with constraints, tradeoffs, and uncertainty (agent stack).
5. **Assign** the next action to one accountable role.
6. **Record** accept, edit, reject, defer, and reason codes.
7. **Verify** against a named signal or human confirmation.
8. **Propose learning** from closed actions. A threshold or template change requires named-owner review and explicit plant acceptance.

This path — from signal to closed action across the five domains — is the product. It is not a single energy detector and not a logistics module. Stamped never silently writes master data, full priorities, quality release, or critical controls.

## 11. Who it is for

Stamped is for a manufacturer with recurring operational friction, enough observable data to support a decision, and a plant person who will own the response. The champion may be a plant manager, operations leader, energy manager, continuous-improvement leader, or manufacturing engineer. The economic buyer may sit elsewhere; pricing and packaging are not settled.

An illustrative beachhead is an India mid-market discrete manufacturer with a visible utility or constraint problem, existing machine or production data, and a single plant willing to run a narrow pilot. This is a hypothesis, not a permanent geography lock.

The first account should have a recurring decision, a named owner, a practical verification source, and enough repetition for evidence to accumulate. A buyer seeking a generic dashboard, autonomous operator, or full ERP/MES/APS/QMS/CMMS replacement is outside the first wedge.

The same note is what we cut a plant conversation from and what we cut a funding conversation from. Energy wins the first conversation; the company is the five-domain loop.

### Business model and GTM — working hypothesis

Pricing is TBD. The wedge hypothesis is a paid, narrowly scoped site pilot or software subscription anchored to a repeatable decision family, with configuration work kept small and reusable. Energy wins the first conversation because the problem is visible and often has an existing data path; the product must earn expansion by closing a non-energy decision such as machine-minute recovery, handoff wait, or short-horizon exception response. The champion proves floor use; the economic buyer approves the operating or financial value. We will not claim outcome pricing or a savings share until the measurement and contracting basis are real.

## 12. Anti-vision: what we will not become

- **Not an energy dashboard, EMS, or AI savings-report vendor.** A chart without an owned action and verification is outside the product center.
- **Not a generic OEE or analytics vendor.** We may use those measures; we must connect them to one decision and one owner.
- **Not a precision CNC, cycle-time, or tooling-consulting SKU.** We can use those signals when they support a reusable decision family; we do not turn every pilot into custom engineering.
- **Not a vibration or predictive-maintenance hardware company.** We can use maintenance evidence and recommend escalation without selling a sensor fleet.
- **Not a vision-quality or robotics company.** We respect quality and equipment constraints; we do not build inspection or robot-cell products.
- **Not agentic ERP, MES, APS, QMS, or CMMS.** We integrate with systems that own those records; we do not silently replace them.
- **Not a plant-wide digitalization or digital-twin services firm.** We do not promise to model everything or implement every department before one decision loop repeats.
- **Not a default CapEx sensor play.** Hardware serves a proven product decision only when existing data cannot support it and the economics justify the burden.
- **Not an operational-excellence suite.** Operational excellence is the plant’s program, not Stamped’s category.
- **Not an agent operating system.** The agent stack supports the product; it is not the company.
- **Not a plant-wide AI that owns judgment or control.** People in the plant decide. Stamped puts the next action in front of the right one.
- **Not a replacement system of record.** Existing plant systems retain ownership of their records.
- **Not a sensing-pod company.** Sensors serve a proven decision where existing data is insufficient.
- **Not a silent-control product.** Earned runs are allowed only inside an accepted boundary; silent control is not.

## 13. Build order: energy-led entry, five-domain vision

The first loop of the vision is energy-led because energy is concrete, measurable, and often opens a practical first data path. The product boundary is the five-domain decision loop because plants do not experience energy, time, cost, flow, and exceptions as five isolated departments.

Pilot 1 proves the action kernel, not all five domains at once.

### Pilot 1 contract

**First decision family:** confirmed machine idle with extra loads still running, with one owner and a measured or confirmed verification path.

**Required inputs:** machine state or operator-confirmed idle state; relevant load or utility signal where available; shift/calendar context; owner role; and a reason code when the action is rejected.

**Pilot 1 includes:** one decision card, one primary owner, recommendation with a visible constraint, assignment, accept/edit/reject, review time, closure states, and evidence classification.

**Pilot 1 does not include:** automatic equipment control; quality or maintenance release; full production scheduling; APS/MRP replacement; plant-wide energy optimization; a new sensor fleet; a second product called Stamped Process; or a claim about total plant savings.

**Pilot exit bar:** repeated cards are issued for a real condition; a named role closes a meaningful number of assign → act → verify loops each week; the plant peer accepts the evidence format; rejection and no-change cases are recorded; and the team can explain which data is measured, confirmed, modeled, or unknown. If that bar is not met, we fix or abandon the decision family before expanding the domain.

### After Pilot 1

The likely sequence is: energy operating actions; machine idle and alarm dwell; cost tradeoffs tied to a visible operating choice; continuity actions such as handoff waits or batch fill; and bounded exception response. The order can change only when data, action frequency, owner access, and verified evidence justify it.

We add integrations, reusable templates, multi-site playbooks, and carefully bounded materials or quality signals only after the kernel repeats. Quality and Process remain out of the current product pillars.

## 14. FAQ

### What does “Process” mean here?
Process means methods, recipes, work instructions, and document or process freezes. It is not a current Stamped pillar; we may revisit it as a separate bet after the decision and closure kernel repeats.

### What happened to Stamped Process as a second product?
It is deferred, not silently included in this product. The current company focus is operational decisions and closure. We will not let a pilot create a dual-product narrative or pull the core team into document management before the kernel is proven.

### Is Stamped still an energy company?
Energy is the entry wedge and one owned decision domain. The product identity is the five-domain decision loop. The product name is Stamped. We should be able to start with idle load or demand decisions and then prove a machine-minute, flow, cost, or exception decision without changing the core product.

### How is Stamped different from MES, APS, and energy point solutions?

| System | Main horizon | Who acts | Proof it usually provides | Stamped relationship |
|---|---|---|---|---|
| MES | Shop-floor execution and production records | Production roles through execution workflows | Production events, states, quantities, traceability | Read the relevant context; add a bounded decision and closure loop |
| APS | Demand, capacity, routing, and production planning | Planners | Feasible plans and schedules | Treat the plan as context; respond to near-term departures, not replace the plan |
| Energy point solution | Metering, monitoring, tariff, or energy recommendations | Energy or facilities roles | Consumption, demand, intensity, or tariff analysis | Start with energy actions, then connect the action to time, cost, flow, and exception evidence |
| Stamped | Next operating decision and verified closure | One accountable plant role | Action chosen, owner assigned, evidence checked, honest closure state | Integrate with the systems above; do not replace their system of record |

Infinite Uptime is a predictive-maintenance and machine-health category example; Stamped may use maintenance evidence but asks what operating response should happen next across the five domains. Greenovative and similar energy-AI products are energy-category examples; Stamped must distinguish itself by assigning and verifying an operating action rather than stopping at an energy finding. These are category comparisons, not claims about another company’s exact implementation.

### What do we read and write?
The default is read and ingest. We may notify or create a task. Write-back is human-confirmed, narrow, allow-listed, and auditable. An earned run (§8) is the only plant-accepted exception for a named low-risk action type. Stamped never silently changes master data, the full dispatch list, customer priority or promise dates, quality status, or critical controls.

### Is holding a job the same as planning?
No. A short operating hold for one batch or step can be an exception response when an authorized role chooses it and the card has a clear verification path. It is not month-ahead planning. It is never a quality hold release or conformance decision.

### What is low-risk automation / an earned run?
An earned run is an approved, reversible, low-risk workflow with a named owner, watch mode, audit trail, and rollback. Suppressing a duplicate notification or opening a review task may qualify after proof. Rerouting a job, changing a customer date, releasing quality, authorizing maintenance, or controlling critical equipment does not.

### Is the agent stack the company?
No. The agent stack is how we present the current generation of the tech that supports recommendation and learning from closed cards. The company is the five-domain decision loop and the closed action it records. ML models and ML methods are also part of the intelligence.

### Are we an operational-excellence platform?
No. Operational excellence is the plant’s program, not Stamped’s category. Stamped owns a bounded decision and closure workflow that a plant can use inside that program.

### What may run without a person pressing go each time?
Only an earned run inside a plant-accepted boundary. It must be reversible, low-risk, owned, audited, watched, and rollback-ready. Duplicate-alert suppression or opening a review task may qualify. Plant control, quality release, maintenance authorization, customer commitment changes, and critical-equipment switching do not.

### How is this not another layer that only recommends?
Stamped owns the closed action, not infinite recommendation-only behavior. It routes one decision to one owner, records what happened, checks the evidence, and learns from verified, no-change, and rejected outcomes. The plant still decides and executes by default. An earned run is a fenced exception, not a replacement for that default.

### How is this not a system that runs the plant?
The hard stops remain in force. Stamped does not make automatic safety decisions, control critical equipment, release quality, authorize maintenance, rewrite dispatch or customer commitments, or outrank known plant constraints. An earned run is a fenced exception, not plant control.

### Are we a logistics product?
No. Stamped can address continuity, handoffs, batches, queues, and short-horizon exceptions when they form part of an operating decision. It is not logistics-only and does not become a dispatch or full planning system.

### What if the recommendation is wrong or the data is offline?
The plant can reject, edit, defer, or mark a card blocked or disputed. Stamped must show the stale or missing source, avoid false verification, and preserve the reason. A wrong recommendation is a product signal; it is not silently converted into a success.

### Is Cost a first-class outcome?
Yes, but within the five-domain boundary. Cost can be the primary tag when the choice is explicitly about overtime, waiting, alternate capacity, or a visible operating cost. Stamped does not own the plant ledger or invent currency precision. Finance-approved inputs own the money calculation.

### Why not make quality or yield a pillar now?
Quality may constrain a recommendation, but quality release, conformance, and defect accountability require different owners and evidence. They stay outside the current pillars. Stamped never releases a quality hold or signs off conformance.

### Who pays, and how are we priced?
Pricing is TBD. The working hypothesis is a paid site pilot or subscription around a repeatable decision family. The champion may be an energy or plant-operations leader; the economic buyer may be the plant or business owner. We will not invent a pricing unit or outcome claim before the measurement basis is clear.

### What is the first market?
An India mid-market discrete manufacturer is an illustrative beachhead hypothesis, not a locked geography. The stronger filter is one plant with a recurring decision, accessible data, a named owner, and willingness to inspect the evidence.

### How do we avoid a services trap?
No value claim without a closed verification state. Configuration may be needed, but each pilot must leave behind a reusable decision template, evidence rule, role route, and closure pattern. Custom analysis that cannot enter the kernel is a consulting request, not product scope.

### What does success look like before expansion?
A real decision family repeats; one owner is accountable per card; plant peers accept the evidence format; closed, rejected, no-change, and blocked cases are visible; and the team can point to measured or confirmed evidence without mixing it with modeled value. Only then do we add a second domain.

## 15. Build / do-not-build test

Before building, ask:

- What operational decision does this help a plant make?
- Which of the five domains is primary, and what are the secondary tags?
- Who is the one accountable owner?
- What are the evidence source, horizon, constraint, and closure state?
- Is this a next-hours operating choice rather than a new schedule?
- Does it preserve safety, quality, maintenance, and customer-commitment boundaries?
- Can it become a reusable decision family rather than custom consulting?
- Does it work with the plant’s existing systems without silently replacing them?
- Will the closed result make the next recommendation sharper, and does it stay inside the hard stops?

Do not build when the feature is only a dashboard, a generic alert, an unsupported savings claim, an autonomous critical action, a full-planning feature, a new pillar, or a request with no owner and no verification path.

The founder test is: **what decision is Stamped helping the plant make, who acts, what evidence closes it, and what will Stamped refuse to change?**

## 16. What to lift

**Plant cut.** Stamped puts the next operating action in front of one named owner. One card covers Energy, Cost, Time / throughput, Continuity / flow, or a short-horizon exception. The card shows the condition, the bounded choice, the constraints, the uncertainty, and the evidence that will close it. The plant can accept, edit, reject, defer, or verify. An idle-load card recommends a safe idle response, assigns the operator or supervisor, and checks machine state and measured load afterward; it does not add an energy effect and a machine-minute into one savings number. Stamped does not make automatic safety decisions or send remote commands to critical equipment; does not release quality holds, sign off conformance, or give metallurgical or process acceptance; does not authorize maintenance or bypass a lockout; does not silently change customer priority, promise date, routing, master data, or the full dispatch sequence; and does not outrank a known plant constraint because a model predicts a benefit.

**Funding cut.** Stamped turns plant signals into one next operating action with one named owner and a reading that closes it. ML models and ML methods find conditions and estimate effects; they do not own money. The self-improving agent stack is how we present the current generation of the tech; it sharpens options, constraints, and the next recommendation from closed cards, including rejection and no measurable change. The loop is scored by honest closure, not by recommendations issued. Stamped sits on systems the plant already runs. It recommends, assigns, records, and verifies. It does not run the plant. A production rule changes only when a named plant owner accepts it.
