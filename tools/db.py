"""CLI SQLite cho các agent.

  python tools/db.py init
  python tools/db.py q  "SELECT ..."          # truy vấn, in bảng
  python tools/db.py x  "INSERT/UPDATE ..."   # ghi
  python tools/db.py status
  python tools/db.py due [--date YYYY-MM-DD]  # bài đến hạn đăng
  python tools/db.py recent --channel page --days 7
  python tools/db.py can-post <account_id> [--group <group_id>]
  python tools/db.py similar <post_id>
  python tools/db.py lint <post_id> | lint --text "câu trả lời comment"
  python tools/db.py ab-report [--days 7]
  python tools/db.py run-start <agent> "<task>" / run-end <run_id> "<summary>"
  python tools/db.py task-add --owner copywriter --title "..." --acceptance "..." --evidence-required "..."
  python tools/db.py task-submit <id> --evidence "..."          # owner nộp
  python tools/db.py task-verify <id> --verifier judge --verdict pass|fail --note "..."   # người KHÁC owner
  python tools/db.py task-close <id> [--status done|dropped|open]   # Lead; 'done' chỉ khi đã verified
  python tools/db.py tasks [--id N] [--all]
"""
import argparse
import re
import unicodedata
from datetime import timedelta
from difflib import SequenceMatcher

from common import SCHEMA_PATH, connect, now_str, now_vn, parse_ts, read_post_file, settings

READY = ("approved", "approved_human")
POSTED = ("published", "pending_approval")


def print_rows(rows) -> None:
    rows = list(rows)
    if not rows:
        print("(0 dòng)")
        return
    cols = rows[0].keys()
    data = [[("" if r[c] is None else str(r[c])) for c in cols] for r in rows]
    widths = [min(max(len(c), *(len(d[i]) for d in data)), 60) for i, c in enumerate(cols)]
    print(" | ".join(c.ljust(w) for c, w in zip(cols, widths)))
    print("-+-".join("-" * w for w in widths))
    for d in data:
        print(" | ".join(v[:60].ljust(w) for v, w in zip(d, widths)))
    print(f"({len(rows)} dòng)")


MIGRATIONS = {  # cột thêm sau khi DB đã tạo: (bảng, cột) → kiểu
    ("posts", "judge_score"): "INTEGER",
    ("posts", "judge_note"): "TEXT",
}


def cmd_init(con, a):
    con.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    for (table, col), typ in MIGRATIONS.items():
        cols = {r["name"] for r in con.execute(f"PRAGMA table_info({table})")}
        if col not in cols:
            con.execute(f"ALTER TABLE {table} ADD COLUMN {col} {typ}")
    con.commit()
    print("OK: DB sẵn sàng")


def cmd_task_add(con, a):
    cur = con.execute(
        "INSERT INTO tasks(loop,title,owner,inputs,acceptance,evidence_required) VALUES(?,?,?,?,?,?)",
        (a.loop, a.title, a.owner, a.inputs, a.acceptance, a.evidence_required))
    con.commit()
    print(cur.lastrowid)


def cmd_task_submit(con, a):
    t = con.execute("SELECT * FROM tasks WHERE id=?", (a.task_id,)).fetchone()
    if not t:
        print("ERROR: không có task")
        return
    if not a.evidence.strip():
        print("ERROR: phải có bằng chứng")
        return
    con.execute("UPDATE tasks SET status='submitted', evidence=?, attempts=attempts+1, updated_at=? WHERE id=?",
                (a.evidence, now_str(), a.task_id))
    con.commit()
    print("OK: đã nộp, chờ kiểm chứng độc lập")


