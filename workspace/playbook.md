# PLAYBOOK: v2.6 (2026-09-28): dự án KDC Đồng Lạc (tên thương mại: Yên Thế Golden Hill)

> Chỉ Lead sửa file này. Mỗi thay đổi tăng version và ghi vào bảng `playbook_changes`.
> v2: chuyển từ khung chung sang dự án Đồng Lạc (vai CĐT, không nêu giá, Page là kênh chính, tắt nhánh B).
> v2.1 (25/09): tên trên bài/comment = **Yên Thế Golden Hill** (Q1, người dùng chốt), hashtag `#YenTheGoldenHill`; KM6 vay 50%: người dùng xác nhận có thật.
> v2.6 (28/09 tối): KM3 mở phần quảng trường buổi tối ("tối nào cũng có hàng trò chơi, hàng quán", người dùng xác nhận); lô từ 04/10 lấy **kinh tế đêm** làm góc chính (≥ 1/2 số bài, ảnh đêm làm bìa cho bài góc này); ưu tiên nhóm mới vào (Hữu Lũng/vùng giáp). Người dùng: "đẩy mạnh đăng bài kinh tế đêm đi".
> v2.5 (28/09): §7 DÒNG ĐẦU = TIÊU ĐỀ GIÁ, ngắn và "đập vào mắt" (người dùng: "headline giá và punchy ở ngay dòng đầu tiên"); ảnh: ≥ 3 ảnh THẬT mỗi bài (flycam + ảnh đêm quảng trường, `tools/anh_bai.py`), bỏ ảnh minh hoạ AI; tần suất 8 bài/ngày, cách ≥ 25 phút.
> v2.4 (26/09): §8 câu trả lời comment hỏi giá: "có lô chỉ khoảng 1 tỷ" (bỏ "khoảng 1 tỷ một lô"), lô mặt đường không đáp khoảng 1 tỷ; mọi lời mời (bài, comment) để khách nhắn/gọi mình kèm mã bài (nick chạm giới hạn nhắn người lạ). Nguồn: compliance duyệt bài 19–27.
> v2.3 (25/09): §7 giọng người thật (bỏ giọng chuyên gia, danh sách dấu hiệu AI cần tránh, bài nào cũng kết bằng lời mời); giá chung chung KM7 "chỉ khoảng 1 tỷ" trên bài và comment hỏi giá (§8); mồi tương tác thử ≤ 1/3 số bài/tuần.
> v2.2 (25/09): nick chính xưng "mình làm bên chủ đầu tư" (người dùng xác nhận không phải nhân viên kinh doanh); không kể trải nghiệm cá nhân chưa có căn cứ; địa danh: huyện Yên Thế cũ nay là 4 xã và phường Bố Hạ (NQ 388/NQ-UBTVQH16, từ 20/9/2026), dự án ở xã Yên Thế.

## 0a. ĐANG CHẠY CHẾ ĐỘ TEST (2026-09-23)
`compliance_mode = test`: mọi pillar (kể cả `du-an`, `uy-tin`) và thông điệp KM1–KM6 đều được dùng (đúng câu chữ checklist §G), group được đăng bằng nick cá nhân qua nhánh A. Mục §0 bên dưới chỉ áp dụng khi quay về `strict`.
Mục tiêu test 2 tuần: tìm pillar/hook/kênh ra inbox tốt nhất, chưa tối ưu pháp lý.
**Kênh đang test: group bằng nick cá nhân (chưa có Page).** Nên:
- Giọng: người thật xưng "mình", **làm bên chủ đầu tư** (người dùng xác nhận 25/09: không viết "nhân viên kinh doanh"), chia sẻ; không xưng "Yên Thế Golden Hill" như Page. Không bịa trải nghiệm cá nhân (kiểu "khách hay hỏi mình…", "mình ngồi bàn công chứng thường xuyên") khi chưa có dữ liệu hoặc người dùng chưa xác nhận.
- CTA: "inbox mình" hoặc "gọi/Zalo 0965 539 599". **Không** viết "nhắn tin Page".
- Group nick đã là thành viên lâu (có lịch sử tương tác) được đăng ngay, không cần warm-up.
- Group mới vào (chế độ test): **warm-up 3 ngày** (like/comment hữu ích 2–3 lần/ngày, tay người dùng), bài đầu là kiến thức/tương tác, từ bài thứ 2 mới nhắc dự án. Xin vào tối đa 5 group/đợt, cách nhau 2–3 ngày.

## 0. (Chế độ strict) Giai đoạn "Khởi động khi còn thiếu tư liệu"
Trong `compliance-checklist.md` §G, phần lớn thông điệp đang **KHOÁ**. Cho tới khi có dòng pháp lý (PL):
- Chỉ đăng **bài kiến thức chung** và **bài tương tác địa phương** (không nêu tên dự án).
- Mục tiêu giai đoạn này: nuôi Page, thu thập người quan tâm khu vực Yên Thế, chưa chào bán.
- Mỗi khi người dùng mở khoá một thông điệp, Lead tăng version playbook và bổ sung pillar tương ứng.

