# AGENT-START — internal handoff for product AI agents

**Audience:** AI systems given this folder to understand Stamped and update **internal** product documentation.  
**Not for:** website, pitch decks, LinkedIn, ads, or other external marketing. That copy will be written later on purpose. Do not restyle public marketing from this pack.

---

## 1. Open these three files in order

| Order | File | Role |
|-------|------|------|
| 1 | This file | Folder contract |
| 2 | [`09-stamped-founder-vision.md`](./09-stamped-founder-vision.md) | **Canonical company vision** — wins on conflict |
| 3 | [`10-stamped-vision-agent-alignment.md`](./10-stamped-vision-agent-alignment.md) | Operating contract: invariants, hard stops, alignment check, change queues |

Then read research `00`–`08a` only as **history and evidence**. Their recommendation sections have been aligned to `09`. Peer survey facts stay. They must not invent a second company.

Human readers may start at [`START-HERE.md`](./START-HERE.md). Agents start **here**.

---

## 2. Company lock (do not drift)

**Product name:** Stamped. Do not append Energy to the product name.

**One sentence:**  
**Stamped helps plant teams choose, assign, and verify the next operating action across energy, cost, time / throughput, continuity / flow, and short-horizon exceptions.**

**Identity in one breath:** one decision card, one owner, honest close. Five domains. Wide coverage, narrow authority. Energy is the entry wedge, not the category. Recommend and assign by default. Hard stops stay. ML models and ML methods find conditions and estimate effects. The self-improving agent stack is how we present the latest tech — it is not the company.

**Internal only.** Wording in `09`, `10`, and this file is founder language for agents that write architecture, prompts, ADRs, research, and product contracts. It is not external marketing.

---

## 3. What each file is for

| File | Agent rule |
|------|------------|
| `AGENT-START` (this) | Entry. Authority map. Out of scope. |
| `09` | Vision. Prefer over everything else. |
| `10` | How to align docs. Alignment check. Internal change queues. |
| `00`–`08a` | Research that led here. Use facts; follow updated recommendations; do not reopen A–E as the company decision. |
| `02`–`04` | Peer facts and vendor-claimed numbers — keep; do not treat competitor copy as our category. |
| `README` / `START-HERE` | Indexes. Point humans and agents to authority. |

---

## 4. How this folder may change itself

**May edit:** banners; recommendation / conclusion / next-step sections in `00`–`08` and `08a`; `README`, `START-HERE`, `AGENT-START`, `10`.

**Leave alone unless asked:** peer survey bodies and vendor numbers in `02`–`04`; mode tables as data inventory in `01`; action-catalog rows as research inventory in `08`.

**Do not:** rewrite `00`–`08` into a second copy of `09`; invent savings, customers, or revenue; update external marketing.

---

## 5. How other projects may change (internal only)

When the human asks you to realign other repos, use [`10`](./10-stamped-vision-agent-alignment.md) §17–§18 (this-folder rules + other-project queue). Prefer architecture, ADRs, value architecture, strategy memos, and agent prompts. Skip sites, decks, and outbound copy.

Do not edit those other repos in the same session **unless the human asked**. Report **Aligned / Changed / Open**.

---

## 6. Anti-vision (tight)

Stamped is not: an energy dashboard / EMS; a generic OEE vendor; a MES/APS/ERP replacement; a plant OS or silent-control product; an operational-excellence suite or agent OS; a logistics-only SKU; a default CapEx sensor play.

---

## 7. Pasteable start prompt

```text
You are working from the plant-efficiency research pack (internal only).
Open AGENT-START.md first, then 09-stamped-founder-vision.md, then 10-stamped-vision-agent-alignment.md.
Product name: Stamped. Company = choose/assign/verify across five domains.
09 wins on conflict. Do not update external marketing.
Do not invent savings, customers, or revenue.
If updating docs: run the ALIGNMENT CHECK in 10. Return Aligned / Changed / Open.
```
