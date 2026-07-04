"""Process the official DISK tag logo into sticker-ready files.

Usage: python3 stickers/process_disk_logo.py <path-to-logo.png>

Outputs (stickers/final/):
  05_disk_tag_transparent.png   black tag, exterior background removed,
                                white letter fills PRESERVED (flood fill
                                from the borders, not color-keying)
  05_disk_tag_STICKER.png       die-cut look: thick white keyline around
                                the tag + barcode / HP-7 lockup beneath
  05_disk_tag_INVERTED.png      white-on-black variant for dark surfaces
"""
import sys, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

SRC = sys.argv[1]
OUT = "/home/user/osiris-motion-comic/stickers/final"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

im = Image.open(SRC).convert("RGB")
g = np.array(im.convert("L"))
h, w = g.shape

# --- exterior detection: BFS flood fill from all border pixels through light areas
light = g > 200
exterior = np.zeros_like(light, bool)
stack = [(0, x) for x in range(w) if light[0, x]] + \
        [(h-1, x) for x in range(w) if light[h-1, x]] + \
        [(y, 0) for y in range(h) if light[y, 0]] + \
        [(y, w-1) for y in range(h) if light[y, w-1]]
for y, x in stack: exterior[y, x] = True
while stack:
    y, x = stack.pop()
    for ny, nx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
        if 0 <= ny < h and 0 <= nx < w and light[ny, nx] and not exterior[ny, nx]:
            exterior[ny, nx] = True
            stack.append((ny, nx))

alpha = np.where(exterior, 0, 255).astype(np.uint8)
alpha = np.array(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(1)))

# 1) transparent original
rgba = np.dstack([np.array(im), alpha])
Image.fromarray(rgba, "RGBA").save(f"{OUT}/05_disk_tag_transparent.png")

# 2) white-keyline die-cut + barcode lockup
KEY = max(10, w // 55)
mask = Image.fromarray(alpha)
for _ in range(4):
    mask = mask.filter(ImageFilter.MaxFilter(2 * (KEY // 4) + 1))
pad, bar_h = KEY * 3, max(70, h // 9)
cw, ch = w + pad * 2, h + pad * 2 + bar_h + 40
canvas = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
white = Image.new("RGBA", (w, h), (255, 255, 255, 255)); white.putalpha(mask)
canvas.paste(white, (pad, pad), white)
tag = Image.fromarray(rgba, "RGBA")
canvas.paste(tag, (pad, pad), tag)
d = ImageDraw.Draw(canvas)
bx, by = pad + KEY, pad + h + 20
random.seed(4)
end_x = pad + int(w * 0.62)
while bx < end_x:
    bw = random.choice([3, 3, 5, 5, 8, 11])
    d.rectangle([bx, by, bx + bw, by + bar_h], fill=(10, 10, 10, 255))
    bx += bw + random.choice([4, 5, 7])
f = ImageFont.truetype(MONO, max(24, bar_h // 2))
d.text((pad + int(w * 0.66), by + bar_h // 2), "HP-7 // HUMBOLDT-PARK",
       font=f, fill=(10, 10, 10, 255), anchor="lm")
# white plate behind the lockup row so it die-cuts as one piece
plate = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
ImageDraw.Draw(plate).rounded_rectangle(
    [pad, pad + h + 8, pad + w, by + bar_h + 16], radius=18, fill=(255, 255, 255, 255))
out2 = Image.alpha_composite(plate, canvas)
out2.save(f"{OUT}/05_disk_tag_STICKER.png")

# 3) inverted white-on-black
inv = np.array(im); inv = 255 - inv
rgba_inv = np.dstack([inv, alpha])
Image.fromarray(rgba_inv, "RGBA").save(f"{OUT}/05_disk_tag_INVERTED.png")
print("done: transparent / STICKER / INVERTED")
