"""Short, explicitly Lohia-branded meeting walkthrough for Vijay.

Fewer scenes than the full Proof Run. Names Lohia / Chaubepur on purpose.
"""

from __future__ import annotations

# Scenes kept from the shared base (order preserved)
KEEP_SCENES = [
    "scene-title",
    "scene-hook",
    # scene-lohia-lines injected after hook by the client builder
    "scene-math",
    "scene-what",
    "scene-prescription",
    "scene-floor",
    "scene-verify",
    # scene-vs-audit injected before offer by the client builder
    "scene-offer",
]

PACK = {
    "label": "Lohia Corp",
    "docTitle": "Stamped Energy · Lohia Corp walkthrough",
    "chromeHint": "Lohia Corp",
    "title": {
        "eyebrowD": "Lohia Corp · woven raffia machinery works after solar and VFDs",
        "eyebrowM": "Lohia Corp · bill-verified next steps",
        "h1D": "Respect the capex. Own what still moves the bill.",
        "h1M": "Own what still moves the Lohia bill.",
        "ledeD": "You build extrusion, winding, weaving, coating, and printing lines for woven raffia, multifilament, monofilament, and recycling. Stamped assigns the next operating actions on that floor in rupees and checks them on the HT bill. Complements Lohia DIC.",
        "ledeM": "On your tape, loom, and coating floors: assigned ₹ actions on the HT bill.",
    },
    "hook": {
        "eyebrow": "What Lohia already fixed",
        "h2": "Capex is done. Ownership of the residual is the gap.",
        "ledeD": "About 2.775 MWp solar and a reported ~17% grid reduction at your works. Compressors, VFDs, chillers, and load alarms are in place. The open question is who owns the next bill line each month on extrusion, loom, and coating days.",
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
        "scada": "Has: extrusion, loom, coating run states",
        "ems": "Has: alarms and study history",
        "meters": "Has: MD window and line / utility profile",
        "bill": "Has: MD, energy, PF line items",
    },
    "whatLede": "Stamped sits on top of the data Lohia already runs across tape lines, winders, circular looms, coating, and printing. Ranked actions in rupees, floor delivery, bill close-out. Complements DIC.",
    "whatStep1": "Chaubepur incomer, sub-meters on extrusion / weaving / coating islands, and existing SCADA / EMS tags. Read-only. No PLC writes. No hardware in Phase 1.",
    "rx1": {
        "badge": "Rx · MD coincidence",
        "aria": "Stagger tape-line trials and utility starts. Show evidence.",
        "action": "Stagger tape-extrusion / machine-acceptance trials vs compressor and chiller start by 10 minutes",
        "why": "Trial bay load and plant air often hit the same MD window on handover",
        "bill": "MD (kVA)",
        "owner": "Electrical POC · Chaubepur · Shift B",
        "impact": "Hypothesis · prove on MD line",
        "effort": "Sequence change · no new equipment",
        "rule": "md_overlap@v2.4 · High",
        "due": "While we are on-site / first cycle",
        "evTitle": "Sample signal window · shift handover",
        "tags": [
            ("HT_INCOMER.MD", "Peak window", "handover"),
            ("TAPE_LINE.TRIAL", "TRUE", "same window"),
            ("COMP_BANK.A", "ON", "same window"),
            ("CHILLER.START", "ON", "same window"),
        ],
        "cite": "physics/md_overlap@v2.4 · walkthrough hypothesis · confirm on live Chaubepur data",
    },
    "rx2": {
        "badge": "Rx · Compressed air",
        "aria": "Cut night unload when looms and coaters are dark. Show evidence.",
        "action": "Stage plant-air unload offline when weaving / coating / fab bays are dark",
        "why": "Residual air after compressor upgrades still hits night energy with no loom or coater tag",
        "bill": "Energy (kWh) · night",
        "owner": "Utilities · Chaubepur",
        "impact": "Hypothesis · prove on energy line",
        "effort": "Staging SOP · no new equipment",
        "rule": "idle_hold@v1.8 · High",
        "due": "While we are on-site / first cycle",
        "evTitle": "Night unload · sample pattern",
        "tags": [
            ("BANK_B.RUN", "ON · unload", "night"),
            ("LOOM.PROD", "0 tags", "same window"),
            ("COATER.RUN", "OFF", "same window"),
            ("NIGHT.UNLOAD", "TRUE", "planned"),
        ],
        "cite": "physics/idle_hold@v1.8 · walkthrough hypothesis · confirm on live plant data",
    },
    "floor": [
        {
            "title": "Stagger tape trials vs utility starts by 10 min",
            "why": "MD peak hypothesis at Chaubepur handover",
            "impact": "Validate on MD line",
            "owner": "Electrical POC · Chaubepur",
            "priority": "High",
            "due": "First proof cycle",
        },
        {
            "title": "Stage night air when looms / coaters are dark",
            "why": "Unload kWh with no weaving or coating tag",
            "impact": "Validate on energy line",
            "owner": "Utilities · Chaubepur",
            "priority": "High",
            "due": "First proof cycle",
        },
        {
            "title": "Idle CNC / fab aux off when bay is dark",
            "why": "Empty fab bay holding loads still on grid",
            "impact": "Validate on energy line",
            "owner": "Fab lead · Chaubepur",
            "priority": "Med",
            "due": "First proof cycle",
        },
    ],
    "verify": [
        ("MD stagger · tape trial/utility", "Baseline MD", "10-min trial lag", "TO PROVE"),
        ("Night air · dark loom/coater", "Night kWh", "Bank staging", "TO PROVE"),
        ("Fab idle aux off", "Empty-bay hours", "Aux shutdown SOP", "TO PROVE"),
    ],
    "math": {
        "eyebrow": "Where ₹ may still hide on Lohia floors",
        "h2": "Tied to your lines, not a generic plant",
        "ledeD": "Hypothesis chips only. We confirm with your electrical team and two HT bills across extrusion, winding, weaving, coating, and printing.",
        "ledeM": "Hypothesis chips on your machine floors. Confirm on bills.",
        "cards": [
            (
                "Extrusion / MD",
                [
                    "Tape-line trials + utilities",
                    "Preheat / start coincidence",
                    "Contract demand headroom",
                ],
                "Bill line · MD (kVA)",
                "Hypothesis: tape acceptance and plant air into the same MD window",
            ),
            (
                "Weaving / coating",
                [
                    "Circular loom + utility overlap",
                    "Coater heat vs schedule gaps",
                    "Printing press idle hold",
                ],
                "Bill line · Energy + MD",
                "Hypothesis: loom or coater utilities running with no production tag",
            ),
            (
                "Winding / compressed air",
                [
                    "Winder bank air residual",
                    "Night unload after upgrades",
                    "Fab / pneumatics leaks",
                ],
                "Bill line · Energy (kWh)",
                "Hypothesis: air unload with winders and looms dark",
            ),
            (
                "Test bay / recycling",
                [
                    "Machine-acceptance idle",
                    "ReclaPro / recycle aux run-on",
                    "Dark-shift holding loads",
                ],
                "Bill line · Energy (kWh)",
                "Hypothesis: trial and recycle aux left online when bays are empty",
            ),
            (
                "Early warnings",
                [
                    "Line-tied drift before a trip",
                    "Utility / motor stress signals",
                    "Not a generic plant alarm dump",
                ],
                "Ops + bill risk",
                "Hypothesis: catch loom, coater, or air trouble before a breakdown or MD event",
            ),
        ],
    },
    "techBullet": "Tape extrusion MD, loom/coater idle, winding air, early warnings, real-time decisions",
    "offerLedeD": "Give us plant access at Chaubepur. We come on-site, connect read-only, show the live workspace on your lines, and start prescribing from real-time plant data.",
    "offerLedeM": "Plant access. On-site connect. Real-time decisions on your lines.",
}

