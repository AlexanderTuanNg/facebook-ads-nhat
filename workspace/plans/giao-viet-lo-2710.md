# Giao việc viết lô bài 29/10–03/11/2026 (lịch tuần 27/10, nick David Nguyễn, nhánh B)

Thư mục gốc: `D:\Tuan\12. Tool bán hàng` (chạy `python -X utf8 tools/...` từ đây). Tiếng Việt.

## Đọc trước (BẮT BUỘC, TOÀN BỘ)
- `workspace/the-luat-viet-bai.md` — đọc hết. Mục "CHÍNH SÁCH THÁNG 10 + CÂU GIÁ TỪ 21/10/2026" THAY các mục câu giá/đối tượng cũ (bỏ "CÓ LÔ CHỈ KHOẢNG 1 TỶ", bỏ "CHỈ DƯỚI 1 TỶ"). Giữ "Giọng SALES BĐS", "LỜI MỜI CUỐI TỪ 11/10", mục "NHÓM CỘNG ĐỒNG / HỘI / DOANH NHÂN TỪ 24/10/2026".
- Bài mẫu đã duyệt (chỉ tham khảo khuôn frontmatter, KHÔNG chép câu): `content/2026-10-28/20261028-g7-v6-yt100.md`.

## Thông tin từng bài
`python -X utf8 tools/db.py q "SELECT p.id,p.slug,p.scheduled_at,p.angle,g.name FROM posts p JOIN groups g ON g.id=p.target_id WHERE p.id BETWEEN <a> AND <b> AND p.status='planned' ORDER BY p.id"`
(nếu bảng nhóm tên khác, xem `python -X utf8 tools/db.py q "SELECT name FROM sqlite_master WHERE type='table'"`). Cột angle có [mã XX] và [góc N]. Ảnh: `workspace/plans/anh-bai.json` khoá = id bài, ĐÚNG 3 ảnh, giữ đúng thứ tự, chép NGUYÊN `mo_ta` và `nguon` vào `images_meta`.
Bài cũ cùng nhóm: `python -X utf8 tools/db.py q "SELECT id,content_path FROM posts WHERE target_id=<target_id> AND content_path IS NOT NULL ORDER BY id DESC LIMIT 3"` → đọc để viết khác hẳn.

## Yêu cầu nội dung
- Đối tượng: người mua đất để XÂY NHÀ Ở. Giọng và góc mở theo LOẠI NHÓM đích (đoán từ tên nhóm): quê/xã, chợ/rao vặt, BĐS, đồng hương, cao tuổi, phụ nữ/phụ huynh, doanh nhân/hội nghề (gà đồi…), KCN/nhà trọ, sở thích (Diều Sáo, Nhã Nam reading club: 1 câu nối chủ đề nếu tự nhiên). Góc [góc N] trong thẻ luật chỉ là gợi ý; giọng nhóm ưu tiên.
- Dòng 1 = 1 emoji + ý mở ≤ 4 chữ + "CHỈ VỚI 500 TRIỆU ĐÃ SỞ HỮU LÔ ĐẤT" (tổng ≤ 14 chữ, không tính emoji). Mỗi bài một ý mở khác. Tiêu đề KHÔNG nói mặt đường.
- Thân BẮT BUỘC có nguyên cụm: "trả trước 500 triệu khi ký (lô đến khoảng 1,3 tỷ), phần còn lại chia 4 đợt 15% trong 180 ngày, đợt cuối nhận sổ" ("trả trước 500 triệu" phải đi liền).
- Được nói: tặng 30 tấn xi măng + 2 vạn gạch cho cư dân về ở sớm (không ghi số tiền quy đổi).
- Ưu đãi 2% cư dân Bắc Ninh / 3% thanh toán sớm cho 15 khách đầu tiên đến 31/10/2026: CHỈ cho bài có scheduled_at ≤ 31/10/2026. Bài từ 01/11 TUYỆT ĐỐI không nhắc ưu đãi 2%/3%.
- Nhắc ảnh chung chung (ảnh chính sách, ảnh trao sổ / anh chị khách đã mua nhận sổ 9/10, ảnh khu đất; ảnh tối thì "quảng trường buổi tối"). Không liệt kê "ảnh đầu… ảnh cuối…", không tả cái ảnh không có. Ảnh trao sổ có túi quà/chậu cây thì nói đúng thế.
- Giọng sales xưng "em", gọi anh chị/cả nhà; câu ngắn, xuống dòng; ≤ 4 dòng ✅; câu hỏi mở ở cuối (trước CTA).
- CTA đúng nguyên văn: "Gọi hoặc Zalo 0965.539.599, báo mã XX để nhận bảng giá và vị trí lô." (XX = mã của bài) rồi dòng "#YenTheGoldenHill".
- Thân 50–150 chữ. Bài nhắc mặt đường TL292 phải có "Lô mặt đường giá riêng.".
- CẤM: "nhà nào cũng", "nhiều nhà", "ai cũng", "không ít nhà", mọi khái quát bịa; "thêm một đợt"; chữ phụ thuộc giờ đăng (hôm nay, tối nay, sáng nay, khuya…); "nhất", "duy nhất", "vô tiền khoáng hậu"; trả góp, lãi suất, vay; khoảng cách/thời gian đi lại; "X mình" cho vùng ("Yên Thế mình"…); tả CGV hay phối cảnh là thật; hứa sinh lời/tăng giá/cho thuê; khan hiếm giả; link; số khách nhận sổ; "nhận sổ ngay"; nói thay khách; kể chuyện khách bịa.
- Câu pháp lý nếu dùng thì NGUYÊN VĂN: "đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô".

## Quy trình mỗi bài
1. Ghi `content/<YYYY-MM-DD theo scheduled_at>/<slug>.md` UTF-8 KHÔNG BOM (dùng Python `open(...,'w',encoding='utf-8')`), frontmatter như bài mẫu (post_id, channel: group, target: "<tên nhóm>", arm: B, pillar: du-an, persona, hook_type: tieu-de-gia, cta_type: inbox, ma_lead, goc, key_messages: [KM7c, KM11, ...], images, images_meta, sources).
2. `python -X utf8 tools/db.py x "UPDATE posts SET content_path='content/...md', status='review' WHERE id=<id>"`
3. `python -X utf8 tools/db.py lint <id>` phải PASS; `python -X utf8 tools/db.py similar <id>` MAX < 0,6 (nếu không thì viết lại khác hơn).
Chỉ đụng các bài trong khoảng id được giao. Không sửa code, không sửa config, không đăng bài.

## Báo cáo cho Lead (≤ 800 token)
1 bảng: post_id | mã | dòng đầu | loại nhóm | similar max | ghi chú. Cuối: số PASS / số lỗi chưa sửa được.
