from pathlib import Path

from PIL import Image

for p in Path("AppPresets").rglob("preview.png"):
    img = Image.open(p).convert("RGBA")
    img.thumbnail((256, 256), Image.LANCZOS)  # pyright: ignore
    img.save(p, optimize=True, compress_level=9)