## 1. Kênh & tần suất (mỗi tuần)
- **Fanpage (kênh chính)**: 5–7 bài.
- **Group, nhánh A (nick_chinh, người bấm Đăng)**: tối đa 3 bài/tuần, group đã warm-up (tuần đầu chỉ tương tác). Ở chế độ test không cần số chứng chỉ; ở strict cần (F9). Group cho phép Page tham gia thì ưu tiên đăng dưới tên Page.
- **Nhánh B (nick_phu_1)**: **TẮT** theo khuyến nghị trong brief §5 (uy tín CĐT). Không lên lịch bài nhánh B.

## 2. Tỉ lệ pillar
| Pillar (mã) | Tỉ lệ | Mô tả | Trạng thái |
|---|---|---|---|
| kien-thuc | 35% | Kinh nghiệm mua đất nền an toàn: kiểm tra pháp lý, hợp đồng công chứng, sang tên GCN, vay mua đất; kiến thức chung, không nêu tên dự án | MỞ |
| dia-phuong | 20% | Yên Thế, Bắc Ninh: đời sống, hạ tầng, tin tức thành phố trực thuộc trung ương (có nguồn chính thống) | MỞ |
| du-an | 25% | Quy mô 12,1 ha – 377 lô, mua trực tiếp CĐT, CTA nhận bảng giá | Cần PL (+ KM2/KM3/KM4 theo §G) |
| uy-tin | 10% | Hậu trường CĐT, ký công chứng/bàn giao sổ (ẩn thông tin khách, có đồng ý) | Cần ảnh thật + PL |
| tuong-tac | 10% | Hỏi đáp: "Anh chị ở Yên Thế đang tìm đất làm nhà hay mặt bằng kinh doanh?" | MỞ |

Pillar còn khoá thì chuyển tỉ lệ sang kien-thuc / dia-phuong / tuong-tac.

## 3. Persona ưu tiên
1. `mua-o-lan-dau`: hộ trẻ tại Yên Thế và vùng lân cận, cần đất làm nhà.
2. `kinh-doanh-dia-phuong`: tiểu thương cần mặt bằng buổi tối.
3. `nha-dau-tu-f0` / `nha-dau-tu-lon`: tỉ trọng thấp hơn; tuyệt đối không nói lợi nhuận/tăng giá.
Ngân sách trong bảng persona **chỉ để định hướng nội dung**, không bao giờ xuất hiện trong bài.

## 4. Khung giờ (giờ VN)
- Page: 11:30–12:30, 19:30–21:00 (người dân địa phương xem điện thoại buổi tối)
- Group: 12:00–13:00, 20:00–21:30

## 5. Công thức hook (hook_type)
- `cau-hoi`: "Mua đất nền, làm sao biết lô đó sang tên được hay không?"
- `canh-bao`: "3 dấu hiệu lô đất 'giấy tay' anh chị nên tránh"
- `danh-sach`: "5 giấy tờ cần xem trước khi ký hợp đồng chuyển nhượng"
- `dia-phuong`: mở đầu bằng hình ảnh/sự kiện quen thuộc ở Yên Thế
- `cau-chuyen`: tình huống người mua (ẩn danh, có thật)
Cấm hook dạng số liệu giá hoặc so sánh giá.

## 6. CTA (cta_type)
- `goi-nhan-tin`: "Nhắn tin Page hoặc gọi 0965 539 599 để nhận bảng giá và chính sách" (KM5: CTA chuẩn cho bài dự án)
- `inbox-tai-lieu`: "Inbox Page để nhận checklist kiểm tra pháp lý đất nền" (bài kiến thức, thu lead mềm)
- `comment`: câu hỏi mở cho bài tương tác
- `none`

## 7. Giọng văn
**Dòng đầu (v2.5, 28/09):** dòng 1 là tiêu đề giá ≤ 14 chữ, có thể VIẾT HOA và 1 emoji đầu dòng (🔥 📍 ✅), mỗi bài một câu khác. Bắt buộc có mốc KM7 đúng dạng: "CÓ LÔ CHỈ KHOẢNG 1 TỶ" / "CHỈ KHOẢNG 1 TỶ LÀ CÓ MỘT LÔ" (lint cho qua cả chữ hoa); bài nói lô mặt đường TL292 → "TRONG KHU CÓ LÔ CHỈ KHOẢNG 1 TỶ". CẤM: "1 tỷ" thiếu khoảng/tầm/cỡ/chừng, "khoảng 1 tỷ một lô", "nhất", "siêu rẻ", "rẻ", "giá sốc", hứa tăng giá. Chiết khấu trên tiêu đề phải đủ "đến 10% (theo chính sách CĐT)". Thân bài không nhắc lại câu giá lần 2. Nếu tiêu đề kết thúc bằng "…1 TỶ" thì dòng 2 KHÔNG mở đầu bằng số đếm ("Hai", "Ba", "Năm"…): lint đọc thành "1 tỷ hai" (= 1,2 tỷ) và chặn (copywriter phát hiện 28/09). Ví dụ: "🔥 CÓ LÔ CHỈ KHOẢNG 1 TỶ NGAY TRUNG TÂM XÃ YÊN THẾ" · "📍 Trung tâm xã Yên Thế: có lô chỉ khoảng 1 tỷ, mua thẳng chủ đầu tư".

