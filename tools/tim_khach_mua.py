"""Quét bảng tin các group địa phương ĐÃ VÀO, lọc người ĐANG TÌM MUA đất (và người đăng bán, để tìm môi giới) —
CHỈ ĐỌC, không bấm thích/bình luận/nhắn (người dùng 11/10/2026: "scout data người mua bán quanh khu vực trong các nhóm đã vào").

  python tools/tim_khach_mua.py                    # tối đa 20 group địa phương, mỗi group lướt 6 lần
  python tools/tim_khach_mua.py --groups 5,6 --scrolls 4

An toàn: ≤ 20 group/lần; tự dừng trước giờ đăng bài kế tiếp 10 phút (không giành hồ sơ trình duyệt của lịch đăng);
chỉ lưu link bài + nội dung công khai (Luật Bảo vệ dữ liệu cá nhân 91/2025 + NĐ 356/2025 thay NĐ 13 từ 01/01/2026: không lập hồ sơ, không chép số để gọi/nhắn; chỉ trả lời công khai dưới bài họ đăng — cần luật sư xác nhận).
Kết quả: data/tim_khach_<ngày_giờ>.jsonl + bảng in ra. KHÔNG tự ghi vào bảng leads — người dùng/Claude xem rồi mới liên hệ.
"""
import argparse
import json
import random
import re
import time
import unicodedata
from datetime import datetime, timedelta

from common import ROOT, connect
from fb_group import FlowError, health_check, open_context

VUNG = ("yen the", "bo ha", "nha nam", "tan yen", "dong lac", "xuan luong", "dong ky", "tam tien", "cao thuong",
        "phon xuong", "cau go")  # 11/10: bỏ "bac giang" (kéo cả nhóm BĐS toàn tỉnh như Việt Yên)
MUA = r"cần mua|can mua|tìm mua|muốn mua|mua (?:đất|nhà|lô|mảnh)|cần tìm (?:đất|nhà|lô|mảnh)|tìm (?:đất|lô|mảnh)|ai (?:có|bán) (?:đất|lô|mảnh|nhà)|có ai bán|cần (?:đất|lô|mảnh)|hỏi mua|ngân sách|tài chính (?:tầm|khoảng|có)"
BAN = r"cần bán|can ban|bán (?:đất|nhà|lô|mảnh)|chính chủ bán|chính chủ cần bán|nhượng lại|bán gấp|hạ giá"
DAT = r"đất|lô|thổ cư|m2|m²|mét|sổ|nhà"


