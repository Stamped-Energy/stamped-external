# Coarse architecture — how L1–L6 evolves

**Date:** 2026-09-24
**Status:** Coarse target. Fine design belongs in each layer repo.
**Authority:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md), then [`10-stamped-vision-agent-alignment.md`](10-stamped-vision-agent-alignment.md). This file does not replace either.
**As-built:** [`13-as-built-invariants.md`](13-as-built-invariants.md).
**Patterns:** [`12-peer-architecture-patterns.md`](12-peer-architecture-patterns.md).

**Stamped helps plant teams choose, assign, and verify the next operating action across energy, cost, time / throughput, continuity / flow, and short-horizon exceptions.**

The six-layer path stays. L4 is rebuilt into a **proper agentic system** (planning, tools, memory, evaluation — memory is one part, not the whole). L3’s contract floor stays, but its **detection technology direction is open** — we aim to be best-in-class, not to freeze today’s engines. L5 is the only layer that may carry out an enabled action. Compute cost is not a reason to under-build L3 or L4. Hard stops still bind what may touch the plant.

## What each layer does

**L1 stays read-only.** A connector is added when a named decision family needs that source. Pilot 1 uses machine state and load the edge path already accepts. No equipment write. No plant message broker.

**L2 grows a little.** It remains the only database. It stores a constraint registry (scope, owner, expiry, source), who holds a role on a shift, and a condition key: asset, state window, and shift. A named plant owner writes constraints in L6. L2 stores them. L4 only reads them. If no live family reads a relation, it does not get a table.

**L3 keeps a contract floor and an open tech ceiling.** Hot, warm, and cold paths, dual-lane emit, no database URL, lab never promotes, calculator owns money — those stay. Each finding gains a condition key, a decision-family id, a primary domain taken from that family, evidence-tiered facts, an effect per domain section, and a verification plan. Findings that share a condition key merge before L4. Beyond that floor, L3 is allowed and expected to become far stronger (methods, features, evals, multi-signal detection). That uplift is designed in the L3 repos later; this note does not freeze today’s detector catalog as the ambition.

**L4 is the agentic system.** Not “a long-lived agent plus a memory product.” The system plans, uses allowlisted tools, runs specialist passes, checks the rest of the plant, evaluates honesty, and emits one card proposal. Memory (Hindsight plant bank + dialogue banks) is a subsystem. The shell that stays is emit, withhold, abstain, a trace on every run, a constraint gate, calculator-owned rupees, and no equipment or master-data write. Inside that shell we aim for state-of-the-art agentic engineering.

**L5 owns the live card.** It resolves the person, records the response, verifies, closes, and runs an action only when that class is certified and enabled.

**L6 is the card.** One queue. Domain sections on the card. Honest closes. Constraint editing for a named owner. Autonomy settings, default off.

## L4 agentic system (memory is one part)

L4 is a **proper agentic system**: planning / orchestration, specialist passes, allowlisted tools, evaluation and gates, and memory. We keep studying how the best agentic systems are built and raise L4 to that bar. Compute is not a reason to shrink it.

