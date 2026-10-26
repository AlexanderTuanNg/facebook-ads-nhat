"""Đăng bài vào Facebook Group bằng trình duyệt (Playwright). Groups API đã bị Meta khai tử 04/2024.

  python tools/fb_group.py login    --account nick_chinh   # NGƯỜI DÙNG tự đăng nhập, đóng trình duyệt để lưu
  python tools/fb_group.py check    --account nick_phu_1   # kiểm tra session / checkpoint
  python tools/fb_group.py prefill  --post-id 12           # Nhánh A: điền sẵn, người bấm Đăng
  python tools/fb_group.py autopost --post-id 13           # Nhánh B: tự đăng (có giới hạn + delay)
  python tools/fb_group.py stats    --post-id 13           # kiểm tra bài còn sống / chờ duyệt / bị xoá

Selector nằm trong tools/fb_selectors.json. Khi FB đổi giao diện, script báo SELECTOR_NOT_FOUND.
"""
import argparse
import json
import random
import re
import sys
import time
from pathlib import Path

from common import PROFILES_DIR, ROOT, connect, get_post, now_str, read_post_file, record_health, settings, update_post
from db import can_post, lint_text

SEL = json.loads((ROOT / "tools" / "fb_selectors.json").read_text(encoding="utf-8"))


class FlowError(Exception):
    """code: SELECTOR_NOT_FOUND | CHECKPOINT | SESSION_EXPIRED | ..."""

    def __init__(self, code: str, detail: str = ""):
        super().__init__(f"{code} {detail}".strip())
        self.code = code


# ---------- trình duyệt ----------
def open_context(pw, account_key: str, headless: bool = False):
    from khoa_ho_so import lay_khoa  # mỗi lúc 1 tiến trình dùng hồ sơ; bận → PROFILE_BUSY (26/09)

    lay_khoa(account_key)
    profile = PROFILES_DIR / account_key
    profile.mkdir(parents=True, exist_ok=True)
    ctx = pw.chromium.launch_persistent_context(
        str(profile), headless=headless, locale="vi-VN", timezone_id="Asia/Ho_Chi_Minh",
        viewport={"width": 1280, "height": 860}, args=["--disable-blink-features=AutomationControlled"])
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    return ctx, page


def locate(page, key: str, timeout_ms: int = 8000, required: bool = True):
    """Thử lần lượt các phương án selector trong fb_selectors.json."""
    deadline = time.time() + timeout_ms / 1000
    while True:
        for spec in SEL[key]:
            kind, _, val = spec.partition(":")
            if kind == "role":
                role, _, name = val.partition("|")
                loc = page.get_by_role(role, name=re.compile(name, re.I))
            elif kind == "text":
                loc = page.get_by_text(re.compile(val, re.I))
            else:
                loc = page.locator(val)
            try:
                if loc.count() and loc.first.is_visible():
                    return loc.first
            except Exception:
                pass
        if time.time() > deadline:
            if required:
                raise FlowError("SELECTOR_NOT_FOUND", key)
            return None
        page.wait_for_timeout(400)


def has_any(page, key: str) -> bool:
    return locate(page, key, timeout_ms=300, required=False) is not None


def health_check(page) -> None:
    url = page.url.lower()
    if "checkpoint" in url or has_any(page, "checkpoint_markers"):
        raise FlowError("CHECKPOINT", page.url)
    if "/login" in url or has_any(page, "login_markers"):
        raise FlowError("SESSION_EXPIRED", page.url)


def human_pause(rng):
    time.sleep(random.uniform(*rng))


# ---------- lệnh ----------
def cmd_login(a):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        ctx, page = open_context(pw, a.account)
        page.goto("https://www.facebook.com/")
        print(f"Trình duyệt đã mở với profile '{a.account}'. Anh tự đăng nhập (kể cả 2FA), "
              "sau đó ĐÓNG cửa sổ trình duyệt để lưu phiên.", flush=True)
        try:
            page.wait_for_event("close", timeout=0)
        except Exception:
            pass
        try:
            ctx.close()
        except Exception:
            pass  # người dùng đóng cả cửa sổ thì trình duyệt đã tự thoát (Playwright mới báo TargetClosedError)
    print(f"OK: đã đóng trình duyệt. Xác nhận phiên bằng: python tools/fb_group.py check --account {a.account}")


