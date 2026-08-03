"""Anonymous forge / die-cast / heat-treatment Proof Run pack (from steel).

Value-first walkthrough for plants with forging, die casting, and heat treatment
under one roof. No named-account branding. Sample rupee figures are illustrative.
"""

from __future__ import annotations

# Scenes kept from the shared base (order preserved). Two-pillars injected after hook.
KEEP_SCENES = [
    "scene-title",
    "scene-hook",
    "scene-math",
    "scene-what",
    "scene-prescription",
    "scene-floor",
    "scene-verify",
    "scene-offer",
]

PACK = {
    "label": "Forge · HT · Die cast",
    "docTitle": "Stamped Energy · Forge and heat-treatment demo",
    "chromeHint": "Forge · HT",
    "title": {
        "eyebrowD": "Forging, die casting, heat treatment · verified with evidence",
        "eyebrowM": "Forge · HT · die cast · verified with evidence",
        "h1D": "From plant data to assigned actions",
        "h1M": "Assigned actions. Verified with evidence.",
        "ledeD": "On floors that run presses, furnaces, and die-casting cells together, Stamped ranks energy and equipment work in rupees, assigns an owner, and checks the outcome with evidence. DISCOM bill confirmation can follow.",
        "ledeM": "Energy and equipment prescriptions on forge and HT floors. Verified with evidence.",
    },
    "hook": {
        "eyebrow": "Monday 06:48 · Forge / heat-treatment handover",
        "h2": "The plant logged the overlap. Nobody owned the fix.",
        "ledeD": "Press start and furnace preheat stacked in the same MD window. EMS recorded it. No work order went out.",
        "ledeM": "Press and furnace overlapped. No work order went out.",
        "t1s": "Press ramp and furnace preheat overlap",
        "t1p": "Day shift brings forging and heat treatment online in the same window.",
        "t2s": "MD spike hits the incomer",
        "t2p": "Threshold crossed. Alert created. Still no assigned owner.",
        "t3s": "Batches and presses continue as usual",
        "t3p": "The bill prices it later. The floor never saw the fix.",
        "meterNote": "Meters and EMS saw the spike. The missing piece is a named action with a rupee impact.",
        "statImpact": "₹42k",
        "statImpactLabel": "Monthly demand impact (sample)",
    },
    "gapHas": {
        "scada": "Has: press, furnace, die-cast run states",
        "ems": "Has: spike logged at 06:48",
        "meters": "Has: MD window and forge / HT load profile",
        "bill": "Has: MD, energy, PF line items",
    },
    "whatLede": "Stamped sits on meters and plant data you already have. It ranks energy and equipment actions in rupees, reaches the floor on WhatsApp, verifies with evidence, and improves from what was followed versus ignored.",
    "whatStep1": "Incomer and feeder meters, furnace / press / die-cast states where available, and bill lines. Optional production or ERP schedule read. Read-only. No control writes.",
    "rx1": {
        "badge": "Rx · Energy · MD",
        "aria": "Stagger press and furnace preheat. Show evidence.",
        "action": "Stagger Press Line 1 start versus SQF furnace preheat by 10-12 minutes at day-shift start",
        "why": "They started together and pushed the incomer MD window",
        "bill": "MD (kVA)",
        "owner": "Electrical shift supervisor · Shift B",
        "impact": "₹0.8-1.2L / month (example)",
        "effort": "Sequence change · no new equipment",
        "rule": "md_overlap@v2.4 · High",
        "due": "This week",
        "evTitle": "Signal window · Mon 06:45-07:05",
        "tags": [
            ("HT_INCOMER.MD", "peak window", "06:48-06:56"),
            ("PRESS_L1.START", "TRUE", "06:47"),
            ("SQF1.PREHEAT", "ON", "06:49+"),
            ("COMP_BANK.RUN", "ON", "06:48+"),
        ],
        "cite": "physics/md_overlap@v2.4 · example only · confirm on live plant data",
    },
    "rx2": {
        "badge": "Rx · Equipment · drift",
        "aria": "Inspect compressor inlet filter after specific-power drift. Show evidence.",
        "action": "Inspect inlet filter and oil separator on Compressor 2 · check unload valve",
        "why": "Specific power up about 16% versus 8-week baseline on similar shift hours",
        "bill": "Energy (kWh) · equipment risk",
        "owner": "Utilities / maintenance",
        "impact": "₹45-70k / month if curve recovers (example)",
        "effort": "About 2 h · bypass on Compressor 1 if available",
        "rule": "sp_drift@v1.6 · High",
        "due": "This maintenance window",
        "evTitle": "Specific-power trend · last 8 weeks",
        "tags": [
            ("COMP2.kW_PER_AIR", "+16% vs base", "same hours"),
            ("COMP2.RUN_H", "aligned", "baseline window"),
            ("PROD.SHIFT", "matched", "not volume-driven"),
            ("FILTER.SERVICE", "overdue proxy", "inspect"),
        ],
        "cite": "rules/sp_drift@v1.6 · example only · confirm on live plant data",
    },
    "floor": [
        {
            "title": "Stagger press vs furnace preheat by 10-12 min",
            "why": "MD peak from Monday forge / HT overlap",
            "impact": "₹0.8-1.2L/mo on MD line (example)",
            "owner": "Electrical supervisor · B",
            "priority": "High",
            "due": "This week · before next peak",
        },
        {
            "title": "Inspect Compressor 2 filter after kW drift",
            "why": "Specific power up versus baseline · fouling proxy",
            "impact": "₹45-70k/mo if curve recovers (example)",
            "owner": "Utilities / maintenance",
            "priority": "High",
            "due": "This maintenance window",
        },
        {
            "title": "Check SQF quench-pump start retries",
            "why": "Trip / retry cluster before heat-treatment batch",
            "impact": "Avoid batch loss + MD risk",
            "owner": "HT electrician · furnace bay",
            "priority": "Med",
            "due": "Before next charge",
        },
    ],
    "verify": [
        ("MD stagger · press/furnace", "Sample MD peak", "10-12 min lag", "VERIFIED"),
        ("Compressor 2 filter service", "kW / air curve", "Service close-out", "PENDING"),
        ("Quench-pump trip cluster", "Start retries", "Inspect + clear", "IN REVIEW"),
    ],
    "math": {
        "eyebrow": "Where value usually shows up on integrated forge floors",
        "h2": "What we check first",
        "ledeD": "Two pillars on the same meters. Energy actions move MD, idle heat, air, and PF. Equipment actions catch drift and trips on presses, furnaces, CNC cells, and utilities before a stoppage. Sample only until live data confirms.",
        "ledeM": "Energy and equipment checks on forge, HT, CNC, and surface floors.",
        "cards": [
            (
                "Energy · MD / demand",
                [
                    "2500 T press / hammer + HT furnace coincidence",
                    "Quench / shot-blast aux with forge start",
                    "CNC bay or surface line in the same MD window",
                ],
                "Bill line · MD (kVA)",
                "Example: press-line ramp and SQF preheat stack at day-shift start",
            ),
            (
                "Energy · process heat / idle",
                [
                    "Carburize / Q&T hold over lunch",
                    "Induction idle between lots",
                    "Surface bath heaters or rectifier left on",
                ],
                "Bill line · Energy (kWh)",
                "Example: sealed-quench hold flat through lunch with no charge scheduled",
            ),
            (
                "Energy · air / PF",
                [
                    "Off-shift compressor unload (forge / CNC air)",
                    "Header pressure too high for gantries and tools",
                    "PF penalty on HT incomer before more APFC",
                ],
                "Bill line · Energy + PF",
                "Example: night air unload with forge, HT, and CNC dark",
            ),
            (
                "Equipment · utility drift",
                [
                    "Compressor specific-power rise between AMC visits",
                    "Inspect / clean / tune cards for filter and unload",
                    "Cooling or quench circuit kW drift",
                ],
                "Ops risk + energy co-benefit",
                "Example: Compressor 2 kW per air unit up 16% versus baseline",
            ),
            (
                "Equipment · trips / duty",
                [
                    "SQF quench / circulation start retries",
                    "Press or hammer ramp signature change",
                    "CNC spindle idle or gantry parked with aux on",
                ],
                "Ops risk · downtime",
                "Example: three quench-pump start retries before a HT batch",
            ),
        ],
    },
    "techBullet": "MD stagger, furnace hold, compressor drift, trip clusters, Improve from acted versus ignored",
    "offerLedeD": "Start with one works. Connect read-only, run ranked energy and equipment prescriptions, then go or no-go on verified outcomes.",
    "offerLedeM": "One works. Connect · prescribe · go / no-go on evidence.",
}

