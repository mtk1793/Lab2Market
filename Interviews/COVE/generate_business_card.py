#!/usr/bin/env python3
"""
AddManuChain — Digital Business Card Generator
Standard business card: 3.5" x 2" @ 300 DPI = 1050 x 600 px
"""

import qrcode
import qrcode.image.svg
from PIL import Image, ImageDraw, ImageFont
import os, math, io

# ── Canvas ────────────────────────────────────────────────────────────────────
W, H = 1050, 600
OUT_FRONT = os.path.join(os.path.dirname(__file__), "BusinessCard_Front.png")
OUT_BACK  = os.path.join(os.path.dirname(__file__), "BusinessCard_Back.png")

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY      = (10,  20,  45)
NAVY2     = (14,  28,  60)
ACCENT    = (0,  140, 255)        # electric blue
ACCENT2   = (0,  200, 180)        # teal
WHITE     = (255, 255, 255)
LGRAY     = (160, 180, 210)
DGRAY     = ( 40,  60,  95)
GOLD      = (220, 170,  40)

# ── Fonts ─────────────────────────────────────────────────────────────────────
def try_font(names, size):
    for name in names:
        for d in ["/System/Library/Fonts", "/Library/Fonts",
                  "/System/Library/Fonts/Supplemental"]:
            path = os.path.join(d, name)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    return ImageFont.load_default()

FONT_BRAND  = try_font(["HelveticaNeue-Bold.ttf","Arial Bold.ttf","Arial.ttf"], 58)
FONT_TITLE  = try_font(["HelveticaNeue.ttf","Arial.ttf"], 26)
FONT_NAME   = try_font(["HelveticaNeue-Bold.ttf","Arial Bold.ttf","Arial.ttf"], 32)
FONT_BODY   = try_font(["HelveticaNeue.ttf","Arial.ttf"], 22)
FONT_SMALL  = try_font(["HelveticaNeue.ttf","Arial.ttf"], 18)
FONT_MICRO  = try_font(["HelveticaNeue.ttf","Arial.ttf"], 15)
FONT_TAG    = try_font(["HelveticaNeue-Bold.ttf","Arial Bold.ttf","Arial.ttf"], 17)

# ── QR Code ───────────────────────────────────────────────────────────────────
def make_qr(url: str, size: int) -> Image.Image:
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="#0A1A40")
    img = img.convert("RGBA")
    img = img.resize((size, size), Image.LANCZOS)
    return img

# ── Helpers ───────────────────────────────────────────────────────────────────
def draw_grid(d: ImageDraw.Draw, w, h, spacing=40, color=(255,255,255,12)):
    for x in range(0, w, spacing):
        d.line([(x,0),(x,h)], fill=color, width=1)
    for y in range(0, h, spacing):
        d.line([(0,y),(w,y)], fill=color, width=1)

def draw_circuit_trace(d: ImageDraw.Draw, pts, color, width=2):
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill=color, width=width)

def rounded_rect(d: ImageDraw.Draw, xy, radius, fill=None, outline=None, width=2):
    d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def pill(d: ImageDraw.Draw, x, y, text, font, bg, fg):
    bbox = font.getbbox(text)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    pad_x, pad_y = 12, 6
    rx = [x, y, x+tw+pad_x*2, y+th+pad_y*2]
    rounded_rect(d, rx, radius=6, fill=bg)
    d.text((x+pad_x, y+pad_y-bbox[1]), text, font=font, fill=fg)
    return rx[2] + 10

