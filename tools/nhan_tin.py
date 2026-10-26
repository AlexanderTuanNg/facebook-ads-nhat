"""Gửi TIN MỞ ĐẦU đã được người dùng duyệt cho lead (Messenger, nick đang đăng nhập).

  python tools/nhan_tin.py --leads 1            # gửi cho 1 lead (thử)
  python tools/nhan_tin.py --tat-ca             # gửi cho mọi lead stage 'new', cách 3–5 phút/tin
  python tools/nhan_tin.py --leads 1 --khong-gui  # chỉ điền sẵn + chụp màn hình, KHÔNG bấm gửi

Chỉ gửi đúng 3 mẫu A1/A2/A3 trong workspace/kich-ban-nhan-tin-lead.md (người dùng duyệt 26/09, chọn "Claude tự gửi
tin mở đầu"). KHÔNG tự trả lời khách: câu trả lời tiếp theo do người dùng duyệt từng tin.
Dừng ngay khi Facebook báo chặn/gửi quá nhanh/checkpoint. Dùng hồ sơ nick_chinh: không chạy cùng lúc lệnh trình duyệt khác.
"""
import argparse
import random
import re
import sys
import time
from datetime import datetime

from common import ROOT, connect, now_str
from db import lint_text
from fb_group import FlowError, health_check, open_context

# Bản 2 — người dùng duyệt 26/09 ~13:00 ("Gửi bản mới"), thêm ý khách quan tâm: pháp lý (câu chuẩn F5),
# "vẫn có khách giao dịch đều", "chủ đầu tư đưa đi xem trực tiếp".
A1 = ("Dạ em chào anh/chị ạ. Em bên chủ đầu tư dự án Yên Thế Golden Hill ở trung tâm xã Yên Thế, TP Bắc Ninh (Đồng Lạc cũ). "
      "Thấy anh/chị có quan tâm đất bên em nên em nhắn hỏi thăm ạ.\n"
      "Dự án đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô, hiện vẫn có khách giao dịch đều. "
      "Có lô chỉ khoảng 1 tỷ, mua trực tiếp chủ đầu tư được chiết khấu đến 10% theo chính sách chủ đầu tư.\n"
      "Anh/chị cho em xin số điện thoại hoặc Zalo, em gửi bảng giá và bên chủ đầu tư đưa anh/chị đi xem đất trực tiếp nhé?")
A2 = ("Dạ em chào anh/chị ạ. Em bên chủ đầu tư dự án Yên Thế Golden Hill (Đồng Lạc cũ, xã Yên Thế, TP Bắc Ninh). "
      "Anh/chị quan tâm pháp lý nên em nói luôn: dự án đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô, "
      "hiện vẫn có khách giao dịch đều.\n"
      "Anh/chị cho em xin số điện thoại hoặc Zalo, em gửi thông tin pháp lý, bảng giá và bên chủ đầu tư đưa anh/chị đi xem đất, "
      "xem hồ sơ trực tiếp nhé?")
A3 = ("Dạ em chào anh/chị ạ. Em bên chủ đầu tư dự án Yên Thế Golden Hill (Đồng Lạc cũ, xã Yên Thế, TP Bắc Ninh). "
      "Anh/chị quan tâm giá nên em báo luôn: có lô chỉ khoảng 1 tỷ, mỗi lô giá khác nhau theo vị trí và diện tích (82–185 m²), "
      "mua trực tiếp chủ đầu tư được chiết khấu đến 10% theo chính sách chủ đầu tư. "
      "Dự án đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô.\n"
      "Anh/chị cho em xin số Zalo, em gửi bảng giá chi tiết từng lô và bên chủ đầu tư đưa anh/chị đi xem đất trực tiếp nhé?")
# Câu thật gặp 26/09 13:02 (sau 3 tin cho người chưa kết bạn): "Bạn đã đạt giới hạn về số tin nhắn đang chờ —
# Số yêu cầu bạn có thể gửi trong 24 giờ là có giới hạn." → hiện thay cho ô gõ.
CHAN = (r"tạm thời bị chặn|quá nhanh|không được gửi|Không thể gửi|bị hạn chế|hạn chế bạn|giới hạn gửi|gửi quá nhiều"
        r"|đạt giới hạn|Số yêu cầu bạn có thể gửi"
        r"|temporarily blocked|going too fast|couldn't send|can't send|reached the limit")
