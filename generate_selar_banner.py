#!/usr/bin/env python3
"""
ICTZoid — Selar Product Banner
300 × 300 px (rendered at 2× then downsampled for crispness)
"""
from PIL import Image, ImageDraw, ImageFont
import math, os

OUT = "/Users/samuel/Documents/Projects/lms/course-format/images/campaign/selar_banner.png"

_FB  = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
_FR  = "/System/Library/Fonts/Supplemental/Arial.ttf"
_FBK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
S = 2  # render at 2×

W, H = 300, 300

def fb(pt):  return ImageFont.truetype(_FB,  pt * S)
def fr(pt):  return ImageFont.truetype(_FR,  pt * S)
def fbk(pt): return ImageFont.truetype(_FBK, pt * S)

# ── Palette ──────────────────────────────────────────────────────────────────
BG1    = (8,   12,  26)
BG2    = (15,  22,  46)
CYAN   = (0,   212, 255)
GREEN  = (34,  197, 94)
WHITE  = (248, 250, 252)
GRAY   = (148, 163, 184)
DGRAY  = (30,  41,  59)

def blend(a, b, t):
    return tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))

def dim(acc, t=0.18):
    return blend(BG2, acc, t)

# ── Canvas ───────────────────────────────────────────────────────────────────
img = Image.new("RGB", (W * S, H * S))
d   = ImageDraw.Draw(img)

# Vertical gradient background
for y in range(H * S):
    t = y / max(H * S - 1, 1)
    c = tuple(int(BG1[i] + (BG2[i] - BG1[i]) * t) for i in range(3))
    d.line([(0, y), (W * S, y)], fill=c)

