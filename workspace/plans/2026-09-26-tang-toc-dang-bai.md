# Tăng tốc đăng bài: 4 khung/ngày, Claude tự đăng (26/09/2026)

Người dùng (26/09 ~14:4x): "đẩy nhanh tiến độ đăng bài trong hôm nay lên nhé, sáng trưa chiều tối đều phải đăng hết (nma làm sao cho có kế hoạch, theo thuật toán và lách được spam). Bạn tự đăng là ok". Nền: phương án v3 (`2026-09-26-phuong-an-v3.md`, Gemini đã duyệt).

## Mục tiêu
Từ 27/09 ngày nào cũng có bài ở cả 4 khung (sáng 7:00–8:00, trưa 11:30–12:30, chiều 16:30–17:30, tối 20:00–21:00), Claude tự bấm Đăng, không bị Facebook/admin coi là spam, đo lead theo từng bài.

## Nút thắt [DỮ LIỆU, DB 26/09 14:4x]
- Không phải giờ đăng mà là **số group còn được đăng**: luật mỗi group cách ≥ 3 ngày, mới có 11 group đăng được bài thường → tối đa ≈ 3,7 bài/ngày. CN 27/09 chỉ còn 1 group đủ điều kiện (17 Chợ Bố Hạ); 28/09: 1, 5, 17; 29/09: 2, 4, 6, 9, 14, 15, 16.
- 4 nhóm Mua–Bán (3, 11, 12, 13) chứa nhiều bài BĐS nhất (13/15 và 16/16 bài đọc được) nhưng chỉ nhận **tin rao "Bán gì đó"** (ô giá bắt buộc 1 con số).
- Hạn mức đang cài: 9 bài/ngày, **12 bài/tuần (đã dùng 10 tính cả 2 bài tối nay)**, cách 5 phút.
- Nick phụ chạm giới hạn "tin nhắn đang chờ" (26/09 13:02) → **mọi lời mời trong bài/bình luận phải để khách nhắn/gọi mình** (tin khách gửi đến không bị giới hạn), không dựa vào việc mình nhắn khách trước.

## Luật "không bị coi là spam" (đúng luật chơi, không mẹo che giấu)
[NGUỒN Meta spam policy: cấm đăng tần suất rất cao, nội dung lặp lại] ≤ 6 bài/ngày, cách ≥ 20 phút, lệch vài phút khỏi giờ chẵn · mỗi group ≥ 3 ngày · mỗi bài 1 biến thể riêng (similar < 0.6) + xoay ảnh · không link · đúng nội quy group · 2 bài bị gỡ ở 1 group → bỏ group · dừng hết khi có cảnh báo/checkpoint. [NGUỒN KaneMedia] group xếp bài theo tương tác gần đây → trả lời bình luận sớm (người dùng duyệt câu trả lời).

**Gemini duyet_ke_hoach vòng 1 (26/09 ~14:5x): SỬA RỒI DUYỆT** → đã sửa: (1) giữ "mỗi group ≥ 3 ngày"; (2) **bỏ** bài trang cá nhân chiều nay (nick đang bị hạn chế nhắn tin, dễ bị quét là nick chuyên quảng cáo); (3) 4 khung/ngày là đích, **tăng dần theo số group đủ điều kiện** — không phá luật để lấp khung (CN: 1 bài, T2: 3 bài, từ T3 29/09: 4–6 bài nếu kho bài kịp).

## Việc
1. **Hôm nay:** chỉ 2 bài tối của phiên gốc (16 → g2 20:00, 15 → g14 ~20:10); các group còn lại đều đã có bài trong 3 ngày. Bài 17 → g17 dời **CN 27/09 11:40** (compliance góp ý: tránh group Bố Hạ thứ 3 trong ngày). → Kiểm: `fb_group.py stats`, ảnh chụp.
2. **Hạn mức** (`config/settings.json`, sao lưu bản cũ): tuần 12 → 35, ngày 9 → 6, cách 5 → 20 phút. → Kiểm: `db.py can-post`.
3. **Lịch tự đăng trên máy** `tools/lich_dang.py`: đọc bài `approved_human` có giờ hẹn trong ngày, tới giờ thì gọi `fb_group.py autopost` (đã có khoá hồ sơ, can-post, lint, dừng khi CHECKPOINT); lỗi/cảnh báo → dừng cả lịch + báo. Chạy nền mỗi sáng. → Kiểm: chạy thử khô in đúng thứ tự; bài 17 đăng thật CN 11:40.
4. **Kho bài v3 cho 28/09–04/10** (~25 biến thể): tin rao có thông số + giá KM7 + câu F5 + mã lead riêng + ảnh xoay vòng; copywriter → compliance → Claude duyệt thay (đã được giao) → xếp lịch 4 khung. → Kiểm: lint PASS, similar < 0.6, compliance approved.
5. **Tin rao cho 4 nhóm Mua–Bán**: công cụ "Bán gì đó" (tiêu đề, giá, vị trí, mô tả, ảnh). [DỮ LIỆU 26/09 14:5x, xem màn hình thật group 3: "Bán gì đó" → 4 loại; "Nhà cần bán hoặc cho thuê" thực ra là mẫu **cho thuê** (giá mỗi tháng, ngày cho thuê) → không dùng; dùng **"Mặt hàng cần bán"**: Ảnh (bắt buộc, ≤ 42) → Tiêu đề → Giá (1 con số) → Tình trạng (danh sách) → "Xem thêm chi tiết" (mô tả) → Tiếp (bước 2 chưa xem: chọn nơi niêm yết — nếu có Marketplace thì bỏ chọn, chỉ đăng trong nhóm). Ảnh chụp `data/xem_ban_loai1.png`, `data/xem_ban_loai2.png`.] **Cần người dùng: giá chính xác 1 lô rẻ nhất + diện tích.** Có giá → đăng từ CN 27/09 chiều/tối. → Kiểm: 1 tin rao thật hiện trong nhóm.
6. **Thêm group:** người dùng tham gia 7 (BĐS Yên Thế 6,2k), 10 (MB Nhà Đất Bắc Giang 193k) + 8–10 group Claude tìm (danh sách link; nhiều group bắt tích "đồng ý nội quy" → người dùng tự bấm); đăng sau 3 ngày làm quen. → Kiểm: `groups.status = joined`.
7. **Mỗi tối** báo: bài đã đăng / bị gỡ / cảnh báo, lead theo mã bài.

## Xong khi
28/09–04/10: mỗi ngày ≥ 4 bài ở ≥ 3 khung, không cảnh báo/checkpoint, ≤ 1 bài bị gỡ/tuần, có số lead/bài.