def _account(con, key=None, account_id=None):
    row = con.execute("SELECT * FROM accounts WHERE key=? OR id=?", (key, account_id)).fetchone()
    if not row:
        sys.exit("ERROR: không tìm thấy account")
    return row


def cmd_check(a):
    from playwright.sync_api import sync_playwright

    con = connect()
    acc = _account(con, key=a.account)
    with sync_playwright() as pw:
        ctx, page = open_context(pw, a.account, headless=settings()["arm_b"]["headless"])
        try:
            page.goto("https://www.facebook.com/", wait_until="domcontentloaded")
            page.wait_for_timeout(4000)
            health_check(page)
            record_health(con, acc["id"], "ok", "check")
            print("OK: session hợp lệ")
        except FlowError as e:
            ev = "checkpoint" if e.code == "CHECKPOINT" else "session_expired"
            record_health(con, acc["id"], ev, str(e))
            print(e.code)
        finally:
            ctx.close()


def _prepare(con, post_id: int, want_arm: str):
    post = get_post(con, post_id)
    if post["channel"] != "group":
        sys.exit("ERROR: post không phải channel=group")
    if post["arm"] != want_arm:
        sys.exit(f"ERROR: post thuộc nhánh {post['arm']}, lệnh này cho nhánh {want_arm}")
    ok = ("approved_human",) if settings()["require_human_approval"] else ("approved", "approved_human")
    if post["status"] not in ok:
        sys.exit(f"ERROR: status={post['status']}, cần {ok}")
    verdict = can_post(con, post["account_id"], post["target_id"])
    if verdict != "OK":
        sys.exit(verdict)
    group = con.execute("SELECT * FROM groups WHERE id=?", (post["target_id"],)).fetchone()
    if not group:
        sys.exit("ERROR: không có group đích")
    acc = _account(con, account_id=post["account_id"])
    meta, body = read_post_file(post["content_path"])
    hits = lint_text(body)
    if hits:
        sys.exit("BLOCKED_BY_LINT:\n" + "\n".join(hits))
    images = [str(ROOT / p) for p in (meta.get("images") or [])]
    for img in images:
        if not Path(img).exists():
            sys.exit(f"ERROR: thiếu ảnh {img}")
    return post, group, acc, body, images


def _fill_composer(page, body: str, images: list, human: bool, strict_images: bool | None = None):
    ab = settings()["arm_b"]
    locate(page, "composer_open", 15000).click()
    locate(page, "composer_dialog", 10000)
    box = locate(page, "composer_textbox", 10000)
    box.click()
    if human:
        human_pause(ab["pre_action_delay_s"])
        lo, hi = ab["typing_delay_ms"]
        for para_i, para in enumerate(body.split("\n")):
            if para_i:
                page.keyboard.press("Shift+Enter")
            for ch in para:
                page.keyboard.type(ch)
                time.sleep(random.uniform(lo, hi) / 1000)
    else:
        page.keyboard.insert_text(body)
    if images:
        try:
            _attach_images(page, images)
        except FlowError as e:
            if human if strict_images is None else strict_images:  # không có người để gắn ảnh tay → dừng
                raise
            print(f"ẢNH CHƯA TỰ LÊN ({e}): bấm biểu tượng ảnh màu xanh lá trong khung soạn, chọn {images[0]}, rồi bấm Đăng.")


def _attach_images(page, images: list):
    """Gắn ảnh vào khung soạn. Ô chọn file của Facebook luôn bị ẩn nên không dùng locate() (locate đòi hiển thị).
    Chỉ tìm trong hộp thoại soạn bài, tránh ô tải ảnh của trang group bên ngoài (sẽ mở một bài khác)."""
    def o_file():
        loc = page.locator("div[role='dialog'] input[type='file']")
        return loc.first if loc.count() else None

    inp = o_file()
    if inp is None:
        btn = locate(page, "photo_button", 6000, required=False)
        if btn is None:
            raise FlowError("SELECTOR_NOT_FOUND", "photo_button")
        try:
            with page.expect_file_chooser(timeout=4000) as fc:
                btn.click()
            fc.value.set_files(images)
            page.wait_for_timeout(3000 + 1500 * len(images) + (20000 if co_video(images) else 0))
            return
        except Exception:
            pass  # nút chỉ mở vùng tải ảnh, chưa bật hộp chọn file → tìm lại ô chọn file
        for _ in range(10):
            inp = o_file()
            if inp is not None:
                break
            page.wait_for_timeout(500)
        if inp is None:
            raise FlowError("SELECTOR_NOT_FOUND", "photo_input")
    inp.set_input_files(images)
    page.wait_for_timeout(3000 + 1500 * len(images) + (20000 if co_video(images) else 0))


