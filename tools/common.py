"""Tiện ích dùng chung: đường dẫn, settings, .env, DB, thời gian VN, đọc file bài viết."""
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "marketing.db"
SCHEMA_PATH = ROOT / "tools" / "schema.sql"
SETTINGS_PATH = ROOT / "config" / "settings.json"
PROFILES_DIR = ROOT / ".profiles"

VN_TZ = timezone(timedelta(hours=7))  # Việt Nam không có DST
TS_FMT = "%Y-%m-%d %H:%M:%S"          # mọi timestamp trong DB: giờ VN, không offset

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except Exception:
        pass


def now_vn() -> datetime:
    return datetime.now(VN_TZ).replace(tzinfo=None)


def now_str() -> str:
    return now_vn().strftime(TS_FMT)


def parse_ts(value: str) -> datetime:
    """Nhận 'YYYY-MM-DD HH:MM[:SS]' (giờ VN) hoặc ISO có offset; trả datetime giờ VN naive."""
    v = value.strip().replace("T", " ")
    if re.search(r"[+-]\d{2}:?\d{2}$|Z$", v):
        dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
        return dt.astimezone(VN_TZ).replace(tzinfo=None)
    for fmt in (TS_FMT, "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(v, fmt)
        except ValueError:
            pass
    raise ValueError(f"Không đọc được thời gian: {value}")


def to_unix(dt_vn: datetime) -> int:
    return int(dt_vn.replace(tzinfo=VN_TZ).timestamp())


def settings() -> dict:
    return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))


def load_env() -> None:
    env = ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con


def read_post_file(path: str | Path) -> tuple[dict, str]:
    """Đọc file content/*.md → (frontmatter dict, nội dung bài)."""
    import yaml

    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        if text.lstrip().startswith("---"):
            # Mở frontmatter mà không đóng → file hỏng; không được coi cả file là thân bài (sẽ đăng nhầm phần khai báo)
            raise ValueError(f"frontmatter chưa đóng (thiếu dòng '---'): {p}")
        return {}, text.strip()
    meta = yaml.safe_load(m.group(1)) or {}
    return meta, m.group(2).strip()


def get_post(con: sqlite3.Connection, post_id: int) -> sqlite3.Row:
    row = con.execute("SELECT * FROM posts WHERE id=?", (post_id,)).fetchone()
    if not row:
        sys.exit(f"ERROR: không có post id {post_id}")
    return row


def update_post(con: sqlite3.Connection, post_id: int, **fields) -> None:
    fields["updated_at"] = now_str()
    cols = ", ".join(f"{k}=?" for k in fields)
    con.execute(f"UPDATE posts SET {cols} WHERE id=?", (*fields.values(), post_id))
    con.commit()


def record_health(con: sqlite3.Connection, account_id: int, event: str, notes: str = "") -> None:
    con.execute(
        "INSERT INTO account_health(account_id, at, event, notes) VALUES(?,?,?,?)",
        (account_id, now_str(), event, notes),
    )
    if event in ("checkpoint", "restricted", "blocked"):
        con.execute("UPDATE accounts SET status='paused' WHERE id=?", (account_id,))
    con.commit()
