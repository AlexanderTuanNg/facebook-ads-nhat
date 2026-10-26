"""Fanpage qua Meta Graph API (chính thức). Cần FB_PAGE_ID, FB_PAGE_TOKEN trong .env.

  python tools/fb_page.py me
  python tools/fb_page.py post --post-id 12 [--schedule "2026-09-28 20:00"] [--now]
  python tools/fb_page.py sync                         # cập nhật bài đã hẹn giờ → published
  python tools/fb_page.py comments --fb-post-id <id>   # comment chưa xử lý (JSON)
  python tools/fb_page.py reply --comment-id <id> --message "..."
  python tools/fb_page.py mark --comment-id <id> --action skipped|escalated
  python tools/fb_page.py stats --post-id 12
"""
import argparse
import json
import os
import sys
from datetime import timedelta

import requests

from common import ROOT, connect, get_post, load_env, now_str, now_vn, parse_ts, read_post_file, settings, to_unix, update_post

load_env()
API = f"https://graph.facebook.com/{settings().get('graph_api_version', 'v23.0')}"
PAGE_ID = os.environ.get("FB_PAGE_ID", "")
TOKEN = os.environ.get("FB_PAGE_TOKEN", "")


def call(method: str, path: str, **kw) -> dict:
    if not PAGE_ID or not TOKEN:
        sys.exit("ERROR: thiếu FB_PAGE_ID / FB_PAGE_TOKEN trong .env (xem docs/02-setup-meta.md)")
    params = kw.pop("params", {})
    params["access_token"] = TOKEN
    r = requests.request(method, f"{API}/{path.lstrip('/')}", params=params, timeout=60, **kw)
    data = r.json() if r.content else {}
    if r.status_code >= 400 or "error" in data:
        err = data.get("error", {})
        sys.exit(f"GRAPH_ERROR {r.status_code}: {err.get('message', r.text)} (code={err.get('code')})")
    return data


def _block_if_lint_fails(text: str) -> None:
    """Chốt chặn cuối: dù compliance đã duyệt, nội dung vi phạm từ cấm/giá vẫn không được gửi lên Facebook."""
    from db import lint_text

    hits = lint_text(text)
    if hits:
        sys.exit("BLOCKED_BY_LINT:\n" + "\n".join(hits))


def cmd_me(a):
    print(json.dumps(call("GET", PAGE_ID, params={"fields": "id,name,fan_count,followers_count,link"}),
                     ensure_ascii=False, indent=2))


def _upload_photo(path: str, published: bool) -> str:
    p = ROOT / path if not os.path.isabs(path) else path
    with open(p, "rb") as f:
        data = {"published": str(published).lower()}
        if not published:
            data["temporary"] = "true"
        return call("POST", f"{PAGE_ID}/photos", data=data, files={"source": f})["id"]


def cmd_post(a):
    con = connect()
    post = get_post(con, a.post_id)
    if post["channel"] != "page":
        sys.exit("ERROR: post này không phải channel=page")
    ok = ("approved_human",) if settings()["require_human_approval"] else ("approved", "approved_human")
    if post["status"] not in ok:
        sys.exit(f"ERROR: status={post['status']}, cần {ok}")
    meta, body = read_post_file(post["content_path"])
    _block_if_lint_fails(body)
    images = meta.get("images") or []

    sched = None
    if not a.now:
        when = a.schedule or post["scheduled_at"]
        if when:
            dt = parse_ts(when)
            if dt - now_vn() < timedelta(minutes=11):
                print("INFO: thời điểm hẹn < 11 phút nữa → đăng ngay")
            elif dt - now_vn() > timedelta(days=29, hours=23):
                sys.exit("ERROR: Graph API chỉ hẹn giờ tối đa 30 ngày")
            else:
                sched = dt

    payload = {"message": body}
    if meta.get("link"):
        payload["link"] = meta["link"]
    if sched:
        payload["published"] = "false"
        payload["scheduled_publish_time"] = str(to_unix(sched))

    if len(images) == 1 and not meta.get("link"):
        p = ROOT / images[0]
        with open(p, "rb") as f:
            res = call("POST", f"{PAGE_ID}/photos", data={**payload, "caption": body}, files={"source": f})
        fb_id = res.get("post_id") or res["id"]
    else:
        for i, img in enumerate(images):
            payload[f"attached_media[{i}]"] = json.dumps({"media_fbid": _upload_photo(img, published=False)})
        fb_id = call("POST", f"{PAGE_ID}/feed", data=payload)["id"]

    if sched:
        update_post(con, a.post_id, status="scheduled", fb_post_id=fb_id, scheduled_at=sched.strftime("%Y-%m-%d %H:%M:%S"))
        print(f"SCHEDULED post {a.post_id} → {fb_id} lúc {sched}")
    else:
        # Đóng vòng lặp: đọc lại từ API, chỉ coi là đăng thành công khi Facebook xác nhận
        d = call("GET", fb_id, params={"fields": "is_published,permalink_url"})
        if not d.get("is_published"):
            update_post(con, a.post_id, status="failed", fb_post_id=fb_id)
            sys.exit(f"VERIFY_FAILED: API tạo {fb_id} nhưng bài chưa ở trạng thái published")
        update_post(con, a.post_id, status="published", fb_post_id=fb_id, published_at=now_str(), url=d.get("permalink_url"))
        print(f"PUBLISHED post {a.post_id} → {fb_id} | VERIFIED {d.get('permalink_url')}")


