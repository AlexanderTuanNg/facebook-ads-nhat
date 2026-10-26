"""Gửi lời mời kết bạn cho lead chưa nhận được tin mở đầu (nick phụ chạm giới hạn "tin nhắn đang chờ" 26/09 13:02).

Người dùng yêu cầu 26/09: "giờ kết bạn với những người này". Gemini duyệt kế hoạch vòng 3 (26/09): tối đa 5 lời mời/ngày
(26 và 27/09, rồi xem lại), cách 3–5 phút, chỉ chạy trước 17:00, dừng ngay khi có bất kỳ cảnh báo nào, cầu dao 2 lượt hỏng
liền, người đầu chạy riêng + đọc ảnh chụp. Không tự huỷ lời mời. Khi họ đồng ý → gửi tin mở đầu bằng tools/nhan_tin.py.

  python tools/ket_ban.py --leads 4        # 1 người (thử)
  python tools/ket_ban.py                  # tiếp các lead stage 'new' chưa có lời mời, tới đủ hạn mức ngày
"""
import argparse
import random
import re
import time
from datetime import datetime

from common import ROOT, connect, now_str
from fb_group import FlowError, health_check, open_context
from nhan_tin import CHAN, vung_chat

HAN_MUC_NGAY = 5
GIO_CHOT = 17  # không chạy từ 17:00 (tránh sát khung đăng bài buổi tối)
DAU_LOI_MOI = "đã gửi lời mời kết bạn"
# Cảnh báo riêng của kết bạn (hộp "Bạn có biết người này không?" = Facebook nghi mình kết bạn người lạ → dừng, không xác nhận)
CANH_BAO = CHAN + r"|có biết người này|Do you know|dùng tính năng này quá nhanh|không thể gửi lời mời|can't send friend"
NUT_KET_BAN = re.compile(r"^(Kết bạn với |Thêm bạn bè$|Add friend)", re.I)
DA_CO_LOI_MOI = re.compile(r"^(Hủy lời mời|Huỷ lời mời|Đã gửi lời mời|Cancel request|Hủy yêu cầu)", re.I)
LA_BAN_BE = re.compile(r"^(Bạn bè|Friends)$", re.I)


def nut(page, mau):
    """Nút (role=button) đầu tiên đang hiện có nhãn khớp mẫu, trong vùng chính của trang cá nhân."""
    btns = page.locator("div[role='main'] [role='button']")
    for i in range(min(btns.count(), 60)):
        b = btns.nth(i)
        try:
            if not b.is_visible():
                continue
            ten = (b.get_attribute("aria-label") or b.inner_text(timeout=500) or "").strip()
            if mau.search(ten):
                return b
        except Exception:
            pass
    return None


def canh_bao(page):
    """Chữ cảnh báo trong vùng chính hoặc trong hộp thoại đang mở."""
    chu = vung_chat(page)
    dl = page.locator("div[role='dialog']")
    for i in range(dl.count()):
        try:
            if dl.nth(i).is_visible():
                chu += "\n" + dl.nth(i).inner_text(timeout=1000)
        except Exception:
            pass
    m = re.search(CANH_BAO, chu, re.I)
    return m.group(0) if m else None


