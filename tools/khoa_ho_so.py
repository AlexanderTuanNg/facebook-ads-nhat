"""Khoá hồ sơ trình duyệt: mỗi lúc chỉ 1 tiến trình dùng .profiles/<nick> (Gemini duyệt kế hoạch 26/09).

- `lay_khoa(nick)`: gọi trong `fb_group.open_context` → mọi công cụ (đăng bài, nhắn tin, kết bạn, đọc group) đều qua khoá.
  Tạo file data/profile_<nick>.lock (PID) nguyên tử; tiến trình khác còn sống đang giữ → FlowError PROFILE_BUSY
  (không mở trình duyệt) + ghi 1 dòng vào data/profile_busy.log cho người dùng xem. Tiến trình thoát → tự trả khoá (atexit).
- Khoá của tiến trình đã chết (tắt ngang) → coi là cũ, thay. Khoá hỏng nội dung → dừng (không ghi đè), người xem rồi tự xoá.
- Kiểm PID bằng OpenProcess (ctypes) — KHÔNG dùng os.kill(pid, 0): trên Windows lệnh đó giết tiến trình.
"""
import atexit
import ctypes
import os
import sys
from contextlib import contextmanager

from common import ROOT, now_str

LOG = ROOT / "data" / "profile_busy.log"


def pid_con_song(pid: int) -> bool:
    if pid <= 0:
        return False
    k32 = ctypes.windll.kernel32
    h = k32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
    if not h:
        return False
    try:
        code = ctypes.c_ulong()
        return bool(k32.GetExitCodeProcess(h, ctypes.byref(code))) and code.value == 259  # STILL_ACTIVE
    finally:
        k32.CloseHandle(h)


def file_khoa(nick: str):
    return ROOT / "data" / f"profile_{nick}.lock"


def _doc_pid(f):
    """None = không có khoá; -1 = khoá hỏng; còn lại = PID đang ghi trong khoá."""
    try:
        noi_dung = f.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    dau = noi_dung.split()[:1]
    return int(dau[0]) if dau and dau[0].isdigit() else -1


def _ghi_log(dong: str) -> None:
    with open(LOG, "a", encoding="utf-8") as fh:  # chỉ ghi thêm (nhật ký), không đọc-rồi-ghi-đè
        fh.write(f"{now_str()} {dong}\n")


def lay_khoa(nick: str) -> None:
    from fb_group import FlowError

    f = file_khoa(nick)
    ten = os.path.basename(sys.argv[0]) or "python"
    for _ in range(3):
        try:
            fd = os.open(f, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            pid = _doc_pid(f)
            if pid is None:
                continue  # vừa bị trả → thử tạo lại
            if pid == os.getpid():
                return  # chính mình đang giữ
            if pid == -1 or pid_con_song(pid):
                ly_do = "khoá hỏng nội dung" if pid == -1 else f"đang được tiến trình {pid} dùng"
                _ghi_log(f"PROFILE_BUSY {nick}: {ten} (pid {os.getpid()}) không mở được trình duyệt — hồ sơ {ly_do} ({f.name})")
                raise FlowError("PROFILE_BUSY", f"hồ sơ {nick} {ly_do} ({f}); xem data/profile_busy.log")
            try:
                f.unlink()  # khoá cũ của tiến trình đã chết
            except FileNotFoundError:
                pass
            continue
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(f"{os.getpid()} {ten}\n")
        atexit.register(tra_khoa, nick)
        return
    raise FlowError("PROFILE_BUSY", f"không giữ được khoá {f} sau 3 lần thử")


def tra_khoa(nick: str) -> None:
    f = file_khoa(nick)
    if _doc_pid(f) == os.getpid():
        try:
            f.unlink()
        except FileNotFoundError:
            pass


@contextmanager
def giu_khoa(nick: str):
    lay_khoa(nick)
    try:
        yield
    finally:
        tra_khoa(nick)
