"""Short, explicitly Lohia-branded meeting walkthrough for Vijay.

Fewer scenes than the full Proof Run. Names Lohia / Chaubepur on purpose.
"""

from __future__ import annotations

# Scenes kept from the shared base (order preserved)
KEEP_SCENES = [
    "scene-title",
    "scene-hook",
    "scene-math",
    "scene-what",
    "scene-prescription",
    "scene-floor",
    "scene-verify",
    # scene-vs-audit is injected by the client builder (not in the shared base)
    "scene-offer",
]

PACK = {
    "label": "Lohia Corp",
    "docTitle": "Stamped Energy · Lohia Corp walkthrough",
    "chromeHint": "Lohia Corp",
    "title": {
        "eyebrowD": "Lohia Corp · Chaubepur operating layer after solar and VFDs",
        "eyebrowM": "Lohia Corp · bill-verified next steps",
        "h1D": "Respect the capex. Own what still moves the bill.",
        "h1M": "Own what still moves the Lohia bill.",
        "ledeD": "You already did solar, VFDs, compressors, and chillers. Stamped assigns the next operating actions in rupees and checks them on the HT bill. Complements Lohia DIC. Does not replace it.",
        "ledeM": "After solar and VFDs: assigned ₹ actions, verified on the HT bill.",
    },
    "hook": {
        "eyebrow": "What Lohia already fixed",
        "h2": "Capex is done. Ownership of the residual is the gap.",
        "ledeD": "About 2.775 MWp solar and a reported ~17% grid reduction at the Kanpur works. Compressors, VFDs, chillers, and load alarms are in place. The open question is who owns the next bill line each month.",
        "ledeM": "Solar and VFDs are done. Who owns the next bill line?",
        "t1s": "Solar and efficiency capex already shipped",
        "t1p": "Rooftop solar plus compressor / VFD / chiller work is on record.",
        "t2s": "Visibility exists; assignment is thin",
        "t2p": "Load alarms and study reports log events. Floor work still needs an owner and a ₹ tag.",
        "t3s": "DIC stays. Stamped sits beside it",
        "t3p": "Read-only on meters you already have. Bill proof on MD, energy, and PF.",
        "meterNote": "We are not claiming prior projects failed. We close the residual operating gap.",
        "statImpact": "Gap",
        "statImpactLabel": "Ownership + ₹ + bill proof",
    },
    "gapHas": {
        "scada": "Has: line and utility run states",
        "ems": "Has: alarms and study history",
        "meters": "Has: MD window and load profile",
        "bill": "Has: MD, energy, PF line items",
    },
    "whatLede": "Stamped sits on top of the data Lohia already runs. Ranked actions in rupees, floor delivery, bill close-out. Complements DIC / SCADA visibility.",
    "whatStep1": "Chaubepur incomer, sub-meters, and existing SCADA / EMS tags. Read-only. No PLC writes. No hardware in Phase 1.",
    "rx1": {
        "badge": "Rx · MD coincidence",
        "aria": "Stagger machine trials and utility starts. Show evidence.",
        "action": "Stagger Chaubepur machine trials vs compressor / chiller start by 10 minutes",
        "why": "Trial and utility coincidence is a common MD driver after solar cuts kWh",
        "bill": "MD (kVA)",
        "owner": "Electrical POC · Chaubepur · Shift B",
        "impact": "Hypothesis · validate on two HT bills",
        "effort": "Sequence change · no new equipment",
        "rule": "md_overlap@v2.4 · High",
        "due": "First proof cycle",
        "evTitle": "Sample signal window · shift handover",
        "tags": [
            ("HT_INCOMER.MD", "Peak window", "handover"),
            ("TEST_BAY.TRIAL", "TRUE", "same window"),
            ("COMP_BANK.A", "ON", "same window"),
            ("CHILLER.START", "ON", "same window"),
        ],
        "cite": "physics/md_overlap@v2.4 · walkthrough hypothesis · confirm on Chaubepur bills",
    },
    "rx2": {
        "badge": "Rx · Compressed air",
        "aria": "Cut night unload baseload. Show evidence.",
        "action": "Stage plant-air unload offline in the planned night window",
        "why": "Residual air load after compressor upgrades often still hits night energy",
        "bill": "Energy (kWh) · night",
        "owner": "Utilities · Chaubepur",
        "impact": "Hypothesis · validate on energy line",
        "effort": "Staging SOP · no new equipment",
        "rule": "idle_hold@v1.8 · High",
        "due": "First proof cycle",
        "evTitle": "Night unload · sample pattern",
        "tags": [
            ("BANK_B.RUN", "ON · unload", "night"),
            ("FAB.PROD", "0 tags", "same window"),
            ("BANK_B.kWh", "Residual", "per event"),
            ("NIGHT.UNLOAD", "TRUE", "planned"),
        ],
        "cite": "physics/idle_hold@v1.8 · walkthrough hypothesis · confirm on energy line",
    },
    "floor": [
        {
            "title": "Stagger trials vs utility starts by 10 min",
            "why": "MD peak hypothesis at Chaubepur handover",
            "impact": "Validate on MD line",
            "owner": "Electrical POC · Chaubepur",
            "priority": "High",
            "due": "First proof cycle",
        },
        {
            "title": "Stage night air unload offline",
            "why": "Residual unload kWh after compressor program",
            "impact": "Validate on energy line",
            "owner": "Utilities · Chaubepur",
            "priority": "High",
            "due": "First proof cycle",
        },
        {
            "title": "Idle CNC aux off when bay is dark",
            "why": "Empty-bay holding loads still on grid",
            "impact": "Validate on energy line",
            "owner": "Fab lead · Chaubepur",
            "priority": "Med",
            "due": "First proof cycle",
        },
    ],
    "verify": [
        ("MD stagger · trial/utility", "Baseline MD", "10-min trial lag", "TO PROVE"),
        ("Night air unload cut", "Night kWh", "Bank staging", "TO PROVE"),
        ("CNC idle aux off", "Empty-bay hours", "Aux shutdown SOP", "TO PROVE"),
    ],
    "math": {
        "eyebrow": "Where ₹ may still hide at Lohia",
        "h2": "Discovery chips, not claims",
        "ledeD": "We will not invent a savings percent. These are the first places we check with your electrical team and two HT bills.",
        "ledeM": "Hypothesis chips. Confirm on Chaubepur bills.",
        "cards": [
            (
                "MD coincidence",
                [
                    "Machine trials + utilities",
                    "Tape-line and chiller overlap",
                    "Contract demand headroom",
                ],
                "Bill line · MD (kVA)",
                "Hypothesis: acceptance bay and plant air into the same MD window",
            ),
            (
                "Compressed air",
                [
                    "Night unload residual",
                    "Leak / load after upgrades",
                    "Bank start coincidence",
                ],
                "Bill line · Energy + MD",
                "Hypothesis: unload hours with no fab or trial tag",
            ),
            (
                "Idle CNC / test bay",
                [
                    "Empty bay chillers",
                    "Holding loads",
                    "Dark-shift aux run-on",
                ],
                "Bill line · Energy (kWh)",
                "Hypothesis: aux left online when the bay is empty",
            ),
            (
                "Chiller drift",
                [
                    "Setpoint creep",
                    "Parallel starts",
                    "Cooling vs trial load",
                ],
                "Bill line · Energy (kWh)",
                "Hypothesis: chillers at full duty on light trial load",
            ),
            (
                "Solar vs residual grid",
                [
                    "~17% grid cut is real",
                    "MD still on grid",
                    "Night / peak residual",
                ],
                "Bill line · MD + ToD",
                "Hypothesis: solar cut kWh; ownership of residual MD and night load is next",
            ),
        ],
    },
    "techBullet": "MD coincidence, compressed air, idle CNC, chiller drift, solar vs residual grid",
    "offerLedeD": "Chaubepur 90-day proof: electrical POC, two HT bills, one walkthrough. Read-only. Kill criteria agreed upfront.",
    "offerLedeM": "Chaubepur 90 days. POC + two HT bills + walkthrough.",
}

