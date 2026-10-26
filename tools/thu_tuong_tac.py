"""Thu người ĐÃ THÍCH / BÌNH LUẬN bài của nick ở các group → thêm vào bảng leads (CHỈ ĐỌC Facebook, không bấm thích/
bình luận/kết bạn). Sau đó ket_ban.py gửi lời mời kết bạn (5/ngày, ưu tiên người bình luận → người thích → lead cũ),
ai đồng ý thì gửi tin mở đầu, 24 giờ chưa trả lời thì nhắc 1 lần (ket_ban.py --gui-tin-ban-moi).

Người dùng yêu cầu 05/10/2026: "nghiên cứu những người nào like và comment thì kết bạn và nhắn tin, sau 1 ngày thì remind".

  python tools/thu_tuong_tac.py                 # mọi group có bài đã đăng của nick
  python tools/thu_tuong_tac.py --groups 6,7    # vài group
  python tools/thu_tuong_tac.py --khong-ghi     # chỉ in, không ghi DB

Giao diện đo thật 05/10: trang /groups/<fbid>/user/<uid>/ liệt kê bài của nick trong group; nút cảm xúc là phần tử
aria-label "Thích: N người" (bấm chuột vào toạ độ → hộp [role=dialog] liệt kê người, link /groups/<g>/user/<uid>/,
nút cạnh tên: "Nhắn tin" = đã là bạn, "Hủy lời mời" = đã có lời mời, "Theo dõi" = không kết bạn được);
bình luận là [role=article], link đầu là trang cá nhân người bình luận (…/<tên>?comment_id=…).
Giới hạn: bình luận bị thu gọn ("Xem thêm bình luận") chưa mở ra; nguồn bài = bài gần nhất của nick ở group đó.
"""
import argparse
import random
import re
from datetime import datetime

from common import ROOT, connect, now_str
from fb_group import FlowError, health_check, open_context

UID_NICK = "100049236953143"  # David Nguyễn (nick_chinh), đọc từ facebook.com/me ngày 05/10
NHAN_CAM_XUC = re.compile(r"^(Thích|Yêu thích|Thương thương|Haha|Wow|Buồn|Phẫn nộ): \d+ người")
DAU_LOI_MOI = "đã gửi lời mời kết bạn"  # trùng ket_ban.DAU_LOI_MOI: lead có dấu này → chờ đồng ý rồi mới nhắn
UI_BINH_LUAN = re.compile(r"^(Trả lời|Chia sẻ|Thích|Đã chỉnh sửa|Tác giả|·|\d+\s*(phút|giờ|ngày|tuần|năm))$")
KHONG_PHAI_HO_SO = {"groups", "profile.php", "photo", "photo.php", "watch", "hashtag", "share", "permalink.php", "events", "reel"}


def ho_so(href: str) -> str | None:
    """Link trong hộp cảm xúc/bình luận → URL trang cá nhân chuẩn (dạng ket_ban/nhan_tin dùng được)."""
    m = re.search(r"/groups/\d+/user/(\d+)", href) or re.search(r"profile\.php\?id=(\d+)", href)
    if m:
        return f"https://www.facebook.com/profile.php?id={m.group(1)}"
    m = re.match(r"https://www\.facebook\.com/([A-Za-z0-9.]+)/?(\?|$)", href)
    if m and m.group(1) not in KHONG_PHAI_HO_SO:
        return f"https://www.facebook.com/{m.group(1)}"
    return None


def khoa(url: str) -> str:
    m = re.search(r"profile\.php\?id=(\d+)", url)
    return m.group(1) if m else url.split("?")[0].rstrip("/").rsplit("/", 1)[-1].lower()


