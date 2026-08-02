#!/usr/bin/env python3
"""Build private client / OEM demo decks (not on the public industry hub).

Outputs:
  demo-decks/clients/machinery-oem.html          anonymous full Proof Run
  demo-decks/clients/machinery-oem/index.html    optional deploy root
  demo-decks/clients/lohia-corp-brief.html       short named walkthrough
  demo-decks/clients/auto-forge-ht.html          forge / HT / die-cast value walkthrough

Assets are co-located under demo-decks/clients/assets/ so relative paths work
when the HTML is opened from the clients/ folder (file:// or HTTP).
"""
from __future__ import annotations

import importlib.util
import re
import shutil
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent  # scripts/decks/build
DECKS_PKG = _HERE.parent  # scripts/decks (deck_packs live here)
EXTERNAL = _HERE.parents[2]  # stamped-external root
DECKS = EXTERNAL / "demo-decks"
CLIENTS = DECKS / "clients"
CLIENT_ASSETS = CLIENTS / "assets"
FORBIDDEN_FULL = re.compile(
    r"lohia|chaubepur|vijay|panki|peenya|lohiagroup", re.I
)
FORBIDDEN_LNM = re.compile(
    r"\blnm\b|lnmauto|divyansh|sandeep\s+mall|sector\s*59|faridabad", re.I
)
SAMPLE_WORKSPACE_URL = "https://trying.stamped.work/"


def load_industry_builder():
    path = _HERE / "build-industry-decks.py"
    code = path.read_text(encoding="utf-8")
    code = code.replace(
        'ROOT = Path("/workspace")', f"ROOT = Path(r{str(EXTERNAL)!r})"
    )
    spec = importlib.util.spec_from_loader("build_industry_decks", loader=None)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    exec(compile(code, str(path), "exec"), mod.__dict__)
    return mod


def sync_client_assets() -> None:
    """Copy OEM + Lohia + forge-HT visuals next to client HTML so assets/ resolves locally."""
    CLIENT_ASSETS.mkdir(parents=True, exist_ok=True)
    for name in ("lohia-corp", "machinery-oem"):
        src = DECKS / "assets" / name
        dst = CLIENT_ASSETS / name
        if not src.is_dir():
            raise SystemExit(f"missing source assets: {src}")
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        # Drop markdown from runtime asset tree (keep sources under demo-decks/assets/)
        for md in dst.glob("*.md"):
            md.unlink()
    # Forge / HT brief reuses steel industry hero (illustrative thermal / heavy floor)
    forge_dst = CLIENT_ASSETS / "auto-forge-ht"
    forge_dst.mkdir(parents=True, exist_ok=True)
    steel_hero = DECKS / "assets" / "steel-hero.jpg"
    if not steel_hero.is_file():
        raise SystemExit(f"missing steel hero for forge-HT deck: {steel_hero}")
    shutil.copy2(steel_hero, forge_dst / "steel-hero.jpg")
    print(f"synced assets -> {CLIENT_ASSETS}")


def rewrite_client_paths(html: str, *, asset_prefix: str, tech_prefix: str) -> str:
    """Rewrite build_one paths for clients/ (local assets) and nested deploy roots."""
    html = html.replace('href="tech/', f'href="{tech_prefix}tech/')
    if asset_prefix != "assets/":
        html = html.replace('src="assets/', f'src="{asset_prefix}')
        html = html.replace('href="assets/', f'href="{asset_prefix}')
        html = html.replace('var rel = "assets/', f'var rel = "{asset_prefix}')
    # Flat clients/*.html: keep assets/ as-is (co-located under clients/assets/)
    # but still need tech up one level
    return html


