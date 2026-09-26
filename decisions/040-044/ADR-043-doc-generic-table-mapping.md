# ADR-043: connectors-doc generic CSV/XLSX mapping via pack schema

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-27 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-041](ADR-041-connectors-doc-charter.md) · [ADR-031](../028-032/ADR-031-l1-l2-context-records.md) · [`contracts/packs/pack.schema.json`](../../contracts/packs/pack.schema.json) |

---

## Context

Plant people upload spreadsheets that are not DISCOM bills. connectors-doc already fingerprints EMS CSVs. Edge already loads system packs (`file_rows` / `rest_rows` / `sql_rows` / `opcua_state`) against `pack.schema.json`. A second mapping language would drift.

---

## Decision

1. **One pack format.** connectors-doc loads the same YAML/JSON pack document the edge pack loader validates (`pack_id`, `pack_version`, `engine`, `record_type`, `field_map`, optional `timezone`, `date_format`, `number_grouping`, `asset_ref`, `secret_ref`, `description`).
2. **User column map = `field_map`.** Saved as a pack with `engine: file_rows` and a catalog `record_type`. No extra keys (`additionalProperties: false`).
3. **XLSX.** First sheet → rows, then the same `field_map`.
4. **No schema bump** in this run. `file_rows` already exists.
5. **Unresolved columns or assets** emit `unmapped_tag`. Never write a zero or a guessed timestamp.

---

## Hard stops

- `secret_ref` is a name, never a literal password.
- No invented money when `record_type` is `bill_line` — ₹1 gate + review still apply.
- Review before publish for human uploads.
- Unmapped → event, never a silent default.

---

## Consequences

- Doc and edge can share pack fixtures in tests.
- EMS fingerprint profiles remain a convenience matcher; the durable map is the pack.
- A new engine value would be a contract change and a new ADR.

---

## Rejected alternatives

- A doc-only column-map JSON beside the pack schema.
- Auto-mapping leftover headers into numeric zeros.
