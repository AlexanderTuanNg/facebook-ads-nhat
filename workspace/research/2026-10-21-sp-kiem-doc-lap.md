# Kiểm độc lập SP-1, SP-2, SP-3: 16/22 khớp; lỗi đáng sửa nhất là chi phí AI xấu nhất 8,6 triệu (tóm tắt SP-3 ghi 4,6) làm lãi M1 có thể âm

> **Dòng đầu:** lập 21/10/2026 · người kiểm độc lập (không viết 3 file) · **đã mở 20 trang, mở được nội dung cần ở 16 trang** (4 trang không ra chữ: Công báo và Cổng Chính phủ chỉ có thông tin tệp NĐ 356; bản PDF NĐ 356 là ảnh quét; vbpl NĐ 330 tải bằng JavaScript) · 5 lượt tìm · chỉ WebSearch, WebFetch và đọc file; không trình duyệt, không chạy script, không tác nhân con.
> Lưu ý chung: WebFetch trả bản tóm do một mô hình nhỏ đọc trang, không phải nguyên văn. Các trích dẫn dưới đây là đoạn ngắn mô hình đó chép lại.
> Không trang nào có câu ra lệnh cho AI.

## 1. Tóm tắt

1. **22 dữ kiện kiểm: 16 KHỚP · 3 LỆCH · 2 NÓI QUÁ · 1 KHÔNG MỞ ĐƯỢC.** Phần luật chơi Meta, Zalo, Anthropic (SP-2, SP-3) gần như đúng hết với nguồn gốc.
2. **Lỗi đổi quyết định số 1 (nhất quán, SP-3):** tóm tắt ghi chi phí AI "tới ~4,6 triệu nếu toàn Opus", nhưng bảng mục 3.3e tính ra **≈ 330 USD ≈ 8,6 triệu**. Với 8,6 triệu, lãi mô hình giá M1 của SP-1 thành **≈ −0,5 triệu/tháng** (11 − 8,6 − 2,5 − 0,4) [ƯỚC TÍNH].
3. **Lỗi số 2 (NÓI QUÁ, SP-1 D15):** SP-1 ghi Meta Business Agent "miễn phí". Bài TechCrunch mà SP-1 dẫn nói Meta **sẽ thu phí** qua gói WhatsApp Business Premium và theo token. Trang Meta (SP-2 M14) chỉ nói "bắt đầu miễn phí", gói trả phí sắp có. Hướng kết luận "Meta làm thay lớp trả lời" vẫn đúng, nhưng không được nói "cho không".
4. **Lỗi số 3 (LỆCH, số nội bộ SP-1):** quỹ marketing 2,9 tỷ là **≈ 2,9% doanh thu**, không phải 4%. Kế hoạch v2 ghi giá lô bình quân 1,39 tỷ (72 lô ≈ 100 tỷ), SP-1 lại tính 72 × 1 tỷ. Hoa hồng 4% theo v2 là ~56 triệu/lô, không phải 40 triệu. Không đổi hướng, chỉ đổi số.
5. **Pháp lý dữ liệu (SP-2 R2) chưa kiểm lại được trên văn bản gốc:** Giấy chứng nhận Bộ Công an và ≥ 3 nhân sự có báo luật nhắc tới. Mức phạt 50–80 triệu thì lượt tìm hôm nay không thấy nguồn nào nhắc. Đây là điều kiện SP-2 gọi là "nặng nhất", nên **giữ nhãn "cần luật sư xác nhận"**.
6. xAI chỉ **ngừng hỗ trợ** đường tương thích Anthropic (vẫn còn trong tài liệu), không phải "đã bỏ hoàn toàn". Hệ quả "không dựa vào đường này" vẫn giữ.
7. Số nội bộ khác đều khớp: 203 bài → 1 SĐT, `tools/db.py` 386 dòng, 8/25 file `tools/*.py` có chữ riêng Yên Thế, QC 48 triệu gánh 5/60 HĐ.

## 2. Bảng kiểm

