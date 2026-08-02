"""Short, explicitly Lohia-branded meeting walkthrough for Vijay.

Fewer scenes than the full Proof Run. Names Lohia / Chaubepur on purpose.
Client-facing copy: professional, plain, not clever-AI tone.
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
        "eyebrowD": "Lohia Corp · Chaubepur operating energy",
        "eyebrowM": "Lohia Corp · Chaubepur",
        "h1D": "Operating ownership for the bill after solar and VFDs",
        "h1M": "Ownership for the remaining bill",
        "ledeD": "Lohia builds extrusion, winding, weaving, coating, and printing equipment for woven raffia, multifilament, monofilament, and recycling. Stamped turns live plant data into assigned rupee actions on those floors, with early warnings on the same lines, and checks results on the HT bill. It sits beside Lohia DIC; it does not replace it.",
        "ledeM": "Assigned rupee actions on your tape, loom, and coating floors, confirmed on the HT bill.",
    },
    "hook": {
        "eyebrow": "Work already completed",
        "h2": "Major efficiency projects are done. Day-to-day follow-through is still open.",
        "ledeD": "About 2.775 MWp solar and a reported ~17% grid reduction at your works. Compressors, VFDs, chillers, and load alarms are already running. What still matters each month is who owns the next change on extrusion, loom, and coating days.",
        "ledeM": "Solar and VFDs are in place. Who owns the next bill line?",
        "t1s": "Solar and efficiency projects completed",
        "t1p": "Rooftop solar plus compressor, VFD, and chiller work is on record.",
        "t2s": "Alarms exist; ownership is still thin",
        "t2p": "Load alarms and study reports record events. The floor still needs a named owner and a rupee impact.",
        "t3s": "DIC remains; Stamped sits beside it",
        "t3p": "Read-only on meters you already have. Proof on MD, energy, and PF.",
        "meterNote": "We are not saying prior projects failed. We close the remaining operating gap.",
        "statImpact": "Next",
        "statImpactLabel": "Owner, rupees, bill proof",
    },
    "gapHas": {
        "scada": "Has: extrusion, loom, coating run states",
        "ems": "Has: alarms and study history",
        "meters": "Has: MD window and line / utility profile",
        "bill": "Has: MD, energy, PF line items",
    },
    "whatLede": "Stamped uses the data Lohia already runs on tape lines, winders, circular looms, coating, and printing. It ranks actions in rupees, reaches the floor, and closes on the bill. Complements DIC.",
    "whatStep1": "Chaubepur incomer, sub-meters on extrusion, weaving, and coating islands, and existing SCADA or EMS tags. Read-only. No PLC writes. No new hardware in the first engagement.",
    "rx1": {
        "badge": "Rx · MD coincidence",
        "aria": "Stagger tape-line trials and utility starts. Show evidence.",
        "action": "Stagger tape-extrusion and machine-acceptance trials versus compressor and chiller start by 10 minutes",
        "why": "Trial bay load and plant air often share the same MD window at handover",
        "bill": "MD (kVA)",
        "owner": "Electrical POC · Chaubepur · Shift B",
        "impact": "To confirm on the MD line",
        "effort": "Sequence change · no new equipment",
        "rule": "md_overlap@v2.4 · High",
        "due": "During the plant visit / first cycle",
        "evTitle": "Example signal window · shift handover",
        "tags": [
            ("HT_INCOMER.MD", "Peak window", "handover"),
            ("TAPE_LINE.TRIAL", "TRUE", "same window"),
            ("COMP_BANK.A", "ON", "same window"),
            ("CHILLER.START", "ON", "same window"),
        ],
        "cite": "physics/md_overlap@v2.4 · example only · confirm on live Chaubepur data",
    },
    "rx2": {
        "badge": "Rx · Compressed air",
        "aria": "Cut night unload when looms and coaters are dark. Show evidence.",
        "action": "Stage plant-air unload offline when weaving, coating, or fab bays are dark",
        "why": "After compressor upgrades, residual air can still load the night bill with no loom or coater tag",
        "bill": "Energy (kWh) · night",
        "owner": "Utilities · Chaubepur",
        "impact": "To confirm on the energy line",
        "effort": "Staging SOP · no new equipment",
        "rule": "idle_hold@v1.8 · High",
        "due": "During the plant visit / first cycle",
        "evTitle": "Night unload · example pattern",
        "tags": [
            ("BANK_B.RUN", "ON · unload", "night"),
            ("LOOM.PROD", "0 tags", "same window"),
            ("COATER.RUN", "OFF", "same window"),
            ("NIGHT.UNLOAD", "TRUE", "planned"),
        ],
        "cite": "physics/idle_hold@v1.8 · example only · confirm on live plant data",
    },
    "floor": [
        {
            "title": "Stagger tape trials vs utility starts by 10 min",
            "why": "Possible MD peak at Chaubepur handover",
            "impact": "Confirm on MD line",
            "owner": "Electrical POC · Chaubepur",
            "priority": "High",
            "due": "First operating cycle",
        },
        {
            "title": "Stage night air when looms / coaters are dark",
            "why": "Unload kWh with no weaving or coating tag",
            "impact": "Confirm on energy line",
            "owner": "Utilities · Chaubepur",
            "priority": "High",
            "due": "First operating cycle",
        },
        {
            "title": "Idle CNC / fab aux off when bay is dark",
            "why": "Empty fab bay holding loads still on grid",
            "impact": "Confirm on energy line",
            "owner": "Fab lead · Chaubepur",
            "priority": "Med",
            "due": "First operating cycle",
        },
    ],
    "verify": [
        ("MD stagger · tape trial/utility", "Baseline MD", "10-min trial lag", "TO CONFIRM"),
        ("Night air · dark loom/coater", "Night kWh", "Bank staging", "TO CONFIRM"),
        ("Fab idle aux off", "Empty-bay hours", "Aux shutdown SOP", "TO CONFIRM"),
    ],
    "math": {
        "eyebrow": "Priority checks on Lohia floors",
        "h2": "First places we look on your lines",
        "ledeD": "These are working hypotheses for discussion with your electrical team across extrusion, winding, weaving, coating, and printing. We do not quote a savings percent until we see live plant data.",
        "ledeM": "Working hypotheses on your machine floors. Confirm with live data.",
        "cards": [
            (
                "Extrusion / MD",
                [
                    "Tape-line trials + utilities",
                    "Preheat / start coincidence",
                    "Contract demand headroom",
                ],
                "Bill line · MD (kVA)",
                "Example: tape acceptance and plant air in the same MD window",
            ),
            (
                "Weaving / coating",
                [
                    "Circular loom + utility overlap",
                    "Coater heat vs schedule gaps",
                    "Printing press idle hold",
                ],
                "Bill line · Energy + MD",
                "Example: loom or coater utilities running with no production tag",
            ),
            (
                "Winding / compressed air",
                [
                    "Winder bank air residual",
                    "Night unload after upgrades",
                    "Fab / pneumatics leaks",
                ],
                "Bill line · Energy (kWh)",
                "Example: air unload with winders and looms dark",
            ),
            (
                "Test bay / recycling",
                [
                    "Machine-acceptance idle",
                    "Recycling aux left online",
                    "Dark-shift holding loads",
                ],
                "Bill line · Energy (kWh)",
                "Example: trial and recycle aux left online when bays are empty",
            ),
            (
                "Early warnings",
                [
                    "Line-level drift before a trip",
                    "Utility / motor stress signals",
                    "Tied to your equipment, not a generic alarm list",
                ],
                "Operations and bill risk",
                "Example: flag loom, coater, or air trouble before a breakdown or MD event",
            ),
        ],
    },
    "techBullet": "MD on tape lines, loom and coater idle, winding air, early warnings, live floor decisions",
    "offerLedeD": "With plant access at Chaubepur, we visit, connect read-only, show the workspace on your lines, and begin from live plant data.",
    "offerLedeM": "Plant visit, on-site connect, live decisions on your lines.",
}

HERO = "assets/lohia-corp/tape-extrusion.jpg"
HERO_ALT = "Lohia Corp tape extrusion line"
SLUG = "lohia-corp-brief"

OFFER_PATCH = {
    "eyebrow": "Proposed next step · Chaubepur",
    "h2": "Start at one works",
    "lede": "We are not asking for a second energy audit, and we are not asking for bills before we meet. If you allow a plant visit at Chaubepur, we walk the floors, review what you already know from prior audits, connect read-only, and show the workspace on site before the engagement continues.",
    "rows": [
        (
            "Access",
            "Nominate a plant host · visit Chaubepur (extrusion, weaving, coating)",
        ),
        (
            "On site",
            "Review lines, utilities, and prior audit findings · no second study report",
        ),
        (
            "Connect and demo",
            "Read-only meters and EMS · on-floor walkthrough of the workspace on your data",
        ),
        (
            "Operate",
            "Live prescriptions and early warnings from current plant conditions · bill proof as actions land",
        ),
    ],
    "chips": [
        "Plant visit",
        "Live decisions",
        "Early warnings on your lines",
        "Works with Lohia DIC",
    ],
    "ask_title": "What we need from you",
    "ask_body": "Permission to visit Chaubepur with your electrical or utilities host. We will not treat two HT bills as an entry ticket. We connect on site, show how Stamped looks on your lines, and work from live plant data.",
}

# Injected after scene-hook by build-client-decks.py
LOHIA_LINES = {
    "eyebrow": "Lohia Corp equipment and processes",
    "h2": "How this maps to your product lines",
    "lede": "Your businesses cover woven raffia, multifilament, monofilament, and recycling. On the shop floor that means extrusion, winding, weaving, coating, and printing. Stamped focuses on energy decisions and early warnings on those same lines.",
    "families_title": "Product families",
    "families": [
        "Woven raffia / Packtex lines",
        "Multifilament spin-draw",
        "Monofilament",
        "Recycling equipment",
    ],
    "tech_title": "Where we add operating value",
    "tech": [
        ("Extrusion", "Tape-line starts, trial MD, preheat overlap with utilities"),
        ("Winding", "Winder banks and plant air when tape is not moving"),
        ("Weaving", "Circular loom coincidence with chillers and compressors"),
        ("Coating", "Extrusion-coating heat and idle hold between jobs"),
        ("Printing", "Press and dryer hold when the substrate line is down"),
        (
            "Early warnings",
            "Signals on your lines that flag machine or utility trouble before a breakdown",
        ),
    ],
    "note": "We do not redesign your machines. We help your team act on energy and early-warning signals while those machines are running, then check the result on the HT bill.",
}

# Injected before scene-offer by build-client-decks.py
VS_AUDIT = {
    "eyebrow": "Energy audit and Stamped",
    "h2": "How an energy study differs from ongoing operating support",
    "lede": "An energy audit is useful as a snapshot. Stamped is built for what happens next: live ranked actions with owners, early warnings on your lines, and proof on the HT bill as those actions land.",
    "left_title": "Typical energy audit",
    "left": [
        "Periodic study and a findings report",
        "Recommendations without a standing owner",
        "Ends when the report is delivered",
        "Limited early warning before equipment or utility failure",
        "Easy for the floor to treat as another document",
    ],
    "right_title": "Stamped at your works",
    "right": [
        "Live prescriptions from meters and line states",
        "Each action has an owner, due time, and expected rupees",
        "Early warnings tied to extrusion, looms, coaters, and utilities",
        "Problems flagged before they become breakdowns or MD spikes",
        "Works with Lohia DIC; does not replace your EMS",
    ],
    "note": "If you only need another diagnostic report, stop here. If you want decisions while the plant is running, that is what the plant visit is for.",
}

# Soften shared base headings that remain in the brief
BRIEF_HEADING_PATCHES = [
    (
        '<p class="eyebrow reveal">What Stamped does</p>\n'
        '        <h2 class="reveal">Signals become work orders.</h2>',
        '<p class="eyebrow reveal">How Stamped works</p>\n'
        '        <h2 class="reveal">From plant data to assigned work</h2>',
    ),
    (
        '<p class="eyebrow reveal">Sample prescriptions</p>\n'
        '        <h2 class="reveal">Every action has a bill line and an owner.</h2>',
        '<p class="eyebrow reveal">Example prescriptions</p>\n'
        '        <h2 class="reveal">Each action has a bill line and an owner</h2>',
    ),
    (
        '<p class="eyebrow reveal hide-mobile">Floor channel</p>\n'
        '            <p class="eyebrow reveal show-mobile">On the floor</p>\n'
        '            <h2 class="reveal">On the supervisor\'s phone.</h2>',
        '<p class="eyebrow reveal hide-mobile">Floor delivery</p>\n'
        '            <p class="eyebrow reveal show-mobile">On the floor</p>\n'
        '            <h2 class="reveal">Reached on the supervisor\'s phone</h2>',
    ),
    (
        '<p class="eyebrow reveal">Measurement and verification</p>\n'
        '        <h2 class="reveal">Verified with evidence.</h2>',
        '<p class="eyebrow reveal">Measurement and verification</p>\n'
        '        <h2 class="reveal">Verified with evidence</h2>',
    ),
]