# ═══════════════════════════════════════════════════════════════════════════════
# FRONT CARD
# ═══════════════════════════════════════════════════════════════════════════════
def make_front() -> Image.Image:
    img = Image.new("RGBA", (W, H), NAVY)
    d   = ImageDraw.Draw(img, "RGBA")

    # — subtle grid —
    draw_grid(d, W, H, spacing=38, color=(255,255,255,10))

    # — left accent bar —
    d.rectangle([0, 0, 6, H], fill=ACCENT)

    # — top diagonal slash —
    for i in range(8):
        off = i * 6
        d.polygon([
            (W-320+off, 0), (W+off, 0),
            (W+off, H//3), (W-320+off, H//3)
        ], fill=(0,140,255, 6))

    # — circuit traces (decorative) —
    trace_col = (*ACCENT, 25)
    draw_circuit_trace(d, [(50,H-30),(50,H-80),(180,H-80),(180,H-120)], trace_col)
    draw_circuit_trace(d, [(620,30),(720,30),(720,80)], trace_col)
    draw_circuit_trace(d, [(580,H-40),(660,H-40),(660,H-100)], trace_col)

    # — company name —
    x0 = 38
    d.text((x0, 42), "AddManuChain", font=FONT_BRAND, fill=WHITE)
    # underline accent
    bb = FONT_BRAND.getbbox("AddManuChain")
    tw = bb[2]-bb[0]
    d.rectangle([x0, 42+bb[3]-bb[1]+6, x0+tw, 42+bb[3]-bb[1]+10], fill=ACCENT)

    # — tagline —
    d.text((x0, 122), "Digital Spare Parts Vault  ·  Certified On-Demand Manufacturing",
           font=FONT_SMALL, fill=LGRAY)

    # — divider line —
    d.line([(x0, 158), (620, 158)], fill=DGRAY, width=1)

    # — name —
    d.text((x0, 172), "Mahmoud Kiasari", font=FONT_NAME, fill=WHITE)

    # — title —
    d.text((x0, 214), "Founder  |  Lab2Market Oceans Program", font=FONT_BODY, fill=LGRAY)
    d.text((x0, 244), "Dalhousie University", font=FONT_BODY, fill=LGRAY)

    # — contact —
    d.text((x0, 290), "✉  mh.kiasari@dal.ca", font=FONT_BODY, fill=ACCENT2)
    d.text((x0, 320), "🌐  addmanuchain-dashboard.vercel.app", font=FONT_BODY, fill=ACCENT2)

    # — tech tags —
    y_tags = 368
    next_x = x0
    for tag, bg in [("Lloyd's Register Certified", (0,80,50,200)),
                    ("DRM-Protected IP", (60,20,100,200)),
                    ("Atlantic XL Partner", (0,60,100,200))]:
        next_x = pill(d, next_x, y_tags, tag, FONT_TAG, bg, WHITE)

    # — QR code block (right side) —
    qr_size = 210
    qr_img  = make_qr("https://addmanuchain-dashboard.vercel.app", qr_size)

    qr_x = W - qr_size - 48
    qr_y = (H - qr_size) // 2

    # QR background card
    rounded_rect(d, [qr_x-18, qr_y-18, qr_x+qr_size+18, qr_y+qr_size+52],
                 radius=14, fill=NAVY2, outline=(*ACCENT, 180), width=2)

    img.paste(qr_img, (qr_x, qr_y))

    # QR label
    label = "Scan to visit"
    lb = FONT_MICRO.getbbox(label)
    lw = lb[2]-lb[0]
    d.text((qr_x + (qr_size-lw)//2, qr_y+qr_size+8), label, font=FONT_MICRO, fill=LGRAY)

    # corner dots
    for cx, cy in [(qr_x-14, qr_y-14), (qr_x+qr_size+14, qr_y-14),
                   (qr_x-14, qr_y+qr_size+46), (qr_x+qr_size+14, qr_y+qr_size+46)]:
        d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=ACCENT)

    # — bottom bar —
    d.rectangle([0, H-38, W, H], fill=NAVY2)
    d.rectangle([0, H-38, W, H-36], fill=ACCENT)
    event_txt = "COVE Ocean Connector  ·  February 26, 2026  ·  Halifax, NS"
    eb = FONT_MICRO.getbbox(event_txt)
    ew = eb[2]-eb[0]
    d.text(((W-ew)//2, H-28), event_txt, font=FONT_MICRO, fill=LGRAY)

    return img.convert("RGB")


# ═══════════════════════════════════════════════════════════════════════════════
# BACK CARD  (key stats + pitch anchor)
# ═══════════════════════════════════════════════════════════════════════════════
def make_back() -> Image.Image:
    img = Image.new("RGBA", (W, H), NAVY)
    d   = ImageDraw.Draw(img, "RGBA")

    draw_grid(d, W, H, spacing=38, color=(255,255,255,9))

    # decorative diagonal
    for i in range(6):
        off = i * 8
        d.polygon([(off,0),(320+off,0),(320+off,H//2),(off,H//2)],
                  fill=(0,140,255, 5))

    # left accent bar
    d.rectangle([0, 0, 6, H], fill=ACCENT2)

    # headline
    d.text((38, 36), "Why AddManuChain?", font=FONT_BRAND, fill=WHITE)
    bb = FONT_BRAND.getbbox("Why AddManuChain?")
    tw = bb[2]-bb[0]
    d.rectangle([38, 36+bb[3]-bb[1]+4, 38+tw, 36+bb[3]-bb[1]+8], fill=ACCENT2)

    # stat blocks
    stats = [
        ("81%",   "Lead-time reduction",      "21 days → 4 days average",         ACCENT),
        ("81%",   "Warehouse cost cut",        "$450K → $85K / year",              ACCENT2),
        ("$1M/d", "Downtime prevented",        "Per vessel per day",               GOLD),
        ("3–5d",  "Part-in-hand delivery",     "Lloyd's Register certified print", LGRAY),
    ]

    col_w = (W - 76) // 2
    for i, (num, label, sub, col) in enumerate(stats):
        col_x = 38 + (i % 2) * (col_w + 20)
        row_y = 140 + (i // 2) * 155

        # block bg
        rounded_rect(d, [col_x, row_y, col_x+col_w, row_y+130],
                     radius=10, fill=NAVY2, outline=(*col[:3], 80), width=1)

        # big number
        d.text((col_x+18, row_y+12), num, font=FONT_BRAND, fill=col)

        # label
        d.text((col_x+18, row_y+72), label, font=FONT_TAG, fill=WHITE)

        # sub
        d.text((col_x+18, row_y+98), sub, font=FONT_MICRO, fill=LGRAY)

    # pitch anchor — bottom
    d.rectangle([0, H-90, W, H-88], fill=ACCENT)
    d.rectangle([0, H-90, W, H], fill=(10,20,45,230))

    pitch = '"OEM-authorized. Cryptographic DRM. Certified in days, not months."'
    pb = FONT_BODY.getbbox(pitch)
    pw = pb[2]-pb[0]
    d.text(((W-pw)//2, H-72), pitch, font=FONT_BODY, fill=LGRAY)

    return img.convert("RGB")


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    front = make_front()
    front.save(OUT_FRONT, dpi=(300,300))
    print(f"✓ Front: {OUT_FRONT}")

    back = make_back()
    back.save(OUT_BACK, dpi=(300,300))
    print(f"✓ Back:  {OUT_BACK}")

    # also save a combined sheet
    combined = Image.new("RGB", (W, H*2+20), (5,10,20))
    combined.paste(front, (0,0))
    combined.paste(back,  (0,H+20))
    out_combined = os.path.join(os.path.dirname(__file__), "BusinessCard_Print_Sheet.png")
    combined.save(out_combined, dpi=(300,300))
    print(f"✓ Sheet: {out_combined}")