def patch_offer_one_works(html: str, lede_d: str) -> str:
    """Tune OEM offer: real-time decisions + early warnings + 60-day Proof Run as needed."""
    html = html.replace(
        '<p class="eyebrow reveal">60-day proof run</p>\n'
        '        <h2 class="reveal">Proof Run</h2>',
        '<p class="eyebrow reveal">Optional 60-day Proof Run</p>\n'
        '        <h2 class="reveal">Start with one works</h2>',
        1,
    )
    old_rows = """            <tr>
              <td>Weeks 1-2</td>
              <td>Plant audit · map meters, EMS, and bill lines · understand the data you already have</td>
            </tr>
            <tr>
              <td>Weeks 3-8</td>
              <td>Connect read-only · floor executes prescriptions · weekly reviews</td>
            </tr>
            <tr>
              <td>Day 60</td>
              <td>Go / no-go: on verified ₹ and fit (efficiency, workload, how the floor actually runs)</td>
            </tr>"""
    new_rows = """            <tr>
              <td>Connect</td>
              <td>Read-only on meters / EMS · map tape, loom, test-bay, and utility islands</td>
            </tr>
            <tr>
              <td>Live</td>
              <td>Real-time prescriptions and line-tied early warnings · floor owns each ₹ action</td>
            </tr>
            <tr>
              <td>Day 60</td>
              <td>Optional scoped Proof Run: go / no-go on verified ₹ and plant fit</td>
            </tr>"""
    if old_rows not in html:
        raise SystemExit("offer phase rows not found for OEM patch")
    html = html.replace(old_rows, new_rows, 1)
    chips = (
        '\n          <span class="chip">Live decisions</span>'
        '\n          <span class="chip">Line-level early warnings</span>'
        '\n          <span class="chip">60-day Proof Run when useful</span>'
        '\n          <span class="chip">Read-only OT</span>\n        '
    )
    html = re.sub(
        r'(<div class="commercial reveal">)(.*?)(</div>\s*<div class="ask-box)',
        rf"\g<1>{chips}\g<3>",
        html,
        count=1,
        flags=re.S,
    )
    html = html.replace(
        "<p>Let’s get on a short call. No bills required upfront.</p>",
        f"<p>{lede_d}</p>",
        1,
    )
    return html


def patch_offer_brief(html: str, offer: dict) -> str:
    html = re.sub(
        r'(<section class="slide slide--light" id="scene-offer"[^>]*>.*?'
        r'<p class="eyebrow reveal">)(.*?)(</p>\s*'
        r'<h2 class="reveal">)(.*?)(</h2>)',
        rf'\g<1>{offer["eyebrow"]}\g<3>{offer["h2"]}\g<5>',
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'(id="offerLedeM"[^>]*>)(.*?)(</)',
        rf'\g<1>{offer["lede"]}\g<3>',
        html,
        count=1,
        flags=re.S,
    )
    if 'id="offerLedeD"' not in html:
        html = html.replace(
            f'<h2 class="reveal">{offer["h2"]}</h2>\n',
            f'<h2 class="reveal">{offer["h2"]}</h2>\n'
            f'        <p class="lede reveal hide-mobile" id="offerLedeD">{offer["lede"]}</p>\n',
            1,
        )
    rows_html = "\n".join(
        f"""            <tr>
              <td>{a}</td>
              <td>{b}</td>
            </tr>"""
        for a, b in offer["rows"]
    )
    html = re.sub(
        r'(<table class="phase-table reveal">\s*<thead>.*?</thead>\s*<tbody>)(.*?)(</tbody>)',
        rf"\g<1>\n{rows_html}\n          \g<3>",
        html,
        count=1,
        flags=re.S,
    )
    chips = "".join(f'\n          <span class="chip">{c}</span>' for c in offer["chips"])
    html = re.sub(
        r'(<div class="commercial reveal">)(.*?)(</div>\s*<div class="ask-box)',
        rf"\g<1>{chips}\n        \g<3>",
        html,
        count=1,
        flags=re.S,
    )
    html = re.sub(
        r'(<div class="ask-box reveal">\s*<strong>)(.*?)(</strong>\s*<p>)(.*?)(</p>)',
        rf'\g<1>{offer["ask_title"]}\g<3>{offer["ask_body"]}\g<5>',
        html,
        count=1,
        flags=re.S,
    )
    return html


def strip_scenes(html: str, keep: list[str]) -> str:
    pattern = re.compile(
        r'<section class="slide[^"]*"[^>]*id="(scene-[^"]+)"[^>]*>.*?</section>',
        re.S,
    )

    def repl(m: re.Match) -> str:
        return m.group(0) if m.group(1) in keep else ""

    out = pattern.sub(repl, html)
    return re.sub(r"\n{3,}", "\n\n", out)


