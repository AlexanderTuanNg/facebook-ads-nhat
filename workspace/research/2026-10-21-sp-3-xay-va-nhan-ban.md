# SP-3. Làm được: đúng có điều kiện — đi được từ dịch vụ sang sản phẩm, nhưng phải đổi "động cơ" sang API, tách lõi khỏi dữ liệu Yên Thế, và chấp nhận phần điều phối khoá vào Claude

> **Đính chính sau kiểm độc lập 21/10** (`2026-10-21-sp-kiem-doc-lap.md`): (1) tóm tắt ý 5: chi phí AI **thường 1,2–2,5 tr/khách/tháng, xấu nhất ≈ 8,6 tr** (toàn Opus, không bộ nhớ đệm — bảng 3.3e), không phải "~4,6 tr"; (2) xAI "**ngừng hỗ trợ**" (deprecated) đường tương thích Anthropic, chưa gỡ hẳn; (3) Muse của Meta đã có bản 1.2, 1.3 và chế độ giá rẻ đổi dữ liệu; giới hạn "chỉ ở Mỹ" [CẦN XÁC NHẬN]. Nội dung gốc bên dưới giữ nguyên.

> Lập 21/10/2026, phiên SP-3 của `workspace/research/2026-10-21-sp-00-chuong-trinh.md`. Phạm vi: câu hỏi 1–5 của SP-3 (đường đi chuẩn, khung nhân bản, đóng gói kỹ thuật, giá và lãi phần riêng ngành marketing, đội 1–3 người).
> **Ngân sách đã dùng: 14 lượt tìm (trên 25), 19 lần mở trang (trên 20).** Trong đó **15 nguồn đọc trọn có dùng**, 1 đọc một phần (trang evals của Anthropic, 100k/153k ký tự), 1 mở nhưng không có thông tin cần (Wikipedia), 2 lỗi (Inc. 403, blog Haldar ngắt kết nối). Đọc thêm trong máy: SU-3, SU-5 mục 3.4/3.6, SU-8 mục 0, 8–15, README + CHANGELOG khung 0.2.4, lộ trình sản phẩm bản 1, nghiên cứu Muse 14/10, tên file và mô tả của dự án.
> **Chỗ còn yếu (đọc trước khi dùng):** (1) **không tìm được nguồn nào cho ngưỡng số** (bao nhiêu khách, bao nhiêu % tự động) để chuyển giai đoạn — các mốc ở mục 3.1 là [NHẬN ĐỊNH] của phiên này; (2) ví dụ "dịch vụ đóng gói → phần mềm" có thật nhưng **đều là nguồn tự kể hoặc trích lại, không có số kiểm toán**; ví dụ Designjoy chỉ có nguồn tổng hợp, số lệch nhau; (3) **chi phí AI mỗi khách là ước tính từ cỡ file và vài số token đã ghi trong log**, chưa đo trên một tuần thật; (4) giá dịch vụ marketing bất động sản ở Việt Nam **không tìm được bảng giá công khai** (để SP-1); (5) chuyện dùng gói Claude trả phí cho việc tự động phục vụ khách là **đọc điều khoản, chưa hỏi Anthropic, chưa có luật sư**.
> Không gặp trang nào ra lệnh cho AI. Không dùng trình duyệt, không đụng Meta, Drive, `config/`, `tools/`, cơ sở dữ liệu; chỉ đọc tên file, cỡ file và đếm chữ bằng lệnh đọc.
> Quy ước: **ĐÃ ĐỌC TOÀN VĂN** · **NGUỒN-TRÍCH** (kết quả tìm kiếm, đọc một phần, bài thứ cấp) · **QUẢNG CÁO** (trang tự nói về mình) · **[NHẬN ĐỊNH]** · **[ƯỚC TÍNH]** (có cách tính) · **[CẦN XÁC NHẬN]** · **[DỮ LIỆU]** (file của dự án). Tỷ giá dùng để so cỡ: 1 USD ≈ 26.000 đ (theo SU-3, [CẦN XÁC NHẬN] tỷ giá ngày dùng).

Giải thích nhanh thuật ngữ dùng nhiều:
- **MVP làm tay đóng vai máy** (concierge / Wizard-of-Oz): khách thấy "sản phẩm", phía sau là người làm tay. Mục đích: học đúng việc gì cần tự động trước khi viết phần mềm.
- **Dịch vụ đóng gói** (productized service): dịch vụ có phạm vi cố định, giá cố định theo tháng, quy trình lặp lại như sản phẩm.
- **Lõi dùng chung / cấu hình riêng**: phần mã và luật giống nhau cho mọi khách / phần chỉ của một khách (tên dự án, luật riêng, ảnh, nhóm, tài khoản).
- **Cài riêng từng khách** (single-tenant, "silo") / **nhiều khách một hệ thống** (multi-tenant, "pool").
- **Kỹ sư làm tại chỗ khách** (forward deployed engineer, FDE): người kỹ thuật ngồi cùng khách để nối hệ thống, chỉnh agent, mang bài học về sản phẩm.
- **Mức tự chạy**: số bước còn phải làm tay mỗi tuần, chia theo loại (xem mục 3.2d).

---

## 1. Tóm tắt

1. **Làm được: ĐÚNG CÓ ĐIỀU KIỆN.** Đường đi "làm tay → dịch vụ đóng gói → phần mềm" có thật và hợp đội nhỏ tự chi, nhưng 3 điều kiện dưới đây chưa đạt; chưa đạt thì không nên bán cho dự án thứ 2. [NHẬN ĐỊNH]
2. **Điều kiện 1 — đổi "động cơ".** Điều khoản người dùng cá nhân của Anthropic cấm truy cập "bằng bot, script" trừ khi dùng API key hoặc được cho phép rõ; tài liệu Agent SDK ghi bên thứ ba **không được** dùng đăng nhập claude.ai cho sản phẩm của mình. → Cách đóng gói 1 của lộ trình bản 1 ("Claude Desktop làm động cơ, mỗi máy 1 tài khoản Claude") chỉ ổn khi **tài khoản đứng tên khách và khách tự dùng**; bán như sản phẩm thì phải chuyển sang **API key + Agent SDK** (Điều khoản thương mại). (D1, D2; ĐÃ ĐỌC TOÀN VĂN; cần luật sư hoặc Anthropic xác nhận cách đọc)
3. **Điều kiện 2 — tách lõi.** Dự án hiện **chưa dựng trên bộ khung 0.2.4** (không có `.khung.json`; `tools/db.py` 386 dòng khác hẳn `db.py` của khung 927 dòng); 8/25 file `tools/*.py` có chữ riêng Yên Thế; playbook có 18 chỗ, checklist 8 chỗ. "Nhân bản bằng 1 thư mục cấu hình" **chưa đúng ở thời điểm này**. (D20, D21; [DỮ LIỆU])
4. **Điều kiện 3 — chấp nhận khoá một phần.** Lớp điều phối agent (Claude Code, Agent SDK) chỉ chạy model Claude; xAI đã **bỏ** đường tương thích Anthropic; API Muse của Meta mới mở cho lập trình viên ở Mỹ. → "Không khoá vào 1 nhà AI" chỉ làm được ở **lõi Python** (lint, đăng bài, đọc số) và ở các bước gọi model đơn lẻ (viết bài, chấm bài) qua một lớp gọi model; phần agent tự điều phối thì khoá vào Claude. (D9, D10, D11; ĐÃ ĐỌC TOÀN VĂN / NGUỒN-TRÍCH)
5. **Chi phí AI không phải nút thắt:** khối lượng như Yên Thế (84 bài/tuần + báo cáo 17:30 mỗi ngày + báo cáo thứ Hai) tốn khoảng **1–2 triệu đ/khách/tháng** với Sonnet 5.5, tới **~4,6 triệu** nếu toàn Opus 5.5 không tận dụng bộ nhớ đệm. Nút thắt là **giờ người** (hỗ trợ, duyệt, đăng nhập lại Facebook). (D5–D7, mục 3.3e; [ƯỚC TÍNH])
6. **Lịch 24/7:** lịch đám mây của Claude Code **không đọc được file trong máy** và cần kho GitHub; lịch Desktop cần **máy bật**. → Phần đăng nhóm bằng trình duyệt (Playwright, phiên Facebook trong máy) **không đưa lên đám mây được**; chỉ phần đi API chính thức (Trang, quảng cáo, báo cáo) mới chạy đám mây. (D3, D4; ĐÃ ĐỌC TOÀN VĂN)
7. **Bằng chứng bác quan trọng nhất:** a16z (2020) cho thấy công ty AI thường **trông như công ty dịch vụ** — biên gộp 50–60%, 40–50% chức năng nằm ở "ca lạ", mỗi khách đòi chỉnh riêng; Toolza (2025) kể "bẫy làm riêng từng khách" khi chuyển từ dịch vụ sang sản phẩm. → Rủi ro lớn nhất không phải kỹ thuật mà là **thành công ty làm thuê theo yêu cầu**. (D13, D17; ĐÃ ĐỌC TOÀN VĂN)
8. **Dịch vụ đóng gói tự nó đã có lãi, không bắt buộc phải thành phần mềm:** Audience Ops (dịch vụ viết blog trọn gói) có lãi, bán được giá "high six-figure"; phần mềm người sáng lập làm sau (ProcessKit) là **sản phẩm khác**, không phải bản tự động của dịch vụ. (D15, D16; ĐÃ ĐỌC TOÀN VĂN / NGUỒN-TRÍCH)
9. **Cài riêng từng khách là đúng cho đội 1–3 người năm đầu** (dễ tính chi phí từng khách, cách ly dữ liệu và tài khoản Facebook của từng chủ đầu tư); nhiều khách một hệ thống chỉ khi > ~10 khách và đã qua duyệt app Meta (SP-2). (D12; SU-5 mục 3.4; [NHẬN ĐỊNH])
10. **Khung chuẩn nhân bản** (mục 5c): 1 thư mục `du-an/<mã>/` gồm 9 nhóm file cấu hình; cài khách mới 7 bước trong ≤ 1 ngày; bộ kiểm bắt buộc 4 lớp; 6 số đo mỗi tuần; 4 cổng. Đã có khoảng **60%** thành phần (luật, ca kiểm, rubric, lịch, đọc số QC); **thiếu**: tách cấu hình, sổ tay cài, bộ ca kiểm chung ngành, đo mức tự chạy bằng máy, đường Fanpage chính thức. [DỮ LIỆU, NHẬN ĐỊNH]
11. **Đội:** 1 người + agent chạy được 1–3 dự án; vai không giao agent được là **bán hàng, giữ quan hệ chủ đầu tư, bấm tiền QC, đăng nhập, chịu trách nhiệm pháp lý**. Thuê người thứ 2 (vận hành, hỗ trợ tại tỉnh) khi giờ hỗ trợ vượt ~60 giờ/tháng, khoảng 4–6 dự án (theo SU-8 mục 12). [ƯỚC TÍNH]

