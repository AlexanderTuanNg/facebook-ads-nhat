"""Dựng video dọc "định vị vị trí đắc địa" (kiểu Reels Vinhomes KingPark mẫu người dùng gửi 25/10/2026).

Nền: bản đồ OpenStreetMap (ODbL, BẮT BUỘC ghi "© OpenStreetMap contributors" — có sẵn ở góc video), tô tối + ánh xanh cho giống mẫu.
Cảnh: phóng dần từ toàn vùng → ghim phát sáng ở vị trí → nhãn địa điểm thật (lấy từ file cấu hình, đã kiểm trên bản đồ) hiện lần lượt
→ thẻ cuối: ảnh thật + vài dòng thông tin + số điện thoại. Không tự bịa địa điểm, không ghi khoảng cách nếu cấu hình không có.

  python tools/video_dinh_vi.py <cau_hinh.json>            # ra file .mp4 theo "ra" trong cấu hình
  python tools/video_dinh_vi.py <cau_hinh.json> --anh      # chỉ xuất 1 ảnh định vị (khung cuối phần bản đồ)

Cấu hình JSON: {"lat","lon","nhan_chinh","phu_de","moc":[{"ten","lat","lon"}],"the_cuoi":{"anh":[...],"dong":[...],"sdt"},
               "zoom_tu":12,"zoom_den":17,"giay_ban_do":11,"giay_the":6,"rong":720,"cao":1280,"ra":"..."}
"""
import json
import math
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
TILE_DIR = ROOT / "data" / "tiles"
UA = {"User-Agent": "YenThe-video-dinh-vi/1.0 (one-off render, cached)"}
FONT = "C:/Windows/Fonts/segoeuib.ttf"
FONT_THUONG = "C:/Windows/Fonts/segoeui.ttf"
VANG = (245, 194, 66)  # 26/10: vàng ánh kim (trước 255,204,0 chói, trông rẻ)
FPS = 30
# Bố cục "thẻ ảnh" (người dùng 26/10: "chữ với banner… ko bị che ảnh", "banner 500 triệu xuyên suốt video, ở trên đỉnh").
# Khung 720×1280: chữ/số chỉ nằm trong y 190–832 = vùng an toàn Reels (14–65%) ∩ phần bảng tin Facebook cắt 4:5 ở giữa (190–1090).
BANG = (190, 266)            # dải chữ cố định trên đỉnh, suốt video
O_ANH = (20, 326, 700, 712)  # ô flycam / ảnh toà nhà: ảnh hiện trọn, không chữ đè
O_THE = (20, 280, 700, 680)  # ô ảnh ở thẻ cuối; dưới ô là khung số điện thoại (694–832)


