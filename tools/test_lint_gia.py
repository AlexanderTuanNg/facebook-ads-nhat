"""Kiểm thử biên cho luật giá F1 + mốc giá KM7 trong lint (spec: workspace/plans/2026-09-25-A2-gia-moc.md).

  python tools/test_lint_gia.py      # in bảng, exit 1 nếu có ca sai

Hàm lint là hàm thuần: không ghi DB hay file. Canh gác (BH-0007): so thời điểm sửa của data/marketing.db
trước/sau khi chạy để khẳng định kiểm thử không đụng dữ liệu thật.
"""
import json
import sys
from datetime import date

from common import ROOT
from db import lint_text

HOM_NAY = date(2026, 9, 25)
PASS, FAIL = "PASS", "FAIL"

CASES = [
    ("🏡 XÂY NHÀ Ở QUÊ? CHỈ VỚI 500 TRIỆU ĐÃ SỞ HỮU LÔ ĐẤT", HOM_NAY, PASS),
    ("Trả trước 500 triệu khi ký, lô đến khoảng 1,3 tỷ.", HOM_NAY, PASS),
    ("Chỉ với 600 triệu đã có lô.", HOM_NAY, FAIL),
    ("Lô giá 1,3 tỷ.", HOM_NAY, FAIL),
    # (câu, hôm nay, đáp án)
    ("Chỉ khoảng 1 tỷ là mua được đất ở khu hạ tầng đẹp, quy hoạch đồng bộ ngay trung tâm Yên Thế.", HOM_NAY, PASS),
    ("CHỈ KHOẢNG 1 TỶ LÀ CÓ ĐẤT Ở TRUNG TÂM YÊN THẾ", HOM_NAY, PASS),
    ("Tầm 1 tỷ một lô, anh chị inbox mình gửi bảng giá chi tiết.", HOM_NAY, PASS),
    ("Giá khoảng 1 tỷ đồng là có lô để làm nhà.", HOM_NAY, PASS),
    ("Chỉ cần khoảng 1 tỷ/lô.", HOM_NAY, PASS),
    ("Cỡ 1 tỉ là đủ.", HOM_NAY, PASS),
    ("Nhắn tin/gọi 0965 539 599 để nhận bảng giá và chính sách.", HOM_NAY, PASS),
    ("Chỉ 1 tỷ là có đất.", HOM_NAY, FAIL),
    ("Hơn 1 tỷ là có lô.", HOM_NAY, FAIL),
    ("Dưới 1 tỷ là có lô.", HOM_NAY, PASS),  # 14/10: người dùng xác nhận còn lô dưới 1 tỷ
    ("🔥 LÀM KCN? CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU", HOM_NAY, PASS),
    ("Dưới 1 tỷ 2 là có lô.", HOM_NAY, FAIL),
    ("Dưới 900 triệu là có lô.", HOM_NAY, FAIL),
    ("Khoảng 1 tỷ 2 là có lô.", HOM_NAY, FAIL),
    ("Khoảng 1 tỷ rưỡi là có lô.", HOM_NAY, FAIL),
    ("Khoảng 1 tỷ 200 triệu.", HOM_NAY, FAIL),
    ("Khoảng 1,2 tỷ là có lô.", HOM_NAY, FAIL),
    ("Khoảng 11 tỷ cho cả dãy.", HOM_NAY, FAIL),
    ("Khoảng 2,1 tỷ lô góc.", HOM_NAY, FAIL),
    ("Chỉ từ 1,2 tỷ sở hữu ngay.", HOM_NAY, FAIL),
    ("Đất nền chỉ từ 650 triệu/lô.", HOM_NAY, FAIL),
    ("Giá khoảng 13 triệu/m².", HOM_NAY, FAIL),
    ("Giá gốc khoảng 1 tỷ, mua trực tiếp.", HOM_NAY, FAIL),
    ("Vị trí có hạ tầng đẹp nhất Yên Thế.", HOM_NAY, FAIL),
    # Hạn dùng mốc giá: xác nhận 2026-10-14 (trước: 2026-09-25) + 30 ngày → ngày cuối còn hạn 2026-11-13
    ("Chỉ khoảng 1 tỷ là mua được đất.", date(2026, 11, 20), PASS),
    ("Chỉ khoảng 1 tỷ là mua được đất.", date(2026, 11, 21), FAIL),
    ("Chỉ dưới 1 tỷ là có cơ hội sở hữu.", date(2026, 11, 21), FAIL),
    ("Bài không có giá, chỉ chia sẻ kinh nghiệm xem sổ.", date(2026, 12, 31), PASS),
]


def main():
    db = ROOT / "data" / "marketing.db"
    mtime_truoc = db.stat().st_mtime if db.exists() else None
    wrong = 0
    for text, today, expect in CASES:
        hits = lint_text(text, today=today)
        got = FAIL if hits else PASS
        ok = got == expect
        wrong += not ok
        print(f"{'OK ' if ok else 'SAI'}  {today}  {got:<4} (đáp án {expect})  {text[:60]}")
        if not ok:
            for h in hits:
                print("       ", h)

    # Hết hạn phải kèm lời nhắc xác nhận lại mốc giá
    hits = lint_text("Chỉ khoảng 1 tỷ là mua được đất.", today=date(2026, 11, 21))
    ok = any("quá hạn xác nhận" in h for h in hits)
    wrong += not ok
    print(f"{'OK ' if ok else 'SAI'}  hết hạn có lời nhắc 'quá hạn xác nhận'")

    # Cấu hình ngày lỗi: không được làm hỏng lint, coi như hết hạn (giá bị chặn)
    rules = json.loads((ROOT / "config" / "banned_terms.json").read_text(encoding="utf-8"))
    rules["_F1_moc_gia"]["F1_moc_gia_xac_nhan"] = "25/09/2026"
    try:
        hits = lint_text("Chỉ khoảng 1 tỷ là mua được đất.", today=HOM_NAY, rules=rules)
        ok = bool(hits) and any("cấu hình mốc giá lỗi" in h for h in hits)
    except Exception as e:  # noqa: BLE001 — kiểm thử phải bắt mọi lỗi để báo SAI
        ok = False
        print("        lỗi:", e)
    wrong += not ok
    print(f"{'OK ' if ok else 'SAI'}  cấu hình ngày sai định dạng → chặn giá, không sập lint")

    mtime_sau = db.stat().st_mtime if db.exists() else None
    ok = mtime_truoc == mtime_sau
    wrong += not ok
    print(f"{'OK ' if ok else 'SAI'}  canh gác: data/marketing.db không bị đụng khi chạy kiểm thử")

    total = len(CASES) + 3
    print(f"\nKẾT QUẢ: {total - wrong}/{total} đúng")
    sys.exit(1 if wrong else 0)


if __name__ == "__main__":
    main()
