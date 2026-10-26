"""Stop hook: không cho Claude kết thúc lượt nếu dự án đã thay đổi mà workspace/STATE.md chưa được cập nhật.

So sánh thời điểm sửa file: file nào trong các thư mục theo dõi mới hơn STATE.md → chặn, yêu cầu cập nhật STATE.md.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "workspace" / "STATE.md"
WATCH = ["CLAUDE.md", ".claude", "workspace", "config", "tools", "content", "assets", "docs", "evals"]
SKIP_PARTS = {"__pycache__", ".profiles", "data"}
SKIP_FILES = {STATE.resolve()}
TOLERANCE_S = 2  # bỏ qua chênh lệch nhỏ khi 2 file được ghi gần như cùng lúc


def changed_files(since: float) -> list[str]:
    out = []
    for name in WATCH:
        p = ROOT / name
        if not p.exists():
            continue
        files = [p] if p.is_file() else (f for f in p.rglob("*") if f.is_file())
        for f in files:
            if SKIP_PARTS & set(f.relative_to(ROOT).parts) or f.resolve() in SKIP_FILES:
                continue
            if f.stat().st_mtime > since + TOLERANCE_S:
                out.append(str(f.relative_to(ROOT)).replace("\\", "/"))
    return out


def main() -> None:
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        payload = {}
    if payload.get("stop_hook_active"):
        return  # đã nhắc 1 lần trong lượt này, không chặn lặp vô hạn
    since = STATE.stat().st_mtime if STATE.exists() else 0.0
    files = changed_files(since)
    if not files:
        return
    shown = ", ".join(files[:8]) + (f" (+{len(files) - 8} file)" if len(files) > 8 else "")
    print(json.dumps({
        "decision": "block",
        "reason": (
            "Dự án đã thay đổi nhưng workspace/STATE.md chưa cập nhật. File mới hơn STATE.md: "
            f"{shown}. Hãy cập nhật STATE.md (Đang ở đâu, Việc vừa làm, Việc tiếp theo, Nhật ký quyết định nếu có) "
            "rồi mới kết thúc."
        ),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