| # | Dữ kiện (file, dòng) | Kết luận | Bằng chứng (link, trích ngắn) |
|---|---|---|---|
| 1 | SP-2 M10 (dòng 36): Groups API bỏ ở v19 (23/01/2024), gỡ sau 90 ngày, gồm `publish_to_groups` | **KHỚP** | developers.facebook.com/blog/post/2024/01/23/introducing-facebook-graph-and-marketing-api-v19/ — "API Nhóm Facebook sẽ ngừng hoạt động trong phiên bản 19" |
| 2 | SP-2 M9 (dòng 35; tóm tắt dòng 13 ghi nhầm "M8"): cấm truy cập tự động khi chưa được phép (3.2); một tài khoản, dùng cho mục đích cá nhân (3.1); hiệu lực 01/01/2025 | **KHỚP** (số hiệu dẫn ở tóm tắt sai, xem mục 3) | facebook.com/terms.php — "không được truy cập hoặc thu thập dữ liệu… bằng các phương tiện tự động" |
| 3 | SP-2 M12 (dòng 38): cấm app thu thập thông tin đăng nhập (6.a.iii); Tech Provider làm theo chỉ dẫn khách (5.b.ii.1); cập nhật 03/02/2026 | **KHỚP** | developers.facebook.com/terms/ — "không được yêu cầu hoặc thu thập riêng thông tin đăng nhập" |
| 4 | SP-2 M13 (dòng 39): Meta Ads AI Connectors bản thử công khai 29/04/2026; không cần thông tin lập trình viên; cập nhật 16/07/2026 cho người toàn quyền danh mục đặt luật cho AI | **KHỚP** | facebook.com/business/news/meta-ads-ai-connectors — "open beta"; "no developer credentials, API setup, or coding required" |
| 5 | SP-2 M14 (dòng 40): Business Agent 03/06/2026, kích hoạt miễn phí hiện tại, gói trả phí sắp có, > 1 triệu doanh nghiệp, không nêu nước | **KHỚP** | about.fb.com/news/2026/06/meta-business-agent/ — "getting started is free"; "paid subscription offerings" |
| 6 | SP-2 M2 (dòng 28): Limited "không dành cho app chạy cho nhà quảng cáo thật"; Full cần ≥ 500 lệnh/15 ngày, lỗi < 15% | **KHỚP** | developers.facebook.com/docs/marketing-api/get-started/authorization — "Not for production apps running for live advertisers" |
| 7 | SP-1 D14 (dòng 48): 06/10/2026, video từ ảnh mở cho mọi người; trợ lý thêm tạo mẫu, sửa đối tượng, đổi ngân sách; mở rộng Meta Ads MCP cho công cụ AI bên thứ ba | **KHỚP** (ghi chú: nguồn không nói trợ lý "đang thử"; phần "đang thử" là báo cáo định kỳ) | socialmediatoday.com/news/meta-introduces-new-ai-powered-tools-at-ad-week-2026/832288/ — "generally available"; "expanded its Meta Ads MCP server" |
| 8 | SP-1 tóm tắt ý 7 (dòng 22) và bảng 3.5 (dòng 129): trợ lý trả lời khách "miễn phí" trên WhatsApp/Instagram toàn cầu (D15) | **NÓI QUÁ** | techcrunch.com/2026/06/03/… — Meta định "charge businesses for using this AI agent"; toàn cầu là WhatsApp, Instagram mới thêm vào tin nhắn |
| 9 | SP-3 D1 (dòng 39): điều khoản cá nhân (08/10/2025) cấm bot, script trừ khi dùng API key hoặc được cho phép rõ; cấm bán lại | **KHỚP** | anthropic.com/legal/consumer-terms — "Except when you are accessing our Services via an Anthropic API Key" |
| 10 | SP-3 D2 (dòng 40): bên thứ ba không được cung cấp đăng nhập claude.ai cho sản phẩm, kể cả agent dựng bằng Agent SDK; Agent SDK chịu Điều khoản thương mại | **KHỚP** | code.claude.com/docs/en/agent-sdk/overview — "does not allow third party developers to offer claude.ai login" |
| 11 | SP-3 D10 (dòng 48) và tóm tắt ý 4 (dòng 24): xAI "đã bỏ hoàn toàn" đường tương thích Anthropic | **NÓI QUÁ** | docs.x.ai/developers/rest-api-reference/inference/legacy — "The Anthropic SDK compatibility is fully deprecated" (ngừng hỗ trợ, chưa ghi ngày gỡ) |
| 12 | SP-3 D11 (dòng 49): API Muse Spark 1.1 giá 1,25/4,25 USD, chỉ mở cho lập trình viên ở Mỹ | **LỆCH** (dữ kiện cũ) | dev.meta.ai/docs/pricing-rate-limits — nay có 1.2, 1.3 và chế độ Contributor 0,10/0,20 USD; trang không nêu giới hạn nước. Giới hạn Mỹ chỉ thấy ở báo 07/2026 (NGUỒN-TRÍCH) |
| 13 | SP-2 R2 (dòng 56) và tóm tắt ý 8: "dịch vụ xử lý dữ liệu cá nhân" cần Giấy chứng nhận Bộ Công an, ≥ 3 nhân sự, thiếu giấy phạt 50–80 triệu (NĐ 356 Điều 21–25; NĐ 330 Điều 59) | **KHÔNG MỞ ĐƯỢC** | congbao.chinhphu.vn/van-ban/nghi-dinh-so-356-2025-nd-cp-468371.htm và vanban.chinhphu.vn (chỉ thông tin tệp); datafiles.chinhphu.vn/…/356-nd.signed.pdf (ảnh quét); vbpl NĐ 330 (không ra chữ). Báo luật (lsvn.vn) nhắc giấy chứng nhận và 03 nhân sự; mức 50–80 triệu không thấy nguồn nào nhắc |
| 14 | SP-2 Z6 (dòng 50): phải có gói Tăng trưởng 2,5 tr/năm (hoặc Toàn diện) mới nối API; 100 lệnh/phút; 3 app | **KHỚP** | zalo.solutions/oa/pricing — "cần sử dụng Gói tăng trưởng hoặc toàn diện" |
| 15 | SP-2 Z5 (dòng 49): nhắn tư vấn qua OpenAPI trong 07 ngày (trang quản lý 365 ngày); miễn phí 48 giờ | **KHỚP** | oa.zalo.me/home/documents/guides/tin-tu-van — "trong vòng 07 ngày kể từ tương tác cuối" |
| 16 | SP-1 D4 (dòng 37): agency Wifim 4 tr (< 20 tr ngân sách), 6,5 tr (< 60 tr), 9 tr, 14 tr; có dòng "10% ngân sách" | **KHỚP** (trang 108.850 ký tự, đọc 100.000; nhãn "toàn văn" hơi mạnh) | wifim.vn/dich-vu-quang-cao-facebook/ — bảng "FB Ads Cơ Bản < 20.000.000 · 4.000.000đ" |
| 17 | SP-1 D10 (dòng 43): ATP Cookie bị Chongluadao phát hiện lấy cookie Facebook, Zalo gửi về máy chủ; công ty nhận lỗi thiết kế, khuyên gỡ (04/07/2023) | **KHỚP** | tech.zingnews.vn/…-post1444841.html — "nhận lỗi trong việc thiết kế phần mềm"; công ty phủ nhận cố ý lưu cookie |
| 18 | SP-1 tóm tắt ý 2, mục 3.1 (dòng 17, 69): quỹ marketing 2,9 tỷ "≈ 4% doanh thu" (tính 72 lô × ~1 tỷ) | **LỆCH** | Kế hoạch v2 dòng 148–150: lô bình quân 1,39 tỷ; 39 + ~60 tỷ ≈ 99 tỷ → 2,9 tỷ ≈ **2,9%** [ƯỚC TÍNH] |
| 19 | SP-1 dòng 17, 73: hoa hồng 4–6% "≈ 40–60 tr/lô" | **LỆCH** | Kế hoạch v2 dòng 56: "Đề xuất 4% (~56tr/lô)" → 4–6% ≈ 56–83 tr/lô |
| 20 | SP-1 D1: QC Meta 48 tr, gánh 5/60 HĐ, kênh miễn phí ~90%, hoa hồng đề xuất 4% (đội cũ 6%), quỹ 2,9 tỷ | **KHỚP** | Kế hoạch v2 dòng 13, 15 ("quảng cáo **5**"), 33, 247 ("quỹ marketing 2,9 tỷ"), 258 |
| 21 | SP-1 D1b, SP-2 R6: 203 bài/79 nhóm → 1 SĐT | **KHỚP** | `workspace/research/2026-10-20-hoc-tu-nhom-david.md` dòng 7–8: "203 bài vào 79 nhóm"; "1 người để lại SĐT" |
| 22 | SP-3 D20, D21: `tools/db.py` 386 dòng; 8/25 file `tools/*.py` có chữ riêng Yên Thế | **KHỚP** | Đếm lại 21/10: db.py 386 dòng; 25 file .py; 8 file trúng: ket_ban, lap_lich_bai, loc_nhom, nhan_tin, tim_nhom, vao_nhom, test_lint_gia, test_similarity |

