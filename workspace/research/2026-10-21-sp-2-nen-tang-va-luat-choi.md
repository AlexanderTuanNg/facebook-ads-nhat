# SP-2. Nền tảng và luật chơi: app bên thứ ba ĐƯỢC làm 5/6 việc qua đường chính thức, có điều kiện; đăng nhóm bằng nick tự động thì KHÔNG

> **Đính chính sau kiểm độc lập 21/10** (`2026-10-21-sp-kiem-doc-lap.md`): (1) tóm tắt ý 4: điều khoản cấm truy cập tự động là **M9**, không phải M8; (2) mức phạt 50–80 tr và điều kiện ≥ 3 nhân sự (R2) **chưa kiểm lại được trên văn bản gốc** ngày 21/10 (PDF quét, vbpl không ra chữ) — không đưa con số ra ngoài trước khi mở lại NĐ 330 Điều 59; (3) L1, L3, R2 là "ĐÃ ĐỌC (phần dẫn)"/"DÙNG LẠI", không tính vào "20 nguồn đọc trọn"; (4) mục 4 ý 1 "không cần App Review" → [CẦN XÁC NHẬN]; "giấy phép lập trình viên" → "thông tin đăng nhập lập trình viên". Nội dung gốc bên dưới giữ nguyên.

> **Dòng đầu (bộ luật B1.8):** lập 21/10/2026 · phạm vi: Meta (Marketing API, Pages API, Messenger, Conversions API, nick cá nhân và nhóm), Zalo (OA, ZNS, QC Zalo), luật Việt Nam phần còn thiếu so với SU-4 và NC-A · ngân sách đã dùng: **14 lượt tìm, 19 trang mở đọc trọn** (thêm 2 lần mở hỏng: trang tài liệu Zalo Developers chỉ ra tiêu đề vì chạy JavaScript; trang Công báo Luật Kinh doanh bất động sản chỉ có thông tin tệp) · một phiên làm tuần tự, không bật tác nhân con, không dùng trình duyệt.
> **Đã đọc trọn 20 nguồn:** 19 trang mở trong phiên (14 trang chính thức của Meta, trong đó trang Conversions API ngắn, ít thông tin; 4 trang chính thức của Zalo; 1 dự thảo nghị định của Bộ Công an, tệp .doc trích chữ bằng máy) + Điều 11 Luật Trí tuệ nhân tạo đọc từ bản chữ SU-4 đã trích từ Công báo (không tính vào 19 lần mở).
> **Chỗ còn yếu:** (1) Zalo: chưa đọc được điều khoản dùng tài khoản Zalo cá nhân, chính sách quảng cáo Zalo cho bất động sản, tiêu chuẩn duyệt mẫu ZNS; (2) Meta: thời gian App Review thật và giấy tờ xác minh doanh nghiệp Việt Nam chưa có nguồn chính thức; (3) luật: dự thảo nghị định chống tin rác **chưa ban hành**; Luật Kinh doanh bất động sản 2023 chưa mở được toàn văn ở nguồn chính thức (dùng lại file 14/10 dẫn caselaw); Nghị định hướng dẫn Điều 11 Luật Trí tuệ nhân tạo về hình thức gắn nhãn chưa tìm.
> Nhãn: **ĐÃ ĐỌC TOÀN VĂN** (mở nguồn và đọc phần được dẫn) · **NGUỒN-TRÍCH** (đoạn trích, kết quả tìm kiếm, bài bên thứ ba) · **QUẢNG CÁO** (trang nhà bán) · **[NHẬN ĐỊNH]** · **[ƯỚC TÍNH]** · **[CẦN XÁC NHẬN]**. Mọi kết luận pháp lý: **cần luật sư xác nhận**. Không gặp trang nào có câu ra lệnh cho AI.

## 1. Tóm tắt

1. **Được phép: ĐÚNG CÓ ĐIỀU KIỆN.** 5/6 việc (tạo bài, đăng Fanpage, quản lý QC, đọc số, tự trả lời tin nhắn) có đường chính thức cho app bên thứ ba; việc thứ 6 (**đăng nhóm bằng nick qua trình duyệt tự động**) **trái điều khoản Meta**, không đưa vào sản phẩm. [NHẬN ĐỊNH dựa trên M1–M12]
2. **Điều kiện Meta cho app phục vụ nhiều doanh nghiệp:** startup phải là doanh nghiệp đã **xác minh với Meta**, qua **xác minh "Nhà cung cấp công nghệ" (Tech Provider)**, **App Review từng quyền** để có mức Nâng cao; quản lý QC thật phải lên bậc **Full** (≥ 500 lệnh gọi/15 ngày, lỗi < 15%). ĐÃ ĐỌC TOÀN VĂN (M1, M2, M4).
3. **Ca mẫu Yên Thế không cần chờ các bước trên:** người có vai trò trên app dùng được ở mức Tiêu chuẩn (M1). Nhưng Meta ghi bậc Limited của Marketing API "không dành cho app chạy cho nhà quảng cáo thật" (M2) → khách thứ 2 trở đi phải đi đủ thủ tục. [NHẬN ĐỊNH]
4. **Groups API đã bị Meta bỏ từ 2024** (M10); điều khoản cấm truy cập tự động khi chưa được phép (M8) và **cấm app thu thập thông tin đăng nhập của người dùng Meta** (M12). App giữ mật khẩu nick của nhiều khách để đăng nhóm = vi phạm hai lần. ĐÃ ĐỌC TOÀN VĂN.
5. **Bằng chứng bác H0, phần "nền tảng làm thay":** Meta đã mở **Meta Ads AI Connectors** (bản thử công khai từ 29/04/2026: doanh nghiệp tự nối AI của mình vào tài khoản QC, không cần giấy phép lập trình viên) và **Meta Business Agent** (AI trả lời tin nhắn trên Messenger, WhatsApp, Instagram, đang miễn phí). Lớp "quản lý QC" và "tự trả lời" đang thành hàng miễn phí của Meta. ĐÃ ĐỌC TOÀN VĂN (M13, M14).
6. **Zalo có đường chính thức cho app bên thứ ba:** một App gửi tin cho "một hoặc nhiều OA" (Z2); nhưng mỗi OA phải mua **gói Tăng trưởng 2,5 triệu/năm** trở lên mới nối API (Z6); qua API chỉ nhắn tư vấn được **trong 7 ngày** từ lần khách tương tác cuối, miễn phí trong 48 giờ (Z5); ZNS 200–300 đ/tin (Z1). ĐÃ ĐỌC TOÀN VĂN.
7. **Luật AI buộc báo khách đang nói với AI** (Điều 11 khoản 1) và **gắn nhãn ảnh, video AI mô phỏng sự kiện thật** (khoản 4) → câu chào "trợ lý AI" và nhãn "ảnh minh hoạ tạo bằng AI" là bắt buộc trong sản phẩm. ĐÃ ĐỌC TOÀN VĂN (L3); áp vào sản phẩm: [NHẬN ĐỊNH, cần luật sư xác nhận].
8. **Giữ sổ khách của nhiều chủ đầu tư:** app là **bên xử lý**; vận hành phần mềm tự động thay bên kiểm soát nằm trong danh mục **"dịch vụ xử lý dữ liệu cá nhân" cần Giấy chứng nhận của Bộ Công an** (≥ 3 nhân sự đủ năng lực; thiếu giấy phạt 50–80 triệu). Dùng lại NC-A (ĐÃ ĐỌC TOÀN VĂN); áp vào app: [NHẬN ĐỊNH, cần luật sư xác nhận]. Đây là điều kiện nặng nhất cho đội 1–3 người.
9. **Tin nhắn quảng cáo sắp siết cả Zalo, Messenger:** dự thảo nghị định thay NĐ 91/2020 (dự kiến hiệu lực 01/01/2027) áp cả ứng dụng OTT, chỉ cho nhắn QC bằng **tên định danh**, cấm dùng số điện thoại để nhắn/gọi QC, khách lạ chỉ được 1 tin xin đăng ký. ĐÃ ĐỌC TOÀN VĂN (bản dự thảo, chưa phải luật).
10. **Rủi ro làm môi giới trá hình:** nếu app tư vấn, hẹn xem đất và thu tiền theo hợp đồng bán được, có thể bị coi là môi giới (Luật KDBĐS Điều 61: phải là doanh nghiệp môi giới, có người có chứng chỉ). Thu phí phần mềm theo tháng, sale của chủ đầu tư chốt thì an toàn hơn. [NHẬN ĐỊNH, cần luật sư xác nhận]

