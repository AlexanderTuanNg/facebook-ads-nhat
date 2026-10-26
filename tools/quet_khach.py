"""Quét khách ban đêm (CHỈ ĐỌC Facebook) → danh sách khách cần liên hệ + số đo thử nghiệm.

Người dùng 25/10/2026: "bằng mọi giá phải tìm được lead… tự test, tự auto đánh giá, ko hiệu quả thì tìm cách khác".
Chạy từ lich_dang.py lúc ~22:20 (sau bài cuối ngày, không giành trình duyệt của lịch đăng):
  1) thu_tuong_tac.py cho các group có bài của nick trong 5 ngày qua → bảng leads (người thích / bình luận)
  2) tim_khach_mua.py (group địa phương) → bài người ĐANG TÌM MUA đất
  3) ghi data/khach/khach-<ngày>.md (danh sách cho sale) + data/khach/so-do-<ngày>.json (số đo thử nghiệm T2/T3)
Không bấm thích, không bình luận, không nhắn tin, không kết bạn. Dữ liệu người thật → để trong data/ (không đưa vào workspace).

  python tools/quet_khach.py                 # đầy đủ
  python tools/quet_khach.py --chi-bao-cao   # chỉ lập báo cáo từ dữ liệu đã có
"""
import argparse
import glob
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta

from common import ROOT, connect

PY = [sys.executable, "-X", "utf8"]
NONG = re.compile(r"giá|gia\b|bao nhiêu|bn\b|sổ|xin|ib|inbox|ỉb|vị trí|ở đâu|địa chỉ|quan tâm|còn lô|mấy tỷ|tỷ|tr\b|triệu|liên hệ|sđt|số điện thoại|\d{9,}", re.I)
RAC = re.compile(r"sửa (?:tivi|máy|tủ)|lh 0\d|chuyên|dịch vụ|nhận làm|vay|tín dụng", re.I)