KHONG_NHAN = r"không thể nhắn tin|không nhận tin nhắn|can't message|không khả dụng"


def vung_chat(page) -> str:
    """Chữ của khung hội thoại đang mở (không lấy danh sách chat bên trái để khỏi nhầm với tin cũ)."""
    try:
        main = page.locator("div[role='main']")
        if main.count():
            return main.last.inner_text(timeout=3000)
    except Exception:
        pass
    return page.inner_text("body")


def mau_cho(need: str) -> tuple[str, str]:
    if "pháp lý" in need or "sổ" in need:
        return "A2", A2
    if "giá" in need:
        return "A3", A3
    return "A1", A1


def link_chat(url: str) -> str:
    m = re.search(r"profile\.php\?id=(\d+)", url)
    ten = m.group(1) if m else url.rstrip("/").rsplit("/", 1)[-1]
    return f"https://www.facebook.com/messages/t/{ten}"


def o_nhap(page):
    for sel in ["div[role='main'] div[role='textbox'][contenteditable='true']",
                "div[role='textbox'][aria-label*='Tin nhắn']", "div[role='textbox'][aria-label*='Message']",
                "div[role='textbox'][contenteditable='true']"]:
        loc = page.locator(sel)
        try:
            if loc.count() and loc.last.is_visible():
                return loc.last
        except Exception:
            pass
    return None


def dong_hop_pin(page) -> None:
    """Hộp 'Nhập mã PIN để khôi phục đoạn chat' (mã hoá đầu cuối): chỉ bấm ×. KHÔNG nhập/tạo PIN (việc của người dùng)."""
    for i in range(page.locator("div[role='dialog']").count()):
        d = page.locator("div[role='dialog']").nth(i)
        try:
            if d.is_visible() and "mã PIN" in d.inner_text(timeout=1000):
                d.locator("[aria-label='Đóng'], [aria-label='Close']").first.click(timeout=3000)
                page.wait_for_timeout(1500)
        except Exception:
            pass


def cho_o_nhap(page, giay: int = 25):
    """Chat với người chưa từng nhắn: Messenger hiện thông báo mã hoá đầu cuối + nút 'Tiếp tục' (bấm → khung soạn
    tin mới, kiểm 26/09) và có lúc hộp PIN khôi phục lịch sử (chỉ bấm ×)."""
    for _ in range(giay):
        m = re.search(CHAN, vung_chat(page), re.I)
        if m:  # cảnh báo có thể hiện muộn, sau khi trang tải xong
            raise FlowError("BI_CHAN", f"Facebook báo: '{m.group(0)}'")
        dong_hop_pin(page)
        box = o_nhap(page)
        if box is not None:
            return box
        nut = page.get_by_role("button", name="Tiếp tục")
        try:
            if nut.count() and nut.first.is_visible():
                nut.first.click(timeout=3000)
                page.wait_for_timeout(2500)
                continue
        except Exception:
            pass
        page.wait_for_timeout(1000)
    return None


