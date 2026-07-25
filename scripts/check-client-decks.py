#!/usr/bin/env python3
"""Playwright + naming gates for private client decks."""
from __future__ import annotations

import http.server
import re
import socketserver
import threading
from functools import partial
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = Path("/tmp/client-deck-audit")
FORBIDDEN = re.compile(r"lohia|chaubepur|vijay|panki|peenya|lohiagroup", re.I)

FULL = "demo-decks/clients/machinery-oem.html"
BRIEF = "demo-decks/clients/lohia-corp-brief.html"

FULL_PREFIX = [
    "scene-title",
    "scene-hook",
    "scene-math",
    "scene-what",
    "scene-prescription",
    "scene-floor",
    "scene-verify",
    "scene-tech",
]
BRIEF_PREFIX = [
    "scene-title",
    "scene-hook",
    "scene-lohia-lines",
    "scene-math",
    "scene-what",
    "scene-prescription",
    "scene-floor",
    "scene-verify",
    "scene-vs-audit",
    "scene-offer",
]


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
    hub = (ROOT / "demo-decks/index.html").read_text(encoding="utf-8")
    root_hub = (ROOT / "index.html").read_text(encoding="utf-8")
    clients_hub = ROOT / "demo-decks/clients/index.html"
    if not clients_hub.is_file():
        issues.append("missing demo-decks/clients/index.html picker")
    else:
        ch = clients_hub.read_text(encoding="utf-8")
        if "lohia-corp-brief.html" not in ch or "machinery-oem.html" not in ch:
            issues.append("clients hub missing deck links")
    if 'href="./clients/"' not in hub and 'href="clients/"' not in hub:
        issues.append("demo-decks hub missing Clients link")
    if "demo-decks/clients/" not in root_hub:
        issues.append("repo root hub missing demo-decks/clients/ link")
    hits = sorted(set(FORBIDDEN.findall(full)))
    if hits:
        issues.append(f"full naming gate failed: {hits}")
    if not FORBIDDEN.search(brief):
        issues.append("brief missing Lohia / Chaubepur naming")
    if "Come to the plant" not in brief and "permission to come" not in brief.lower():
        issues.append("brief missing on-site / plant-visit ask")
    # Allow explicit "will not ask for two HT bills"; block asks that require bills as a gate
    if re.search(
        r"(?:share|send|provide|need)\s+two(?:\s+consecutive)?\s+HT bills",
        brief,
        re.I,
    ):
        issues.append("brief should not gate on two HT bills up front")
    if "60-day proof plan" in brief.lower() or "Chaubepur · 60-day ask" in brief:
        issues.append("brief still uses homework-style 60-day proof-plan ask")
    if "real-time" not in brief.lower():
        issues.append("brief missing real-time decision framing")
    if "Early warnings" not in brief and "early warning" not in brief.lower():
        issues.append("brief missing early-warnings framing")
    if "90-day" in brief.lower() or "Day 90" in brief:
        issues.append("brief still mentions 90-day pilot")
    if 'id="scene-vs-audit"' not in brief:
        issues.append("brief missing scene-vs-audit")
    if 'id="scene-lohia-lines"' not in brief:
        issues.append("brief missing scene-lohia-lines")
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
    if "Energy audit vs Stamped" not in brief:
        issues.append("brief missing energy-audit vs Stamped framing")
    if "Not another energy audit" not in brief and "not another energy audit" not in brief.lower():
        issues.append("brief missing explicit not-an-audit framing")
    if "60-day" not in full.lower() and "Day 60" not in full:
        issues.append("full missing 60-day Proof Run framing")
    if "real-time" not in full.lower():
        issues.append("full missing real-time decision framing")
    if "Early warnings" not in full and "early warning" not in full.lower():
        issues.append("full missing early-warnings framing")
    if "90-day" in full.lower() or "Day 90" in full:
        issues.append("full OEM deck still mentions 90-day pilot (should be 60-day)")
    if "trying.stamped.work" not in full:
        issues.append("full missing trying.stamped.work sample workspace")
    if 'id="openSampleWorkspace"' not in full:
        issues.append("full missing Open workspace button")
    # Co-located assets must resolve next to the HTML
    for rel in (
        "demo-decks/clients/assets/machinery-oem/tape-line.jpg",
        "demo-decks/clients/assets/lohia-corp/tape-extrusion.jpg",
        "demo-decks/clients/assets/lohia-corp/lohia-logo.svg",
    ):
        if not (ROOT / rel).is_file():
            issues.append(f"missing co-located asset: {rel}")
    if 'src="assets/machinery-oem/tape-line.jpg"' not in full:
        issues.append("full hero src should be clients-local assets/...")
    if 'src="assets/lohia-corp/tape-extrusion.jpg"' not in brief:
        issues.append("brief hero src should be clients-local assets/...")
    # no em dash / en dash in user-facing copy
    for label, html in (("full", full), ("brief", brief)):
        body = re.sub(r"<style[\s\S]*?</style>", "", html)
        body = re.sub(r"<script[\s\S]*?</script>", "", body)
        if re.search(r"[—–]", body):
            issues.append(f"{label}: em/en dash in visible HTML")
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

    if deck.endswith("lohia-corp-brief.html") and "scene-vs-audit" in slides:
        go_to(page, "scene-vs-audit")
        body = page.locator("#scene-vs-audit").inner_text()
        if re.search(r"\bIIT\b|IITK|Roorkee", body, re.I):
            issues.append(f"{label}: vs-audit slide must not mention IIT / Roorkee")
        if "Generic energy audit" not in body and "energy audit" not in body.lower():
            issues.append(f"{label}: vs-audit slide missing audit contrast")
        if "Stamped" not in body:
            issues.append(f"{label}: vs-audit slide missing Stamped side")

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
