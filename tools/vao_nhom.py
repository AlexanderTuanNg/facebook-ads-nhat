"""Vào thêm group Facebook, tối đa N nhóm/ngày (người dùng 26/09: "Ok vào thêm 2 nhóm mỗi ngày đi").

  python tools/vao_nhom.py            # vào tối đa 2 nhóm hôm nay (ứng viên `candidate`, ưu tiên quality_score cao)
  python tools/vao_nhom.py --so 1

Mỗi nhóm: mở trang → cảnh báo/checkpoint → dừng · đã là thành viên → ghi `joined` · bấm "Tham gia nhóm" (nút đầu trang)
→ hộp nội quy chỉ có nút đồng ý → lưu nội quy vào `groups.rules` rồi đồng ý · hộp có ô trả lời câu hỏi → KHÔNG tự điền,
lưu câu hỏi vào `notes`, đặt `cho_tra_loi` · sau cùng đọc nút: "Đã tham gia" → `joined` (làm quen 3 ngày mới đăng),
"Hủy yêu cầu"/"Đang chờ" → `requested`. Cách nhau 2–4 phút. Hồ sơ trình duyệt đi qua khoá chung.
"""
import argparse
import random
import re
import time
from datetime import datetime, timedelta

from common import ROOT, connect, now_str
from fb_group import FlowError, health_check, open_context
from ket_ban import CANH_BAO

DAU = "[VAO_NHOM"
VUNG_GIAP = r"hữu lũng|lạng sơn|chi lăng|võ nhai|đồng hỷ|phú bình"
VUNG_KCN = (r"đình trám|quang châu|vân trung|song khê|nội hoàng|hòa phú|hoà phú|yên lư|việt yên|nếnh|my điền|mi điền|vân cốc|"
            r"quang biểu|phước yên|trung đồng|hiệp hòa|hiệp hoà|yên dũng")
# 23/10: nhóm lạc đề (đã lỡ vào "Hội Diều Sáo Tân Yên", "Nhã Nam reading club") → bỏ qua từ tên, không mở trình duyệt
LAC_DE = re.compile(r"diều|sáo|reading|club|đọc sách|ăn vặt|đồ ăn|cây giống|keo hom|thú cưng|chim cảnh|cá cảnh|game|bóng đá|"
                    r"phượt|câu cá|mẹ và bé|mỹ phẩm|quần áo|thời trang", re.I)
DONG_Y = re.compile(r"^(Đồng ý|Tôi đồng ý|Agree|I agree)$", re.I)


def nut_chu(page, mau: re.Pattern):
    b = page.locator("div[role='main'] [role='button']")
    for i in range(min(b.count(), 60)):
        try:
            x = b.nth(i)
            t = (x.get_attribute("aria-label") or x.inner_text(timeout=300) or "").strip()
            if x.is_visible() and mau.search(t):
                return x
        except Exception:
            pass
    return None


def trang_thai(page) -> str:
    if nut_chu(page, re.compile(r"^Đã tham gia$", re.I)):
        return "joined"
    if nut_chu(page, re.compile(r"^(Hủy yêu cầu|Huỷ yêu cầu|Đang chờ|Đã gửi yêu cầu|Cancel request)", re.I)):
        return "requested"
    return ""