## 2. Bảng dữ kiện

Ngày tra mọi dòng: 21/10/2026, trừ dòng "dùng lại" ghi ngày của file gốc.

| # | Dữ kiện | Nguồn (link) | Trạng thái |
|---|---|---|---|
| M1 | Quyền truy cập có 2 mức: **Tiêu chuẩn** (chỉ người có vai trò trên app) và **Nâng cao** (bất kỳ ai). App phục vụ người không có vai trò trên app cần mức Nâng cao; mức này phải qua **App Review cho từng quyền** và **Xác minh doanh nghiệp** (bắt buộc từ 01/02/2023); có "kiểm tra sử dụng dữ liệu" hằng năm; hạ từ Nâng cao về Tiêu chuẩn thì mọi quyền với người ngoài bị tắt | https://developers.facebook.com/docs/graph-api/overview/access-levels | ĐÃ ĐỌC TOÀN VĂN |
| M2 | Marketing API có 2 bậc: **Limited** (mặc định, "chỉ để phát triển", "không dành cho app chạy cho nhà quảng cáo thật") và **Full** (cần App Review). Lên Full cần **≥ 500 lệnh gọi trong 15 ngày** và **lỗi < 15%** trên 500 lệnh gần nhất. Full quản lý không giới hạn số tài khoản QC, mỗi tài khoản phải được chủ bấm cho phép (`ads_management` / `ads_read`) | https://developers.facebook.com/docs/marketing-api/get-started/authorization | ĐÃ ĐỌC TOÀN VĂN |
| M3 | Giới hạn gọi: QC mức tiêu chuẩn 300 + 40 × số QC đang chạy mỗi giờ, mức nâng cao 100.000 + 40 × số QC; Trang 4.800 × số người tương tác/24 giờ; Messenger 200 × số người tương tác/24 giờ. Không thấy phí dùng API | https://developers.facebook.com/docs/graph-api/overview/rate-limiting | ĐÃ ĐỌC TOÀN VĂN (phí: không thấy trang nào thu, [CẦN XÁC NHẬN]) |
| M4 | Doanh nghiệp làm app truy cập dữ liệu do **doanh nghiệp khác** sở hữu là **Tech Provider**, phải qua **xác minh quyền truy cập** (khoảng 5 ngày làm việc); doanh nghiệp mới phải xác minh doanh nghiệp và nộp App Review trước; quá hạn thì lệnh gọi API "dần không thực hiện được" | https://developers.facebook.com/blog/post/2022/06/02/access-verification-process-for-tech-provider-apps/ | ĐÃ ĐỌC TOÀN VĂN (bài 2022; quy trình hiện nay: [CẦN XÁC NHẬN]) |
| M5 | Xác minh doanh nghiệp thường mất 2–5 ngày làm việc | https://docs.360dialog.com/partner/get-started/tech-providers/becoming-a-meta-tech-provider-a-step-by-step-guide | NGUỒN-TRÍCH (bên thứ ba, nói về WhatsApp) |
| M6 | Đăng bài lên Trang: người dùng của app phải có nhiệm vụ `CREATE_CONTENT` trên Trang; mọi quyền phải qua App Review trước khi app chạy thật; "Facebook Login for Business" là cách đăng nhập Meta khuyên cho Tech Provider | https://developers.facebook.com/docs/pages-api/overview | ĐÃ ĐỌC TOÀN VĂN |
| M7 | Messenger: tin chuẩn trong **cửa sổ 24 giờ** từ hành động của khách; sau QC bấm-để-nhắn có thể tới **7 ngày**; ngoài cửa sổ chỉ dùng **thẻ tin nhắn** đúng mục đích (dùng sai bị hạn chế); thẻ `HUMAN_AGENT` cho **người thật** trả lời trong 7 ngày; tin quảng cáo ngoài cửa sổ chỉ qua **Sponsored Messages** (trả tiền) | https://developers.facebook.com/docs/messenger-platform/policy/policy-overview | ĐÃ ĐỌC TOÀN VĂN |
| M8 | Messenger: nơi luật bắt buộc thì bot phải **báo khách đang nói với dịch vụ tự động** (đầu cuộc, sau thời gian dài im, khi chuyển từ người sang máy); Meta khuyên báo cả khi luật không bắt; bot tự động phải trả lời trong **30 giây**, sai mà không sửa trong 7 ngày có thể bị hạn chế | như M7 | ĐÃ ĐỌC TOÀN VĂN |
| M9 | Điều khoản Facebook (hiệu lực 01/01/2025): **không được truy cập hoặc thu thập dữ liệu bằng phương tiện tự động khi chưa được Meta cho phép trước** (mục 3.2); không chia sẻ mật khẩu, không cho người khác vào tài khoản; **mỗi người một tài khoản, tên thật, dùng cho mục đích cá nhân** (3.1); vi phạm có thể bị đình chỉ, khoá vĩnh viễn (3.2, 4.2) | https://www.facebook.com/terms.php | ĐÃ ĐỌC TOÀN VĂN |
| M10 | **Groups API đã bỏ**: ngừng ở Graph API v19 (công bố 23/01/2024), gỡ khỏi mọi phiên bản sau 90 ngày, gồm `publish_to_groups`, `groups_access_member_info` | https://developers.facebook.com/blog/post/2024/01/23/introducing-facebook-graph-and-marketing-api-v19/ | ĐÃ ĐỌC TOÀN VĂN |
| M11 | Tiêu chuẩn cộng đồng "Spam": cấm đăng, chia sẻ, tương tác, tạo tài khoản, nhóm, Trang "với tần suất rất cao", **thủ công hay tự động**; tần suất thấp hơn vẫn có thể bị hạn chế khi có dấu hiệu khác (nội dung lặp lại); cấm mua bán tài khoản, nhóm, Trang | https://transparency.meta.com/policies/community-standards/spam/ | ĐÃ ĐỌC TOÀN VĂN |
| M12 | Điều khoản nền tảng (cập nhật 03/02/2026): Tech Provider chỉ dùng nền tảng **thay mặt và theo chỉ dẫn của khách** (5.b.ii.1); **dữ liệu từng khách để riêng** (5.b.ii.2); cấm bán, mua dữ liệu (3.a.iv); xoá dữ liệu khi người dùng yêu cầu hoặc khi ngừng sản phẩm (3.d); Meta được kiểm tra, kiểm toán ≤ 1 lần/năm, tạm ngừng hoặc gỡ app và tài khoản (7); **"không được yêu cầu hoặc thu thập riêng thông tin đăng nhập của người dùng Meta"** (6.a.iii) | https://developers.facebook.com/terms/ | ĐÃ ĐỌC TOÀN VĂN |
| M13 | **Meta Ads AI Connectors** (bản thử công khai, 29/04/2026): máy chủ MCP và dòng lệnh của Meta để doanh nghiệp, agency quản lý QC từ công cụ AI đang dùng: báo cáo, tạo và sửa chiến dịch bằng lời thường, quản lý danh mục; "không cần thông tin lập trình viên"; cập nhật 16/07/2026: người có toàn quyền danh mục doanh nghiệp đặt được AI được làm gì (đổi ngân sách…). Không nêu giá, không nêu danh sách nước | https://www.facebook.com/business/news/meta-ads-ai-connectors | ĐÃ ĐỌC TOÀN VĂN |
| M14 | **Meta Business Agent** (03/06/2026): AI trả lời câu hỏi, gợi ý sản phẩm, đặt lịch, **sàng lọc khách**, chốt đơn; doanh nghiệp chọn lúc người thật vào; chạy trên Messenger, WhatsApp, Instagram; "toàn cầu, tiếng địa phương" nhưng không nêu nước nào; **kích hoạt miễn phí "hiện tại"**, gói trả phí sắp có; > 1 triệu doanh nghiệp đang dùng | https://about.fb.com/news/2026/06/meta-business-agent/ | ĐÃ ĐỌC TOÀN VĂN (có ở Việt Nam, tiếng Việt: [CẦN XÁC NHẬN]) |
| M15 | Meta One (09/2026) gói kèm Business Agent, từ 14,99 USD/tháng; tin Business Agent trên WhatsApp tính phí từ 01/08/2026 | kết quả tìm kiếm about.fb.com, developers.facebook.com (pricing WhatsApp) | NGUỒN-TRÍCH [CẦN XÁC NHẬN] |
| M16 | Tháng 01/2026 Meta nói đang thử "trợ lý kinh doanh Meta AI" cho nhà quảng cáo từ quý 4/2025; doanh thu công cụ tạo video AI đạt mức 10 tỷ USD/năm ở quý 4/2025. Không thấy cam kết "tự động trọn gói QC" | https://about.fb.com/news/2026/01/2026-ai-drives-performance/ | ĐÃ ĐỌC TOÀN VĂN |
| M17 | WhatsApp Business: từ 15/01/2026 cấm "nhà cung cấp AI" có AI là sản phẩm chính (trợ lý AI đa năng) trên nền tảng, Meta tự quyết thế nào là "chính"; AI chăm sóc khách của doanh nghiệp vẫn được | https://respond.io/blog/whatsapp-general-purpose-chatbots-ban (và báo khác) | NGUỒN-TRÍCH (chưa đọc văn bản gốc của Meta) |
| M18 | Conversions API nối dữ liệu của nhà quảng cáo (gồm sự kiện ngoại tuyến từ sổ khách, CRM) với Meta qua máy chủ; trang không nói cần App Review hay không, có gửi được "khách đủ chất lượng" không | https://developers.facebook.com/docs/marketing-api/conversions-api | ĐÃ ĐỌC TOÀN VĂN (trang ngắn; điều kiện: [CẦN XÁC NHẬN]) |
| Z1 | ZNS giá theo tin gửi thành công: **200 đ** (đa số mẫu), **300 đ** (OTP, yêu cầu thanh toán, voucher); nút thứ 2 trở đi +100 đ; chưa gồm VAT | https://zalo.solutions/zns/pricing | ĐÃ ĐỌC TOÀN VĂN |
| Z2 | Tin mẫu ZBS (ZNS) là tin **chăm sóc khách hàng**; mẫu phải được Zalo **duyệt 2–3 ngày làm việc**; cần tài khoản ZBS + OA + **App "đại diện cho một hoặc nhiều OA"**; có thưởng/phạt theo phản hồi người nhận | https://zalo.solutions/business-message/guidelines/intro | ĐÃ ĐỌC TOÀN VĂN (tiêu chuẩn duyệt, có cho nội dung quảng cáo không: [CẦN XÁC NHẬN]) |
| Z3 | Tin truyền thông: OA đã xác thực tối đa 4 tin/người, 40 lần/tháng (chưa xác thực 1 và 20) | https://helpcenter.esms.vn/cau-hoi-thuong-gap/zalo-oa | NGUỒN-TRÍCH (nhà bán, không ghi ngày) [CẦN XÁC NHẬN] |
| Z4 | Xác thực OA khoảng 7 ngày làm việc, thông tin khớp giấy đăng ký kinh doanh; ngành đặc thù có thể phải nộp giấy phép con. Quy định riêng cho bất động sản: không tìm được | helpcenter.esms.vn | NGUỒN-TRÍCH [CẦN XÁC NHẬN] |
| Z5 | Tin Tư vấn = tin cơ bản để **trả lời khách**; chỉ gửi khi khách đã tương tác (nhắn, gọi, bình luận, bấm menu, quan tâm OA) và không chặn OA; **qua OA OpenAPI chỉ gửi trong 07 ngày** từ tương tác cuối (trang quản lý OA: 365 ngày); **miễn phí trong 48 giờ**, ngoài 48 giờ tính phí | https://oa.zalo.me/home/documents/guides/tin-tu-van | ĐÃ ĐỌC TOÀN VĂN |
| Z6 | Gói OA (gồm VAT): Cơ bản miễn phí, Tiêu chuẩn 1 tr/năm (**không có API**), **Tăng trưởng 2,5 tr/năm** (có API, 100 lệnh/phút, 3 app được uỷ quyền, 500 tin tư vấn ngoài 48 giờ/tháng), Toàn diện 6 tr/năm (2.000 lệnh/phút, app không giới hạn). **"Để liên kết ứng dụng với OA thông qua API, bạn cần sử dụng Gói tăng trưởng hoặc toàn diện"**; tin tư vấn vượt hạn mức 55 đ/tin | https://zalo.solutions/oa/pricing | ĐÃ ĐỌC TOÀN VĂN (cột bảng hiện hơi lệch, số hạn mức cần đối chiếu) |
| Z7 | Khách 45+ dùng Zalo hơn Messenger: thế hệ X nhắn hằng ngày bằng Zalo 75%, Messenger 10% (Decision Lab, đăng 06/11/2024) | dùng lại `workspace/research/2026-10-15-chuyen-mon-qc-bds-nguon.md` mục 1 ý 4 (15/10) | NGUỒN-TRÍCH (dùng lại) |
| L1 | **Dự thảo** nghị định "Chống tin nhắn rác, thư điện tử rác, cuộc gọi rác" của Bộ Công an (đăng 09/2026), dự kiến **hiệu lực 01/01/2027, thay NĐ 91/2020**; phạm vi **gồm cả tin nhắn, cuộc gọi qua ứng dụng OTT** (Điều 1) | https://bocongan.gov.vn/media/bca-media/library-20260909084715-f7e1171f-eb0c-4ae2-97ed-7017b136dc65-1-nghi-inh-thay-the-n-91.doc | ĐÃ ĐỌC TOÀN VĂN Điều 1, 2, 3, 25–28, 43 (dự thảo, chưa phải luật) |
| L2 | Dự thảo Điều 25: không gửi QC tới "Danh sách không quảng cáo" hoặc người đã không đồng ý; số khác chỉ được **01 tin đăng ký đầu tiên và duy nhất**, 24 giờ không xác nhận thì dừng; nhắn 7–22 giờ, gọi QC 8–17 giờ; **chỉ nhắn/gọi QC khi đã có tên định danh, không dùng số điện thoại**. Điều 27: tin QC phải gắn nhãn; Điều 28: cách từ chối ở cuối tin, từ chối bằng tin nhắn và cuộc gọi | như L1 | ĐÃ ĐỌC TOÀN VĂN (dự thảo) |
| L3 | Luật Trí tuệ nhân tạo Điều 11: (1) nhà cung cấp bảo đảm hệ thống tương tác trực tiếp với người cho người dùng **biết đang tương tác với hệ thống**; (2) âm thanh, hình ảnh, video AI tạo được đánh dấu máy đọc được; (3) bên triển khai **thông báo rõ khi đưa ra công chúng văn bản, âm thanh, hình ảnh, video do AI tạo/sửa nếu có khả năng gây nhầm lẫn về tính xác thực của sự kiện, nhân vật**; (4) nội dung AI mô phỏng ngoại hình, giọng người thật hoặc **tái hiện sự kiện thực tế** phải gắn nhãn dễ nhận biết; (6) Chính phủ quy định hình thức | Công báo (bản .docx, bản chữ SU-4 đã trích; xem SU-4 mục 7 nguồn [L134]) | ĐÃ ĐỌC TOÀN VĂN Điều 11 |
| R1 | Dùng lại SU-4: startup bán dưới tên mình là **"nhà cung cấp"**, khách dùng là **"bên triển khai"** (Luật AI Điều 3); chatbot nói chuyện với khách **ít nhất rủi ro trung bình** → hồ sơ phân loại và **thông báo Bộ KHCN qua Cổng một cửa trước khi dùng** (Điều 9, 10); hợp đồng phải ghi ai chịu gì (Điều 29) | `D:\0. AI\goi-phong-kham\nghien-cuu\startup\su-4-phap-ly-startup-ai-y-te.md` mục 2.1, câu 2, câu 7 (16/10) | ĐÃ ĐỌC TOÀN VĂN luật; phân loại là [NHẬN ĐỊNH] của SU-4 |
| R2 | Dùng lại NC-A: bên xử lý chỉ nhận dữ liệu sau hợp đồng (Luật 91/2025 Điều 37); **"dịch vụ xử lý dữ liệu cá nhân" gồm vận hành phần mềm tự động thay mặt bên kiểm soát, phân tích dữ liệu, xử lý tự động bằng AI** (NĐ 356 Điều 21) → cần Giấy chứng nhận Bộ Công an: tổ chức Việt Nam, người phụ trách là công dân thường trú, **≥ 3 nhân sự**, hồ sơ đánh giá tác động đạt (Điều 22–25); thiếu giấy phạt **50–80 triệu** (NĐ 330 Điều 59); lưu dữ liệu trên đám mây nước ngoài hoặc gửi cho AI nước ngoài = chuyển xuyên biên giới, nộp hồ sơ trong 60 ngày | `D:\0. AI\goi-phong-kham\nghien-cuu\nc-a-phap-ly-du-lieu-va-ai.md` mục 1, dòng 21, 36, 41, 42, 52 (15/10) | ĐÃ ĐỌC TOÀN VĂN (dùng lại) |
| R3 | Dùng lại NC-F2: Luật Quảng cáo sửa đổi 75/2025 (hiệu lực 01/01/2026): người chuyển tải QC trên mạng chịu trách nhiệm nếu nội dung sai Điều 19; NĐ 342/2025 hướng dẫn; NĐ 87/2026 xử phạt, tổ chức bị phạt gấp đôi cá nhân; từ "nhất, số 1" chỉ dùng khi có khảo sát hoặc giải thưởng (TT 12/2026) | `D:\0. AI\goi-phong-kham\nghien-cuu\nc-f2-quang-cao-luat-su-duoc-thi-truong.md` dòng 1–5, 14–16 (16/10) | ĐÃ ĐỌC TOÀN VĂN (dùng lại) |
| R4 | Dùng lại file 14/10 và checklist §H: QC phải khớp thông tin dự án đã công khai (Luật KDBĐS 2023 Điều 6, NĐ 96/2024 Điều 4); **Điều 61: môi giới phải có chứng chỉ và hành nghề trong doanh nghiệp môi giới hoặc sàn**; doanh nghiệp môi giới cần ≥ 1 người có chứng chỉ; chủ đầu tư không bắt buộc bán qua sàn | `workspace/research/2026-10-14-best-practice-quang-cao-bds.md` dòng 183, 229, 246; `workspace/compliance-checklist.md` §H; kết quả tìm kiếm luatvietnam, thuvienphapluat | NGUỒN-TRÍCH (caselaw, báo); toàn văn chính thức chưa mở được [CẦN XÁC NHẬN] |
| R5 | Chính phủ đã có nghị quyết về dự án Luật sửa đổi Luật Đất đai, Nhà ở, **Kinh doanh bất động sản**, Các tổ chức tín dụng (NQ 79/NQ-CP, 84/NQ-CP) | https://vanban.chinhphu.vn/?docid=210361&pageid=27160 (kết quả tìm kiếm) | NGUỒN-TRÍCH; nội dung sửa đổi và thời điểm: [CẦN XÁC NHẬN] |
| R6 | Dùng lại STATE dự án: nick_chinh là "acc clone", bị hạn chế gửi tin từ 11/10; nhóm FB **203 bài/79 nhóm → 1 SĐT**; Fanpage CĐT chưa nối; kết nối `meta-ads` chỉ đọc (app "AI ads marketing") | `workspace/STATE.md` mục 2 và "Vận hành đang chạy" (21/10) | [DỮ LIỆU] dự án |

