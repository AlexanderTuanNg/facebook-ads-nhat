# Thẻ luật viết bài group — bản gọn cho copywriter (28/09/2026)

Đọc thẻ này THAY cho cả playbook/brief/checklist (tiết kiệm token). Chỉ mở file gốc khi thẻ không nói tới: `workspace/playbook.md` v2.5, `workspace/brief.md`, `workspace/compliance-checklist.md`.

## Dữ kiện được dùng
- Dự án **Yên Thế Golden Hill**, bên mình là chủ đầu tư (Công ty CP Đầu tư và Phát triển Thắng Anh).
- Địa chỉ: **trung tâm xã Yên Thế, thành phố Bắc Ninh (Đồng Lạc cũ)**; có thể nói "Yên Thế (Bắc Giang cũ)". Không ghi sai cấp hành chính.
- 12,1 ha · 377 lô · lô 82–185 m² · có dãy lô mặt đường TL292.
- Thấy trong ảnh flycam (tả được): đường nhựa kẻ vạch, đèn đường, quảng trường, sân chơi (cầu trượt, khung leo), sân thể thao, cây xanh. Ảnh đêm: quảng trường sáng đèn, người ra chơi. Bể cát/tô tượng/xe điện/nhà hơi, bàn ghế trong ảnh đêm là **hàng trò chơi, hàng quán buổi tối, tối nào cũng có** (người dùng xác nhận 28/09 tối) → được tả là có hằng tối, được lên tiêu đề, được dùng "nhộn nhịp"/"đông vui" cho quảng trường buổi tối; gọi là hàng quán/hàng trò chơi, KHÔNG gọi là tiện ích của dự án.
- Câu được dùng: "hiện vẫn có khách giao dịch đều" · "bên chủ đầu tư đưa anh chị đi xem đất trực tiếp" · "mua trực tiếp chủ đầu tư được chiết khấu đến 10% (theo chính sách CĐT)" · "ngân hàng hỗ trợ vay đến 50% giá trị lô" (+ "ngân hàng xét từng hồ sơ").
- Pháp lý, NGUYÊN VĂN: "đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô".
- Hotline **0965 539 599** · hashtag **#YenTheGoldenHill**.

## Luật cứng (máy kiểm bằng `tools/kiem_bai.py` — nếu file chưa có: Lead viết trước lô 04/10; tạm thời chạy lint + similar của `tools/db.py` như cũ)
1. **Dòng 1 = tiêu đề giá** ≤ 14 chữ, VIẾT HOA được + 1 emoji đầu dòng (🔥 📍 ✅ 🏡), mỗi bài một câu khác. Phải có "CÓ LÔ CHỈ KHOẢNG 1 TỶ" hoặc "CHỈ KHOẢNG 1 TỶ LÀ CÓ MỘT LÔ". Bài nhắc mặt đường → "TRONG KHU CÓ LÔ CHỈ KHOẢNG 1 TỶ" và thân có "lô mặt đường giá riêng".
2. Giá nói **đúng 1 lần** (ở tiêu đề). Không số giá khác, không đơn giá/m², không mã lô. Tiêu đề kết thúc "…1 TỶ" thì dòng 2 không mở bằng số đếm (Hai, Ba, Năm…).
3. **Cấm**: "nhất", "rẻ", "siêu rẻ", "giá sốc", "hiếm hoi", "giữ giá", "sầm uất", "chợ đêm", "sẵn khách", hứa tăng giá/lợi nhuận, lãi suất, ưu đãi 48 giờ, trả góp, khoảng cách/tiện ích không có trong ảnh hay brief, kể chuyện khách hư cấu, lịch sử khu đất ("ngày xưa là…"), định kiến giới, link.
4. **Lời mời cuối**: khách tự nhắn/gọi, MÃ đứng trước số: "Nhắn mình chữ XX1 để nhận bảng giá và vị trí lô, hoặc gọi 0965 539 599." Không "comment để mình inbox", không "mình nhắn anh chị".
5. 50–150 chữ (góc 6, 7: tới 170). Giọng người Yên Thế thật (xưng mình, gọi anh chị), không gạch đầu dòng dày, không câu đệm kiểu AI.
6. **Ảnh** (từ 05/10, kho xoay vòng 36 góc ảnh thật, `assets/dong-lac/kho-anh/danh_muc.json`): Lead chạy `python tools/anh_bai.py --post-ids <ids>` (góc 5 kinh tế đêm thêm `--dem-bia <id>` → ảnh đêm làm ảnh ĐẦU; bài từ 19:00 tự có ảnh đêm CUỐI) SAU khi có giờ hẹn + group. Dùng đúng danh sách và thứ tự của bài trong `workspace/plans/anh-bai.json`, **chép NGUYÊN `mo_ta` và `nguon` vào `images_meta`** (không tả thêm cái ảnh không có); câu chữ phải khớp thứ tự ảnh ("ảnh đầu"/"ảnh cuối"). Mỗi bài ảnh khác nhau → không viết câu tả ảnh chung cho cả lô. Bài cũ trước 05/10: `anh-bai-2809.json`.
7. Khác rõ mọi bài khác (similar < 0,6, đo 2 chiều). Bài đăng lại ở cùng group: đọc bài cũ theo mã, viết khác hẳn.