def ket_ban_mot(page, lead: dict) -> str:
    page.goto(lead["channel_user"], wait_until="domcontentloaded")
    page.wait_for_timeout(random.randint(5000, 7000))
    health_check(page)
    anh = str(ROOT / "data" / f"ket_ban_lead{lead['id']}.png")
    cb = canh_bao(page)
    if cb:
        page.screenshot(path=anh)
        raise FlowError("BI_CHAN", f"Facebook báo: '{cb}'")
    if nut(page, DA_CO_LOI_MOI):
        return "DA_CO_LOI_MOI"
    if nut(page, LA_BAN_BE):
        return "DA_LA_BAN_BE"
    # Chỉ bấm nút của chủ trang ("Kết bạn với <tên ở h1>"); sau khi gửi, Facebook hiện dải "Những người bạn có thể
    # biết" cũng toàn nút "Thêm bạn bè" của người khác (ảnh 26/09 lead 4).
    try:
        ten = page.locator("div[role='main'] h1").first.inner_text(timeout=3000).strip()
    except Exception:
        ten = ""
    b = nut(page, re.compile(rf"^Kết bạn với {re.escape(ten)}$", re.I)) if ten else None
    if b is None:
        b = nut(page, NUT_KET_BAN)  # nút đầu tiên theo thứ tự trang = nút ở phần đầu trang cá nhân
    if b is None:
        page.screenshot(path=anh)
        return "KHONG_CO_NUT_KET_BAN"
    page.wait_for_timeout(random.randint(1500, 3000))
    b.click()
    page.wait_for_timeout(4000)
    cb = canh_bao(page)
    if cb:
        page.screenshot(path=anh)
        page.keyboard.press("Escape")  # không bấm xác nhận
        raise FlowError("BI_CHAN", f"Facebook báo sau khi bấm: '{cb}'")
    page.screenshot(path=anh)
    return "DA_GUI_LOI_MOI" if nut(page, DA_CO_LOI_MOI) else "CHUA_CHAC"


def _khoa_ho_so_url(url: str) -> str:
    """'https://www.facebook.com/abc?x' → 'abc'; '...profile.php?id=123&...' → '123'."""
    m = re.search(r"profile\.php\?id=(\d+)", url)
    if m:
        return m.group(1)
    return url.split("?")[0].rstrip("/").rsplit("/", 1)[-1].lower()


def gui_tin_ban_moi(page, con) -> None:
    """Ai đã đồng ý kết bạn → gửi đúng tin mở đầu đã duyệt (tools/nhan_tin.py). Đọc 1 trang danh sách bạn bè thay vì
    mở từng trang cá nhân (ít thao tác hơn). Tin cho bạn bè không phải 'tin nhắn đang chờ'."""
    from nhan_tin import gui_mot

    cho = [dict(r) for r in con.execute(
        "SELECT * FROM leads WHERE stage='new' AND (notes LIKE ? OR notes LIKE '%kết bạn: DA_LA_BAN_BE%')", (f"%{DAU_LOI_MOI}%",))]
    ban_san = {l["id"] for l in cho if "kết bạn: DA_LA_BAN_BE" in (l["notes"] or "")}
    if not cho:
        print("Không có lead nào đang chờ đồng ý kết bạn.")
        return
    page.goto("https://www.facebook.com/me/friends", wait_until="domcontentloaded")
    page.wait_for_timeout(6000)
    health_check(page)
    ban = set()
    for _ in range(8):
        for a in page.locator("div[role='main'] a[href]").all():
            try:
                ban.add(_khoa_ho_so_url(a.get_attribute("href") or ""))
            except Exception:
                pass
        page.mouse.wheel(0, 2500)
        page.wait_for_timeout(1200)
    moi = [l for l in cho if l["id"] in ban_san or _khoa_ho_so_url(l["channel_user"]) in ban]
    print(f"{datetime.now():%H:%M:%S} {len(moi)}/{len(cho)} lead đã đồng ý kết bạn", flush=True)
    for i, lead in enumerate(moi):
        kq = gui_mot(page, lead, gui=True)  # FlowError (bị chặn/checkpoint) → lan ra ngoài, dừng cả lượt
        print(f"{datetime.now():%H:%M:%S} lead {lead['id']:>2} (bạn mới) {kq}", flush=True)
        if kq.startswith(("DA_GUI", "CHUA_CHAC")):
            con.execute("UPDATE leads SET stage='contacted', notes=COALESCE(notes,'') || ? WHERE id=?",
                        (f" | {now_str()} đồng ý kết bạn → gửi tin mở đầu ({kq})", lead["id"]))
            con.commit()
            if i < len(moi) - 1:
                time.sleep(random.uniform(180, 300))