def cmd_sync(a):
    con = connect()
    rows = con.execute("SELECT id, fb_post_id, scheduled_at FROM posts WHERE channel='page' AND status='scheduled'").fetchall()
    for r in rows:
        if parse_ts(r["scheduled_at"]) > now_vn():
            continue
        d = call("GET", r["fb_post_id"], params={"fields": "is_published,permalink_url,created_time"})
        if d.get("is_published"):
            update_post(con, r["id"], status="published", published_at=r["scheduled_at"], url=d.get("permalink_url"))
            print(f"post {r['id']} → published")
    print("OK sync")


def cmd_comments(a):
    con = connect()
    done = {r[0] for r in con.execute("SELECT comment_id FROM comments_handled")}
    data = call("GET", f"{a.fb_post_id}/comments", params={
        "fields": "id,from{id,name},message,created_time,comment_count", "filter": "stream", "limit": 100})
    out = [c for c in data.get("data", [])
           if c["id"] not in done and (c.get("from") or {}).get("id") != PAGE_ID]
    print(json.dumps(out, ensure_ascii=False, indent=2))


def _mark(comment_id, action, fb_post_id=None):
    con = connect()
    con.execute("INSERT OR REPLACE INTO comments_handled(comment_id, fb_post_id, action, handled_at) VALUES(?,?,?,?)",
                (comment_id, fb_post_id, action, now_str()))
    con.commit()


def cmd_reply(a):
    _block_if_lint_fails(a.message)
    res = call("POST", f"{a.comment_id}/comments", data={"message": a.message})
    _mark(a.comment_id, "replied")
    print(f"REPLIED {res.get('id')}")


def cmd_mark(a):
    _mark(a.comment_id, a.action)
    print("OK")


def cmd_stats(a):
    con = connect()
    post = get_post(con, a.post_id)
    if not post["fb_post_id"]:
        sys.exit("ERROR: post chưa có fb_post_id")
    d = call("GET", post["fb_post_id"], params={
        "fields": "reactions.summary(total_count).limit(0),comments.summary(total_count).limit(0),shares,is_published"})
    reactions = d.get("reactions", {}).get("summary", {}).get("total_count")
    comments = d.get("comments", {}).get("summary", {}).get("total_count")
    shares = (d.get("shares") or {}).get("count", 0)
    views = None
    metrics = settings().get("post_view_metrics") or []
    if metrics:  # metric insights thay đổi theo Meta: cấu hình trong settings sau khi kiểm tra docs
        try:
            ins = call("GET", f"{post['fb_post_id']}/insights", params={"metric": ",".join(metrics)})
            views = sum((m["values"][0]["value"] or 0) for m in ins.get("data", []) if isinstance(m["values"][0]["value"], int))
        except SystemExit as e:
            print(f"WARN insights: {e}")
    con.execute("INSERT INTO metrics(post_id,captured_at,reactions,comments,shares,views,alive,state,source) "
                "VALUES(?,?,?,?,?,?,1,'published','graph')",
                (a.post_id, now_str(), reactions, comments, shares, views))
    con.commit()
    print(json.dumps({"post_id": a.post_id, "reactions": reactions, "comments": comments, "shares": shares, "views": views}))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("me")
    p = sp.add_parser("post"); p.add_argument("--post-id", type=int, required=True); p.add_argument("--schedule"); p.add_argument("--now", action="store_true")
    sp.add_parser("sync")
    p = sp.add_parser("comments"); p.add_argument("--fb-post-id", required=True)
    p = sp.add_parser("reply"); p.add_argument("--comment-id", required=True); p.add_argument("--message", required=True)
    p = sp.add_parser("mark"); p.add_argument("--comment-id", required=True); p.add_argument("--action", required=True, choices=["skipped", "escalated", "replied"])
    p = sp.add_parser("stats"); p.add_argument("--post-id", type=int, required=True)
    a = ap.parse_args()
    globals()["cmd_" + a.cmd](a)


if __name__ == "__main__":
    main()