## 3. Phân tích theo từng câu hỏi

### Câu 1. Meta mở đủ đường chính thức cho app làm thay doanh nghiệp khác, nhưng khách thứ 2 trở đi phải qua 4 cửa, mất khoảng 1–2 tháng

**Bốn cửa (theo thứ tự):**

| Cửa | Việc phải làm | Mất bao lâu | Căn cứ |
|---|---|---|---|
| 1. Xác minh doanh nghiệp | Startup có pháp nhân (công ty), nộp giấy tờ trong Business Manager | 2–5 ngày làm việc | M1; M5 (NGUỒN-TRÍCH) |
| 2. Xác minh Tech Provider | Khai doanh nghiệp mình dùng app thay cho doanh nghiệp khác thế nào | ~5 ngày làm việc | M4 |
| 3. App Review từng quyền | Quay video luồng dùng, giải thích vì sao cần: đăng Trang (`pages_manage_posts`…), tin nhắn (`pages_messaging`), QC (`ads_management`, `ads_read`) | [CẦN XÁC NHẬN] | M1, M6 |
| 4. Marketing API bậc Full | Chạy ≥ 500 lệnh/15 ngày, lỗi < 15%, rồi bấm nâng cấp | ≥ 15 ngày chạy thử | M2 |

- **Tổng thời gian [ƯỚC TÍNH]:** cửa 1–2 khoảng 2 tuần; App Review chưa có số chính thức, giả định 1–4 tuần, có thể bị trả lại; cửa 4 cần ≥ 15 ngày gọi API thật. Cộng lại **khoảng 4–8 tuần** nếu không bị từ chối. Cách tính: 10 + 5–20 + 15 ngày, một phần chạy song song.
- **Chi phí:** không thấy Meta thu phí API (M3). Chi phí thật là ngày công làm hồ sơ, quay video, sửa theo góp ý. [NHẬN ĐỊNH]
- **Giới hạn gọi không phải nút thắt** ở quy mô 5–20 khách: mức tiêu chuẩn 300 + 40 × số QC mỗi giờ là đủ cho đọc số hằng ngày (M3). [NHẬN ĐỊNH]
- **Luật nền tảng cho Tech Provider (M12):** chỉ làm theo chỉ dẫn của khách; dữ liệu từng khách để riêng; không bán dữ liệu; xoá khi khách hoặc người dùng yêu cầu; Meta được kiểm toán và gỡ app. Khớp với nghĩa vụ "bên xử lý" của luật Việt Nam (R2).
- **Tin nhắn Messenger (M7, M8):** máy trả lời trong 24 giờ (QC bấm-để-nhắn: tới 7 ngày); ngoài cửa sổ chỉ người thật trả lời bằng thẻ `HUMAN_AGENT` trong 7 ngày; không gửi tin chào hàng ngoài cửa sổ trừ khi trả tiền. Bot phải trả lời trong 30 giây.
- **Conversions API (M18):** dùng được để gửi ngược "khách đã cho số, đã xem đất" từ sổ khách về Meta, giúp QC tối ưu cho khách thật. Điều kiện quyền cho app nhiều khách: [CẦN XÁC NHẬN].
- **Bằng chứng bác tìm được:** chưa thấy trang Meta nào cấm app bên thứ ba quản lý QC, Trang, tin nhắn. Bác thật nằm ở câu 5 (Meta tự làm) chứ không ở luật chơi.