def inject_brief_brand(html: str) -> str:
    logo = "assets/lohia-corp/lohia-logo.svg"
    chip = (
        f'<p class="industry-chip reveal" id="industryChip">Lohia Corp</p>\n'
        f'            <img class="client-logo reveal" src="{logo}" alt="Lohia Corp" '
        f'width="160" height="40" loading="eager" decoding="async" '
        f'style="height:36px;width:auto;margin:0.35rem 0 0.5rem;" />'
    )
    html = html.replace(
        '<p class="industry-chip reveal" id="industryChip">Lohia Corp</p>',
        chip,
        1,
    )
    html = html.replace(
        'data-industry="lohia corp"',
        'data-industry="lohia-corp" data-client-brief="lohia"',
        1,
    )
    # Client-facing: no academic affiliation lines on the Lohia brief
    html = re.sub(
        r'\s*<p class="cred-quiet[^"]*"[^>]*>Built on energy systems research at IIT Roorkee\.</p>',
        "",
        html,
        count=1,
    )
    return html


def inject_lohia_lines_scene(html: str, lines: dict) -> str:
    """Named brief only: Lohia product families + machine technologies."""
    fam = "\n".join(f"              <li>{item}</li>" for item in lines["families"])
    tech = "\n".join(
        f"              <li><strong>{name}</strong> — {desc}</li>"
        for name, desc in lines["tech"]
    )
    # Use middle-dot instead of em dash for client copy consistency
    tech = tech.replace(" — ", " · ")
    scene = f"""
    <section class="slide slide--light" id="scene-lohia-lines" data-theme="light" aria-label="Lohia product lines and technologies">
      <div class="slide__inner slide__inner--wide">
        <p class="eyebrow reveal">{lines["eyebrow"]}</p>
        <h2 class="reveal">{lines["h2"]}</h2>
        <p class="lede reveal">{lines["lede"]}</p>
        <div class="bound-grid reveal" style="margin-top:1rem;">
          <div class="bound-col bound-col--not">
            <h3>{lines["families_title"]}</h3>
            <ul class="bound-list">
{fam}
            </ul>
          </div>
          <div class="bound-col bound-col--ot">
            <h3>{lines["tech_title"]}</h3>
            <ul class="bound-list">
{tech}
            </ul>
          </div>
        </div>
        <p class="meta reveal hide-mobile" style="margin-top:1.1rem;max-width:48em;">{lines["note"]}</p>
      </div>
    </section>

"""
    marker = '<section class="slide slide--light" id="scene-math"'
    if marker not in html:
        raise SystemExit("scene-math not found for lohia-lines inject")
    if 'id="scene-lohia-lines"' in html:
        return html
    return html.replace(marker, scene + marker, 1)


def inject_vs_audit_scene(html: str, vs: dict) -> str:
    left = "\n".join(f"              <li>{item}</li>" for item in vs["left"])
    right = "\n".join(f"              <li>{item}</li>" for item in vs["right"])
    scene = f"""
    <section class="slide slide--light" id="scene-vs-audit" data-theme="light" aria-label="Not another energy audit">
      <div class="slide__inner slide__inner--wide">
        <p class="eyebrow reveal">{vs["eyebrow"]}</p>
        <h2 class="reveal">{vs["h2"]}</h2>
        <p class="lede reveal">{vs["lede"]}</p>
        <div class="bound-grid reveal" style="margin-top:1rem;">
          <div class="bound-col bound-col--not">
            <h3>{vs["left_title"]}</h3>
            <ul class="bound-list">
{left}
            </ul>
          </div>
          <div class="bound-col bound-col--ot">
            <h3>{vs["right_title"]}</h3>
            <ul class="bound-list">
{right}
            </ul>
          </div>
        </div>
        <p class="meta reveal hide-mobile" style="margin-top:1.1rem;max-width:46em;">{vs["note"]}</p>
      </div>
    </section>

"""
    marker = '<section class="slide slide--light" id="scene-offer"'
    if marker not in html:
        raise SystemExit("scene-offer not found for vs-audit inject")
    if 'id="scene-vs-audit"' in html:
        return html
    return html.replace(marker, scene + marker, 1)


