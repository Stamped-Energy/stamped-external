#!/usr/bin/env python3
"""Build private client / OEM demo decks (not on the public industry hub).

Outputs:
  demo-decks/clients/machinery-oem.html          anonymous full Proof Run
  demo-decks/clients/machinery-oem/index.html    optional deploy root
  demo-decks/clients/lohia-corp-brief.html       short named walkthrough

Reuses helpers from build-industry-decks.py without adding client decks to HUB.
"""
from __future__ import annotations

import importlib.util
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DECKS = ROOT / "demo-decks"
CLIENTS = DECKS / "clients"
FORBIDDEN_FULL = re.compile(
    r"lohia|chaubepur|vijay|panki|peenya|lohiagroup", re.I
)


def load_industry_builder():
    path = SCRIPTS / "build-industry-decks.py"
    code = path.read_text(encoding="utf-8")
    code = code.replace('ROOT = Path("/workspace")', f"ROOT = Path(r{str(ROOT)!r})")
    spec = importlib.util.spec_from_loader("build_industry_decks", loader=None)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    exec(compile(code, str(path), "exec"), mod.__dict__)
    return mod


def rewrite_client_paths(html: str, *, depth: int) -> str:
    """depth=1 for clients/*.html; depth=2 for clients/<slug>/index.html."""
    prefix = "../" * depth
    html = html.replace('href="tech/', f'href="{prefix}tech/')
    html = html.replace('src="assets/', f'src="{prefix}assets/')
    html = html.replace('href="assets/', f'href="{prefix}assets/')
    # Boot script resolves the hero from a relative path string
    html = html.replace('var rel = "assets/', f'var rel = "{prefix}assets/')
    return html