### Câu 2. Đăng nhóm bằng nick qua trình duyệt tự động trái điều khoản Meta; nhân ra nhiều khách thì rủi ro tăng nhiều lần

- **Không còn đường chính thức:** Groups API bị bỏ hẳn từ 2024 (M10). Mọi cách đăng nhóm tự động bây giờ đều là điều khiển trình duyệt.
- **Trái điều khoản [NHẬN ĐỊNH, căn cứ ĐÃ ĐỌC TOÀN VĂN]:**
  1. "Không được truy cập… bằng phương tiện tự động khi chưa được chúng tôi cho phép trước" (M9, mục 3.2). Điều khiển trình duyệt để đăng bài là truy cập tự động; Meta chưa cho phép.
  2. Tài khoản "dùng cho mục đích cá nhân", tên thật, một người một tài khoản (M9, mục 3.1). Nick clone và nick dùng cho việc bán hàng của doanh nghiệp khác đều trái mục này.
  3. App bên thứ ba **"không được yêu cầu hoặc thu thập riêng thông tin đăng nhập của người dùng Meta"** (M12, 6.a.iii). App giữ mật khẩu hoặc phiên đăng nhập nick của khách là trái thẳng điều này, và có thể kéo theo việc Meta gỡ cả app chính thức (M12, mục 7).
  4. Chính sách spam bắt cả việc đăng tự động "tần suất rất cao" và nội dung lặp lại (M11).