# Kịch bản §B (người dùng duyệt 26/09) + yêu cầu 05/10 "sau 1 ngày thì remind": 1 tin nhắc duy nhất, chỉ khi CHẮC chưa trả lời.
NHAC = ("NHAC", "Dạ em nhắn lại anh/chị một chút ạ. Anh/chị cần bảng giá hay muốn qua xem đất thì nhắn em, "
                "hoặc gọi 0965 539 599 nhé.")
DUOI_TIN_MO = "trực tiếp nhé?"  # câu cuối chung của A1/A2/A3
UI_CHAT = re.compile(r"^(Trang cá nhân|Tìm kiếm|File phương tiện và file|Quyền riêng tư và hỗ trợ|Chỉ báo trạng thái online"
                     r"|Đang hoạt động|Hoạt động .*trước|Đã xem.*|Đã gửi.*|Bạn đã gửi.*|Enter|\d{1,2}:\d{2}.*|Tin nhắn)$")
GIO_NHAC = 24


def chac_chua_tra_loi(page, ten: str) -> bool | None:
    """True = tin cuối là tin mở đầu của mình; None = không đọc được (mã hoá đầu cuối khoá lịch sử...) → KHÔNG nhắc."""
    from nhan_tin import vung_chat
    body = vung_chat(page)
    i = body.rfind(DUOI_TIN_MO)
    if i < 0:
        return None
    sau = [d.strip() for d in body[i + len(DUOI_TIN_MO):].splitlines() if d.strip()]
    return all(UI_CHAT.match(d) or d == ten for d in sau)