def ffmpeg() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def deg2px(lat, lon, z):
    n = 256 * 2 ** z
    x = (lon + 180) / 360 * n
    y = (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n
    return x, y


def tile(z, x, y) -> Image.Image:
    f = TILE_DIR / str(z) / str(x) / f"{y}.png"
    if not f.exists():
        f.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(f"https://tile.openstreetmap.org/{z}/{x}/{y}.png", headers=UA)
        f.write_bytes(urllib.request.urlopen(req, timeout=30).read())
        time.sleep(0.15)  # nhẹ tay với máy chủ OSM, có bộ nhớ đệm
    return Image.open(f).convert("RGB")


def nen_zoom(lat, lon, z, w, h) -> Image.Image:
    """Ảnh bản đồ w×h ở mức zoom nguyên z, tâm (lat, lon), đã tô tối."""
    cx, cy = deg2px(lat, lon, z)
    x0, y0 = cx - w / 2, cy - h / 2
    im = Image.new("RGB", (w, h))
    for tx in range(int(x0 // 256), int((x0 + w) // 256) + 1):
        for ty in range(int(y0 // 256), int((y0 + h) // 256) + 1):
            im.paste(tile(z, tx, ty), (int(tx * 256 - x0), int(ty * 256 - y0)))
    xam = ImageOps.grayscale(im)
    toi = ImageOps.colorize(ImageOps.invert(xam), black=(4, 10, 22), white=(70, 150, 170))
    return ImageEnhance.Contrast(toi).enhance(1.25)


OVERPASS = ("https://overpass-api.de/api/interpreter", "https://overpass.kumi.systems/api/interpreter")


def lay_vung(lat, lon, loai="building") -> list:
    """Đường viền (toà nhà hoặc khu đất) CHỨA ghim, lấy từ OSM; không có → toà nhà gần nhất trong 30 m; vẫn không → []."""
    import urllib.parse
    loc = {"building": '["building"]', "landuse": '["landuse"]'}[loai]
    q = (f'[out:json][timeout:40];is_in({lat},{lon})->.a;way(pivot.a){loc}->.w;'
         f'(.w;way(around:30,{lat},{lon}){loc};);out geom 3;')
    for ep in OVERPASS:
        try:
            req = urllib.request.Request(ep, data=urllib.parse.urlencode({"data": q}).encode(), headers=UA)
            el = json.load(urllib.request.urlopen(req, timeout=60)).get("elements", [])
            if el:
                return [[g["lat"], g["lon"]] for g in el[0]["geometry"]]
            return []
        except Exception as e:  # noqa: BLE001 — máy chủ bận thì thử máy chủ khác
            print("Overpass lỗi:", ep, type(e).__name__)
    return []


def chu(d, xy, s, size, fill, font=FONT, vien=True, canh="mm", toi_da=680):
    f = ImageFont.truetype(font, size)
    while size > 14 and d.textlength(s, font=f) > toi_da:  # tự thu nhỏ cho vừa khung dọc
        size -= 2
        f = ImageFont.truetype(font, size)
    if vien:
        d.text(xy, s, font=f, fill=(0, 0, 0), anchor=canh, stroke_width=max(2, size // 12), stroke_fill=(0, 0, 0))
    d.text(xy, s, font=f, fill=fill, anchor=canh)


def khung_ban_do(cfg, nen, t, T):
    """t: giây trong phần bản đồ (0..T). Zoom mượt bằng phóng ảnh giữa 2 mức nguyên."""
    w, h = cfg["rong"], cfg["cao"]
    z0, z1 = cfg["zoom_tu"], cfg["zoom_den"]
    p = min(1, t / (T * 0.45))  # 25/10 người dùng "cho tốc độ nhanh hơn": phóng xong trong 45% thời lượng
    p = p * p * (3 - 2 * p)
    z = z0 + (z1 - z0) * p
    zi = min(int(z), z1 - 1) if z < z1 else z1
    s = 2 ** (z - zi)
    base = nen[zi]
    cw, ch = w / s, h / s
    bx, by = base.size[0] / 2, base.size[1] / 2
    im = base.crop((int(bx - cw / 2), int(by - ch / 2), int(bx + cw / 2), int(by + ch / 2))).resize((w, h), Image.LANCZOS)
    zp = 2 ** z
    cx, cy = deg2px(cfg["lat"], cfg["lon"], 0)
    xy = lambda la, lo: (w / 2 + (deg2px(la, lo, 0)[0] - cx) * zp, h / 2 + (deg2px(la, lo, 0)[1] - cy) * zp)
    nhip = 0.5 + 0.5 * math.sin(t * 6)
    # khoanh vùng toà nhà/khu đất: viền vàng phát sáng + tô mờ (người dùng: "khoanh khu vực toà nhà vào")
    lop = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dl = ImageDraw.Draw(lop)
    vung = cfg.get("vung") or []
    if vung:
        pts = [xy(la, lo) for la, lo in vung]
        dl.polygon(pts, fill=(255, 204, 0, int(70 + 50 * nhip)))
        dl.line(pts + [pts[0]], fill=(255, 220, 60, 255), width=12, joint="curve")
    else:
        r = 46 + 10 * nhip
        dl.ellipse((w / 2 - r, h / 2 - r, w / 2 + r, h / 2 + r), outline=(255, 220, 60, 255), width=10, fill=(255, 204, 0, 80))
    sang = lop.filter(ImageFilter.GaussianBlur(14))
    im = Image.alpha_composite(Image.alpha_composite(im.convert("RGBA"), sang), lop)
    d = ImageDraw.Draw(im, "RGBA")
    if vung:
        d.line([xy(la, lo) for la, lo in vung] + [xy(*vung[0])], fill=(255, 255, 255, 235), width=3)
    d.ellipse((w / 2 - 8, h / 2 - 8, w / 2 + 8, h / 2 + 8), fill=(255, 255, 255, 255))
    for i, m in enumerate(cfg.get("moc", [])):
        t_hien = T * 0.42 + i * 0.25
        if t < t_hien:
            continue
        a = min(1, (t - t_hien) / 0.25)
        x, y = xy(m["lat"], m["lon"])
        if not (40 < x < w - 40 and 230 < y < h * 0.56):
            continue
        # tia sáng chạy từ mốc vào dự án (kiểu video mẫu), vẽ dần trong 0,6 giây
        b = min(1, (t - t_hien) / 0.6)
        ex, ey = x + (w / 2 - x) * b, y + (h / 2 - y) * b
        for rr, aa in ((9, 40), (5, 90), (2, 230)):
            d.line((x, y, ex, ey), fill=(120, 230, 255, int(aa * a)), width=rr)
        dai = 60 + (i % 3) * 45
        d.line((x, y, x, y - dai), fill=(255, 255, 255, int(220 * a)), width=3)
        d.ellipse((x - 8, y - 8, x + 8, y + 8), fill=(120, 230, 255, int(255 * a)))
        rong = d.textlength(m["ten"], font=ImageFont.truetype(FONT, 28))
        tx = min(max(x, rong / 2 + 14), w - rong / 2 - 14)
        chu(d, (tx, y - dai - 20), m["ten"], 28, (255, 255, 255, int(255 * a)))
    # ảnh nổi cả toà nhà/khu đất, có đường nối tới chỗ khoanh (người dùng: "cần ảnh cả toà nhà")
    anh = cfg.get("_anh_noi")
    if anh is not None and t > T * 0.40:
        a = min(1, (t - T * 0.40) / 0.35)
        aw, ah = anh.size
        x0, y0 = (w - aw) // 2, int(h * 0.60 + (1 - a) * 80)
        d.line((w / 2, h / 2 + 12, w / 2, y0), fill=(255, 220, 60, int(255 * a)), width=4)
        khung = Image.new("RGBA", (aw + 12, ah + 12), (255, 204, 0, int(255 * a)))
        m = Image.new("L", khung.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, aw + 11, ah + 11), radius=22, fill=int(255 * a))
        im.paste(khung, (x0 - 6, y0 - 6), m)
        m2 = Image.new("L", (aw, ah), 0)
        ImageDraw.Draw(m2).rounded_rectangle((0, 0, aw - 1, ah - 1), radius=18, fill=int(255 * a))
        im.paste(anh, (x0, y0), m2)
        d = ImageDraw.Draw(im, "RGBA")
    a = min(1, t / 0.6)
    chu(d, (w / 2, 140), cfg["nhan_chinh"], 58, VANG + (int(255 * a),))
    if cfg.get("phu_de") and t > 0.5:
        chu(d, (w / 2, 205), cfg["phu_de"], 30, (255, 255, 255, int(255 * min(1, (t - 0.5) / 0.4))))
    chu(d, (w - 12, h - 14), "© OpenStreetMap contributors", 18, (220, 220, 220), font=FONT_THUONG, vien=False, canh="rb")
    return im.convert("RGB")


def lam_dep(im):
    """Chỉnh ảnh đồng bộ cho cả video: kéo tương phản giữ tông, sáng nhẹ, ấm nhẹ, tươi nhẹ, nét nhẹ (26/10: 'trông vẫn amateur')."""
    im = ImageOps.autocontrast(im, cutoff=0.4, preserve_tone=True)
    im = ImageEnhance.Color(ImageEnhance.Brightness(im).enhance(1.04)).enhance(1.08)
    r, g, b = im.split()
    im = Image.merge("RGB", (r.point(lambda v: min(255, int(v * 1.03))), g, b.point(lambda v: int(v * 0.97))))
    return im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=3))


def o_anh(cfg):
    """Ô flycam/ảnh toà nhà, dời xuống theo chiều cao dải đỉnh (dải có số điện thoại cao thêm _dy px)."""
    return (O_ANH[0], O_ANH[1] + cfg.get("_dy", 0), O_ANH[2], O_ANH[3])


def mo_anh(f, cat_tren=0.0, cat_duoi=0.0, rong_toi_da=1400) -> Image.Image:
    """Mở ảnh (đường dẫn, hoặc {"file", "cat": [x0, y0, x1, y1] tỉ lệ 0–1}), bỏ băng chữ in sẵn ở mép, chỉnh màu;
    thu nhỏ trước cho nhanh; KHÔNG cắt theo khung video (ảnh hiện trọn trong ô)."""
    cat, giu = None, False
    if isinstance(f, dict):  # "giu_mau": ảnh người dùng đã chỉnh sẵn → không chỉnh màu thêm
        cat, giu, f = f.get("cat"), f.get("giu_mau", False), f["file"]
    im = Image.open(ROOT / f).convert("RGB")
    if cat:
        im = im.crop((int(im.width * cat[0]), int(im.height * cat[1]), int(im.width * cat[2]), int(im.height * cat[3])))
    elif cat_tren or cat_duoi:
        im = im.crop((0, int(im.height * cat_tren), im.width, int(im.height * (1 - cat_duoi))))
    if im.width > rong_toi_da:
        im = im.resize((rong_toi_da, int(im.height * rong_toi_da / im.width)), Image.LANCZOS)
    return im if giu else lam_dep(im)


def nen_mo(anh, w, h) -> Image.Image:
    """Nền: chính ảnh đó phủ kín khung rồi làm mờ, tối đi (chữ và ô ảnh nằm trên nền này, không đè lên ảnh chính)."""
    r = max(w / anh.width, h / anh.height)
    im = anh.resize((int(anh.width * r) + 1, int(anh.height * r) + 1))
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return ImageEnhance.Brightness(im.crop((x, y, x + w, y + h)).filter(ImageFilter.GaussianBlur(24))).enhance(0.42)


def dat_anh(nen, anh, box, phong=1.0, bo=18) -> Image.Image:
    """Đặt ảnh VỪA KHÍT trong ô (giữ tỉ lệ, hiện trọn ảnh), bo góc, viền vàng mảnh, bóng mờ; phong > 1 = đẩy nhẹ bên trong ô."""
    x0, y0, x1, y1 = box
    r = min((x1 - x0) / anh.width, (y1 - y0) / anh.height)
    fw, fh = int(anh.width * r), int(anh.height * r)
    a2 = anh.resize((max(fw, int(fw * phong)), max(fh, int(fh * phong))), Image.LANCZOS)
    cx, cy = (a2.width - fw) // 2, (a2.height - fh) // 2
    a2 = a2.crop((cx, cy, cx + fw, cy + fh))
    px, py = x0 + ((x1 - x0) - fw) // 2, y0 + ((y1 - y0) - fh) // 2
    bong = Image.new("RGBA", nen.size, (0, 0, 0, 0))
    ImageDraw.Draw(bong).rounded_rectangle((px - 6, py + 8, px + fw + 6, py + fh + 20), radius=bo + 6, fill=(0, 0, 0, 175))
    nen = Image.alpha_composite(nen.convert("RGBA"), bong.filter(ImageFilter.GaussianBlur(14))).convert("RGB")
    ImageDraw.Draw(nen).rounded_rectangle((px - 2, py - 2, px + fw + 1, py + fh + 1), radius=bo + 2, fill=(255, 255, 255))  # viền trắng mảnh
    m = Image.new("L", (fw, fh), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, fw - 1, fh - 1), radius=bo, fill=255)
    nen.paste(a2, (px, py), m)
    return nen


def khung_the(cfg, anh, nen, t, T):
    """Thẻ cuối: ảnh thật chạy lần lượt trong ô trên (hiện trọn, không chữ đè) + khung số điện thoại bên dưới ô ảnh."""
    w = cfg["rong"]
    tc = cfg["the_cuoi"]
    dong = tc.get("dong") or []
    o = (O_THE[0], O_THE[1] + cfg.get("_dy", 0), O_THE[2], O_THE[3] - 32 * max(0, len(dong) - 1))  # thêm dòng chữ → ô ảnh thấp lại, không đè
    n = len(anh)
    doan = T / n
    cache = cfg.setdefault("_the_cache", {})

    def ve(k, tt):  # 26/10 người dùng "ảnh bị rung rung, đừng cho rung": ảnh đứng yên (bỏ phóng nhẹ làm ảnh nhảy 1 px), vẽ 1 lần rồi dùng lại
        if k not in cache:
            cache[k] = dat_anh(nen[k].copy(), anh[k], o)
        return cache[k].copy()
    k = min(n - 1, int(t / doan))
    tt = t - k * doan
    im = ve(k, tt)
    if k < n - 1 and tt > doan - 0.35:  # chuyển ảnh mờ dần 0,35 giây
        im = Image.blend(im, ve(k + 1, 0), (tt - (doan - 0.35)) / 0.35)
    d = ImageDraw.Draw(im, "RGBA")
    y = o[3] + 14
    d.rounded_rectangle((32, y, w - 32, 832), radius=22, fill=(0, 22, 60, 232), outline=(255, 255, 255, 70), width=1)
    for i, s in enumerate(dong):
        chu(d, (w / 2, y + 28 + 32 * i), s, 25 if i == 0 else 21, (255, 255, 255) if i == 0 else (255, 226, 122), toi_da=w - 100)
    yp = 832 - 14 - 72
    d.rounded_rectangle((w / 2 - 230, yp, w / 2 + 230, yp + 72), radius=36, fill=VANG + (255,))
    chu(d, (w / 2, yp + 36), tc["sdt"], 46, (0, 35, 100), vien=False)
    return im


def khung_phap_ly(cfg):
    """Đoạn pháp lý: câu pháp lý chuẩn (checklist F5) ở trên, ảnh lễ bàn giao GCN hiện trọn từng ảnh trong ô lớn, chú thích ở dưới.
    Người dùng 26/10: "thêm ảnh sổ đỏ trao tay, đủ điều kiện chuyển nhượng" — cụm "sổ đỏ trao tay" là từ cấm (F2) nên không ghi."""
    pl = cfg["doan_phap_ly"]
    w, h = cfg["rong"], cfg["cao"]
    anh = [mo_anh(a) for a in pl["anh"]]
    nen = [nen_mo(a, w, h) for a in anh]
    T = pl.get("giay", 3.2)
    n = len(anh)
    doan = T / n
    dy = cfg.get("_dy", 0)
    o = (20, 360 + dy, 700, 786)

    cache = {}

    def ve(k, tt):  # ảnh đứng yên, không rung (26/10)
        if k in cache:
            return cache[k].copy()
        im = dat_anh(nen[k].copy(), anh[k], o)
        d = ImageDraw.Draw(im, "RGBA")
        chu(d, (w / 2, 298 + dy), pl["tieu_de"], 32, VANG, toi_da=w - 80)
        if pl.get("phu"):
            chu(d, (w / 2, 336 + dy), pl["phu"], 22, (255, 255, 255), toi_da=w - 60)
        if pl.get("chu_duoi"):
            chu(d, (w / 2, 810), pl["chu_duoi"], 20, (255, 255, 255), toi_da=w - 60)
        cache[k] = im
        return im.copy()
    for i in range(int(T * FPS)):
        t = i / FPS
        k = min(n - 1, int(t / doan))
        tt = t - k * doan
        im = ve(k, tt)
        if k < n - 1 and tt > doan - 0.3:
            im = Image.blend(im, ve(k + 1, 0), (tt - (doan - 0.3)) / 0.3)
        yield im


def khung_tuyen_anh(cfg):
    """Chèn giữa đoạn bay ("chen_giua_ban_do"): 3 hàng ảnh thật xếp dọc, mỗi hàng ảnh bên trái + tên/khoảng cách bên phải
    (người dùng 26/10: "thêm ảnh toà nhà và tt hành chính công bên cạnh cho dễ hình dung"). Hàng hiện dần, ảnh đứng yên."""
    cg = cfg["chen_giua_ban_do"]
    w, h = cfg["rong"], cfg["cao"]
    dy = cfg.get("_dy", 0)
    hang = cg["hang"]
    anh = [ImageOps.fit(mo_anh({"file": x["anh"], "giu_mau": x.get("giu_mau", False)}), (300, 146), Image.LANCZOS, centering=(0.5, 0.45)) for x in hang]
    nen = nen_mo(mo_anh({"file": hang[0]["anh"], "giu_mau": True}), w, h)
    y0, buoc = 278 + dy, 160
    lop = [y0 + k * buoc for k in range(len(hang))]  # đỉnh từng hàng ảnh
    # vẽ tĩnh: nền + từng hàng (ảnh, tên, khoảng cách); đường nối vàng mảnh giữa các ảnh
    hinh = []
    for n in range(1, len(hang) + 1):
        im = nen.copy()
        d = ImageDraw.Draw(im, "RGBA")
        for k in range(n):
            y = lop[k]
            if k:
                d.line((174, lop[k - 1] + 150, 174, y - 4), fill=VANG + (230,), width=3)
            im = dat_anh(im, anh[k], (24, y, 324, y + 146), bo=12)
            d = ImageDraw.Draw(im, "RGBA")
            chu(d, (340, y + 52), hang[k]["ten"], 24, (255, 255, 255), canh="lm", toi_da=360)
            if hang[k].get("phu"):
                chu(d, (340, y + 92), hang[k]["phu"], 21, VANG, canh="lm", toi_da=360)
        if cg.get("chu_thich"):
            chu(d, (w / 2, 826), cg["chu_thich"], 14, (225, 225, 225), font=FONT_THUONG, toi_da=w - 40)
        hinh.append(im)
    so = int(round((cg["den"] - cg["tu"]) * FPS))
    hien = cg.get("hien_cach", 0.45)  # mỗi hàng hiện sau hàng trước 0,45 giây, mờ dần 0,25 giây
    for i in range(so):
        t = i / FPS
        k = min(len(hang) - 1, int(t / hien))
        im = hinh[k]
        if k < len(hang) - 1 and t - k * hien > hien - 0.25:
            im = Image.blend(hinh[k], hinh[k + 1], (t - k * hien - (hien - 0.25)) / 0.25)
        yield im.copy()


def khung_anh_rieng(cfg, T=2.2):
    """Nhịp riêng ảnh cả toà nhà/khu đất: ảnh hiện trọn trong ô, tiêu đề ở dải trên ô (không đè lên ảnh)."""
    w, h = cfg["rong"], cfg["cao"]
    anh = mo_anh({"file": cfg["anh_noi"], "giu_mau": cfg.get("anh_noi_giu_mau", False)})
    nen = nen_mo(anh, w, h)
    o = o_anh(cfg)
    im = dat_anh(nen.copy(), anh, (o[0], o[1], o[2], o[3] + 60))  # ảnh đứng yên, không rung (26/10)
    d = ImageDraw.Draw(im, "RGBA")
    chu(d, (w / 2, 300 + cfg.get("_dy", 0)), cfg.get("anh_noi_chu", ""), 34, VANG, toi_da=w - 90)
    duoi = cfg.get("anh_noi_chu_duoi")  # 26/10: dòng dưới ảnh (cùng toà nhà với…, tiện ích); 1 chuỗi hoặc danh sách 2 dòng
    for i, s in enumerate([duoi] if isinstance(duoi, str) else (duoi or [])):
        chu(d, (w / 2, o[3] + (88 if isinstance(duoi, str) else 80 + 30 * i)), s, 24 if i == 0 else 21,
            (255, 255, 255) if i == 0 else VANG, toi_da=w - 60)
    for i in range(int(T * FPS)):
        yield im.copy()


def khung_ve_tinh(cfg, T):
    """Đoạn mở đầu bay 3D trên ảnh vệ tinh (tools/bay_ve_tinh.py) thay cho bản đồ vẽ; dán ảnh nổi toà nhà/khu đất ở cuối đoạn."""
    w, h = cfg["rong"], cfg["cao"]
    f = ROOT / cfg["ban_do_video"]
    p = subprocess.Popen([ffmpeg(), "-loglevel", "error", "-i", str(f), "-vf", f"fps={FPS},scale={w}:{h}", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    n = 0
    anh = cfg.get("_anh_noi")
    while True:
        buf = p.stdout.read(w * h * 3)
        if len(buf) < w * h * 3:
            break
        im = Image.frombytes("RGB", (w, h), buf)
        t = n / FPS
        n += 1
        yield im
    p.wait()


def khung_video(cfg):
    """Chèn đoạn video thật (flycam) giữa phần bản đồ và thẻ cuối: video hiện trọn trong ô, tiêu đề ở trên ô, chú thích ở dưới ô."""
    cv = cfg["chen_video"]
    w, h = cfg["rong"], cfg["cao"]
    vw, vh = 1280, 720
    p = subprocess.Popen([ffmpeg(), "-loglevel", "error", "-ss", str(cv.get("tu", 0)), "-t", str(cv.get("dai", 4)), "-i", str(ROOT / cv["file"]),
                          "-vf", f"fps={FPS},scale={vw}:{vh}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    while True:
        buf = p.stdout.read(vw * vh * 3)
        if len(buf) < vw * vh * 3:
            break
        fr = ImageEnhance.Color(ImageEnhance.Contrast(Image.frombytes("RGB", (vw, vh), buf)).enhance(1.05)).enhance(1.08)
        im = dat_anh(nen_mo(fr.resize((320, 180)), w, h), fr, o_anh(cfg))
        d = ImageDraw.Draw(im, "RGBA")
        chu(d, (w / 2, 300 + cfg.get("_dy", 0)), cv.get("tieu_de", ""), 34, VANG)
        if cv.get("chu_duoi"):
            chu(d, (w / 2, O_ANH[3] - 12 + 40), cv["chu_duoi"], 24, (255, 255, 255), toi_da=w - 80)
        yield im
    p.wait()


def ghep_tieng(cfg, video: Path, giay: float) -> None:
    """Ghép tiếng: nhạc nền tự tổng hợp + lời đọc; nhạc tự nhỏ khi có lời (sidechaincompress); chuẩn −14 LUFS, đỉnh −1,5 dBTP
    bằng loudnorm 2 lượt; AAC stereo 48 kHz 192 kbps (nghiên cứu 26/10 `reports/2026-10-26-nghien-cuu-video-vi-tri.md` mục 5)."""
    import re as _re
    co_doc = bool(cfg.get("loi_doc"))
    if not cfg.get("nhac_nen") and not co_doc:
        return
    tam = video.with_name(video.stem + "-tam.mp4")
    video.replace(tam)
    vao, loc = ["-i", str(tam)], []
    if cfg.get("nhac_nen"):
        tan = [261.63, 329.63, 392.00, 220.00, 277.18, 329.63]
        for f in tan:
            vao += ["-f", "lavfi", "-i", f"sine=frequency={f}:sample_rate=48000:duration={giay}"]
        loc.append("".join(f"[{i + 1}:a]" for i in range(len(tan))) + f"amix=inputs={len(tan)}:normalize=0,volume=0.6,"
                   f"tremolo=f=0.25:d=0.5,aecho=0.8:0.7:180|360:0.3|0.2,lowpass=f=1800,aformat=channel_layouts=stereo,"
                   f"afade=t=in:d=1.2,afade=t=out:st={max(0, giay - 1.5)}:d=1.5[nhac]")
    if co_doc:
        k = sum(1 for x in vao if x == "-i")
        vao += ["-i", str(ROOT / cfg["loi_doc"])]
        tre = int(cfg.get("doc_tre", 0.4) * 1000)
        loc.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={tre}|{tre},apad=whole_dur={giay},asplit=2[doc][khoa]")
    if cfg.get("nhac_nen") and co_doc:
        loc.append("[nhac][khoa]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=350:makeup=1[nhacnho]")
        loc.append("[nhacnho][doc]amix=inputs=2:normalize=0:duration=longest[tron]")
    elif co_doc:
        loc.append("[doc]anull[tron]"); loc.append("[khoa]anullsink")
    else:
        loc.append("[nhac]anull[tron]")
    loc_do = ";".join(loc) + f";[tron]atrim=0:{giay},loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json[ra]"
    r = subprocess.run([ffmpeg(), "-hide_banner", *vao, "-filter_complex", loc_do, "-map", "[ra]", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = _re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr)
    do = json.loads(m.group(0)) if m else None
    ln = ("loudnorm=I=-14:TP=-1.5:LRA=11:linear=true:" + f"measured_I={do['input_i']}:measured_TP={do['input_tp']}:"
          f"measured_LRA={do['input_lra']}:measured_thresh={do['input_thresh']}:offset={do['target_offset']}") if do else          "loudnorm=I=-14:TP=-1.5:LRA=11"
    loc_ra = ";".join(loc) + f";[tron]atrim=0:{giay},{ln},aresample=48000[ra]"
    subprocess.run([ffmpeg(), "-y", "-loglevel", "error", *vao, "-filter_complex", loc_ra, "-map", "0:v", "-map", "[ra]",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest", str(video)], check=True)
    tam.unlink()

def ve_bang(im, cfg):
    """Dải chữ cố định trên đỉnh suốt video ("bang_tren": dong1 = câu chính, dong2 = điều kiện) + nhãn "Giọng đọc AI"."""
    b = cfg.get("bang_tren")
    if not b:
        return im
    w = im.width
    d = ImageDraw.Draw(im, "RGBA")
    y0, y1 = BANG[0], BANG[1] + cfg.get("_dy", 0)
    d.rectangle((0, y0, w, y1), fill=(0, 30, 90, 238))
    d.rectangle((0, y1 - 3, w, y1), fill=VANG + (255,))
    chu(d, (w / 2, y0 + 26), b["dong1"], 32, VANG, toi_da=w - 150)
    if b.get("dong2"):
        chu(d, (w / 2, y0 + 56), b["dong2"], 19, (255, 255, 255), font=FONT_THUONG, vien=False, toi_da=w - 36)
    if b.get("sdt"):  # 26/10 người dùng: "ghi sđt ở ngay trên banner"
        d.rounded_rectangle((w / 2 - 175, y0 + 74, w / 2 + 175, y0 + 110), radius=18, fill=VANG + (255,))
        chu(d, (w / 2, y0 + 92), "Gọi/Zalo " + b["sdt"], 25, (0, 35, 100), vien=False)
    if cfg.get("loi_doc") and cfg.get("nhan_ai", True):  # nhãn nội dung AI (Luật TTNT 134/2025 Đ.11, NĐ 142/2026 — cần luật sư xác nhận)
        d.text((w - 8, y0 + 3), "Giọng đọc AI", font=ImageFont.truetype(FONT_THUONG, 13), fill=(220, 230, 255, 235), anchor="ra")
    return im


def ve_phu_de(im, cfg, tg, y0=None):
    """Phụ đề từng câu khớp lời đọc (mốc thời gian lấy từ edge-tts SentenceBoundary, lưu cạnh file lời đọc).
    "phu_de_tat": true → không vẽ (26/10: mọi câu đọc đã có trên dải đỉnh/tiêu đề/nhãn bản đồ/thẻ cuối, hộp phụ đề chỉ che ảnh)."""
    if cfg.get("loi_doc") and cfg.get("nhan_ai", True) and not cfg.get("bang_tren"):  # nhãn nội dung AI ("nhan_ai": false → ghi ở chú thích bài) (Luật TTNT 134/2025 Đ.11 — cần luật sư xác nhận; Meta AI label)
        ImageDraw.Draw(im, "RGBA").text((46, int(im.height * 0.145)), "Giọng đọc AI", font=ImageFont.truetype(FONT_THUONG, 18),
                                       fill=(255, 255, 255, 210), stroke_width=2, stroke_fill=(0, 0, 0, 160))
    if cfg.get("phu_de_tat"):
        return im
    pd = cfg.get("_phu_de") or []
    tg -= cfg.get("doc_tre", 0.4)
    cau = next((c for c in pd if c["tu"] <= tg <= c["den"] + 0.15), None)
    if not cau:
        return im
    w = im.width
    d = ImageDraw.Draw(im, "RGBA")
    f = ImageFont.truetype(FONT, 30)
    tu = cau["chu"].split()
    dong, cur = [], ""
    for x in tu:  # ngắt dòng ≤ 92% bề rộng
        thu = (cur + " " + x).strip()
        if d.textlength(thu, font=f) > w * 0.86 and cur:
            dong.append(cur); cur = x
        else:
            cur = thu
    dong.append(cur)
    cao = 44 * len(dong) + 18
    if y0 is None:
        y0 = int(im.height * 0.55)  # vùng an toàn Reels: phụ đề ở 0,55–0,64H
    d.rounded_rectangle((w * 0.04, y0, w * 0.96, y0 + cao), radius=16, fill=(0, 0, 0, 150))
    for k, line in enumerate(dong):
        d.text((w / 2, y0 + 30 + 44 * k), line, font=f, fill=(255, 255, 255), anchor="mm")
    return im


def chuan_anh(f, w, h, cat_duoi=0.0, cat_tren=0.0):
    im = Image.open(f).convert("RGB")
    if cat_tren:  # bỏ nhãn số ảnh ("VĂN PHÒNG TẦNG 2 • 04/10") ở góc trên ảnh gốc
        im = im.crop((0, int(im.height * cat_tren), im.width, im.height))
    if cat_duoi:  # bỏ băng chữ có sẵn ở đáy ảnh gốc (ảnh cho thuê có thanh xanh + số điện thoại)
        im = im.crop((0, 0, im.width, int(im.height * (1 - cat_duoi))))
    r = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def main():
    cfg = {"zoom_tu": 12, "zoom_den": 17, "giay_ban_do": 7, "giay_the": 5, "rong": 720, "cao": 1280}
    cfg.update(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    cfg["_dy"] = 44 if (cfg.get("bang_tren") or {}).get("sdt") else 0  # dải đỉnh có số điện thoại → cao thêm 44 px
    w, h = cfg["rong"], cfg["cao"]
    nen = {} if (cfg.get("ban_do_video") or cfg.get("bo_ban_do")) else {z: nen_zoom(cfg["lat"], cfg["lon"], z, w * 2 if z < cfg["zoom_den"] else w, h * 2 if z < cfg["zoom_den"] else h)
           for z in range(cfg["zoom_tu"], cfg["zoom_den"] + 1)}
    T = cfg["giay_ban_do"]
    if cfg.get("tu_lay_vung") and not cfg.get("vung"):
        cfg["vung"] = lay_vung(cfg["lat"], cfg["lon"], cfg.get("loai_vung", "building"))
        print("Đường viền lấy từ OSM:", len(cfg["vung"]), "điểm" if cfg["vung"] else "(không có → khoanh tròn)")
    if cfg.get("anh_noi"):
        a = Image.open(ROOT / cfg["anh_noi"]).convert("RGB")
        aw = int(w * 0.84)
        cfg["_anh_noi"] = a.resize((aw, int(a.height * aw / a.width)), Image.LANCZOS)
        if cfg["_anh_noi"].height > int(h * 0.25):
            hh = int(h * 0.25); oy = (cfg["_anh_noi"].height - hh) // 2
            cfg["_anh_noi"] = cfg["_anh_noi"].crop((0, oy, aw, oy + hh))
    if "--anh" in sys.argv:
        out = ROOT / Path(cfg["ra"]).with_suffix(".jpg")
        out.parent.mkdir(parents=True, exist_ok=True)
        khung_ban_do(cfg, nen, T, T).save(out, quality=92)
        print("ẢNH:", out)
        return
    pdf = ROOT / Path(cfg["loi_doc"]).with_suffix(".json") if cfg.get("loi_doc") else None
    cfg["_phu_de"] = json.loads(pdf.read_text(encoding="utf-8")) if pdf and pdf.exists() else []
    tc = cfg["the_cuoi"]
    anh = [mo_anh(a, tc.get("cat_tren", 0), tc.get("cat_duoi", 0)) for a in tc["anh"]]
    nen_the = [nen_mo(a, w, h) for a in anh]
    out = ROOT / cfg["ra"]
    out.parent.mkdir(parents=True, exist_ok=True)
    p = subprocess.Popen([ffmpeg(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}", "-r", str(FPS),
                          "-i", "-", "-vf", f"scale={cfg.get('xuat_rong', 1080)}:{cfg.get('xuat_cao', 1920)}:flags=lanczos", "-c:v", "libx264", "-preset", "medium", "-threads", "2", "-x264-params", "rc-lookahead=10", "-pix_fmt", "yuv420p", "-crf", "19", "-movflags", "+faststart", str(out)],
                         stdin=subprocess.PIPE)
    so = 0
    ghi = lambda fr, y0=None: p.stdin.write(ve_bang(ve_phu_de(fr, cfg, so / FPS, y0=y0), cfg).tobytes())  # dải đỉnh vẽ sau cùng, trên mọi cảnh
    if cfg.get("bo_ban_do"):  # 26/10: video "bên trong văn phòng" — không có đoạn bản đồ, mở bằng ảnh toà nhà
        if cfg.get("anh_noi"):
            for fr in khung_anh_rieng(cfg, cfg.get("giay_anh_noi", 2.2)):
                ghi(fr); so += 1
    elif cfg.get("ban_do_video") and (ROOT / cfg["ban_do_video"]).exists():
        cg = cfg.get("chen_giua_ban_do")
        chen = khung_tuyen_anh(cfg) if cg else None
        for i, fr in enumerate(khung_ve_tinh(cfg, T)):
            if cg and cg["tu"] <= i / FPS < cg["den"]:  # thay khung bay bằng khung ảnh, giữ nguyên độ dài để khớp lời đọc
                fr = next(chen, fr)
            ghi(fr); so += 1
        if cfg.get("anh_noi"):
            for fr in khung_anh_rieng(cfg, cfg.get("giay_anh_noi", 2.2)):
                ghi(fr); so += 1
    else:
        for i in range(int(T * FPS)):
            ghi(khung_ban_do(cfg, nen, i / FPS, T)); so += 1
    if cfg.get("chen_video"):
        for fr in khung_video(cfg):
            ghi(fr, int(cfg["cao"] * 0.17)); so += 1
    if cfg.get("doan_phap_ly"):
        for fr in khung_phap_ly(cfg):
            ghi(fr); so += 1
    for i in range(int(cfg["giay_the"] * FPS)):
        ghi(khung_the(cfg, anh, nen_the, i / FPS, cfg["giay_the"]), int(cfg["cao"] * 0.17)); so += 1
    p.stdin.close()
    p.wait()
    ghep_tieng(cfg, out, so / FPS)
    print("VIDEO:", out, f"{T + cfg['giay_the'] + (cfg.get('chen_video') or {}).get('dai', 0)} giây", f"{w}x{h}")


if __name__ == "__main__":
    main()
