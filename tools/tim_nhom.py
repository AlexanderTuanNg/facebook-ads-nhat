"""Tìm group Facebook quanh Yên Thế (chỉ đọc trang kết quả tìm kiếm, không bấm Tham gia).

  python tools/tim_nhom.py --tu-khoa "Bố Hạ,Cầu Gồ,Tân Yên"
  python tools/tim_nhom.py                      # danh sách từ khoá mặc định (các xã/thị trấn quanh Yên Thế)

Mỗi từ khoá: mở facebook.com/search/groups/?q=…, lướt vài lần, lấy tên nhóm + link + dòng mô tả ("Công khai · 13K thành viên ·
10+ bài viết/ngày"). Ghi data/tim_nhom_<giờ>.jsonl; in bảng, đánh dấu nhóm đã có trong DB. Người dùng 28/09: "nghiên cứu đăng
tại các group xung quanh yên thế nữa".
"""
import argparse
import json
import re
import time
from datetime import datetime
from urllib.parse import quote

from common import ROOT, connect
from fb_group import FlowError, health_check, open_context

MAC_DINH = ["Yên Thế", "Bố Hạ", "Cầu Gồ", "Phồn Xương", "Đồng Kỳ", "Tam Tiến", "Xuân Lương", "Canh Nậu", "Đồng Vương",
            "Tân Yên", "Nhã Nam", "Cao Thượng", "Lạng Giang", "Kép Lạng Giang", "Lục Nam", "Việt Yên"]


def so_tv(chu: str) -> int | None:
    m = re.search(r"([\d.,]+)\s*([KkNnTr]*)\s*(?:thành viên|members)", chu)
    if not m:
        return None
    so = float(m.group(1).replace(".", "").replace(",", ".")) if m.group(2) else float(m.group(1).replace(".", "").replace(",", ""))
    return int(so * (1000 if m.group(2).lower() in ("k", "n") else 1_000_000 if m.group(2).lower() == "tr" else 1))


def tim(page, kw: str) -> list[dict]:
    page.goto(f"https://www.facebook.com/search/groups/?q={quote(kw)}", wait_until="domcontentloaded")
    page.wait_for_timeout(6000)
    health_check(page)
    kq = {}
    for _ in range(4):
        for a in page.locator("div[role='main'] a[href*='/groups/']").all():
            try:
                href = (a.get_attribute("href") or "").split("?")[0].rstrip("/")
                if not re.search(r"facebook\.com/groups/[^/]+$", href) or href in kq:
                    continue
                ten = a.inner_text(timeout=300).strip().split("\n")[0]
                if len(ten) < 3:
                    continue
                the = a.locator("xpath=ancestor::div[contains(., 'thành viên') or contains(., 'members')][1]")
                mo_ta = the.first.inner_text(timeout=500).replace("\n", " · ") if the.count() else ""
                kq[href] = {"tu_khoa": kw, "ten": ten, "url": href, "mo_ta": mo_ta[:220], "thanh_vien": so_tv(mo_ta),
                            "cong_khai": "Công khai" in mo_ta or "Public" in mo_ta,
                            "bai_ngay": (re.search(r"(\d+\+?)\s*bài viết", mo_ta) or [None, None])[1]}
            except Exception:
                pass
        page.mouse.wheel(0, 2500)
        page.wait_for_timeout(1500)
    return list(kq.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tu-khoa")
    a = ap.parse_args()
    tu_khoa = [k.strip() for k in (a.tu_khoa.split(",") if a.tu_khoa else MAC_DINH) if k.strip()]
    co = {r[0].rstrip("/") for r in connect().execute("SELECT url FROM groups")}
    ra = ROOT / "data" / f"tim_nhom_{datetime.now():%Y%m%d_%H%M}.jsonl"
    from playwright.sync_api import sync_playwright

    tong = {}
    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            for kw in tu_khoa:
                try:
                    ds = tim(page, kw)
                except FlowError as e:
                    print(f"DỪNG: {e.code} {e}"); break
                for g in ds:
                    tong.setdefault(g["url"], g)
                print(f"{datetime.now():%H:%M:%S} '{kw}': {len(ds)} nhóm", flush=True)
                time.sleep(4)
        finally:
            ctx.close()
    with open(ra, "w", encoding="utf-8") as fh:
        for g in tong.values():
            g["da_co_trong_db"] = g["url"] in co
            fh.write(json.dumps(g, ensure_ascii=False) + "\n")
    print(f"→ {ra.name}: {len(tong)} nhóm ({sum(g['da_co_trong_db'] for g in tong.values())} đã có trong DB)")


if __name__ == "__main__":
    main()
