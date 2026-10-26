"""Đọc số quảng cáo Meta mỗi tuần → phễu 6 bậc + đề xuất TẮT/GIỮ/TĂNG (skill quang-cao-bds §4–6, kế hoạch v2 §4.1).

  python tools/doc_ads.py --ads data/ads/ads.csv --leads data/ads/so-nguon-khach.csv
  python tools/doc_ads.py --ads ... --leads ... --luu      # lưu số kỳ vào DB (ad_metrics) để so "2 tuần liền"
  python tools/doc_ads.py --ads ... --tran-cpv 1500000     # trần chi phí / lượt xem đất (VND)

--ads   : file CSV xuất ở cấp "Quảng cáo" trong Ads Manager (giao diện Anh hoặc Việt đều được).
--leads : file CSV tải từ Google Sheet "sổ nguồn khách" (cột ma_qc, trang_thai = BẬC CAO NHẤT đã đạt;
          tuỳ chọn nghe_may, xem_dat, coc, goi_lai_phut). Dòng không có mã QC-… (kênh khác) bị bỏ qua.
Quy ước tên quảng cáo: mã ý tưởng + số bản, vd "QC-A1 | so-da-trao". QC-SK… = sự kiện, QC-NN… = Nhật/Hàn/Đài.
Thước đo chính: chi phí / lượt xem đất (CPV). Tín hiệu sớm: chi phí / cuộc nói chuyện (tin nhắn + gọi + form).
Chỉ đọc các cột cần thiết; KHÔNG đọc/in tên, SĐT khách. Đề xuất để người dùng duyệt "ok" trước mọi lần tiêu tiền mới.
"""
import argparse
import csv
import re
import statistics
import sys
import unicodedata
from datetime import date
from pathlib import Path

# Ngưỡng mặc định = kế hoạch v2 §4.1 + §6 (người dùng chốt 15/10). Ghi đè: settings.json khoá "qc".
NGUONG_MAC_DINH = {
    "tran_cpv": 1_500_000,      # chi phí/lượt xem đất > trần 2 tuần liền → giảm tiền, đổi video
    "tang_cpv": 800_000,        # ≤ mức này 2 tuần liền → tăng 20% từ khoản dự phòng
    "doi_video": 3_000_000,     # tiêu tới đây chưa có lượt xem đất → đổi video
    "tat": 6_000_000,           # tiêu tới đây vẫn 0 lượt xem → tắt, dồn tiền sang xe đón khách
    "tran_coc": 8_000_000,      # chi phí/cọc
    "tran_su_kien": 400_000,    # chi phí/gia đình đến dự sự kiện
    "nn_dung": 2_500_000,       # Nhật/Hàn/Đài: tiêu tới đây chưa ai để lại số → dừng
    "som_nc": 1_000_000,        # [GIẢ THUYẾT] tiêu tới đây chưa ai nhắn/gọi → cảnh báo sớm
    "tan_suat_met": 2.5,        # [GIẢ THUYẾT] vùng nhỏ nhàm nhanh → làm sẵn mẫu thay
}

