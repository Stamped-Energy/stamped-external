#!/usr/bin/env python3
"""Playwright + naming gates for private client decks."""
from __future__ import annotations

import http.server
import re
import socketserver
import tempfile
import threading
from functools import partial
from pathlib import Path

from playwright.sync_api import sync_playwright

# external/scripts/decks/checks → stamped-external root
ROOT = Path(__file__).resolve().parents[3]
OUT = Path(tempfile.gettempdir()) / "client-deck-audit"
FORBIDDEN = re.compile(r"lohia|chaubepur|vijay|panki|peenya|lohiagroup", re.I)
FORBIDDEN_LNM = re.compile(
    r"\blnm\b|lnmauto|divyansh|sandeep\s+mall|sector\s*59|faridabad", re.I
)

FULL = "demo-decks/clients/machinery-oem.html"
BRIEF = "demo-decks/clients/lohia-corp-brief.html"
FORGE = "demo-decks/clients/auto-forge-ht.html"
LNM = "demo-decks/clients/lnm-auto-faridabad-technical/index.html"

TECH_BRIEF_PREFIX = [
    "scene-title",
    "scene-gap",
    "scene-fit",
    "scene-load",
    "scene-equipment",
    "scene-prescription",
    "scene-agentic",
    "scene-floor",
    "scene-verify",
    "scene-integration",
    "scene-offer",
]
FULL_PREFIX = TECH_BRIEF_PREFIX
BRIEF_PREFIX = TECH_BRIEF_PREFIX
FORGE_PREFIX = TECH_BRIEF_PREFIX


def start_server() -> tuple[socketserver.TCPServer, str]:
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}"


def visible_slides(page) -> list[str]:
    return page.evaluate(
        """() => Array.from(document.querySelectorAll('.slide'))
          .filter((s) => getComputedStyle(s).display !== 'none')
          .map((s) => s.id)"""
    )


def go_to(page, slide_id: str) -> None:
    page.evaluate(
        """(slideId) => {
      const slides = Array.from(document.querySelectorAll('.slide')).filter(
        (s) => getComputedStyle(s).display !== 'none'
      );
      const idx = slides.findIndex((s) => s.id === slideId);
      if (idx < 0) throw new Error('missing ' + slideId);
      const dots = document.querySelectorAll('#dots .dots__dot');
      if (dots[idx]) dots[idx].click();
      else slides.forEach((s, i) => s.classList.toggle('active', i === idx));
    }""",
        slide_id,
    )
    page.wait_for_selector(f"#{slide_id}.active", timeout=5000)


