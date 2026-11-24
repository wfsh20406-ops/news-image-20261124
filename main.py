"""make.fun entry: one image summing up the world news of Tuesday 24 November 2026.

The image (entry.png) is pre-rendered from src/page.html and committed to this
repository. This program only copies it, byte for byte, to /output/entry.png,
so every run writes identical bytes and needs no network.
"""
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
OUT = Path("/output/entry.png")

OUT.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT)