COT_ADS = {
    "ten": ["ad name", "ten quang cao"],
    "chi_tieu": ["amount spent", "so tien da chi tieu", "so tien da chi", "chi tieu"],
    "hien_thi": ["impressions", "luot hien thi"],
    "tiep_can": ["reach", "nguoi tiep can", "luot tiep can", "so nguoi tiep can"],
    "tan_suat": ["frequency", "tan suat"],
    "luot_bam": ["link clicks", "luot click vao lien ket", "clicks (all)", "luot click (tat ca)"],
    "tin_nhan": ["messaging conversations started", "cuoc tro chuyen qua tin nhan da bat dau",
                 "luot bat dau cuoc tro chuyen qua tin nhan", "so cuoc tro chuyen qua tin nhan da bat dau"],
    "cuoc_goi": ["calls placed", "estimated call confirmation clicks", "cuoc goi da thuc hien", "luot goi dien",
                 "so cuoc goi"],
    "lead": ["leads", "khach hang tiem nang", "luot khach hang tiem nang"],
    "xem_3s": ["3-second video plays", "luot phat video 3 giay", "luot phat video lien tuc 3 giay"],
    "thruplay": ["thruplays", "luot thruplay"],
    "bat_dau": ["reporting starts", "bat dau bao cao", "ngay bat dau bao cao"],
    "ket_thuc": ["reporting ends", "ket thuc bao cao", "ngay ket thuc bao cao"],
}
COT_LEADS = {
    "ten": ["ma_qc", "ma qc", "ad_name", "ad name", "ten quang cao", "nguon"],
    "trang_thai": ["trang_thai", "trang thai", "bac", "lead_status"],
    "nghe_may": ["nghe_may", "nghe may"],
    "xem_dat": ["xem_dat", "da xem dat", "xem dat"],
    "coc": ["coc", "dat coc"],
    "goi_lai_phut": ["goi_lai_phut", "phut goi lai", "goi lai (phut)"],
}


def chuan(s) -> str:
    """Bỏ dấu, thường hoá, gộp khoảng trắng — để khớp tên cột/giá trị Anh–Việt."""
    s = unicodedata.normalize("NFD", str(s or "")).replace("đ", "d").replace("Đ", "D")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def so(v) -> float:
    """'1.250.000' | '1,250,000' | '1,85' | '1.85' | '' → số."""
    s = re.sub(r"[^\d,.\-]", "", str(v or "").replace(" ", ""))
    if not s or s in "-.,":
        return 0.0
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    elif "," in s:
        s = s.replace(",", "") if re.fullmatch(r"-?\d{1,3}(,\d{3})+", s) else s.replace(",", ".")
    elif "." in s and re.fullmatch(r"-?\d{1,3}(\.\d{3})+", s):
        s = s.replace(".", "")
    return float(s)


def tim_cot(headers, bang) -> dict:
    """Map khoá nội bộ → tên cột thật. Ưu tiên khớp đúng (theo thứ tự bí danh), sau đó khớp đầu chuỗi."""
    nh = {h: chuan(h) for h in headers}
    out = {}
    for khoa, alias in bang.items():
        al = [chuan(a) for a in alias]
        hit = next((h for a in al for h, n in nh.items() if n == a), None) or \
            next((h for h, n in nh.items() if any(n.startswith(a) for a in al)), None)
        if hit:
            out[khoa] = hit
    return out


def doc_csv(path) -> list[dict]:
    text = Path(path).read_text(encoding="utf-8-sig")
    try:
        dialect = csv.Sniffer().sniff(text[:4096], delimiters=",;\t")
    except csv.Error:
        dialect = csv.excel
    return list(csv.DictReader(text.splitlines(), dialect=dialect))


def ma_tu_ten(ten) -> str:
    m = re.search(r"\bQC-[A-Z]+\d*\b", str(ten or ""), re.I)
    return m.group(0).upper() if m else "KHONG-MA"


def y_tuong(ma) -> str:
    m = re.match(r"(QC-[A-Z]+)", ma)
    return m.group(1) if m else ma


def loai(ma) -> str:
    """nen · su_kien (QC-SK…) · nuoc_ngoai (QC-NN…)."""
    return "su_kien" if ma.startswith("QC-SK") else "nuoc_ngoai" if ma.startswith("QC-NN") else "nen"


