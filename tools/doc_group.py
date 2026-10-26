"""Đọc bảng tin group Facebook (CHỈ ĐỌC, không bấm thích/bình luận/đăng) để phân tích bài nào được tương tác nhiều.

  python tools/doc_group.py --groups 1,5,6 --scrolls 8
  python tools/doc_group.py --all

Kết quả: data/doc_group_<ngày>.jsonl (mỗi dòng 1 bài) + bảng top bài theo điểm tương tác in ra màn hình.
Dùng hồ sơ trình duyệt nick_chinh: KHÔNG chạy cùng lúc với lệnh đăng bài (prefill/autopost/stats).
"""
import argparse
import json
import random
import re
import time
from datetime import datetime

from common import ROOT, connect
from fb_group import FlowError, health_check, open_context

SO = r"(\d+(?:[.,]\d+)?)\s*([KkNn]|nghìn|triệu)?"


def so(txt: str | None) -> int:
    """'12' → 12, '1,2K' / '1,2 N' / '1,2 nghìn' → 1200."""
    if not txt:
        return 0
    m = re.match(SO, txt.strip())
    if not m:
        return 0
    v = float(m.group(1).replace(",", "."))
    if m.group(2):
        v *= 1_000_000 if m.group(2) == "triệu" else 1000
    return int(v)


def phan_tich(raw: str) -> dict:
    t = raw.replace("\xa0", " ")
    cx = re.search(r"Tất cả cảm xúc:\s*\n?\s*" + SO, t)
    bl = re.search(SO + r"\s*bình luận", t)
    cs = re.search(SO + r"\s*lượt chia sẻ", t)
    # Trên bảng tin group, số cảm xúc thường hiện thành một dòng chỉ có con số (vd "2") → lấy số lớn nhất như vậy (≤ 9999)
    le = [int(x) for x in re.findall(r"(?m)^\s*(\d{1,4})\s*$", t)]
    return {
        "reactions": so(cx.group(0).split(":", 1)[1]) if cx else (max(le) if le else 0),
        "comments": so(bl.group(0)) if bl else 0,
        "shares": so(cs.group(0)) if cs else 0,
        "co_gia": bool(re.search(r"\d[\d.,]*\s*(tỷ|tỉ|triệu|tr\b)", t, re.I)),
    }


def doc_group(page, g: dict, scrolls: int) -> list[dict]:
    page.goto(g["url"], wait_until="domcontentloaded")
    page.wait_for_timeout(random.randint(4000, 6000))
    health_check(page)
    # Facebook chỉ vẽ nội dung các bài gần màn hình (bài đã lướt qua bị xoá trắng) → đọc dần trong lúc lướt,
    # mỗi bài nhận diện bằng số thứ tự aria-posinset.
    posts, seen = [], set()
    for _ in range(scrolls * 2):
        arts = page.locator("[aria-posinset]")
        for i in range(arts.count()):
            el = arts.nth(i)
            try:
                key = el.get_attribute("aria-posinset", timeout=1000)
                if key in seen:
                    continue
                raw = el.inner_text(timeout=2000)
            except Exception:
                continue
            if len(raw) < 40:
                continue
            seen.add(key)
            posts.append(_bai(el, raw, g))
        page.mouse.wheel(0, random.randint(800, 1100))
        page.wait_for_timeout(random.randint(1500, 2600))
    return posts


def _bai(el, raw: str, g: dict) -> dict:
    """Một bài trong bảng tin → số liệu tương tác + nội dung rút gọn."""
    info = phan_tich(raw)
    try:
        info["co_video"] = el.locator("video").count() > 0
        info["so_anh"] = el.locator("img[src*='scontent']").count()
        msg = el.locator("div[data-ad-preview='message'], div[data-ad-comet-preview='message']")
        noi_dung = msg.first.inner_text(timeout=1000) if msg.count() else ""
    except Exception:
        info["co_video"], info["so_anh"], noi_dung = False, 0, ""
    dong = [d.strip() for d in raw.split("\n") if d.strip()]
    info.update({"group_id": g["id"], "group": g["name"], "tac_gia": dong[0] if dong else "",
                 "noi_dung": (noi_dung or " ".join(dong[1:]))[:600], "raw": raw[:1500]})
    info["diem"] = info["reactions"] + 2 * info["comments"] + 3 * info["shares"]
    return info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", help="danh sách id group, vd 1,5,6")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--scrolls", type=int, default=8)
    a = ap.parse_args()
    con = connect()
    q = "SELECT id, name, url FROM groups WHERE status='joined'"
    rows = [dict(r) for r in con.execute(q)]
    if not a.all:
        ids = {int(x) for x in (a.groups or "").split(",") if x.strip()}
        rows = [r for r in rows if r["id"] in ids]
    out = ROOT / "data" / f"doc_group_{datetime.now():%Y%m%d_%H%M}.jsonl"
    from playwright.sync_api import sync_playwright

    tat_ca = []
    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            for g in rows:
                try:
                    posts = doc_group(page, g, a.scrolls)
                except FlowError as e:
                    print(f"DỪNG: {e.code} ở group {g['id']}")
                    break
                except Exception as e:  # noqa: BLE001 — một group lỗi thì ghi lại, đọc group khác
                    print(f"LỖI group {g['id']} {g['name']}: {e}")
                    continue
                tat_ca += posts
                print(f"group {g['id']:>2} {g['name'][:34]:<34} đọc {len(posts)} bài")
                time.sleep(random.uniform(3, 7))
        finally:
            ctx.close()
    with out.open("w", encoding="utf-8") as f:
        for p in tat_ca:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f"\nĐã lưu {len(tat_ca)} bài → {out}")
    for p in sorted(tat_ca, key=lambda x: -x["diem"])[:25]:
        print(f"{p['diem']:>5} | ❤{p['reactions']:>4} 💬{p['comments']:>4} ↗{p['shares']:>3} | "
              f"{'VIDEO' if p['co_video'] else str(p['so_anh']) + ' ảnh':<7} | {'giá' if p['co_gia'] else '    '} | "
              f"g{p['group_id']:<2} | {p['noi_dung'][:90]}")


if __name__ == "__main__":
    main()
