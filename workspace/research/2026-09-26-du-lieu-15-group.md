# Dữ liệu thật: bảng tin 15 group mục tiêu (26/09/2026 11:07–11:18)

Nguồn: `tools/doc_group.py --all --scrolls 6` (chỉ đọc, nick đang đăng nhập, bảng tin mặc định "Phù hợp nhất", khoảng 13–18 bài đầu mỗi group) → `data/doc_group_20260926_1107.jsonl` (216 bài). Phân loại bài BĐS bằng từ khoá (đất, nhà, lô, m², thổ cư, sổ, mặt đường, dự án, đấu giá…).

**Giới hạn:** một lần chụp, chỉ bài đầu bảng tin; số tương tác đọc từ chữ trên trang (Facebook xáo cấu trúc chống đọc tự động) nên là số gần đúng — đã loại 1 số sai (431 = 3 số cuối SĐT bị tách dòng). Không đọc được inbox/cuộc gọi, thứ quyết định lead.

## 1. Mỗi group có bao nhiêu bài BĐS (bài BĐS / bài đọc được)
| Group | BĐS | Ghi chú |
|---|---|---|
| 13 Mua bán BĐS Từ Sơn (57k) | 16/16 | nhóm Mua–Bán (không đăng được bài thường) |
| 11 Chợ BĐS Quế Võ (48k) | 13/15 | nhóm Mua–Bán |
| 9 MB Nhà Đất Tân Yên (31k) | 12/16 | đăng được, admin duyệt bài |
| 3 MB Nhà Đất Yên Thế BG (13k) | 11/13 | nhóm Mua–Bán |
| 1 Nhà đất Cụm Yên Thế (20k) | 10/15 | |
| 8 MB Nhà Đất Yên Thế–Tân Yên–Bố Hạ (5,5k) | 10/13 | |
| 4 Nhà Đất Yên Thế–BN (7,3k) | 9/13 | |
| 12 Nhà đất Quế Võ (66,9k) | 4/14 | nhóm Mua–Bán |
| 15 Chợ Quế Võ (207k) · 5 Yên Thế Online (98k) · 14 Chợ Làng Ngà (58k) | 4/15 · 3/13 · 3/18 | group chợ/cộng đồng: ít bài BĐS cạnh tranh |
| 2 Chợ Yên Thế (63k) · 6 CHỢ BỐ HẠ (61k) · 16, 17 Chợ Bố Hạ | 1/14 · 2/13 · 2/15 · 2/13 | |
**Tổng: 102/216 bài (47%) là BĐS.**

## 2. Tương tác công khai của bài BĐS
- Trung vị **0**; **75/102 (74%) không có lượt thích/bình luận/chia sẻ nào**; chỉ 2 bài ≥ 5 (sau khi loại số sai).
- → [DỮ LIỆU] Ở group rao vặt địa phương, like/comment **không phản ánh** nhu cầu; người mua nhắn tin/gọi riêng. **KPI phải là số tin nhắn/lead theo từng bài**, không phải lượt tương tác.

## 3. Bài BĐS điển hình trông thế nào (102 bài)
| Đặc điểm | Tỉ lệ |
|---|---|
| Có ảnh | 89/102 (87%) |
| **≥ 3 ảnh** | 53/102 (52%) |
| Có video | 18/102 (18%) |
| Ghi con số giá | 22/102 (22%) |
| Ghi diện tích cụ thể (m²) | 36/102 (35%) |
| Tiện ích gần (KCN, trường, chợ, Aeon…) | 29/102 (28%) |
| Mặt đường / mặt tiền / trục chính | 27/102 (26%) |
| SĐT ngay trong bài | 16/102 (16%) |
| "Chính chủ" | 15/102 (15%) |
| Sổ / thổ cư / pháp lý | 13/102 (13%) |
| Gấp / cần tiền / ngộp / cắt lỗ / rẻ hơn | 12/102 (12%) |
Ví dụ câu mở hay gặp: "Chính chủ đấu được lô… giờ không gồng nổi lãi, bán cắt lỗ còn 1 tỷ 2", "Lô góc… 2 mặt tiền, trục chính đang đổ áp phan", "Bác nào tài chính nhỉnh tỷ… muốn mua lô trục chính kinh doanh", "Đất 2 mặt đường liên xã, cách cổng trường cấp 3 khoảng 350 m".

## 4. So với bài của mình (9 bài 25–26/09)
- Mình: **1 ảnh** (ảnh AI làm đẹp, ghi "minh hoạ"), phần lớn không ghi diện tích/mặt đường/khoảng cách tiện ích; nhiều bài dạng kiến thức (sổ gốc, giấy tay). Bài BĐS trong group: **nhiều ảnh thật + thông số cụ thể của lô**.
- Group Mua–Bán (3, 11, 12, 13) là nơi tập trung bài BĐS nhất nhưng tool chưa đăng được (chỉ có "Bán gì đó" = tin rao có giá, diện tích, vị trí).

## 5. Gợi ý rút ra (cần đối chiếu với nghiên cứu bên ngoài trước khi chốt)
1. [DỮ LIỆU] Đo bằng lead/inbox theo bài, không đo like → cần cách gắn nguồn lead cho từng bài.
2. [DỮ LIỆU] Chuẩn của chợ: ≥ 3 ảnh thật + thông số cụ thể (diện tích, mặt tiền, đường, khoảng cách tiện ích) → bài 1 ảnh AI kiểu "kiến thức" lạc chuẩn.
3. [GIẢ THUYẾT] Group chợ/cộng đồng lớn (Chợ Quế Võ 207k, Yên Thế Online 98k) ít bài BĐS cạnh tranh → bài dễ nổi hơn, nhưng ý định mua thấp hơn; group chuyên nhà đất có ý định cao nhưng bài trôi nhanh. → cần đo lead theo loại group.
4. [GIẢ THUYẾT] Tin rao đúng định dạng "Bán gì đó" ở 4 nhóm Mua–Bán có thể là kênh lớn nhất chưa khai thác.