def bo_dau(s: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFD", s or "") if unicodedata.category(ch) != "Mn").replace("đ", "d").lower()


# 25/10 người dùng: dự án phụ cho thuê toà nhà (đăng bằng nick này) → bắt người CẦN THUÊ nhà nguyên căn / văn phòng / mặt bằng / toà nhà
THUE = r"cần thuê|can thue|tìm thuê|muốn thuê|đang tìm (?:mặt bằng|văn phòng|nhà nguyên căn)|thuê (?:mặt bằng|văn phòng|nhà nguyên căn|tòa nhà|toà nhà|nhà mặt|kho|xưởng)"
CHO_THUE = r"cho thuê|cần cho thuê|chính chủ cho thuê"
CHO_O = r"mặt bằng|văn phòng|nhà nguyên căn|tòa nhà|toà nhà|nhà mặt (?:đường|phố|tiền)|kinh doanh|m2|m²|tầng|sàn"


def phan_loai(t: str) -> str | None:
    t = t.lower()
    if re.search(THUE, t) and re.search(CHO_O, t) and not re.search(CHO_THUE, t):
        return "thue"
    if re.search(MUA, t) and re.search(DAT, t):
        return "mua"
    if re.search(BAN, t) and re.search(DAT, t):
        return "ban"
    return None


def moc_dung(con) -> datetime:
    """10 phút trước bài đã duyệt kế tiếp hôm nay (không có bài → hết ngày)."""
    now = datetime.now()
    fmt = "%Y-%m-%d %H:%M:%S"
    # Bài đã tới giờ (≤ 60 phút trước) mà chưa đăng xong → lịch sắp/đang dùng trình duyệt → dừng ngay.
    # (11/10 lần đầu: mốc tính cả bài đã quá giờ → tưởng "sắp tới giờ", dừng khi chưa quét được nhóm nào.)
    dang = con.execute("SELECT 1 FROM posts WHERE status='approved_human' AND channel='group' AND scheduled_at BETWEEN ? AND ?",
                       ((now - timedelta(minutes=60)).strftime(fmt), now.strftime(fmt))).fetchone()
    if dang:
        return now
    r = con.execute("SELECT min(scheduled_at) FROM posts WHERE status='approved_human' AND channel='group' AND scheduled_at>?",
                    (now.strftime(fmt),)).fetchone()[0]
    return datetime.strptime(r[:16], "%Y-%m-%d %H:%M") - timedelta(minutes=10) if r else now + timedelta(hours=6)


def quet(page, g: dict, scrolls: int, het: datetime) -> list[dict]:
    page.goto(g["url"], wait_until="domcontentloaded")
    page.wait_for_timeout(random.randint(4000, 6000))
    health_check(page)
    ra, seen = [], set()
    for _ in range(scrolls * 2):
        if datetime.now() >= het:
            break
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
            seen.add(key)
            loai = phan_loai(raw)
            if not loai:
                continue
            try:
                a = el.locator("a[href*='/posts/'], a[href*='/permalink/'], a[href*='story_fbid']").first
                link = (a.get_attribute("href", timeout=1000) or "").split("?")[0]
            except Exception:
                link = ""
            # Facebook chèn chữ "Facebook" ẩn lặp lại để chống đọc máy → lấy khung nội dung bài, bỏ chữ ẩn đó
            try:
                msg = el.locator("div[data-ad-preview='message'], div[data-ad-comet-preview='message']")
                noi_dung = msg.first.inner_text(timeout=1000) if msg.count() else ""
            except Exception:
                noi_dung = ""
            dong = [d.strip() for d in raw.split("\n") if d.strip() and d.strip() != "Facebook"]
            noi_dung = re.sub(r"(Facebook\s*)+", " ", noi_dung or " ".join(dong[1:])).strip()
            ra.append({"group_id": g["id"], "group": g["name"], "tac_gia": dong[0] if dong else "", "loai": loai,
                       "noi_dung": noi_dung[:500], "link": link, "doc_luc": f"{datetime.now():%Y-%m-%d %H:%M}"})
        page.mouse.wheel(0, random.randint(800, 1100))
        page.wait_for_timeout(random.randint(1500, 2600))
    return ra


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", help="id group, vd 5,6 (mặc định: group địa phương đã vào, nhiều thành viên trước)")
    ap.add_argument("--so", type=int, default=20)
    ap.add_argument("--scrolls", type=int, default=6)
    a = ap.parse_args()
    con = connect()
    rows = [dict(r) for r in con.execute("SELECT id, name, url, members FROM groups WHERE status='joined' AND url IS NOT NULL "
                                         "ORDER BY COALESCE(members,0) DESC")]
    if a.groups:
        ids = {int(x) for x in a.groups.split(",") if x.strip()}
        rows = [r for r in rows if r["id"] in ids]
    else:
        rows = [r for r in rows if any(v in bo_dau(r["name"]) for v in VUNG)]
    rows = rows[:min(a.so, 20)]
    het = moc_dung(con)
    print(f"Quét {len(rows)} group, dừng muộn nhất {het:%H:%M}")
    out = ROOT / "data" / f"tim_khach_{datetime.now():%Y%m%d_%H%M}.jsonl"
    from playwright.sync_api import sync_playwright

    tat_ca = []
    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            for g in rows:
                if datetime.now() >= het:
                    print(f"DỪNG {datetime.now():%H:%M}: sắp tới giờ đăng bài"); break
                try:
                    kq = quet(page, g, a.scrolls, het)
                except FlowError as e:
                    print(f"DỪNG: {e.code} ở group {g['id']}"); break
                except Exception as e:  # noqa: BLE001 — một group lỗi thì sang group khác
                    print(f"LỖI group {g['id']} {g['name'][:30]}: {type(e).__name__}"); continue
                tat_ca += kq
                print(f"g{g['id']:<4} {g['name'][:36]:<36} mua {sum(x['loai']=='mua' for x in kq)} · bán {sum(x['loai']=='ban' for x in kq)}", flush=True)
                time.sleep(random.uniform(3, 7))
        finally:
            ctx.close()
    with out.open("w", encoding="utf-8") as f:
        for x in tat_ca:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print(f"\nĐã lưu {len(tat_ca)} bài → {out}")
    for x in sorted(tat_ca, key=lambda x: x["loai"] != "mua"):
        print(f"[{x['loai'].upper()}] g{x['group_id']} | {x['noi_dung'][:110]} | {x['link'][:70]}")


if __name__ == "__main__":
    main()