**Giọng người thật (v2.3, 25/09; người dùng: "giọng điệu các caption vẫn còn AI lắm và nghe không được thật tình"):** viết như một người Yên Thế làm bên chủ đầu tư đang nói chuyện với bà con trong group, không như chuyên gia viết bài.
- Ngắn 50–150 chữ, câu ngắn, từ đời thường ("bên mình", "lô này", "qua xem thử"), xuống dòng như nhắn tin. Dòng đầu là cái móc cụ thể: giá KM7 "chỉ khoảng 1 tỷ", một chi tiết thật ở Yên Thế, hoặc câu người mua hay hỏi thật.
- **Tránh dấu hiệu AI:** liệt kê "Một là/Hai là/Ba là", mũi tên "→", ✅ dày đặc, 3 ý cân đối tăm tắp, dấu hai chấm và gạch ngang dài liên tục, hỏi tu từ rồi tự trả lời, câu rào đón ("nói rõ để anh chị yên tâm", "không nói mập mờ", "mình không dám hứa thay anh chị"), câu kết đạo lý ("…mà để hai bên yên tâm"), "anh chị" lặp quá 2 lần.
- Mỗi bài 1 ý + 1 lời mời rõ (inbox / gọi 0965 539 599). Bài kiến thức vẫn kết bằng 1 câu nhắc dự án + giá KM7 + lời mời (bài nào cũng phải kéo khách).
- Group (nick cá nhân): không chữ ký, emoji ≤ 2, hashtag ≤ 1 (`#YenTheGoldenHill` khi nhắc dự án). Page: xưng "Yên Thế Golden Hill"/"Chủ đầu tư", 80–200 chữ, hashtag ≤ 3, cuối bài dự án có dòng PL (khi mở) + "CĐT: Công ty CP Đầu tư và Phát triển Thắng Anh" + SĐT.
- Chỉ nói điều có thật (brief, người dùng xác nhận); không bịa trải nghiệm, khách, giao dịch.

## 8. Kịch bản trả lời comment
- Hỏi giá (v2.4, 26/09): "Dạ có lô chỉ khoảng 1 tỷ anh/chị {tên} ạ, mỗi lô giá khác nhau theo vị trí. Anh/chị nhắn mình chữ {mã bài} để nhận bảng giá chi tiết, hoặc gọi 0965 539 599 ạ." (chỉ mốc KM7, viết "có lô chỉ khoảng 1 tỷ", KHÔNG "khoảng 1 tỷ một lô"; hỏi giá lô mặt đường TL292 → không đáp khoảng 1 tỷ, chỉ mời nhắn/gọi nhận bảng giá; không nêu giá lô/đơn giá, không bàn giá qua lại trên comment; không hứa "mình nhắn anh/chị" vì nick chạm giới hạn nhắn người lạ 26/09 — luôn để khách nhắn/gọi mình)
- Hỏi pháp lý: chỉ dùng câu chuẩn F5; nếu PL còn KHOÁ thì trả lời "CĐT xin gửi hồ sơ pháp lý chi tiết qua tin nhắn ạ".
- Hỏi vay: KM6 còn KHOÁ thì "CĐT sẽ tư vấn phương án tài chính qua tin nhắn ạ"; không nêu tỉ lệ/lãi suất.
- Tiêu cực / hỏi về nợ, thế chấp, tranh chấp: **không trả lời tự động**, chuyển người dùng.

## 9. Kịch bản inbox (theo giai đoạn)
1. Cảm ơn, hỏi nhu cầu: làm nhà ở hay kinh doanh, hay đầu tư giữ tài sản
2. Hỏi diện tích mong muốn (82–185 m²), mặt đường TL 292 hay trong khu, ngân sách
3. Phòng KD gửi bảng giá 1-1 + chính sách (chỉ lô trong danh sách quỹ lô còn bán)
4. Hẹn xem thực tế (ưu tiên buổi tối, để khách thấy tuyến phố)
→ Lead đạt chuẩn = có SĐT + lô/dãy quan tâm + ngân sách, đã được Phòng KD gọi xác minh.

## 10. Thử nghiệm đang chạy
- A/B nhánh Group: **tạm dừng** (nhánh B tắt theo brief). Thay bằng thử nghiệm: hook `canh-bao` vs `cau-hoi` trên bài kiến thức (so theo inbox/bài).
