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
    hits = sorted(set(FORBIDDEN.findall(full)))
    if hits:
        issues.append(f"full naming gate failed: {hits}")
    if not FORBIDDEN.search(brief):
        issues.append("brief missing Lohia / Chaubepur naming")
    if "Chaubepur · 90-day ask" not in brief and "90-day ask" not in brief:
        issues.append("brief missing Chaubepur 90-day ask")
    if 'id="scene-vs-audit"' not in brief:
        issues.append("brief missing scene-vs-audit")
    if "IIT Kanpur" not in brief and "IITK" not in brief:
        issues.append("brief missing IIT Kanpur audit differentiation")
    if "Not another energy audit" not in brief and "not a second audit" not in brief.lower():
        issues.append("brief missing explicit not-an-audit framing")
    if "90-day proof run" not in full:
        issues.append("full missing 90-day proof run framing")
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
        if "IIT Kanpur" not in body and "IITK" not in body:
            issues.append(f"{label}: vs-audit slide missing IIT Kanpur mention")
        if "audit" not in body.lower():
            issues.append(f"{label}: vs-audit slide missing audit contrast")

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