def doc_hop_cam_xuc(page) -> list[dict]:
    """Hộp đang mở → [{url, ten, trang_thai}]; cuộn trong hộp để tải hết."""
    dlg = page.locator("[role='dialog']").last
    tab = dlg.get_by_role("tab", name=re.compile(r"^Tất cả", re.I))
    try:
        if tab.count():
            tab.first.click(timeout=3000)
            page.wait_for_timeout(1500)
    except Exception:
        pass
    nguoi = {}
    for _ in range(6):
        hang = dlg.evaluate("""d => [...d.querySelectorAll('a[href*="/user/"]')].map(a => {
            let p = a, nut = '';
            for (let i = 0; i < 8 && p; i++) { p = p.parentElement;
              const b = p && p.querySelector('[role="button"]');
              if (b && /Nhắn tin|Hủy lời mời|Huỷ lời mời|Theo dõi|Thêm bạn bè|Kết bạn/.test(b.innerText)) { nut = b.innerText; break } }
            return [a.getAttribute('href'), a.innerText.trim(), nut.trim()] })""")
        for href, ten, nut in hang:
            url = ho_so(href)
            if not url or khoa(url) == UID_NICK:
                continue
            cu = nguoi.get(url, {})
            nguoi[url] = {"url": url, "ten": ten or cu.get("ten", ""), "trang_thai": nut or cu.get("trang_thai", "")}
        bb = dlg.bounding_box()
        if bb:
            page.mouse.move(bb["x"] + bb["width"] / 2, bb["y"] + bb["height"] * 0.6)
            page.mouse.wheel(0, 1200)
            page.wait_for_timeout(1200)
    page.keyboard.press("Escape")
    page.wait_for_timeout(1000)
    return list(nguoi.values())


def doc_binh_luan(page) -> list[dict]:
    ds = []
    for a in page.locator("[role='article']").all():
        try:
            links = a.evaluate("e => [...e.querySelectorAll('a[href]')].map(x => [x.getAttribute('href'), x.innerText.trim()])")
            txt = a.inner_text(timeout=3000)
        except Exception:
            continue
        url = next((ho_so(h) for h, _ in links if ho_so(h)), None)
        if not url or khoa(url) == UID_NICK:
            continue
        ten = next((t for h, t in links if t and ho_so(h) == url), "")
        dong = [d.strip() for d in txt.splitlines() if d.strip() and d.strip() != ten and not UI_BINH_LUAN.match(d.strip())]
        ds.append({"url": url, "ten": ten, "noi_dung": " ".join(dong)[:300]})
    return ds


def doc_group(page, fbid: str) -> tuple[list[dict], list[dict]]:
    page.goto(f"https://www.facebook.com/groups/{fbid}/user/{UID_NICK}/", wait_until="domcontentloaded")
    page.wait_for_timeout(random.randint(5000, 7000))
    health_check(page)
    for _ in range(4):
        page.mouse.wheel(0, 1600)
        page.wait_for_timeout(random.randint(1000, 1600))
    nhan = [n for n in page.evaluate("() => [...document.querySelectorAll('[aria-label]')].map(e => e.getAttribute('aria-label'))")
            if NHAN_CAM_XUC.match(n or "")]
    thich = []
    for ten_nhan in dict.fromkeys(nhan):
        loc = page.locator(f"[aria-label=\"{ten_nhan}\"]")
        for i in range(loc.count()):
            try:
                loc.nth(i).scroll_into_view_if_needed(timeout=5000)
                page.wait_for_timeout(600)
                bb = loc.nth(i).bounding_box()
                page.mouse.click(bb["x"] + bb["width"] / 2, bb["y"] + bb["height"] / 2)  # .click() không mở hộp (đo 05/10)
                page.wait_for_timeout(4000)
                if page.locator("[role='dialog']").count():
                    thich += doc_hop_cam_xuc(page)
            except Exception as e:  # noqa: BLE001 — 1 bài lỗi không bỏ cả group; in ra để biết
                print(f"  ! không mở được hộp cảm xúc '{ten_nhan}' #{i}: {type(e).__name__}", flush=True)
    return thich, doc_binh_luan(page)


