# Phân tích chiến dịch group Facebook (25/09 – 11/10/2026)

## 1. Số liệu thật [DỮ LIỆU: data/marketing.db]
| Chỉ số | Con số |
|---|---|
| Bài đã đưa vào nhóm | ~132 (93 hiện công khai, 39 chờ quản trị duyệt, 2 bị gỡ) |
| Tương tác thu được (thích + bình luận) | ~24 thích + 5 bình luận ⇒ **~0,2 tương tác/bài** |
| Bình luận là khách thật | 3/5 (2 bình luận là quảng cáo sửa tivi) |
| Khách để lại số điện thoại | **1** (Ngô Quốc, 0332876975, 07/10 — chưa gọi) |
| Khách nhắn lại | 2 (lead 18, lead 34) — đều từ danh sách người dùng gửi 26/09, **không phải từ bài đăng** |
| Người nhắn mã lead (TS1, YO2…) | 0 |
| Bài nhiều thích nhất | Bài 55 "Con dẫn người yêu về ra mắt?" ở Chợ Bố Hạ (6 thích) — chuyện gia đình, không phải tin dự án |
| Nhóm có bài chờ duyệt > 3 ngày | 17 nhóm (vd Mua Bán Nhà Đất Bắc Giang 145k, 193k) → khả năng bài không bao giờ hiện |

## 2. Insight
1. **Đăng nhiều ≠ có khách.** 16 bài/ngày nhưng gần như 0 khách từ bài. Nút thắt không phải số bài mà là (a) bài có hiện không, (b) người đọc có lý do để lên tiếng không. [DỮ LIỆU]
2. **Bài quảng cáo dự án bị lướt qua ở nhóm chợ; bài chạm chuyện gia đình được thích hơn.** [DỮ LIỆU, mẫu nhỏ]
3. **"Nhắn em chữ XX" không ai dùng.** Người ở quê ngại nhắn người lạ; dễ bình luận hỏi hoặc gọi hơn. [GIẢ THUYẾT — test: bài kết bằng câu hỏi dễ trả lời]
4. **Khách nóng đang tự đăng "cần mua đất" trong chính các nhóm đã vào** — nên chủ động tìm họ thay vì chờ. [GIẢ THUYẾT — test bằng quét thử 20 nhóm]
5. **Trả lời chậm làm mất khách:** 2 khách đã trả lời nhưng nằm chờ nhiều ngày. [DỮ LIỆU]
6. **Nick phụ là người lạ** ⇒ quản trị duyệt chậm, người đọc ít tin. [GIẢ THUYẾT]

## 3. Phương án
- **A. Quét khách mua (đề xuất chính).** Mỗi ngày đọc bảng tin ~20 nhóm địa phương đã vào (chỉ đọc), lọc bài/bình luận có "cần mua đất", "tìm mua", "tìm đất", "tài chính tầm", "1 tỷ", "inbox giá"… ⇒ danh sách: link bài, câu yêu cầu, ngày. Bình luận ngay dưới bài họ (họ đang mời chào) + nhắn 1 tin đúng nhu cầu. Khả thi: đã có `tools/doc_group.py` đọc bảng tin, cần thêm bộ lọc từ khoá. Rủi ro: Facebook hạn chế nếu đọc quá nhiều ⇒ ≤ 20 nhóm/ngày, chạy giờ không đăng bài; dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP) ⇒ chỉ lưu link + nội dung công khai, liên hệ 1 lần đúng nhu cầu họ đăng, không chia sẻ danh sách.
- **B. Môi giới địa phương làm đối tác.** Người hay đăng bán đất quanh Yên Thế/Bố Hạ thường là môi giới, có sẵn khách ⇒ mời cộng tác bán hưởng hoa hồng. [Cần người dùng xác nhận chính sách hoa hồng của CĐT]
- **C. Ít bài hơn, đúng chỗ hơn.** 16 → 6–8 bài/ngày, chỉ nhóm hiện bài ngay; dồn công trả lời bình luận/tin nhắn trong 1 giờ.
- **D. Nội dung kéo bình luận.** Cuối bài 1 câu hỏi dễ trả lời ("Nhà mình đang tìm lô tầm bao nhiêu m²?"); ảnh người thật; video ngắn đi một vòng khu; số 0965 539 599 đưa lên sớm.
- **E. Fanpage + quảng cáo trả tiền** nhắm bán kính ~15 km quanh Yên Thế: đo được chi phí/khách. [Chờ văn bản pháp lý cho chế độ strict]
- **F. Claude tự đọc và trả lời tin khách hằng ngày** (người dùng cho phép 11/10), gắn vào việc 14:10.

## 4. Đổi ngay (rủi ro thấp)
1. Lô 12/10: 8 bài, chỉ nhóm hiện ngay, mỗi bài kết bằng 1 câu hỏi mời bình luận.
2. Bỏ đếm "lead" là bình luận quảng cáo.
3. Nhóm có bài chờ duyệt > 3 ngày ⇒ ưu tiên thấp.
4. Trả lời khách: Claude tự đọc + trả lời theo kịch bản §B.

## 5. Diễn biến 11/10 (sau báo cáo)
- **Nick đăng bài bị Facebook hạn chế gửi tin** ("Xác nhận danh tính… hoạt động bất thường"); không xác nhận được vì là acc không chính chủ ⇒ nick chỉ còn đăng bài, có thể bị khoá hẳn.
- Lead 18 thực ra **chưa trả lời** (công cụ nhắc tin đọc nhầm) ⇒ cần sửa cách đọc "có trả lời".
- Đã đổi: lời mời cuối mọi bài ⇒ **"Gọi hoặc Zalo 0965 539 599, báo mã…"**; tắt mời kết bạn + nhắn tin tự động; vào nhóm 2/ngày; trần **8 bài/ngày**; cuối bài có **câu hỏi dễ trả lời**; xen góc chuyện gia đình.
- Lỗi của Claude: hạ trần tuần xuống 56 làm lịch bỏ 4 bài chiều 11/10 ⇒ đã trả về 112, dời 4 bài sang sáng 13/10.

## 6. Bước tiếp theo
1. **Ngay:** chạy công cụ quét khách đang tìm mua (`tools/tim_khach_mua.py`, chỉ đọc, ≤ 20 nhóm) ⇒ danh sách người đăng "cần mua đất" để gọi/Zalo hoặc bình luận dưới bài họ.
2. **12/10:** 8 bài kiểu mới tự đăng 07:30–20:30.
3. **13/10 sáng:** đo cách mới (bình luận trả lời câu hỏi cuối bài, cuộc gọi báo mã TS21–TS28) so với mức cũ 0,2 tương tác/bài; đặt lại luật cách 3 ngày/nhóm; hạn mức về 70%; lô 13/10 thêm 4 bài (đã có 4 bài dời).
4. **Hướng bền (cần người dùng quyết):** số 0965 539 599 có người trực + Zalo; đăng từ Fanpage chủ đầu tư hoặc nick thật của nhân viên kinh doanh; quảng cáo trả tiền nhắm Yên Thế/Bố Hạ/Nhã Nam/Tân Yên.