HERO = "assets/lohia-corp/tape-extrusion.jpg"
HERO_ALT = "Lohia Corp tape extrusion line"
SLUG = "lohia-corp-brief"

OFFER_PATCH = {
    "eyebrow": "Chaubepur · 90-day ask",
    "h2": "One works. One proof cycle.",
    "lede": "Not a second energy study. Electrical POC + two HT bills + a short floor walkthrough. Ranked actions with owners. Go / no-go on verified ₹.",
    "rows": [
        (
            "Week 0",
            "Name electrical POC · share two Chaubepur HT bills · walk the floor once",
        ),
        (
            "Days 1-30",
            "Read-only connect · turn meters + the IITK findings you already have into ranked prescriptions with owners",
        ),
        (
            "Days 31-90",
            "Floor executes weekly · potential vs realised on MD / energy / PF",
        ),
        (
            "Day 90",
            "Go / no-go on verified ₹ and fit. Kill if the math does not close.",
        ),
    ],
    "chips": [
        "Not another energy audit",
        "Uses the IITK study as input",
        "Complements Lohia DIC",
        "Read-only OT",
    ],
    "ask_title": "Ask for tomorrow",
    "ask_body": "Introduce the Chaubepur electrical POC and share two consecutive HT bills. We return a one-page proof plan with success criteria in ₹. We will not re-run the IIT Kanpur study.",
}

# Injected before scene-offer by build-client-decks.py
VS_AUDIT = {
    "eyebrow": "After the IIT Kanpur energy study",
    "h2": "A study finds opportunities. Stamped closes them on the bill.",
    "lede": "Lohia just completed an energy audit with IIT Kanpur. That work matters. Stamped is not a second audit. It is the operating layer that assigns owners, puts ₹ on each action, and checks the next HT bill.",
    "left_title": "Typical energy audit",
    "left": [
        "Periodic study and a findings report",
        "Recommendations without a weekly owner",
        "Ends when the report is delivered",
        "Rarely ties each action to an HT bill line",
        "Easy for the floor to treat as one more PDF",
    ],
    "right_title": "Stamped proof cycle",
    "right": [
        "Uses your IITK findings and live meters as input",
        "Every action: owner, due date, expected ₹",
        "Runs every week on the shift that can change it",
        "Potential vs realised on MD, energy, and PF",
        "Complements Lohia DIC. Does not replace the study",
    ],
    "note": "If the room only needs another diagnostic, stop here. If the gap is ownership and bill proof after the study, that is the 90-day ask.",
}