def inject_two_pillars_scene(html: str, pillars: dict) -> str:
    left = "\n".join(f"              <li>{item}</li>" for item in pillars["left"])
    right = "\n".join(f"              <li>{item}</li>" for item in pillars["right"])
    scene = f"""
    <section class="slide slide--light" id="scene-two-pillars" data-theme="light" aria-label="Two pillars one product">
      <div class="slide__inner slide__inner--wide">
        <p class="eyebrow reveal">{pillars["eyebrow"]}</p>
        <h2 class="reveal">{pillars["h2"]}</h2>
        <p class="lede reveal">{pillars["lede"]}</p>
        <div class="bound-grid reveal" style="margin-top:1rem;">
          <div class="bound-col bound-col--ot">
            <h3>{pillars["left_title"]}</h3>
            <ul class="bound-list">
{left}
            </ul>
          </div>
          <div class="bound-col bound-col--not">
            <h3>{pillars["right_title"]}</h3>
            <ul class="bound-list">
{right}
            </ul>
          </div>
        </div>
        <p class="meta reveal hide-mobile" style="margin-top:1.1rem;max-width:48em;">{pillars["note"]}</p>
      </div>
    </section>

"""
    marker = '<section class="slide slide--light" id="scene-math"'
    if marker not in html:
        raise SystemExit("scene-math not found for two-pillars inject")
    if 'id="scene-two-pillars"' in html:
        return html
    return html.replace(marker, scene + marker, 1)


def patch_what_loop(html: str, loop_html: str) -> str:
    """Replace the four-step do-chain with Connect→Improve (six steps)."""
    pattern = re.compile(
        r'<div class="do-chain reveal">.*?</div>\s*<div class="flow-tags',
        re.S,
    )
    html2, n = pattern.subn(
        loop_html.strip() + '\n        <div class="flow-tags', html, count=1
    )
    if n != 1:
        raise SystemExit(f"what-loop patch failed (n={n})")
    return html2


def patch_sample_workspace(html: str, url: str = SAMPLE_WORKSPACE_URL) -> str:
    """Point the Sample workspace iframe at trying.stamped.work and add an Open button."""
    old_title = """        <div class="dash-title-row reveal">
          <h2>Sample workspace</h2>
          <p>Simulated data, not your plant</p>
        </div>
        <div class="dash-shell reveal">
          <div class="dash-badge hide-mobile">Simulated sample</div>
          <iframe
            id="dashFrame"
            data-src="https://stamped-energy.vercel.app/"
            title="Stamped Energy simulated dashboard"
            sandbox="allow-scripts allow-same-origin allow-popups allow-forms"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>"""
    new_title = f"""        <div class="dash-title-row reveal dash-title-row--actions">
          <div>
            <h2>Sample workspace</h2>
            <p>Live demo · trying.stamped.work · sample plant, not your site</p>
          </div>
          <a class="btn btn--primary" id="openSampleWorkspace" href="{url}" target="_blank" rel="noopener noreferrer">Open workspace</a>
        </div>
        <div class="dash-shell reveal">
          <div class="dash-badge hide-mobile">trying.stamped.work</div>
          <iframe
            id="dashFrame"
            data-src="{url}"
            title="Stamped Energy sample workspace"
            sandbox="allow-scripts allow-same-origin allow-popups allow-forms"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>"""
    if old_title not in html:
        raise SystemExit("sample workspace block not found")
    html = html.replace(old_title, new_title, 1)
    css = """
    .dash-title-row--actions {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .dash-title-row--actions .btn { flex: 0 0 auto; text-decoration: none; }
"""
    if ".dash-title-row--actions" not in html:
        html = html.replace("</style>", css + "\n  </style>", 1)
    return html


def normalize_dashes(html: str) -> str:
    """Client decks forbid em/en dashes in visible copy (check-client-decks gate)."""
    return html.replace("—", " · ").replace("–", "-")


def build_full(mod, base: str) -> str:
    from deck_packs.machinery_oem import (
        HERO,
        HERO_ALT,
        OEM_HEADING_PATCHES,
        PACK,
        SLUG,
    )

    mod.PACKS[SLUG] = PACK
    mod.HERO_BY_INDUSTRY[SLUG] = HERO
    mod.HERO_ALT[SLUG] = HERO_ALT
    html = mod.build_one(base, SLUG)
    # Flat file in clients/: assets/ is local; tech is ../tech/
    html = rewrite_client_paths(html, asset_prefix="assets/", tech_prefix="../")
    html = patch_offer_one_works(html, PACK["offerLedeD"])
    for old, new in OEM_HEADING_PATCHES:
        if old not in html:
            raise SystemExit(f"OEM heading patch missed:\n{old[:80]}...")
        html = html.replace(old, new, 1)
    html = patch_sample_workspace(html)
    return normalize_dashes(html)


