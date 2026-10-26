"""Kho ảnh xoay vòng `assets/dong-lac/kho-anh/danh_muc.json` (05/10/2026).

  python tools/kho_anh.py --cat-khung        # cắt khung từ video theo danh mục (crop_px + làm mờ 'mo') → kho-anh/khung/
  python tools/kho_anh.py --xem <out.jpg>    # ảnh lưới mọi góc ảnh trong danh mục, có id + loại → soát mắt trước khi dùng

Thêm nguyên liệu mới: thêm mục vào danh_muc.json (mo_ta phải đúng cái thấy), chạy --cat-khung nếu là video, --xem để soát.
"""
import argparse
import json
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from common import ROOT

KHO = ROOT / "assets" / "dong-lac" / "kho-anh"
DANH_MUC = KHO / "danh_muc.json"


def doc_danh_muc() -> dict:
    return json.loads(DANH_MUC.read_text(encoding="utf-8"))


def mo_vung(im: Image.Image, hop_ds) -> Image.Image:
    """Làm mờ các hộp (px, toạ độ trên khung đã cắt), viền mềm."""
    if not hop_ds:
        return im
    mat_na = Image.new("L", im.size, 0)
    ve = ImageDraw.Draw(mat_na)
    for hop in hop_ds:
        ve.rectangle(hop, fill=255)
    mat_na = mat_na.filter(ImageFilter.GaussianBlur(12))
    return Image.composite(im.filter(ImageFilter.GaussianBlur(14)), im, mat_na)


def cat_khung() -> None:
    import imageio_ffmpeg

    ff = imageio_ffmpeg.get_ffmpeg_exe()
    for m in doc_danh_muc()["anh"]:
        if "video" not in m:
            continue
        ra = ROOT / m["src"]
        ra.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory() as td:
            png = Path(td) / "k.png"
            r = subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-y", "-ss", str(m["t"]), "-i",
                                str(ROOT / m["video"]), "-frames:v", "1", str(png)], capture_output=True, text=True)
            if r.returncode or not png.exists():
                print("LOI", m["id"], r.stderr[-300:])
                continue
            im = Image.open(png).convert("RGB").crop(tuple(m["crop_px"]))
        mo_vung(im, m.get("mo")).save(ra, quality=92)
        print("OK", m["id"], im.size)


def mo_goc(m: dict) -> Image.Image:
    im = Image.open(ROOT / m["src"]).convert("RGB")
    w, h = im.size
    x0, y0, x1, y1 = m["box"]
    return im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))


def xem(out: str) -> None:
    ds = doc_danh_muc()["anh"]
    o, cot = 300, 6
    luoi = Image.new("RGB", (cot * o, ((len(ds) + cot - 1) // cot) * (o + 30)), "white")
    for i, m in enumerate(ds):
        im = mo_goc(m)
        im.thumbnail((o, o))
        x, y = (i % cot) * o, (i // cot) * (o + 30)
        luoi.paste(im, (x + (o - im.width) // 2, y + 30))
        ImageDraw.Draw(luoi).text((x + 4, y + 8), f"{i} {m['id']} [{m['loai']}/{m['goc_nhin']}]", fill="black")
    luoi.save(out, quality=82)
    print("OK", out, len(ds), "góc ảnh")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cat-khung", action="store_true")
    ap.add_argument("--xem")
    a = ap.parse_args()
    if a.cat_khung:
        cat_khung()
    if a.xem:
        xem(a.xem)


if __name__ == "__main__":
    main()