BAC = {  # giá trị ô trang_thai (đã bỏ dấu) → bậc phễu v2 §6; 0 = loại trước khi đủ chất lượng
    1: ("", "1", "lead", "moi", "new", "intake", "co so", "da lien he"),
    2: ("2", "du chat luong", "du cl", "qualified", "dat"),
    3: ("3", "xem dat", "da xem dat", "converted", "den du", "check-in", "check in"),
    4: ("4", "giu cho", "phieu", "phieu uu tien", "da giu cho"),
    5: ("5", "coc", "da coc"),
    6: ("6", "ky", "da ky", "hd", "ky hd"),
    0: ("0", "lost", "loai", "khong nghe", "not qualified", "not_qualified", "khong du chat luong", "sai nhu cau",
        "so rac"),
}


def trang_thai(v):
    """→ bậc 0–6 (bậc cao nhất đã đạt), None nếu giá trị lạ."""
    n = chuan(v)
    return next((b for b, ds in BAC.items() if n in ds), None)


def co(v) -> bool:
    return chuan(v) in ("co", "yes", "x", "1", "true", "dung", "roi", "da coc", "da xem")


def tong_hop(ads_rows, lead_rows) -> tuple[dict, dict]:
    """→ (số theo mã QC, thông tin chung). Không đụng DB."""
    ca = tim_cot(ads_rows[0].keys(), COT_ADS) if ads_rows else {}
    if ads_rows and "ten" not in ca:
        raise SystemExit(f"ERROR: file Ads Manager thiếu cột tên quảng cáo. Cột có: {list(ads_rows[0].keys())}")
    m: dict[str, dict] = {}

    def dong(ma):
        return m.setdefault(ma, dict(chi_tieu=0.0, hien_thi=0.0, tiep_can=0.0, tan_suat_cot=0.0, luot_bam=0.0,
                                     tin_nhan=0.0, cuoc_goi=0.0, lead_qc=0.0, xem_3s=0.0, thruplay=0.0,
                                     lead=0, moi=0, loai_bo=0, la=0, dcl=0, xem_dat=0, coc=0, ky=0,
                                     nghe_may=0, goi_lai=[]))

    ngay = []
    for r in ads_rows:
        ten = r.get(ca["ten"], "")
        if not str(ten).strip():
            continue  # dòng tổng của Ads Manager
        d = dong(ma_tu_ten(ten))
        for k in ("chi_tieu", "hien_thi", "tiep_can", "luot_bam", "tin_nhan", "cuoc_goi", "xem_3s", "thruplay"):
            if k in ca:
                d[k] += so(r.get(ca[k]))
        if "lead" in ca:
            d["lead_qc"] += so(r.get(ca["lead"]))
        if "tan_suat" in ca:
            d["tan_suat_cot"] = max(d["tan_suat_cot"], so(r.get(ca["tan_suat"])))
        for k in ("bat_dau", "ket_thuc"):
            if k in ca and r.get(ca[k]):
                ngay.append((k, str(r[ca[k]])[:10]))

    cl = tim_cot(lead_rows[0].keys(), COT_LEADS) if lead_rows else {}
    if lead_rows and not {"ten", "trang_thai"} <= cl.keys():
        raise SystemExit(f"ERROR: file sổ nguồn khách cần cột ma_qc + trang_thai. Cột có: {list(lead_rows[0].keys())}")
    bo_qua = 0
    for r in lead_rows:
        ma = ma_tu_ten(r.get(cl["ten"]))
        if ma == "KHONG-MA":
            bo_qua += 1     # khách từ kênh khác (giới thiệu, đại lý…) hoặc quên ghi mã
            continue
        d = dong(ma)
        d["lead"] += 1
        b = trang_thai(r.get(cl["trang_thai"]))
        if b is None:
            d["la"] += 1
            b = 1
        d["moi"] += b == 1
        d["loai_bo"] += b == 0
        d["dcl"] += b >= 2
        d["xem_dat"] += b >= 3 or ("xem_dat" in cl and co(r.get(cl["xem_dat"])))
        d["coc"] += b >= 5 or ("coc" in cl and co(r.get(cl["coc"])))
        d["ky"] += b >= 6
        if "nghe_may" in cl and (co(r.get(cl["nghe_may"])) or b >= 2):
            d["nghe_may"] += 1
        if "goi_lai_phut" in cl and str(r.get(cl["goi_lai_phut"]) or "").strip():
            d["goi_lai"].append(so(r.get(cl["goi_lai_phut"])))

    for d in m.values():
        d["noi_chuyen"] = int(d["tin_nhan"] + d["cuoc_goi"] + d["lead_qc"])
        if not lead_rows:
            d["lead"] = d["noi_chuyen"]     # chưa có sổ nguồn khách → tạm coi mỗi cuộc nói chuyện là 1 khách
        d["tan_suat"] = d["hien_thi"] / d["tiep_can"] if d["tiep_can"] else d["tan_suat_cot"]
        if "nghe_may" not in cl:
            d["nghe_may"] = None            # không có cột → không đoán
    bd = [v for k, v in ngay if k == "bat_dau"]
    kt = [v for k, v in ngay if k == "ket_thuc"]
    info = {"tu": min(bd) if bd else None, "den": max(kt) if kt else None, "co_cot_nghe_may": "nghe_may" in cl,
            "co_file_lead": bool(lead_rows), "bo_qua": bo_qua, "co_cot_3s": "xem_3s" in ca,
            "co_cot_bam": "luot_bam" in ca}
    return m, info


