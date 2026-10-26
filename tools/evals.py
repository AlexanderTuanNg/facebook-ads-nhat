"""Eval lớp máy: lint phải cho đúng kết quả `expect_lint` ở mọi ca trong evals/compliance/.

  python tools/evals.py            # chạy, in bảng, exit 1 nếu có ca sai
  python tools/evals.py --list     # liệt kê ca cần agent xử lý (expect_lint PASS nhưng expect_agent REJECT)

Lớp agent (compliance có bắt được thông điệp KHOÁ không) chạy qua `/lead eval`.
"""
import argparse
import sys

from common import ROOT, read_post_file
from db import lint_text

CASES = ROOT / "evals" / "compliance"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    files = sorted(CASES.glob("*.md"))
    if not files:
        sys.exit("ERROR: không có ca eval")
    wrong = 0
    for f in files:
        meta, body = read_post_file(f)
        if a.list:
            print(f"{f.name}: lint={meta['expect_lint']} agent={meta['expect_agent']} | {meta.get('why', '')}")
            continue
        got = "FAIL" if lint_text(body) else "PASS"
        ok = got == meta["expect_lint"]
        wrong += not ok
        print(f"{'OK ' if ok else 'SAI'}  {f.name:<32} lint={got:<4} (đáp án {meta['expect_lint']})")
    if not a.list:
        print(f"\nKẾT QUẢ: {len(files) - wrong}/{len(files)} đúng")
        sys.exit(1 if wrong else 0)


if __name__ == "__main__":
    main()
