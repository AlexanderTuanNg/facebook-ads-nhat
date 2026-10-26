# Chi phí token của hệ thống (đo thật 25–28/09/2026) và cách tối ưu

**Cách đo:** đọc nhật ký gốc của Claude Code (phiên chính: 518 lượt gọi AI; 16 tác nhân: 831 lượt), cộng 4 loại token của từng lượt rồi nhân giá niêm yết Claude Opus 5.5 (skill claude-api, bảng 2026-06-24): đầu vào $4 · đầu ra $20 · đọc bộ nhớ đệm $0,20 · ghi bộ nhớ đệm 1 giờ ×2 = $8 (5 phút ×1,25) cho mỗi 1 triệu token. Nếu dùng gói thuê bao thì con số USD = mức tiêu hao hạn mức, dùng để so sánh. Script: `scratchpad/do_token.py`, `scratchpad/chi_phi_token.py` (thư mục tạm của phiên).

## 1. Tổng quan
| Phần | Token | Quy ra USD | Tỉ lệ |
|---|---|---|---|
| Phiên chính (Lead: điều phối, sửa code, xem ảnh chụp, duyệt) | 285 triệu | $109,5 | 60% |
| 16 tác nhân (viết bài, kiểm duyệt, nghiên cứu) | 174 triệu | $72,4 | 40% |
| **Cộng 3,5 ngày** | 459 triệu | **$182** | |

97% token là "đọc lại bộ nhớ đệm" (rẻ), nhưng tiền nằm nhiều ở **ghi bộ nhớ đệm** ($65 = 36%, vì loại 1 giờ giá gấp đôi) và **đọc lại** ($90 = 49%).

## 2. Theo ngày (phiên chính)
25/09 $28 · **26/09 $49** (ngày dựng + gỡ lỗi + nhiều ảnh chụp) · 27/09 $16,5 (ngày chạy tự động) · 28/09 đến 10:00 $15,8.

## 3. Theo bài
| Việc | Chi phí/bài | Dao động |
|---|---|---|
| Viết bài (tác nhân) | **$0,47** | $0,26 (lô 16 bài, ít việc) – $0,71 (lô "sáng tạo", 2 tác nhân chồng góc phải viết lại) |
| Kiểm duyệt (tác nhân) | **$0,34** | $0,15 – $0,71 (lô có 2 lần gọi lại tác nhân xem ảnh) |
| **Cộng tác nhân** | **≈ $0,81/bài** | |
| Điều phối của Lead | ≈ $1–2/bài | tuỳ ngày |
→ Một ngày 8 bài hiện tốn ≈ **$20–25** (ngày có sửa code/gỡ lỗi: $50+).

## 4. Thứ tốn nhất
1. **Phiên chính dài**: mỗi bước Lead đọc lại toàn bộ hội thoại (hàng trăm nghìn token); ảnh chụp màn hình, báo cáo dài của tác nhân, file đọc vào đều bị ghi đệm giá $8/triệu rồi đọc lại ở mọi bước sau.
2. **Xem ảnh lặp lại**: mỗi lượt kiểm duyệt mở lại 28–46 ảnh; copywriter mở 3–16 ảnh.
3. **Làm lại**: đổi kiểu tiêu đề sau khi đã duyệt 14 bài (≈ $13); 2 copywriter chạy song song trùng góc phải viết lại 7 bài; gọi lại tác nhân kiểm duyệt cho việc nhỏ (+$1–2/lần vì nạp lại cả ngữ cảnh cũ).
4. **Việc máy làm được mà AI đang làm**: tính mã ảnh, chạy lint/similar, kiểm câu F5, SĐT, thứ tự ảnh.
5. Nghiên cứu (5 tác nhân, ≈ $19) — chi 1 lần, chấp nhận được.

## 5. Phương án tối ưu (xếp theo tiết kiệm ÷ công sức)
| # | Làm gì | Ước tiết kiệm | Ai |
|---|---|---|---|
| 1 | **Mỗi ngày mở phiên mới** (STATE.md giữ trí nhớ), phiên ngắn → Lead đọc lại ít | 50–70% phần Lead | Người dùng mở phiên; Claude khởi động lại lịch |
| 2 | Hạ mức "effort" khi vận hành thường ngày (đang để tối đa), để tối đa khi thiết kế/gỡ lỗi | 20–40% phần Lead | Người dùng chọn trong app |
| 3 | Tác nhân trả báo cáo dạng bảng ngắn (≤ 800 token) | 5–10% | Claude |
| 4 | `tools/kiem_bai.py`: máy tự kiểm lint, độ giống, F5, SĐT, mã lead, hashtag, ảnh (thuộc bộ gốc đã duyệt, thứ tự, mã) → kiểm duyệt AI chỉ xét câu chữ cần phán đoán | kiểm duyệt $0,34 → ~$0,12/bài | Claude |
| 5 | Duyệt **1 lần** bộ 13 ảnh gốc; không mở ảnh từng bài nữa | gồm trong #4 | Claude + compliance |
| 6 | 1 copywriter cho 2–3 ngày bài (16–24 bài), góc không trùng, đọc "thẻ luật" 1 trang thay vì cả playbook/brief/checklist | viết $0,47 → ~$0,25/bài | Claude |
| 7 | Chốt định dạng trước khi viết; việc nhỏ dùng script hoặc tác nhân mới gọn, không gọi lại tác nhân lớn | tránh $10–15 mỗi lần làm lại | Claude |
| 8 | (Người dùng quyết) viết bài bằng Sonnet 5 (rẻ bằng nửa), giữ Opus cho kiểm duyệt | viết thêm −50% | Người dùng |
**Kỳ vọng:** 8 bài/ngày từ ≈ $20–25 xuống ≈ **$7–9/ngày** (−60–70%) mà giữ nguyên chất lượng kiểm duyệt.
