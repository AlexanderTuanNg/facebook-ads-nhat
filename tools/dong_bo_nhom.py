"""Đồng bộ danh sách nhóm nick đã vào (trang "Nhóm của bạn") vào bảng groups.

  python tools/dong_bo_nhom.py          # chỉ in: nhóm nick đã vào mà DB chưa ghi 'joined'
  python tools/dong_bo_nhom.py --ghi    # ghi: thêm nhóm mới / chuyển candidate|requested → joined

Người dùng 06/10: "mình vào nhiều group lắm mà, test thử những group khác nhiều lên" — DB chỉ biết 61 nhóm 'joined'
(nhóm người dùng tự vào tay không được ghi). Nhóm 'bo_qua' / 'cho_tra_loi' giữ nguyên (đã có lý do bỏ).
Nhóm mới ghi warmup_until = lúc đồng bộ (đã vào từ trước, không biết ngày → không bắt làm quen thêm).
Hồ sơ trình duyệt đi qua khoá chung (open_context) → lịch đăng bài đang chạy sẽ tự chờ.
"""
import argparse
import re

from common import connect, now_str
from fb_group import FlowError, health_check, open_context

URL = "https://www.facebook.com/groups/joins/?nav_source=tab"


def doc_nhom(page) -> dict:
    """{id_hoặc_slug: tên} của mọi nhóm trong danh sách, cuộn tới khi không thêm được nữa."""
    page.goto(URL, wait_until="domcontentloaded")
    page.wait_for_timeout(5000)
    health_check(page)
    thay, dung_yen = {}, 0
    while dung_yen < 4:
        truoc = len(thay)
        for a in page.locator("div[role='main'] a[href*='/groups/']").all():
            try:
                href = a.get_attribute("href") or ""
                m = re.search(r"/groups/([^/?#]+)/?(?:[?#]|$)", href)
                ten = (a.inner_text(timeout=300) or "").strip().split("\n")[0]
            except Exception:
                continue
            if m and ten and m.group(1) not in ("joins", "feed", "discover", "create") and not ten.startswith("Xem nhóm"):
                thay.setdefault(m.group(1), ten)
        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(1800)
        dung_yen = dung_yen + 1 if len(thay) == truoc else 0
    return thay


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ghi", action="store_true")
    ap.add_argument("--account", default="nick_chinh")
    a = ap.parse_args()
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        ctx, page = open_context(pw, a.account, headless=False)
        try:
            thay = doc_nhom(page)
        except FlowError as e:
            print(e.code, e)
            return
        finally:
            ctx.close()
    con = connect()
    db = {}
    for r in con.execute("SELECT id, url, name, status FROM groups"):
        m = re.search(r"/groups/([^/?#]+)", r["url"] or "")
        if m:
            db[m.group(1)] = dict(r)
    moi, chuyen = [], []
    for k, ten in thay.items():
        g = db.get(k)
        if g is None:
            moi.append((k, ten))
        elif g["status"] in ("candidate", "requested"):
            chuyen.append((g["id"], g["status"], ten))
    print(f"Trang 'Nhóm của bạn': {len(thay)} nhóm · DB chưa có: {len(moi)} · DB có nhưng chưa 'joined': {len(chuyen)}")
    for k, ten in moi:
        print(f"  MỚI  {k}  {ten}")
    for gid, st, ten in chuyen:
        print(f"  g{gid} {st} → joined  {ten}")
    if not a.ghi:
        print("(chạy khô — thêm --ghi để ghi DB)")
        return
    t = now_str()
    for k, ten in moi:
        con.execute("INSERT INTO groups (url, name, status, joined_at, warmup_until, notes) VALUES (?,?,?,?,?,?)",
                    (f"https://www.facebook.com/groups/{k}", ten, "joined", t, t, f"[DONG_BO {t[:16]}] có trong 'Nhóm của bạn'"))
    for gid, st, ten in chuyen:
        con.execute("UPDATE groups SET status='joined', joined_at=COALESCE(joined_at, ?), warmup_until=?, "
                    "notes=COALESCE(notes,'') || ? WHERE id=?", (t, t, f" | [DONG_BO {t[:16]}] {st} → joined", gid))
    con.commit()
    print(f"ĐÃ GHI: +{len(moi)} nhóm mới, {len(chuyen)} nhóm chuyển joined")


if __name__ == "__main__":
    main()
