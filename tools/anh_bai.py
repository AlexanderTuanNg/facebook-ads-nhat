"""Tạo bộ ảnh thật riêng cho từng bài, XOAY VÒNG kho ảnh `assets/dong-lac/kho-anh/danh_muc.json` (05/10/2026: người dùng
"thay đổi ảnh liên tục", 16 bài/ngày). Bản cũ (28/09, 11 ảnh gốc cố định): workspace/reports/backup/2026-10-05-gap-doi/.

  python tools/anh_bai.py --post-ids 31,32,19                # tạo assets/dong-lac/media/bai/p<id>-<k>.jpg + mô tả
  python tools/anh_bai.py --post-ids 40 --dem-bia 40         # góc 5 kinh tế đêm: ảnh đêm làm BÌA (ảnh 1)
  python tools/anh_bai.py --post-ids 33 --dem 33             # thêm ảnh đêm (cuối) dù đăng trước 19:00
  python tools/anh_bai.py --post-ids 31 --lam-lai            # chọn lại bộ ảnh mới cho bài đã có
  python tools/anh_bai.py --lam-mo-bien-so                   # (1 lần) tạo m01b.jpg: ảnh đêm đã làm mờ biển số xe máy

Mỗi bài: 1 bìa (chụp chéo/mặt đất) + 1 flycam nhìn thẳng + 1 ảnh chéo/mặt đất khác nguồn (+ ảnh đêm cuối nếu đăng từ
19:00 hoặc --dem). Luôn lấy góc ảnh ÍT DÙNG NHẤT; bìa không trùng 10 bài gần nhất và không trùng bài trước ở cùng group.
Mỗi ảnh cắt lệch ngẫu nhiên 88–96% vùng của góc ảnh, chỉnh sáng/tương phản/màu ±4%, thu về cạnh dài ≤ 2048 px, bỏ EXIF
→ không bài nào trùng y hệt ảnh bài khác. Không lật ảnh, không chèn chữ, không ảnh AI (ảnh thật nên không ghi "Ảnh minh hoạ").
Mô tả từng ảnh (đúng cái thấy) ghi vào workspace/plans/anh-bai.json → chép NGUYÊN vào images_meta của bài.
"""
import argparse
import json
import random
from collections import Counter
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

from common import ROOT, connect, now_str

GOC = ROOT / "assets" / "dong-lac" / "anh-moi-2809"
RA = ROOT / "assets" / "dong-lac" / "media" / "bai"
KHO = ROOT / "assets" / "dong-lac" / "kho-anh"
DA_DUNG = KHO / "da_dung.json"
DS_ANH_BAI = ROOT / "workspace" / "plans" / "anh-bai.json"
BIA_GAN_DAY = 10  # bìa không trùng 10 bài gần nhất (kho có ~15 bìa ban ngày; 16 thì hết ứng viên — đo 05/10)


# Ảnh đêm m01 (2560×1920): biển số xe máy + khuôn mặt (compliance 28/09: Luật Quảng cáo Đ8 k8, BLDS Đ32 — không dùng hình
# ảnh cá nhân khi chưa được đồng ý). Toạ độ đo trên ảnh gốc, nới rộng khung.
MO_MANH = [(2120, 1757, 2266, 1866),                       # biển số xe máy
           (110, 1460, 210, 1560), (485, 1490, 600, 1590),  # phụ nữ bên trái; bé áo đỏ (bập bênh)
           (620, 1510, 720, 1610), (380, 1600, 490, 1700),  # bé áo hồng; bé trên cầu trượt
           (695, 1470, 800, 1570)]                          # bé sau bập bênh
MO_NHE = [(990, 1380, 1610, 1690)]                          # nhóm bàn/bể cát phía phải, gồm trẻ trong bể cát (ở xa)


def lam_mo_bien_so() -> Path:
    """Tạo m01b.jpg từ m01.jpg: làm mờ biển số + khuôn mặt (tên hàm giữ như cũ). Mặt nạ viền mềm → không thấy khung."""
    from PIL import ImageDraw

    im = Image.open(GOC / "m01.jpg").convert("RGB")
    for hop_ds, ban_kinh, vien, hinh in ((MO_MANH, 16, 10, "elip"), (MO_NHE, 8, 30, "chu_nhat")):
        mat_na = Image.new("L", im.size, 0)
        ve = ImageDraw.Draw(mat_na)
        for hop in hop_ds:
            (ve.ellipse if hinh == "elip" else ve.rectangle)(hop, fill=255)
        mat_na = mat_na.filter(ImageFilter.GaussianBlur(vien))
        im = Image.composite(im.filter(ImageFilter.GaussianBlur(ban_kinh)), im, mat_na)
    ra = GOC / "m01b.jpg"
    im.save(ra, quality=90)
    return ra


def doc_json(p: Path, mac_dinh):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else mac_dinh


def ghi_json(p: Path, d) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    tam = p.with_suffix(".tmp")
    tam.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    tam.replace(p)


def co_the_lam_bia(m: dict) -> bool:
    # m07 có cột điện tháp thép (compliance 28/09) → không làm bìa dù vùng cắt đã chừa cột điện
    return m["loai"] == "bia" or (m["loai"] == "phu" and m["goc_nhin"] in ("cheo", "mat_dat") and not m["id"].startswith("m07"))


