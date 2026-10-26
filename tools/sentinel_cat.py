"""Cắt ảnh vệ tinh Sentinel-2 màu thật (10 m) từ kho mở AWS (Element 84 Earth Search) — dùng thương mại được.

Người dùng 26/10/2026 đồng ý đổi ảnh vệ tinh sang Sentinel-2 ("1. ok"), vì Esri World Imagery cần giấy phép trả phí
và Google Earth cấm dùng cho quảng bá (nghiên cứu `workspace/reports/2026-10-26-nghien-cuu-video-vi-tri.md` mục 2).
Giấy phép Copernicus Sentinel: tự do sao chép, chỉnh sửa, dùng thương mại; BẮT BUỘC ghi
"Contains modified Copernicus Sentinel data <năm>".

Chỉ tải đúng các ô 1024×1024 của tệp TCI.tif (COG, nén DEFLATE + predictor 2) giao với vùng cần — không tải cả tệp.

  python tools/sentinel_cat.py <cau_hinh.json>
Cấu hình đọc: lat, lon (tâm) hoặc "sentinel": {"tam":[lat,lon], "rong_km":30, "cao_km":30, "canh":"S2C_48QXJ_20260107_0_L2A"}
Ghi: <thư mục cấu hình>/sentinel.jpg + cập nhật cấu hình "anh_ve_tinh": {"file", "goc": [[lon,lat]×4 TL,TR,BR,BL], "nguon"}
"""
import json
import math
import struct
import sys
import urllib.request
import zlib
from itertools import accumulate
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

ROOT = Path(__file__).resolve().parents[1]
UA = {"User-Agent": "YenThe-video-dinh-vi/1.0"}
A, F = 6378137.0, 1 / 298.257223563
K0 = 0.9996


def latlon_utm(lat, lon, zone):
    e2 = F * (2 - F); ep2 = e2 / (1 - e2)
    l0 = math.radians((zone - 1) * 6 - 180 + 3)
    p, l = math.radians(lat), math.radians(lon)
    N = A / math.sqrt(1 - e2 * math.sin(p) ** 2); T = math.tan(p) ** 2; C = ep2 * math.cos(p) ** 2; Aa = math.cos(p) * (l - l0)
    M = A * ((1 - e2 / 4 - 3 * e2 ** 2 / 64 - 5 * e2 ** 3 / 256) * p - (3 * e2 / 8 + 3 * e2 ** 2 / 32 + 45 * e2 ** 3 / 1024) * math.sin(2 * p)
             + (15 * e2 ** 2 / 256 + 45 * e2 ** 3 / 1024) * math.sin(4 * p) - (35 * e2 ** 3 / 3072) * math.sin(6 * p))
    x = K0 * N * (Aa + (1 - T + C) * Aa ** 3 / 6 + (5 - 18 * T + T * T + 72 * C - 58 * ep2) * Aa ** 5 / 120) + 500000
    y = K0 * (M + N * math.tan(p) * (Aa * Aa / 2 + (5 - T + 9 * C + 4 * C * C) * Aa ** 4 / 24
                                    + (61 - 58 * T + T * T + 600 * C - 330 * ep2) * Aa ** 6 / 720))
    return x, y


def utm_latlon(x, y, zone):
    e2 = F * (2 - F); ep2 = e2 / (1 - e2); e1 = (1 - math.sqrt(1 - e2)) / (1 + math.sqrt(1 - e2))
    l0 = math.radians((zone - 1) * 6 - 180 + 3)
    M = y / K0; mu = M / (A * (1 - e2 / 4 - 3 * e2 ** 2 / 64 - 5 * e2 ** 3 / 256))
    p1 = mu + (3 * e1 / 2 - 27 * e1 ** 3 / 32) * math.sin(2 * mu) + (21 * e1 ** 2 / 16 - 55 * e1 ** 4 / 32) * math.sin(4 * mu) \
        + (151 * e1 ** 3 / 96) * math.sin(6 * mu) + (1097 * e1 ** 4 / 512) * math.sin(8 * mu)
    N1 = A / math.sqrt(1 - e2 * math.sin(p1) ** 2); T1 = math.tan(p1) ** 2; C1 = ep2 * math.cos(p1) ** 2
    R1 = A * (1 - e2) / (1 - e2 * math.sin(p1) ** 2) ** 1.5; D = (x - 500000) / (N1 * K0)
    lat = p1 - (N1 * math.tan(p1) / R1) * (D * D / 2 - (5 + 3 * T1 + 10 * C1 - 4 * C1 * C1 - 9 * ep2) * D ** 4 / 24
                                          + (61 + 90 * T1 + 298 * C1 + 45 * T1 * T1 - 252 * ep2 - 3 * C1 * C1) * D ** 6 / 720)
    lon = l0 + (D - (1 + 2 * T1 + C1) * D ** 3 / 6 + (5 - 2 * C1 + 28 * T1 - 3 * C1 * C1 + 8 * ep2 + 24 * T1 * T1) * D ** 5 / 120) / math.cos(p1)
    return math.degrees(lat), math.degrees(lon)


def doc_khoang(url, a, b):
    req = urllib.request.Request(url, headers={**UA, "Range": f"bytes={a}-{b}"})
    return urllib.request.urlopen(req, timeout=90).read()


