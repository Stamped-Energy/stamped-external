# ADR-042: connectors-doc OCR and review confidence

| Field | Value |
| --- | --- |
| **Status** | Accepted |
| **Date** | 2026-09-27 |
| **Deciders** | Product + Engineering |
| **Related** | [ADR-041](ADR-041-connectors-doc-charter.md) · research `docs/plans/l1-complete/RESEARCH.md` |

---

## Context

Photos, scans, and handwriting are in the doc charter. The live ladder (`pdfplumber` → Tesseract → Textract) scores a whole page, invents bill lines when text is thin, and auto-publishes a passing recompute. Plant records must not guess amounts.

---

## Decision

1. **Baseline engine for photos/scans:** Tesseract 5 via `pytesseract` in the doc container (`python:3.12-slim-bookworm` + `tesseract-ocr`, `tesseract-ocr-eng`, `tesseract-ocr-hin`).
2. **Fallback:** keep the existing ladder for native-text PDFs (`pdfplumber` first). Textract stays optional and mockable; it is not required for local Docker.
3. **Not baseline:** PaddleOCR / PP-StructureV3 (better tables and handwriting; ~2 GB image and first-run model fetch — later optional provider behind the same `OcrProvider` protocol).
4. **Per-field confidence:** Tesseract `image_to_data` word `conf` ÷ 100, averaged onto the mapped field. Unmapped words do not invent a field.
5. **Review threshold:** confidence **< 0.75** → field is `null` / empty and `review_required`. **Never guess.**
6. **Publish:** documents do not MQTT-publish without an explicit human publish. A flagged money field or a missing printed total cannot pass the ₹1 gate.

---

## Hard stops

- No invented ₹, qty, rate, or dates.
- Flag, never guess, on low-confidence fields.
- Review before publish.
- Local-first: default path runs in Docker without AWS.

---

## Consequences

- Handwriting will often flag; that is correct. A person types or confirms the field.
- B2 implements photo tests against the Tesseract baseline.
- Changing the threshold or swapping the baseline engine needs a new ADR.

---

## Rejected alternatives

- PaddleOCR as the default container engine.
- Page-level confidence only.
- Filling low-confidence cells from LLM hints without review.
