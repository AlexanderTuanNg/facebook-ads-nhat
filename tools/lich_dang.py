"""Lịch tự đăng trên máy — kế hoạch `workspace/plans/2026-09-26-tang-toc-dang-bai.md` (Gemini duyệt vòng 2, 26/09).

  python tools/lich_dang.py --tu "2026-09-27 00:00" --den "2026-09-27 23:59" --thu   # chạy khô: in lịch, không đăng
  python tools/lich_dang.py --tu "2026-09-27 00:00" --den "2026-09-27 23:59"         # chờ tới giờ từng bài rồi tự đăng

Chọn bài: group, `approved_human`, nhánh B, `scheduled_at` trong [--tu, --den], sắp theo giờ. Mỗi bài: chờ tới giờ hẹn
+ lệch ngẫu nhiên 1–5 phút → `fb_group.py autopost` (tiến trình riêng; đã có khoá hồ sơ, can-post, lint, dừng khi
checkpoint). Có data/stop_batch (dừng tay khi có sự cố; từ 28/09 tối hạn mức tuần ≥ 70% KHÔNG dừng lịch — CLAUDE.md) → không đăng. Kết quả:
  PUBLISHED / PENDING_APPROVAL → đi tiếp · PROFILE_BUSY (công cụ khác đang dùng trình duyệt) → chờ 3 phút, thử lại
  · "WAIT n phút" → chờ n phút · "LIMIT ..." → bỏ bài này, đi tiếp · mọi lỗi khác (CHECKPOINT, SESSION_EXPIRED, lỗi
  giao diện, lint...) → DỪNG CẢ LỊCH. Có file data/stop_batch → dừng. Nhật ký: data/lich_dang_<ngày>.log.
"""
import argparse
import random
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta

from common import ROOT, connect, now_str, read_post_file
from db import can_post, lint_text

PY = [sys.executable, "-X", "utf8"]
STOP = ROOT / "data" / "stop_batch"
# Việc hằng ngày ~14:10 (ngoài khung đăng bài, trước 17:00): gửi tin cho lead vừa đồng ý kết bạn → 5 lời mời mới
# (ket_ban.py tự giới hạn 5/ngày) → vào 4 nhóm mới (người dùng 26/09: "vào thêm 2 nhóm mỗi ngày"; 28/09 chiều: nhóm cũ không
# ra lead, "chủ động vào các group khác đi… tự bạn xử lý" → 4/ngày, cách 2–4 phút, dừng ngay khi Facebook cảnh báo).
# 05/10: người dùng chốt 16 bài/ngày → cần thêm group (52 group cách 3 ngày ≈ tối đa 17 bài/ngày) → 6 nhóm/ngày.
# 11/10: Messenger báo nick bị hạn chế ("xác nhận danh tính… hoạt động bất thường") → người dùng chọn "giảm tải, giữ đăng
# bài": TẠM bỏ ket_ban (mời kết bạn + nhắn tin), vào nhóm 6 → 2/ngày, tới khi người dùng xác nhận danh tính xong.
# Bản đầy đủ để bật lại: [["thu_tuong_tac.py"], ["ket_ban.py", "--gui-tin-ban-moi"], ["ket_ban.py"], ["vao_nhom.py", "--so", "6"]]
# 14/10: người dùng "tập trung nhóm khu công nghiệp và đồng hương trước" → 190 nhóm ứng viên (quality_score 40/25) → vào 4/ngày.
# 20/10: người dùng "Mình vẫn thấy check post và kết bạn đấy, giờ bạn chỉ cho đăng bài thôi đi" → TẮT HẾT việc 14:10
# (thu_tuong_tac mở trang người thích bài có nút "Thêm bạn bè"; vao_nhom). Bật lại: [["thu_tuong_tac.py"], ["vao_nhom.py", "--so", "4"]]
# 21/10: người dùng chọn "12 bài/ngày + bật lại vào nhóm mới" → chỉ bật vao_nhom (thu_tuong_tac, ket_ban, nhan_tin vẫn TẮT).
VIEC_NGAY = [["vao_nhom.py", "--so", "4"]]
GIO_VIEC_NGAY = (14, 10)
# 25/10 người dùng: "bằng mọi giá phải tìm được lead… tự test, tự auto đánh giá" → việc ĐÊM ~22:20 (sau bài cuối, không giành trình
# duyệt ban ngày): quet_khach.py = thu_tuong_tac (CHỈ ĐỌC bình luận/thích bài 5 ngày qua) + tim_khach_mua (người đang tìm mua) → data/khach/.
# Không kết bạn, không nhắn tin. Tắt: VIEC_DEM = [].
VIEC_DEM = [["quet_khach.py"]]
GIO_VIEC_DEM = (22, 20)