def cmd_task_verify(con, a):
    t = con.execute("SELECT * FROM tasks WHERE id=?", (a.task_id,)).fetchone()
    if not t:
        print("ERROR: không có task")
        return
    if a.verifier.strip().lower() == t["owner"].strip().lower():
        print("ERROR: người kiểm chứng phải khác owner (không tự duyệt việc của mình)")
        return
    if t["status"] != "submitted":
        print(f"ERROR: task đang '{t['status']}', chỉ kiểm chứng task 'submitted'")
        return
    status = "verified" if a.verdict == "pass" else "rejected"
    con.execute("UPDATE tasks SET status=?, verifier=?, verdict=?, verdict_note=?, updated_at=? WHERE id=?",
                (status, a.verifier, a.verdict, a.note, now_str(), a.task_id))
    con.commit()
    print(f"OK: task {a.task_id} → {status}")


def cmd_task_close(con, a):
    t = con.execute("SELECT status FROM tasks WHERE id=?", (a.task_id,)).fetchone()
    if not t:
        print("ERROR: không có task")
        return
    if a.status == "done" and t["status"] != "verified":
        print("ERROR: chỉ đóng 'done' khi task đã 'verified'")
        return
    con.execute("UPDATE tasks SET status=?, updated_at=? WHERE id=?", (a.status, now_str(), a.task_id))
    con.commit()
    print("OK")


def cmd_tasks(con, a):
    if a.id:
        row = con.execute("SELECT * FROM tasks WHERE id=?", (a.id,)).fetchone()
        for k in (row.keys() if row else []):
            print(f"{k}: {row[k]}")
        return
    where = "" if a.all else "WHERE status NOT IN ('done','dropped')"
    print_rows(con.execute(f"SELECT id, loop, owner, status, verdict, attempts, title FROM tasks {where} ORDER BY id"))


def cmd_q(con, a):
    print_rows(con.execute(a.sql).fetchall())


def cmd_x(con, a):
    cur = con.execute(a.sql)
    con.commit()
    print(f"OK: {cur.rowcount} dòng, lastrowid={cur.lastrowid}")


def cmd_status(con, a):
    print("== Bài theo trạng thái ==")
    print_rows(con.execute("SELECT channel, arm, status, COUNT(*) n FROM posts GROUP BY 1,2,3 ORDER BY 1,2,3"))
    print("\n== Tài khoản ==")
    print_rows(con.execute("SELECT id, key, type, arm, status FROM accounts"))
    print("\n== Group ==")
    print_rows(con.execute("SELECT status, arm, COUNT(*) n FROM groups GROUP BY 1,2"))
    print("\n== Lead 7 ngày ==")
    print_rows(con.execute(
        "SELECT stage, COUNT(*) n FROM leads WHERE created_at >= datetime('now','+7 hours','-7 days') GROUP BY 1"))
    print("\n== Task đang mở ==")
    print_rows(con.execute("SELECT id, owner, status, title FROM tasks WHERE status NOT IN ('done','dropped') ORDER BY id"))
    print("\n== Sự cố nick 14 ngày ==")
    print_rows(con.execute(
        "SELECT a.key, h.at, h.event, h.notes FROM account_health h JOIN accounts a ON a.id=h.account_id "
        "WHERE h.event <> 'ok' AND h.at >= datetime('now','+7 hours','-14 days') ORDER BY h.at DESC"))


def cmd_due(con, a):
    day = a.date or now_vn().strftime("%Y-%m-%d")
    print_rows(con.execute(
        f"SELECT id, slug, channel, arm, account_id, target_id, scheduled_at, status FROM posts "
        f"WHERE status IN ({','.join('?' * len(READY))}) AND substr(replace(scheduled_at,'T',' '),1,10) <= ? "
        f"ORDER BY scheduled_at", (*READY, day)))


def cmd_recent(con, a):
    since = (now_vn() - timedelta(days=a.days)).strftime("%Y-%m-%d %H:%M:%S")
    print_rows(con.execute(
        "SELECT id, slug, channel, arm, fb_post_id, url, published_at, status FROM posts "
        "WHERE channel=? AND status IN ('published','pending_approval') AND published_at >= ? ORDER BY published_at",
        (a.channel, since)))


