#!/usr/bin/env python3
"""Extract rx-action + phone prescription titles from demo-decks into JSON-ish stdout."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3] / "demo-decks"
OUT = Path(__file__).resolve().parents[3] / "copy" / "prescriptions" / "_extracted.json"

RX_ACTION = re.compile(
    r'<p class="rx-action"[^>]*>(.*?)</p>', re.I | re.S
)
RX_BADGE = re.compile(
    r'<span class="rx-badge"[^>]*>(.*?)</span>.*?<p class="rx-action"[^>]*>(.*?)</p>',
    re.I | re.S,
)
PHONE_TITLE = re.compile(
    r'class="(?:phone-rx__title|phone-card__title|floor-rx__title)"[^>]*>(.*?)<',
    re.I | re.S,
)
# Nestlé-style phone slides often use <strong> or h3 inside phone
PHONE_H = re.compile(
    r'<div class="phone(?:-rx|-card)?[^"]*"[^>]*>.*?<h[34][^>]*>(.*?)</h[34]>',
    re.I | re.S,
)
WHY = re.compile(
    r'<p class="rx-action"[^>]*>.*?</p>.*?<div class="rx-row"><dt>Why</dt><dd[^>]*>(.*?)</dd>',
    re.I | re.S,
)


def strip_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = (
        s.replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&nbsp;", " ")
        .replace("&#39;", "'")
        .replace("&quot;", '"')
    )
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main() -> None:
    files = sorted(ROOT.glob("*.html")) + sorted(ROOT.glob("clients/**/*.html"))
    rows: list[dict] = []
    seen: set[str] = set()
    for f in files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        rel = str(f.relative_to(ROOT)).replace("\\", "/")
        for m in RX_ACTION.finditer(text):
            title = strip_html(m.group(1))
            if len(title) < 8 or title.lower() in seen:
                continue
            seen.add(title.lower())
            start = max(0, m.start() - 400)
            chunk = text[start : m.end() + 800]
            badge_m = re.search(r'<span class="rx-badge"[^>]*>(.*?)</span>', chunk, re.I | re.S)
            why_m = re.search(r'<dt>Why</dt><dd[^>]*>(.*?)</dd>', chunk, re.I | re.S)
            impact_m = re.search(r'<dt>Impact</dt><dd[^>]*>(.*?)</dd>', chunk, re.I | re.S)
            rows.append(
                {
                    "title": title,
                    "badge": strip_html(badge_m.group(1)) if badge_m else "",
                    "why": strip_html(why_m.group(1)) if why_m else "",
                    "impact": strip_html(impact_m.group(1)) if impact_m else "",
                    "source": rel,
                    "kind": "rx-card",
                }
            )
        for m in PHONE_TITLE.finditer(text):
            title = strip_html(m.group(1))
            key = title.lower()
            if len(title) < 8 or key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "title": title,
                    "badge": "Floor phone",
                    "why": "",
                    "impact": "",
                    "source": rel,
                    "kind": "phone",
                }
            )
        # Floor phone payloads embedded as window.__FLOOR_RX__ = [...]
        fm = re.search(r"window\.__FLOOR_RX__\s*=\s*(\[[\s\S]*?\]);", text)
        if fm:
            try:
                payload = json.loads(fm.group(1))
            except json.JSONDecodeError:
                payload = []
            if isinstance(payload, list):
                for item in payload:
                    if not isinstance(item, dict):
                        continue
                    title = str(item.get("title") or "").strip()
                    if len(title) < 8 or title.lower() in seen:
                        continue
                    seen.add(title.lower())
                    rows.append(
                        {
                            "title": title,
                            "badge": f"Floor · {item.get('priority', '')}".strip(" ·"),
                            "why": str(item.get("why") or ""),
                            "impact": str(item.get("impact") or ""),
                            "source": rel,
                            "kind": "floor-rx",
                        }
                    )
    OUT.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(rows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