## 3. Nhất quán

**Trong từng file**
1. **SP-3, chi phí AI (lệch, đổi quyết định):** tóm tắt ý 5 (dòng 25) ghi "1–2 triệu với Sonnet 5.5, tới ~4,6 triệu nếu toàn Opus". Bảng mục 3.3e (dòng 162) và dòng 168 ghi **≈ 46 USD ≈ 1,2 triệu** (Sonnet) và **≈ 330 USD ≈ 8,6 triệu** (toàn Opus, trần xấu nhất). Con số 4,6 triệu không có trong bảng. Mục 3.4 (dòng 183) và "kịch bản giữa" (dòng 165) lại dùng 1,5–2,5 triệu. Đã cộng lại bảng: 173 + 90 + 26 + 42 ≈ 331 USD, tức 8,6 triệu là đúng; **tóm tắt sai**.
2. **SP-2, dẫn số hiệu:** tóm tắt ý 4 (dòng 13) dẫn "(M8)" cho điều khoản cấm truy cập tự động; đúng ra là **M9** (M8 là luật báo khách đang nói với bot của Messenger). Đề bài kiểm độc lập cũng chép theo chữ "M8" này.
3. **SP-2, nhãn ĐÃ ĐỌC TOÀN VĂN:** dòng 6 tự định nghĩa nhãn là "mở nguồn và đọc phần được dẫn", tức nghĩa hẹp hơn chương trình (mục 3 luật 6). L1 ghi "ĐÃ ĐỌC TOÀN VĂN Điều 1, 2, 3, 25–28, 43": đây là đọc một phần. L3 và R2 gắn "ĐÃ ĐỌC TOÀN VĂN" nhưng hôm nay không mở lại (dùng lại SU-4, NC-A); L3 còn được tính vào "20 nguồn đọc trọn".
4. **SP-2, mục 4 (dòng 125):** "không cần app, không cần App Review (M13)". Trang M13 chỉ nói không cần thông tin lập trình viên, không nhắc App Review → nói hơi quá (mục có nhãn [NHẬN ĐỊNH]). Tóm tắt ý 5 viết "không cần giấy phép lập trình viên": nguồn nói "credentials" (thông tin đăng nhập lập trình viên), không phải giấy phép.
5. **SP-1, nhãn:** dòng 4 ghi 1 trang chỉ đọc 100.000/108.850 ký tự. Đó là trang Wifim (D4), nhưng D4 vẫn gắn ĐÃ ĐỌC TOÀN VĂN. SP-1 nói thẳng rằng WebFetch trả bản tóm, không phải nguyên văn. Điều này đúng cho cả 3 file và cho bản kiểm này.

