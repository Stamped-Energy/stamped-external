"""Anonymous packaging-machinery OEM Proof Run pack.

Hard gate: no Lohia / Chaubepur / Vijay / plant-city naming in any string.
Sample ₹ figures are walkthrough hypotheses, not client claims.
"""

from __future__ import annotations

PACK = {
    "label": "Machinery OEM",
    "docTitle": "Stamped Energy · Packaging machinery OEM demo",
    "chromeHint": "Machinery OEM",
    "title": {
        "eyebrowD": "Packaging-machinery OEM · real-time decisions after solar and VFDs",
        "eyebrowM": "Machinery OEM · real-time ₹ decisions",
        "h1D": "Tape lines and test bays, priced onto the bill.",
        "h1M": "Machine-trial ₹ actions on the bill.",
        "ledeD": "After solar, VFDs, and compressor upgrades, the remaining value is real-time floor decisions in rupees, line-tied early warnings, and proof on the next DISCOM bill. A 60-day Proof Run when you want a scoped pilot.",
        "ledeM": "Real-time actions and early warnings after solar and VFDs. 60-day Proof Run as needed.",
    },
    "hook": {
        "eyebrow": "Monday 06:50 · Machine acceptance / utilities handover",
        "h2": "Your plant already logs this. Nobody owns the fix.",
        "ledeD": "Test bay and utility banks overlapped. EMS logged it. No work order went out.",
        "ledeM": "Test bay and utilities overlapped. No work order went out.",
        "t1s": "Machine trial and compressor bank start together",
        "t1p": "Shift B brings test bay load and plant air online in the same window.",
        "t2s": "MD spike hits the incomer",
        "t2p": "EMS threshold crossed. Alert created. Still no assigned owner.",
        "t3s": "Trials and fab continue as usual",
        "t3p": "The bill will price this later. The floor never saw the fix.",
        "meterNote": "The EMS recorded the spike, but nobody was assigned to change the next trial / utility sequence.",
        "statImpact": "₹45k",
        "statImpactLabel": "Monthly demand impact (sample)",
    },
    "gapHas": {
        "scada": "Has: tape line, loom, test-bay run states",
        "ems": "Has: spike logged at 06:50",
        "meters": "Has: MD window and trial / utility load profile",
        "bill": "Has: MD, energy, PF line items",
    },
    "whatLede": "Stamped sits on top of the meters and EMS you already run. It reads trial bays, utilities, and incomer data in real time, issues a ranked action in rupees, sends early warnings tied to those lines, and closes the result on the next bill.",
    "whatStep1": "Incomer, sub-meters, SCADA and PLC states for tape lines, looms, test bays, CNC, compressors, and chillers. Read-only. Real-time decisions and line-tied early warnings. No control writes to the plant.",
    "rx1": {
        "badge": "Rx · MD coincidence",
        "aria": "Stagger machine trials and utility starts. Show evidence.",
        "action": "Stagger machine-acceptance trials vs compressor / chiller start by 10 minutes",
        "why": "They started together and pushed MD over the limit",
        "bill": "MD (kVA)",
        "owner": "Electrical shift supervisor · Shift B",
        "impact": "₹2-3.5L / month",
        "effort": "Sequence change · no new equipment",
        "rule": "md_overlap@v2.4 · High",
        "due": "This week",
        "evTitle": "Signal window · Mon 06:45-07:00",
        "tags": [
            ("HT_INCOMER.MD", "1,050 kVA", "06:52-06:56"),
            ("TEST_BAY.TRIAL", "TRUE", "06:48"),
            ("COMP_BANK.A", "ON", "06:50+"),
            ("CHILLER.START", "ON", "06:51+"),
        ],
        "cite": "physics/md_overlap@v2.4 · model conf 0.90 · tariff MD slab · baseline sample peak week",
    },
    "rx2": {
        "badge": "Rx · Compressed air",
        "aria": "Cut night unload baseload on plant air. Show evidence.",
        "action": "Stage Compressor Bank B offline in the planned night unload window",
        "why": "Unload kWh with no trial or fab tag on 3 of last 5 nights",
        "bill": "Energy (kWh) · night",
        "owner": "Utilities supervisor · Plant air",
        "impact": "₹70k-1.2L / month",
        "effort": "Staging SOP · no new equipment",
        "rule": "idle_hold@v1.8 · High",
        "due": "Next night unload",
        "evTitle": "Night unload windows · last 5 events",
        "tags": [
            ("BANK_B.RUN", "ON · unload", "95 min avg"),
            ("FAB.PROD", "0 tags", "same window"),
            ("BANK_B.kWh", "185 kWh", "per event"),
            ("NIGHT.UNLOAD", "TRUE", "planned"),
        ],
        "cite": "physics/idle_hold@v1.8 · model conf 0.86 · energy line · baseline last 5 nights",
    },
    "floor": [
        {
            "title": "Stagger trials vs utility starts by 10 min",
            "why": "MD peak from Monday trial / air overlap",
            "impact": "₹2-3.5L/mo on MD line",
            "owner": "Electrical supervisor · B",
            "priority": "High",
            "due": "This week · before next peak",
        },
        {
            "title": "Stage Bank B offline in night unload",
            "why": "Unload kWh with no fab or trial tag",
            "impact": "₹0.7-1.2L/mo on energy",
            "owner": "Utilities supervisor · A",
            "priority": "High",
            "due": "Next night unload",
        },
        {
            "title": "Act on early warning · tape-line motor stress",
            "why": "Line-tied drift signal before a trial bay trip",
            "impact": "Avoid unplanned downtime + MD risk",
            "owner": "Electrical supervisor · B",
            "priority": "Med",
            "due": "Same shift · before next trial",
        },
    ],
    "verify": [
        ("MD stagger · trial/utility", "Sample MD peak", "10-min trial lag", "VERIFIED"),
        ("Night air unload cut", "Night unload kWh", "Bank B staging", "PENDING"),
        ("Early warning · line stress", "Pre-trip drift window", "Same-shift action", "IN REVIEW"),
    ],
    "math": {
        "eyebrow": "Where packaging-machinery electricity cost usually hides",
        "h2": "Real-time looks on your lines after solar and VFDs",
        "ledeD": "Avoidable ₹ and early risk once major capex is done. We watch what the plant is doing now, not a quarterly PDF.",
        "ledeM": "Real-time ₹ and early warnings on your lines.",
        "cards": [
            (
                "MD / demand",
                [
                    "Machine trials + utility coincidence",
                    "Tape-line and chiller overlap",
                    "Contract demand headroom",
                ],
                "Bill line · MD (kVA)",
                "Sample hypothesis: acceptance bay and compressor bank into the same MD window",
            ),
            (
                "Compressed air",
                [
                    "Night unload baseload",
                    "Leak / load residual after upgrades",
                    "Simultaneous bank starts",
                ],
                "Bill line · Energy + MD",
                "Sample hypothesis: Bank B unload with zero fab or trial tags",
            ),
            (
                "Idle CNC / aux",
                [
                    "Empty bay chillers",
                    "Test-bay holding loads",
                    "Aux run-on across dark shifts",
                ],
                "Bill line · Energy (kWh)",
                "Sample hypothesis: CNC aux left online when the bay is empty",
            ),
            (
                "Early warnings",
                [
                    "Line-tied drift before a trip",
                    "Motor / utility stress on tape or loom islands",
                    "Not a generic plant alarm dump",
                ],
                "Ops + bill risk",
                "Sample hypothesis: catch trial-bay or air trouble before a breakdown or MD event",
            ),
            (
                "Real-time decisions",
                [
                    "Ranked ₹ actions while the shift is live",
                    "Owner and due time on WhatsApp",
                    "60-day Proof Run when you want a scoped pilot",
                ],
                "Bill line · MD + energy",
                "Sample hypothesis: close the loop in the week, not after the next audit cycle",
            ),
        ],
    },
    "techBullet": "Real-time MD and idle actions, line-tied early warnings, compressed-air residual, 60-day Proof Run as needed",
    "offerLedeD": "Start with one works. Real-time prescriptions and line-tied early warnings from live meters. A 60-day Proof Run when you want a scoped go / no-go on verified ₹ and plant fit.",
    "offerLedeM": "One works. Real-time decisions + early warnings. 60-day Proof Run as needed.",
}

HERO = "assets/machinery-oem/tape-line.jpg"
HERO_ALT = "Tape extrusion line on a packaging-machinery manufacturing floor"
SLUG = "machinery-oem"
