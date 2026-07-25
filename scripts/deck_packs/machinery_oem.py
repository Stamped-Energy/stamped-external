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
        "eyebrowD": "Packaging-machinery OEM · post-solar / post-VFD operating layer",
        "eyebrowM": "Machinery OEM · bill-verified decisions",
        "h1D": "Tape lines and test bays, priced onto the bill.",
        "h1M": "Machine-trial ₹ actions on the bill.",
        "ledeD": "After solar, VFDs, and compressor upgrades, the remaining value is assigned floor work in rupees, checked on the next DISCOM bill.",
        "ledeM": "Ranked actions after solar and VFDs. Verified on the DISCOM bill.",
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
    "whatLede": "Stamped sits on top of the meters and EMS you already run. It reads trial bays, utilities, and incomer data, issues a ranked action in rupees, sends it to the floor, and closes the result on the next bill.",
    "whatStep1": "Incomer, sub-meters, SCADA and PLC states for tape lines, looms, test bays, CNC, compressors, and chillers. Read-only. No control writes to the plant.",
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
            "title": "Idle CNC aux off when bay is dark",
            "why": "CNC chillers / aux left online across empty shifts",
            "impact": "₹0.4-0.8L/mo on energy",
            "owner": "Fab lead · B",
            "priority": "Med",
            "due": "Next empty bay window",
        },
    ],
    "verify": [
        ("MD stagger · trial/utility", "Sample MD peak", "10-min trial lag", "VERIFIED"),
        ("Night air unload cut", "Night unload kWh", "Bank B staging", "PENDING"),
        ("CNC idle aux off", "Empty-bay hours", "Aux shutdown SOP", "IN REVIEW"),
    ],
    "math": {
        "eyebrow": "Where packaging-machinery electricity cost usually hides",
        "h2": "Where we look first after solar and VFDs",
        "ledeD": "Avoidable ₹ on an HT bill once major capex is done, starting with these lines.",
        "ledeM": "Avoidable ₹ on the HT bill after solar and VFDs.",
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
                "Chiller drift",
                [
                    "Setpoint creep after VFD work",
                    "Parallel chiller starts",
                    "Cooling vs actual trial load",
                ],
                "Bill line · Energy (kWh)",
                "Sample hypothesis: chillers at full duty while trial load is light",
            ),
            (
                "Solar vs residual grid",
                [
                    "Self-consumption timing",
                    "Grid MD still exposed",
                    "Export / import mistiming",
                ],
                "Bill line · MD + ToD energy",
                "Sample hypothesis: solar cuts kWh while MD and night grid still move the bill",
            ),
        ],
    },
    "techBullet": "MD coincidence, compressed-air residual, idle CNC/aux, chiller drift, solar vs residual grid",
    "offerLedeD": "Start with one works. Connect read-only, run prescriptions on the floor, then go or no-go at Day 90: on verified ₹ and plant fit.",
    "offerLedeM": "One works. Connect → floor → go / no-go at Day 90.",
}

HERO = "assets/machinery-oem/tape-line.jpg"
HERO_ALT = "Tape extrusion line on a packaging-machinery manufacturing floor"
SLUG = "machinery-oem"
