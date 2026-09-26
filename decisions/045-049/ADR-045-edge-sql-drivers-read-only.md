# ADR-045: edge SQL drivers and read-only enforcement

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-27 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-031](../028-032/ADR-031-l1-l2-context-records.md) · [ADR-044](../040-044/ADR-044-edge-field-protocols.md) · research `docs/plans/l1-complete/RESEARCH.md` |

---

## Context

Historian and `sql_rows` open `database/sql` with the sqlite driver only (`modernc.org/sqlite`). `ValidateSelect` already rejects writes at load time. Plant historians are Postgres or MySQL. Query-text checks are not enough if a DSN is writable.

---

## Decision

1. **Drivers.** `github.com/jackc/pgx/v5/stdlib` **v5.11.0** (register `"pgx"` / `"pgx/v5"`) and `github.com/go-sql-driver/mysql` **v1.10.0** (register `"mysql"`). sqlite remains the default and the unit-test path.
2. **Keep** `ValidateSelect` (SELECT/WITH only, no multi-statement, no write keywords) **and** the watermark poll (`WHERE {wm} > ? ORDER BY {wm} ASC LIMIT …`).
3. **Session read-only on connect**, before the first query:
   - Postgres: DSN `options=-c default_transaction_read_only=on` and `SET SESSION CHARACTERISTICS AS TRANSACTION READ ONLY`.
   - MySQL: `SET SESSION TRANSACTION READ ONLY`.
4. **Poll** inside `BeginTx(ctx, &sql.TxOptions{ReadOnly: true})` (pgx → `BEGIN READ ONLY`; mysql → `START TRANSACTION READ ONLY`).
5. **Lab images:** `postgres:16-alpine`, `mysql:8.4`. Integration tests assert that INSERT/UPDATE fail at the database.

---

## Hard stops

- Read-only. A SQL write attempt must not succeed, even if `ValidateSelect` is bypassed in a test.
- No OT write. Historian/sql_rows never issue SET/ACTION against field devices.
- No `L2_DATABASE_URL` in L1. Plant historian DSNs are site secrets by reference.
- Unmapped columns → `unmapped_tag`, never a zero.

---

## Consequences

- B5 adds the modules to `edge-agent` `go.mod` and driver switch in historian + `sql_rows`.
- `default_transaction_read_only` can be overridden in a session; the connector must not issue `SET … READ WRITE`.
- Changing drivers or dropping session GUC/SET needs a new ADR.

---

## Rejected alternatives

- Query-text validation alone.
- lib/pq (unmaintained relative to pgx v5).
- Opening L2 Timescale from L1.
