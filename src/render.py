"""Render src/page.html to entry.png (1024x1024). Build-time only; not run by the grader."""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parent.parent
out = root / "entry.png"
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
    pg.goto((root / "src" / "page.html").as_uri())
    pg.wait_for_timeout(500)
    pg.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": 1024, "height": 1024})
    b.close()
print(out, out.stat().st_size)