def file_gate() -> list[str]:
    issues: list[str] = []
    full = (ROOT / FULL).read_text(encoding="utf-8")
    brief = (ROOT / BRIEF).read_text(encoding="utf-8")
    forge_path = ROOT / FORGE
    if not forge_path.is_file():
        issues.append(f"missing {FORGE}")
        forge = ""
    else:
        forge = forge_path.read_text(encoding="utf-8")
    hub = (ROOT / "demo-decks/index.html").read_text(encoding="utf-8")
    root_hub = (ROOT / "index.html").read_text(encoding="utf-8")
    clients_hub = ROOT / "demo-decks/clients/index.html"
    if not clients_hub.is_file():
        issues.append("missing demo-decks/clients/index.html picker")
    else:
        ch = clients_hub.read_text(encoding="utf-8")
        if "lohia-corp-brief.html" not in ch or "machinery-oem.html" not in ch:
            issues.append("clients hub missing deck links")
        if "auto-forge-ht.html" not in ch:
            issues.append("clients hub missing auto-forge-ht.html link")
        if "technical-explainer.html" not in ch:
            issues.append("clients hub missing technical-explainer.html link")
        if "itc-nadiad-technical" not in ch:
            issues.append("clients hub missing ITC brief link")
        if "nestle-pantnagar-technical" not in ch:
            issues.append("clients hub missing Nestlé brief link")
        if "lnm-auto-faridabad-technical" not in ch:
            issues.append("clients hub missing LNM Faridabad brief link")
        if "Industry Energy Management" not in ch or "Asset Health Intelligence" not in ch:
            issues.append("clients hub missing website pillar names")
    if 'href="./clients/"' not in hub and 'href="clients/"' not in hub:
        issues.append("demo-decks hub missing Clients link")
    if "demo-decks/clients/" not in root_hub:
        issues.append("repo root hub missing demo-decks/clients/ link")
    hits = sorted(set(FORBIDDEN.findall(full)))
    if hits:
        issues.append(f"full naming gate failed: {hits}")
    if not FORBIDDEN.search(brief):
        issues.append("brief missing Lohia / Chaubepur naming")
    if (
        "plant visit" not in brief.lower()
        and "permission to visit" not in brief.lower()
        and "visit chaubepur" not in brief.lower()
    ):
        issues.append("brief missing on-site / plant-visit ask")
    if "Come to the plant" in brief:
        issues.append("brief still uses punchy AI-style heading: Come to the plant")
    # Allow explicit "will not ask for two HT bills"; block asks that require bills as a gate
    if re.search(
        r"(?:share|send|provide|need)\s+two(?:\s+consecutive)?\s+HT bills",
        brief,
        re.I,
    ):
        issues.append("brief should not gate on two HT bills up front")
    if "60-day proof plan" in brief.lower() or "Chaubepur · 60-day ask" in brief:
        issues.append("brief still uses homework-style 60-day proof-plan ask")
    if "live" not in brief.lower() and "real-time" not in brief.lower():
        issues.append("brief missing live / real-time decision framing")
    if "early warning" not in brief.lower():
        issues.append("brief missing early-warnings framing")
    if "90-day" in brief.lower() or "Day 90" in brief:
        issues.append("brief still mentions 90-day pilot")
    for sid in TECH_BRIEF_PREFIX:
        if f'id="{sid}"' not in brief:
            issues.append(f"brief missing {sid}")
    if 'id="scene-vs-audit"' in brief or 'id="scene-lohia-lines"' in brief:
        issues.append("brief still has Proof Run-only scenes (vs-audit / lohia-lines)")
    for needle in (
        "Woven raffia",
        "Multifilament",
        "Monofilament",
        "Extrusion",
        "Weaving",
        "Coating",
        "Printing",
    ):
        if needle not in brief:
            issues.append(f"brief missing Lohia-specific term: {needle}")
    if re.search(r"\bIIT\b|IITK|Roorkee", brief, re.I):
        issues.append("brief must not mention IIT / IITK / Roorkee (client-facing)")
    if "Energy audit and Stamped" not in brief and "Energy audit vs Stamped" not in brief:
        issues.append("brief missing energy-audit vs Stamped framing")
    if (
        "not another energy audit" not in brief.lower()
        and "not asking for a second energy audit" not in brief.lower()
        and "not an energy-audit replacement" not in brief.lower()
    ):
        issues.append("brief missing explicit not-an-audit framing")
    if "60-day" not in full.lower() and "Day 60" not in full:
        issues.append("full missing 60-day Proof Run framing")
    if "live" not in full.lower() and "real-time" not in full.lower():
        issues.append("full missing live / real-time decision framing")
    if "early warning" not in full.lower():
        issues.append("full missing early-warnings framing")
    if "priced onto the bill" in full:
        issues.append("full still has AI-ish title phrasing: priced onto the bill")
    if "90-day" in full.lower() or "Day 90" in full:
        issues.append("full OEM deck still mentions 90-day pilot (should be 60-day)")
    for sid in TECH_BRIEF_PREFIX:
        if f'id="{sid}"' not in full:
            issues.append(f"full missing {sid}")
    if "hypothesis chip" in full.lower() or "Hypothesis chips" in full:
        issues.append("full still uses AI-ish 'hypothesis chip' language")
    if "hands you a report" in full.lower() or "hands you a report" in brief.lower():
        issues.append("client deck still uses AI-ish audit contrast phrasing")
    if "Signals become work orders" in brief or "On the supervisor's phone." in brief:
        issues.append("brief still has punchy shared-base headings")
    if forge:
        lnm_hits = sorted(set(FORBIDDEN_LNM.findall(forge)))
        if lnm_hits:
            issues.append(f"forge-HT naming gate failed: {lnm_hits}")
        for sid in TECH_BRIEF_PREFIX:
            if f'id="{sid}"' not in forge:
                issues.append(f"forge-HT missing {sid}")
        if "Verified with evidence" not in forge:
            issues.append("forge-HT missing verified-with-evidence framing")
        if "Industry Energy Management" not in forge:
            issues.append("forge-HT missing Industry Energy Management pillar")
        if "Asset Health Intelligence" not in forge:
            issues.append("forge-HT missing Asset Health Intelligence pillar")
        if "Signals become work orders" in forge or "On the supervisor's phone." in forge:
            issues.append("forge-HT still has punchy shared-base headings")
        if 'src="assets/auto-forge-ht/steel-hero.jpg"' not in forge:
            issues.append("forge-HT hero src should be clients-local assets/auto-forge-ht/...")

    lnm_path = ROOT / LNM
    if not lnm_path.is_file():
        issues.append(f"missing {LNM}")
        lnm = ""
    else:
        lnm = lnm_path.read_text(encoding="utf-8")
        for sid in TECH_BRIEF_PREFIX:
            if f'id="{sid}"' not in lnm:
                issues.append(f"lnm missing {sid}")
        if "Industry Energy Management" not in lnm or "Asset Health Intelligence" not in lnm:
            issues.append("lnm missing website pillar names")
        if "₹" not in lnm:
            issues.append("lnm missing ₹ currency")
        if "LNM" not in lnm or "Faridabad" not in lnm or "Sector 59" not in lnm:
            issues.append("lnm missing LNM / Faridabad / Sector 59 naming")
        for needle in ("forge", "machine", "heat treatment", "DHBVN", "precision"):
            if needle.lower() not in lnm.lower():
                issues.append(f"lnm missing precision term: {needle}")
        if 'src="assets/lnm-auto-faridabad-technical/cnc-shop-hero.jpg"' not in lnm:
            issues.append("lnm hero src should be cnc-shop-hero.jpg")
        if re.search(r"\bIIT\b|IITK|Roorkee", lnm, re.I):
            issues.append("lnm must not mention IIT / Roorkee")
        if "divyansh" in lnm.lower() or "sandeep mall" in lnm.lower():
            issues.append("lnm must not name Divyansh / Sandeep on slides")
        lnm_body = re.sub(r"<style[\s\S]*?</style>", "", lnm)
        lnm_body = re.sub(r"<script[\s\S]*?</script>", "", lnm_body)
        if re.search(r"[—–]", lnm_body):
            issues.append("lnm: em/en dash in visible HTML")
        if not (ROOT / "demo-decks/clients/lnm-auto-faridabad-technical/assets/lnm-auto-faridabad-technical/cnc-shop-hero.jpg").is_file():
            issues.append("missing LNM cnc-shop-hero.jpg asset")
    # Co-located assets must resolve next to the HTML
    for rel in (
        "demo-decks/clients/assets/machinery-oem/tape-line.jpg",
        "demo-decks/clients/assets/lohia-corp/tape-extrusion.jpg",
        "demo-decks/clients/assets/lohia-corp/lohia-logo.svg",
        "demo-decks/clients/assets/auto-forge-ht/steel-hero.jpg",
    ):
        if not (ROOT / rel).is_file():
            issues.append(f"missing co-located asset: {rel}")
    if 'src="assets/machinery-oem/tape-line.jpg"' not in full:
        issues.append("full hero src should be clients-local assets/...")
    if 'src="assets/lohia-corp/tape-extrusion.jpg"' not in brief:
        issues.append("brief hero src should be clients-local assets/...")
    # no em dash / en dash in user-facing copy
    for label, html in (("full", full), ("brief", brief), ("forge", forge)):
        if not html:
            continue
        body = re.sub(r"<style[\s\S]*?</style>", "", html)
        body = re.sub(r"<script[\s\S]*?</script>", "", body)
        if re.search(r"[—–]", body):
            issues.append(f"{label}: em/en dash in visible HTML")

    nestle_path = ROOT / "demo-decks/clients/nestle-pantnagar-technical/index.html"
    if not nestle_path.is_file():
        issues.append("missing Nestlé Pantnagar technical brief")
    else:
        nestle = nestle_path.read_text(encoding="utf-8")
        if "rupee" not in nestle.lower():
            issues.append("nestle missing rupee(s) spelling")
        nestle_body = re.sub(r"<style[\s\S]*?</style>", "", nestle)
        nestle_body = re.sub(r"<script[\s\S]*?</script>", "", nestle_body)
        if "₹" in nestle_body:
            issues.append("nestle visible copy should keep rupee(s), not ₹")
        if "Industry Energy Management" not in nestle or "Asset Health Intelligence" not in nestle:
            issues.append("nestle missing website pillar names")
        if re.search(r"[—–]", nestle_body):
            issues.append("nestle: em/en dash in visible HTML")

    banned = (
        "pay-as-you-save",
        "Signals become work orders",
        "Load & Energy Efficiency",
        "Prescriptive Equipment Intelligence",
        "priced onto the bill",
    )
    meeting_decks = (
        "demo-decks/cement.html",
        "demo-decks/steel.html",
        "demo-decks/pharma.html",
        "demo-decks/clients/technical-explainer.html",
        "demo-decks/clients/itc-nadiad-technical/index.html",
        "demo-decks/clients/itc-nadiad-technical.html",
        "demo-decks/clients/nestle-pantnagar-technical/index.html",
        LNM,
        FULL,
        BRIEF,
        FORGE,
    )
    for rel in meeting_decks:
        path = ROOT / rel
        if not path.is_file():
            issues.append(f"missing meeting deck: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in banned:
            if needle in text:
                issues.append(f"{rel}: banned phrase {needle!r}")
    return issues


def audit(page, base: str, deck: str, label: str, width: int, height: int, prefix: list[str]) -> list[str]:
    issues: list[str] = []
    page.set_viewport_size({"width": width, "height": height})
    page.goto(f"{base}/{deck}", wait_until="networkidle")
    slides = visible_slides(page)
    if slides[: len(prefix)] != prefix:
        issues.append(f"{label}: order={slides[: len(prefix)+1]} expected={prefix}")

    hero = page.evaluate(
        """() => {
      const img = document.getElementById('heroPhotoImg');
      if (!img) return {ok:false, reason:'no hero'};
      return {ok: img.complete && img.naturalWidth > 0, src: img.currentSrc || img.src, nw: img.naturalWidth};
    }"""
    )
    if not hero.get("ok"):
        issues.append(f"{label}: hero failed {hero}")

    for sid in slides:
        go_to(page, sid)
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT / f"{label}_{sid}.png"), full_page=False)
        overflow = page.evaluate(
            """(slideId) => {
      const slide = document.getElementById(slideId);
      const vw = window.innerWidth;
      const problems = [];
      slide.querySelectorAll('h1,h2,h3,p,li,td,th,button,a,.chip,.lede,.eyebrow').forEach((el) => {
        const t = (el.textContent || '').trim();
        if (!t) return;
        const r = el.getBoundingClientRect();
        if (r.width < 2 || r.height < 2) return;
        if (getComputedStyle(el).visibility === 'hidden') return;
        if (r.right > vw + 2) problems.push(el.tagName + ':' + t.slice(0, 40));
      });
      return problems;
    }""",
            sid,
        )
        for p in overflow:
            issues.append(f"{label}/{sid}: overflow {p}")

    if "scene-floor" in slides:
        go_to(page, "scene-floor")
        t0 = page.locator("#floorTitle").inner_text()
        page.locator("#floorAck").click()
        page.wait_for_timeout(350)
        if page.locator("#floorTitle").inner_text() == t0:
            issues.append(f"{label}: floor ack did not advance")

    if deck.endswith("machinery-oem.html") and "scene-tech" in slides:
        go_to(page, "scene-tech")
        href = page.locator('a.tech-card[href*="physics"]').get_attribute("href") or ""
        if "from=machinery-oem" not in href:
            issues.append(f"{label}: tech card missing from=machinery-oem ({href})")
        if not href.startswith("../tech/"):
            issues.append(f"{label}: tech card path should be ../tech/ ({href})")

    if deck.endswith("machinery-oem.html") and "scene-live" in slides and width > 720:
        go_to(page, "scene-live")
        open_btn = page.locator("#openSampleWorkspace")
        if open_btn.count() != 1:
            issues.append(f"{label}: missing Open workspace button")
        else:
            href = open_btn.get_attribute("href") or ""
            if "trying.stamped.work" not in href:
                issues.append(f"{label}: Open workspace href={href!r}")
            frame_src = page.locator("#dashFrame").get_attribute("src") or page.locator("#dashFrame").get_attribute("data-src") or ""
            if "trying.stamped.work" not in frame_src:
                issues.append(f"{label}: dashFrame src={frame_src!r}")

    if deck.endswith("lohia-corp-brief.html") and "scene-offer" in slides:
        go_to(page, "scene-offer")
        body = page.locator("#scene-offer").inner_text()
        if re.search(r"\bIIT\b|IITK|Roorkee", body, re.I):
            issues.append(f"{label}: offer slide must not mention IIT / Roorkee")
        if "energy audit" not in body.lower():
            issues.append(f"{label}: offer slide missing audit contrast")
        if "Stamped" not in body:
            issues.append(f"{label}: offer slide missing Stamped side")
        if "Chaubepur" not in body and "visit" not in body.lower():
            issues.append(f"{label}: offer slide missing Chaubepur visit ask")

    if deck.endswith("auto-forge-ht.html") and "scene-fit" in slides:
        go_to(page, "scene-fit")
        body = page.locator("#scene-fit").inner_text()
        if FORBIDDEN_LNM.search(body):
            issues.append(f"{label}: fit slide must stay anonymous")

    if deck.endswith("auto-forge-ht.html") and "scene-load" in slides:
        go_to(page, "scene-load")
        body = page.locator("#scene-load").inner_text()
        if "energy" not in body.lower():
            issues.append(f"{label}: load slide missing energy framing")

    if deck.endswith("auto-forge-ht.html") and "scene-equipment" in slides:
        go_to(page, "scene-equipment")
        body = page.locator("#scene-equipment").inner_text()
        if "equipment" not in body.lower() and "asset" not in body.lower():
            issues.append(f"{label}: equipment slide missing asset-health framing")

    return issues


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    all_issues = file_gate()
    httpd, base = start_server()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for label, deck, prefix, w, h in [
                ("full-desktop", FULL, FULL_PREFIX, 1440, 900),
                ("full-mobile", FULL, FULL_PREFIX, 390, 844),
                ("brief-desktop", BRIEF, BRIEF_PREFIX, 1440, 900),
                ("brief-mobile", BRIEF, BRIEF_PREFIX, 390, 844),
                ("forge-desktop", FORGE, FORGE_PREFIX, 1440, 900),
                ("forge-mobile", FORGE, FORGE_PREFIX, 390, 844),
            ]:
                page = browser.new_page()
                all_issues += audit(page, base, deck, label, w, h, prefix)
                page.close()
            browser.close()
    finally:
        httpd.shutdown()

    if all_issues:
        print("ISSUES:")
        for i in all_issues:
            print(" -", i)
        raise SystemExit(1)
    print("OK: client decks passed naming + Playwright gates")
    print(f"screenshots: {OUT}")


if __name__ == "__main__":
    main()