def build_brief(mod, base: str) -> str:
    from deck_packs.lohia_corp_brief import (
        BRIEF_HEADING_PATCHES,
        HERO,
        HERO_ALT,
        KEEP_SCENES,
        LOHIA_LINES,
        OFFER_PATCH,
        PACK,
        SLUG,
        VS_AUDIT,
    )

    key = "lohia-corp"
    mod.PACKS[key] = PACK
    mod.HERO_BY_INDUSTRY[key] = HERO
    mod.HERO_ALT[key] = HERO_ALT
    html = mod.build_one(base, key)
    html = strip_scenes(html, KEEP_SCENES)
    html = rewrite_client_paths(html, asset_prefix="assets/", tech_prefix="../")
    html = inject_brief_brand(html)
    html = inject_lohia_lines_scene(html, LOHIA_LINES)
    html = inject_vs_audit_scene(html, VS_AUDIT)
    html = patch_offer_brief(html, OFFER_PATCH)
    for old, new in BRIEF_HEADING_PATCHES:
        if old not in html:
            raise SystemExit(f"brief heading patch missed:\n{old[:80]}...")
        html = html.replace(old, new, 1)
    html = re.sub(
        r"<title>.*?</title>",
        f"<title>{PACK['docTitle']}</title>",
        html,
        count=1,
    )
    _ = SLUG
    return normalize_dashes(html)


def build_forge_ht(mod, base: str) -> str:
    from deck_packs.auto_forge_ht import (
        HEADING_PATCHES,
        HERO,
        HERO_ALT,
        KEEP_SCENES,
        OFFER_PATCH,
        PACK,
        SLUG,
        TWO_PILLARS,
        WHAT_LOOP_HTML,
    )

    key = SLUG
    mod.PACKS[key] = PACK
    mod.HERO_BY_INDUSTRY[key] = HERO
    mod.HERO_ALT[key] = HERO_ALT
    html = mod.build_one(base, key)
    html = strip_scenes(html, KEEP_SCENES)
    html = rewrite_client_paths(html, asset_prefix="assets/", tech_prefix="../")
    html = inject_two_pillars_scene(html, TWO_PILLARS)
    html = patch_what_loop(html, WHAT_LOOP_HTML)
    html = patch_offer_brief(html, OFFER_PATCH)
    # Offer slide: keep eyebrow/h2/table; drop lede paragraphs when pack lede is blank
    html = re.sub(
        r'\s*<p class="lede reveal[^"]*" id="offerLede[DM]"[^>]*>.*?</p>',
        "",
        html,
        count=2,
        flags=re.S,
    )
    for old, new in HEADING_PATCHES:
        if old not in html:
            # allow already-patched verify heading
            if "Verified with evidence" in new and "Verified with evidence" in html:
                continue
            raise SystemExit(f"forge-HT heading patch missed:\n{old[:80]}...")
        html = html.replace(old, new, 1)
    html = html.replace(
        'data-industry="forge · ht · die cast"',
        'data-industry="auto-forge-ht" data-client-brief="forge-ht"',
        1,
    )
    html = re.sub(
        r"<title>.*?</title>",
        f"<title>{PACK['docTitle']}</title>",
        html,
        count=1,
    )
    hits = FORBIDDEN_LNM.findall(html)
    if hits:
        raise SystemExit(f"forge-HT pack must stay anonymous; found {sorted(set(hits))}")
    return normalize_dashes(html)


def assert_anonymous(html: str, path: Path) -> None:
    hits = FORBIDDEN_FULL.findall(html)
    if hits:
        raise SystemExit(
            f"FORBIDDEN client names in {path}: {sorted(set(hits))[:12]}"
        )