- **Rủi ro khi nhân rộng [NHẬN ĐỊNH]:** một khách thì mất một nick; mười khách thì app giữ mười bộ đăng nhập, cùng một kiểu hành vi, dễ bị Meta nhận diện hàng loạt; nếu cùng doanh nghiệp đứng tên app chính thức, có thể mất luôn quyền API của mọi khách.
- **Số của dự án:** 203 bài/79 nhóm ra 1 SĐT; nick chính đã bị hạn chế gửi tin từ 11/10 (R6). Lợi ích thấp, rủi ro đã thành thật.
- **Kết luận:** đăng nhóm **không đưa vào sản phẩm**. Nếu khách muốn có mặt ở nhóm: app chỉ **soạn bài và nhắc lịch**, người thật của khách tự đăng bằng tay. [NHẬN ĐỊNH]

### Câu 3. Zalo có đường chính thức cho app phục vụ nhiều OA, chi phí thấp; hai giới hạn: phải mua gói, và chỉ trả lời khách đã chủ động nhắn

- **Mô hình app nhiều OA có sẵn:** "App" đại diện một hoặc nhiều OA gửi tin (Z2).
- **Chi phí mỗi khách [ƯỚC TÍNH]:** gói Tăng trưởng 2,5 tr/năm (≈ 208 nghìn/tháng) để nối API (Z6) + ZNS 200–300 đ/tin (Z1). Ví dụ 1.000 tin ZNS/tháng ≈ 200–300 nghìn. Tổng ≈ 0,4–0,5 tr/tháng/khách, chưa VAT phần ZNS.
- **Giới hạn 1, thời gian:** qua API chỉ nhắn tư vấn trong 7 ngày từ lần khách tương tác cuối; trong 48 giờ miễn phí (Z5). Hợp với "trả lời nhanh khách vừa nhắn", không hợp với "chăm khách cũ hàng tháng". Chăm khách cũ phải dùng ZNS (mẫu duyệt trước) hoặc tin truyền thông có hạn mức (Z3).
- **Giới hạn 2, nội dung:** ZNS là tin chăm sóc khách hàng (Z2); dùng ZNS để chào hàng có bị từ chối mẫu không: [CẦN XÁC NHẬN]. Quảng cáo Zalo cho bất động sản cần giấy tờ gì: chưa tìm được [CẦN XÁC NHẬN].
- **Vì sao Zalo quan trọng:** khách 45–60 tuổi nhắn hằng ngày bằng Zalo 75%, Messenger 10% (Z7). Phễu nên là: QC Meta → Messenger → **xin số, chuyển Zalo OA của chủ đầu tư**. [NHẬN ĐỊNH]
- **Chưa kiểm:** điều khoản Zalo về tự động hoá **tài khoản Zalo cá nhân** (nhắn hàng loạt, kết bạn tự động). Không đưa vào sản phẩm cho đến khi đọc được. Thêm vào đó, dự thảo L2 sẽ cấm nhắn QC bằng số điện thoại từ 2027.

### Câu 4. Luật Việt Nam cho phép, nhưng có 4 điều kiện; điều kiện dữ liệu khách là nặng nhất

Trục chia: 4 nhóm nghĩa vụ theo việc app làm (dữ liệu khách · nội dung AI · nội dung QC bất động sản · tin nhắn chào hàng). Mọi dòng: **cần luật sư xác nhận**.

