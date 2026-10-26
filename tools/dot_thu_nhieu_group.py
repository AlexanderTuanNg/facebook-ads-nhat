"""Lượt đăng thử nhiều group: NGƯỜI DÙNG TỰ CHẠY (hệ thống an toàn không cho Claude tự chạy đăng hàng loạt).

  python "D:\\Tuan\\12. Tool bán hàng\\tools\\dot_thu_nhieu_group.py"

Mỗi bài theo thứ tự: chờ bài được duyệt (approved_human) → chờ đủ khoảng cách giữa 2 bài (can-post, đang 5 phút)
→ trình duyệt điền sẵn → người dùng tự xem và bấm Đăng. Dừng ngay khi: có file data/stop_batch, can-post báo
LIMIT/PAUSED/ERROR, hoặc bước điền bài lỗi. Dừng tay: Ctrl+C.
Người dùng chọn "9 group, cách 5 phút" ngày 25/09/2026 (xem STATE.md, nhật ký quyết định).
"""
import os
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THU_TU = [11, 12, 13, 16, 14, 3, 17, 15, 18]  # bài đã duyệt đi trước; bài 14 và 18 giống nhau 0.54 → xếp xa nhau
STOP = ROOT / "data" / "stop_batch"
KET_THUC = ("approved_human", "rejected", "published", "failed", "skipped", "pending_approval")


def gio():
    return datetime.now().strftime("%H:%M:%S")


def trang_thai(pid):
    con = sqlite3.connect(ROOT / "data" / "marketing.db")
    try:
        return con.execute("SELECT status, target_id FROM posts WHERE id=?", (pid,)).fetchone()
    finally:
        con.close()


def can_post(gid):
    out = subprocess.run([sys.executable, "tools/db.py", "can-post", "2", "--group", str(gid)],
                         capture_output=True, text=True, encoding="utf-8").stdout.strip().splitlines()
    return out[-1] if out else "ERROR không đọc được can-post"


def main():
    os.chdir(ROOT)
    os.environ["PYTHONUTF8"] = "1"
    os.environ["PYTHONUNBUFFERED"] = "1"
    sys.stdout.reconfigure(encoding="utf-8")
    xong = 0
    for pid in THU_TU:
        if STOP.exists():
            print(f"{gio()} DỪNG: có file data/stop_batch")
            break
        st, gid = trang_thai(pid)
        for _ in range(120):  # chờ bài được duyệt, tối đa 40 phút
            st, gid = trang_thai(pid)
            if st in KET_THUC or STOP.exists():
                break
            time.sleep(20)
        if st != "approved_human":
            print(f"{gio()} BỎ QUA bài {pid} (trạng thái {st})")
            continue
        v = ""
        for _ in range(60):  # chờ đủ khoảng cách giữa 2 bài
            v = can_post(gid)
            if v == "OK" or v.startswith(("LIMIT", "PAUSED", "ERROR")) or STOP.exists():
                break
            time.sleep(20)
        if v != "OK":
            print(f"{gio()} DỪNG: bài {pid} (group {gid}): {v}")
            break
        print(f"{gio()} >>> Bài {pid} → group {gid}: trình duyệt đang điền sẵn, bạn xem rồi bấm ĐĂNG")
        r = subprocess.run([sys.executable, "tools/fb_group.py", "prefill", "--post-id", str(pid)],
                           capture_output=True, text=True, encoding="utf-8")
        print((r.stdout or "") + (r.stderr or ""), end="")
        print(f"{gio()} <<< Bài {pid}: mã thoát {r.returncode}")
        if r.returncode != 0:
            if "composer_open" in (r.stdout or "") + (r.stderr or ""):
                # Nhóm kiểu Mua–Bán (chỉ có nút "Bán gì đó"), không phải Facebook chặn → bỏ qua group này, đi tiếp
                print(f"BỎ QUA bài {pid}: group không có ô viết bài thường (nhóm Mua–Bán)")
                continue
            print(f"DỪNG: bước điền bài lỗi (xem data/error_post{pid}.png nếu có). "
                  "Nếu lỗi là photo_input: bạn tự bấm nút Ảnh trong khung soạn để chọn ảnh, rồi báo Claude.")
            break
        xong += 1
    print(f"{gio()} KẾT THÚC lượt thử: {xong} bài đã điền xong")


if __name__ == "__main__":
    main()
