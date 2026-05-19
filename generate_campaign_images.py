#!/usr/bin/env python3
"""
ICTZoid Campaign — Visual Image Generator
Images are graphic illustrations only. Text is posted alongside separately.
"""
from PIL import Image, ImageDraw, ImageFont
import os, math, random

ROOT = "/Users/samuel/Documents/Projects/lms/course-format/images/campaign"
for sub in ("whatsapp","instagram","twitter","linkedin"):
    os.makedirs(f"{ROOT}/{sub}", exist_ok=True)

_FBLK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
_FB   = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
_FR   = "/System/Library/Fonts/Supplemental/Arial.ttf"
S = 2  # render at 2x, downsample for smooth edges

def fbb(pt): return ImageFont.truetype(_FBLK, pt*S)
def fb(pt):  return ImageFont.truetype(_FB,   pt*S)
def fr(pt):  return ImageFont.truetype(_FR,   pt*S)

BG1    = (8,  12,  26)
BG2    = (15, 22,  46)
CYAN   = (0,  212, 255)
PURPLE = (139, 92, 246)
ORANGE = (249, 115, 22)
GREEN  = (34,  197, 94)
WHITE  = (248, 250, 252)
GRAY   = (148, 163, 184)
DGRAY  = (51,  65,  85)

def blend(a, b, t):
    return tuple(int(a[i]*(1-t) + b[i]*t) for i in range(3))

def dim(acc, t=0.2):
    """Blend accent toward BG2."""
    return blend(BG2, acc, t)

def vgrad(w, h, c1=BG1, c2=BG2):
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h-1, 1)
        d.line([(0,y),(w,y)], fill=tuple(int(a+(b-a)*t) for a,b in zip(c1,c2)))
    return img

def rrect(d, x0, y0, x1, y1, r, fill=None, outline=None, lw=3):
    r = int(r)
    if fill:
        d.rectangle([x0+r, y0, x1-r, y1], fill=fill)
        d.rectangle([x0, y0+r, x1, y1-r], fill=fill)
        for cx, cy in [(x0,y0),(x1-2*r,y0),(x0,y1-2*r),(x1-2*r,y1-2*r)]:
            d.ellipse([cx, cy, cx+2*r, cy+2*r], fill=fill)
    if outline:
        d.arc([x0,y0,x0+2*r,y0+2*r], 180, 270, fill=outline, width=lw)
        d.arc([x1-2*r,y0,x1,y0+2*r], 270, 360, fill=outline, width=lw)
        d.arc([x0,y1-2*r,x0+2*r,y1],  90, 180, fill=outline, width=lw)
        d.arc([x1-2*r,y1-2*r,x1,y1],   0,  90, fill=outline, width=lw)
        d.line([(x0+r,y0),(x1-r,y0)], fill=outline, width=lw)
        d.line([(x0+r,y1),(x1-r,y1)], fill=outline, width=lw)
        d.line([(x0,y0+r),(x0,y1-r)], fill=outline, width=lw)
        d.line([(x1,y0+r),(x1,y1-r)], fill=outline, width=lw)

def base(W, H, acc):
    img = vgrad(W*S, H*S)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 10*S, H*S], fill=acc)
    return img, d

def footer(d, W, H, acc):
    fy = (H - 76) * S
    d.line([(60*S, fy), ((W-60)*S, fy)], fill=DGRAY, width=S)
    d.text((60*S, fy + 12*S), "ICTZoid", font=fb(30), fill=acc)
    lbl = "Web Development Program"
    lw = int(d.textlength(lbl, font=fr(24)))
    d.text(((W-60)*S - lw, fy + 16*S), lbl, font=fr(24), fill=GRAY)

def day_tag(d, day, tag, acc):
    d.text((28*S, 28*S), f"DAY {day}", font=fr(22), fill=GRAY)
    f = fb(20)
    tw = int(d.textlength(tag, font=f))
    px, py, r = 14*S, 7*S, 8*S
    x0, y0 = 28*S, 60*S
    x1, y1 = x0+tw+2*px, y0+f.size+2*py
    rrect(d, x0, y0, x1, y1, r, fill=acc)
    tc = (8,12,26) if (0.299*acc[0]+0.587*acc[1]+0.114*acc[2]) > 140 else WHITE
    d.text((x0+px, y0+py), tag, font=f, fill=tc)