| Nhóm | Điều kiện [NHẬN ĐỊNH] | Căn cứ | Mức nặng với đội 1–3 người |
|---|---|---|---|
| Dữ liệu khách (sổ khách nhiều chủ đầu tư) | Chủ đầu tư là **bên kiểm soát**, app là **bên xử lý**; ký hợp đồng xử lý dữ liệu với từng khách; để riêng dữ liệu từng khách. App vận hành phần mềm tự động, phân tích, chấm khách bằng AI thay chủ đầu tư → nhiều khả năng là **"dịch vụ xử lý dữ liệu cá nhân" cần Giấy chứng nhận Bộ Công an**; dùng máy chủ hoặc AI nước ngoài → hồ sơ chuyển xuyên biên giới; lưu dữ liệu tài khoản người dùng tại Việt Nam (NĐ 333) | R2; SU-4 mục 2.6, câu 5; M12 | **Nặng nhất.** Cần ≥ 3 nhân sự đủ năng lực. Đường né (như SU-4): khách tự đứng tên tài khoản, dữ liệu nằm ở tài khoản của khách (Google Sheet, Meta), app không giữ bản sao |
| Nội dung do AI tạo | Chatbot: câu chào "đây là trợ lý AI của [chủ đầu tư]" (Luật AI Điều 11 khoản 1; cũng là điều Messenger đòi khi luật bắt, M8). Ảnh, video AI tái hiện cảnh thật (phối cảnh hạ tầng xong, khách đông): gắn nhãn dễ thấy (khoản 4). Bài chữ AI viết: chỉ phải báo khi có thể gây nhầm về sự kiện, nhân vật thật (khoản 3). Chatbot ít nhất rủi ro trung bình → hồ sơ phân loại, thông báo Bộ KHCN trước khi dùng | L3; R1 | Vừa. Làm một lần cho sản phẩm, dùng chung cho mọi khách |
| Nội dung QC bất động sản | QC khớp thông tin dự án đã công khai; không hứa lời; không so sánh đối thủ; ảnh người thật phải có đồng ý; người chuyển tải QC chịu trách nhiệm khi nội dung sai → app và startup **có thể cùng chịu** với chủ đầu tư | R3; R4; checklist §H (H1–H11) | Vừa. Bộ kiểm luật §H của Yên Thế đã là một mô-đun bán được |
| Tin nhắn chào hàng | Hiện tại: NĐ 91/2020 (QC phải được đồng ý trước; chi tiết số tin/ngày chưa đối chiếu [CẦN XÁC NHẬN]). Từ 2027 (nếu dự thảo thông qua): áp cả Zalo, Messenger; chỉ nhắn QC bằng tên định danh; khách lạ chỉ 1 tin xin đăng ký; 7–22 giờ; gắn nhãn QC; có nút từ chối | L1; L2 | Nhẹ nếu app chỉ trả lời khách tự nhắn; nặng nếu app định nhắn hàng loạt |

- **Môi giới trá hình [NHẬN ĐỊNH]:** app trả lời, tư vấn, hẹn xem đất thay chủ đầu tư là công cụ của chủ đầu tư. Nhưng nếu startup **ăn tiền theo hợp đồng bán được** hoặc **đứng ra đàm phán**, việc đó gần định nghĩa môi giới, cần doanh nghiệp môi giới có người có chứng chỉ (R4). Giữ giá là phí phần mềm/dịch vụ theo tháng; sale của chủ đầu tư chốt và ký.
- **Luật Kinh doanh bất động sản đang được sửa** (R5): theo dõi phần quảng cáo, công khai thông tin. [CẦN XÁC NHẬN]

### Câu 5. Meta đang tự làm lớp "quản lý QC" và "tự trả lời"; khoảng trống của startup là luật Việt Nam, Zalo và số bán hàng thật

Xem mục 4.

## 4. Góc nhìn thời AI [NHẬN ĐỊNH]

**Nền tảng đang làm thay phần nào:**
- **Quản lý QC:** Meta Ads AI Connectors cho chủ tài khoản nối thẳng AI (Claude, công cụ khác) vào QC, không cần app, không cần App Review (M13). Một chủ đầu tư rành máy có thể tự làm điều app định bán. Kết nối `meta-ads` dự án đang dùng là đúng loại này (R6).
- **Tự trả lời tin nhắn:** Meta Business Agent miễn phí hiện tại, sàng lọc khách, đặt lịch, chuyển người thật (M14); sau sẽ thu phí qua Meta One (M15).
- **Tạo mẫu QC:** công cụ tạo video, ảnh AI của Meta đã thành mảng doanh thu lớn (M16).
- **Nền tảng có thể cắt bên thứ ba bất cứ lúc nào:** WhatsApp đã cấm trợ lý AI đa năng của bên thứ ba từ 15/01/2026 (M17); Groups API bị bỏ chỉ với 90 ngày báo trước (M10).

**Cái nền tảng không làm cho chủ đầu tư bất động sản Việt Nam:**
1. **Kiểm luật Việt Nam trước khi đăng:** Luật KDBĐS Điều 6, Luật QC, Luật AI Điều 11, sổ thông điệp KHOÁ/MỞ của từng dự án. Meta chỉ kiểm chính sách của Meta.
2. **Nối hai nền tảng:** Meta QC → Messenger → Zalo OA → sổ khách. Business Agent của Meta không chạy trên Zalo; Zalo không có AI QC kiểu Meta.
3. **Đo bằng số bán hàng thật:** lượt xem đất, cọc, hợp đồng do đội bán ghi, rồi gửi ngược về Meta bằng Conversions API. Meta chỉ thấy cuộc trò chuyện.
4. **Tiếng nói và luật của từng dự án:** giá "chỉ khoảng 1 tỷ", không mã lô, dòng pháp lý; Business Agent tự nói dễ hứa sai.
5. **Người thật chịu trách nhiệm và hồ sơ pháp lý:** hợp đồng xử lý dữ liệu, hồ sơ phân loại AI, nhãn AI. Đây là việc người ở tỉnh không tự làm được.

**Hệ quả cho H0:** bán "công cụ đăng, chạy QC, trả lời" là bán thứ Meta sắp cho không. Bán **"kết quả marketing đúng luật Việt Nam, đo bằng lượt xem đất, chạy trên Meta + Zalo"** thì còn khoảng trống. Lõi sản phẩm nên dựng **trên** công cụ của Meta (Ads AI Connectors, Business Agent khi có tiếng Việt) thay vì làm lại chúng.

## 5. Hệ quả

### 5.0 Bảng 6 việc: app được làm gì

