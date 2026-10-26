"""Video dọc kiểu "đi bộ xem văn phòng" (người dùng 26/10 gửi mẫu Reel Hanoi Office: cảnh quay phủ kín màn hình,
logo nhỏ trên đỉnh, ô chữ trắng bo góc có dấu ngoặc kép ở giữa, ít chữ).

  python tools/video_ben_trong.py <cau_hinh.json>

Cấu hình:
  "doan": [{"loai": "video", "file", "tu", "dai", "cx": 0.5},          # cắt khung dọc 9:16 ở giữa (cx = vị trí ngang 0–1)
           {"loai": "anh", "file", "giay", "cx": 0.5, "cat_tren", "cat_duoi"},   # ảnh phủ kín khung dọc, đứng yên
           {"loai": "anh_ngang", "file", "giay", "giu_mau": true}],     # ảnh ngang đặt hết bề ngang, nền mờ (ảnh mặt tiền)
  "o_chu": [{"tu", "den", "dong": ["DÒNG 1", "dòng 2"]}],               # ô chữ trắng giữa màn hình theo giây
  "dau_trang": ["SUN CITY · 1B HÙNG VƯƠNG", "Gọi/Zalo 0965.539.599"],   # chữ nhỏ trên đỉnh, suốt video
  "loi_doc", "doc_tre", "nhac_nen", "ra"
Ảnh/video đứng yên (không phóng nhẹ — 26/10 "đừng cho rung"); chuyển cảnh mờ dần 0,3 giây; chữ trong y 190–832.
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from video_dinh_vi import FONT, FPS, ROOT, VANG, chu, ffmpeg, ghep_tieng, mo_anh, nen_mo  # noqa: E402

W, H = 720, 1280


def khung_video(d):
    """Đoạn quay ngang → cắt khung dọc 9:16 phủ kín màn hình (giữ chiều cao, cắt hai bên)."""
    vh = H
    vw = int(round(1280 * H / 720)) // 2 * 2  # phóng chiều cao 720 → 1280
    p = subprocess.Popen([ffmpeg(), "-loglevel", "error", "-ss", str(d.get("tu", 0)), "-t", str(d["dai"]), "-i", str(ROOT / d["file"]),
                          "-vf", f"fps={FPS},scale={vw}:{vh}:flags=lanczos", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    x0 = int((vw - W) * d.get("cx", 0.5))
    while True:
        buf = p.stdout.read(vw * vh * 3)
        if len(buf) < vw * vh * 3:
            break
        yield Image.frombytes("RGB", (vw, vh), buf).crop((x0, 0, x0 + W, H))
    p.wait()


def khung_anh(d):
    im = mo_anh({"file": d["file"], "giu_mau": d.get("giu_mau", False), "cat": d.get("cat")}, d.get("cat_tren", 0), d.get("cat_duoi", 0),
                rong_toi_da=2600)  # "cat": [x0, y0, x1, y1] tỉ lệ 0–1 → khung gần hơn (vd dãy biển hiệu)
    if d["loai"] == "anh_ngang":  # ảnh ngang: đặt hết bề ngang giữa khung, nền là chính nó làm mờ
        nen = nen_mo(im, W, H)
        a = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
        nen.paste(a, (0, d.get("y", 268)))  # sát dưới chữ đỉnh; ô chữ đặt dưới ảnh
        im = nen
    else:
        im = ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(d.get("cx", 0.5), 0.5))
    for _ in range(int(round(d["giay"] * FPS))):
        yield im


def ve_o_chu(im, o, a):
    """Ô chữ trắng bo góc giữa màn hình + dấu ngoặc kép (kiểu mẫu Hanoi Office); a = độ hiện 0–1."""
    if a <= 0:
        return im
    lop = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(lop)
    dong = o["dong"]
    cao = 34 + 42 * len(dong)
    y0 = o.get("y", 610) - cao // 2  # "y": tâm ô chữ (ảnh ngang → đặt ô dưới ảnh cho khỏi che)
    d.rounded_rectangle((70, y0, W - 70, y0 + cao), radius=18, fill=(255, 255, 255, int(236 * a)))
    d.ellipse((92, y0 - 22, 136, y0 + 22), fill=(10, 31, 68, int(255 * a)))
    d.text((114, y0 + 2), "❝", font=ImageFont.truetype("C:/Windows/Fonts/seguisym.ttf", 26), fill=(255, 255, 255, int(255 * a)), anchor="mm")
    for i, s in enumerate(dong):
        size = 30 if i == 0 else 25
        f = ImageFont.truetype(FONT, size)
        while d.textlength(s, font=f) > W - 180 and size > 16:
            size -= 1
            f = ImageFont.truetype(FONT, size)
        d.text((W / 2, y0 + 38 + 42 * i), s, font=f, fill=(10, 31, 68, int(255 * a)) if i == 0 else (60, 70, 90, int(255 * a)), anchor="mm")
    return Image.alpha_composite(im.convert("RGBA"), lop).convert("RGB")


def ve_dau(im, cfg):
    """Chữ nhỏ trên đỉnh suốt video (thay logo trong mẫu)."""
    d = ImageDraw.Draw(im, "RGBA")
    dt = cfg.get("dau_trang") or []
    if dt:
        chu(d, (W / 2, 214), dt[0], 24, (255, 255, 255), toi_da=W - 80)
    if len(dt) > 1:
        chu(d, (W / 2, 246), dt[1], 21, VANG, toi_da=W - 80)
    return im


def main():
    cp = Path(sys.argv[1])
    cfg = json.loads(cp.read_text(encoding="utf-8"))
    out = ROOT / cfg["ra"]
    out.parent.mkdir(parents=True, exist_ok=True)
    p = subprocess.Popen([ffmpeg(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-vf", "scale=1080:1920:flags=lanczos", "-c:v", "libx264", "-preset", "medium", "-threads", "2", "-x264-params",
                          "rc-lookahead=10", "-pix_fmt", "yuv420p", "-crf", "19", "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
    so, truoc, last = 0, None, None
    for d in cfg["doan"]:
        nguon = khung_video(d) if d["loai"] == "video" else khung_anh(d)
        for k, fr in enumerate(nguon):
            if truoc is not None and k < 9:  # mờ dần 0,3 giây sang cảnh mới
                fr = Image.blend(truoc, fr, (k + 1) / 10)
            t = so / FPS
            for o in cfg.get("o_chu", []):
                if o["tu"] <= t <= o["den"]:
                    fr = ve_o_chu(fr, o, min(1, (t - o["tu"]) / 0.25, (o["den"] - t) / 0.25))
            p.stdin.write(ve_dau(fr.copy(), cfg).tobytes())
            so += 1
            last = fr
        truoc = last
    p.stdin.close()
    p.wait()
    ghep_tieng(cfg, out, so / FPS)
    print("VIDEO:", out, f"{so / FPS:.1f} giây")


if __name__ == "__main__":
    main()