def patch_offer_90_day(html: str, lede_d: str) -> str:
    """Tune offer slide toward a 90-day single-works proof (full OEM demo)."""
    html = html.replace(
        '<p class="eyebrow reveal">60-day proof run</p>\n'
        '        <h2 class="reveal">Proof Run</h2>',
        '<p class="eyebrow reveal">90-day proof run</p>\n'
        '        <h2 class="reveal">Proof Run · one works</h2>',
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
              <td>Weeks 1-2</td>
              <td>Works audit · map meters, EMS, and bill lines · understand data you already have</td>
            </tr>
            <tr>
              <td>Weeks 3-10</td>
              <td>Connect read-only · floor executes prescriptions · weekly reviews</td>
            </tr>
            <tr>
              <td>Day 90</td>
              <td>Go / no-go: on verified ₹ and fit. Kill criteria agreed upfront.</td>
            </tr>"""
    if old_rows not in html:
        raise SystemExit("offer phase rows not found for OEM patch")
    html = html.replace(old_rows, new_rows, 1)
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
    # Replace mobile lede if present
    html = re.sub(
        r'(id="offerLedeM"[^>]*>)(.*?)(</)',
        rf'\g<1>{offer["lede"]}\g<3>',
        html,
        count=1,
        flags=re.S,
    )
    # Inject desktop lede after h2 if missing
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
    """Remove <section ... id="scene-..."> blocks not in keep."""
    pattern = re.compile(
        r'<section class="slide[^"]*"[^>]*id="(scene-[^"]+)"[^>]*>.*?</section>',
        re.S,
    )

    def repl(m: re.Match) -> str:
        sid = m.group(1)
        return m.group(0) if sid in keep else ""

    out = pattern.sub(repl, html)
    # collapse excess blank lines between sections
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out


def inject_brief_brand(html: str) -> str:
    """Show Lohia logo chip on title for the named brief."""
    logo = "../assets/lohia-corp/lohia-logo.svg"
    chip = (
        f'<p class="industry-chip reveal" id="industryChip">Lohia Corp</p>\n'
        f'            <img class="client-logo reveal" src="{logo}" alt="Lohia Corp" '
        f'width="160" height="40" loading="eager" decoding="async" '
        f'style="height:36px;width:auto;margin:0.35rem 0 0.5rem;" />'
    )
    # industry chip already injected by build_one; prepend logo after chip
    html = html.replace(
        '<p class="industry-chip reveal" id="industryChip">Lohia Corp</p>',
        chip,
        1,
    )
    # mark html for brief mode
    html = html.replace(
        'data-industry="lohia corp"',
        'data-industry="lohia-corp" data-client-brief="lohia"',
        1,
    )
    return html


def build_full(mod, base: str) -> str:
    from deck_packs.machinery_oem import HERO, HERO_ALT, PACK, SLUG

    mod.PACKS[SLUG] = PACK
    mod.HERO_BY_INDUSTRY[SLUG] = HERO
    mod.HERO_ALT[SLUG] = HERO_ALT
    html = mod.build_one(base, SLUG)
    html = rewrite_client_paths(html, depth=1)
    html = patch_offer_90_day(
        html,
        "Start with one works: electrical POC, two HT bills, and a walkthrough. "
        "Read-only. Kill criteria agreed upfront.",
    )
    # deep-dive from= must match slug
    html = html.replace("?from=machinery-oem", "?from=machinery-oem")
    return html


def build_brief(mod, base: str) -> str:
    from deck_packs.lohia_corp_brief import (
        HERO,
        HERO_ALT,
        KEEP_SCENES,
        OFFER_PATCH,
        PACK,
        SLUG,
    )

    # Use a temporary industry key that build_one accepts
    key = "lohia-corp"
    mod.PACKS[key] = PACK
    mod.HERO_BY_INDUSTRY[key] = HERO
    mod.HERO_ALT[key] = HERO_ALT
    html = mod.build_one(base, key)
    html = strip_scenes(html, KEEP_SCENES)
    html = rewrite_client_paths(html, depth=1)
    html = inject_brief_brand(html)
    html = patch_offer_brief(html, OFFER_PATCH)
    # Hide second rx card emphasis on mobile via note in meta - keep both for flip demo
    # Retarget tech links if any remain (should be stripped with scene-tech)
    html = html.replace("?from=lohia-corp", "?from=lohia-corp")
    # Ensure title tag matches brief
    html = re.sub(
        r"<title>.*?</title>",
        f"<title>{PACK['docTitle']}</title>",
        html,
        count=1,
    )
    _ = SLUG
    return html


def assert_anonymous(html: str, path: Path) -> None:
    hits = FORBIDDEN_FULL.findall(html)
    if hits:
        raise SystemExit(
            f"FORBIDDEN client names in {path}: {sorted(set(hits))[:12]}"
        )


def main() -> None:
    sys.path.insert(0, str(SCRIPTS))
    mod = load_industry_builder()
    snapshot = DECKS / "_base.snapshot.html"
    if not snapshot.exists():
        raise SystemExit("missing demo-decks/_base.snapshot.html")
    base = snapshot.read_text(encoding="utf-8")

    CLIENTS.mkdir(parents=True, exist_ok=True)

    full = build_full(mod, base)
    full_path = CLIENTS / "machinery-oem.html"
    full_path.write_text(full, encoding="utf-8")
    assert_anonymous(full, full_path)
    print(f"wrote {full_path} ({len(full)} bytes)")

    deploy_dir = CLIENTS / "machinery-oem"
    deploy_dir.mkdir(parents=True, exist_ok=True)
    deploy_path = deploy_dir / "index.html"
    from deck_packs.machinery_oem import HERO, HERO_ALT, PACK, SLUG

    mod.PACKS[SLUG] = PACK
    mod.HERO_BY_INDUSTRY[SLUG] = HERO
    mod.HERO_ALT[SLUG] = HERO_ALT
    raw = mod.build_one(base, SLUG)
    raw = patch_offer_90_day(
        raw,
        "Start with one works: electrical POC, two HT bills, and a walkthrough. "
        "Read-only. Kill criteria agreed upfront.",
    )
    deploy_html = rewrite_client_paths(raw, depth=2)
    assert_anonymous(deploy_html, deploy_path)
    deploy_path.write_text(deploy_html, encoding="utf-8")
    print(f"wrote {deploy_path} ({len(deploy_html)} bytes)")

    brief = build_brief(mod, base)
    brief_path = CLIENTS / "lohia-corp-brief.html"
    brief_path.write_text(brief, encoding="utf-8")
    if not FORBIDDEN_FULL.search(brief):
        raise SystemExit("brief should contain Lohia naming")
    print(f"wrote {brief_path} ({len(brief)} bytes)")

    # Copy robots-style note
    note = CLIENTS / "README.md"
    note.write_text(
        "# Private client decks\n\n"
        "Not linked from the public cement/steel/pharma hub.\n\n"
        "| File | Use |\n"
        "|------|-----|\n"
        "| [machinery-oem.html](./machinery-oem.html) | Anonymous full Proof Run (packaging-machinery OEM) |\n"
        "| [machinery-oem/](./machinery-oem/) | Optional standalone deploy root |\n"
        "| [lohia-corp-brief.html](./lohia-corp-brief.html) | Short Lohia-branded meeting walkthrough |\n\n"
        "Rebuild: `python3 scripts/build-client-decks.py`\n",
        encoding="utf-8",
    )
    print("wrote clients/README.md")


if __name__ == "__main__":
    main()