| Việc | Kết luận | Điều kiện hoặc lý do | Căn cứ |
|---|---|---|---|
| Tạo bài (chữ, ảnh, video bằng AI) | **Được làm** | Không cần quyền nền tảng. Phải: kiểm luật QC bất động sản; nhãn cho ảnh, video AI tái hiện cảnh thật; người của khách duyệt trước khi đăng | L3; R3; R4 |
| Đăng Fanpage | **Làm có điều kiện** | Qua Pages API; người dùng có nhiệm vụ tạo nội dung trên Trang; app qua xác minh doanh nghiệp, Tech Provider, App Review quyền đăng. Ca mẫu: dùng mức Tiêu chuẩn khi người của khách có vai trò trên app | M1, M4, M6 |
| Đăng nhóm bằng nick (trình duyệt tự động) | **Không nên làm** | Groups API đã bỏ; điều khoản cấm truy cập tự động, cấm app thu thập đăng nhập, nick phải cá nhân, tên thật; spam. Thay bằng: app soạn bài, người thật tự đăng | M9, M10, M11, M12 |
| Quản lý quảng cáo | **Làm có điều kiện** | Marketing API bậc Full (App Review, ≥ 500 lệnh/15 ngày) và chủ tài khoản bấm cho phép; hoặc dùng Meta Ads AI Connectors dưới quyền của chủ tài khoản. Chủ đầu tư phải là chủ TK QC, Trang, danh mục; startup chỉ được giao vai trò | M2, M13 |
| Đọc số | **Làm có điều kiện** | Quyền `ads_read`, quyền đọc số Trang qua App Review; số bán hàng từ sổ khách là dữ liệu cá nhân → hợp đồng xử lý dữ liệu; gửi ngược bằng Conversions API: điều kiện [CẦN XÁC NHẬN] | M2, M18, R2 |
| Tự trả lời tin nhắn (Messenger, Zalo OA) | **Làm có điều kiện** | Messenger: trong 24 giờ (QC: 7 ngày), trả lời ≤ 30 giây, câu chào báo là AI, chuyển người thật bằng `HUMAN_AGENT`. Zalo: gói Tăng trưởng, trong 7 ngày từ tương tác cuối. Luật AI: hồ sơ phân loại, thông báo Bộ KHCN. Không nhắn chào hàng cho người chưa nhắn | M7, M8, Z5, Z6, L3, R1, L2 |

### 5.a Cho startup tự chi
**Nên làm:**
1. Đi **đường chính thức ngay từ đầu**, nộp hồ sơ Meta sớm (4–8 tuần [ƯỚC TÍNH]); trong lúc chờ, phục vụ khách bằng quyền khách giao cho người của startup trên tài khoản của chính khách.
2. **Khách đứng tên mọi tài sản:** Trang, danh mục doanh nghiệp, tài khoản QC, Zalo OA, sổ khách. Startup chỉ được giao vai trò, **không giữ mật khẩu**. Vừa đúng M12, vừa giảm gánh "dịch vụ xử lý dữ liệu" (R2).
3. Dựng **trên** công cụ Meta (Ads AI Connectors; Business Agent khi có tiếng Việt), bán phần Meta không làm: kiểm luật Việt Nam, nối Zalo, đo lượt xem đất.
4. Đóng gói **bộ hồ sơ pháp lý dùng chung**: mẫu hợp đồng xử lý dữ liệu, hồ sơ phân loại AI, câu chào "trợ lý AI", nhãn ảnh AI, câu "không phải dịch vụ môi giới".
5. Giá theo tháng (phí dịch vụ), **không** theo hợp đồng bán được.

**Không nên làm:**
1. Không bán tính năng đăng nhóm tự động, nick clone, nhắn Zalo cá nhân hàng loạt.
2. Không giữ bản sao sổ khách của nhiều chủ đầu tư trên máy chủ của startup khi chưa có ý kiến luật sư về Giấy chứng nhận dịch vụ xử lý dữ liệu.
3. Không cạnh tranh bằng "chatbot" hay "bảng điều khiển QC": Meta đang cho không.

### 5.b Áp vào dự án Yên Thế (Chặng 1, tới 30/11)
1. **Nhánh đăng nhóm bằng nick đang chạy hằng ngày là trái điều khoản Meta** (M9; lịch dùng trình duyệt tự động, nick clone). Đề xuất cho người dùng quyết: giữ ở mức thử nhỏ hiện tại, **không mở rộng, không đưa vào app**, ghi rõ rủi ro mất nick; tính dừng hẳn nếu đến 09/11 vẫn ≈ 0 SĐT. Người giữ D: người dùng. [NHẬN ĐỊNH]
2. **Nối Fanpage chủ đầu tư bằng Pages API ở mức Tiêu chuẩn** (luồng C2 đang Đỏ): admin Trang của chủ đầu tư được thêm vai trò trên app của dự án → không cần App Review cho ca mẫu (M1). Phải: chủ đầu tư là chủ Trang (khớp điều kiện H7 của checklist).
3. **Tin nhắn:** câu chào tự động của QC thêm "Em là trợ lý tự động của [chủ đầu tư]…" (M8, L3), mời để lại số hoặc nhắn Zalo ngay (Z7); người thật trả lời trong 7 ngày bằng thẻ người thật.
4. **Zalo OA của chủ đầu tư:** mở và xác thực OA đứng tên công ty; dùng trang quản lý OA bằng tay (miễn phí) cho Chặng 1; chỉ mua gói Tăng trưởng 2,5 tr/năm khi app thật sự nối API.
5. **Ảnh, video AI trong QC** (phối cảnh, cảnh đông khách) gắn chữ "Ảnh minh hoạ tạo bằng AI". Thêm 1 luật vào checklist §H. [NHẬN ĐỊNH]

### 5.c Đưa gì vào khung chuẩn nhân rộng
1. **Danh sách kiểm "giấy phép nền tảng" mỗi khách mới** (≤ 1 ngày cài): chủ đầu tư là chủ Trang, danh mục, TK QC, OA; đã giao vai trò cho startup; đã bấm cho phép app; đã ký hợp đồng dịch vụ + hợp đồng xử lý dữ liệu; câu chào AI và nhãn AI đã bật.
2. **Hồ sơ app một lần cho mọi khách:** xác minh doanh nghiệp, Tech Provider, App Review (danh sách quyền), Marketing API Full, hồ sơ phân loại AI, thông báo Bộ KHCN.
3. **Danh sách cấm cứng trong code:** không lưu mật khẩu Meta, Zalo; không điều khiển trình duyệt để đăng; không nhắn chào hàng ngoài cửa sổ; dữ liệu mỗi khách tách riêng (M12).
4. **Mô-đun kiểm luật:** checklist §H + Luật AI Điều 11 + luật tin nhắn 2027, chạy trước mọi lần đăng và mọi mẫu QC.
5. **Lịch theo dõi luật chơi mỗi quý:** chính sách Meta (Business Agent, Ads AI Connectors, Messenger), gói Zalo, nghị định chống tin rác, Luật KDBĐS sửa đổi, nghị định hướng dẫn Điều 11 Luật AI.

## 6. Điều chưa biết; câu cần hỏi

**Luật sư:**
1. App giữ và chấm sổ khách cho nhiều chủ đầu tư có phải "kinh doanh dịch vụ xử lý dữ liệu cá nhân" (NĐ 356 Điều 21) cần Giấy chứng nhận không? Nếu dữ liệu nằm ở tài khoản Google, Meta của chủ đầu tư và startup chỉ có quyền truy cập thì sao?
2. Chatbot trả lời khách mua đất cho chủ đầu tư có phải rủi ro trung bình, phải thông báo Bộ KHCN không? Ai làm thủ tục: startup (nhà cung cấp) hay chủ đầu tư (bên triển khai)?
3. Bài chữ do AI viết, sale duyệt, có phải ghi nhãn AI không (Điều 11 khoản 3)? Ảnh phối cảnh 3D thường (không AI) so với ảnh AI khác nhau thế nào?
4. Startup soạn, đăng và chạy QC cho chủ đầu tư có là "người kinh doanh dịch vụ quảng cáo" hay "người chuyển tải", chịu trách nhiệm liên đới đến đâu?
5. Thu phí thưởng theo lượt xem đất hoặc hợp đồng có biến startup thành môi giới (Luật KDBĐS Điều 61) không?
6. NĐ 91/2020 hiện có áp cho tin nhắn Zalo OA, Messenger không; giới hạn số tin QC/ngày; dự thảo thay thế đã ban hành chưa.

