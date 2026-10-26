"""Kiểm thử tools/doc_ads.py bằng số liệu GIẢ (không đụng data/marketing.db).

  python tools/test_doc_ads.py
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import DB_PATH, ROOT  # noqa: E402
from doc_ads import (COT_ADS, COT_LEADS, NGUONG_MAC_DINH, loai, ma_tu_ten, quyet_dinh, so, tim_cot,  # noqa: E402
                     tong_hop, trang_thai, y_tuong)

ok = sai = 0


def kiem(ten, dung):
    global ok, sai
    ok += bool(dung)
    sai += not dung
    print(f"{'OK ' if dung else 'SAI'}  {ten}")


NG = dict(NGUONG_MAC_DINH)
moc = DB_PATH.stat() if DB_PATH.exists() else None

# 1. Đọc số kiểu Việt / Mỹ
kiem("so '1.250.000' = 1250000", so("1.250.000") == 1_250_000)
kiem("so '1,250,000' = 1250000", so("1,250,000") == 1_250_000)
kiem("so '1,85' = 1.85", abs(so("1,85") - 1.85) < 1e-9)
kiem("so '1.85' = 1.85", abs(so("1.85") - 1.85) < 1e-9)
kiem("so '' = 0", so("") == 0)
kiem("so '2.500.000 ₫' = 2500000", so("2.500.000 ₫") == 2_500_000)

# 2. Nhận cột Anh / Việt (cả cột tin nhắn, cuộc gọi)
en = tim_cot(["Ad name", "Amount spent (VND)", "Impressions", "Reach", "Frequency", "Leads", "Cost per lead (VND)",
              "Messaging conversations started", "Cost per messaging conversation started (VND)", "Calls placed",
              "3-second video plays", "Reporting starts", "Reporting ends"], COT_ADS)
kiem("cột Anh: chi_tieu/lead/tan_suat", en.get("chi_tieu") == "Amount spent (VND)" and en.get("lead") == "Leads"
     and en.get("tan_suat") == "Frequency")
kiem("cột Anh: tin nhắn/cuộc gọi/3 giây (không lấy nhầm cột 'Cost per…')",
     en.get("tin_nhan") == "Messaging conversations started" and en.get("cuoc_goi") == "Calls placed"
     and en.get("xem_3s") == "3-second video plays")
vi = tim_cot(["Tên quảng cáo", "Số tiền đã chi tiêu (VND)", "Lượt hiển thị", "Người tiếp cận", "Tần suất",
              "Khách hàng tiềm năng", "Chi phí trên mỗi khách hàng tiềm năng (VND)",
              "Lượt bắt đầu cuộc trò chuyện qua tin nhắn"], COT_ADS)
kiem("cột Việt: ten/chi_tieu/lead/tin_nhan", vi.get("ten") == "Tên quảng cáo" and vi.get("chi_tieu", "").startswith("Số tiền")
     and vi.get("lead") == "Khách hàng tiềm năng" and vi.get("tin_nhan", "").startswith("Lượt bắt đầu"))
so_nguon = tim_cot(["Ngày", "Tên khách", "SĐT", "Nguồn", "Mã QC", "Trạng thái", "Nghe máy"], COT_LEADS)
kiem("sổ nguồn khách: ưu tiên cột 'Mã QC' hơn 'Nguồn'", so_nguon.get("ten") == "Mã QC"
     and so_nguon.get("trang_thai") == "Trạng thái")

# 3. Mã QC, loại chiến dịch, bậc phễu
kiem("ma_tu_ten 'QC-A1 | so-da-trao'", ma_tu_ten("QC-A1 | so-da-trao") == "QC-A1")
kiem("ma_tu_ten không mã → KHONG-MA", ma_tu_ten("Quảng cáo mới") == "KHONG-MA")
kiem("y_tuong QC-A1 → QC-A", y_tuong("QC-A1") == "QC-A")
kiem("loai: QC-SK1 sự kiện · QC-NN2 nước ngoài · QC-B1 nền",
     (loai("QC-SK1"), loai("QC-NN2"), loai("QC-B1")) == ("su_kien", "nuoc_ngoai", "nen"))
kiem("trang_thai → bậc (lead, đủ CL, xem đất, giữ chỗ, cọc, ký, loại, Converted cũ, lạ)",
     [trang_thai(x) for x in ("lead", "Đủ chất lượng", "Xem đất", "giữ chỗ", "Cọc", "Ký", "Loại", "Converted", "abc")]
     == [1, 2, 3, 4, 5, 6, 0, 3, None])

# 4. Gộp số + KHÔNG đọc tên/SĐT
ads = [{"Ad name": "QC-A1 | so-da-trao", "Amount spent (VND)": "1.500.000", "Impressions": "6000", "Reach": "3000",
        "Frequency": "2", "Messaging conversations started": "9", "Calls placed": "3", "Leads": "",
        "Reporting starts": "2026-10-20", "Reporting ends": "2026-10-26"},
       {"Ad name": "QC-A2 | so-da-trao", "Amount spent (VND)": "500.000", "Impressions": "2000", "Reach": "1000",
        "Frequency": "2", "Messaging conversations started": "4", "Calls placed": "0", "Leads": "",
        "Reporting starts": "2026-10-20", "Reporting ends": "2026-10-26"},
       {"Ad name": "", "Amount spent (VND)": "2.000.000"}]  # dòng tổng → bỏ
leads = [{"ma_qc": ma, "ten_khach": "Nguyen Van Gia", "sdt": "+84900000001", "trang_thai": s, "nghe_may": n,
          "goi_lai_phut": g}
         for ma, s, n, g in [("QC-A1", "đủ chất lượng", "có", "3"), ("QC-A1", "xem đất", "có", "4"),
                             ("QC-A1", "cọc", "có", "2"), ("QC-A1", "loại", "không", "9"), ("QC-A1", "lead", "", ""),
                             ("", "xem đất", "có", "")]]  # dòng cuối: khách giới thiệu, không có mã QC
m, info = tong_hop(ads, leads)
a1 = m["QC-A1"]
kiem("QC-A1: có số 5, đủ CL 3, xem đất 2, cọc 1, nghe máy 3",
     (a1["lead"], a1["dcl"], a1["xem_dat"], a1["coc"], a1["nghe_may"]) == (5, 3, 2, 1, 3))
kiem("QC-A1: nói chuyện = 9 tin nhắn + 3 gọi = 12", a1["noi_chuyen"] == 12)
kiem("QC-A1: tần suất = hiển thị/tiếp cận = 2", abs(a1["tan_suat"] - 2) < 1e-9)
kiem("bỏ dòng tổng (chỉ còn QC-A1, QC-A2)", set(m) == {"QC-A1", "QC-A2"})
kiem("dòng sổ không có mã QC bị bỏ qua và đếm", info["bo_qua"] == 1)
kiem("ngày báo cáo 2026-10-20 → 2026-10-26", (info["tu"], info["den"]) == ("2026-10-20", "2026-10-26"))
kiem("không giữ tên/SĐT trong kết quả", "Nguyen" not in repr(m) and "+849" not in repr(m))
m2, _ = tong_hop(ads, [])
kiem("không có sổ nguồn khách → khách = số cuộc nói chuyện", m2["QC-A1"]["lead"] == 12)


# 5. Luật quyết định (skill §7, kế hoạch v2 §4.1)
def d(chi, xem=0, nc=10, lead=5, ts=2.0):
    return dict(chi_tieu=chi, xem_dat=xem, noi_chuyen=nc, lead=lead, tan_suat=ts)


kiem("ngày 7 tiêu < 50% chia đều → TẮT phân phối",
     quyet_dinh(d(400_000), NG, 2_000_000, 7).startswith("TẮT (Meta"))
kiem("< 3 triệu → CHỜ", quyet_dinh(d(2_000_000, 1), NG, 2_000_000, 7).startswith("CHỜ"))
kiem("tiêu ≥ 1 triệu chưa ai nhắn/gọi → cảnh báo sớm", "chưa ai nhắn/gọi" in quyet_dinh(d(1_200_000, nc=0), NG, 1_200_000, 7))
kiem("3–6 triệu, 0 lượt xem → ĐỔI VIDEO", quyet_dinh(d(3_500_000), NG, 3_500_000, 7).startswith("ĐỔI VIDEO"))
kiem("≥ 6 triệu, 0 lượt xem → TẮT + bỏ ý tưởng", "bỏ ý tưởng" in quyet_dinh(d(6_500_000), NG, 6_500_000, 7))
kiem("giá/xem > 1,5 tr lần đầu → THEO DÕI", quyet_dinh(d(4_000_000, 2), NG, 4_000_000, 7).startswith("THEO DÕI"))
kiem("giá/xem > 1,5 tr 2 tuần liền → GIẢM TIỀN + ĐỔI VIDEO",
     quyet_dinh(d(4_000_000, 2), NG, 4_000_000, 7, cpv_truoc=2_000_000).startswith("GIẢM TIỀN"))
kiem("0,8–1,5 tr → GIỮ", quyet_dinh(d(4_000_000, 4), NG, 4_000_000, 7).startswith("GIỮ"))
kiem("≤ 0,8 tr lần đầu → ỨNG VIÊN (chờ tăng)", "chờ tuần sau" in quyet_dinh(d(4_000_000, 6), NG, 4_000_000, 7))
kiem("≤ 0,8 tr, tuần trước trong trần, tần suất < 3 → xin ok TĂNG 20%",
     "TĂNG 20%" in quyet_dinh(d(4_000_000, 6), NG, 4_000_000, 7, cpv_truoc=1_000_000))
kiem("< 3 lượt xem → gắn [GIẢ THUYẾT], không đề xuất tăng",
     "GIẢ THUYẾT" in quyet_dinh(d(3_000_000, 2), NG, 3_000_000, 7, cpv_truoc=1_000_000))
kiem("tần suất > 2,5 → cảnh báo mệt mẫu", "⚠" in quyet_dinh(d(4_000_000, 4, ts=3.1), NG, 4_000_000, 7))
kiem("sự kiện: > 400k/gia đình đến dự → GIẢM TIỀN",
     quyet_dinh(d(2_000_000, 3), NG, 2_000_000, 7, kieu="su_kien").startswith("GIẢM TIỀN"))
kiem("sự kiện: ≤ 400k/gia đình → GIỮ", quyet_dinh(d(2_000_000, 6), NG, 2_000_000, 7, kieu="su_kien").startswith("GIỮ"))
kiem("Nhật/Hàn/Đài: ≥ 2,5 tr chưa ai để lại số → DỪNG",
     quyet_dinh(d(2_600_000, lead=0), NG, 2_600_000, 7, kieu="nuoc_ngoai").startswith("DỪNG"))

# 6. Chạy thật qua dòng lệnh với file tạm (không --luu)
with tempfile.TemporaryDirectory() as td:
    import csv
    pa, pl = Path(td) / "ads.csv", Path(td) / "so-nguon-khach.csv"
    for p, rows in ((pa, ads[:2]), (pl, leads)):
        with p.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, "-X", "utf8", str(ROOT / "tools" / "doc_ads.py"), "--ads", str(pa),
                        "--leads", str(pl)], capture_output=True, text=True, encoding="utf-8", env=env, cwd=ROOT)
    out = r.stdout + r.stderr
    kiem("dòng lệnh chạy được (mã 0)", r.returncode == 0)
    kiem("có báo cáo + phễu + bảng theo ý tưởng + theo mẫu",
         all(x in out for x in ("BÁO CÁO QUẢNG CÁO", "Cuộc nói chuyện", "Phễu:", "THEO Ý TƯỞNG", "THEO MẪU")))
    kiem("báo cáo không in tên/SĐT khách", "Nguyen" not in out and "+849" not in out)
    kiem("có cảnh báo [GIẢ THUYẾT] khi tổng chi < 10 triệu", "< 10 triệu" in out)
    if r.returncode:
        print(out[-1500:])

moc2 = DB_PATH.stat() if DB_PATH.exists() else None
kiem("canh gác: data/marketing.db không bị đụng",
     (moc is None and moc2 is None) or (moc and moc2 and (moc.st_mtime, moc.st_size) == (moc2.st_mtime, moc2.st_size)))
print(f"\nKẾT QUẢ: {ok}/{ok + sai} đúng")
sys.exit(1 if sai else 0)