HERO = "assets/auto-forge-ht/steel-hero.jpg"
HERO_ALT = "Thermal and heavy manufacturing floor (illustrative)"
SLUG = "auto-forge-ht"

TWO_PILLARS = {
    "eyebrow": "One product · two pillars",
    "h2": "How Stamped helps on these floors",
    "lede": "Same meters. Same loop. Two kinds of assigned work: cut avoidable electricity cost, and flag equipment issues early so maintenance can act before a stoppage.",
    "left_title": "01 · Load and energy efficiency",
    "left": [
        "Maximum demand and shift-start overlap",
        "Furnace hold, idle loads, tariff windows",
        "Ranked prescriptions with owner and monthly rupees",
        "Proof on the energy ledger · bill can confirm",
    ],
    "right_title": "02 · Prescriptive equipment intelligence",
    "right": [
        "Early warnings from electrical and process signatures",
        "Inspect / clean / tune cards for utilities and cells",
        "Not vibration PdM and not a CMMS replacement",
        "Verify when the signature recovers after close-out",
    ],
    "note": "Not an MES. Not a plant OS. Shared plant context (schedules, departments) only makes management actions practical.",
}

OFFER_PATCH = {
    "eyebrow": "Scoped proof",
    "h2": "How a 60-day proof works",
    "lede": "",
    "rows": [
        (
            "Connect",
            "Read-only meters · optional feeder · bill lines for context",
        ),
        (
            "Live",
            "Energy and equipment prescriptions · WhatsApp to the owner",
        ),
        (
            "Verify",
            "Evidence pack on signature or MD / energy movement · bill optional",
        ),
        (
            "Day 60",
            "Go / no-go on verified outcomes and plant fit",
        ),
    ],
    "chips": [
        "Two pillars",
        "Verified with evidence",
        "Read-only OT",
        "Improve from follow / ignore",
    ],
    "ask_title": "Useful next step",
    "ask_body": "A short walk of one boundary with your electrical or maintenance host, plus recent HT bills when you are ready. No hardware. No PLC writes.",
}