def main() -> None:
    sys.path.insert(0, str(DECKS_PKG))
    mod = load_industry_builder()
    snapshot = DECKS / "_base.snapshot.html"
    if not snapshot.exists():
        raise SystemExit("missing demo-decks/_base.snapshot.html")
    base = snapshot.read_text(encoding="utf-8")

    CLIENTS.mkdir(parents=True, exist_ok=True)
    sync_client_assets()

    full = build_full(mod, base)
    full_path = CLIENTS / "machinery-oem.html"
    full_path.write_text(full, encoding="utf-8")
    assert_anonymous(full, full_path)
    print(f"wrote {full_path} ({len(full)} bytes)")

    deploy_dir = CLIENTS / "machinery-oem"
    deploy_dir.mkdir(parents=True, exist_ok=True)
    deploy_path = deploy_dir / "index.html"
    from deck_packs.machinery_oem import (
        HERO,
        HERO_ALT,
        OEM_HEADING_PATCHES,
        PACK,
        SLUG,
    )

    mod.PACKS[SLUG] = PACK
    mod.HERO_BY_INDUSTRY[SLUG] = HERO
    mod.HERO_ALT[SLUG] = HERO_ALT
    raw = mod.build_one(base, SLUG)
    raw = patch_offer_one_works(raw, PACK["offerLedeD"])
    for old, new in OEM_HEADING_PATCHES:
        if old not in raw:
            raise SystemExit(f"OEM deploy heading patch missed:\n{old[:80]}...")
        raw = raw.replace(old, new, 1)
    raw = patch_sample_workspace(raw)
    deploy_html = rewrite_client_paths(
        raw, asset_prefix="../assets/", tech_prefix="../../"
    )
    assert_anonymous(deploy_html, deploy_path)
    deploy_path.write_text(normalize_dashes(deploy_html), encoding="utf-8")
    print(f"wrote {deploy_path} ({len(deploy_html)} bytes)")

    brief = build_brief(mod, base)
    brief_path = CLIENTS / "lohia-corp-brief.html"
    brief_path.write_text(brief, encoding="utf-8")
    if not FORBIDDEN_FULL.search(brief):
        raise SystemExit("brief should contain Lohia naming")
    if 'id="scene-vs-audit"' not in brief:
        raise SystemExit("brief missing vs-audit scene")
    if 'id="scene-lohia-lines"' not in brief:
        raise SystemExit("brief missing lohia-lines scene")
    print(f"wrote {brief_path} ({len(brief)} bytes)")

    forge = build_forge_ht(mod, base)
    forge_path = CLIENTS / "auto-forge-ht.html"
    forge_path.write_text(forge, encoding="utf-8")
    if 'id="scene-two-pillars"' not in forge:
        raise SystemExit("forge-HT missing scene-two-pillars")
    if "Improve" not in forge:
        raise SystemExit("forge-HT missing Improve loop step")
    if FORBIDDEN_LNM.search(forge):
        raise SystemExit("forge-HT must not name LNM / Faridabad / Mall")
    print(f"wrote {forge_path} ({len(forge)} bytes)")

    write_clients_hub()
    note = CLIENTS / "README.md"
    note.write_text(
        "# Client decks\n\n"
        "Linked from the main demo hub via **Clients** → [`index.html`](./index.html).\n\n"
        "| File | Use |\n"
        "|------|-----|\n"
        "| [index.html](./index.html) | Client deck picker |\n"
        "| [machinery-oem.html](./machinery-oem.html) | Anonymous full Proof Run (packaging-machinery OEM) |\n"
        "| [machinery-oem/](./machinery-oem/) | Optional standalone deploy root |\n"
        "| [lohia-corp-brief.html](./lohia-corp-brief.html) | Short Lohia-branded meeting walkthrough |\n"
        "| [auto-forge-ht.html](./auto-forge-ht.html) | Forge / HT / die-cast value walkthrough (two pillars) |\n"
        "| [assets/](./assets/) | Co-located images (open HTML from this folder) |\n\n"
        "Rebuild: `python scripts/decks/build/build-client-decks.py`\n",
        encoding="utf-8",
    )
    print("wrote clients/README.md")


