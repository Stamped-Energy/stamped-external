# ADR-041: connectors-doc — rename and charter

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-27 |
| **Deciders** | Product + Engineering |
| **Amends** | [ADR-001](../001-005/ADR-001-l1-repo-split-and-boundaries.md) §1 / §6 |
| **Related** | [ADR-007](../006-010/ADR-007-connectors-cloud-repo-charter.md) · [ADR-031](../028-032/ADR-031-l1-l2-context-records.md) |

---

## Context

ADR-001 split L1 into two repos (`connectors-edge`, `connectors-bill`) and deferred cloud ingest. ADR-007 already chartered `connectors-cloud`. The third live L1 repo is still named and scoped as “bill ingest,” which hides the people door: photos, scans, PDFs, and spreadsheets. Utility bills are one document family, not the company.

---

## Decision

1. **Rename.** The third L1 repo is **`connectors-doc`** (was `connectors-bill`). Folder, GitHub, CI, compose, and live docs follow in the B0 node. Paths on disk may still be `connectors-bill` until that rename lands.
2. **Charter.** Human document ingest: photos, scans, PDFs, CSV/XLSX. Someone uploads; the service extracts; a person reviews; an explicit publish sends records to MQTT. Quality sheets, production logs, handwritten plant records, and mapped spreadsheets are equal citizens.
3. **Bills.** Utility bills remain one family on this door, with the **₹1 recompute gate**. A `bill_line` is trusted only when extracted lines sum to the printed total within ₹1. Missing printed total fails the gate. No invented charge lines.
4. **Payload names unchanged.** `bill_line`, MQTT `…/bills`, `discom_bill` lane, `recompute_bill`, `templates/bills/` stay. Do not bump contracts for the rename.
5. **Producer string.** If any contract enum pins the producer `'connectors-bill'`, add `'connectors-doc'` **additively**. The old value stays accepted. No exclusive cutover in this ADR.
6. **L1 is three repos.** `connectors-edge` (OT/IT read), `connectors-cloud` (ingest door to L2), `connectors-doc` (people door). Cloud is not deferred.

---

## Hard stops

- Read-only door: no OT write, no ERP/MES/CMMS write-back.
- No invented money. No silent repair of amounts.
- Nothing publishes to MQTT without an explicit human publish call.
- No `L2_DATABASE_URL` in this repo.

---

## Consequences

- B0 performs the rename. Later nodes write as `connectors-doc`.
- Review UI and PWA stay in this repo; this ADR does not redesign UI.
- Edge and cloud keep publishing/consuming the same `bill_line` schema.

---

## Rejected alternatives

- Keep the repo name `connectors-bill` and only retitle docs.
- New record types or a contract version bump for the rename.
- Auto-publish when recompute passes.