def quyet_dinh(d, ng, chia_deu, so_ngay, cpv_truoc=None, kieu="nen") -> str:
    """Luật skill quang-cao-bds §6a (kế hoạch v2), dừng ở luật đầu tiên khớp."""
    ghi = ""
    if d["tan_suat"] > ng["tan_suat_met"]:
        ghi = f" ⚠ tần suất > {ng['tan_suat_met']:g}: làm sẵn 2 mẫu thay"
    if so_ngay >= 7 and chia_deu > 0 and d["chi_tieu"] < 0.5 * chia_deu:
        return "TẮT (Meta gần như không phân phối) → thay mẫu khác góc" + ghi
    chi, xem = d["chi_tieu"], d["xem_dat"]
    it = " [GIẢ THUYẾT: < 3 lượt xem]" if 0 < xem < 3 else ""

    if kieu == "su_kien":
        if chi < 3 * ng["tran_su_kien"]:
            return "CHỜ (chưa đủ tiền để kết luận)" + ghi
        if xem == 0:
            return "GIẢM TIỀN, đổi mẫu (chưa gia đình nào đến dự)" + ghi
        if chi / xem > ng["tran_su_kien"]:
            return f"GIẢM TIỀN (chi phí/gia đình đến dự > {tien(ng['tran_su_kien'])})" + it + ghi
        return "GIỮ (trong trần chi phí/gia đình)" + it + ghi

    if kieu == "nuoc_ngoai":
        if d["lead"] == 0 and chi >= ng["nn_dung"]:
            return f"DỪNG (tiêu ≥ {tien(ng['nn_dung'])} chưa ai để lại số)" + ghi
        if chi < ng["nn_dung"]:
            return "CHỜ" + ghi
        return "GIỮ, theo dõi chi phí/khách có số" + ghi

    if chi < ng["doi_video"]:
        som = ""
        if d["noi_chuyen"] == 0 and chi >= ng["som_nc"]:
            som = f" ⚠ tiêu ≥ {tien(ng['som_nc'])} chưa ai nhắn/gọi: xem lại câu mở, nút, tin chào"
        elif d["noi_chuyen"]:
            som = f"; {d['noi_chuyen']} cuộc nói chuyện, {xem} lượt xem"
        return f"CHỜ (chưa tiêu đủ {tien(ng['doi_video'])}{som})" + ghi
    if xem == 0:
        if chi >= ng["tat"]:
            return f"TẮT + bỏ ý tưởng (tiêu ≥ {tien(ng['tat'])} vẫn 0 lượt xem → dồn tiền sang xe đón khách)" + ghi
        return f"ĐỔI VIDEO khác góc/câu mở (tiêu ≥ {tien(ng['doi_video'])} chưa có lượt xem đất)" + ghi
    cpv = chi / xem
    if cpv > ng["tran_cpv"]:
        if cpv_truoc is not None and cpv_truoc > ng["tran_cpv"]:
            return "GIẢM TIỀN + ĐỔI VIDEO (chi phí/lượt xem > trần 2 tuần liền)" + it + ghi
        return "THEO DÕI (chi phí/lượt xem > trần lần đầu)" + it + ghi
    if cpv > ng["tang_cpv"]:
        return "GIỮ (chi phí/lượt xem trong trần)" + it + ghi
    if cpv_truoc is not None and cpv_truoc <= ng["tran_cpv"] and d["tan_suat"] < 3 and not it:
        return "ỨNG VIÊN THẮNG → xin \"ok\" TĂNG 20% từ khoản dự phòng" + ghi
    return "ỨNG VIÊN THẮNG (chờ tuần sau để tăng)" + it + ghi


