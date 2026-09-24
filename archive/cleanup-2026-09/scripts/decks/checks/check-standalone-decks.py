#!/usr/bin/env python3
"""Static + Playwright gates for standalone decks, hubs, and tech pages."""
from __future__ import annotations

import filecmp
import http.server
import socketserver
import tempfile
import threading
from functools import partial
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(tempfile.gettempdir()) / "standalone-deck-audit"

FORBIDDEN = (
    "Agentic decision layer",
    "Foundation models",
    "Agentic prescriptions",
    "ML spots the issue",
    "Gurugram RFP",
    "model conf 0.",
)

SCAN_PATHS = (
    "demo-decks/prescriptions-examples.html",
    "demo-decks/clients/technical-explainer.html",
    "demo-decks/clients/itc-nadiad-technical.html",
    "demo-decks/clients/itc-nadiad-technical/index.html",
    "demo-decks/clients/nestle-pantnagar-technical/index.html",
    "demo-decks/tech/physics.html",
    "demo-decks/tech/models.html",
    "demo-decks/tech/agents.html",
    "demo-decks/tech/evidence.html",
    "demo-decks/index.html",
    "demo-decks/clients/index.html",
    "index.html",
)

PAGES = (
    "demo-decks/prescriptions-examples.html",
    "demo-decks/clients/technical-explainer.html",
    "demo-decks/clients/itc-nadiad-technical.html",
    "demo-decks/clients/nestle-pantnagar-technical/index.html",
    "demo-decks/tech/physics.html",
    "demo-decks/tech/models.html",
    "demo-decks/tech/agents.html",
    "demo-decks/tech/evidence.html",
    "demo-decks/index.html",
    "demo-decks/clients/index.html",
    "index.html",
)

CONTROL_SEL = ", ".join(
    (
        ".nav-btn",
        ".btn",
        ".topbar__back",
        ".topbar__brand",
        ".nav-pills a",
        ".action-btn",
        ".chip[role='tab']",
        ".pipe-node",
        "a.card",
    )
)


def start_server() -> tuple[socketserver.TCPServer, str]:
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    httpd = socketserver.TCPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    return httpd, f"http://127.0.0.1:{httpd.server_address[1]}"


def file_gate() -> list[str]:
    issues: list[str] = []
    itc = ROOT / "demo-decks/clients/itc-nadiad-technical.html"
    itc_folder = ROOT / "demo-decks/clients/itc-nadiad-technical/index.html"
    if not filecmp.cmp(itc, itc_folder, shallow=False):
        issues.append("ITC flat and folder copies are not byte-identical")

    explainer = (ROOT / "demo-decks/clients/technical-explainer.html").read_text(
        encoding="utf-8"
    )
    if "Feasibility and ownership checks" not in explainer:
        issues.append("technical explainer missing feasibility pipeline label")

    for rel in SCAN_PATHS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in FORBIDDEN:
            if needle in text:
                issues.append(f"{rel}: leftover copy {needle!r}")
    return issues


def check_page(page, base: str, path: str) -> None:
    page.set_viewport_size({"width": 390, "height": 844})
    page.goto(f"{base}/{path}", wait_until="networkidle")
    h1 = page.locator("h1").first
    assert h1.is_visible(), f"{path}: h1 not visible on mobile"

    overflow = page.evaluate("() => document.documentElement.scrollWidth > window.innerWidth + 1")
    assert not overflow, f"{path}: horizontal overflow on mobile"

    controls = page.evaluate(
        f"""() => Array.from(document.querySelectorAll({CONTROL_SEL!r}))
          .filter((el) => {{
            const cs = getComputedStyle(el);
            return cs.display !== 'none' && cs.visibility !== 'hidden';
          }})
          .map((el) => ({{
            tag: el.tagName.toLowerCase(),
            cls: el.className,
            h: Math.round(el.getBoundingClientRect().height),
          }}))"""
    )
    short = [c for c in controls if c["h"] < 44]
    assert not short, f"{path}: controls below 44px {short}"

    OUT.mkdir(parents=True, exist_ok=True)
    slug = path.replace("/", "_").replace(".html", "")
    page.screenshot(path=str(OUT / f"{slug}-390.png"), full_page=False)

    page.set_viewport_size({"width": 1440, "height": 900})
    page.reload(wait_until="networkidle")
    assert page.locator("h1").first.is_visible(), f"{path}: h1 not visible on desktop"
    page.screenshot(path=str(OUT / f"{slug}-1440.png"), full_page=False)
    print(f"OK {path}")


def main() -> None:
    issues = file_gate()
    if issues:
        raise SystemExit("standalone file gate failed:\n- " + "\n- ".join(issues))

    httpd, base = start_server()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            for path in PAGES:
                check_page(page, base, path)
            browser.close()
        print("STANDALONE_DECK_AUDIT_PASSED")
        print(f"screenshots: {OUT}")
    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()
