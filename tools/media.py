"""Dựng video/ảnh từ tư liệu thật (ffmpeg + Playwright). Không tạo cảnh dự án bằng AI.

  python tools/media.py clip  --src <video> --segments 36-50,54-66 [--crop w:h:x:y] [--size 1080] [--mute] --out <mp4>
  python tools/media.py still --src <video> --at 55,58.5 [--crop w:h:x:y] --out-prefix <path>
  python tools/media.py sheet --src <video> [--every 3] --out <jpg>     # xem nhanh khung hình có mốc thời gian
  python tools/media.py card  --data <json> [--size 1080x1350] --out <png>  # ảnh kiến thức, chữ tiếng Việt chuẩn

Output để trong assets/dong-lac/media/. Ảnh/video đưa lên bài vẫn phải qua compliance (chữ trên hình = nội dung bài).
"""
import argparse
import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FONT = "C\\:/Windows/Fonts/arial.ttf"


def run(args):
    r = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode:
        sys.exit("FFMPEG_ERROR " + r.stderr[-800:])


def crop_scale(crop, size):
    vf = []
    if crop:
        w, h, x, y = crop.split(":")
        vf.append(f"crop={w}:{h}:{x}:{y}")
    if size:
        vf.append(f"scale={size}:-2:flags=lanczos")
    return vf


def cmd_clip(a):
    segs = [tuple(map(float, s.split("-"))) for s in a.segments.split(",")]
    vf = ",".join(crop_scale(a.crop, a.size) + ["setsar=1", "fps=30"]) or "null"
    parts, fc = [], []
    for i, (s, e) in enumerate(segs):
        fc.append(f"[0:v]trim={s}:{e},setpts=PTS-STARTPTS,{vf}[v{i}]")
        parts.append(f"[v{i}]")
        if not a.mute:
            fc.append(f"[0:a]atrim={s}:{e},asetpts=PTS-STARTPTS[a{i}]")
            parts.append(f"[a{i}]")
    n = len(segs)
    fc.append("".join(parts) + f"concat=n={n}:v=1:a={0 if a.mute else 1}" + ("[v]" if a.mute else "[v][a]"))
    maps = ["-map", "[v]"] + ([] if a.mute else ["-map", "[a]"])
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    run(["-i", a.src, "-filter_complex", ";".join(fc), *maps, "-c:v", "libx264", "-crf", "20",
         "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
         *(["-c:a", "aac", "-b:a", "128k"] if not a.mute else ["-an"]), a.out])
    print("OK", a.out, f"{sum(e - s for s, e in segs):.1f}s")


def cmd_still(a):
    vf = ",".join(crop_scale(a.crop, a.size)) or "null"
    for t in a.at.split(","):
        out = f"{a.out_prefix}-{t.replace('.', '_')}s.jpg"
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        run(["-ss", t, "-i", a.src, "-frames:v", "1", "-vf", vf, "-q:v", "2", out])
        print("OK", out)


def cmd_sheet(a):
    dt = (f"drawtext=fontfile='{FONT}':text='%{{pts\\:hms}}':x=4:y=4:fontsize=18:"
          "fontcolor=yellow:box=1:boxcolor=black")
    run(["-i", a.src, "-vf", f"fps=1/{a.every},scale=180:-2,{dt},tile=10x4", "-frames:v", "1", a.out])
    print("OK", a.out)


CARD_CSS = """
*{box-sizing:border-box;margin:0}
body{width:%(w)dpx;height:%(h)dpx;font-family:'Segoe UI',Arial,sans-serif;background:#f6f1e7;color:#1f2a24;
     padding:84px 80px;display:flex;flex-direction:column}
.kicker{font-size:30px;letter-spacing:2px;text-transform:uppercase;color:#8a6a2f;font-weight:600}
h1{font-size:64px;line-height:1.15;margin:18px 0 44px;font-weight:800}
ol{list-style:none;padding:0;display:flex;flex-direction:column;gap:26px;flex:1}
li{display:flex;gap:28px;align-items:flex-start;background:#fff;border-radius:22px;padding:28px 32px;
   box-shadow:0 2px 0 #e4dccb}
.n{flex:none;width:64px;height:64px;border-radius:50%%;background:#2f5d46;color:#fff;font-size:34px;
   font-weight:800;display:flex;align-items:center;justify-content:center}
.t b{display:block;font-size:36px;line-height:1.2}
.t span{display:block;font-size:28px;line-height:1.35;color:#4b5a52;margin-top:6px}
.foot{margin-top:40px;font-size:30px;color:#2f5d46;font-weight:700;border-top:3px solid #2f5d46;padding-top:22px}
"""


def cmd_card(a):
    d = json.loads(Path(a.data).read_text(encoding="utf-8"))
    w, h = map(int, a.size.split("x"))
    items = "".join(
        f'<li><div class="n">{i}</div><div class="t"><b>{html.escape(it["title"])}</b>'
        f'<span>{html.escape(it.get("note", ""))}</span></div></li>'
        for i, it in enumerate(d["items"], 1))
    page = (f'<html><head><meta charset="utf-8"><style>{CARD_CSS % {"w": w, "h": h}}</style></head><body>'
            f'<div class="kicker">{html.escape(d.get("kicker", ""))}</div><h1>{html.escape(d["title"])}</h1>'
            f'<ol>{items}</ol><div class="foot">{html.escape(d.get("footer", ""))}</div></body></html>')
    from playwright.sync_api import sync_playwright
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(page)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page(viewport={"width": w, "height": h})
        p.goto(Path(f.name).as_uri())
        p.screenshot(path=a.out)
        b.close()
    print("OK", a.out)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("clip"); c.add_argument("--src", required=True); c.add_argument("--segments", required=True)
    c.add_argument("--crop"); c.add_argument("--size", type=int); c.add_argument("--mute", action="store_true")
    c.add_argument("--out", required=True)
    s = sp.add_parser("still"); s.add_argument("--src", required=True); s.add_argument("--at", required=True)
    s.add_argument("--crop"); s.add_argument("--size", type=int); s.add_argument("--out-prefix", required=True)
    t = sp.add_parser("sheet"); t.add_argument("--src", required=True); t.add_argument("--every", type=float, default=3)
    t.add_argument("--out", required=True)
    k = sp.add_parser("card"); k.add_argument("--data", required=True); k.add_argument("--size", default="1080x1350")
    k.add_argument("--out", required=True)
    a = ap.parse_args()
    globals()["cmd_" + a.cmd](a)


if __name__ == "__main__":
    main()