HERO = "assets/lohia-corp/tape-extrusion.jpg"
HERO_ALT = "Lohia Corp tape extrusion line"
SLUG = "lohia-corp-brief"

OFFER_PATCH = {
    "eyebrow": "Chaubepur · one works ask",
    "h2": "One works. One proof cycle.",
    "lede": "Not another energy audit and not a homework list of bills up front. Give us permission to come to Chaubepur. We walk your floors, sit with what you already audited, connect read-only, and show you the live workspace on-site before the pilot starts.",
    "rows": [
        (
            "Permission",
            "Name a plant host · we come to Chaubepur (extrusion, weaving, coating)",
        ),
        (
            "On-site",
            "Understand your lines, utilities, and prior audit findings · no second study report",
        ),
        (
            "Connect + demo",
            "Read-only meters / EMS · offline / on-floor demo of the live workspace on your data",
        ),
        (
            "Start",
            "Real-time prescriptions and early warnings from what the plant is doing now · bill proof as actions land",
        ),
    ],
    "chips": [
        "Come to the plant",
        "Real-time decisions",
        "Early warnings on your lines",
        "Complements Lohia DIC",
    ],
    "ask_title": "Ask for tomorrow",
    "ask_body": "Give us permission to visit Chaubepur with your electrical / utilities host. We will not ask for two HT bills as a gate. We connect on-site, show how Stamped looks on your lines, and start from live plant data.",
}

