#!/usr/bin/env python3
"""Build private client / OEM demo decks (not on the public industry hub).

Outputs:
  demo-decks/clients/machinery-oem.html          anonymous full Proof Run
  demo-decks/clients/machinery-oem/index.html    optional deploy root
  demo-decks/clients/lohia-corp-brief.html       short named walkthrough

Assets are co-located under demo-decks/clients/assets/ so relative paths work
when the HTML is opened from the clients/ folder (file:// or HTTP).
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
CLIENT_ASSETS = CLIENTS / "assets"
FORBIDDEN_FULL = re.compile(
    r"lohia|chaubepur|vijay|panki|peenya|lohiagroup", re.I
)
SAMPLE_WORKSPACE_URL = "https://trying.stamped.work/"


def load_industry_builder():
    path = SCRIPTS / "build-industry-decks.py"
    code = path.read_text(encoding="utf-8")
    code = code.replace('ROOT = Path("/workspace")', f"ROOT = Path(r{str(ROOT)!r})")
    spec = importlib.util.spec_from_loader("build_industry_decks", loader=None)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    exec(compile(code, str(path), "exec"), mod.__dict__)
    return mod


def sync_client_assets() -> None:
    """Copy OEM + Lohia visuals next to client HTML so assets/ resolves locally."""
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
    print(f"synced assets → {CLIENT_ASSETS}")


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
              <td>Connect read-only · map meters, EMS tags, and bill lines</td>
            </tr>
            <tr>
              <td>Weeks 3-10</td>
              <td>Floor executes prescriptions · weekly reviews</td>
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
    return html


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


def build_full(mod, base: str) -> str:
    from deck_packs.machinery_oem import HERO, HERO_ALT, PACK, SLUG

    mod.PACKS[SLUG] = PACK
    mod.HERO_BY_INDUSTRY[SLUG] = HERO
    mod.HERO_ALT[SLUG] = HERO_ALT
    html = mod.build_one(base, SLUG)
    # Flat file in clients/: assets/ is local; tech is ../tech/
    html = rewrite_client_paths(html, asset_prefix="assets/", tech_prefix="../")
    html = patch_offer_90_day(
        html,
        "Start with one works: electrical POC, two HT bills, and a walkthrough. "
        "Read-only. Kill criteria agreed upfront.",
    )
    html = patch_sample_workspace(html)
    return html


def build_brief(mod, base: str) -> str:
    from deck_packs.lohia_corp_brief import (
        HERO,
        HERO_ALT,
        KEEP_SCENES,
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
    html = inject_vs_audit_scene(html, VS_AUDIT)
    html = patch_offer_brief(html, OFFER_PATCH)
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
    sync_client_assets()

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
    raw = patch_sample_workspace(raw)
    deploy_html = rewrite_client_paths(
        raw, asset_prefix="../assets/", tech_prefix="../../"
    )
    assert_anonymous(deploy_html, deploy_path)
    deploy_path.write_text(deploy_html, encoding="utf-8")
    print(f"wrote {deploy_path} ({len(deploy_html)} bytes)")

    brief = build_brief(mod, base)
    brief_path = CLIENTS / "lohia-corp-brief.html"
    brief_path.write_text(brief, encoding="utf-8")
    if not FORBIDDEN_FULL.search(brief):
        raise SystemExit("brief should contain Lohia naming")
    if 'id="scene-vs-audit"' not in brief:
        raise SystemExit("brief missing vs-audit scene")
    print(f"wrote {brief_path} ({len(brief)} bytes)")

    note = CLIENTS / "README.md"
    note.write_text(
        "# Private client decks\n\n"
        "Not linked from the public cement/steel/pharma hub.\n\n"
        "| File | Use |\n"
        "|------|-----|\n"
        "| [machinery-oem.html](./machinery-oem.html) | Anonymous full Proof Run (packaging-machinery OEM) |\n"
        "| [machinery-oem/](./machinery-oem/) | Optional standalone deploy root |\n"
        "| [lohia-corp-brief.html](./lohia-corp-brief.html) | Short Lohia-branded meeting walkthrough |\n"
        "| [assets/](./assets/) | Co-located images (open HTML from this folder) |\n\n"
        "Rebuild: `python3 scripts/build-client-decks.py`\n",
        encoding="utf-8",
    )
    print("wrote clients/README.md")


if __name__ == "__main__":
    main()