def doc_ifd0(url):
    h = doc_khoang(url, 0, 65535)
    assert h[:2] == b"II" and struct.unpack("<H", h[2:4])[0] == 42, "không phải TIFF thường"
    off = struct.unpack("<I", h[4:8])[0]
    n = struct.unpack("<H", h[off:off + 2])[0]
    t = {}
    for i in range(n):
        tag, typ, cnt, val = struct.unpack("<HHII", h[off + 2 + 12 * i:off + 14 + 12 * i])
        t[tag] = (typ, cnt, val)

    def mang(tag):
        typ, cnt, val = t[tag]
        sz = {3: 2, 4: 4, 16: 8}[typ]
        fm = {3: "H", 4: "I", 16: "Q"}[typ]
        if cnt * sz <= 4:
            return [val]
        return list(struct.unpack("<" + fm * cnt, h[val:val + cnt * sz]))
    assert t[259][2] == 8 and t[317][2] == 2 and t[277][2] == 3, "cần DEFLATE + predictor 2 + 3 kênh"
    return {"W": t[256][2], "H": t[257][2], "tw": t[322][2], "th": t[323][2], "toff": mang(324), "tcnt": mang(325)}


def giai_o(raw, tw, th):
    b = bytearray(zlib.decompress(raw))
    hang = tw * 3
    for r in range(th):  # predictor 2: cộng dồn theo hàng, từng kênh (mod 256)
        s = r * hang
        for c in range(3):
            b[s + c:s + hang:3] = bytes(accumulate(b[s + c:s + hang:3], lambda x, y: (x + y) & 255))
    return Image.frombytes("RGB", (tw, th), bytes(b))


def main():
    cp = Path(sys.argv[1]).resolve()
    cfg = json.loads(cp.read_text(encoding="utf-8"))
    sc = {"tam": [cfg["lat"], cfg["lon"]], "rong_km": 30, "cao_km": 30, "canh": "S2C_48QXJ_20260107_0_L2A"}
    sc.update(cfg.get("sentinel", {}))
    item = json.load(urllib.request.urlopen(urllib.request.Request(
        f"https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/{sc['canh']}", headers=UA), timeout=90))
    url = item["assets"]["visual"]["href"]
    epsg = item["properties"].get("proj:epsg") or int(str(item["properties"].get("proj:code", "EPSG:32648")).split(":")[-1])
    zone = epsg - 32600
    tf = item["assets"]["visual"]["proj:transform"]  # [10, 0, X0, 0, -10, Y0]
    res, X0, Y0 = tf[0], tf[2], tf[5]
    cx, cy = latlon_utm(sc["tam"][0], sc["tam"][1], zone)
    hw, hh = sc["rong_km"] * 500, sc["cao_km"] * 500
    px0, px1 = int((cx - hw - X0) / res), int((cx + hw - X0) / res)
    py0, py1 = int((Y0 - (cy + hh)) / res), int((Y0 - (cy - hh)) / res)
    ifd = doc_ifd0(url)
    px0, py0 = max(0, px0), max(0, py0)
    px1, py1 = min(ifd["W"], px1), min(ifd["H"], py1)
    tw, th = ifd["tw"], ifd["th"]
    so_cot = math.ceil(ifd["W"] / tw)
    ra = Image.new("RGB", (px1 - px0, py1 - py0))
    o = 0
    for ty in range(py0 // th, (py1 - 1) // th + 1):
        for tx in range(px0 // tw, (px1 - 1) // tw + 1):
            k = ty * so_cot + tx
            raw = doc_khoang(url, ifd["toff"][k], ifd["toff"][k] + ifd["tcnt"][k] - 1)
            ra.paste(giai_o(raw, tw, th), (tx * tw - px0, ty * th - py0))
            o += 1
            print(f"ô {o}", flush=True)
    # màu: Sentinel TCI thường tối, mờ → kéo tương phản GIỮ TÔNG (cùng 1 đường cong cho 3 kênh), sáng, bão hoà nhẹ.
    # 26/10 bản 2: bản 1 kéo từng kênh riêng (cutoff 0,6, bão hoà 1,25) làm làng/đường ngả tím hồng.
    ra = ImageOps.autocontrast(ra, cutoff=0.5, preserve_tone=True)
    ra = ImageEnhance.Brightness(ra).enhance(1.05)
    ra = ImageEnhance.Color(ra).enhance(1.12)
    out = cp.parent / "sentinel.jpg"
    ra.save(out, quality=90)
    goc = []
    for (px, py) in [(px0, py0), (px1, py0), (px1, py1), (px0, py1)]:
        la, lo = utm_latlon(X0 + px * res, Y0 - py * res, zone)
        goc.append([round(lo, 7), round(la, 7)])
    nam = item["properties"]["datetime"][:4]
    cfg["anh_ve_tinh"] = {"file": str(out.relative_to(ROOT)).replace("\\", "/"), "goc": goc,
                          "nguon": f"Contains modified Copernicus Sentinel data {nam}", "canh": sc["canh"],
                          "ngay_chup": item["properties"]["datetime"][:10]}
    cp.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"XONG: {out} {ra.size} từ {o} ô · ngày chụp {item['properties']['datetime'][:10]} · góc {goc[0]} … {goc[2]}")


if __name__ == "__main__":
    main()
