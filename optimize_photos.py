#!/usr/bin/env python3
"""Make web-sized copies of the gallery photos.

The originals are 2-4 MB each, which is far too heavy to load on a page.
This writes resized, re-encoded copies into assets/pics/<name>/web/ and
leaves the originals untouched.

Run:  python3 optimize_photos.py
"""

from pathlib import Path

from PIL import Image

MAX_W, MAX_H = 1400, 1400
QUALITY = 82


def main():
    root = Path("assets/pics")
    for src in sorted(root.glob("*/*.jpg")):
        if src.parent.name == "web":
            continue
        out_dir = src.parent / "web"
        out_dir.mkdir(exist_ok=True)

        with Image.open(src) as im:
            im = im.convert("RGB")
            before = src.stat().st_size
            im.thumbnail((MAX_W, MAX_H), Image.LANCZOS)
            dst = out_dir / src.name
            im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)

        after = dst.stat().st_size
        print(
            f"{src}  {before // 1024} KB -> {dst}  {after // 1024} KB"
            f"  ({im.size[0]}x{im.size[1]})"
        )


if __name__ == "__main__":
    main()