def viec_dem(da_lam: set) -> None:
    bay_gio = datetime.now()
    dau = ROOT / "data" / f"viec_dem_{bay_gio:%Y-%m-%d}.xong"
    if not VIEC_DEM or bay_gio.date() in da_lam or dau.exists() or (bay_gio.hour, bay_gio.minute) < GIO_VIEC_DEM:
        return
    con = connect()
    con_bai = con.execute("SELECT 1 FROM posts WHERE status='approved_human' AND channel='group' AND scheduled_at BETWEEN ? AND ?",
                          ((bay_gio - timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S"), f"{bay_gio:%Y-%m-%d} 23:59:59")).fetchone()
    if con_bai:
        return  # còn bài hôm nay chưa đăng → chờ
    da_lam.add(bay_gio.date())
    dau.write_text(now_str(), encoding="utf-8")
    for lenh in VIEC_DEM:
        if STOP.exists():
            return
        try:
            r = subprocess.run(PY + [str(ROOT / "tools" / lenh[0]), *lenh[1:]], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", cwd=str(ROOT), timeout=7200)
            out = (r.stdout + chr(10) + r.stderr).strip()
        except subprocess.TimeoutExpired:
            out = "QUÁ 120 PHÚT"
        ghi(f"VIỆC ĐÊM {' '.join(lenh)}: " + " / ".join(out.splitlines()[-3:]))


def viec_hang_ngay(da_lam: set) -> None:
    bay_gio = datetime.now()
    # Dấu đã làm ghi ra file → lịch khởi động lại trong ngày (Windows Task Scheduler bật khi đăng nhập) không làm lại lần 2
    dau = ROOT / "data" / f"viec_ngay_{bay_gio:%Y-%m-%d}.xong"
    if bay_gio.date() in da_lam or dau.exists() or (bay_gio.hour, bay_gio.minute) < GIO_VIEC_NGAY or bay_gio.hour >= 17:
        return
    da_lam.add(bay_gio.date())
    dau.write_text(now_str(), encoding="utf-8")
    for lenh in VIEC_NGAY:
        if STOP.exists():
            return
        try:
            r = subprocess.run(PY + [str(ROOT / "tools" / lenh[0]), *lenh[1:]], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", cwd=str(ROOT), timeout=3600)
            out = (r.stdout + "\n" + r.stderr).strip()
        except subprocess.TimeoutExpired:
            out = "QUÁ 60 PHÚT"
        ghi(f"VIỆC NGÀY {' '.join(lenh)}: " + " / ".join(out.splitlines()[-3:]))
        if re.search(r"DỪNG NGAY|CHECKPOINT|SESSION_EXPIRED|PROFILE_BUSY|QUÁ 60 PHÚT", out):
            ghi("VIỆC NGÀY: có cảnh báo/lỗi → bỏ các việc còn lại hôm nay")
            return


def ghi(dong: str) -> None:
    dong = f"{now_str()} {dong}"
    print(dong, flush=True)
    with open(ROOT / "data" / f"lich_dang_{now_str()[:10]}.log", "a", encoding="utf-8") as fh:
        fh.write(dong + "\n")


def bai_trong_khung(con, tu: str, den: str):
    return [dict(r) for r in con.execute(
        "SELECT p.id, p.target_id, p.account_id, p.scheduled_at, p.content_path, g.name AS nhom FROM posts p "
        "JOIN groups g ON g.id = p.target_id WHERE p.channel='group' AND p.status='approved_human' AND p.arm='B' "
        "AND p.published_at IS NULL AND p.scheduled_at BETWEEN ? AND ? ORDER BY p.scheduled_at", (tu, den))]


def cho_toi(moc: datetime) -> bool:
    """Ngủ tới mốc; trả False nếu có data/stop_batch."""
    while True:
        if STOP.exists():
            return False
        con_lai = (moc - datetime.now()).total_seconds()
        if con_lai <= 0:
            return True
        time.sleep(min(30, con_lai))


def phut_toi_moc_group(group_id: int):
    """Số phút còn lại tới khi bài gần nhất của mình ở group này đủ `same_group_min_days` ngày (None nếu chưa có bài)."""
    from common import settings

    r = connect().execute("SELECT MAX(published_at) FROM posts WHERE target_id=? AND channel='group' AND published_at IS NOT NULL "
                          "AND status IN ('published','pending_approval','removed')", (group_id,)).fetchone()[0]
    if not r:
        return None
    moc = datetime.strptime(r[:19], "%Y-%m-%d %H:%M:%S") + timedelta(days=settings()["limits"]["same_group_min_days"])
    return max(0, int((moc - datetime.now()).total_seconds() // 60) + 1)


def bai_truoc_bi_go(bai: dict) -> bool:
    """Trước khi đăng vào group: bài gần nhất của mình ở group đó còn hiện không (`fb_group.py stats`)? Bị admin gỡ → không đăng
    tiếp vào group này (compliance 28/09: bài 25, 27 chỉ đăng khi bài trước còn hiện; luật "2 bài bị gỡ → bỏ group").
    20/10: người dùng "chỉ cho đăng bài thôi" (thấy trình duyệt mở bài cũ tưởng là check post/kết bạn) → TẮT, không mở bài cũ.
    Bật lại: xoá 2 dòng KIEM_BAI_TRUOC ngay dưới."""
    KIEM_BAI_TRUOC = False
    if not KIEM_BAI_TRUOC:
        return False
    r = connect().execute(
        "SELECT id FROM posts WHERE target_id=? AND id<>? AND channel='group' AND status IN ('published','pending_approval','removed') "
        "AND published_at IS NOT NULL ORDER BY published_at DESC LIMIT 1", (bai["target_id"], bai["id"])).fetchone()
    if not r:
        return False
    kq = subprocess.run(PY + [str(ROOT / "tools" / "fb_group.py"), "stats", "--post-id", str(r["id"])], capture_output=True,
                        text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
    m = re.search(r'"state":\s*"(\w+)"', kq.stdout)
    st = m.group(1) if m else "?"  # bận trình duyệt / lỗi đọc → không kết luận gỡ, vẫn đăng
    ghi(f"KIỂM bài trước {r['id']} ở {bai['nhom']}: {st}")
    return st == "removed"


def chon_nhom_thay(con, bai: dict, da_thu: set):
    """Nhóm thay khi nhóm của bài hỏng: 'joined', hết làm quen, chưa từng bị gỡ bài, không trong LOAI, can-post OK
    (đủ 3 ngày). Ưu tiên nhóm KHÔNG có bài hẹn trong 3 ngày tới (khỏi giành chỗ bài khác), rồi nhóm không 'ƯU TIÊN THẤP',
    rồi nhóm ít bài, rồi nhóm lâu chưa đăng. Không còn nhóm → None."""
    from lap_lich_bai import LOAI

    t = now_str()
    sau3 = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S")
    ds = []
    for g in con.execute(
            "SELECT g.id, g.name, g.notes, (SELECT count(*) FROM posts p WHERE p.target_id=g.id AND p.published_at IS NOT NULL) AS da_dang, "
            "(SELECT max(published_at) FROM posts p WHERE p.target_id=g.id) AS cuoi, "
            "(SELECT count(*) FROM posts p WHERE p.target_id=g.id AND p.id<>? AND p.status='approved_human' "
            " AND p.published_at IS NULL AND p.scheduled_at BETWEEN ? AND ?) AS sap "
            "FROM groups g WHERE g.status='joined' AND COALESCE(g.removed_count,0)=0 "
            "AND (g.warmup_until IS NULL OR g.warmup_until<=?)", (bai["id"], t, sau3, t)):
        if g["id"] in LOAI or g["id"] in da_thu or g["id"] == bai["target_id"]:
            continue
        cp = can_post(con, bai["account_id"], g["id"])
        if not (cp == "OK" or cp.startswith("WAIT")):  # WAIT = chỉ chờ giãn cách giữa 2 bài, nhóm vẫn dùng được
            continue
        ds.append(dict(g))
    ds.sort(key=lambda g: (g["sap"] > 0, "ƯU TIÊN THẤP" in (g["notes"] or ""), g["da_dang"], g["cuoi"] or ""))
    return ds[0] if ds else None


def doi_nhom(bai: dict, da_thu: set):
    """Chuyển bài sang nhóm thay (DB + dòng target: trong file bài, giữ nguyên byte khác — không dùng PowerShell vì chèn BOM)."""
    con = connect()
    g = chon_nhom_thay(con, bai, da_thu)
    if g is None:
        return None
    f = ROOT / bai["content_path"]
    txt = f.read_text(encoding="utf-8")
    ten = g["name"].replace('"', "'")
    f.write_text(re.sub(r"^target: .*$", f'target: "{ten}"', txt, count=1, flags=re.M), encoding="utf-8", newline="")
    con.execute("UPDATE posts SET target_id=?, status='approved_human' WHERE id=?", (g["id"], bai["id"]))
    con.commit()
    ghi(f"ĐỔI NHÓM bài {bai['id']}: g{bai['target_id']} {bai['nhom']} → g{g['id']} {g['name']}"
        + (" (mượn nhóm đã có bài hẹn 3 ngày tới)" if g["sap"] else ""))
    return {**bai, "target_id": g["id"], "nhom": g["name"]}


def dang_mot(bai: dict) -> str:
    """'OK' | 'BO_QUA' | 'DUNG' | 'DOI_NHOM'."""
    for lan in range(8):
        if STOP.exists():
            return "DUNG"
        r = subprocess.run(PY + [str(ROOT / "tools" / "fb_group.py"), "autopost", "--post-id", str(bai["id"])],
                           capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(ROOT))
        out = (r.stdout + "\n" + r.stderr).strip()
        cuoi = out.splitlines()[-1] if out else ""
        if r.returncode == 0 and re.search(r"^(PUBLISHED|PENDING_APPROVAL) post", r.stdout, re.M):
            ghi(f"OK bài {bai['id']} → {bai['nhom']}: {r.stdout.strip().splitlines()[-1]}")
            return "OK"
        if "PROFILE_BUSY" in out:
            ghi(f"CHỜ bài {bai['id']}: trình duyệt đang bận (lần {lan + 1}) → thử lại sau 3 phút")
            time.sleep(180)
            continue
        # Chưa đủ 3 ngày cùng group nhưng chỉ thiếu ít (bài trước đăng trễ vài phút) → chờ tới mốc rồi đăng, không bỏ bài
        if re.search(r"LIMIT group \d+ đã đăng", out):
            cho = phut_toi_moc_group(bai["target_id"])
            if cho is not None and cho <= 90:
                ghi(f"CHỜ bài {bai['id']}: còn {cho} phút mới đủ 3 ngày ở group này")
                time.sleep((cho + 2) * 60)
                continue
        m = re.search(r"WAIT (\d+) phút", out)
        if m:
            ghi(f"CHỜ bài {bai['id']}: can-post {m.group(0)}")
            time.sleep((int(m.group(1)) + 1) * 60)
            continue
        # "không thấy ô đăng bài" (nhóm Mua–Bán, chưa được duyệt vào) là lỗi riêng của group → bỏ bài này, không dừng cả lịch.
        # 06/10: bài 70, 71 rơi vào nhóm Mua–Bán (chỉ có nút "Bán gì đó") vì nhóm vẫn 'joined' → đánh dấu bo_qua để
        # lap_lich_bai.py (chỉ lấy 'joined') không xếp lại.
        if re.search(r"SELECTOR_NOT_FOUND:? composer_open", out):
            con = connect()
            con.execute("UPDATE groups SET status='bo_qua', notes=COALESCE(notes,'') || ? WHERE id=?",
                        (f" | [{now_str()[:16]}] không thấy ô đăng bài thường (nhóm Mua–Bán 'Bán gì đó'?) → bo_qua", bai["target_id"]))
            con.commit()
        # Lỗi do NHÓM (không phải do bài) → đổi sang nhóm khác cho đủ KPI ngày (người dùng 06/10: "không đăng được thì đổi
        # hết sang các group khác đi, chủ động lên, đăng cho đủ KPI 1 ngày")
        if re.search(r"SELECTOR_NOT_FOUND:? composer_open|LIMIT group \d+ đã đăng", out):
            ghi(f"CẦN ĐỔI NHÓM bài {bai['id']} → {bai['nhom']}: {cuoi}")
            return "DOI_NHOM"
        if re.search(r"LIMIT|ERROR: status=|BLOCKED_BY_LINT|ERROR: thiếu ảnh|ERROR: không có group|SELECTOR_NOT_FOUND:? composer_open", out):
            ghi(f"BỎ QUA bài {bai['id']} → {bai['nhom']} (lỗi riêng của bài): {cuoi}")
            return "BO_QUA"
        # Nick có vấn đề → dừng cả lịch. Lỗi lạ khác (06/10 18:46 bài 82: Playwright hết giờ, chạy tay lại thì đăng được)
        # → chỉ bỏ bài này, lịch đi tiếp. KHÔNG tự thử lại: có thể đã bấm Đăng trước khi hỏng → thử lại = đăng trùng.
        if re.search(r"CHECKPOINT|SESSION_EXPIRED|LOGIN|BLOCKED|đăng nhập", out, re.I) and "BLOCKED_BY_LINT" not in out:
            ghi(f"DỪNG LỊCH ở bài {bai['id']} → {bai['nhom']} (mã {r.returncode}): {cuoi}")
            return "DUNG"
        ghi(f"BỎ QUA bài {bai['id']} → {bai['nhom']} (lỗi lạ, không tự thử lại để tránh đăng trùng; Claude kiểm tay) (mã {r.returncode}): {cuoi}")
        return "BO_QUA"
    ghi(f"DỪNG LỊCH: bài {bai['id']} thử 8 lần vẫn chưa đăng được")
    return "DUNG"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tu", help='"YYYY-MM-DD HH:MM"')
    ap.add_argument("--den", help='"YYYY-MM-DD HH:MM"')
    ap.add_argument("--hom-nay", action="store_true",
                    help="chạy từ giờ tới 23:59 hôm nay (Windows Task Scheduler bật mỗi sáng 06:30 + khi đăng nhập)")
    ap.add_argument("--thu", action="store_true", help="chạy khô: chỉ in lịch + kiểm tra, không đăng")
    ap.add_argument("--bo-viec-hom-nay", action="store_true", help="không chạy việc hằng ngày trong hôm nay (đã làm tay)")
    a = ap.parse_args()
    if a.hom_nay:
        d = datetime.now().strftime("%Y-%m-%d")
        a.tu, a.den = f"{d} 00:00", f"{d} 23:59"
    if not (a.tu and a.den):
        ap.error("cần --tu và --den, hoặc --hom-nay")
    if not a.thu:
        # Chỉ 1 lịch chạy một lúc (Windows Task Scheduler có thể bật lại khi đăng nhập / mỗi sáng)
        from fb_group import FlowError
        from khoa_ho_so import lay_khoa

        try:
            lay_khoa("lich_dang")
        except FlowError:
            ghi("Đã có một lịch tự đăng khác đang chạy → bản này thoát")
            return
    con = connect()
    ds = bai_trong_khung(con, a.tu, a.den)
    ghi(f"LỊCH {a.tu} → {a.den}: {len(ds)} bài" + (" (chạy khô)" if a.thu else ""))
    for b in ds:
        meta, body = read_post_file(ROOT / b["content_path"])
        anh = [p for p in (meta.get("images") or []) if not (ROOT / p).exists()]
        ghi(f"  bài {b['id']:>3} {b['scheduled_at']} → g{b['target_id']} {b['nhom'][:40]} | lint "
            f"{'PASS' if not lint_text(body) else 'LỖI'} | ảnh {'đủ' if not anh else 'THIẾU ' + ', '.join(anh)} | "
            f"can-post lúc này: {can_post(con, b['account_id'], b['target_id'])}")
    if a.thu:
        return
    # Chạy tới --den; đọc lại DB mỗi ≤ 5 phút để nhận bài mới duyệt thêm. Bài trễ giờ quá 60 phút (máy tắt, lịch
    # khởi động muộn) → bỏ qua, không dồn đăng một lúc nhiều bài.
    den = datetime.strptime(a.den[:16], "%Y-%m-%d %H:%M")
    lech, xong, da_lam = {}, set(), {datetime.now().date()} if a.bo_viec_hom_nay else set()
    da_lam_dem = set()
    while datetime.now() < den:
        if STOP.exists():
            ghi("DỪNG LỊCH: có data/stop_batch"); return
        viec_hang_ngay(da_lam)
        viec_dem(da_lam_dem)
        tu = max(a.tu, (datetime.now() - timedelta(minutes=60)).strftime("%Y-%m-%d %H:%M:%S"))
        ds = [b for b in bai_trong_khung(con, tu, a.den) if b["id"] not in xong]
        if not ds:
            time.sleep(300); continue
        b = ds[0]
        moc = datetime.strptime(b["scheduled_at"][:16], "%Y-%m-%d %H:%M") + timedelta(
            seconds=lech.setdefault(b["id"], random.randint(60, 300)))
        if (moc - datetime.now()).total_seconds() > 300:
            time.sleep(300); continue  # còn xa → ngủ rồi đọc lại DB
        ghi(f"Tới giờ bài {b['id']} → {b['nhom']} (hẹn {b['scheduled_at'][11:16]}, đăng lúc ~{moc:%H:%M})")
        if not cho_toi(moc):
            ghi("DỪNG LỊCH: có data/stop_batch"); return
        xong.add(b["id"])
        # Nhóm hỏng (chưa vào xong / bài trước bị gỡ / nhóm Mua–Bán / chưa đủ 3 ngày) → đổi tối đa 4 nhóm khác, đăng ngay
        da_thu = set()
        for _ in range(5):
            da_thu.add(b["target_id"])
            g = connect().execute("SELECT status, warmup_until FROM groups WHERE id=?", (b["target_id"],)).fetchone()
            if g["status"] != "joined" or (g["warmup_until"] and g["warmup_until"] > now_str()):
                ghi(f"CẦN ĐỔI NHÓM bài {b['id']} → {b['nhom']}: group chưa vào xong / còn làm quen (status {g['status']}, làm quen tới {g['warmup_until']})")
                kq = "DOI_NHOM"
            elif bai_truoc_bi_go(b):
                ghi(f"CẦN ĐỔI NHÓM bài {b['id']} → {b['nhom']}: bài trước của mình ở group này đã bị gỡ")
                kq = "DOI_NHOM"
            else:
                kq = dang_mot(b)
            if kq == "DUNG":
                return
            if kq != "DOI_NHOM":
                break
            moi = doi_nhom(b, da_thu)
            if moi is None:
                ghi(f"BỎ QUA bài {b['id']}: hết nhóm thay hợp lệ (cần vào thêm nhóm đúng vùng)")
                break
            b = moi
    ghi("XONG LỊCH")


if __name__ == "__main__":
    try:
        main()
    except Exception:  # noqa: BLE001 — chạy bằng pythonw (không cửa sổ) → lỗi phải vào nhật ký
        import traceback

        ghi("LỖI LỊCH (dừng): " + traceback.format_exc().replace("\n", " | ")[-1500:])
        raise