**Giữa các file**
6. **Giá SP-1 và kết luận pháp lý SP-2: M1 không mâu thuẫn trực tiếp, M2 thì có.** SP-2 (tóm tắt ý 10, mục 5.a ý 5) khuyên "giá theo tháng, **không** theo hợp đồng bán được". M2 của SP-1 (0,3% giá trị hợp đồng) đi ngược khuyến nghị này; SP-1 có tự ghi rủi ro môi giới. M1 (phí nền 9 tr + 200 nghìn/lượt xem đất) không thu theo hợp đồng, nhưng SP-2 mục 6 câu 5 vẫn hỏi luật sư cả "thưởng theo lượt xem đất". Vì vậy M1 cũng phải ghi "chờ luật sư", không phải "an toàn".
7. **Chi phí AI mỗi khách lệch giữa SP-1 và SP-3:** SP-1 dùng 2,6 tr (mỗi khách một gói Claude ~100 USD) hoặc "~1 tr qua API". SP-3 nói gói Claude chỉ hợp khi **khách tự đứng tên**, còn bán thật thì phải đi API: 1,5–2,5 tr (giữa), 8,6 tr (xấu nhất). Lãi M1 5,5 tr của SP-1 chưa có kịch bản xấu.
8. **Chi đội để tính hoà vốn lệch:** SP-1 dùng 60 tr/tháng (theo SU-3), ra 11–12 khách. SP-3 dùng 40 tr/tháng (theo SU-8), ra ~8 dự án ở giá 10 tr. Hai phiên dùng hai giả định khác nhau.
9. **Business Agent:** SP-1 tóm tắt ghi "toàn cầu trên WhatsApp/Instagram, miễn phí". SP-2 M14 ghi "không nêu nước nào, miễn phí hiện tại". Bản SP-2 sát nguồn hơn.
10. Giờ hỗ trợ: SP-1 dùng 10 giờ/tháng (16 giờ tháng đầu), SP-3 dùng 8–10 giờ (20 giờ tháng đầu). Lệch nhỏ, không đổi kết luận.