def co_video(files) -> bool:
    """26/10: bài gắn video (.mp4/.mov) — tải lên lâu hơn ảnh nhiều (video ~10–15 MB)."""
    return any(str(f).lower().endswith((".mp4", ".mov")) for f in files)


def _wait_enabled(page, key: str, timeout_s: int = 60):
    """Chờ nút bật rồi mới trả về. Facebook khoá nút Đăng (aria-disabled) khi ảnh đang tải hoặc khung soạn chưa nhận chữ,
    và vẽ lại nút sau khi ảnh tải xong → tìm lại nút mỗi giây thay vì giữ một phần tử cũ."""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        btn = locate(page, key, 5000, required=False)
        if btn is not None and (btn.get_attribute("aria-disabled") or "false") != "true":
            return btn
        page.wait_for_timeout(1000)
    raise FlowError("POST_BUTTON_DISABLED", f"{key} vẫn bị khoá sau {timeout_s} giây")


def _after_submit_state(page) -> str:
    page.wait_for_timeout(5000)
    health_check(page)
    return "pending_approval" if has_any(page, "pending_markers") else "published"


def _run_group_flow(post_id: int, arm: str):
    from playwright.sync_api import sync_playwright

    con = connect()
    post, group, acc, body, images = _prepare(con, post_id, arm)
    ab = settings()["arm_b"]
    with sync_playwright() as pw:
        ctx, page = open_context(pw, acc["key"], headless=(arm == "B" and ab["headless"]))
        try:
            page.goto(group["url"], wait_until="domcontentloaded")
            page.wait_for_timeout(random.randint(3000, 6000))
            health_check(page)

            if arm == "A":
                _fill_composer(page, body, images, human=False)
                wait_min = settings()["arm_a_wait_minutes"]
                print(f"READY: đã điền sẵn bài vào '{group['name']}'. Anh kiểm tra rồi bấm ĐĂNG (chờ {wait_min} phút).")
                dialog = locate(page, "composer_dialog", 5000)
                try:
                    dialog.wait_for(state="detached", timeout=wait_min * 60_000)
                except Exception:
                    update_post(con, post_id, status="skipped")
                    print("SKIPPED: hết thời gian chờ, chưa đăng")
                    return
                state = _after_submit_state(page)
            else:
                # Dán cả đoạn như người dùng copy-paste. Gõ từng ký tự (26/09, bài 13) làm nút Đăng bị khoá → không bấm được.
                _fill_composer(page, body, images, human=False, strict_images=True)
                human_pause(ab["pre_action_delay_s"])
                vid = co_video(images)  # 26/10: video tải lên lâu → chờ nút Đăng tới 4 phút, chờ hộp soạn đóng tới 3 phút
                _wait_enabled(page, "post_button", 240 if vid else 60).click()
                try:
                    locate(page, "composer_dialog", 1000).wait_for(state="detached", timeout=180_000 if vid else 60_000)
                except FlowError:
                    pass
                except Exception:  # 07/10 bài 87, 88: bấm Đăng xong hộp soạn vẫn mở 60 giây → ghi chữ trong hộp để biết vì sao
                    try:
                        chu = page.locator("div[role='dialog']").last.inner_text(timeout=3000)
                    except Exception:
                        chu = "?"
                    raise FlowError("DIALOG_KHONG_DONG", "đã bấm Đăng, hộp soạn không đóng sau 60 giây — CÓ THỂ ĐÃ ĐĂNG, kiểm tay: "
                                    + " ".join(chu.split())[:300])
                state = _after_submit_state(page)

            update_post(con, post_id, status=state, published_at=now_str(), url=group["url"])
            record_health(con, acc["id"], "ok", f"post {post_id}")
            print(f"{state.upper()} post {post_id} → {group['name']}")
            if arm == "B":
                human_pause(ab["post_cooldown_s"])
        except FlowError as e:
            if e.code == "CHECKPOINT":
                record_health(con, acc["id"], "checkpoint", str(e))
                update_post(con, post_id, status="failed")
                print(f"CHECKPOINT: đã tạm dừng account {acc['key']}. Kiểm tra tài khoản thủ công.")
            elif e.code == "SESSION_EXPIRED":
                record_health(con, acc["id"], "session_expired", str(e))
                print(f"SESSION_EXPIRED: chạy `python tools/fb_group.py login --account {acc['key']}`")
            else:
                shot = ROOT / "data" / f"error_post{post_id}.png"
                page.screenshot(path=str(shot))
                update_post(con, post_id, status="failed")
                print(f"{e.code}: {e} (ảnh chụp: {shot})")
            sys.exit(1)
        except Exception as e:  # lỗi Playwright khác (06/10 bài 82, 07/10 bài 101): trước đây văng ra không ảnh → chụp lại
            shot = ROOT / "data" / f"error_post{post_id}.png"
            try:
                page.screenshot(path=str(shot))
            except Exception:
                pass
            update_post(con, post_id, status="failed")  # không để lịch khởi động lại tự đăng lần 2 (có thể trùng)
            print(f"LOI_LA: {type(e).__name__}: {' '.join(str(e).split())[:300]} (ảnh chụp: {shot})")
            sys.exit(1)
        finally:
            ctx.close()