def can_post(con, account_id: int, group_id: int | None = None) -> str:
    acc = con.execute("SELECT * FROM accounts WHERE id=?", (account_id,)).fetchone()
    if not acc:
        return "ERROR không có account"
    if acc["status"] != "active":
        return f"PAUSED account status={acc['status']}"
    if acc["type"] == "page":
        return "OK"
    lim = settings()["limits"]
    now = now_vn()
    rows = con.execute(
        f"SELECT published_at, target_id FROM posts WHERE account_id=? AND channel='group' "
        f"AND status IN ({','.join('?' * len(POSTED))}) AND published_at IS NOT NULL",
        (account_id, *POSTED)).fetchall()
    times = [(parse_ts(r["published_at"]), r["target_id"]) for r in rows]
    today = [t for t, _ in times if t.date() == now.date()]
    if len(today) >= lim["profile_group_posts_per_day"]:
        return f"LIMIT đã đăng {len(today)} bài hôm nay"
    week = [t for t, _ in times if t >= now - timedelta(days=7)]
    if len(week) >= lim["profile_group_posts_per_week"]:
        return f"LIMIT đã đăng {len(week)} bài/7 ngày"
    if times:
        last = max(t for t, _ in times)
        gap = (now - last).total_seconds() / 60
        if gap < lim["min_minutes_between_posts"]:
            return f"WAIT {int(lim['min_minutes_between_posts'] - gap) + 1} phút"
    if group_id is not None:
        same = [t for t, g in times if g == group_id and t >= now - timedelta(days=lim["same_group_min_days"])]
        if same:
            return f"LIMIT group {group_id} đã đăng trong {lim['same_group_min_days']} ngày qua"
    return "OK"


def cmd_can_post(con, a):
    print(can_post(con, a.account_id, a.group))


def _norm(text: str) -> str:
    text = unicodedata.normalize("NFC", text.lower())
    text = re.sub(r"https?://\S+|#\S+", " ", text)
    return " ".join(re.sub(r"[^\w\s]", " ", text).split())


def _shingles(text: str, n: int = 3) -> set:
    words = re.findall(r"\w+", unicodedata.normalize("NFC", text.lower()))
    return {" ".join(words[i:i + n]) for i in range(max(len(words) - n + 1, 1))}


def similarity(a: str, b: str) -> float:
    """max(Jaccard cụm 3 chữ, SequenceMatcher), ĐỐI XỨNG. SequenceMatcher (autojunk) phụ thuộc thứ tự: 28/09 bài 39→41 = 0,657
    nhưng 41→39 = 0,445 → cặp trùng lọt khi chỉ kiểm từ một phía. Lấy max hai chiều, giữ autojunk để không đổi thang đo
    (tắt autojunk làm mọi cặp tăng ~+0,3 vì câu pháp lý/lời mời bắt buộc giống nhau → ngưỡng 0,6 mất nghĩa)."""
    sa, sb = _shingles(a), _shingles(b)
    jac = len(sa & sb) / len(sa | sb) if sa | sb else 0.0
    na, nb = _norm(a), _norm(b)
    seq = max(SequenceMatcher(None, na, nb).ratio(), SequenceMatcher(None, nb, na).ratio())
    return round(max(jac, seq), 3)