def finish(img, W, H):
    return img.resize((W, H), Image.LANCZOS)

def poly_arrow_up(d, tip_x, tip_y, acc):
    hw, hs, stem_h, stem_w = 36*S, 50*S, 70*S, 20*S
    pts = [
        (tip_x, tip_y),
        (tip_x+hw, tip_y+hs),
        (tip_x+stem_w, tip_y+hs),
        (tip_x+stem_w, tip_y+hs+stem_h),
        (tip_x-stem_w, tip_y+hs+stem_h),
        (tip_x-stem_w, tip_y+hs),
        (tip_x-hw, tip_y+hs),
    ]
    d.polygon(pts, fill=acc)

# ── Illustrations ─────────────────────────────────────────────────────────────

def illus_burst(d, w, h, acc, n=28):
    """Radial starburst — Welcome."""
    cx, cy = w//2, h//2 + 30*S
    r_inner, r_outer = 60*S, 280*S
    for i in range(n):
        a = i * 2*math.pi / n
        bright = (i % 4 == 0)
        col = acc if bright else dim(acc, 0.35)
        r_end = r_outer if bright else r_outer - 50*S
        lw = 4 if bright else 2
        x1 = cx + int(r_inner * math.cos(a))
        y1 = cy + int(r_inner * math.sin(a))
        x2 = cx + int(r_end   * math.cos(a))
        y2 = cy + int(r_end   * math.sin(a))
        d.line([(x1,y1),(x2,y2)], fill=col, width=lw)
        dr = 10*S if bright else 5*S
        d.ellipse([x2-dr, y2-dr, x2+dr, y2+dr], fill=col)
    d.ellipse([cx-44*S, cy-44*S, cx+44*S, cy+44*S], fill=acc)
    for rr in [62*S, 80*S]:
        d.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], outline=dim(acc,0.3), width=2)

def illus_network(d, w, h, acc, seed=1):
    """Connected nodes — Internet / DNS."""
    random.seed(seed)
    cx, cy = w//2, h//2 + 20*S
    R = 265*S
    nodes = [(cx, cy)]
    for _ in range(14):
        a = random.uniform(0, 2*math.pi)
        r = random.uniform(R*0.28, R)
        nodes.append((int(cx+r*math.cos(a)), int(cy+r*math.sin(a))))
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            dx = nodes[i][0]-nodes[j][0]; dy = nodes[i][1]-nodes[j][1]
            dist = math.sqrt(dx*dx+dy*dy)
            if dist < R*0.82:
                t = max(0.08, 0.4 - dist/(R*2.2))
                d.line([nodes[i], nodes[j]], fill=dim(acc,t), width=3)
    for i, (nx, ny) in enumerate(nodes):
        r = random.randint(9*S, 18*S) if i > 0 else 28*S
        col = acc if i < 4 else dim(acc, random.uniform(0.4, 0.7))
        d.ellipse([nx-r, ny-r, nx+r, ny+r], fill=col)
    for rr in [40*S, 58*S, 76*S]:
        d.ellipse([cx-rr, cy-rr, cx+rr, cy+rr], outline=dim(acc,0.22), width=2)

def illus_path(d, w, h, acc):
    """Ascending staircase — Learning progression."""
    steps = 5
    sw, sh = 112*S, 84*S
    bx = w//2 - (steps*sw)//2
    by = h//2 + (steps*sh)//2 + 20*S
    for i in range(steps):
        t = (i+1) / steps
        col = blend(dim(acc, 0.18), acc, t)
        d.rectangle([bx+i*sw+4, by-(i+1)*sh+4, bx+(i+1)*sw-4, by-4], fill=col)
    poly_arrow_up(d, bx+steps*sw+50*S, by-(steps*sh)-60*S, acc)

def illus_bars(d, w, h, acc):
    """Horizontal bar chart — Poll A/B/C/D."""
    items = [("A", 0.85), ("B", 0.55), ("C", 0.42), ("D", 0.72)]
    bh, gap = 68*S, 38*S
    total = len(items)*(bh+gap) - gap
    sy = h//2 - total//2
    bx = w//4
    max_w = w//2
    for i, (lbl, pct) in enumerate(items):
        y = sy + i*(bh+gap)
        t = 0.3 + 0.7*pct
        col = blend(dim(acc, 0.35), acc, t)
        bw = int(max_w * pct)
        rrect(d, bx, y, bx+bw, y+bh, 10*S, fill=col)
        d.text((bx-52*S, y+12*S), lbl, font=fb(26), fill=WHITE)