## Góc bài (chi tiết: `workspace/research/2026-09-28-goc-sang-tao.md`)
1 rủ anh em mua gần · 2 hai vợ chồng cùng xem · 3 đất làm nhà cưới cho con · 4 Tết về quê có đất · 5 tối cho con ra quảng trường (ảnh đêm) · 6 dạo flycam ("Ảnh 1: …" đúng từng ảnh) · 7 hỏi–đáp 3–4 cặp · 8 làm KCN về quê · 9 khu dân cư mới · 10 mặt đường TL292 · 11 giao dịch đều + CĐT dẫn xem · 12 người [xã lân cận].

## Quy trình mỗi bài
Viết `content/<YYYY-MM-DD>/<slug>.md` (frontmatter mở/đóng `---`: post_id, channel: group, target, arm: B, pillar: du-an, persona, hook_type: tieu-de-gia, cta_type: inbox, ma_lead, goc, key_messages, images, images_meta) → `python tools/kiem_bai.py <id>` PASS → `python tools/db.py x "UPDATE posts SET content_path='content/...md', status='review' WHERE id=<id>"`.
**Báo cáo cho Lead: 1 bảng ngắn** post_id | mã | dòng đầu | ghi chú (≤ 800 token, không kể lại quy trình).

## Giọng SALES BĐS (người dùng 09/10/2026: "đừng cho AI quá… chân thật, gợi ý, tăng độ tin tưởng… cách mà các sales bđs hay viết") — ÁP DỤNG TỪ 09/10, thay mục 5 khi khác
- Xưng **em**, gọi **anh chị / cả nhà**. CTA: "Nhắn em chữ XX để nhận bảng giá và vị trí lô, hoặc gọi 0965 539 599." (vẫn giữ MÃ đứng trước số).
- Câu ngắn, xuống dòng nhiều, mỗi đoạn 1–2 câu. Được 3–4 dòng ý chính đầu dòng ✅ (không hơn 4), vd "✅ Lô 82 đến 185 m²", "✅ Đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô", "✅ Bên chủ đầu tư đưa anh chị đi xem đất trực tiếp".
- Mở bằng chuyện THẬT (không nói thay khách kiểu "ai cũng…", không "thêm một đợt", không câu phụ thuộc giờ đăng như "hôm nay/khuya rồi/tin cuối ngày"; nói "khách ĐÃ MUA" để khỏi hiểu là mua xong có sổ ngay), có hơi người: "Chúc mừng các anh chị khách hàng đã cầm sổ hôm 9/10 🎉", "Hôm 9/10 bên em trao sổ cho các anh chị đã mua 🎉". Có thể 1–2 emoji trong thân (🎉 🏡 📍 ☎️), không rải emoji mỗi câu.
- **KHÔNG liệt kê ảnh kiểu "ảnh đầu… ảnh thứ hai… ảnh cuối…"** (dấu hiệu máy viết). Chỉ nói gọn "ảnh thật buổi trao sổ hôm 9/10" / "ảnh anh chị khách nhận sổ"; nhưng không câu nào được tả sai ảnh (ảnh văn phòng, túi quà thì không gọi là cảnh cầm sổ).
- Bỏ giọng văn mẫu: không "Không chỉ… mà còn…", không câu triết lý/cảm thán chung, không "hãy", không văn hoa, không giải thích dài sau dấu ":".
- Giọng sales nhưng vẫn giữ mọi luật cứng ở trên: tiêu đề giá dòng 1, giá 1 lần, câu pháp lý nguyên văn, cấm "nhất", "nhận sổ ngay", "sổ đỏ trao tay", không khan hiếm giả ("sắp hết lô", "chỉ còn…"), không hứa tăng giá, không bịa chuyện khách/câu hỏi của nhóm, không nêu số khách nhận sổ.