def gop_y_tuong(m) -> dict:
    out: dict[str, dict] = {}
    cong = ("chi_tieu", "hien_thi", "tiep_can", "luot_bam", "noi_chuyen", "xem_3s", "lead", "dcl", "xem_dat", "coc",
            "ky")
    for ma, d in m.items():
        g = out.setdefault(y_tuong(ma), dict({k: 0 for k in cong}, nghe_may=0 if d["nghe_may"] is not None else None,
                                             tan_suat=0.0))
        for k in cong:
            g[k] += d[k]
        if g["nghe_may"] is not None and d["nghe_may"] is not None:
            g["nghe_may"] += d["nghe_may"]
        g["tan_suat"] = g["hien_thi"] / g["tiep_can"] if g["tiep_can"] else max(g["tan_suat"], d["tan_suat"])
    return out


def tien(x) -> str:
    return "—" if x is None else (f"{x / 1e6:.2f}tr" if x >= 1e6 else f"{x / 1e3:.0f}k")


def pt(a, b) -> str:
    return "—" if a is None or not b else f"{100 * a / b:.0f}%"


def chia(a, b):
    return a / b if b else None


def in_bang(tieu_de, rows, ng, chia_deu, so_ngay, truoc) -> None:
    print(f"\n{tieu_de}")
    cols = ["Mã", "Chi tiêu", "Nói chuyện", "Giá/NC", "Có số", "Đủ CL", "Xem đất", "Giá/xem", "Cọc", "Tần suất",
            "Đề xuất"]
    data = []
    for ma, d in sorted(rows.items()):
        data.append([ma, tien(d["chi_tieu"]), str(d["noi_chuyen"]), tien(chia(d["chi_tieu"], d["noi_chuyen"])),
                     str(d["lead"]), f"{d['dcl']} ({pt(d['dcl'], d['lead'])})", str(d["xem_dat"]),
                     tien(chia(d["chi_tieu"], d["xem_dat"])), str(d["coc"]), f"{d['tan_suat']:.2f}",
                     quyet_dinh(d, ng, chia_deu, so_ngay, truoc.get(ma), loai(ma))])
    w = [max(len(c), *(len(r[i]) for r in data)) if data else len(c) for i, c in enumerate(cols)]
    print(" | ".join(c.ljust(x) for c, x in zip(cols, w)))
    print("-+-".join("-" * x for x in w))
    for r in data:
        print(" | ".join(v.ljust(x) for v, x in zip(r, w)))