def cmd_prefill(a):
    _run_group_flow(a.post_id, "A")


def cmd_autopost(a):
    _run_group_flow(a.post_id, "B")


def cmd_stats(a):
    """So khớp đoạn đầu bài với trang 'nội dung của bạn' trong group → published / pending / removed."""
    from playwright.sync_api import sync_playwright

    con = connect()
    post = get_post(con, a.post_id)
    group = con.execute("SELECT * FROM groups WHERE id=?", (post["target_id"],)).fetchone()
    acc = _account(con, account_id=post["account_id"])
    _, body = read_post_file(post["content_path"])
    probe = re.sub(r"\s+", " ", body)[:50].strip()
    base = group["url"].rstrip("/")
    state = None
    with sync_playwright() as pw:
        ctx, page = open_context(pw, acc["key"], headless=True)
        try:
            for suffix, st in (("/my_posted_content", "published"), ("/my_pending_content", "pending")):
                page.goto(base + suffix, wait_until="domcontentloaded")
                page.wait_for_timeout(4000)
                health_check(page)
                if probe and page.get_by_text(probe[:40], exact=False).count():
                    state = st
                    break
        except FlowError as e:
            print(e.code)
            sys.exit(1)
        finally:
            ctx.close()
    if state is None:
        # Không thấy 1 lần có thể do trang tải chậm → chỉ kết luận 'removed' khi 2 lần liên tiếp không thấy
        prev = con.execute("SELECT state FROM metrics WHERE post_id=? ORDER BY captured_at DESC LIMIT 1",
                           (a.post_id,)).fetchone()
        state = "removed" if prev and prev["state"] in ("not_found", "removed") else "not_found"
    con.execute("INSERT INTO metrics(post_id,captured_at,alive,state,source) VALUES(?,?,?,?,'browser')",
                (a.post_id, now_str(), {"removed": 0, "not_found": None}.get(state, 1), state))
    if state == "removed" and post["status"] != "removed":
        update_post(con, a.post_id, status="removed")
        con.execute("UPDATE groups SET removed_count = removed_count + 1 WHERE id=?", (group["id"],))
        record_health(con, acc["id"], "post_removed", f"post {a.post_id} @ {group['name']}")
    con.commit()
    print(json.dumps({"post_id": a.post_id, "state": state}, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    for name in ("login", "check"):
        sp.add_parser(name).add_argument("--account", required=True)
    for name in ("prefill", "autopost", "stats"):
        sp.add_parser(name).add_argument("--post-id", type=int, required=True)
    a = ap.parse_args()
    globals()["cmd_" + a.cmd](a)


if __name__ == "__main__":
    main()