## ⚠️ LỜI MỜI CUỐI TỪ 11/10/2026 (thay mục 4 và CTA ở mục Giọng SALES)
Nick đăng bài là acc không chính chủ, bị Facebook hạn chế GỬI TIN (không xác nhận danh tính được) → khách nhắn vào nick sẽ KHÔNG ai trả lời.
CTA bắt buộc: "Gọi hoặc Zalo 0965.539.599, báo mã XX để nhận bảng giá và vị trí lô." KHÔNG viết "nhắn em/nhắn mình", "inbox".

## 🎯 ĐỐI TƯỢNG ƯU TIÊN TỪ 14/10/2026 (người dùng: "tập trung nhóm khu công nghiệp và đồng hương trước")
Góc mới, dùng cho ≥ 2/3 số bài (nhóm KCN, nhóm đồng hương, và cả nhóm địa phương vì nhiều thành viên đang làm xa):
- **Góc 13 — công nhân KCN:** vợ chồng đi ca, thuê trọ, dành dụm mua mảnh đất ở quê trước; được nói "ngân hàng hỗ trợ vay đến 50% giá trị lô, ngân hàng xét từng hồ sơ". Câu hỏi cuối: làm ca ngày/đêm, làm KCN nào.
- **Góc 14 — đồng hương xa quê** (Hà Nội, miền Nam, Nhật/Hàn/Đài): tiền gửi về muốn có mảnh đất ở quê; "người nhà ở quê qua xem trước, bên chủ đầu tư đưa đi xem đất trực tiếp". Câu hỏi cuối: đang làm ở đâu/nước nào, Tết có về không.
- **Góc 15 — ông bà/bố mẹ để dành đất cho con cháu.**
CẤM với các góc này: hứa mua từ xa/ký hộ/đứng tên hộ/gọi video chốt; khoảng cách hay thời gian đi tới KCN; "trả góp", lãi suất; khái quát bịa ("nhà nào cũng có người đi Nhật"); "X mình" cho vùng.

## 💰 CÂU GIÁ TỪ 14/10/2026 (thay mục 1, người dùng xác nhận còn lô DƯỚI 1 tỷ)
Dòng 1 = [emoji] + ý mở ≤ 4 chữ + "CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU" (tổng ≤ 14 chữ, emoji không tính). Vd "🏡 LÀM KCN? CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU".
Bài nhắc mặt đường: "TRONG KHU CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU" + thân có "lô mặt đường giá riêng". Giá vẫn nói đúng 1 lần; không "dưới 900 triệu", không giá từng lô.

## 🏠 CHÍNH SÁCH THÁNG 10 + CÂU GIÁ TỪ 21/10/2026 (THAY "CÂU GIÁ TỪ 14/10"; chỉ áp cho nick David Nguyễn — lịch nhóm nhánh B)
- Đối tượng: **người mua để XÂY NHÀ Ở** (gia đình trẻ, bố mẹ làm nhà cho con, người xa quê về làm nhà); nhóm quanh Yên Thế, Bố Hạ, Tân Yên/Nhã Nam. Bỏ góc đầu tư lướt sóng.
- Dòng 1 = [emoji] + ý mở ≤ 4 chữ + **"CHỈ VỚI 500 TRIỆU ĐÃ SỞ HỮU LÔ ĐẤT"** (≤ 14 chữ). Người dùng chọn câu này 21/10 sau khi được báo rủi ro gây hiểu nhầm → **thân bài BẮT BUỘC có câu rõ điều kiện**: "trả trước 500 triệu khi ký (lô đến khoảng 1,3 tỷ), phần còn lại chia 4 đợt 15% trong 180 ngày, đợt cuối nhận sổ".
- Được nói (nguồn: ảnh CSBH `assets/dong-lac/csbh-2110/`): tặng **30 tấn xi măng và 2 vạn gạch** cho cư dân về ở sớm (KHÔNG ghi số tiền quy đổi); **ưu đãi 2% cho cư dân Bắc Ninh**, **3% khi thanh toán sớm**, mỗi loại cho 15 khách đầu tiên, đến 31/10/2026 (đúng mốc, không thêm "sắp hết", không "duy nhất").
- Ảnh 1 = ảnh chính sách có hotline (`assets/dong-lac/csbh-2110/csbh-0965539599.jpg`, bản cắt nhẹ mỗi bài); ảnh sau = ảnh thật khu đất. Không tả CGV, không tả phối cảnh là thật.
- Giữ: CTA gọi/Zalo 0965.539.599 + mã; câu pháp lý nguyên văn; giọng sales; cấm khái quát bịa, "nhất", "duy nhất", "vô tiền khoáng hậu", khoảng cách, trả góp, lãi suất.