HEADING_PATCHES = [
    (
        '<p class="eyebrow reveal">What Stamped does</p>\n'
        '        <h2 class="reveal">Signals become work orders.</h2>',
        '<p class="eyebrow reveal">How Stamped works</p>\n'
        '        <h2 class="reveal">Connect to Improve</h2>',
    ),
    (
        '<p class="eyebrow reveal">Sample prescriptions</p>\n'
        '        <h2 class="reveal">Every action has a bill line and an owner.</h2>',
        '<p class="eyebrow reveal">Example prescriptions</p>\n'
        '        <h2 class="reveal">One energy card. One equipment card.</h2>',
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

# Six-step loop replacement for scene-what do-chain
WHAT_LOOP_HTML = """        <div class="do-chain reveal">
          <article class="do-step">
            <div class="do-step__num">01</div>
            <h3>Connect</h3>
            <p id="whatStep1">Incomer and feeder meters, furnace / press / die-cast states where available, and bill lines. Optional production or ERP schedule read. Read-only. No control writes.</p>
            <span class="do-arrow" aria-hidden="true">&rarr;</span>
          </article>
          <article class="do-step">
            <div class="do-step__num">02</div>
            <h3>Observe</h3>
            <p>Baselines, MD windows, idle and hold patterns, equipment drift and trip clusters.</p>
            <span class="do-arrow" aria-hidden="true">&rarr;</span>
          </article>
          <article class="do-step">
            <div class="do-step__num">03</div>
            <h3>Decide</h3>
            <p>Ranked prescriptions with why, owner, effort, and expected rupee or risk impact.</p>
            <span class="do-arrow" aria-hidden="true">&rarr;</span>
          </article>
          <article class="do-step">
            <div class="do-step__num">04</div>
            <h3>Execute</h3>
            <p>WhatsApp and dashboard to the person who can act. Status tracked.</p>
            <span class="do-arrow" aria-hidden="true">&rarr;</span>
          </article>
          <article class="do-step">
            <div class="do-step__num">05</div>
            <h3>Verify</h3>
            <p>Ops-cleared evidence pack. Bill confirmation optional when the period closes.</p>
            <span class="do-arrow" aria-hidden="true">&rarr;</span>
          </article>
          <article class="do-step">
            <div class="do-step__num">06</div>
            <h3>Improve</h3>
            <p>Learn from followed versus ignored actions. Tighten ranking and baselines with human review.</p>
          </article>
        </div>"""
