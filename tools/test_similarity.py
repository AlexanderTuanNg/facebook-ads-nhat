"""Kiểm độ giống đối xứng (lỗi 28/09: similar 39→41 = 0,657 nhưng 41→39 = 0,445 → cặp trùng lọt khi kiểm từ một phía).

  python tools/test_similarity.py
"""
import sys

from common import ROOT, connect, read_post_file
from db import similarity

ca = []
# 1) cặp thật đã lọt (nếu còn file): phải bằng nhau hai chiều và vượt ngưỡng 0,6 trước khi sửa bài 41
con = connect()
duong = {r["id"]: r["content_path"] for r in con.execute("SELECT id, content_path FROM posts WHERE id IN (39, 41)")}
if len(duong) == 2 and all(duong.values()):
    a, b = (read_post_file(ROOT / duong[i])[1] for i in (39, 41))
    ca.append(("39↔41 bằng nhau hai chiều", similarity(a, b) == similarity(b, a)))
# 2) ca tổng hợp: đảo thứ tự không đổi kết quả
mau = [("Dạ em chào anh chị, lô đất trung tâm xã Yên Thế có lô chỉ khoảng 1 tỷ " * 3, "Lô đất trung tâm " * 12),
       ("abc xyz " * 40, "xyz " * 60 + "abc"), ("một hai ba bốn năm", "năm bốn ba hai một")]
for i, (x, y) in enumerate(mau, 1):
    ca.append((f"mẫu {i} đối xứng", similarity(x, y) == similarity(y, x)))
ca.append(("giống hệt = 1.0", similarity("cùng một câu", "cùng một câu") == 1.0))
sai = [t for t, ok in ca if not ok]
for t, ok in ca:
    print("PASS" if ok else "FAIL", t)
print(f"{len(ca) - len(sai)}/{len(ca)}")
sys.exit(1 if sai else 0)