def chon(ung_vien: list, dem: Counter, rng: random.Random, tranh_src: set, tranh_id: set):
    """Góc ảnh ít dùng nhất; tránh nguồn đã có trong bài và id cần tránh (nới dần nếu hết ứng viên)."""
    for loc in ((lambda m: m["src"] not in tranh_src and m["id"] not in tranh_id),
                (lambda m: m["src"] not in tranh_src), (lambda m: True)):
        ds = [m for m in ung_vien if loc(m)]
        if ds:
            return min(ds, key=lambda m: (dem[m["id"]], rng.random()))
    raise SystemExit("ERROR: kho ảnh rỗng")


def chon_bo(post_id: int, gio: int, dem_cuoi: bool, dem_bia: bool, nhom, da_dung: dict, kho: list) -> list[str]:
    rng = random.Random(post_id * 7919)
    dem = Counter(i for v in da_dung.values() for i in v["ids"])
    cu = [(int(k), v) for k, v in da_dung.items() if int(k) != post_id]
    bia_tranh = {v["ids"][0] for _, v in sorted(cu)[-BIA_GAN_DAY:]}
    bia_tranh |= {v["ids"][0] for k, v in sorted(cu) if nhom is not None and v.get("nhom") == nhom}
    anh_dem = [m for m in kho if m["loai"] == "dem"]
    ds = [chon(anh_dem if dem_bia else [m for m in kho if co_the_lam_bia(m)], dem, rng, set(), bia_tranh)]
    ds.append(chon([m for m in kho if m["loai"] == "phu" and m["goc_nhin"] == "thang"], dem, rng,
                   {m["src"] for m in ds}, set()))
    ds.append(chon([m for m in kho if m["loai"] in ("bia", "phu") and m["goc_nhin"] in ("cheo", "mat_dat")],
                   dem, rng, {m["src"] for m in ds}, {m["id"] for m in ds}))
    if not dem_bia and (dem_cuoi or gio >= 19):
        ds.append(chon(anh_dem, dem, rng, set(), set()))
    return [m["id"] for m in ds]


def cat(m: dict, ra: Path, rng: random.Random) -> None:
    im = Image.open(ROOT / m["src"]).convert("RGB")
    w, h = im.size
    x0, y0, x1, y1 = m["box"]
    im = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    w, h = im.size
    tl = rng.uniform(0.88, 0.96)
    cw, ch = int(w * tl), int(h * tl)
    x, y = rng.randint(0, w - cw), rng.randint(0, h - ch)
    im = im.crop((x, y, x + cw, y + ch))
    for lop in (ImageEnhance.Brightness, ImageEnhance.Contrast, ImageEnhance.Color):
        im = lop(im).enhance(rng.uniform(0.96, 1.04))
    im.thumbnail((2048, 2048))
    im.save(ra, quality=88)  # lưu mới → không mang EXIF


def bo_anh(post_id: int, gio: int, dem: bool = False, dem_bia: bool = False, nhom=None, lam_lai: bool = False) -> list[dict]:
    dm = json.loads((KHO / "danh_muc.json").read_text(encoding="utf-8"))
    kho = {m["id"]: m for m in dm["anh"]}
    so = doc_json(DA_DUNG, {"bai": {}})
    cu = so["bai"].get(str(post_id))
    if cu and not lam_lai and all(i in kho for i in cu["ids"]):
        ids = cu["ids"]  # chạy lại → cùng bộ ảnh (cùng hạt ngẫu nhiên → cùng vùng cắt)
    else:
        ids = chon_bo(post_id, gio, dem, dem_bia, nhom, so["bai"], list(kho.values()))
        so["bai"][str(post_id)] = {"ids": ids, "nhom": nhom, "luc": now_str()}
        ghi_json(DA_DUNG, so)
    rng = random.Random(post_id * 7919 + (1 if lam_lai else 0))
    RA.mkdir(parents=True, exist_ok=True)
    out = []
    for k, i in enumerate(ids, 1):
        p = RA / f"p{post_id}-{k}.jpg"
        cat(kho[i], p, rng)
        out.append({"file": p.relative_to(ROOT).as_posix(), "mo_ta": kho[i]["mo_ta"], "nguon": dm["nguon"][kho[i]["nguon"]]})
    ds = doc_json(DS_ANH_BAI, {})
    ds[str(post_id)] = out
    ghi_json(DS_ANH_BAI, ds)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--post-ids")
    ap.add_argument("--dem", help="id bài dùng thêm ảnh đêm (cuối) dù đăng trước 19:00, vd 32,23")
    ap.add_argument("--dem-bia", help="id bài góc kinh tế đêm: ảnh đêm làm bìa, vd 40,41")
    ap.add_argument("--lam-lai", action="store_true", help="chọn lại bộ ảnh mới cho bài đã có")
    ap.add_argument("--lam-mo-bien-so", action="store_true")
    a = ap.parse_args()
    if a.lam_mo_bien_so:
        print("đã tạo", lam_mo_bien_so())
    if a.post_ids:
        tach = lambda s: {int(x) for x in (s or "").split(",") if x.strip()}  # noqa: E731
        dem, dem_bia = tach(a.dem), tach(a.dem_bia)
        con = connect()
        for pid in [int(x) for x in a.post_ids.split(",") if x.strip()]:
            r = con.execute("SELECT scheduled_at, target_id FROM posts WHERE id=?", (pid,)).fetchone()
            gio = int(r["scheduled_at"][11:13]) if r and r["scheduled_at"] else 12
            ds = bo_anh(pid, gio, pid in dem, pid in dem_bia, r["target_id"] if r else None, a.lam_lai)
            print(pid, json.dumps(ds, ensure_ascii=False))


if __name__ == "__main__":
    main()