def cmd_similar(con, a):
    post = con.execute("SELECT * FROM posts WHERE id=?", (a.post_id,)).fetchone()
    if not post or not post["content_path"]:
        print("ERROR: post chưa có content_path")
        return
    _, body = read_post_file(post["content_path"])
    since = (now_vn() - timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S")
    others = con.execute(
        "SELECT id, slug, channel, content_path FROM posts WHERE id<>? AND content_path IS NOT NULL "
        # có cả 'rejected': bài bị chặn thường được sửa rồi đăng (28/09: similar 41 không thấy bài 39 đang rejected)
        "AND status IN ('review','approved','approved_human','scheduled','published','pending_approval','rejected') "
        "AND COALESCE(published_at, scheduled_at, created_at) >= ?", (a.post_id, since)).fetchall()
    thr = settings()["similarity_threshold"]
    results = []
    for o in others:
        try:
            _, ob = read_post_file(o["content_path"])
        except FileNotFoundError:
            continue
        results.append((similarity(body, ob), o["id"], o["slug"], o["channel"]))
    results.sort(reverse=True)
    for s, oid, slug, ch in results[:5]:
        flag = "  <-- VƯỢT NGƯỠNG" if s > thr else ""
        print(f"{s:.3f}  post {oid} ({ch}) {slug}{flag}")
    top = results[0][0] if results else 0.0
    print(f"MAX={top:.3f} THRESHOLD={thr} → {'FAIL' if top > thr else 'PASS'}")


def moc_gia_con_han(cfg: dict, today) -> tuple[bool, str]:
    """Mốc giá KM7 (`_F1_moc_gia` trong banned_terms.json) còn hạn xác nhận không.
    Cấu hình lỗi → coi như hết hạn (an toàn: mọi con số giá lại bị chặn), không làm hỏng lint."""
    from datetime import date

    try:
        d0 = date.fromisoformat(str(cfg["F1_moc_gia_xac_nhan"]))
        n = int(cfg["F1_moc_gia_han_ngay"])
    except (KeyError, TypeError, ValueError):
        return False, "cấu hình mốc giá lỗi (F1_moc_gia_xac_nhan / F1_moc_gia_han_ngay)"
    if today > d0 + timedelta(days=n):
        return False, f"mốc giá quá hạn xác nhận ({d0.isoformat()} + {n} ngày)"
    return True, ""


def lint_text(text: str, today=None, rules: dict | None = None) -> list[str]:
    """Quét từ cấm/con số giá theo config/banned_terms.json. Trả danh sách lỗi (rỗng = đạt).

    Mốc giá được phép (KM7, khoá `_F1_moc_gia`) chỉ được che khỏi nhóm F1_gia khi còn hạn xác nhận.
    `today` và `rules` chỉ dùng cho kiểm thử (tools/test_lint_gia.py)."""
    import json
    from common import ROOT

    if rules is None:
        rules = json.loads((ROOT / "config" / "banned_terms.json").read_text(encoding="utf-8"))
    today = today or now_vn().date()
    text = unicodedata.normalize("NFC", text)
    f1_text, het_han = text, ""
    moc = rules.get("_F1_moc_gia")
    if moc:
        con_han, het_han = moc_gia_con_han(moc, today)
        if con_han:
            for pat in moc.get("F1_gia_duoc_phep", []):
                f1_text = re.sub(unicodedata.normalize("NFC", pat), "‹MOC_GIA›", f1_text, flags=re.I)
    hits = []
    for group, patterns in rules.items():
        if group.startswith("_"):
            continue
        src = f1_text if group == "F1_gia" else text
        for pat in patterns:
            for m in re.finditer(pat, src, re.I):
                s = max(m.start() - 25, 0)
                hits.append(f"{group}: '{m.group(0)}' … {src[s:m.end() + 25].replace(chr(10), ' ')}")
    if het_han and any(h.startswith("F1_gia:") for h in hits):
        hits.append(f"F1_gia: {het_han} → hỏi người dùng xác nhận lại mốc giá rồi sửa config/banned_terms.json")
    return hits


def cmd_lint(con, a):
    if a.text is not None:
        hits = lint_text(a.text)
    else:
        post = con.execute("SELECT content_path FROM posts WHERE id=?", (a.post_id,)).fetchone()
        if not post or not post["content_path"]:
            print("ERROR: post chưa có content_path")
            return
        hits = lint_text(read_post_file(post["content_path"])[1])
    for h in hits:
        print(h)
    print("FAIL" if hits else "PASS")


def cmd_ab_report(con, a):
    since = (now_vn() - timedelta(days=a.days)).strftime("%Y-%m-%d %H:%M:%S")
    q = """
    WITH p AS (
        SELECT * FROM posts WHERE channel='group' AND arm IN ('A','B')
          AND published_at >= ? AND status IN ('published','pending_approval','removed')
    ),
    lm AS (SELECT post_id, MAX(captured_at) mx FROM metrics GROUP BY post_id),
    m AS (SELECT me.* FROM metrics me JOIN lm ON lm.post_id=me.post_id AND lm.mx=me.captured_at)
    SELECT p.arm,
           COUNT(DISTINCT p.id)                                              AS n_bai,
           ROUND(AVG(COALESCE(m.reactions,0)+3*COALESCE(m.comments,0)+5*COALESCE(m.shares,0)),1) AS score_tb,
           (SELECT COUNT(*) FROM leads l WHERE l.source_post_id IN (SELECT id FROM p p2 WHERE p2.arm=p.arm)) AS leads,
           SUM(CASE WHEN p.status='removed' OR m.alive=0 THEN 1 ELSE 0 END)  AS bi_xoa,
           SUM(CASE WHEN p.status='pending_approval' THEN 1 ELSE 0 END)      AS cho_duyet
    FROM p LEFT JOIN m ON m.post_id=p.id
    GROUP BY p.arm
    """
    print(f"== A/B Group {a.days} ngày ==")
    print_rows(con.execute(q, (since,)))
    print("\n== Sự cố nick theo nhánh ==")
    print_rows(con.execute(
        "SELECT a.arm, a.key, h.event, COUNT(*) n FROM account_health h JOIN accounts a ON a.id=h.account_id "
        "WHERE h.at >= ? AND h.event <> 'ok' GROUP BY 1,2,3", (since,)))


def cmd_run_start(con, a):
    cur = con.execute("INSERT INTO runs(agent,task,started_at) VALUES(?,?,?)", (a.agent, a.task, now_str()))
    con.commit()
    print(cur.lastrowid)


def cmd_run_end(con, a):
    con.execute("UPDATE runs SET finished_at=?, summary=? WHERE id=?", (now_str(), a.summary, a.run_id))
    con.commit()
    print("OK")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("init")
    sp.add_parser("q").add_argument("sql")
    sp.add_parser("x").add_argument("sql")
    sp.add_parser("status")
    p = sp.add_parser("due"); p.add_argument("--date")
    p = sp.add_parser("recent"); p.add_argument("--channel", default="page"); p.add_argument("--days", type=int, default=7)
    p = sp.add_parser("can-post"); p.add_argument("account_id", type=int); p.add_argument("--group", type=int)
    p = sp.add_parser("similar"); p.add_argument("post_id", type=int)
    p = sp.add_parser("lint"); p.add_argument("post_id", type=int, nargs="?"); p.add_argument("--text")
    p = sp.add_parser("ab-report"); p.add_argument("--days", type=int, default=7)
    p = sp.add_parser("task-add"); p.add_argument("--owner", required=True); p.add_argument("--title", required=True)
    p.add_argument("--acceptance", required=True); p.add_argument("--evidence-required", required=True)
    p.add_argument("--inputs"); p.add_argument("--loop", default="inner", choices=["inner", "outer"])
    p = sp.add_parser("task-submit"); p.add_argument("task_id", type=int); p.add_argument("--evidence", required=True)
    p = sp.add_parser("task-verify"); p.add_argument("task_id", type=int); p.add_argument("--verifier", required=True)
    p.add_argument("--verdict", required=True, choices=["pass", "fail"]); p.add_argument("--note", default="")
    p = sp.add_parser("task-close"); p.add_argument("task_id", type=int); p.add_argument("--status", default="done", choices=["done", "dropped", "open"])
    p = sp.add_parser("tasks"); p.add_argument("--id", type=int); p.add_argument("--all", action="store_true")
    p = sp.add_parser("run-start"); p.add_argument("agent"); p.add_argument("task")
    p = sp.add_parser("run-end"); p.add_argument("run_id", type=int); p.add_argument("summary")
    a = ap.parse_args()
    con = connect()
    globals()["cmd_" + a.cmd.replace("-", "_")](con, a)


if __name__ == "__main__":
    main()