def ghi_lead(con, nguoi: dict, loai: str, post_id, group_ten: str, ghi: bool) -> str:
    """'MOI' | 'DA_CO' (đã có trong leads)."""
    co = {khoa(r[0]) for r in con.execute("SELECT channel_user FROM leads WHERE channel_user IS NOT NULL")}
    if khoa(nguoi["url"]) in co:
        return "DA_CO"
    tt = nguoi.get("trang_thai", "")
    ghi_chu = f"{now_str()} thu_tuong_tac: {loai} bài của nick ở '{group_ten[:50]}'"
    if re.search(r"Nhắn tin", tt):
        ghi_chu += " | kết bạn: DA_LA_BAN_BE (hộp cảm xúc hiện nút Nhắn tin)"
    elif re.search(r"Hủy lời mời|Huỷ lời mời", tt):
        ghi_chu += f" | lời mời có sẵn từ trước — {DAU_LOI_MOI} (hộp cảm xúc hiện Hủy lời mời)"
    elif re.search(r"Theo dõi", tt):
        ghi_chu += " | kết bạn: KHONG_CO_NUT_KET_BAN (hộp cảm xúc chỉ có nút Theo dõi)"
    need = f"bình luận: {nguoi['noi_dung']}" if loai == "bình luận" else "thích bài"
    if ghi:
        con.execute("INSERT INTO leads (source_post_id, name, channel_user, need, stage, notes) VALUES (?,?,?,?, 'new', ?)",
                    (post_id, nguoi.get("ten") or None, nguoi["url"], need, ghi_chu))
        con.commit()
    return "MOI"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--groups", help="id group trong DB, vd 6,7")
    ap.add_argument("--khong-ghi", action="store_true")
    a = ap.parse_args()
    con = connect()
    nhom = [dict(r) for r in con.execute(
        "SELECT g.id, g.url, g.name, (SELECT p.id FROM posts p WHERE p.target_id=g.id AND p.status IN ('published','pending_approval') "
        "ORDER BY p.published_at DESC LIMIT 1) AS post_id FROM groups g WHERE EXISTS (SELECT 1 FROM posts p WHERE p.target_id=g.id "
        "AND p.channel='group' AND p.status IN ('published','pending_approval')) ORDER BY g.id")]
    if a.groups:
        chon = {int(x) for x in a.groups.split(",")}
        nhom = [g for g in nhom if g["id"] in chon]
    from playwright.sync_api import sync_playwright

    tong = {"MOI": 0, "DA_CO": 0}
    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            for g in nhom:
                if (ROOT / "data" / "stop_batch").exists():
                    print("DỪNG: có data/stop_batch")
                    break
                fbid = g["url"].rstrip("/").split("/")[-1]
                try:
                    thich, bl = doc_group(page, fbid)
                except FlowError:
                    raise
                except Exception as e:  # noqa: BLE001
                    print(f"{datetime.now():%H:%M:%S} g{g['id']} LỖI {type(e).__name__}: {str(e)[:120]}", flush=True)
                    if page.is_closed() or "crashed" in str(e).lower():  # trang sập (đo 05/10) → mở trang mới, đi tiếp
                        try:
                            page.close()
                        except Exception:
                            pass
                        page = ctx.new_page()
                    continue
                kq = [("bình luận", n, ghi_lead(con, n, "bình luận", g["post_id"], g["name"], not a.khong_ghi)) for n in bl]
                kq += [("thích", n, ghi_lead(con, n, "thích", g["post_id"], g["name"], not a.khong_ghi)) for n in thich]
                for _, _, k in kq:
                    tong[k] += 1
                if kq:
                    print(f"{datetime.now():%H:%M:%S} g{g['id']:<4} {len(thich)} thích, {len(bl)} bình luận → " + ", ".join(
                        f"{n['ten'] or n['url'][25:]} ({loai}{', ' + n['trang_thai'] if n.get('trang_thai') else ''})"
                        f"{' MỚI' if k == 'MOI' else ''}" for loai, n, k in kq), flush=True)
                try:
                    page.wait_for_timeout(random.randint(3000, 6000))
                except Exception:
                    page = ctx.new_page()
        except FlowError as e:
            print(f"{datetime.now():%H:%M:%S} DỪNG NGAY: {e.code} {e}", flush=True)
        finally:
            ctx.close()
    print(f"XONG thu tương tác: {tong['MOI']} lead mới, {tong['DA_CO']} người đã có trong leads"
          + (" (chạy không ghi)" if a.khong_ghi else ""))


if __name__ == "__main__":
    main()