# Injected after scene-hook by build-client-decks.py
LOHIA_LINES = {
    "eyebrow": "Lohia Corp · your product lines",
    "h2": "Built for the machines you make.",
    "lede": "Woven raffia, multifilament, monofilament, and recycling are the businesses. Extrusion, winding, weaving, coating, and printing are the floors. Stamped makes energy waste on those floors owned, priced, and checked on the bill.",
    "families_title": "Product families",
    "families": [
        "Woven raffia / Packtex lines",
        "Multifilament spin-draw",
        "Monofilament",
        "Recycling (ReclaPro-class)",
    ],
    "tech_title": "Where Stamped helps on your tech",
    "tech": [
        ("Extrusion", "Tape-line starts, trial MD, preheat overlap vs utilities"),
        ("Winding", "Winder banks and plant air when tape is not moving"),
        ("Weaving", "Circular loom coincidence with chillers and compressors"),
        ("Coating", "Extrusion-coating heat and idle hold between jobs"),
        ("Printing", "Press and dryer hold when the substrate line is down"),
        (
            "Early warnings",
            "Line-tied signals that flag machine / utility trouble before a breakdown, not a generic plant alarm dump",
        ),
    ],
    "note": "We do not redesign your machines. We assign the next real-time operating decision on the works that builds and proves them, and surface early warnings tied to those lines.",
}

# Injected before scene-offer by build-client-decks.py
VS_AUDIT = {
    "eyebrow": "Energy audit vs Stamped",
    "h2": "An audit hands you a report. Stamped hands the floor a live decision.",
    "lede": "A generic energy audit is a snapshot with a PDF. Stamped runs on what your plant is doing now: real-time ranked actions, owners, and early warnings on your lines, then proof on the HT bill as those actions land.",
    "left_title": "Generic energy audit",
    "left": [
        "One-time study and a findings PDF",
        "Recommendations without a live owner",
        "Stops when the report is delivered",
        "Little early warning before a machine or utility fails",
        "Floor treats it as one more document",
    ],
    "right_title": "Stamped for your plant",
    "right": [
        "Real-time prescriptions from live meters and line states",
        "Every action: owner, due date, expected ₹",
        "Early warnings tied to extrusion, looms, coaters, and utilities",
        "Catch problems before they become breakdowns or MD spikes",
        "Complements Lohia DIC. Does not replace your EMS",
    ],
    "note": "If you only need another diagnostic PDF, you do not need us. If you want decisions while the plant is running, that is the on-site ask.",
}