def chay(lenh: list[str], gioi_han: int) -> str:
    try:
        r = subprocess.run(PY + [str(ROOT / "tools" / lenh[0]), *lenh[1:]], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", cwd=str(ROOT), timeout=gioi_han)
        return (r.stdout + "\n" + r.stderr).strip()
    except subprocess.TimeoutExpired:
        return f"QUÁ {gioi_han // 60} PHÚT"


def bao_cao(con, ngay: str) -> dict:
    tu = (datetime.strptime(ngay, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d 22:00:00")
    leads = [dict(r) for r in con.execute(
        "SELECT l.id, l.source_post_id, l.name, l.channel_user, l.need, l.notes, l.created_at, p.compliance_note, g.name nhom "
        "FROM leads l LEFT JOIN posts p ON p.id=l.source_post_id LEFT JOIN groups g ON g.id=p.target_id WHERE l.created_at>=?", (tu,))]
    for x in leads:
        x["nong"] = bool(x["need"] and x["need"].startswith("bình luận") and NONG.search(x["need"]) and not RAC.search(x["need"]))
        x["rac"] = bool(x["need"] and RAC.search(x["need"]))
    mua = []
    for f in sorted(glob.glob(str(ROOT / "data" / f"tim_khach_{ngay.replace('-', '')}_*.jsonl"))):
        for dong in open(f, encoding="utf-8"):
            x = json.loads(dong)
            if x.get("loai") in ("mua", "thue"):
                mua.append(x)
    # Số đo T3: bình luận theo kiểu lời kêu gọi (CTA-B = "bình luận giá"), bài đăng trong 5 ngày qua
    tu5 = (datetime.strptime(ngay, "%Y-%m-%d") - timedelta(days=5)).strftime("%Y-%m-%d")
    bai = [dict(r) for r in con.execute(
        "SELECT p.id, p.compliance_note, (SELECT count(*) FROM leads l WHERE l.source_post_id=p.id AND l.need LIKE 'bình luận%') bl, "
        "(SELECT count(*) FROM leads l WHERE l.source_post_id=p.id AND l.need LIKE 'thích%') th FROM posts p "
        "WHERE p.account_id=2 AND p.channel='group' AND p.status IN ('published','pending_approval') AND p.published_at>=? "
        "AND p.published_at<?", (tu5, (datetime.strptime(ngay, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")))]
    nhom = {"A": [b for b in bai if "[CTA-B]" not in (b["compliance_note"] or "")],
            "B": [b for b in bai if "[CTA-B]" in (b["compliance_note"] or "")]}
    so_do = {"ngay": ngay, "lead_moi": len(leads), "lead_nong": sum(x["nong"] for x in leads), "rac": sum(x["rac"] for x in leads),
             "nguoi_tim_mua": sum(x.get("loai") == "mua" for x in mua), "nguoi_can_thue": sum(x.get("loai") == "thue" for x in mua),
             "cta": {k: {"so_bai": len(v), "binh_luan": sum(b["bl"] for b in v), "thich": sum(b["th"] for b in v)} for k, v in nhom.items()}}
    thu = ROOT / "data" / "khach"
    thu.mkdir(exist_ok=True)
    (thu / f"so-do-{ngay}.json").write_text(json.dumps(so_do, ensure_ascii=False, indent=1), encoding="utf-8")
    d = [f"# Khách cần liên hệ — {ngay}", "",
         f"Người tìm mua đất: **{len(mua)}** · bình luận hỏi giá/sổ (nóng): **{so_do['lead_nong']}** · thích/bình luận khác: "
         f"{len(leads) - so_do['lead_nong'] - so_do['rac']} · quảng cáo rác: {so_do['rac']}", "",
         "Cách liên hệ: sale dùng nick thật của mình, TRẢ LỜI CÔNG KHAI dưới bài/bình luận của họ trong 1 giờ, mời gọi hotline; "
         "không chép số điện thoại từ bài người khác để gọi/nhắn, không gửi hàng loạt (Luật BVDLCN 91/2025 — cần luật sư xác nhận).", ""]
    for loai, tieu_de in (("mua", "## 1. Người đang tìm mua đất (Yên Thế Golden Hill — trả lời trước)"),
                          ("thue", "## 1b. Người đang cần thuê nhà / văn phòng / mặt bằng (dự án cho thuê toà nhà)")):
        ds = [x for x in mua if x.get("loai") == loai]
        if ds:
            d += [tieu_de, ""] + [f"- [{x.get('group', '')[:40]}] {x.get('noi_dung', '')[-220:].strip()} — {x.get('link', '')}" for x in ds] + [""]
    nong = [x for x in leads if x["nong"]]
    if nong:
        d += ["## 2. Bình luận hỏi giá / hỏi sổ dưới bài của mình", ""]
        d += [f"- {x['name']} ({x['nhom'] or ''}) · \"{x['need'][11:120]}\" — {x['channel_user']}" for x in nong]
        d.append("")
    khac = [x for x in leads if not x["nong"] and not x["rac"]]
    if khac:
        d += ["## 3. Người thích / bình luận khác (chăm sau)", ""]
        d += [f"- {x['name']} ({x['nhom'] or ''}) · {x['need'][:60]} — {x['channel_user']}" for x in khac[:40]]
        d.append("")
    d += ["## Số đo thử nghiệm", "", "```", json.dumps(so_do, ensure_ascii=False, indent=1), "```"]
    (thu / f"khach-{ngay}.md").write_text("\n".join(d) + "\n", encoding="utf-8")
    return so_do


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chi-bao-cao", action="store_true")
    ap.add_argument("--ngay", default=datetime.now().strftime("%Y-%m-%d"))
    a = ap.parse_args()
    con = connect()
    if not a.chi_bao_cao:
        tu5 = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d %H:%M:%S")
        ids = [str(r[0]) for r in con.execute(
            "SELECT DISTINCT target_id FROM posts WHERE account_id=2 AND channel='group' AND status IN ('published','pending_approval') "
            "AND published_at>=?", (tu5,))]
        if ids:
            out = chay(["thu_tuong_tac.py", "--groups", ",".join(ids)], 3600)
            print("thu_tuong_tac:", " / ".join(out.splitlines()[-2:]), flush=True)
            if re.search(r"DỪNG NGAY|CHECKPOINT|SESSION_EXPIRED|PROFILE_BUSY", out):
                print("DỪNG NGAY: cảnh báo khi quét bình luận → bỏ quét người tìm mua")
                bao_cao(con, a.ngay)
                return
        out = chay(["tim_khach_mua.py", "--so", "20", "--scrolls", "6"], 2400)
        print("tim_khach_mua:", " / ".join(out.splitlines()[-2:]) if out else "", flush=True)
    s = bao_cao(con, a.ngay)
    print(f"XONG quét khách: tìm mua {s['nguoi_tim_mua']}, hỏi giá/sổ {s['lead_nong']}, lead mới {s['lead_moi']} → data/khach/khach-{a.ngay}.md")


if __name__ == "__main__":
    main()