def nhac_lai(page, con) -> None:
    from nhan_tin import dong_hop_pin, gui_mot, link_chat
    rows = [dict(r) for r in con.execute(
        "SELECT * FROM leads WHERE stage='contacted' AND notes LIKE '%gửi tin mở đầu%' AND notes NOT LIKE '%nhắc lại:%'")]
    han = []
    for l in rows:
        moc = re.findall(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})[^|]*gửi tin mở đầu", l["notes"])
        if moc and (datetime.now() - datetime.strptime(moc[-1], "%Y-%m-%d %H:%M:%S")).total_seconds() >= GIO_NHAC * 3600:
            han.append(l)
    print(f"{datetime.now():%H:%M:%S} nhắc lại: {len(han)} lead đã quá {GIO_NHAC} giờ sau tin mở đầu", flush=True)
    for l in han[:10]:
        page.goto(link_chat(l["channel_user"]), wait_until="domcontentloaded")
        page.wait_for_timeout(random.randint(6000, 8000))
        health_check(page)
        dong_hop_pin(page)
        chac = chac_chua_tra_loi(page, l["name"] or "")
        if chac is None:
            kq = "KHONG_RO (không đọc được khung chat, có thể do mã hoá đầu cuối) → không nhắc"
        elif chac is False:
            kq = "CO_TRA_LOI → không nhắc, chờ người dùng trả lời khách"
        else:
            kq = gui_mot(page, l, gui=True, tin_rieng=NHAC)  # FlowError → dừng cả lượt
        print(f"{datetime.now():%H:%M:%S} lead {l['id']:>3} nhắc lại: {kq}", flush=True)
        con.execute("UPDATE leads SET notes=COALESCE(notes,'') || ? WHERE id=?", (f" | {now_str()} nhắc lại: {kq}", l["id"]))
        con.commit()
        time.sleep(random.uniform(120, 240) if str(kq).startswith(("DA_GUI", "CHUA_CHAC")) else random.uniform(10, 20))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leads", help="id lead, vd 4 hoặc 4,5")
    ap.add_argument("--gui-tin-ban-moi", action="store_true", help="chỉ gửi tin mở đầu cho lead đã đồng ý kết bạn")
    a = ap.parse_args()
    if datetime.now().hour >= GIO_CHOT:
        raise SystemExit(f"DỪNG: sau {GIO_CHOT}:00 không chạy kết bạn (kế hoạch đã duyệt)")
    if a.gui_tin_ban_moi:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as pw:
            ctx, page = open_context(pw, "nick_chinh", headless=False)
            try:
                gui_tin_ban_moi(page, connect())
                nhac_lai(page, connect())
            except FlowError as e:
                print(f"{datetime.now():%H:%M:%S} DỪNG NGAY: {e.code} {e}", flush=True)
            finally:
                ctx.close()
        return
    con = connect()
    hom_nay = now_str()[:10]
    da_gui = con.execute("SELECT COUNT(*) FROM leads WHERE notes LIKE ? OR notes LIKE ?",
                         (f"%{hom_nay} __:__:__ {DAU_LOI_MOI} (DA_GUI%", f"%{hom_nay} __:__:__ {DAU_LOI_MOI} (CHUA_CHAC%")).fetchone()[0]
    con_lai = HAN_MUC_NGAY - da_gui
    if con_lai <= 0:
        raise SystemExit(f"DỪNG: hôm nay đã gửi {da_gui}/{HAN_MUC_NGAY} lời mời")
    rows = [dict(r) for r in con.execute(
        "SELECT * FROM leads WHERE stage='new' AND COALESCE(notes,'') NOT LIKE ? AND COALESCE(notes,'') NOT LIKE '%kết bạn: %' "
        "ORDER BY CASE WHEN need LIKE 'bình luận%' THEN 0 WHEN need='thích bài' THEN 1 ELSE 2 END, id DESC", (f"%{DAU_LOI_MOI}%",))]
    if a.leads:
        ids = {int(x) for x in a.leads.split(",") if x.strip()}
        rows = [r for r in rows if r["id"] in ids]
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            hong_lien = 0
            for lead in rows:
                if con_lai <= 0:
                    print(f"Đủ hạn mức {HAN_MUC_NGAY}/ngày."); break
                if datetime.now().hour >= GIO_CHOT or (ROOT / "data" / "stop_batch").exists():
                    print("DỪNG: tới 17:00 hoặc có data/stop_batch"); break
                try:
                    kq = ket_ban_mot(page, lead)
                except FlowError as e:
                    page.screenshot(path=str(ROOT / "data" / f"ket_ban_dung_lead{lead['id']}.png"))
                    print(f"{datetime.now():%H:%M:%S} DỪNG NGAY ở lead {lead['id']}: {e.code} {e}", flush=True); break
                except Exception as e:  # noqa: BLE001 — ghi lại, cầu dao xử lý
                    kq = f"LOI {type(e).__name__}"
                print(f"{datetime.now():%H:%M:%S} lead {lead['id']:>2} {lead['channel_user'][25:60]:<35} {kq}", flush=True)
                if kq in ("DA_GUI_LOI_MOI", "DA_CO_LOI_MOI", "CHUA_CHAC"):
                    con.execute("UPDATE leads SET notes=COALESCE(notes,'') || ? WHERE id=?",
                                (f" | {now_str()} {DAU_LOI_MOI} ({kq})", lead["id"]))
                    con.commit()
                    con_lai -= kq != "DA_CO_LOI_MOI"
                elif kq in ("DA_LA_BAN_BE", "KHONG_CO_NUT_KET_BAN"):
                    con.execute("UPDATE leads SET notes=COALESCE(notes,'') || ? WHERE id=?",
                                (f" | {now_str()} kết bạn: {kq}", lead["id"]))
                    con.commit()
                hong_lien = hong_lien + 1 if kq.startswith(("KHONG", "LOI", "CHUA")) else 0
                if hong_lien >= 2:
                    print(f"DỪNG: 2 lead liền không gửi được — xem data/ket_ban_lead{lead['id']}.png"); break
                if con_lai > 0 and lead is not rows[-1]:
                    time.sleep(random.uniform(180, 300) if kq == "DA_GUI_LOI_MOI" else random.uniform(30, 60))
        finally:
            ctx.close()


if __name__ == "__main__":
    main()