# ── Decorative grid dots (background texture) ────────────────────────────────
for gx in range(0, W * S, 28 * S // 2):
    for gy in range(0, H * S, 28 * S // 2):
        d.ellipse([gx - S, gy - S, gx + S, gy + S], fill=dim(CYAN, 0.12))

# ── Top accent bar ────────────────────────────────────────────────────────────
d.rectangle([0, 0, W * S, 5 * S], fill=CYAN)

# ── Glowing orb (centre-left decorative element) ─────────────────────────────
ox, oy = 68 * S, 148 * S
for r, t in [(70*S, 0.04), (50*S, 0.07), (32*S, 0.13), (18*S, 0.25), (8*S, 0.55)]:
    d.ellipse([ox-r, oy-r, ox+r, oy+r], fill=dim(CYAN, t))

# ── Stacked course pills (right side decoration) ─────────────────────────────
courses = ["HTML", "CSS", "JS", "React", "AI"]
accents = [CYAN, CYAN, CYAN, CYAN, GREEN]
pill_w, pill_h = 66 * S, 20 * S
pill_r  = 5 * S
pill_x  = 212 * S
pill_y0 = 76 * S
gap     = 25 * S

for i, (label, acc) in enumerate(zip(courses, accents)):
    y0 = pill_y0 + i * (pill_h + gap - 4)
    y1 = y0 + pill_h

    # pill background
    def rrect_simple(x0, y0, x1, y1, r, fill):
        r = int(r)
        d.rectangle([x0+r, y0, x1-r, y1], fill=fill)
        d.rectangle([x0, y0+r, x1, y1-r], fill=fill)
        for cx, cy in [(x0,y0),(x1-2*r,y0),(x0,y1-2*r),(x1-2*r,y1-2*r)]:
            d.ellipse([cx, cy, cx+2*r, cy+2*r], fill=fill)

    rrect_simple(pill_x, y0, pill_x + pill_w, y1, pill_r, dim(acc, 0.22))

    # pill border
    d.rectangle([pill_x,              y0, pill_x + pill_w, y0 + S],    fill=dim(acc, 0.5))
    d.rectangle([pill_x,              y1 - S, pill_x + pill_w, y1],    fill=dim(acc, 0.5))
    d.rectangle([pill_x,              y0, pill_x + S,          y1],    fill=dim(acc, 0.5))
    d.rectangle([pill_x + pill_w - S, y0, pill_x + pill_w,     y1],    fill=dim(acc, 0.5))

    # label
    pf  = fr(9)
    tw  = int(d.textlength(label, font=pf))
    tx  = pill_x + (pill_w - tw) // 2
    ty  = y0 + (pill_h - pf.size) // 2
    d.text((tx, ty), label, font=pf, fill=acc)

# ── Main text ─────────────────────────────────────────────────────────────────
lx = 18 * S

# Brand name
brand_f = fb(9)
d.text((lx, 16 * S), "ICTZoid", font=brand_f, fill=CYAN)

# Program type tag
tag    = "WEB DEVELOPMENT"
tag_f  = fr(7)
tw     = int(d.textlength(tag, font=tag_f))
tag_px, tag_py, tag_r = 8 * S, 4 * S, 4 * S
tx0, ty0 = lx, 34 * S
tx1, ty1 = tx0 + tw + 2*tag_px, ty0 + tag_f.size + 2*tag_py
# pill bg
d.rectangle([tx0 + tag_r, ty0, tx1 - tag_r, ty1], fill=dim(CYAN, 0.14))
d.rectangle([tx0, ty0 + tag_r, tx1, ty1 - tag_r], fill=dim(CYAN, 0.14))
for ccx, ccy in [(tx0,ty0),(tx1-2*tag_r,ty0),(tx0,ty1-2*tag_r),(tx1-2*tag_r,ty1-2*tag_r)]:
    d.ellipse([ccx, ccy, ccx+2*tag_r, ccy+2*tag_r], fill=dim(CYAN, 0.14))
d.text((tx0 + tag_px, ty0 + tag_py), tag, font=tag_f, fill=dim(CYAN, 0.9))

# Headline — "PROGRAM"
hl1_f = fbk(28)
d.text((lx, 62 * S), "PROGRAM", font=hl1_f, fill=WHITE)

# Sub-headline line
sub_f = fb(10)
d.text((lx, 118 * S), "6 Courses · 2 Master Sessions", font=sub_f, fill=GRAY)
d.text((lx, 133 * S), "85+ Lessons · Certificate",     font=sub_f, fill=GRAY)

# ── Divider line ──────────────────────────────────────────────────────────────
d.line([(lx, 152 * S), (200 * S, 152 * S)], fill=DGRAY, width=S)

# ── Feature bullets ───────────────────────────────────────────────────────────
features = [
    ("✓", "HTML, CSS, JavaScript"),
    ("✓", "React + Tailwind"),
    ("✓", "AI (Claude & GPT-4o)"),
    ("✓", "Git & GitHub CI/CD"),
]
bul_f = fr(9)
by    = 162 * S
for icon, text in features:
    d.text((lx,          by), icon, font=bul_f, fill=GREEN)
    d.text((lx + 14 * S, by), text, font=bul_f, fill=GRAY)
    by += 19 * S

# ── Bottom bar ────────────────────────────────────────────────────────────────
bar_y = 267 * S
d.rectangle([0, bar_y, W * S, H * S], fill=dim(CYAN, 0.08))
d.line([(0, bar_y), (W * S, bar_y)], fill=dim(CYAN, 0.25), width=S)

# "Enrol now" CTA
cta_f  = fb(9)
cta    = "Enrol Now"
ctw    = int(d.textlength(cta, font=cta_f))
cta_x  = (W * S - ctw) // 2
d.text((cta_x, bar_y + 10 * S), cta, font=cta_f, fill=CYAN)

# ── Bottom accent bar ─────────────────────────────────────────────────────────
d.rectangle([0, H * S - 4 * S, W * S, H * S], fill=CYAN)

# ── Export ────────────────────────────────────────────────────────────────────
out = img.resize((W, H), Image.LANCZOS)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
out.save(OUT, quality=97)
print(f"Saved: {OUT}  ({W}×{H} px)")