def cpv_tuan_truoc(tu) -> dict:
    """Chi phí/lượt xem đất của lần lưu gần nhất kết thúc trước `tu` (để xét '2 tuần liền'). Không có DB → {}."""
    if not tu:
        return {}
    from common import DB_PATH, connect
    if not DB_PATH.exists():
        return {}
    con = connect()
    try:
        rows = con.execute(
            "SELECT ma_qc, chi_tieu, xem_dat FROM ad_metrics a WHERE den_ngay < ? AND den_ngay = "
            "(SELECT MAX(den_ngay) FROM ad_metrics b WHERE b.ma_qc = a.ma_qc AND b.den_ngay < ?)", (tu, tu)).fetchall()
    except Exception:
        return {}
    finally:
        con.close()
    return {r["ma_qc"]: (r["chi_tieu"] / r["xem_dat"] if r["xem_dat"] else float("inf")) for r in rows}


def luu(m, tu, den, ng, chia_deu, so_ngay, truoc) -> None:
    from common import connect
    con = connect()
    with con:
        for ma, d in m.items():
            con.execute(
                "INSERT OR REPLACE INTO ad_metrics(ma_qc,y_tuong,tu_ngay,den_ngay,chi_tieu,hien_thi,tiep_can,tan_suat,"
                "luot_bam,lead,nghe_may,du_chat_luong,xem_dat,coc,quyet_dinh) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (ma, y_tuong(ma), tu, den, d["chi_tieu"], int(d["hien_thi"]), int(d["tiep_can"]), round(d["tan_suat"], 3),
                 int(d["luot_bam"]), d["lead"], d["nghe_may"], d["dcl"], d["xem_dat"], d["coc"],
                 quyet_dinh(d, ng, chia_deu, so_ngay, truoc.get(ma), loai(ma))))
    con.close()
    print(f"\nĐÃ LƯU {len(m)} dòng vào ad_metrics ({tu} → {den}).")


