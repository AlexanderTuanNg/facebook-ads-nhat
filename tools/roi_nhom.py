"""Rời nhóm Facebook (người dùng 26/10: "tin hữu lũng bị decline suốt thì out ra và bỏ group ấy đi").

  python tools/roi_nhom.py --nhom 291,293

Mở trang nhóm bằng hồ sơ nick_chinh (qua khoá hồ sơ, như mọi công cụ), KIỂM tên nhóm trên trang khớp tên trong DB rồi mới bấm
"Đã tham gia" → "Rời nhóm" → xác nhận "Rời nhóm". Ghi groups.status='bo_qua' + ghi chú "[ROI_NHOM <giờ>] DA_ROI" (hoặc mã lỗi).
Không đăng, không nhắn, không kết bạn.
"""
import argparse
import re
import unicodedata

from common import connect, now_str
from fb_group import FlowError, health_check, open_context


def _chuan(s: str) -> str:
    s = unicodedata.normalize("NFC", s or "").lower()
    return re.sub(r"[^\w]+", " ", s).strip()


def roi_mot(page, g) -> str:
    page.goto(g["url"], wait_until="domcontentloaded", timeout=60000)
    page.wait_for_timeout(4500)
    health_check(page)
    ten_db = _chuan(g["name"])[:14]
    h1 = page.locator("h1")
    tren_trang = _chuan(page.title()) + " " + (_chuan(h1.first.inner_text(timeout=5000)) if h1.count() else "")
    if ten_db and ten_db not in tren_trang:
        return "TEN_KHAC"  # trang không đúng nhóm → không bấm gì
    nut = page.get_by_role("button", name=re.compile(r"Đã tham gia|Joined", re.I))
    if nut.count() == 0:
        return "KHONG_THAY_NUT_DA_THAM_GIA"
    nut.first.click()
    page.wait_for_timeout(1500)
    muc = page.get_by_role("menuitem", name=re.compile(r"Rời nhóm|Leave group", re.I))
    if muc.count() == 0:
        muc = page.get_by_text(re.compile(r"^\s*(Rời nhóm|Leave group)\s*$", re.I))
    if muc.count() == 0:
        page.keyboard.press("Escape")
        return "KHONG_THAY_ROI_NHOM"
    muc.first.click()
    page.wait_for_timeout(1500)
    xn = page.get_by_role("dialog").get_by_role("button", name=re.compile(r"Rời khỏi nhóm|Rời nhóm|Leave group", re.I))  # hộp xác nhận 26/10: "Hủy" / "Rời khỏi nhóm"
    if xn.count() == 0:
        page.keyboard.press("Escape")
        return "KHONG_THAY_XAC_NHAN"
    xn.first.click()
    page.wait_for_timeout(3500)
    return "DA_ROI"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nhom", required=True, help="danh sách id nhóm, cách nhau dấu phẩy")
    a = ap.parse_args()
    ids = [int(x) for x in a.nhom.split(",") if x.strip()]
    con = connect()
    ds = [dict(r) for r in con.execute(f"SELECT * FROM groups WHERE id IN ({','.join('?' * len(ids))})", ids)]
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            for g in ds:
                try:
                    kq = roi_mot(page, g)
                except FlowError as e:
                    print(f"DỪNG ở nhóm {g['id']}: {e.code} {e}", flush=True)
                    break
                except Exception as e:  # lỗi lạ ở 1 nhóm → ghi lại, đi tiếp
                    kq = "LOI " + str(e).splitlines()[0][:100]
                con.execute("UPDATE groups SET status=CASE WHEN ?='DA_ROI' THEN 'bo_qua' ELSE status END, notes=COALESCE(notes,'') || ? WHERE id=?",
                            (kq, f" | [ROI_NHOM {now_str()}] {kq}", g["id"]))
                con.commit()
                print(f"nhóm {g['id']:>4} {g['name'][:45]:<45} {kq}", flush=True)
        finally:
            ctx.close()


if __name__ == "__main__":
    main()
