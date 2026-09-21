# Tech OVN vs Stamped — plain English

## In one sentence
Tech OVN (Gurugram) manufactures **Titan** smart meters in India and sells a cloud **Energy Intelligence Platform (EIP)** so factories and buildings can see circuit-level kWh, alerts, and PAT/ISO-ready reports — meters and dashboard as one stack.

## What they actually do (no jargon)
- Design and build **Class 0.5S** three-phase DIN-rail meters (utility-grade accuracy) with WiFi, Ethernet, and RS485; speak Modbus and MQTT at once; no extra gateway to their cloud.
- Sell **Titan Audit** — clamp-on portable loggers for energy audits with phone PDF reports, then leave meters in place for ongoing measurement.
- Cloud SaaS dashboards: multi-site view, sub-metering by line/floor/tenant/machine, demand and Power Factor alerts, tariff/cost allocation, anomaly flags.
- Factory pitch: attribute kWh to line / shift / machine; compute **Specific Energy Consumption (SEC)** and **EnPI** (energy performance indicators); export BEE **PAT** / ISO 50001 / BRSR-style reports.
- SEC can start with **manual or CSV production totals** — they say you do not need full MES to get SEC working.
- Runs **beside** BMS/SCADA; does not replace plant control. Limited meter relay “disconnect on threshold” — not a plant optimiser.
- Also sell into hospitals, data centres, hotels, commercial buildings — broader than HT manufacturing alone. White-label meter programme for partners.

## What Stamped already does in the same area
- We already ingest Modbus/MQTT (and more), multi-site style plant data, and raise MD/PF/ToD/idle/compressor Findings.
- We already turn those into ₹ Prescriptions with owners — not just charts and alerts.
- We already have SEC/EnPI paths and compressor / HVAC / motor waste rules in catalog.
- We already sit beside customer SCADA/EMS as a software overlay.
- We already specify PAT/ISO/BRSR as **evidence enable/export**, not filing.
- We explicitly are **not** a meter manufacturer or hardware retrofit programme.

## What they can do that we cannot (the real gaps)

### Own Class 0.5S smart meter product line (Titan)
- **What it is:** India-made DIN-rail meter with harmonics, up to eight Time-of-Day zones, dual grid/DG, on-device CO₂, MQTT-native.
- **Why a plant would care:** Greenfield or ESCO deals often want “buy meters + cloud” as one purchase order.
- **Software, hardware, or both?** Hardware.
- **Can Stamped add this?** No — strategic non-goal; we stay meter-agnostic.
- **Should we?** No. Partner Titan (or any Class 0.5S) and ingest their streams.

### Titan Audit clamp-on logger + phone audit PDF
- **What it is:** Fast, no-shutdown survey kit that becomes ongoing monitoring.
- **Why a plant would care:** Energy auditors and ESCOs need a wedge before permanent install.
- **Software, hardware, or both?** Hardware + app.
- **Can Stamped add this?** Yes with partners — ingest leave-in-place data via existing connectors.
- **Should we?** Partner auditors/ESCOs; do not build logger hardware.

### Meter → cloud with no gateway box
- **What it is:** Each Titan talks MQTT straight to EIP over WiFi/Ethernet.
- **Why a plant would care:** Simpler bill of materials and fewer failure points for basic monitoring.
- **Software, hardware, or both?** Both (their meter design).
- **Can Stamped add this?** No as our hardware; Yes software already — once any meter speaks Modbus/MQTT/REST we ingest.
- **Should we?** Irrelevant to copy; keep edge normaliser for messy brownfield.

### On-meter relay / power disconnection on thresholds
- **What it is:** Meter can alert and cut power when limits trip.
- **Why a plant would care:** Local protection / load trip without waiting for a cloud app.
- **Software, hardware, or both?** Hardware.
- **Can Stamped add this?** No — autonomous OT write is a hard non-goal.
- **Should we?** No; partner meter OEM if a site needs it.

### Packaged PAT / ISO 50001 / BRSR exports next to meters
- **What it is:** Audit-ready PDF/Excel from the same SKU as the hardware.
- **Why a plant would care:** Compliance checkbox sells with the meters.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** Yes software — deepen evidence exports; stay enable-not-file.
- **Should we?** Yes (shared with VolTwin-driven backlog).

### Buildings / hospitals / data-centre multi-tenant EMS SKU
- **What it is:** Same platform sold as tenant chargeback, PUE, OT/ICU monitoring, etc.
- **Why a plant would care:** Portfolio buyers outside manufacturing.
- **Software, hardware, or both?** Software.
- **Can Stamped add this?** Unclear / dilutive — not our ICP.
- **Should we?** No as core roadmap; park unless a deal pulls.

## Bottom line for Stamped
Tech OVN is a **hardware-led adjacent niche**, not a peer Prescription product. They win “Class 0.5S meters + cloud charts.” We win when meters (any brand) already exist and the plant needs India HT Findings → ₹ Prescriptions → closure. Do not become a meter OEM. Partner Titan/Audit channels; polish compliance evidence exports in software. Ignore their 5–15% industry-study marketing as our proof.