def vao_mot(page, con, g: dict) -> str:
    page.goto(g["url"], wait_until="domcontentloaded")
    page.wait_for_timeout(random.randint(6000, 8000))
    health_check(page)
    anh = str(ROOT / "data" / f"vao_nhom_g{g['id']}.png")
    m = re.search(CANH_BAO, page.locator("body").inner_text(timeout=5000), re.I)
    if m:
        page.screenshot(path=anh)
        raise FlowError("BI_CHAN", f"Facebook báo: '{m.group(0)}'")
    tt = trang_thai(page)
    if tt:
        return f"DA_{tt.upper()}_TU_TRUOC"
    # Trùng tên địa danh: "Yên Thế" còn là thị trấn ở Lục Yên (Yên Bái) → trang nhóm nói Yên Bái mà không nói Bắc Giang/Bắc Ninh thì bỏ
    chu = page.locator("div[role='main']").first.inner_text(timeout=5000)
    if re.search(r"Yên Bái|Lục Yên", chu) and not re.search(r"Bắc Giang|Bắc Ninh", chu):
        return "SAI_VUNG"
    # Tên nhóm không nói rõ vùng (vd "Chợ Quê An Thượng") → trang nhóm phải nhắc vùng đích, không thì bỏ (tên xã hay trùng nơi khác)
    # 28/09 chiều: thêm vùng giáp Yên Thế (Hữu Lũng/Lạng Sơn, Võ Nhai/Đồng Hỷ/Phú Bình của Thái Nguyên)
    # 15/10: nhóm KCN/nhà trọ quanh Việt Yên – Hiệp Hòa – Yên Dũng (người dùng 14/10 "tập trung nhóm khu công nghiệp") hay
    # không nhắc tên tỉnh ("Nhà trọ quang châu") → bị SAI_VUNG nhầm 5 nhóm → nhận thêm tên KCN và khu quanh KCN.
    if not re.search(r"yên thế|tân yên|bắc giang|bắc ninh|nhã nam|cao thượng|bố hạ|cầu gồ|" + VUNG_GIAP + "|" + VUNG_KCN, g["name"], re.I) and \
            not re.search(r"Yên Thế|Tân Yên|Bắc Giang|Bắc Ninh|" + VUNG_GIAP + "|" + VUNG_KCN, chu, re.I):
        return "SAI_VUNG"
    nut = nut_chu(page, re.compile(r"^Tham gia nhóm$", re.I))
    if nut is None:
        page.screenshot(path=anh)
        return "KHONG_CO_NUT_THAM_GIA"
    nut.click()
    page.wait_for_timeout(5000)
    dl = [d for d in page.locator("div[role='dialog']").all() if d.is_visible()]
    for d in dl:
        chu = d.inner_text(timeout=2000)
        if re.search(CANH_BAO, chu, re.I):
            page.screenshot(path=anh)
            raise FlowError("BI_CHAN", "hộp thoại cảnh báo khi vào nhóm")
        o_nhap = d.locator("textarea, input[type='text'], [contenteditable='true']")
        if o_nhap.count():
            page.screenshot(path=anh)
            con.execute("UPDATE groups SET status='cho_tra_loi', notes=COALESCE(notes,'') || ? WHERE id=?",
                        (f" | {now_str()} hỏi khi vào nhóm (chưa trả lời): {chu[:600]}", g["id"]))
            con.commit()
            page.keyboard.press("Escape")
            return "CO_CAU_HOI"
        dy = d.get_by_role("button", name=DONG_Y)
        if dy.count():
            con.execute("UPDATE groups SET rules=? WHERE id=?", (chu[:2000], g["id"]))
            con.commit()
            dy.first.click()
            page.wait_for_timeout(3000)
    page.screenshot(path=anh)
    tt = trang_thai(page)
    return {"joined": "DA_VAO", "requested": "CHO_DUYET"}.get(tt, "CHUA_CHAC")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--so", type=int, default=2, help="tối đa số nhóm vào hôm nay")
    a = ap.parse_args()
    con = connect()
    hom_nay = now_str()[:10]
    da_vao = con.execute("SELECT COUNT(*) FROM groups WHERE notes LIKE ?", (f"%{DAU} {hom_nay}%",)).fetchone()[0]
    con_lai = a.so - da_vao
    if con_lai <= 0:
        raise SystemExit(f"Hôm nay đã vào {da_vao}/{a.so} nhóm")
    ds = [dict(r) for r in con.execute(
        "SELECT * FROM groups WHERE status='candidate' ORDER BY COALESCE(quality_score,0) DESC, COALESCE(members,0) DESC, id")]
    lac = [g for g in ds if LAC_DE.search(g["name"] or "")]
    for g in lac:
        con.execute("UPDATE groups SET status='bo_qua', notes=COALESCE(notes,'') || ? WHERE id=?",
                    (f" | {now_str()} bỏ qua: nhóm lạc đề (không phải mua bán/nhà đất/tin địa phương)", g["id"]))
    con.commit()
    ds = [g for g in ds if g not in lac]
    if not ds:
        raise SystemExit("Hết nhóm ứng viên (status candidate) — cần tìm thêm")
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        ctx, page = open_context(pw, "nick_chinh", headless=False)
        try:
            for g in ds:
                if con_lai <= 0 or (ROOT / "data" / "stop_batch").exists():
                    break
                try:
                    kq = vao_mot(page, con, g)
                except FlowError as e:
                    print(f"{datetime.now():%H:%M:%S} DỪNG NGAY ở nhóm {g['id']}: {e.code} {e}", flush=True)
                    break
                except Exception as e:  # 23/10: nút "Tham gia" bị khoá ở 1 nhóm làm cả việc dừng 3 ngày liền → bỏ nhóm đó, đi tiếp
                    loi = str(e).splitlines()[0][:120]
                    print(f"{datetime.now():%H:%M:%S} nhóm {g['id']:>2} {g['name'][:45]:<45} LỖI_NHÓM {loi}", flush=True)
                    da_loi = "LỖI_NHÓM" in (g.get("notes") or "")
                    con.execute("UPDATE groups SET status=?, notes=COALESCE(notes,'') || ? WHERE id=?",
                                ("bo_qua" if da_loi else "candidate", f" | {now_str()} LỖI_NHÓM khi vào: {loi}", g["id"]))
                    con.execute("UPDATE groups SET quality_score=COALESCE(quality_score,0)-30 WHERE id=?", (g["id"],))
                    con.commit()
                    continue
                print(f"{datetime.now():%H:%M:%S} nhóm {g['id']:>2} {g['name'][:45]:<45} {kq}", flush=True)
                n = now_str()
                if kq in ("DA_VAO", "CHO_DUYET"):
                    st = "joined" if kq == "DA_VAO" else "requested"
                    lam_quen = (datetime.now() + timedelta(days=3)).strftime("%Y-%m-%d 00:00:00")
                    con.execute("UPDATE groups SET status=?, joined_at=?, warmup_until=?, notes=COALESCE(notes,'') || ? WHERE id=?",
                                (st, n, lam_quen, f" | {DAU} {n}] {kq}", g["id"]))
                    con_lai -= 1
                elif kq.startswith("DA_"):
                    con.execute("UPDATE groups SET status=?, notes=COALESCE(notes,'') || ? WHERE id=?",
                                ("joined" if "JOINED" in kq else "requested", f" | {n} kiểm: {kq}", g["id"]))
                elif kq == "SAI_VUNG":
                    con.execute("UPDATE groups SET status='bo_qua', notes=COALESCE(notes,'') || ? WHERE id=?",
                                (f" | {n} bỏ qua: không phải vùng đích (trang nhóm nói Yên Bái/Lục Yên, hoặc không nhắc Yên Thế/Tân Yên/Bắc Giang/Bắc Ninh/vùng giáp)", g["id"]))
                elif kq != "CO_CAU_HOI":
                    con.execute("UPDATE groups SET notes=COALESCE(notes,'') || ? WHERE id=?", (f" | {n} vào nhóm: {kq}", g["id"]))
                con.commit()
                if con_lai > 0:
                    time.sleep(random.uniform(120, 240))
        finally:
            ctx.close()


if __name__ == "__main__":
    main()