Memory is [Hindsight](https://hindsight.vectorize.io/). Hosting, their cloud or self-host, is decided in the L4 repo.

The plant bank is one per plant, tagged by section, asset, decision family, and shift. It stores world facts (conditions, constraints, neighboring state) and short learning facts. It does not store the card body or a chat transcript. A learning fact carries family, asset, sections touched, disposition or withhold reason, the constraint that fired, and the evidence tier.

[Observations](https://hindsight.vectorize.io/developer/observations) consolidate those facts in the background, with quotes and a proof count. A contradiction updates the belief and keeps the history. The observations mission asks for durable operating patterns and ignores one-off card text. An ineligible close may teach that evidence was missing. It may not teach that the action worked. Reflect reads mental models, then observations, then raw facts, and checks a stale observation against the facts. Directives are the hard stops, plus cite an evidence tier, plus do not invent rupees. A production threshold, template, or mental model changes only after a named owner accepts it.

Dialogue banks are one per conversation. Threads cannot see each other or the plant bank. Hindsight has no cross-bank query. Ask, below, merges the two reads in L4.

## Cross-section check

Before emit, L4 checks the sections that share the condition: upstream feed, downstream block, shared utilities, the shift, and open cards on related assets. A local action that starves or blocks another cell is withheld, or it ships with that conflict on the card. Specialist passes inside L4 may look at energy, flow, and constraints. They reconcile into one card. They do not each talk to the plant.

The public pattern this follows is a whole-operation check before a local action. Stamped does not adopt a sensing pod, does not run the plant, and does not publish a new schedule. See [`12-peer-architecture-patterns.md`](12-peer-architecture-patterns.md).

## One card, five domain sections

Energy, cost, time / throughput, continuity / flow, and exception response are sections of one proposal. One primary domain names the decision. Optional secondary domains appear only as their own sections. Each section has its own claim, evidence tier, and effect. Energy and machine-minutes stay apart. Rupees stay in the calculator's section. A domain that does not apply is absent. L5 stores the sections unchanged. L6 renders them on the one card. There are not five inboxes.

## Two objects

L4 emits an immutable card proposal: domain sections, one recommended action, at most two alternatives, one of which is always "no action," a proposed owner role, an autonomy class or "human only," uncertainty, and a verification plan copied from the finding and allowed only to narrow.

L5 owns the mutable live card: the person, the eight closure states, history, the same domain sections, and whether a human ran it or an enabled class did.

Prescription 1.0.0 stays. The proposal is a new schema beside it. L5 reads both through an adapter until 1.0.0 is retired. One product.

## Who decides what

L4 decides what should be proposed. L5 decides what is allowed to happen, who the person is, and whether it happened.

- L4 chooses one role from the configured set. A production task routes to the production head. An operational task routes to the ops head. The language model makes that choice now. The set is closed, so a later decision model can replace that call. L5 resolves the role to the person on the shift. It does not pick a different role.
- L4 withholds when a known constraint conflicts, whatever the predicted benefit. L5 refuses execution when the class is off, uncertified, or a hard stop.
- L4 labels an autonomy class. It does not run it.
- L4 writes the trace. L5 assigns, notifies, records accept, edit, reject, or defer, verifies, closes, and supplies the short learning fact.

## Autonomy

Default: no autonomous actions. A class runs only after Stamped certifies it and a named plant owner enables it. The first two classes, from `09`, are suppress a duplicate notification, and open a review task. A plant may propose another class. It stays pending until Stamped certifies that it is reversible, low-risk, audited, watched, rollback-ready, and not a hard stop. Idle-load and any equipment action are not in the catalog.

## Decision seams

[Jev](https://jevtypesafeai.com/jev-ai) returns a typed choice and a probability. It does not write prose. This note does not call it. The closed moments, where a later decision model may replace the language model, are:

- emit, withhold, or abstain
- which capped action to recommend, including "no action"
- whether a named secondary domain applies
- whether a cross-section conflict is present
- which autonomy class label applies, or human-only
- which configured owner role to propose

The primary domain stays on the decision family. A low-confidence result falls back to the generative agent. A probability never runs an action and never emits rupees. The explanation on the card comes from the trace and from the generative path.

## Ask

L6 paints the thread. L4 holds it. The browser never holds a bank key. Ask reads the dialogue bank for this thread and the plant bank for what the plant did, then answers. A chat line enters the plant bank only as an explicit promoted fact, after a person confirms it or a closure verifies it. Ask does not emit a card, does not change autonomy policy, and does not issue a second recommendation. A new action goes through the same propose path as any other finding.

## Tools

Allowlisted typed reads: L2 query HTTP, the constraint registry, open cards, and Hindsight recall and reflect. No raw SQL. No open web as authority. No equipment write.

## Pilot 1, in one pass

Confirmed machine idle with extra loads still on. Configured as an operational task, so the role is the ops head. Primary section is energy. A machine-minute effect, if any, is a separate time section. Verification follows [`16-pilot-and-hard-stops.md`](16-pilot-and-hard-stops.md). Autonomy stays off. The old template lane runs only when the agent cannot emit a valid, cited, constraint-checked proposal.

## Next family

Alarm dwell, then one handoff or exception, only with a named owner role, a verification source already in L2, a reviewed constraint, and a reusable template. New connectors follow that list. Not a full MES, routing, or quality model.

## Alignment check

- Product name is Stamped.
- The sentence is still choose, assign, and verify across five domains.
- One condition, one card, one owner, one close.
- Evidence tiers stay Measured, Confirmed, Modeled, Unknown. Wallets stay separate. The calculator owns money.
- Hard stops are intact.
- Recommend and assign are the default. An autonomous class is certified, enabled, reversible, and watched.
- The agentic system (and strong L3 detection) is how the current tech is presented. The company is the closed decision.
- No summed savings headline. No claim that Stamped runs the plant.