## 🏘️ NHÓM CỘNG ĐỒNG / HỘI / DOANH NHÂN TỪ 24/10/2026 (người dùng 23/10: "đăng mạnh hơn các nhóm khác ở yên thế… hội người cao tuổi, hội này hội kia… cả mấy nhóm doanh nhân" → "cứ giữ ở 50% bđs và 50% các nhóm còn lại")
- **Tỉ lệ mỗi ngày: 50% nhóm BĐS/chợ, 50% nhóm khác** (quê/xã, hội, đồng hương, cao tuổi, cựu chiến binh, phụ nữ, doanh nhân, KCN, nhóm sở thích địa phương). `tools/lap_lich_bai.py --ti-le-bds 0.5` (mặc định) tự xen kẽ.
- Mọi luật mục "CHÍNH SÁCH THÁNG 10" vẫn giữ (dòng 1 có "CHỈ VỚI 500 TRIỆU ĐÃ SỞ HỮU LÔ ĐẤT", câu điều kiện, quà, ưu đãi tới 31/10, CTA). Chỉ đổi **giọng và góc mở** cho hợp nhóm:
  - Nhóm quê/xã, "Người Yên Thế": giọng người cùng quê, mở bằng tin thật của dự án (lễ trao sổ 9/10, quảng trường buổi tối đã có người ra chơi), một lời mời, ít chữ in hoa.
  - Đồng hương xa quê (Hà Nội, Sài Gòn, Nhật, Hàn, Đài Loan): về quê làm nhà gần bố mẹ; nhờ người nhà ở quê đi xem đất trước (KHÔNG hứa mua từ xa, KHÔNG nói chuyện chuyển tiền).
  - Cao tuổi, cựu chiến binh: ông bà lo đất cho con cháu làm nhà; nói chậm, rõ, không dồn ép.
  - Phụ nữ, phụ huynh: tổ ấm riêng, con có sân chơi ở quảng trường (chỉ tả cái có trong ảnh/KM3).
  - Doanh nhân, doanh nghiệp: tiền thanh toán giãn 180 ngày nên nhẹ dòng tiền; lô mặt đường TL292 để làm cửa hàng thì PHẢI có "Lô mặt đường giá riêng."; CẤM hứa sinh lời, tăng giá, "đầu tư chắc thắng", cho thuê thu tiền.
  - Công nhân KCN: đi làm xa, có đất làm nhà ở quê; không nói vay, không nói khoảng cách.
  - Nhóm sở thích (diều sáo, đọc sách…): MỘT câu mở nối với chủ đề nhóm nếu tự nhiên được, không gượng; còn lại như nhóm quê.
- Nhóm có nội quy cấm quảng cáo/PR → KHÔNG đăng (đổi nhóm). Nhóm từng gỡ bài → không đăng lại (đã có trong lập lịch).
- Đo sau 5 ngày (29/10): tỉ lệ bài hiện/chờ duyệt/bị gỡ và cuộc gọi theo mã, tách 2 loại nhóm; nhóm cộng đồng bị gỡ > 30% → báo người dùng trước khi đăng tiếp.

- **25/10 người dùng: số điện thoại trong chữ bài viết dạng `0965.539.599`** ("thêm dấu . . . để dễ viral hơn"); ảnh chính sách giữ nguyên. [GIẢ THUYẾT] dấu chấm khó bị bộ lọc số điện thoại của nhóm bắt hơn; rủi ro: Facebook có thể không tự biến thành nút bấm gọi → đo cuộc gọi theo mã.
