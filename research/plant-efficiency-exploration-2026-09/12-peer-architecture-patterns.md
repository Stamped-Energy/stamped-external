# Peer architecture patterns — adopt, adapt, or reject

**Date:** 2026-09-24  
**Status:** Research for the coarse architecture. Not an implementation.  
**Authority:** [`09-stamped-founder-vision.md`](09-stamped-founder-vision.md) wins on conflict.  
**Confidence:** **High** means a vendor doc or product page states it. **Medium** means a consistent implication. **Low** means a third-party or thin public record. Nothing here is a private architecture.

**L4 follow-on:** for agent-system peers, dual-model reviews, plant-wide methods, and the L4 adopt map, use [`19-l4-agent-peer-systems.md`](19-l4-agent-peer-systems.md). Keep this file for the earlier layer adopt / adapt / reject map.

## Sight Machine — semantic model and investigation agents

**Paradigm (High):** plant data is mapped into a semantic model so agents can investigate and recommend. Public pages name controls, historians, MES, and ERP as sources, and describe expert approval of mappings before agents reason. FactoryTX docs describe edge or cloud collection into a cloud path. **Medium:** that path is acquisition into their cloud, not a bidirectional equipment bus. Public docs reviewed here do not describe silent PLC write-back as a first-class product path (**High** that the acquisition docs are one-directional; **Low** on whether an undocumented connector writes back).

They publish manufacturing intelligence as an MCP server and name Teams, Excel, Databricks, and Omniverse as places recommendations can go (**High**, product pages). A homepage output-gain figure is a **vendor claim**.

**Adopt:** expert-approved mapping with provenance, before an agent recommends.  
**Adapt:** edge collect with durable offsets. Stamped already has a read-only edge agent. Do not become their full multi-protocol product.  
**Reject:** a line-wide semantic program before one decision exists; scheduling autonomy; agent-written production apps as the default; progressive permission to control equipment.