**Meta:** thời gian App Review hiện nay cho `pages_manage_posts`, `pages_messaging`, `ads_management`; giấy tờ xác minh doanh nghiệp Việt Nam; Business Agent có tiếng Việt, có mở ở Việt Nam chưa, giá; Ads AI Connectors có cho agency dùng thay nhiều khách không; Conversions API cho app nhiều khách cần quyền gì.

**Zalo:** tiêu chuẩn duyệt mẫu ZNS (có cho nội dung chào bán đất không); chính sách quảng cáo Zalo cho bất động sản (giấy tờ dự án); điều khoản tự động hoá tài khoản Zalo cá nhân; chương trình đối tác cho app bên thứ ba; hạn mức chính xác của 4 gói từ 01/06/2026.

**Khách (chủ đầu tư):** có chịu đứng tên Trang, TK QC, OA và giao vai trò cho startup không; có chịu ký hợp đồng xử lý dữ liệu không; sale có chịu ghi "đã xem đất, đã cọc" vào sổ để gửi ngược về Meta không.

## 7. Danh sách nguồn

**Meta, chính thức (ĐÃ ĐỌC TOÀN VĂN, tra 21/10/2026):**
- Mức truy cập: https://developers.facebook.com/docs/graph-api/overview/access-levels
- Marketing API, uỷ quyền và bậc truy cập: https://developers.facebook.com/docs/marketing-api/get-started/authorization
- Giới hạn gọi: https://developers.facebook.com/docs/graph-api/overview/rate-limiting
- Xác minh quyền truy cập cho Tech Provider (06/2022): https://developers.facebook.com/blog/post/2022/06/02/access-verification-process-for-tech-provider-apps/
- Pages API tổng quan: https://developers.facebook.com/docs/pages-api/overview
- Chính sách Messenger Platform: https://developers.facebook.com/docs/messenger-platform/policy/policy-overview
- Graph API v19, bỏ Groups API (23/01/2024): https://developers.facebook.com/blog/post/2024/01/23/introducing-facebook-graph-and-marketing-api-v19/
- Điều khoản nền tảng (cập nhật 03/02/2026): https://developers.facebook.com/terms/
- Conversions API: https://developers.facebook.com/docs/marketing-api/conversions-api
- Điều khoản Facebook (hiệu lực 01/01/2025): https://www.facebook.com/terms.php
- Tiêu chuẩn cộng đồng, Spam: https://transparency.meta.com/policies/community-standards/spam/
- Meta Ads AI Connectors (29/04/2026, cập nhật 16/07/2026): https://www.facebook.com/business/news/meta-ads-ai-connectors
- Meta Business Agent (06/2026): https://about.fb.com/news/2026/06/meta-business-agent/
- 2026: AI Drives Performance (28/01/2026): https://about.fb.com/news/2026/01/2026-ai-drives-performance/

**Zalo, chính thức (ĐÃ ĐỌC TOÀN VĂN):**
- Bảng giá ZNS: https://zalo.solutions/zns/pricing
- Giới thiệu ZBS Template Message: https://zalo.solutions/business-message/guidelines/intro
- Tin Tư vấn: https://oa.zalo.me/home/documents/guides/tin-tu-van
- Bảng giá dịch vụ OA: https://zalo.solutions/oa/pricing
- Mở hỏng (chỉ có tiêu đề): https://developers.zalo.me/docs/official-account/tin-nhan/tong-quan

**Luật Việt Nam:**
- Dự thảo nghị định chống tin nhắn rác, thư điện tử rác, cuộc gọi rác (Bộ Công an, 09/2026), ĐÃ ĐỌC TOÀN VĂN các điều dẫn: https://bocongan.gov.vn/media/bca-media/library-20260909084715-f7e1171f-eb0c-4ae2-97ed-7017b136dc65-1-nghi-inh-thay-the-n-91.doc ; bản so sánh (chưa mở): https://bocongan.gov.vn/media/bca-media/library-20260909084715-c3d4dec4-0f78-459d-96de-3293d10b69b5-4-ban-so-sanh-du-thao.docx
- Luật Trí tuệ nhân tạo 134/2025/QH15, Điều 11: bản Công báo theo SU-4 mục 7 [L134], ĐÃ ĐỌC TOÀN VĂN
- Luật KDBĐS 29/2023/QH15, trang Công báo (chỉ thông tin tệp): https://congbao.chinhphu.vn/tai-ve-van-ban-so-29-2023-qh15-40868-47862 ; trang Chính phủ: https://vanban.chinhphu.vn/?pageid=27160&docid=209624
- NQ 84/NQ-CP về dự án luật sửa 4 luật (kết quả tìm kiếm): https://vanban.chinhphu.vn/?docid=210361&pageid=27160

**Bên thứ ba (NGUỒN-TRÍCH, chỉ để tìm):**
- 360dialog, trở thành Tech Provider: https://docs.360dialog.com/partner/get-started/tech-providers/becoming-a-meta-tech-provider-a-step-by-step-guide
- respond.io, WhatsApp cấm chatbot đa năng: https://respond.io/blog/whatsapp-general-purpose-chatbots-ban
- techcrunch, Business Agent toàn cầu: https://www.techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/
- techpoint.africa, bỏ Groups API: https://techpoint.africa/2024/02/06/meta-facebook-disrupts-scheduling
- eSMS, câu hỏi về Zalo OA (QUẢNG CÁO, nhà bán): https://helpcenter.esms.vn/cau-hoi-thuong-gap/zalo-oa
- SDK RedAI Zalo (tài liệu lập trình bên thứ ba): https://unpkg.com/@warriorteam/redai-zalo-sdk@1.11.1/docs/CONSULTATION_SERVICE.md
- luatvietnam, điều kiện môi giới từ 01/8/2024: https://luatvietnam.vn/linh-vuc-khac/dieu-kien-hanh-nghe-moi-gioi-bat-dong-san-tu-2025-883-96769-article.html

**Dùng lại (không đọc lại):** SU-4 (`D:\0. AI\goi-phong-kham\nghien-cuu\startup\su-4-phap-ly-startup-ai-y-te.md`), NC-A (`D:\0. AI\goi-phong-kham\nghien-cuu\nc-a-phap-ly-du-lieu-va-ai.md`), NC-F2 (`D:\0. AI\goi-phong-kham\nghien-cuu\nc-f2-quang-cao-luat-su-duoc-thi-truong.md`), Muse (`D:\0. AI\nghien-cuu\2026-10-14-cach-mo-muse-ai.md`: Muse chỉ ở Mỹ, Canada; Meta AI có ở Việt Nam), `workspace/research/2026-10-15-chuyen-mon-qc-bds-nguon.md`, `workspace/research/2026-10-14-best-practice-quang-cao-bds.md`, `workspace/compliance-checklist.md` §D, §H, `workspace/STATE.md`.
