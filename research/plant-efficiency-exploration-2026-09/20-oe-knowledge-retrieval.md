# OE knowledge retrieval — gap, GraphRAG pattern choice, corpus

**Date:** 2026-09-25  
**Status:** Research + architecture intent. Not an implementation.  
**Authority:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md) wins on conflict. L4 contract: [`../../technical/l4/`](../../technical/l4/).  
**Companion:** [`../../technical/l4/23-oe-knowledge-corpus.md`](../../technical/l4/23-oe-knowledge-corpus.md)  
**Source article:** [GraphRAG: A Practitioner’s Guide to 6 Advanced Architectural Patterns](https://towardsdatascience.com/graphrag-a-practitioners-guide-to-6-advanced-architectural-patterns/) (Partha Sarkar, Towards Data Science, 2026-09-20).

---

## 1. Is this already in the L4 architecture?

**Short answer: no — not as a first-class OE knowledge corpus.**

What L4 *does* have today:

| Piece | What it is | What it is not |
| --- | --- | --- |
| Playbook bullets (procedural memory) | Short, versioned, lockfile-pinned bullets under ACE-style improvement | Not a place to dump books or sourcebooks |
| “Grammar always on; knowledge retrieved” ([`05`](../../technical/l4/05-context-engineering.md)) | Retrieves playbook + case summaries + workflow excerpts into the **advisory** partition | Not semantic search over a large document store |
| Hindsight plant bank | Plant-specific world facts and learning facts from closures | Not general “how to drive efficiency” literature |
| Case library | Episodic traces + L5 outcomes | Not textbooks |
| Research `19` | DOE / Roser / NIST methods **adopted into design** (scanners, constraint kinds) | Not a runtime retrieval store the LLM queries |

So the major gap you named is real: there is no subsystem where we ingest operational-excellence documentation and books so that, for a given plant situation, L4 can retrieve *how efficiency is typically driven in that class of scenario* — as advisory knowledge — without inventing rupees or overriding hard stops.

Plant memory answers “what worked *here*.”  
OE knowledge answers “what methods exist *in general* for this class of waste.”  
Both are needed. Only the first was specified.

---

## 2. What the GraphRAG article says (six patterns)

From Sarkar’s practitioner guide — GraphRAG is an umbrella, not one product:

| # | Pattern | Strength | Weakness | Fit for Stamped OE corpus? |
| --- | --- | --- | --- | --- |
| 1 | Text-to-Cypher | Exact traversals, counts, aggregations | Brittle without embeddings; no prose nuance | Useful later for “which methods apply to shared-resource X” if ontology is tight |
| 2 | **Parallel Hybrid (vector + graph)** | High recall; semantic + relational; concurrent | Token-heavy; some redundancy | **Strong default for mixed OE queries** |
| 3 | Sequential Graph-First | Precise; filters vector by entity docs | Sequential latency; fails if edge missing | Good when query is entity-centric (asset class → method family) |
| 3b | Sparse Graph + Graph-First | Cheap skeletal graph; vector fills nuance | Less relational richness | **Best v1 cost path** |
| 4 | Sequential Vector-First | Fuzzy start; then expand relations | Context bloat risk | Good for Ask / open “what should we look for?” |
| 5 | Adaptive Router | Routes to cheap path when possible | Router can misclassify | Later, when Ask traffic is diverse |
| 6 | Agentic GraphRAG | Deep multi-step research | Minutes of latency; unbounded cost | **Offline council / research only — never plant request path** |

Microsoft’s hierarchical community GraphRAG (global themes / map-reduce) is a seventh cousin: useful for offline corpus QA (“what themes dominate this sourcebook set?”), not for a 2-second DecisionCase.

---

## 3. Pattern choice for Stamped

### Constraints that pick the pattern

- Plant path must stay low-latency and pinned (lockfile, dual-family Flash + Luna).
- Retrieved OE text is **advisory only** — measured partition and calculator still own facts and ₹ ([`05`](../../technical/l4/05-context-engineering.md)).
- Hard stops / hard gates never come from a document chunk.
- Models never traverse plant topology graphs ([`03`](../../technical/l4/03-plant-situation-model.md)); that stays code. The OE knowledge graph is a **different** graph: methods ↔ scenarios ↔ evidence needs ↔ typical footprints — not the plant.
- Prefer sparse extraction cost in v1 (article Challenge 1).

### Decision

| Layer | Pattern | Why |
| --- | --- | --- |
| **v1 plant DecisionCase** | **Sparse ontology + Vector-First (or Parallel Hybrid with a small graph)** | Fuzzy “idle auxiliary on shared air header” → retrieve method bullets + sourcebook chunks; optional 1-hop expand to related methods / required signals |
| **Ask / staff research** | Parallel Hybrid or Adaptive Router | Mixed conceptual + relational questions |
| **Offline council / corpus curation** | Agentic GraphRAG or Microsoft-style global search | Build playbook proposals from the corpus; never on the live card path |
| **Not chosen for plant path** | Pure Text-to-Cypher alone; dense LLM extraction of every page; Agentic loops | Brittleness / cost / latency |

**Rejected:** treating the Plant Situation Model as the GraphRAG store. PSM is plant truth cache. OE corpus is general method knowledge. Mixing them recreates “graph becomes the product” for literature.

**Would change this:** measured Pilot evidence that Vector-only (no graph) already lifts accept rate enough; or that Graph-First with a richer method ontology beats Vector-First on precision without latency pain.

---

## 4. How retrieval plugs into L4 (so it does not break the kernel)

```text
Finding / discovery situation
        │
        ▼
 code builds evidence ledger (measured)
        │
        ▼
 OE retrieval seam (typed): situation features → top-K chunks + optional method nodes
        │
        ▼
 advisory partition rows (tier=Advisory, provenance=doc_id#chunk)
        │
        ▼
 dual-family draft / critique (may cite advisory rows; may not invent ₹)
        │
        ▼
 hard gates / constraints / calculator unchanged
```

Rules:

1. OE retrieval is a **read tool / seam** with closed options (mission ids, max chunks, allowed corpora).
2. Rows land only in the **advisory** partition — never Measured.
3. Uncited OE claims are dropped like any other claim.
4. OE text never sets a rupee; never evaluates a constraint; never chooses emit.
5. Corpus version + embedding model pin sit in the **release lockfile**.
6. Plant-specific SOPs may be ingested only with named owner approval (license + confidentiality).

---

## 5. What to ingest (corpus inventory)

### Tier A — public, high priority (v1 seed)

| Corpus | Why | License note |
| --- | --- | --- |
| **DOE AMO / BestPractices sourcebooks** — compressed air, pumps, fans, motors, steam, process heating | System-level efficiency opportunities; already cited in research `19` | Public US gov; confirm edition on ingest |
| **DOE tip sheets / fact sheets** (Save Energy Now pack) | Short, actionable; good chunk size | Public |
| **EPA Lean, Energy & Climate Toolkit** | Links lean (VSM, kaizen, TPM, standard work) to energy waste | Public |
| **ISO 50001 / SEP overview materials** (public summaries, not pirated paid text) | Energy management system framing | Prefer public guidance docs |
| **IPMVP / verification primers** (public summaries Stamped already uses for Pilot 1) | Keeps verification language consistent | Public / licensed |

### Tier B — methods Stamped already designed against (curate → bullets + selective chapters)

| Source | Use |
| --- | --- |
| Roser et al. — shifting bottleneck / active-period / blocked-starved | Discovery system methods; do not dump entire papers if paywalled — curate method cards |
| Factory Physics (Hopp & Spearman) — variability, WIP, buffers | Continuity / time domain analysis playbooks — **licensed book; ingest only if Stamped holds rights** |
| Goldratt TOC — constraint focus | Exception / bottleneck framing — same license rule |
| NIST digital-twin / simulation credibility guidance | Envelope language for L3 simulators |

### Tier C — plant-private (per site pack, owner-gated)

| Source | Use |
| --- | --- |
| Named plant SOPs / energy treasure-hunt reports | Site-specific advisory; hard wall from other plants |
| OEM manuals for commissioned assets | Idle / setpoint / maintenance windows — never write instructions that imply OT write |
| DISCOM tariff schedules / plant energy policy | Context for calculator, not a second money path |
| Prior approved Stamped playbooks from other sites | Only anonymised, owner-approved (cross-plant seam — not v1) |

### Tier D — deliberately out of corpus

- Marketing PDFs with unverified % savings claims
- Anything that instructs silent setpoint / PLC write
- Full chat transcripts
- Raw L2 series (those stay in L2 / PSM)
- Copyrighted textbooks without a license

---

## 6. Ontology for the sparse OE graph (minimal)

Nodes (examples):

- `Method` (e.g. leak-survey, pressure-band, idle-auxiliary-shutdown-check)
- `ScenarioClass` (idle load, partial load, shared-resource peak, handoff wait, bottleneck shift)
- `Domain` (registry id: energy, cost, time, continuity, exception)
- `RequiredSignal` (meter class, state tag, buffer fill)
- `HardStopTag` (safety, quality hold, metallurgy) — retrieval **must not** propose actions that violate these
- `SourceDoc` / `Chunk`

Edges (examples):

- `APPLIES_TO` Method → ScenarioClass  
- `NEEDS_SIGNAL` Method → RequiredSignal  
- `IN_DOMAIN` Method → Domain  
- `CITED_IN` Method → Chunk  
- `CONFLICTS_WITH` Method → HardStopTag  

v1 extraction: deterministic NLP / structured curation for Tier A fact sheets; optional LLM extraction only on high-value pages (article sparse-graph practice).

---

## 7. Retrieval missions (how the DecisionCase calls it)

Suggested allowlisted missions (registry):

| Mission | Trigger | Returns |
| --- | --- | --- |
| `oe_methods_for_scenario` | Family / pattern / scanner class | Top methods + chunks |
| `oe_required_signals` | Method under consideration | Signal checklist as advisory rows |
| `oe_conflict_warnings` | Footprint + hard-stop tags | Warnings only |
| `oe_ask_explore` | Ask thread | Broader Parallel Hybrid pack |

Each mission logs a seam decision record ([`11`](../../technical/l4/11-models-and-seams.md)) for later Jev / classifier replacement of the *routing* choice — not of the document store itself.

---

## 8. Relationship to playbooks (do not double-build)

| Store | Mutability | Authority |
| --- | --- | --- |
| OE corpus (this note) | Versioned ingest; large | Advisory literature |
| Playbook bullets | Curated, ACE-improved, lockfile | Procedural — what Stamped *chooses* to prefer after replay |
| Case library | Plant outcomes | Outcome authority |

Offline council may **propose** playbook bullets *from* OE retrieval + case outcomes. It may not auto-promote corpus text into playbooks.

---

## 9. v1 slice vs later

| v1 | Later |
| --- | --- |
| Tier A public sourcebooks + tip sheets; vector index; sparse method ontology hand-curated for Pilot families | Broader Tier B under license; denser extraction |
| Vector-First retrieval into advisory partition on investigative lane + Ask | Parallel Hybrid default; Adaptive Router for Ask |
| No Agentic GraphRAG on plant path | Offline corpus curation agent |
| No plant-private SOP ingest until owner pack | Per-plant corpus partition |

---

## 10. What would change this note

- A Pilot A/B where OE retrieval raises eligible accept rate without raising hard-gate hits or invented-₹ withholds.
- Evidence that Graph-First alone beats Vector-First for method selection precision.
- Legal clearance (or blockage) for specific commercial books.

---

## 11. Sources

- Sarkar, P. — GraphRAG practitioner patterns (Towards Data Science, 2026-09-20).  
- DOE EERE / AMO technical publications by system (compressed air, pumps, fans, motors, steam, process heating).  
- EPA Lean, Energy & Climate Toolkit.  
- Stamped research `19` (DOE sourcebooks, Roser, NIST) and L4 docs `05`, `06`, `13`.