Sources: [semantic model](https://www.sightmachine.com/platform-semantic-model), [dynamic production](https://www.sightmachine.com/platform-dynamic-production), [FactoryTX concepts](https://factorytx-docs.sightmachine.com/v4.2.1/concepts/index.html).

## Cognite — knowledge graph and tool confirmation

**Paradigm (High):** extractors near the source, raw staging, transforms, then a property graph. Agents retrieve and summarize. Side-effecting tools such as calling a function require an explicit allow or deny in the API docs (**High**). Atlas guidance says agents are unsuitable for fully autonomous safety-critical decisions (**High**).

**Adopt:** the confirmation gate on any side effect. Stamped’s version is L5 policy, default off.  
**Adapt:** stable IDs and a thin context for one condition.  
**Reject:** a mandatory industrial graph of documents, 3D, and every asset as the price of the first card. **Medium:** a customer can wire a function to write anywhere that function can reach. That is not our action path.

Sources: [CDF overview](https://docs.cognite.com/cdf), [contextualization](https://docs.cognite.com/cdf/integration/concepts/contextualization), [call function tool](https://docs.cognite.com/cdf/atlas_ai/references/atlas_ai_call_function_tool).

## HighByte and the unified namespace

**Paradigm (High):** edge DataOps publishes a hierarchical namespace, often MQTT and ISA-95 shaped. Pipelines can write OPC UA tags and MQTT topics. That write path is intentional.

**Adapt:** ISA-95 names as a contract for “where this signal sits.”  
**Reject:** becoming the plant’s message broker, and any OPC UA write pipeline. An event-driven write is automation, not a verified human action.

Sources: [Intelligence Hub](https://www.highbyte.com/intelligence-hub), [namespaces](https://www.highbyte.com/intelligence-hub/namespaces), [pipeline outputs](https://guide.highbyte.com/dev/configuration/connect/outputs/).

## Palantir — governed actions

**Paradigm (High):** an ontology of objects and links, and typed actions with permissions and submission criteria. Agents call those actions. They do not freely edit records. **Medium:** manufacturing case studies are workflow-shaped; the depth of closed-loop control is not fully public.

**Adapt:** a proposal is typed, and a gate decides whether it may be applied.  
**Reject:** ungated ontology actions, and owning routing, quality release, or maintenance authorization.

Sources: [ontology system](https://palantir.com/docs/foundry/architecture-center/ontology-system/), [action types](https://palantir.com/docs/foundry/action-types/overview/).

## Tulip — tools as the gate

**Paradigm (High):** an agent may only use the tables and connector functions it was given, and it cannot raise the caller’s permissions. Public docs describe builder evaluation tables. A plant-outcome learning loop is **not disclosed**.

**Adapt:** tools are an allowlist.  
**Reject:** giving the card agent open read-write on plant tables.

Source: [Tulip AI agents](https://support.tulip.co/docs/tulip-ai-agents).

## Braincube and Fero — recommend, and sometimes write a setpoint

**Braincube (Medium):** recommendations or steering from a product-centric model plus edge streams. Fine-grained write policy is thinner than Palantir or Tulip.  
**Fero (High):** recommendations can stay on a screen. Optional control writes stay inside engineer-set bounds. Outcome-labeled acceptance is **not disclosed** as a first-class object.

**Adapt:** human-default, with bounds.  
**Reject:** setpoint write as a Stamped action. Idle-load and equipment actions stay human-only.

Sources: [Braincube platform](https://braincube.com/platform/), [Fero live optimization](https://www.ferolabs.com/insights/post/faq-what-is-live-optimization).

## Augury, as a closure reference only

The public loop is a work order plus a later healthy-state check (**Medium**, partner material). **Reject** learning from a closed ticket that was never verified. Stamped’s eligible lesson is a verified signal or an explicit reason, not “the card was closed.”

## Hindsight — memory, not the company

[Hindsight](https://hindsight.vectorize.io/) is an agent memory system. **High**, from their docs:

- `retain` stores facts. `recall` searches. `reflect` reasons.
- Recall runs semantic, keyword, graph, and temporal search together (TEMPR).
- After retain, related facts consolidate into observations with quotes and a proof count. A contradiction updates the belief and keeps history. See [observations](https://hindsight.vectorize.io/developer/observations).
- A bank is a hard wall. One bank cannot see another. Tags only filter inside a bank, and a missed filter can leak. Their [bank guide](https://hindsight.vectorize.io/blog/2026/07/16/bank-strategy-agent-memory) says hard isolation belongs in separate banks.
- Directives are rules `reflect` must follow. They do not apply to `recall`.
- A conversation should be one document, updated with a stable document id ([retain](https://hindsight.vectorize.io/developer/api/retain)).

**Adopt:** one operational bank per plant; one dialogue bank per conversation; directives for the hard stops; observations built from short learning facts, not from stored cards.  
**Reject:** tagging chat inside the plant bank; retaining a full card body; letting an unverified close teach that an action worked. Hosting (their cloud or self-host) is an L4-repo choice, not this note.

## Noetive — whole-operation check, not their category

[Noetive](https://noetive.ai/) describes decisions made on the whole operation, working knowledge learned from how a business actually runs, and a loop where outcomes sharpen the next decision (**High**, their site). Investor descriptions add a digital twin, self-improving agents, and coordination across people and machines (**Medium**, secondary write-ups). Their own category language is an intelligence that runs the operation, paired with sensing pods.

**Adopt:** before one card is emitted, check upstream feed, downstream block, shared utilities, the shift, and open cards on related assets.  
**Reject:** sensing pods; any claim that Stamped runs the plant; full self-driving language; replanning the plant schedule. Those phrases are barred by [`10-stamped-vision-agent-alignment.md`](10-stamped-vision-agent-alignment.md).

## Layer map

- **L1.** Adopt read-only collect. Adapt a durable edge buffer and ISA-95 names. Reject OPC UA write and becoming the broker of record.
- **L2.** Adopt provenance on maps. Adapt thin context for one condition, plus constraint rows. Reject a full industrial graph.
- **L3.** Adopt deterministic detection before prose. Adapt domain tags and a verification plan on the finding. Reject promoting the lab to the floor.
- **L4.** Adopt the Hindsight plant bank, directives, and the cross-section check. Adapt typed reads and decision seams a later model may fill. Reject chat in the plant bank and any equipment write.
- **L5.** Adopt confirmation before a side effect. Adapt certified autonomy classes, default off. Reject setpoint or dispatch write.
- **L6.** Adopt one card and an honest close. Adapt Ask as a view over L4. Reject a second memory and a dashboard home.