## 4. Đề xuất sửa cho người tổng hợp

1. SP-3 tóm tắt ý 5: thay "tới ~4,6 triệu" bằng "giữa 1,5–2,5 triệu; xấu nhất ≈ 8,6 triệu (toàn Opus, không đệm)". Đưa kịch bản 8,6 triệu vào bảng lãi M1 của SP-1: ở mức đó lãi ≈ −0,5 tr/tháng. Vì vậy phải đo token thật trước khi báo giá.
2. SP-1 tóm tắt ý 7 và bảng 3.5: đổi "miễn phí" thành "bắt đầu miễn phí, Meta đã báo sẽ thu phí qua gói trả phí và theo token (D15, M14)".
3. SP-1 tóm tắt ý 2, mục 3.1: đổi "≈ 4% doanh thu" thành "≈ 2,9% (72 lô × 1,39 tỷ bình quân, theo v2)". Đổi "40–60 tr/lô" thành "~56–83 tr/lô". Ví dụ "1 HĐ ≈ 40 tr, gấp ~4 lần phí" sửa thành "≈ 56 tr".
4. SP-2 tóm tắt ý 4: sửa "(M8)" thành "(M9)".
5. SP-3 D10 và tóm tắt ý 4: đổi "đã bỏ hoàn toàn" thành "đã ngừng hỗ trợ (deprecated), khuyên chuyển sang Responses API". Kết luận giữ nguyên.
6. SP-3 D11: thêm "trang giá 21/10 đã có Muse Spark 1.2, 1.3 và chế độ Contributor 0,10/0,20 USD (đổi lại cho Meta dùng dữ liệu để huấn luyện); giới hạn Mỹ chỉ thấy ở báo 07/2026 [CẦN XÁC NHẬN]".
7. SP-2 R2: ghi rõ "chưa kiểm lại văn bản gốc ngày 21/10 (PDF quét, vbpl không ra chữ); mức phạt 50–80 triệu chỉ dựa trên NC-A". Người tổng hợp không đưa con số này ra ngoài khi chưa mở lại Điều 59 NĐ 330.
8. SP-2 L1, L3, R2 và SP-1 D4: đổi nhãn thành "ĐÃ ĐỌC (phần dẫn)" hoặc "DÙNG LẠI". Bỏ L3 khỏi đếm "20 nguồn đọc trọn".
9. SP-2 mục 4 ý 1: bỏ "không cần App Review" hoặc gắn [CẦN XÁC NHẬN]. Tóm tắt ý 5: đổi "giấy phép lập trình viên" thành "thông tin đăng nhập lập trình viên".
10. Bản tổng hợp: ghi M1 là "chờ luật sư (SP-2 câu 5)", không ghi "an toàn". Loại M2 cho tới khi có ý kiến luật sư. Thống nhất một giả định chi đội (40 hay 60 tr/tháng) và một số giờ hỗ trợ cho cả hai phiên.