CLIENT_HUB = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>Stamped Energy · Client decks</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet" />
  <style>
    :root {
      --primary: #F75440; --secondary: #051F13; --surface: #f7faf5;
      --on-surface: #191c1a; --muted: #5a403c; --line: #e3beb8;
      --font-d: "Plus Jakarta Sans", system-ui, sans-serif;
      --font-b: Inter, system-ui, sans-serif;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0; min-height: 100dvh; font-family: var(--font-b);
      color: var(--on-surface); background:
        radial-gradient(1200px 600px at 10% -10%, rgba(247,84,64,0.12), transparent 55%),
        radial-gradient(900px 500px at 100% 0%, rgba(0,102,107,0.08), transparent 50%),
        var(--surface);
      padding: max(1.5rem, env(safe-area-inset-top)) 1.25rem max(2rem, env(safe-area-inset-bottom));
    }
    main { max-width: 720px; margin: 0 auto; }
    .logo { height: 36px; width: auto; margin-bottom: 1.25rem; }
    .back {
      display: inline-block; margin-bottom: 1rem; font-size: 0.88rem; font-weight: 650;
      color: var(--secondary); text-decoration: none;
    }
    .back:hover { color: var(--primary); }
    h1 {
      font-family: var(--font-d); font-weight: 800; letter-spacing: -0.04em;
      font-size: clamp(1.8rem, 5vw, 2.4rem); line-height: 1.05; margin: 0 0 0.65rem;
      color: var(--secondary);
    }
    .lede { color: var(--muted); line-height: 1.5; margin: 0 0 1.75rem; max-width: 36em; }
    .grid { display: grid; gap: 0.85rem; }
    a.card {
      display: block; text-decoration: none; color: inherit;
      background: #fff; border: 1px solid var(--line); border-radius: 14px;
      padding: 1.15rem 1.25rem; transition: border-color 0.15s, transform 0.15s;
    }
    a.card:hover { border-color: var(--primary); transform: translateY(-1px); }
    a.card strong {
      display: block; font-family: var(--font-d); font-size: 1.2rem;
      margin-bottom: 0.35rem; color: var(--secondary);
    }
    a.card span { display: block; color: var(--muted); font-size: 0.92rem; line-height: 1.4; }
    a.card em {
      display: inline-block; margin-top: 0.75rem; font-style: normal;
      font-size: 0.8rem; font-weight: 700; color: var(--primary);
    }
    footer { margin-top: 2rem; font-size: 0.85rem; color: var(--muted); }
    footer a { color: var(--secondary); }
  </style>
</head>
<body>
  <main>
    <a class="back" href="../index.html">← Back to industry decks</a>
    <img class="logo" src="https://stamped.work/LogoOrange.png" alt="Stamped Energy" width="140" height="36" />
    <h1>Client decks</h1>
    <p class="lede">Meeting walkthroughs for named accounts and anonymous process demos. Same Stamped Proof Run design as the industry decks.</p>
    <div class="grid">
      <a class="card" href="./auto-forge-ht.html">
        <strong>Forge · HT · Die cast</strong>
        <span>Value walkthrough: two pillars (energy + equipment), evidence, Improve loop. Process-focused, not a named-account brochure.</span>
        <em>Open forge / HT demo →</em>
      </a>
      <a class="card" href="./lohia-corp-brief.html">
        <strong>Lohia Corp · brief</strong>
        <span>Named walkthrough: woven raffia lines, real-time decisions vs audit, early warnings, on-site Chaubepur ask.</span>
        <em>Open Lohia brief →</em>
      </a>
      <a class="card" href="./machinery-oem.html">
        <strong>Packaging machinery OEM</strong>
        <span>Full anonymous Proof Run. Real-time decisions, line-tied early warnings, 60-day pilot as needed.</span>
        <em>Open OEM demo →</em>
      </a>
      <a class="card" href="./machinery-oem/">
        <strong>OEM demo · deploy root</strong>
        <span>Same machinery OEM deck as a folder index for standalone hosting.</span>
        <em>Open deploy root →</em>
      </a>
    </div>
    <footer>
      <a href="../index.html">Industry hub</a>
      ·
      <a href="https://stamped.work">stamped.work</a>
    </footer>
  </main>
</body>
</html>
"""


def write_clients_hub() -> None:
    path = CLIENTS / "index.html"
    path.write_text(CLIENT_HUB, encoding="utf-8")
    print(f"wrote {path} ({len(CLIENT_HUB)} bytes)")


if __name__ == "__main__":
    main()