---

## 2. Bảng dữ kiện

| # | Dữ kiện | Nguồn (link, ngày tra) | Trạng thái |
|---|---|---|---|
| D1 | Điều khoản người dùng cá nhân của Anthropic (hiệu lực 08/10/2025) áp cho Claude.ai, Claude Pro "cho cá nhân". Cấm truy cập dịch vụ "bằng cách tự động hoặc không phải người, qua bot, script…", **trừ khi** dùng API key của Anthropic hoặc Anthropic cho phép rõ. Cấm bán lại dịch vụ | anthropic.com/legal/consumer-terms (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN |
| D2 | Tài liệu Agent SDK: "trừ khi được duyệt trước, Anthropic không cho bên thứ ba cung cấp đăng nhập claude.ai hoặc hạn mức gói cho sản phẩm của họ, kể cả agent dựng bằng Agent SDK"; phải dùng API key. Agent SDK chịu **Điều khoản thương mại**, kể cả khi dùng để phục vụ khách của mình. SDK có sẵn công cụ, hook, agent con, MCP, quyền, phiên, skill, plugin; chạy bằng Python và TypeScript. Không được gọi sản phẩm là "Claude Code" | code.claude.com/docs/en/agent-sdk/overview (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN |
| D3 | Lịch đám mây của Claude Code (tên cũ routines): có ở gói Pro, Max, Team, Enterprise; chạy trên máy chủ Anthropic khi máy mình tắt; **thuộc tài khoản cá nhân, trừ vào hạn mức gói**; mỗi lần chạy clone kho GitHub mới, **không đọc file trong máy**; tối thiểu 1 giờ/lần; 100 lần chạy theo lịch mỗi giờ mỗi tài khoản; đang ở bản "research preview", có thể đổi | code.claude.com/docs/en/routines (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN |
| D4 | So 3 cách lên lịch: đám mây (không cần máy bật, không file trong máy, tối thiểu 1 giờ); **Desktop (cần máy bật, đọc được file trong máy, tối thiểu 1 phút)**; `/loop` (cần phiên mở, tự hết hạn sau 7 ngày) | code.claude.com/docs/en/scheduled-tasks (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN |
| D5 | Giá API (USD/triệu token, vào/ra): **Opus 5.5: 4 / 20**, đọc bộ nhớ đệm 0,20; **Sonnet 5.5: 2 / 10**, đọc bộ nhớ đệm 0,10; **Haiku 5.5: 0,10 / 0,50** (lời nhắc ≤ 100.000 token; dài hơn: 0,50 / 2,50). Ghi bộ nhớ đệm 5 phút: Opus 5,5 5; Sonnet 2,50. Xử lý theo lô (Batch) giảm 50%. Chạy chỉ ở Mỹ (`inference_geo: us`) nhân 1,1 | platform.claude.com/docs/en/about-claude/pricing (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN |
| D6 | Tìm web qua API: **10 USD/1.000 lượt tìm** cộng token; đọc trang (web fetch) không tính thêm. Managed Agents (agent chạy trên máy chủ Anthropic): token theo giá thường + **0,08 USD/giờ phiên chạy**; không có giảm giá Batch | như D5 | ĐÃ ĐỌC TOÀN VĂN |
| D7 | Số token đã ghi ở dự án: 4 tác nhân soạn việc ngày 20/10 tổng **~1,02 triệu token**; hội đồng 5 tác nhân 15/10 **~1,09 triệu**; 1 tác nhân nghiên cứu web 15/10 **~282 nghìn**. Bài nhóm trung bình **2.259 byte** (12 bài ngày 26/10). Bộ ngữ cảnh chính (CLAUDE.md, STATE, brief, playbook, checklist, rubric, thẻ luật, 8 tác nhân, 2 skill, luật top-down) **~163 KB** | `workspace/reports/log.md` dòng 272, 274, 298; `content/2026-10-26/`; đo cỡ file 21/10 | [DỮ LIỆU] |
| D8 | Bộ khung 0.2.4 ghi: Sonnet 5.5 giá API 2/10, Opus 5.5 4/20; một lượt kiểm chéo tốn **230–480 nghìn token, 13–21 phút** | `khung-agent-marketplace/CHANGELOG.md` mục 0.2.4, 0.2.3 | [DỮ LIỆU] (khớp D5) |
| D9 | Claude Code đi qua cổng trung gian (LLM gateway) bằng `ANTHROPIC_BASE_URL` hoặc biến riêng Bedrock, Vertex, Foundry. Khi dò model, Claude Code **chỉ giữ tên có chữ "claude" hoặc "anthropic"**; tài liệu không nói chạy được model khác | code.claude.com/docs/en/llm-gateway, llm-gateway-protocol (kết quả tìm, 21/10/2026) | NGUỒN-TRÍCH; chạy model khác trong Claude Code [CẦN XÁC NHẬN] |
| D10 | xAI: giá Grok (USD/triệu token, lời nhắc < 200k): grok-4.7 **2 / 6** (đệm 0,50); grok-4.3 **1,25 / 2,50**; ≥ 200k token tính gấp đôi. API tương thích OpenAI; **đường tương thích Anthropic (`/v1/messages`) "đã bỏ hoàn toàn"**, khuyên chuyển sang Responses API | docs.x.ai/docs/models (ĐÃ ĐỌC TOÀN VĂN); docs.x.ai/developers/rest-api-reference/inference/legacy (kết quả tìm) — 21/10/2026 | ĐÃ ĐỌC TOÀN VĂN (giá); NGUỒN-TRÍCH (bỏ tương thích) |
| D11 | Meta: Muse Spark 1.1 qua Meta Model API **1,25 / 4,25 USD** mỗi triệu token, **chỉ mở cho lập trình viên ở Mỹ**; Muse (agent cá nhân) chỉ có ở Mỹ, Canada | `D:\0. AI\nghien-cuu\2026-10-14-cach-mo-muse-ai.md` dòng 70, 74 (dẫn dev.meta.ai, about.fb.com) | Dẫn lại (nguồn gốc ghi ĐÃ ĐỌC 14/10; có thể đã đổi [CẦN XÁC NHẬN]) |
| D12 | AWS (khung SaaS): cài riêng từng khách ("silo") cách ly mạnh nhất, **dễ gắn chi phí cho từng khách**, nhưng tốn nhất và khó gom số liệu toàn bộ khách; dùng chung ("pool") rẻ nhất, cách ly yếu nhất; "bridge" là lai. SaaS đòi **tự động hoá việc đón khách mới** | docs.aws.amazon.com SaaS Lens, SaaS Tenant Isolation (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN trang tenant isolation (ghi "chỉ để tham khảo lịch sử"); phần silo/pool là NGUỒN-TRÍCH |
| D13 | a16z, Casado và Bornstein (16/02/2020): biên gộp công ty AI thường **50–60%** so với 60–80%+ của phần mềm thường, công ty dịch vụ 30–50%; người trong vòng (gắn nhãn, duyệt) có thể ăn **10–15% doanh thu**; với vài sản phẩm, **40–50% chức năng nằm ở ca lạ**; mỗi khách đòi chỉnh riêng làm chậm triển khai. Khuyên: thu hẹp bài toán, một mô hình dùng chung thay vì mỗi khách một mô hình, tính đủ chi phí biến đổi, chọn hẳn một chiến lược | a16z.com/the-new-business-of-ai-and-how-its-different-from-traditional-software (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN (bài cũ 2020, trước thời agent; số là nhận định của quỹ) |
| D14 | a16z, Joe Schmidt (04/06/2025): kỹ sư làm tại chỗ khách (FDE) nối sản phẩm AI vào dữ liệu, quy trình của khách, "dạy" agent như dạy nhân viên mới; chấp nhận biên thấp lúc đầu để có chỗ đứng; tự động hoá quy trình triển khai, ghi tài liệu mọi thứ, thư viện dùng chung; dịch vụ là **một giai đoạn**. ServiceNow biên gộp 63,2% lúc lên sàn → 79% năm 2024; Workday 54,1% → 75% | a16z.com/services-led-growth (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN (quỹ đầu tư viết) |
| D15 | Brian Casel: Audience Ops là "dịch vụ blog làm hộ", khoảng 25 người, **có lãi và chạy gần như không cần anh**; ProcessKit (phần mềm quản lý quy trình cho công ty dịch vụ, 49 USD/tháng trở lên) ra đời từ nỗi khổ "chắp vá nhiều công cụ" của chính dịch vụ đó; khách đầu tiên 06/2019, chủ yếu từ cộng đồng sẵn có; vốn từ lãi của dịch vụ. Không có số doanh thu | failory.com/interview/processkit (phỏng vấn 01/04/2020; tra 21/10/2026) | ĐÃ ĐỌC TOÀN VĂN (người sáng lập tự kể) |
| D16 | Audience Ops bán 09/2021 cho Graffam Cos., giá "high six-figure" theo bài của chính Casel; Restaurant Engine của anh **đi ngược**: định làm phần mềm, chuyển thành dịch vụ đóng gói | kết quả tìm (theygotacquired.com, nichepursuits.com, startupsfortherestofus.com), 21/10/2026 | NGUỒN-TRÍCH; ngày bán lệch giữa nguồn |
| D17 | Toolza, Dmytro Tymoshchuk (08/12/2025), 12 năm làm dịch vụ: khi chuyển sang sản phẩm thì **suýt kẹt làm riêng cho khách cũ**; vừa làm vừa phỏng vấn khách nên lộ trình đổi gần như hằng tuần; mất ~1,5 năm để thị trường thôi coi là công ty dịch vụ. Luật: coi cả ngành là khách; biến mỗi lần sửa cho khách thành mô-đun hoặc mẫu dùng chung; chỉ nhận yêu cầu nào nhân rộng được; chốt bản 1 rồi mới dựng | therecursive.com (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN (người sáng lập tự kể, không có số doanh thu) |
| D18 | Paul Graham (07/2013): với ít khách, **làm tay việc định tự động sau** (Stripe mở tài khoản thật bằng tay phía sau); làm tay dạy mình đúng việc cần tự động; làm như tư vấn cho một khách để tìm sản phẩm là an toàn **khi khách chưa trả tiền cho sự chăm chút** — trả rồi thì "họ đòi mình làm mọi thứ" | paulgraham.com/ds.html (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN |
| D19 | Tunguz (07/07/2026): các hãng AI cam kết **~9,75 tỷ USD trong 12 tháng** cho đội FDE (OpenAI 4, Microsoft 2,5, Anthropic 1,5, Amazon 1, Google Cloud 0,75); lập luận FDE là "hào" vì chi phí đổi nhà cung cấp nằm ở thói quen tổ chức | tomtunguz.com/the-10b-fde-boom (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN (nhà đầu tư viết; không có số biên lợi nhuận) |
| D20 | Dự án **không dựng trên bộ khung 0.2.4**: không có `.khung.json`; `tools/db.py` 386 dòng (khung 927), `evals.py` 40 (khung 67), `schema.sql` 157 (khung 124), không file nào giống. Khung 0.2.4 có mô-đun lịch chạy, trình duyệt, kế toán, thẩm định — **chưa có mô-đun marketing** | so file 21/10/2026 | [DỮ LIỆU] |
| D21 | Chữ riêng Yên Thế (Yên Thế, Đồng Lạc, Thắng Anh, 0965…) nằm trong **8 file `tools/*.py`** (ket_ban, lap_lich_bai, loc_nhom, nhan_tin, tim_nhom, vao_nhom, 2 file test); playbook 18 dòng, checklist 8 dòng, skill quang-cao-bds 5 dòng; 8 tác nhân và skill lead gần như sạch (copywriter 1 dòng) | grep 21/10/2026 | [DỮ LIỆU] |
| D22 | Plugin marketplace của Claude Code: thư mục có `.claude-plugin/marketplace.json`; đẩy lên git (kho **riêng tư được**); người khác `claude plugin marketplace add <kho>` rồi cài; quản trị viên có thể **bắt buộc cài trên mọi máy**; plugin gói skill, agent, hook, máy chủ MCP | code.claude.com/docs/en/plugin-marketplaces (21/10/2026) | ĐÃ ĐỌC TOÀN VĂN |
| D23 | Anthropic về evals: làm ca kiểm **giống việc thật, gồm ca lạ**; **tự động chấm khi có thể** (khớp chuỗi, mã kiểm, model chấm); **nhiều ca chấm tự động hơn ít ca chấm tay**; tiêu chí phải cụ thể, đo được; model chấm nên khác model làm | platform.claude.com/docs/en/test-and-evaluate/develop-tests (21/10/2026) | NGUỒN-TRÍCH (đọc 100k/153k ký tự) |
| D24 | Carta: khoảng **36%** startup lập năm 2025 trên Carta do **một người sáng lập** (2024: 31%; 2019: 23,7%); Carta cho là có phần do công cụ AI | carta.com/data/founder-ownership-2026-full-report (kết quả tìm, 21/10/2026) | NGUỒN-TRÍCH (chỉ startup trên nền Carta, chủ yếu Mỹ) |
| D25 | Designjoy (Brett Williams, một người, thiết kế thuê bao): giá khoảng 5.000 USD/tháng, khoảng 20 khách, doanh thu các nguồn ghi từ 1,3 đến 3 triệu USD/năm, tự kể có lúc kiệt sức | kết quả tìm (bài tổng hợp, podcast), 21/10/2026 | NGUỒN-TRÍCH, số lệch nhau [CẦN XÁC NHẬN] |
| D26 | YC: danh sách "xin startup" mùa Thu 2026 không có mục riêng "agency AI"; mục gần nhất là hệ điều hành cho ngành dịch vụ tốn nhiều công người. Các bài thứ cấp nói mùa Xuân 2026 có mục "AI-native agencies" (bán việc đã xong thay vì bán phần mềm) | ycombinator.com/rfs (ĐÃ ĐỌC TOÀN VĂN); bài thứ cấp (NGUỒN-TRÍCH) — 21/10/2026 | Mục Xuân 2026 [CẦN XÁC NHẬN] |
| D27 | Phí quản lý quảng cáo Facebook ở Mỹ cho doanh nghiệp địa phương: khoảng **1.500–5.000 USD/tháng**, hay gặp phí nền 1.500–2.500 USD + **5–10% (có nơi 15%) ngân sách QC**. Không tìm được bảng giá Việt Nam cho bất động sản | clicksgeek.com và bài tiếng Việt (Terus, 24hmoney), kết quả tìm 21/10/2026 | NGUỒN-TRÍCH, QUẢNG CÁO; giá Việt Nam [CẦN XÁC NHẬN, chuyển SP-1] |
| D28 | SP-2 (đang làm): app phục vụ người **không có vai trò trên app** (khách của mình) cần quyền Nâng cao, phải qua App Review từng quyền + xác minh doanh nghiệp; Marketing API bậc Full cần ≥ 500 lệnh gọi/15 ngày và lỗi < 15%; doanh nghiệp làm app cho doanh nghiệp khác là "Tech Provider" | `workspace/research/2026-10-21-sp-2-nen-tang-va-luat-choi.md` M1, M2, M4 | Dẫn lại từ SP-2 (bản nháp) |

---

## 3. Phân tích theo từng câu hỏi

### 3.1 Đường đi chuẩn có thật, nhưng không thẳng một chiều; mốc chuyển giai đoạn phải tự đặt vì không ai công bố số

**Ba bậc và bằng chứng** (trục chia: ai làm phần việc chính — người, người theo quy trình, máy):

| Bậc | Nghĩa ở dự án này | Bằng chứng | Bằng chứng bác / cảnh báo |
|---|---|---|---|
| **1. Làm tay đóng vai máy** | Yên Thế hiện nay: AI viết, kiểm, đăng, đọc số; người duyệt, đăng nhập, bấm tiền, sửa khi hỏng | PG: Stripe mở tài khoản bằng tay phía sau; làm tay dạy mình cái cần tự động (D18) | Khi khách đã trả tiền cho sự chăm chút thì "họ đòi mình làm mọi thứ" (D18) → bậc này chỉ nên kéo dài ở **1 khách** |
| **2. Dịch vụ đóng gói** | "Phòng marketing AI" giá cố định theo tháng, phạm vi cố định (4 khâu số), cùng quy trình cho mọi dự án | Audience Ops có lãi, ~25 người, chạy không cần chủ, bán được (D15, D16); Designjoy một người (D25, độ tin thấp); SU-3 mục 3.2: "dịch vụ có AI" hợp đội 3 người | a16z: công ty AI hay mắc kẹt ở biên kiểu dịch vụ (D13); Toolza: bẫy làm riêng (D17) |
| **3. Phần mềm thuê bao** | Khách tự dùng app, đội chỉ hỗ trợ | ServiceNow, Workday đi từ triển khai nặng lên biên 75–79% (D14) | ProcessKit là **sản phẩm khác** chứ không phải dịch vụ tự động hoá (D15); Restaurant Engine **đi ngược** từ phần mềm về dịch vụ (D16) |

**Kết luận** [NHẬN ĐỊNH]:
- Bậc 2 là **đích thực tế** cho 12–24 tháng của đội tự chi; bậc 3 là lựa chọn, không phải bắt buộc. Lộ trình bản 1 (`lo-trinh-san-pham-app.md` mục 3) đặt "app riêng nhiều người dùng" ở Chặng 4: đúng hướng, nên giữ là "quyết sau".
- Ở Việt Nam, bậc 2 còn hợp hơn ở Mỹ: chủ đầu tư ở tỉnh mua "kết quả và người chịu trách nhiệm", không mua phần mềm (SU-3 mục 4 ý 3; SP-1 sẽ kiểm).
- **Không tìm được nguồn nào công bố mốc số** (bao nhiêu khách, bao nhiêu % tự động thì chuyển bậc). Bài a16z 2025 và Tunguz chỉ nói hướng, không nói ngưỡng (D14, D19). Vì vậy đặt cổng tự đo, viết trước:

| Cổng | Đi tiếp khi (viết trước) [NHẬN ĐỊNH] | Dừng hoặc làm lại khi |
|---|---|---|
| Bậc 1 → 2 (Yên Thế → dự án 2), dự kiến 30/11 | (a) 2 tuần liền chỉ còn việc tay loại "người bắt buộc" (mục 3.2d); (b) cùng một quy trình chạy mỗi tuần không sửa lõi; (c) có số kết quả thật (lượt xem đất từ QC) để bán | Sau 30/11 vẫn còn > 10 bước tay "có thể tự động"/tuần → làm lại Chặng 1, chưa bán |
| Dự án 2 chạy | Cài ≤ 1 ngày; 2 tuần không sửa lõi; giờ người/dự án ≤ 20 giờ/tháng sau tháng đầu | Phải sửa lõi cho dự án 2 > 3 lần → lõi chưa tách xong |
| Bậc 2 ổn (bán cho khách thứ 3–5) | 3 dự án cùng gói; lãi đóng góp dương ở từng dự án (mục 3.4); ≥ 80% yêu cầu riêng của khách được trả lời bằng cấu hình, không bằng mã mới | > 1/3 thời gian đội là làm riêng theo yêu cầu (dấu hiệu bẫy D17) |
| Bậc 2 → 3 (app nhiều người dùng) | ≥ 5–10 dự án; đã qua App Review của Meta (D28); khách đòi tự dùng | Khách vẫn muốn "có người làm hộ" → ở lại bậc 2 |

### 3.2 Khung nhân bản đã có hình mẫu chuẩn: tách cấu hình, cài riêng từng khách, sổ tay cài, ca kiểm theo ngành, đo mức tự chạy

**(a) Lõi dùng chung và cấu hình riêng.** Chuẩn của SaaS là tự động hoá việc đón khách mới (D12); a16z: thư viện dùng chung, ghi tài liệu mọi thứ (D14); Toolza: biến mỗi lần sửa cho khách thành mô-đun (D17). Ở dự án này đã thấy rõ ranh giới [DỮ LIỆU D21]:
- **Gần như lõi rồi:** 8 tác nhân, skill lead, rubric 40 điểm, khuôn top-down, cổng lint + compliance + judge, lịch chạy, `doc_ads.py`.
- **Đang trộn:** playbook, compliance-checklist (§A–E chung, §F–§G riêng dự án — tách đôi được), skill quang-cao-bds (luật chung đất nền tỉnh + số riêng Yên Thế), 8 file `tools/*.py` có chữ Yên Thế.
- **Thuần cấu hình:** brief, ảnh `assets/dong-lac/`, danh sách nhóm, SĐT, tài khoản QC, `config/banned_terms.json` (từ cấm chung + con số giá riêng).

**(b) Cài riêng từng khách hay nhiều khách một hệ thống.** Khuyên **cài riêng** cho tới khoảng 10 dự án [NHẬN ĐỊNH], vì:
1. Mỗi chủ đầu tư có Trang, tài khoản QC, nick riêng; cài riêng thì sự cố hoặc khoá tài khoản của khách này không lan sang khách khác (cách ly mạnh nhất, D12).
2. Dễ tính chi phí AI từng khách (D12) — cần cho mục 3.4.
3. Nhiều khách một hệ thống đòi app Meta qua quyền Nâng cao, App Review, Tech Provider (D28) — chưa đội nào 1–3 người làm xong trong 3 tháng [NHẬN ĐỊNH].
4. Khớp SU-5 mục 3.4 (dữ liệu ở lại phía khách, đội không thành bên xử lý dữ liệu lớn).
Giá phải trả: cập nhật lõi cho N chỗ cài → dùng **plugin marketplace kho riêng** (D22) để đẩy bản mới; bộ khung đã có lệnh `nang-cap --thu` (README khung).

**(c) Đón khách mới trong 1 ngày.** Chuẩn: một danh sách bước cố định, phần lớn là điền cấu hình, có bước kiểm cuối. Khung 0.2.4 đã có mẫu: "cài 3 bước, dùng 3 bước, `/khung:kiem-tra` kết luận đủ điều kiện" (README khung). Việc tốn giờ nhất ở dự án này **không phải cài mã** mà là **thu tư liệu** (pháp lý, ảnh, bảng hàng, giá) và **đăng nhập Facebook** (phiên khoá theo máy, lộ trình bản 1 mục 5). → Phải có **phiếu thu tư liệu gửi trước 3–5 ngày**, ngày cài chỉ là ngày điền và chạy thử. Bước cụ thể ở mục 5c.

**(d) Đo "mức tự chạy".** Không có chuẩn công khai; đề xuất [NHẬN ĐỊNH]: mỗi tuần đếm **số lần người phải chạm tay**, chia 3 loại:
- **Người bắt buộc** (không bao giờ giao máy): "ok" tiêu tiền mới, đăng nhập/nhập PIN, duyệt thông điệp pháp lý mới, trả lời khách thật khi chưa bật trả lời tự động.
- **Có thể tự động nhưng chưa:** sửa lỗi đăng, chép số tay, sửa câu chữ sau compliance, chạy lại lịch.
- **Sự cố:** nick bị chặn, lịch không chạy, sai dữ liệu.
Chỉ số = số lần loại 2 + loại 3 mỗi tuần. Ghi bằng máy: mỗi lần can thiệp là một dòng trong DB (bảng `viec_tay`), báo cáo thứ Hai đếm. Cổng: loại 2 + 3 ≤ 3 lần/tuần trong 2 tuần liền (khớp cổng Chặng 1 của lộ trình bản 1).

**(e) Bộ ca kiểm theo ngành.** Anthropic: ca giống việc thật, có ca lạ, chấm tự động, nhiều ca (D23). Dự án đã có 20 ca compliance + lint giá 31 ca + test đọc số 43 ca [DỮ LIỆU STATE, log]. Thiếu: tách thành **bộ chung "đất nền tỉnh"** (giá, cam kết lợi nhuận, quy hoạch chưa duyệt, so sánh đối thủ, khuyến mãi chưa có văn bản…) và **bộ riêng từng dự án** (mã lô, tên cũ, địa danh). Khi đổi model (mục 3.3d) chạy lại cả hai bộ trong 1 ngày (SU-5 mục 3.6 ý 3). Đây là **lợi thế bền** đúng nghĩa SU-3 mục 3.3: bộ quy tắc kiểm lỗi tích luỹ theo ngành.

**(f) Kỹ sư làm tại chỗ khách.** Các hãng AI lớn đổ ~9,75 tỷ USD vào vai này (D19); a16z coi là giai đoạn để học và giữ khách (D14). Với đội tự chi, đây chính là chủ sở hữu ở 3 dự án đầu: đến tận nơi, ngồi với TPKD, chỉnh luật, rồi **mang mỗi lần chỉnh về lõi hoặc về cấu hình mẫu** (luật D17). Rủi ro: làm FDE mãi thì thành công ty làm thuê (D13, D17).

### 3.3 Đóng gói kỹ thuật làm được, nhưng "Claude Desktop làm động cơ" chỉ hợp khi khách tự đứng tên; 24/7 cần máy bật cho phần trình duyệt; không khoá AI chỉ làm được ở lõi

**(a) Bốn cách chạy "bộ não" và mức hợp lệ** (trục chia: ai giữ tài khoản AI × chạy ở đâu):

| Cách | Chạy ở đâu | Hợp điều khoản? | Hợp đội 1–3 người? [NHẬN ĐỊNH] |
|---|---|---|---|
| A. Claude Desktop/Claude Code, **gói của khách**, khách tự dùng | Máy của khách | Gói cá nhân cấm script, bot trừ khi Anthropic cho phép rõ (D1); lịch Desktop và lịch đám mây là tính năng của chính Anthropic, có ở Pro/Max/Team (D3, D4) → có vẻ được phép **cho chính người đứng tên** [CẦN XÁC NHẬN] | Hợp lúc đầu (rẻ, dùng lại nguyên hệ thống); nhưng mỗi khách cần người biết dùng Claude Code |
| B. Như A nhưng **gói của đội** chạy hộ nhiều khách | Máy của đội | Rủi ro cao: gói cá nhân "cho cá nhân" và cấm bán lại (D1); Agent SDK cấm bên thứ ba cung cấp hạn mức gói cho sản phẩm (D2) | **Không nên** khi đã thu tiền nhiều khách |
| C. **Agent SDK + API key** của đội, cài riêng từng khách | Máy khách hoặc máy chủ ảo (VPS) | Hợp: Điều khoản thương mại cho phép dùng để phục vụ khách của mình (D2) | **Đích của Chặng 3**; trả tiền theo token (mục e) |
| D. **Managed Agents** (agent chạy trên máy chủ Anthropic) | Đám mây Anthropic, hoặc hộp cát tự host | Hợp (Điều khoản thương mại) | Hợp cho phần đi API chính thức (viết bài, chấm, báo cáo); **không** hợp phần trình duyệt Facebook trong máy |

→ Lộ trình bản 1 mục 4 "Cách 1" nên ghi lại: **cách 1 = A** (khách tự đứng tên, giai đoạn thử); **cách 2 = C/D** (bán thật). Không đi B. Cần luật sư và câu hỏi gửi Anthropic (mục 6).

**(b) Lịch chạy 24/7.**
- Phần đi **API chính thức** (đọc số QC, viết bài, kiểm bài, báo cáo 17:30): chạy được trên lịch đám mây của Claude Code (cần kho GitHub, không file trong máy, D3) hoặc Managed Agents (D6), hoặc VPS chạy Agent SDK theo lịch hệ điều hành.
- Phần **trình duyệt** (đăng nhóm bằng nick, Playwright, phiên Facebook lưu trong máy): **cần một máy bật** — máy của khách, máy của đội, hoặc VPS Windows. Chuyển sang VPS ở trung tâm dữ liệu thì Facebook thấy đăng nhập từ chỗ lạ [GIẢ THUYẾT: tăng nguy cơ checkpoint, đã gặp khoá theo máy ngày 25/09 — lộ trình bản 1 mục 5]. → Thêm lý do để **dời trọng tâm sang Fanpage + QC qua API**, đúng H0 và lộ trình bản 1.
- Hiện nay Yên Thế dùng Windows Task Scheduler + lịch Claude Desktop trên máy người dùng [DỮ LIỆU STATE] = cách A, cần máy bật.

**(c) Phân phối bản cài.** Plugin marketplace kho git riêng (D22) là đường chính thức để: đẩy bản lõi mới cho mọi chỗ cài, bắt buộc cài trên máy của đội. Khung 0.2.4 đã đi đúng đường này. Khi chuyển sang cách C, Agent SDK nạp được plugin và skill từ `.claude/` (D2) → **dùng lại nguyên skill và tác nhân hiện có**, không viết lại.

**(d) Không khoá vào một nhà AI — làm được ở đâu.**

| Lớp | Đổi model được? | Bằng chứng |
|---|---|---|
| Lõi Python: lint giá, từ cấm, lịch đăng, đọc số QC, DB | **Có, vì không dùng AI** | SU-5 mục 3.6 ý 1; `tools/` hiện nay [DỮ LIỆU] |
| Bước gọi model đơn lẻ: viết bài, chấm rubric, tóm tắt số | **Có**, nếu qua 1 lớp gọi model (nhận "việc + dữ liệu", nhà cung cấp trong cấu hình). Grok qua API kiểu OpenAI (D10); Muse chưa mở cho Việt Nam (D11) | SU-5 mục 3.6 ý 2 |
| Lớp agent tự điều phối (Lead, tác nhân con, hook, skill) | **Không** — Claude Code và Agent SDK chạy model Claude (D9); xAI bỏ đường tương thích Anthropic (D10) | D9, D10 |

→ Cách giữ đường lui [NHẬN ĐỊNH]: (1) luật, mẫu, ca kiểm, rubric để dạng file trong git, không nằm trong nền tảng của hãng; (2) viết lớp gọi model cho 2 bước "viết bài" và "chấm bài" trước, vì đó là chỗ tốn token nhất; (3) đo Grok 4.3 và Haiku 5.5 trên bộ ca kiểm (mục 3.2e) trước khi chuyển; (4) chấp nhận lớp điều phối khoá vào Claude — đổi lớp này là viết lại, nhưng lớp này nhỏ.

**(e) Chi phí AI mỗi khách mỗi tháng cho khối lượng như Yên Thế** [ƯỚC TÍNH; giá D5, D6 đã đọc toàn văn; lượng token là giả định].

Khối lượng: 84 bài nhóm/tuần (viết + compliance + judge + sửa), báo cáo QC 17:30 mỗi ngày, báo cáo thứ Hai, việc lặt vặt (sửa mẫu QC, phân tích, soạn trả lời tin nhắn).

Giả định lượng token (neo vào D7, D8): bộ ngữ cảnh ~163 KB ≈ 55 nghìn token [GIẢ ĐỊNH 1 token ≈ 3 byte chữ Việt, CẦN XÁC NHẬN bằng đếm token thật]; 4 tác nhân soạn 1 ngày ≈ 1,02 triệu token (D7).

| Việc | Token mỗi lần (giả định) | Sonnet 5.5, có bộ nhớ đệm 80% | Toàn Opus 5.5, đệm ít, token gấp đôi |
|---|---|---|---|
| Lô bài tuần (84 bài) | 4 triệu vào (0,8 triệu mới + 3,2 triệu đọc đệm), 0,2 triệu ra | 0,8 × 2,5 + 3,2 × 0,10 + 0,2 × 10 ≈ **4,3 USD/tuần** → 18,7 USD/tháng (× 4,33) | 8 triệu vào × 4 + 0,4 triệu ra × 20 = 40 USD/tuần → 173 USD/tháng |
| Báo cáo 17:30 | 0,3 triệu vào (70% đệm), 15 nghìn ra | 0,09 × 2,5 + 0,21 × 0,10 + 0,015 × 10 ≈ **0,40 USD/ngày** → 12 USD/tháng | 0,6 × 4 + 0,03 × 20 = 3 USD/ngày → 90 USD/tháng |
| Báo cáo thứ Hai | 0,6 triệu vào, 30 nghìn ra | ≈ 0,8 USD × 4,33 ≈ 3,5 USD/tháng | ≈ 6 USD × 4,33 ≈ 26 USD/tháng |
| Việc lặt vặt + tìm web (~200 lượt) | — | ~10 USD + 2 USD tìm web | ~40 USD + 2 USD |
| **Cộng** | | **≈ 46 USD ≈ 1,2 triệu đ/tháng** | **≈ 330 USD ≈ 8,6 triệu đ/tháng** (trần xấu nhất) |

Đọc bảng:
- Kịch bản giữa (Sonnet làm việc theo hợp đồng rõ, Opus chỉ ở compliance và giám khảo — đúng bảng model của khung 0.2.4): **~1,5–2,5 triệu đ/khách/tháng**. Tốt: dùng Haiku 5.5 cho bước lint-chữ, Batch −50% cho lô bài (không cần gấp) → **< 1 triệu**.
- Nếu chạy trên Managed Agents thêm 0,08 USD/giờ phiên (D6): 40 giờ/tháng ≈ 3,2 USD, không đáng kể.
- **Chưa gồm:** tạo ảnh/video bằng AI, ngân sách QC Meta, VAT, máy chủ ảo.
- Kịch bản xấu nhất 8,6 triệu xảy ra khi để phiên dài, không đệm, toàn Opus — đúng thứ khung đã cảnh báo ("phiên chat dài tốn nhất", README khung). → Luật cho sản phẩm: **đo token thật một tuần ở Yên Thế** (khung có `/khung:kiem-tra token`) trước khi báo giá dự án 2.
- So với số người: hỗ trợ 8–10 giờ/tháng × 250.000 đ = 2–2,5 triệu (SU-8 mục 13.1) → **giờ người ≥ tiền AI**. Khớp SU-3 mục 3.4 ý 4: "giờ hỗ trợ là khoản quyết định, không phải tiền AI".

### 3.4 Giá và lãi: dùng lại SU-3 mục 3.5; ngành marketing có sẵn thói quen "phí nền + % ngân sách QC", nhưng thu theo lead dễ cãi nhau

Dùng lại nguyên tắc SU-3 mục 3.5.4: **có phí nền cố định**, phần theo kết quả là thưởng có trần; không tính theo token, không theo số agent. Phần riêng ngành marketing:
- Ở Mỹ agency quảng cáo Facebook cho doanh nghiệp địa phương thu **1.500–5.000 USD/tháng**, hay gặp **phí nền + 5–15% ngân sách QC** (D27, QUẢNG CÁO). Mô hình "phí nền + % ngân sách" là thói quen sẵn của ngành, khách dễ hiểu [NHẬN ĐỊNH]. Giá Việt Nam: [CẦN XÁC NHẬN, SP-1].
- **Ba cách thu cho "phòng marketing AI"** [NHẬN ĐỊNH]:

| Cách | Hợp khi | Rủi ro cho đội tự chi |
|---|---|---|
| Theo tháng, phạm vi cố định (vd 84 bài/tuần + quản lý QC + báo cáo ngày) | Mặc định cho dự án 2–5 | Khách đòi thêm việc ngoài phạm vi (bẫy D17, D18) → ghi phạm vi trong hợp đồng |
| Theo dự án (đợt mở bán 3 tháng) | Chủ đầu tư bán theo đợt | Doanh thu đứt quãng; cần tính cả công thu tư liệu |
| Theo lead/lượt xem đất | Chỉ làm **thưởng**, có trần | Cãi "lead này nhờ ai" (SU-3 mục 3.5.2); lead do đội bán ghi, đội mình không kiểm được (sổ nguồn khách Yên Thế chưa có dòng thật [DỮ LIỆU STATE]) |

- Phép tính lãi đóng góp [ƯỚC TÍNH, giả định để tập tính]: phí X − AI 1,5–2,5 triệu − giờ người (20 giờ tháng đầu, 10 giờ sau × 250.000 đ = 5 / 2,5 triệu) − máy, phần mềm ~0,5 triệu. Nếu X = 10 triệu: lãi đóng góp ≈ 2–3 triệu tháng đầu, **4,5–5,5 triệu từ tháng 2**. Với quỹ chi 40 triệu/tháng (SU-8 mục 13.2) cần khoảng **8 dự án**; X = 20 triệu thì khoảng **3–4 dự án**. Ngưỡng giá thật do SP-1 quyết.

### 3.5 Đội 1–3 người cộng agent làm được phần sản xuất; vai bán hàng, giữ quan hệ, bấm tiền và chịu trách nhiệm vẫn là người

- **Bằng chứng xu hướng:** 36% startup mới năm 2025 trên Carta có một người sáng lập (D24); Audience Ops chạy không cần chủ (D15). Nhưng Designjoy một người có lúc kiệt sức (D25), Cydoc một người thất bại vì không bán được (SU-3 D22).
- **Ở Yên Thế hiện nay** [DỮ LIỆU]: 1 người (chủ sở hữu) + 8 tác nhân đã viết, kiểm, đăng 12 bài/ngày, đọc số QC mỗi ngày. Việc tay còn lại đúng loại "người bắt buộc": ok tiền, đăng nhập, hỏi Phòng KD, dán tin cho người chạy QC.
- **Vai và người** [NHẬN ĐỊNH]:

| Vai | Agent làm được | Phải là người |
|---|---|---|
| Bán và giữ khách (chủ đầu tư, sàn) | Soạn chào giá, tài liệu, tóm tắt buổi gặp | Đi gặp, đàm phán, ký; nhận điện khi khách phàn nàn (B3.8 luật tư duy) |
| Vận hành 4 khâu | Viết, kiểm, đăng, đọc số, báo cáo | "Ok" tiền QC, đăng nhập, duyệt thông điệp pháp lý mới, xử lý khi nick bị khoá |
| Kỹ thuật lõi | Viết mã, ca kiểm, sửa lỗi | Quyết kiến trúc, chịu trách nhiệm khi hỏng |
| Pháp lý | Rà chữ theo checklist | Chịu trách nhiệm trước luật; hỏi luật sư |

- **Khi nào thuê** [ƯỚC TÍNH, theo SU-8 mục 12]: người thứ 2 (vận hành và hỗ trợ tại tỉnh, có thể là người cũ của Phòng KD) khi tổng giờ hỗ trợ vượt ~60 giờ/tháng, khoảng **4–6 dự án**; người thứ 3 (bán hàng) khi chủ sở hữu không còn ≥ 2 buổi gặp khách mới/tuần. Không thuê trước khi lãi đóng góp của các dự án đang chạy trả được lương người đó (B4.6).

---

## 4. Góc nhìn thời AI [NHẬN ĐỊNH]

1. **Thời AI làm bậc 1 (làm tay đóng vai máy) rẻ hơn hẳn:** trước kia "làm tay phía sau" tốn người; nay agent làm phần lớn, người chỉ chạm 5–10 lần/tuần. Vì vậy chặng thử ở Yên Thế ngắn được (6 tuần) — điều startup kiểu cũ cần 6–12 tháng.
2. **Nhưng AI làm "bẫy làm riêng" nguy hiểm hơn:** sửa riêng cho một khách giờ chỉ mất vài phút, nên rất dễ nói "có" với mọi yêu cầu (D17). Luật: mỗi yêu cầu riêng phải đổi được thành dòng cấu hình hoặc ca kiểm chung; không thì từ chối hoặc tính tiền riêng.
3. **Giá model giảm là lợi cho bán theo tháng** (SU-3 mục 4 ý 1): tiền AI 1–2 triệu hôm nay có thể còn một nửa sau 12 tháng, phí tháng giữ nguyên → lãi tăng. Bán theo token thì mất lợi này.
4. **Lớp điều phối khoá vào hãng là cái giá thật của tốc độ:** dùng Claude Code và Agent SDK thì dựng nhanh gấp nhiều lần, đổi lại không đổi hãng ở lớp đó được. Chỗ tự giữ được là luật, ca kiểm, dữ liệu kết quả theo ngành.
5. **Kỹ sư tại chỗ khách là việc AI không làm thay được** (D19): hiểu Phòng KD nói gì, lấy được bảng hàng, đứng ra chịu trách nhiệm. Đây là lợi thế của đội ở tỉnh so với phần mềm nước ngoài.

---

## 5. Hệ quả

### (a) Cho startup tự chi — nên làm, không nên làm

**Nên làm**
- Coi **dịch vụ đóng gói "phòng marketing AI"** là sản phẩm của 12–24 tháng; app nhiều người dùng chỉ quyết khi ≥ 5–10 dự án.
- **Đổi lộ trình bản 1 mục 4:** cách 1 = khách tự đứng tên gói Claude (thử); cách 2 = Agent SDK + API key của đội (bán thật). Bỏ phương án đội dùng gói của mình chạy hộ nhiều khách.
- **Tách lõi trước khi bán dự án 2** (Chặng 2 tháng 12); dựng lại trên bộ khung (mô-đun mới `mo-dun/marketing-bds`) để một lõi, một cách nâng cấp.
- Đo **token thật 1 tuần** và **mức tự chạy** bằng máy trước khi báo giá.
- Ưu tiên đường **API chính thức** (Fanpage, QC) vì chạy được trên đám mây và không chết theo nick.

**Không nên làm**
- Không bán cho dự án 2 khi "mức tự chạy" chưa qua cổng.
- Không nhận làm riêng mà không đổi được thành cấu hình.
- Không dựng nhiều khách một hệ thống trước khi qua App Review của Meta (SP-2).
- Không hứa "không phụ thuộc AI nào" với khách: chỉ hứa "dữ liệu và luật của anh chị nằm ở máy anh chị, đổi được nhà cung cấp ở bước viết bài".

### (b) Áp vào dự án Yên Thế (Chặng 1, tới 30/11)

| Việc | Vì sao | Khi nào |
|---|---|---|
| 1. Thêm sổ "việc tay" (mỗi lần người chạm tay = 1 dòng, 3 loại mục 3.2d); báo cáo thứ Hai đếm | Không có số này thì không biết lúc nào sẵn sàng đóng gói | Tuần 43–44 |
| 2. Đo token thật của lô bài tuần 28/10 và báo cáo 17:30 (`/khung:kiem-tra token` hoặc thẻ Usage) | Thay ước tính mục 3.3e bằng số thật trước khi báo giá | 28/10–03/11 |
| 3. Đánh dấu chỗ trộn lõi/cấu hình: checklist §A–E (chung) vs §F–§G (riêng); playbook; skill quang-cao-bds; 8 file `tools/` | Chuẩn bị Chặng 2, không sửa gì ở Chặng 1 | Tới 30/11 (chỉ ghi danh sách) |
| 4. Nối Fanpage chủ đầu tư (đường API chính thức) | Phần chạy 24/7 được, không phụ thuộc nick | Theo cap-3 luồng C2 |
| 5. Gửi 2 câu hỏi điều khoản (mục 6) cho Anthropic và luật sư | Quyết cách đóng gói trước 30/11 | Trước 15/11 |

Không đổi gì đang chạy (lịch đăng, QC, `tools/`) — các việc trên chỉ là đo và ghi.

### (c) Đưa gì vào khung chuẩn nhân rộng

**c1. Thư mục cấu hình một dự án** — `du-an/<ma-du-an>/` (9 nhóm; trục chia: thông tin gì của khách mà lõi cần đọc)

| # | File | Nội dung | Đã có ở Yên Thế? |
|---|---|---|---|
| 1 | `du-an.json` | Tên thương mại, tên pháp lý, vai (CĐT/sàn), chủ đầu tư, vùng, SĐT/Zalo CTA, múi giờ, người giữ D | Có nhưng rải: `brief.md`, `CLAUDE.md`, chữ trong `tools/` → **phải gom** |
| 2 | `brief.md` | Nguồn sự thật kinh doanh: sản phẩm, pháp lý, tiện ích, khách mục tiêu | **Có** (`workspace/brief.md`) |
| 3 | `luat-rieng.md` + `thong-diep.md` | Quy tắc riêng dự án (§F) và sổ thông điệp KHOÁ/MỞ (§G) | **Có** nhưng nằm chung checklist → **tách** |
| 4 | `gia-va-tu-cam.json` | Mốc giá được nói, con số cấm, từ cấm riêng | **Có** trong `config/banned_terms.json` (trộn chung) → **tách** |
| 5 | `kho-anh/` + `kho-anh.json` | Ảnh/video đã duyệt, nhãn góc (sổ đỏ, đêm, flycam), ngày chụp | **Có** (`assets/dong-lac/`, `tools/kho_anh.py`) |
| 6 | `nhom.csv` | Danh sách nhóm FB, vùng, luật nhóm, giãn cách | **Có** trong DB và `data/` → **xuất ra file** |
| 7 | `tai-khoan.json` | Mã Trang, tài khoản QC, nick (chỉ mã, **không mật khẩu, không cookie**), ai có quyền | Rải trong STATE, settings → **gom**; bí mật ở kho bí mật của máy |
| 8 | `qc.json` | Ngân sách, trần, ngưỡng TẮT/GIỮ/TĂNG, vùng, lịch giờ trực | **Có** trong skill quang-cao-bds và `doc_ads.py` (trộn) → **tách số ra** |
| 9 | `lich.json` + `ca-kiem-rieng/` | Số bài/ngày, giờ đăng, giờ báo cáo; ca kiểm riêng dự án | `config/settings.json`, `evals/compliance/` (trộn chung + riêng) → **tách** |

Lõi (không đổi giữa dự án): 8 tác nhân, skill lead, rubric, khuôn top-down, `tools/` đã sạch chữ riêng, **bộ ca kiểm chung "đất nền tỉnh"**, checklist §A–E, mẫu báo cáo 17:30 và thứ Hai.

**c2. Các bước cài cho khách mới (7 bước, mục tiêu ≤ 1 ngày làm việc tại chỗ)**
0. *(Trước 3–5 ngày)* Gửi **phiếu thu tư liệu** 1 trang: pháp lý, bảng hàng, mốc giá được nói, ảnh, SĐT nhận khách, ai giữ D. Chưa đủ thì không hẹn ngày cài.
1. Kiểm máy: Windows, Python, Claude (tài khoản đứng tên khách) hoặc API key của đội; chạy lệnh chẩn đoán → "đủ điều kiện chạy".
2. Cài lõi từ marketplace kho riêng (1 lệnh), tạo thư mục `du-an/<mã>/` từ mẫu.
3. Điền 9 nhóm file cấu hình từ phiếu thu tư liệu (agent điền nháp, người soát).
4. **Khách tự đăng nhập** Facebook, Trang, tài khoản QC trên máy (đội không giữ mật khẩu); nối kết nối QC chỉ đọc.
5. Chạy **bộ kiểm bắt buộc** (c3); trượt ca nào sửa cấu hình, không sửa lõi.
6. Chạy thử: viết 6 bài + 1 mẫu QC, khách duyệt; đăng 1 bài lên Trang; chạy báo cáo 17:30 một lần.
7. Bật lịch (đăng, báo cáo), ghi STATE, giao 1 tờ A4 "ai làm gì, gọi ai khi hỏng".

**c3. Bộ kiểm bắt buộc (4 lớp; trượt một lớp là chưa bàn giao)**
1. **Máy kiểm cấu hình:** đủ 9 nhóm file, không ô trống, không còn chữ của dự án mẫu (vd "Yên Thế" xuất hiện ở dự án khác = trượt).
2. **Ca kiểm chung ngành** (đất nền tỉnh: giá, cam kết lời, quy hoạch, so sánh đối thủ, khuyến mãi chưa văn bản, vay vốn…) — 100% đúng.
3. **Ca kiểm riêng dự án** (mã lô, tên cũ, địa danh, thông điệp KHOÁ) — 100% đúng; mỗi dự án ≥ 10 ca.
4. **Chạy khô 7 ngày lịch đăng** + đọc lại 1 lần số QC: 0 lỗi chặn.

**c4. Số đo mỗi tuần (6 số, báo cáo thứ Hai)**
1. Mức tự chạy: số lần chạm tay loại "có thể tự động" + "sự cố" (mục 3.2d).
2. Giờ người cho dự án (đội ghi).
3. Tiền AI thật (token × giá D5).
4. Tỉ lệ bài qua cổng lần đầu (lint + compliance + judge).
5. Kết quả QC: cuộc nói chuyện, người cho SĐT/Zalo, lượt xem đất (đội bán ghi sổ nguồn khách).
6. Số yêu cầu riêng của khách: trả bằng cấu hình / bằng mã mới / từ chối.

**c5. Cổng đi tiếp / dừng** — như bảng mục 3.1 (4 cổng, tiêu chí viết trước, 4 kết cục đi tiếp · dừng · tạm dừng · làm lại theo luật tư duy A7).

**c6. Đối chiếu với cấu trúc hiện tại**

| Thành phần khung chuẩn | Hiện trạng | Thiếu gì |
|---|---|---|
| Tác nhân, skill, rubric, khuôn trình bày | Có (8 tác nhân, lead, quang-cao-bds, rubric 40 điểm, luật top-down) | Gỡ chữ riêng ở copywriter (1 dòng), quang-cao-bds (5 dòng) |
| Máy kiểm + ca kiểm | Có: 20 ca compliance, lint giá 31, test đọc số 43 | Tách bộ chung ngành / bộ riêng; máy kiểm cấu hình (lớp 1) |
| Lịch chạy | Có (Task Scheduler, lịch Claude) | Phần API chưa đưa lên đám mây; lịch gắn máy người dùng |
| Đọc số QC, báo cáo | Có (`doc_ads.py`, mẫu 17:30, thứ Hai) | Ngưỡng số trộn trong mã/skill → `qc.json` |
| Thư mục cấu hình 1 dự án | **Chưa** (rải ở brief, CLAUDE.md, config, DB, 8 file tools) | Toàn bộ c1 |
| Bộ khung chung, nâng cấp | Khung 0.2.4 có, nhưng **dự án không dựng trên khung** (D20) | Mô-đun `marketing-bds` trong khung; chuyển dự án sang lõi khung |
| Sổ tay cài, phiếu thu tư liệu | **Chưa** | c2 |
| Đo mức tự chạy, giờ người, tiền AI | **Chưa** bằng máy | c4 số 1–3, 6 |
| Đường Fanpage chính thức | Mã có, **chưa nối** [DỮ LIỆU lộ trình bản 1] | Nối + App Review nếu đi nhiều khách (SP-2) |

Ước tỉ lệ đã có: khoảng **60%** thành phần (5/9 dòng có ít nhất một phần) [NHẬN ĐỊNH, đếm thô theo bảng c6].

---

## 6. Điều chưa biết; câu cần hỏi

**Hỏi Anthropic (qua kênh bán hàng/hỗ trợ chính thức) và luật sư — cần luật sư xác nhận:**
1. Khách là doanh nghiệp tự mua gói Claude (Team/Max) đứng tên mình, đội cài hệ thống agent và lịch tự chạy trên máy khách: có phạm điều khoản "không truy cập bằng script" (D1) không, hay thuộc phần "Anthropic cho phép rõ" vì dùng tính năng lịch của chính Claude?
2. Đội dùng **một** gói Claude của mình để chạy việc cho nhiều chủ đầu tư có thu tiền: chắc chắn phải chuyển sang API key (D1, D2)?
3. Hợp đồng "phòng marketing AI": ai chịu trách nhiệm khi bài vi phạm luật quảng cáo bất động sản — mẫu hợp đồng nên có trần trách nhiệm (SU-4).

**Chưa đo, tự đo được:**
4. Token thật một tuần ở Yên Thế (thay mục 3.3e). [CẦN XÁC NHẬN]
5. Tỉ lệ byte/token với chữ Việt của model Claude (giả định 3 byte/token). [CẦN XÁC NHẬN]
6. Mức tự chạy hiện nay (chưa có sổ việc tay). [CẦN XÁC NHẬN]
7. Grok 4.3, Haiku 5.5 đạt bao nhiêu % trên bộ ca kiểm compliance so với Opus. [CẦN XÁC NHẬN]

**Hỏi Meta (để SP-2):**
8. Mỗi chủ đầu tư tự tạo app Meta đứng tên mình (người dùng đều có vai trò trên app) thì có tránh được App Review/Tech Provider không? [CẦN XÁC NHẬN, SP-2]
9. Đăng nhập Facebook từ máy chủ ảo ở trung tâm dữ liệu có làm tăng checkpoint không. [GIẢ THUYẾT]

**Hỏi khách (để SP-1):**
10. Chủ đầu tư ở tỉnh chọn trả theo tháng cố định, theo đợt mở bán, hay phí nền + thưởng lượt xem đất? Agency bất động sản Việt Nam đang thu bao nhiêu? [CẦN XÁC NHẬN]
11. Khách có chấp nhận tự mua và đứng tên gói Claude không (cách A)?

**Chưa có nguồn:**
12. Ngưỡng số chuyển bậc (số khách, % tự động, biên) từ startup thật — không tìm được trong ngân sách; mốc mục 3.1 là [NHẬN ĐỊNH].
13. Claude Code có chạy được model không phải Claude qua cổng trung gian không (D9). [CẦN XÁC NHẬN]

---

## 7. Danh sách nguồn

Đọc trọn (ĐÃ ĐỌC TOÀN VĂN), tra 21/10/2026:
1. Anthropic, Consumer Terms of Service (hiệu lực 08/10/2025) — https://www.anthropic.com/legal/consumer-terms
2. Claude Code Docs, Agent SDK overview — https://code.claude.com/docs/en/agent-sdk/overview
3. Claude Code Docs, Automate work with scheduled tasks (routines) — https://code.claude.com/docs/en/routines
4. Claude Code Docs, Run prompts on a schedule (bảng so 3 cách lịch) — https://code.claude.com/docs/en/scheduled-tasks
5. Claude Code Docs, Create a marketplace — https://code.claude.com/docs/en/plugin-marketplaces
6. Claude Platform Docs, Pricing — https://platform.claude.com/docs/en/about-claude/pricing
7. xAI Docs, Models and pricing — https://docs.x.ai/docs/models
8. AWS Whitepaper, SaaS Architecture Fundamentals: Tenant isolation — https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/tenant-isolation.html
9. a16z, Casado & Bornstein, The New Business of AI (16/02/2020) — https://a16z.com/the-new-business-of-ai-and-how-its-different-from-traditional-software/
10. a16z, Joe Schmidt, Trading Margin for Moat (04/06/2025) — https://a16z.com/services-led-growth/
11. Tomasz Tunguz, The $10B FDE Boom (07/07/2026) — https://tomtunguz.com/the-10b-fde-boom
12. Paul Graham, Do Things that Don't Scale (07/2013) — https://paulgraham.com/ds.html
13. Failory, phỏng vấn Brian Casel về ProcessKit (01/04/2020) — https://failory.com/interview/processkit
14. The Recursive, Dmytro Tymoshchuk về Toolza (08/12/2025) — https://www.therecursive.com/agency-product-pivot-customization-trap-saas-strategy-toolza-first-hand/
15. Y Combinator, Requests for Startups (Thu 2026) — https://www.ycombinator.com/rfs

Đọc một phần / trích (NGUỒN-TRÍCH):
16. Claude Platform Docs, Develop tests (đọc 100k/153k ký tự) — https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
17. Claude Code Docs, LLM gateway, gateway protocol (kết quả tìm) — https://code.claude.com/docs/en/llm-gateway ; https://code.claude.com/docs/en/llm-gateway-protocol
18. xAI Docs, Legacy & Deprecated (kết quả tìm) — https://docs.x.ai/developers/rest-api-reference/inference/legacy
19. AWS SaaS Lens, Pool isolation; SaaS Storage Strategies (kết quả tìm) — https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/pool-isolation.html
20. Carta, 2026 Founder Ownership Report; Solo founders 2016–2025 (kết quả tìm) — https://carta.com/data/founder-ownership-2026-full-report/
21. Audience Ops bán 2021 (kết quả tìm) — https://theygotacquired.com/services/audience-ops-sold-to-jd-graffam/ ; https://www.startupsfortherestofus.com/tag/audienceops
22. Designjoy (bài tổng hợp, độ tin thấp) — https://sujalkumar.beehiiv.com/p/18-million-solopreneur
23. Phí agency quảng cáo Facebook (QUẢNG CÁO) — https://clicksgeek.com/facebook-advertising-agency-pricing/
24. Mailchimp khởi đầu từ agency thiết kế (kết quả tìm, không dùng làm dữ kiện) — https://www.inc.com/jon-fine/mailchimp-ben-chestnut-founders-house-founders-project.html (mở lỗi 403)

Mở nhưng không dùng được: Wikipedia "Ben Chestnut" (không có thông tin cần); vivekhaldar.com (lỗi kết nối).

Tài liệu trong máy (dẫn lại, không nghiên cứu lại):
- `D:\0. AI\goi-phong-kham\nghien-cuu\startup\su-3-thoi-ai-mo-hinh-kinh-doanh.md` mục 1, 3.2, 3.4, 3.5, 4, 5
- `...\su-5-cong-nghe-va-ai-stack.md` mục 3.4, 3.6
- `...\su-8-tong-hop-startup-a-z.md` mục 0, 8.3, 9, 12, 13, 14
- `D:\0. AI\nghien-cuu\2026-10-14-cach-mo-muse-ai.md` dòng 70, 74
- `D:\0. AI\(NỘI BỘ) Bộ cài AI agent Xanh BG\_he-thong\khung-agent-marketplace\README.md`, `CHANGELOG.md` (0.1.0–0.2.4)
- `workspace/ke-hoach/lo-trinh-san-pham-app.md`; `workspace/STATE.md`; `workspace/reports/log.md` dòng 272, 274, 298, 317; `workspace/research/2026-10-21-sp-2-nen-tang-va-luat-choi.md` (bản nháp, M1–M5)
- Cấu trúc dự án: `CLAUDE.md`, `.claude/agents/` (8), `.claude/skills/` (2), `tools/` (25 file .py), `config/`, `evals/compliance/` (20 ca) — chỉ đọc tên, mô tả, cỡ file, đếm chữ