def illus_hourglass(d, w, h, acc):
    """Hourglass — Coming soon."""
    cx, cy = w//2, h//2 + 20*S
    hw, hh, neck = 180*S, 200*S, 32*S
    top = [(cx-hw,cy-hh),(cx+hw,cy-hh),(cx+neck,cy),(cx-neck,cy)]
    bot = [(cx-neck,cy),(cx+neck,cy),(cx+hw,cy+hh),(cx-hw,cy+hh)]
    d.polygon(top, fill=dim(acc, 0.45))
    d.polygon(bot, fill=dim(acc, 0.22))
    d.polygon(top, outline=acc, width=4)
    d.polygon(bot, outline=acc, width=4)
    d.line([(cx-hw,cy-hh),(cx+hw,cy-hh)], fill=acc, width=5)
    d.line([(cx-hw,cy+hh),(cx+hw,cy+hh)], fill=acc, width=5)
    random.seed(7)
    for _ in range(20):
        px = cx + random.randint(-hw//2, hw//2)
        py = random.randint(int(cy-hh+16*S), int(cy-16*S))
        r = random.randint(5*S, 11*S)
        d.ellipse([px-r, py-r, px+r, py+r], fill=acc)

def illus_diamond(d, w, h, acc):
    """Gem / diamond — Reveal."""
    cx, cy = w//2, h//2 + 20*S
    sz = 220*S
    hw = sz * 2 // 3
    pts = [(cx,cy-sz),(cx+hw,cy),(cx,cy+sz),(cx-hw,cy)]
    d.polygon(pts, fill=dim(acc, 0.18))
    d.polygon(pts, outline=acc, width=5)
    for (ax,ay),(bx2,by2) in [
        ((cx,cy-sz),(cx,cy+sz)), ((cx-hw,cy),(cx+hw,cy)),
        ((cx,cy-sz),(cx+hw,cy)), ((cx,cy-sz),(cx-hw,cy)),
    ]:
        d.line([(ax,ay),(bx2,by2)], fill=dim(acc,0.4), width=2)
    for angle, dist in [(45,300*S),(135,270*S),(225,305*S),(315,275*S)]:
        a = math.radians(angle)
        sx, sy2 = cx+int(dist*math.cos(a)), cy+int(dist*math.sin(a))
        for da in [0, 90]:
            aa = math.radians(da)
            d.line([(sx-int(16*S*math.cos(aa)), sy2-int(16*S*math.sin(aa))),
                    (sx+int(16*S*math.cos(aa)), sy2+int(16*S*math.sin(aa)))],
                   fill=acc, width=3)

def illus_xmark(d, w, h, acc):
    """Bold X — Myth bust."""
    cx, cy = w//2, h//2 + 20*S
    sz, thick = 200*S, 30*S
    d.ellipse([cx-sz-40*S,cy-sz-40*S,cx+sz+40*S,cy+sz+40*S], fill=dim(acc,0.07))
    def fat_line(x1,y1,x2,y2,col):
        dx, dy = x2-x1, y2-y1
        length = math.sqrt(dx*dx+dy*dy)
        if not length: return
        nx, ny = -dy/length*thick/2, dx/length*thick/2
        pts = [(int(x1+nx),int(y1+ny)),(int(x2+nx),int(y2+ny)),
               (int(x2-nx),int(y2-ny)),(int(x1-nx),int(y1-ny))]
        d.polygon(pts, fill=col)
    fat_line(cx-sz,cy-sz,cx+sz,cy+sz, dim(acc,0.65))
    fat_line(cx+sz,cy-sz,cx-sz,cy+sz, acc)
    for px,py in [(cx-sz,cy-sz),(cx+sz,cy+sz),(cx+sz,cy-sz),(cx-sz,cy+sz)]:
        r = int(thick//2)
        col = acc if abs(px-cx)==sz and py<cy else dim(acc,0.65)
        d.ellipse([px-r,py-r,px+r,py+r], fill=col)

def illus_pillars(d, w, h, acc):
    """Two pillars — Master Sessions."""
    cx = w//2
    pw, ph, gap = 100*S, 340*S, 60*S
    by = h//2 + ph//2 + 30*S
    for side, col_t in [(-1, 0.7), (1, 1.0)]:
        px = cx + side*(pw//2 + gap//2)
        col = blend(dim(acc, 0.2), acc, col_t)
        rrect(d, px-pw//2, by-ph, px+pw//2, by, 10*S, fill=col)
        rrect(d, px-pw//2-16*S, by-ph-22*S, px+pw//2+16*S, by-ph, 6*S, fill=col)
        rrect(d, px-pw//2-16*S, by, px+pw//2+16*S, by+22*S, 6*S, fill=dim(col,0.5))
    aw = pw + gap + 32*S
    al = cx - aw//2; ar = cx + aw//2
    at = by - ph - 22*S - 80*S; ab = by - ph - 22*S
    d.arc([al, at, ar, ab], 180, 0, fill=dim(acc,0.5), width=4)

def illus_browser(d, w, h, acc):
    """Browser window — Portfolio."""
    bw, bh = 500*S, 370*S
    bx = w//2 - bw//2
    by = h//2 - bh//2 + 20*S
    rrect(d, bx, by, bx+bw, by+bh, 12*S, fill=dim(acc,0.12))
    rrect(d, bx, by, bx+bw, by+bh, 12*S, outline=dim(acc,0.5), lw=4)
    tb = 52*S
    rrect(d, bx, by, bx+bw, by+tb, 12*S, fill=dim(acc,0.28))
    d.rectangle([bx, by+tb//2, bx+bw, by+tb], fill=dim(acc,0.28))
    for i, col in enumerate([ORANGE, dim(ORANGE,0.6), GREEN]):
        tx = bx + (20+i*22)*S
        ty = by + 18*S
        d.ellipse([tx-8*S, ty-8*S, tx+8*S, ty+8*S], fill=col)
    rrect(d, bx+80*S, by+10*S, bx+bw-20*S, by+42*S, 8*S, fill=dim(acc,0.4))
    cy2 = by + tb + 20*S
    content = [
        (bx+20*S, cy2,       bw-40*S,      28*S, 0.38),
        (bx+20*S, cy2+50*S,  int(bw*0.58), 80*S, 0.22),
        (bx+20*S+int(bw*0.62), cy2+50*S, int(bw*0.32), 80*S, 0.16),
        (bx+20*S, cy2+150*S, bw-40*S,      20*S, 0.20),
        (bx+20*S, cy2+182*S, int(bw*0.44), 20*S, 0.15),
    ]
    for cx2, cy3, cw, ch, t in content:
        rrect(d, int(cx2), int(cy3), int(cx2+cw), int(cy3+ch), 6*S, fill=dim(acc,t))

def illus_circuit(d, w, h, acc):
    """Circuit / neural network grid — AI."""
    cols, rows = 7, 5
    ox, oy = 50*S, 110*S
    gx = (w - 2*ox) // (cols-1)
    gy = (h - 2*oy - 100*S) // (rows-1)
    nodes = [(ox + c*gx, oy + r*gy) for r in range(rows) for c in range(cols)]
    random.seed(42)
    hl = set(random.sample(range(len(nodes)), 9))
    for r in range(rows):
        for c in range(cols-1):
            i, j = r*cols+c, r*cols+c+1
            is_h = i in hl and j in hl
            d.line([nodes[i], nodes[j]], fill=dim(acc, 0.45 if is_h else 0.12), width=4 if is_h else 2)
    for r in range(rows-1):
        for c in range(cols):
            i, j = r*cols+c, (r+1)*cols+c
            is_h = i in hl and j in hl
            d.line([nodes[i], nodes[j]], fill=dim(acc, 0.4 if is_h else 0.1), width=3 if is_h else 2)
    for i, (nx, ny) in enumerate(nodes):
        is_h = i in hl
        r = 17*S if is_h else 10*S
        d.ellipse([nx-r, ny-r, nx+r, ny+r], fill=acc if is_h else dim(acc, 0.45))

def illus_target(d, w, h, acc):
    """Bullseye — Mission / goal."""
    cx, cy = w//2, h//2 + 20*S
    rings = [250*S, 190*S, 130*S, 70*S, 28*S]
    fills = [0.07, 0.14, 0.27, 0.52, 1.0]
    for r, t in zip(rings, fills):
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=dim(acc,t))
    for r in rings[:-1]:
        d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=dim(acc,0.22), width=2)
    start_x = cx - int(rings[0]*0.72)
    start_y = cy + int(rings[0]*0.72)
    end_x   = cx + int(rings[1]*0.62)
    end_y   = cy - int(rings[1]*0.62)
    d.line([(start_x, start_y),(end_x, end_y)], fill=acc, width=7)
    a = math.atan2(end_y-start_y, end_x-start_x)
    hl2 = 28*S
    pts = [(end_x, end_y),
           (int(end_x - hl2*math.cos(a-0.5)), int(end_y - hl2*math.sin(a-0.5))),
           (int(end_x - hl2*math.cos(a+0.5)), int(end_y - hl2*math.sin(a+0.5)))]
    d.polygon(pts, fill=acc)

def illus_git(d, w, h, acc):
    """Git branch diagram."""
    my = h//2 + 50*S
    by2 = my - 160*S
    lx, rx = 80*S, w-80*S
    commits = [lx+60*S, lx+200*S, lx+370*S, rx-200*S, rx-60*S]
    bc = [commits[1]+110*S, commits[1]+250*S]
    d.line([(lx, my),(rx, my)], fill=dim(acc,0.4), width=5)
    d.line([(commits[1], my),(bc[0]-20*S, by2)], fill=dim(acc,0.6), width=3)
    d.line([(bc[0]-20*S, by2),(bc[-1]+20*S, by2)], fill=dim(acc,0.6), width=3)
    d.line([(bc[-1]+20*S, by2),(commits[3], my)], fill=dim(acc,0.6), width=3)
    for i, cx2 in enumerate(commits):
        r = 20*S
        col = acc if i in (0,4) else dim(acc, 0.7)
        d.ellipse([cx2-r, my-r, cx2+r, my+r], fill=col)
        d.ellipse([cx2-r-5, my-r-5, cx2+r+5, my+r+5], outline=dim(acc,0.3), width=2)
    for cx2 in bc:
        r = 17*S
        d.ellipse([cx2-r, by2-r, cx2+r, by2+r], fill=acc)
    d.text((lx, my+30*S), "main", font=fr(20), fill=GRAY)
    d.text((bc[0]-20*S, by2-48*S), "feature", font=fr(20), fill=dim(acc,0.8))

def illus_clock(d, w, h, acc):
    """Clock face — Countdown."""
    cx, cy = w//2, h//2 + 20*S
    R = 240*S
    d.ellipse([cx-R, cy-R, cx+R, cy+R], fill=dim(acc, 0.08))
    d.ellipse([cx-R, cy-R, cx+R, cy+R], outline=acc, width=5)
    for i in range(12):
        a = i*math.pi/6 - math.pi/2
        r_in = R*0.80 if i%3==0 else R*0.88
        lw = 5 if i%3==0 else 3
        col = acc if i==0 else dim(acc, 0.5)
        d.line([(cx+int(r_in*math.cos(a)), cy+int(r_in*math.sin(a))),
                (cx+int(R*0.96*math.cos(a)), cy+int(R*0.96*math.sin(a)))],
               fill=col, width=lw)
    ha = math.radians(330) - math.pi/2
    d.line([(cx,cy),(cx+int(R*0.54*math.cos(ha)), cy+int(R*0.54*math.sin(ha)))],
           fill=WHITE, width=9)
    ma = -math.pi/2
    d.line([(cx,cy),(cx+int(R*0.77*math.cos(ma)), cy+int(R*0.77*math.sin(ma)))],
           fill=acc, width=7)
    d.ellipse([cx-13*S, cy-13*S, cx+13*S, cy+13*S], fill=acc)

def illus_rocket(d, w, h, acc):
    """Rocket launch."""
    cx = w//2
    nose_y  = h//4
    body_t  = nose_y + 60*S
    body_b  = h//2 + 80*S
    hw      = 56*S
    d.polygon([(cx,nose_y),(cx-hw,body_t),(cx+hw,body_t)], fill=acc)
    rrect(d, cx-hw, body_t, cx+hw, body_b, 8*S, fill=dim(acc,0.7))
    wr = 28*S
    wy = body_t + 60*S
    d.ellipse([cx-wr, wy-wr, cx+wr, wy+wr], fill=dim(acc,0.12))
    d.ellipse([cx-wr, wy-wr, cx+wr, wy+wr], outline=acc, width=4)
    for side in (-1, 1):
        fx = cx + side*hw
        pts = [(fx, body_b-80*S),(fx+side*50*S, body_b+20*S),(fx, body_b)]
        d.polygon(pts, fill=dim(acc,0.6))
    for fw, t in [(32*S,0.9),(22*S,0.6),(13*S,0.35)]:
        d.ellipse([cx-fw, body_b-fw, cx+fw, body_b+fw], fill=dim(acc,t))
        body_b += 40*S
    random.seed(99)
    for _ in range(22):
        sx = random.randint(30*S, w-30*S)
        sy = random.randint(30*S, int(h*0.65))
        if abs(sx - cx) > 100*S:
            r = random.randint(3*S, 7*S)
            d.ellipse([sx-r, sy-r, sx+r, sy+r], fill=dim(acc, random.uniform(0.4,1.0)))

def illus_stacked(d, w, h, acc):
    """Stacked course blocks — Program overview."""
    labels = ["HTML","CSS","JS","React","AI"]
    bw, bh, gap = 420*S, 68*S, 14*S
    total = len(labels)*(bh+gap) - gap
    bx = w//2 - bw//2
    by = h//2 - total//2 + 20*S
    for i, lbl in enumerate(labels):
        t = (i+1) / len(labels)
        col = blend(dim(acc,0.18), acc, t)
        y = by + i*(bh+gap)
        rrect(d, bx, y, bx+bw, y+bh, 10*S, fill=col)
        d.text((bx+20*S, y+15*S), lbl, font=fb(26), fill=WHITE)

def illus_chat(d, w, h, acc):
    """Chat bubbles — Community / WhatsApp."""
    cx, cy = w//2, h//2
    bw1, bh1 = 380*S, 110*S
    x1, y1 = cx-200*S, cy-130*S
    rrect(d, x1, y1, x1+bw1, y1+bh1, 20*S, fill=dim(acc,0.45))
    d.polygon([(x1+40*S, y1+bh1),(x1+20*S, y1+bh1+30*S),(x1+80*S, y1+bh1)],
              fill=dim(acc,0.45))
    for i in range(3):
        dx2 = x1+80*S+i*60*S; r = 14*S
        d.ellipse([dx2-r, y1+bh1//2-r, dx2+r, y1+bh1//2+r], fill=WHITE)
    bw2, bh2 = 400*S, 100*S
    x2, y2 = cx-80*S, cy+30*S
    rrect(d, x2, y2, x2+bw2, y2+bh2, 20*S, fill=acc)
    d.polygon([(x2+bw2-80*S, y2+bh2),(x2+bw2-50*S, y2+bh2+30*S),(x2+bw2-20*S, y2+bh2)],
              fill=acc)
    tc = (8,12,26) if (0.299*acc[0]+0.587*acc[1]+0.114*acc[2]) > 140 else dim(acc,0.3)
    for i in range(3):
        dx2 = x2+80*S+i*60*S; r = 14*S
        d.ellipse([dx2-r, y2+bh2//2-r, dx2+r, y2+bh2//2+r], fill=tc)

def illus_globe(d, w, h, acc):
    """Globe with connections — Internet / global reach."""
    cx, cy = w//2, h//2 + 20*S
    R = 230*S
    d.ellipse([cx-R, cy-R, cx+R, cy+R], fill=dim(acc,0.07))
    d.ellipse([cx-R, cy-R, cx+R, cy+R], outline=dim(acc,0.4), width=4)
    for lat in [-0.55, -0.28, 0, 0.28, 0.55]:
        ry = int(lat*R)
        rx2 = int(math.sqrt(max(0, R*R - ry*ry)))
        if rx2 > 0:
            d.arc([cx-rx2, cy+ry-rx2//3, cx+rx2, cy+ry+rx2//3],   0, 180, fill=dim(acc,0.28), width=2)
            d.arc([cx-rx2, cy+ry-rx2//3, cx+rx2, cy+ry+rx2//3], 180, 360, fill=dim(acc,0.14), width=2)
    for lon in [-0.55, -0.28, 0, 0.28, 0.55]:
        dx2 = int(lon*R)
        rh = int(math.sqrt(max(0, R*R - dx2*dx2)))
        if rh > 0:
            d.arc([cx+dx2-rh//4, cy-R, cx+dx2+rh//4, cy+R], 0, 360, fill=dim(acc,0.18), width=2)
    pts2 = [(0.3,0.2),(-0.5,0.35),(0.55,-0.3),(-0.2,-0.48),(0.1,0.55)]
    nds = [(cx+int(t*R), cy+int(u*R)) for t,u in pts2]
    for i in range(len(nds)):
        for j in range(i+1, len(nds)):
            d.line([nds[i], nds[j]], fill=dim(acc,0.4), width=2)
    for nx2, ny2 in nds:
        r = 14*S
        d.ellipse([nx2-r, ny2-r, nx2+r, ny2+r], fill=acc)

# ── Card makers ───────────────────────────────────────────────────────────────

WA_DATA = [
    (1,  "WELCOME",        CYAN,   illus_burst),
    (2,  "DID YOU KNOW",   PURPLE, illus_network),
    (3,  "INSIGHT",        CYAN,   illus_path),
    (4,  "POLL",           ORANGE, illus_bars),
    (5,  "COMING SOON",    PURPLE, illus_hourglass),
    (6,  "REVEAL",         ORANGE, illus_diamond),
    (7,  "MYTH BUST",      GREEN,  illus_xmark),
    (8,  "SPOTLIGHT",      PURPLE, illus_pillars),
    (9,  "YOUR PORTFOLIO", GREEN,  illus_browser),
    (10, "AI SPOTLIGHT",   CYAN,   illus_circuit),
    (11, "OUR MISSION",    PURPLE, illus_target),
    (12, "GIT SPOTLIGHT",  ORANGE, illus_git),
    (13, "COUNTDOWN",      ORANGE, illus_clock),
    (14, "WE'RE LIVE",     GREEN,  illus_rocket),
]

IG_DATA = [
    ("ig_01_program",   CYAN,   illus_stacked),
    ("ig_02_ai",        PURPLE, illus_circuit),
    ("ig_03_portfolio", GREEN,  illus_browser),
    ("ig_04_cta",       ORANGE, illus_chat),
]

TW_DATA = [
    ("tw_thread",  CYAN,   illus_globe),
    ("tw_s1",      CYAN,   illus_network),
    ("tw_s2",      ORANGE, illus_git),
    ("tw_s3",      PURPLE, illus_circuit),
]

LI_DATA = [
    ("li_01_announcement", CYAN,   illus_stacked),
    ("li_02_philosophy",   PURPLE, illus_pillars),
]

def make_wa(day, tag, acc, fn):
    W, H = 1080, 1080
    img, d = base(W, H, acc)
    fn(d, W*S, H*S, acc)
    footer(d, W, H, acc)
    return finish(img, W, H)

def make_ig(slug, acc, fn):
    W, H = 1080, 1080
    img, d = base(W, H, acc)
    fn(d, W*S, H*S, acc)
    footer(d, W, H, acc)
    return finish(img, W, H)

def make_tw(slug, acc, fn):
    W, H = 1200, 675
    img, d = base(W, H, acc)
    fn(d, W*S, H*S, acc)
    footer(d, W, H, acc)
    return finish(img, W, H)

def make_li(slug, acc, fn):
    W, H = 1200, 628
    img, d = base(W, H, acc)
    fn(d, W*S, H*S, acc)
    footer(d, W, H, acc)
    return finish(img, W, H)

# ── Generate ──────────────────────────────────────────────────────────────────
print("WhatsApp...")
for day, tag, acc, fn in WA_DATA:
    img = make_wa(day, tag, acc, fn)
    name = f"day_{str(day).zfill(2)}_{tag.lower().replace(' ','_')}.png"
    img.save(f"{ROOT}/whatsapp/{name}")
    print(f"  + {name}")

print("Instagram...")
for slug, acc, fn in IG_DATA:
    make_ig(slug, acc, fn).save(f"{ROOT}/instagram/{slug}.png")
    print(f"  + {slug}.png")

print("Twitter...")
for slug, acc, fn in TW_DATA:
    make_tw(slug, acc, fn).save(f"{ROOT}/twitter/{slug}.png")
    print(f"  + {slug}.png")

print("LinkedIn...")
for slug, acc, fn in LI_DATA:
    make_li(slug, acc, fn).save(f"{ROOT}/linkedin/{slug}.png")
    print(f"  + {slug}.png")

print(f"\nDone. {ROOT}")