def gui_mot(page, lead: dict, gui: bool, tin_rieng: tuple[str, str] | None = None) -> str:
    ma, tin = tin_rieng or mau_cho(lead["need"] or "")
    page.goto(link_chat(lead["channel_user"]), wait_until="domcontentloaded")
    page.wait_for_timeout(random.randint(5000, 8000))
    health_check(page)
    body = vung_chat(page)
    m = re.search(CHAN, body, re.I)
    if m:
        page.screenshot(path=str(ROOT / "data" / f"nhan_tin_lead{lead['id']}_chan.png"))
        raise FlowError("BI_CHAN", f"Facebook báo: '{m.group(0)}'")
    box = cho_o_nhap(page)
    if box is None:
        page.screenshot(path=str(ROOT / "data" / f"nhan_tin_lead{lead['id']}.png"))
        return "KHONG_NHAN_DUOC" if re.search(KHONG_NHAN, body, re.I) else "KHONG_THAY_O_NHAP"
    box.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Delete")
    for i, dong in enumerate(tin.split("\n")):
        if i:
            page.keyboard.press("Shift+Enter")
        page.keyboard.insert_text(dong)
        page.wait_for_timeout(random.randint(400, 900))
    if not gui:
        page.screenshot(path=str(ROOT / "data" / f"nhan_tin_lead{lead['id']}_dien_san.png"))
        box.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Delete")  # thử xong thì xoá chữ, không để lại bản nháp
        return f"DIEN_SAN_{ma}"
    page.wait_for_timeout(random.randint(1500, 3000))
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    body2 = vung_chat(page)
    m = re.search(CHAN, body2, re.I)
    if m:
        page.screenshot(path=str(ROOT / "data" / f"nhan_tin_lead{lead['id']}_chan.png"))
        raise FlowError("BI_CHAN", f"Facebook báo sau khi gửi: '{m.group(0)}'")
    da_gui = (tin.splitlines()[-1][-25:] in body2) and (box.inner_text(timeout=2000).strip() == "")
    page.screenshot(path=str(ROOT / "data" / f"nhan_tin_lead{lead['id']}.png"))
    return f"DA_GUI_{ma}" if da_gui else f"CHUA_CHAC_{ma}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leads", help="id lead, vd 1,2,3")
    ap.add_argument("--tat-ca", action="store_true")
    ap.add_argument("--khong-gui", action="store_true")
    a = ap.parse_args()
    for t in (A1, A2, A3):
        assert not lint_text(t), lint_text(t)
    con = connect()
    rows = [dict(r) for r in con.execute("SELECT * FROM leads WHERE stage='new' ORDER BY id")]
    if not a.tat_ca:
        ids = {int(x) for x in (a.leads or "").split(",") if x.strip()}
        rows = [r for r in rows if r["id"] in ids]
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            hong_lien = 0
            for n, lead in enumerate(rows):
                if (ROOT / "data" / "stop_batch").exists():
                    print("DỪNG: có data/stop_batch"); break
                try:
                    kq = gui_mot(page, lead, gui=not a.khong_gui)
                except FlowError as e:
                    page.screenshot(path=str(ROOT / "data" / f"nhan_tin_dung_lead{lead['id']}.png"))
                    print(f"{datetime.now():%H:%M:%S} DỪNG NGAY ở lead {lead['id']}: {e.code} {e}"); break
                except Exception as e:  # noqa: BLE001 — một lead lỗi thì ghi lại, sang lead khác
                    kq = f"LOI {type(e).__name__}"
                print(f"{datetime.now():%H:%M:%S} lead {lead['id']:>2} {lead['channel_user'][25:60]:<35} {kq}", flush=True)
                # cầu dao: 2 lead liền không gửi được = có thứ lạ trên màn hình → dừng, người xem ảnh chụp
                hong_lien = hong_lien + 1 if kq.startswith(("KHONG", "LOI")) else 0
                if hong_lien >= 2:
                    print(f"DỪNG: 2 lead liền không gửi được — xem data/nhan_tin_lead{lead['id']}.png"); break
                if kq.startswith("DA_GUI") or kq.startswith("CHUA_CHAC"):
                    con.execute("UPDATE leads SET stage='contacted', notes=COALESCE(notes,'') || ? WHERE id=?",
                                (f" | {now_str()} gửi tin mở đầu {kq[-2:]} ({kq})", lead["id"]))
                    con.commit()
                elif kq.startswith("KHONG"):
                    con.execute("UPDATE leads SET notes=COALESCE(notes,'') || ? WHERE id=?",
                                (f" | {now_str()} không gửi được: {kq}", lead["id"]))
                    con.commit()
                if not a.khong_gui and n < len(rows) - 1:
                    # đã gửi → nghỉ 3–5 phút; không gửi được → nghỉ ngắn
                    time.sleep(random.uniform(180, 300) if kq[:3] in ("DA_", "CHU") else random.uniform(30, 60))
        finally:
            ctx.close()


if __name__ == "__main__":
    main()