def nguong(tran_cpv=None) -> tuple[dict, str]:
    ng, nguon = dict(NGUONG_MAC_DINH), "kế hoạch v2 §4.1"
    try:
        from common import settings
        qc = settings().get("qc") or {}
        ng.update({k: v for k, v in qc.items() if k in ng and v})
        if qc:
            nguon = "settings.json qc"
    except Exception:
        pass
    if tran_cpv:
        ng["tran_cpv"], nguon = tran_cpv, "--tran-cpv"
    return ng, nguon


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ads", required=True)
    ap.add_argument("--leads")
    ap.add_argument("--tran-cpv", type=float)
    ap.add_argument("--tu", help="YYYY-MM-DD nếu file không có cột ngày")
    ap.add_argument("--den", help="YYYY-MM-DD nếu file không có cột ngày")
    ap.add_argument("--luu", action="store_true")
    a = ap.parse_args()

    ng, nguon_ng = nguong(a.tran_cpv)
    m, info = tong_hop(doc_csv(a.ads), doc_csv(a.leads) if a.leads else [])
    tu, den = a.tu or info["tu"], a.den or info["den"]
    so_ngay = (date.fromisoformat(den) - date.fromisoformat(tu)).days + 1 if tu and den else 7
    tong = sum(d["chi_tieu"] for d in m.values())
    so_mau = sum(1 for d in m.values() if d["chi_tieu"] > 0)
    chia_deu = tong / so_mau if so_mau else 0
    truoc = cpv_tuan_truoc(tu)

    t = {k: sum(d[k] for d in m.values()) for k in ("hien_thi", "luot_bam", "tin_nhan", "cuoc_goi", "lead_qc",
                                                     "noi_chuyen", "xem_3s", "lead", "dcl", "xem_dat", "coc", "ky")}
    nghe = sum(d["nghe_may"] or 0 for d in m.values()) if info["co_cot_nghe_may"] else None
    goi = [x for d in m.values() for x in d["goi_lai"]]
    print(f"BÁO CÁO QUẢNG CÁO {tu or '?'} → {den or '?'} ({so_ngay} ngày) · trần chi phí/lượt xem đất "
          f"{tien(ng['tran_cpv'])} · trần chi phí/cọc {tien(ng['tran_coc'])} ({nguon_ng})")
    ctr = pt(t["luot_bam"], t["hien_thi"]) if info["co_cot_bam"] else "—"
    print(f"Tổng chi {tien(tong)} · CPM {tien(chia(tong * 1000, t['hien_thi']))} · CTR {ctr}"
          + (f" · giữ chân 3 giây {pt(t['xem_3s'], t['hien_thi'])}" if info["co_cot_3s"] else ""))
    print(f"Cuộc nói chuyện {t['noi_chuyen']} (tin nhắn {t['tin_nhan']:.0f} · gọi {t['cuoc_goi']:.0f} · form "
          f"{t['lead_qc']:.0f}) · giá/cuộc {tien(chia(tong, t['noi_chuyen']))}")
    print(f"Phễu: có số {t['lead']} → nghe máy {pt(nghe, t['lead'])} → đủ chất lượng {t['dcl']} ({pt(t['dcl'], t['lead'])})"
          f" → xem đất {t['xem_dat']} (giá/lượt {tien(chia(tong, t['xem_dat']))}) → cọc {t['coc']} "
          f"(giá/cọc {tien(chia(tong, t['coc']))}) → ký {t['ky']}")
    cpv, cpc = chia(tong, t["xem_dat"]), chia(tong, t["coc"])
    dat = cpv is not None and cpv <= ng["tran_cpv"] and cpc is not None and cpc <= ng["tran_coc"]
    print(f"Mốc v2 (xem đất ≤ {tien(ng['tran_cpv'])} và cọc ≤ {tien(ng['tran_coc'])}): {'ĐẠT' if dat else 'CHƯA ĐẠT'}"
          + (" — đạt 2 tuần liền thì đề nghị CĐT mở thêm quỹ (v2 §4.1)" if dat else ""))
    if info["co_file_lead"]:
        print(f"Gọi lại trung vị {f'{statistics.median(goi):.0f} phút' if goi else '— (chưa có cột goi_lai_phut)'}"
              f" (mục tiêu ≤ 5) · {info['bo_qua']} dòng sổ không có mã QC (kênh khác) đã bỏ qua")
    print(f"Số mẫu đánh giá được cùng lúc ≈ {tong / so_ngay * 14 / ng['doi_video']:.1f} "
          f"(ngân sách/ngày × 14 ÷ {tien(ng['doi_video'])} mốc đổi video)")
    canh_bao = []
    if tong < 10_000_000:
        canh_bao.append("tổng chi < 10 triệu → mọi kết luận chỉ là [GIẢ THUYẾT]")
    if "KHONG-MA" in m:
        canh_bao.append("có quảng cáo không mang mã QC-… trong tên → đặt lại tên trong Ads Manager")
    if any(d["la"] for d in m.values()):
        canh_bao.append("có trang_thai lạ (dùng: lead · đủ chất lượng · xem đất · giữ chỗ · cọc · ký · loại)")
    if info["co_file_lead"] and t["noi_chuyen"] and t["lead"] > t["noi_chuyen"]:
        canh_bao.append("sổ có nhiều khách mang mã QC hơn số cuộc nói chuyện → kiểm lại mã ghi trong sổ")
    for c in canh_bao:
        print(f"⚠ {c}")
    y = gop_y_tuong(m)
    in_bang("THEO Ý TƯỞNG (chấm ý tưởng trước)", y, ng, tong / len(y) if y else 0, so_ngay, {})
    in_bang("THEO MẪU", m, ng, chia_deu, so_ngay, truoc)
    print("\nĐề xuất để người dùng duyệt — mọi lần tiêu tiền mới (bật mẫu, tăng ngân sách) cần \"ok\".")
    if a.luu:
        if not (tu and den):
            sys.exit("ERROR: cần --tu/--den (file không có cột ngày) để lưu")
        luu(m, tu, den, ng, chia_deu, so_ngay, truoc)


if __name__ == "__main__":
    main()
