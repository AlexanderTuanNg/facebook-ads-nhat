# CHECKLIST COMPLIANCE (bản nháp: cần pháp chế/luật sư xác nhận)

Căn cứ tham khảo: Luật Kinh doanh BĐS 2023 (29/2023/QH15), Luật Quảng cáo và văn bản sửa đổi, Nghị định 339/2026/NĐ-CP (xử phạt lĩnh vực xây dựng, nhà ở, KDBĐS; ban hành 26/08/2026: cần đọc toàn văn để bổ sung điều khoản cụ thể), Tiêu chuẩn cộng đồng Meta.

## 0. MỨC XỬ LÝ: CHẶN hay GÓP Ý (bản chuẩn, đổi 25/09/2026)
Người dùng yêu cầu (25/09): "giảm ngưỡng của agent compliance xuống" và "giảm thêm phần compliance xuống, mục tiêu để kéo được nhiều khách nhất có thể". Vì vậy compliance **chỉ chặn khi bài dính "sàn cứng"**; mọi thứ khác duyệt kèm góp ý ngắn. Mỗi mục A–F bên dưới có nhãn **[CHẶN]**, **[GÓP Ý]**, **[CHẶN khi …]** hoặc **[chỉ strict]**. Prompt `.claude/agents/compliance.md` tóm tắt lại mục này; sửa mức thì sửa cả hai file. Spec: `workspace/plans/2026-09-25-A-nguong-compliance.md`.

**Sàn cứng (CHẶN):**
1. Lint máy hoặc similar FAIL: F1 con số giá ngoài mốc KM7, F2 từ cấm, F3 chủ đề cấm, F4 tên tỉnh sai, placeholder; D1 độ tương đồng > 0.6.
2. Sai sự thật / bịa: khẳng định cụ thể, kiểm được mà brief/nguồn không có (dự án, địa danh hành chính, khuyến mại/vay khác nội dung §G, tư cách người đăng, con số, giao dịch/khách hàng/sự kiện).
3. Cam kết lợi nhuận/tăng giá/mua lại/kinh doanh chắc thắng (A2), huy động vốn (A3), nhận cọc sai điều kiện (A1), khan hiếm giả (B3).
4. F6 thanh toán, F7 so sánh đích danh, F8 mã lô/dãy, F11 sai tên dự án, F5 câu pháp lý khác câu chuẩn, SĐT/Zalo khác brief (E1).
5. Ảnh (A4, F12, D6): thiếu "minh hoạ"; ảnh AI có giấy tờ, con dấu, logo ngân hàng, giá, tiện ích không có, hoặc giả làm ảnh chụp nơi có thật; không có quyền dùng.
6. An toàn nick: vi phạm nội quy group đã ghi trong DB (D2); tag hàng loạt, link rút gọn (D4).
7. Thông tin cá nhân khách chưa ẩn danh/đồng ý (B4); M&A (§C).
8. Chỉ strict: thông điệp §G đang KHOÁ, dòng PL (F5), F9, F10.

**Luật khi phân vân:** chỉ CHẶN nếu là khẳng định cụ thể, kiểm được, thuộc nhóm 2 mà không có căn cứ (ghi rõ cần căn cứ gì). Còn lại → GÓP Ý.

**Được phép (không chặn, không bắt thêm rào đón):** giá chung chung đúng mốc KM7 §G ("chỉ khoảng 1 tỷ" một lô); nói mạnh lợi ích có trong brief; cảm nhận chủ quan, không đo được về khu vực ("đường vào dễ đi", "không khí thoáng"); khuyến mại §G diễn đạt tự nhiên (giữ đúng nội dung); CTA mạnh, nhiều kênh (inbox, gọi, Zalo, "nhắn ngay"); cấp bách từ sự thật có trong brief; chuyện thật của người đăng đã được xác nhận; câu hỏi mở; so sánh chung không đích danh.

**Góp ý (vẫn duyệt):** văn phong, giọng, độ dài, câu "nghe AI"; nhận xét đời thường; chi tiết đời tư nhỏ chưa xác nhận, không liên quan dự án/giao dịch (Lead tự quyết); mồi tương tác D5 (Lead thử ≤ 1/3 số bài/tuần và đo); D3; thiếu hashtag, `sources`, trường `images_meta`; nội quy group chưa có trong DB; nội dung dùng lại có quyền nhưng chưa dựng lại; chính tả (compliance tự sửa lỗi hiển nhiên).

**Cách gợi ý sửa:** sửa tối thiểu, giữ lực bán: xoá hoặc viết lại đúng câu có vấn đề; không đề xuất thêm câu rào đón ("nói rõ để anh chị yên tâm", "mình không dám hứa thay anh chị"…).
**Định dạng ghi chú:** duyệt `[TEST] OK | GÓP Ý: … | ĐIỀU KIỆN ĐĂNG: …` (≤ 500 ký tự; "ĐIỀU KIỆN ĐĂNG" chỉ ghi điều bắt buộc lúc đăng); chặn `[TEST] CHẶN <mã> | <câu vi phạm> | <cách sửa>`. Bỏ `[TEST]` khi strict.
**Không đổi ở bước này:** lint máy (`config/banned_terms.json`), `similarity_threshold`, giới hạn tần suất, người dùng duyệt mọi bài. F1 đã nới theo mốc KM7 (người dùng chốt 25/09, spec `workspace/plans/2026-09-25-A2-gia-moc.md`); F8 (không mã lô) là quy định công ty: chỉ đổi khi người dùng/công ty quyết.

## ⚙️ CHẾ ĐỘ HIỆN TẠI: xem `config/settings.json` → `compliance_mode`
**`test`** (từ 2026-09-23, người dùng quyết định: "đăng bài trước, chứng chỉ/luật để sau"):
- **TẮT:** F5 (không cần dòng pháp lý số văn bản; vẫn dùng câu chuẩn "đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô"), F9 (nick cá nhân đăng không cần số chứng chỉ), F10 (nói "sầm uất về đêm" không bắt buộc ảnh có ngày quay), yêu cầu tư liệu ở §G. Mọi thông điệp KM1–KM6 được dùng **đúng nội dung §G** (diễn đạt tự nhiên được, không đổi mức và điều kiện; trước 25/09 là "đúng câu chữ").
- **VẪN GIỮ:** sàn cứng §0 nhóm 1–7 (gồm quy định của HĐQT trong brief + lint tự động: F1 chỉ mốc giá KM7, F2 từ cấm, F3 chủ đề nhạy cảm, F4 địa danh, F6 thanh toán, F7 không so sánh, F8 không mã lô, B2 không placeholder, không cam kết lợi nhuận/kinh doanh chắc thắng). Vay: không nêu tên ngân hàng/lãi suất khi brief chưa có.
- Chuyển về **`strict`** trước khi chạy quảng cáo trả tiền hoặc khi có tư liệu (tuỳ người dùng).

## A. Pháp lý BĐS
- A1. **[CHẶN]** Thông tin dự án (vị trí, quy mô, pháp lý, tiến độ, giá) khớp `brief.md`; dự án chưa đủ điều kiện kinh doanh thì **không** chào bán/nhận đặt chỗ, giữ chỗ, đặt cọc.
- A2. **[CHẶN]** Không cam kết lợi nhuận, cam kết mua lại, "chắc chắn tăng giá", "lãi X%/năm" (trừ khi là chính sách chính thức bằng văn bản của CĐT, ghi rõ nguồn).
- A3. **[CHẶN]** Không huy động vốn / góp vốn đầu tư dưới mọi hình thức trong bài.
- A4. **[CHẶN khi thiếu "minh hoạ" hoặc ảnh làm sai lệch thực tế]** Phối cảnh/render ghi "Hình ảnh minh hoạ"; không dùng ảnh làm sai lệch thực tế.
- A5. **[CHẶN khi nêu quy hoạch/hạ tầng cụ thể mà không có nguồn, hoặc ghi "dự kiến" thành "đã duyệt"]** Thông tin quy hoạch/hạ tầng phải có nguồn chính thống kèm ngày; phân biệt "đã phê duyệt" vs "đề xuất/dự kiến".
- A6. **[CHẶN khi sai tư cách]** · **[GÓP Ý khi không nêu tư cách, chế độ test]** Người đăng thể hiện đúng tư cách (môi giới thuộc sàn/doanh nghiệp nào).

## B. Trung thực & dữ liệu
- B1. **[CHẶN khi con số không có trong brief/nguồn]** · **[GÓP Ý khi có trong brief nhưng frontmatter thiếu `sources`]** Mọi con số có nguồn trong frontmatter `sources`.
- B2. **[CHẶN]** Không còn placeholder `[CẦN XÁC NHẬN]` / `[ĐIỀN]`.
- B3. **[CHẶN]** Không tạo khan hiếm giả ("chỉ còn 2 căn") nếu brief không xác nhận.
- B4. **[CHẶN]** Câu chuyện khách hàng: đã ẩn danh hoặc có đồng ý.

## C. M&A **[CHẶN]**
- C1. Không nêu tên dự án, chủ đầu tư, địa chỉ chi tiết, số thửa, số quyết định có thể định danh.
- C2. Có câu yêu cầu NDA trước khi cung cấp hồ sơ.
- C3. Không công bố giá nếu brief ghi "không công khai".

## D. An toàn nền tảng Facebook
- D1. **[CHẶN]** Độ tương đồng với bài group khác trong 14 ngày ≤ 0.6.
- D2. **[CHẶN khi vi phạm nội quy đã ghi trong DB]** · **[GÓP Ý khi group chưa có nội quy trong DB]** Tuân `rules` của group (link, ngày rao, định dạng).
- D3. **[GÓP Ý]** Không chứa từ ngữ dễ bị lọc spam dồn dập (VD: nhiều "LH ngay", "giá sốc", viết hoa toàn bộ).
- D4. **[CHẶN]** Không tag hàng loạt, không link rút gọn đáng ngờ.
- D5. **[GÓP Ý, thử có kiểm soát từ 25/09]** Mồi tương tác (engagement bait): "comment 'quan tâm'/chấm (.) để nhận…", "tag người thân", "share để…". Meta hạ phân phối các bài và tài khoản làm vậy nhiều lần ([Transparency Center: Engagement Bait](https://transparency.meta.com/features/approach-to-ranking/content-distribution-guidelines/engagement-bait/)). Người dùng ưu tiên kéo nhiều khách nhất (25/09) nên không chặn: compliance ghi mã `D5`; Lead giữ **≤ 1/3 số bài/tuần** có mồi tương tác, ghi `cta_type` và so inbox/lead với bài CTA inbox; số liệu xấu (reach tụt, bị cảnh báo) thì tắt. Luôn được: câu hỏi mở thật để thảo luận, CTA cụ thể "inbox mình để nhận…". (Thêm 25/09; đổi mức 25/09)
- D6. **[CHẶN khi không có quyền dùng]** · **[GÓP Ý khi có quyền nhưng chưa dựng lại]** Video/ảnh lấy lại của người khác (vd. QC của môi giới) mà không chỉnh sửa có ý nghĩa có thể bị coi là nội dung không nguyên bản và bị hạ phân phối ([Transparency Center: Types of content we demote](https://transparency.meta.com/features/approach-to-ranking/types-of-content-we-demote/)). Ưu tiên bản gốc/quay mới; khi dùng lại phải dựng lại (cắt, khung, phụ đề) và có quyền dùng. (Thêm 25/09)

## E. Hình thức
- E1. **[GÓP Ý]** Chính tả, dấu tiếng Việt chuẩn (compliance tự sửa lỗi hiển nhiên) · **[CHẶN]** SĐT/Zalo sai brief.

---

## F. Quy tắc riêng: KDC Đồng Lạc (tên thương mại: Yên Thế Golden Hill)
Nguồn: `brief.md` §1.1 và §6. Mức xử lý ghi ở từng mục (xem §0); mục không ghi "chỉ strict" thì áp dụng cả chế độ test.

- F1. **[CHẶN]** Con số giá **chỉ được theo mốc KM7** ("chỉ khoảng 1 tỷ" / "tầm, cỡ, chừng 1 tỷ" một lô; §G; người dùng chốt 25/09/2026). Chặn: đơn giá ("tr/m²"), giá từng lô/vị trí, mọi con số giá khác ("chỉ 1 tỷ", "hơn/dưới 1 tỷ", "1,2 tỷ", "chỉ từ …"), "giá gốc/sỉ/sốc", ngân sách trong bảng persona (dữ liệu nội bộ). Lint máy kiểm; mốc tự hết hạn sau 30 ngày (`config/banned_terms.json` → `_F1_moc_gia`).
- F2. **[CHẶN]** Từ cấm: `nhất`, `duy nhất`, `độc nhất`, `số 1`, `rẻ nhất`, `x2`, `không rủi ro`, `sắp lên thành phố`, `sổ đỏ trao tay`, `nhận sổ ngay`, `0 đồng`, `ai cũng vay được`, `cam kết` (khi nói về vay/lợi nhuận).
- F3. **[CHẶN]** Không nhắc: dư nợ, ngân hàng tài trợ, giải chấp, thế chấp, GPMB, nhà thầu, quyết toán, thuế dự án, MB Bank, "Blue Sky", giá Sở phê duyệt.
- F4. **[CHẶN]** Địa danh: chỉ "xã Yên Thế, thành phố Bắc Ninh"; cho phép kèm "(khu vực Yên Thế – Bắc Giang cũ)". Cấm "tỉnh Bắc Giang", "tỉnh Bắc Ninh". Căn cứ: Bắc Ninh là thành phố trực thuộc trung ương từ 20/09/2026 theo Nghị quyết số 39/2026/QH16 (nguồn có số hiệu: https://www.vietnam.vn/en/bac-ninh-chinh-thuc-tro-thanh-thanh-pho-truc-thuoc-trung-uong-tu-ngay-20-9; nguồn không có số hiệu: vietnamplus.vn). Bài nêu số hiệu phải dẫn nguồn có số hiệu.
- F5. **[CHẶN khi dùng câu pháp lý khác câu chuẩn]** · **[chỉ strict: dòng PL số văn bản]** Pháp lý chỉ dùng đúng câu: "đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô". Brief yêu cầu dòng pháp lý "trên mọi ấn phẩm", nên **mọi bài có nhắc tên dự án / chào bán** phải kèm **dòng pháp lý** (số hiệu + ngày văn bản Sở Xây dựng, xem PL ở G). Bài kiến thức chung không nhắc dự án thì không cần. PL còn KHOÁ thì chỉ được đăng bài kiến thức chung.
- F6. **[CHẶN]** Thanh toán: chỉ vào tài khoản công ty tại BIDV; không có câu nào gợi ý chuyển khoản cá nhân, cọc qua đại lý/môi giới.
- F7. **[CHẶN]** Không so sánh đích danh dự án/CĐT khác.
- F8. **[CHẶN]** Không nhắc mã lô / tên dãy cụ thể trên bài hoặc comment công khai (không có danh sách lô được duyệt để đối chiếu). Muốn tư vấn lô cụ thể thì chuyển inbox cho Phòng KD.
- F9. **[chỉ strict]** Tư cách người đăng: Page = CĐT (Công ty CP Đầu tư và Phát triển Thắng Anh). Nick cá nhân đăng bài phải ghi rõ là nhân viên CĐT kèm số chứng chỉ môi giới (brief §1 còn [ĐIỀN]; chưa có thì **không đăng bằng nick cá nhân**).
- F10. **[chỉ strict]** Ảnh "buổi tối sầm uất" phải là ảnh thật có ghi ngày quay trong frontmatter (`images_meta`); cấm ảnh mạng hoặc ảnh AI minh hoạ cho thông điệp này (ảnh AI cho thông điệp này vẫn CHẶN theo F12 ở mọi chế độ).
- F11. **[CHẶN khi sai tên dự án]** · **[GÓP Ý khi thiếu hashtag]** Tên dự án trên bài/comment: **Yên Thế Golden Hill** (tên thương mại, người dùng chốt 25/09), hashtag `#YenTheGoldenHill`. Không dùng "Đồng Lạc Golden Hill". Khi cần dẫn văn bản pháp lý (dòng PL) thì dùng tên pháp lý "Khu dân cư trung tâm xã Đồng Lạc".
- F12. **[CHẶN]** · **[GÓP Ý khi chỉ thiếu trường `images_meta`]** Ảnh/video do AI tạo (người dùng cho phép 25/09): phải ghi "Ảnh minh hoạ" (hoặc "Phối cảnh minh hoạ") trên ảnh hoặc ngay trong bài; phối cảnh dự án chỉ được thể hiện những gì có trong brief/mặt bằng 1/500 (không thêm tiện ích chưa có); cấm giấy tờ nhà đất, con dấu, logo ngân hàng, con số giá do AI vẽ; cấm dùng ảnh AI cho KM3 và cho nơi có thật ở Yên Thế (đường, phố, khu đất) như thể ảnh chụp (F10). Chữ tiếng Việt trên ảnh phải do `tools/media.py` chèn, không để AI tự viết. `images_meta` ghi nguồn (vd `ai: gemini`).
- F13. **[CHẶN khi tự giới thiệu sai, bịa trải nghiệm/giao dịch/sự kiện liên quan dự án, hoặc địa danh hành chính sai]** · **[GÓP Ý: nhận xét đời thường; chi tiết đời tư nhỏ không liên quan dự án/giao dịch; liệt kê nhiều tên xã, phường]** Câu tự giới thiệu và trải nghiệm ngôi thứ nhất phải đúng sự thật: nick chính xưng "làm bên chủ đầu tư" (không "nhân viên kinh doanh", người dùng xác nhận 25/09); cấm kể trải nghiệm chưa có dữ liệu hoặc chưa được người dùng xác nhận khi trải nghiệm đó nói về dự án, khách hàng, giao dịch. Địa danh hành chính phải khớp văn bản **mới nhất tại ngày đăng**: huyện Yên Thế cũ nay là 4 xã (Yên Thế, Đồng Kỳ, Tam Tiến, Xuân Lương) và **phường Bố Hạ** (NQ 1658/NQ-UBTVQH15 từ 01/7/2025; Bố Hạ lên phường từ 20/9/2026 theo NQ 388/NQ-UBTVQH16; xã Yên Thế vẫn là xã); không viết như thể cả vùng Yên Thế cũ là xã Yên Thế; hạn chế liệt kê tên xã, phường khác trong bài.

## G. Sổ cái thông điệp: thông điệp nào được dùng khi nào
Compliance đối chiếu bài với bảng này. **[chỉ strict]** Thông điệp đang **KHOÁ** mà xuất hiện trong bài thì CHẶN. Ở `test`: dùng được mọi KM, giữ đúng nội dung (diễn đạt tự nhiên được); đổi nội dung (bỏ "đến", bỏ "theo chính sách CĐT", nêu tên ngân hàng/lãi suất) = CHẶN nhóm 2 §0. Người dùng cập nhật cột "Trạng thái" khi đã có tư liệu.

| # | Thông điệp (câu được dùng) | Tư liệu bắt buộc | Trạng thái |
|---|---|---|---|
| KM1 | "Đất nền giá mềm tại thành phố trực thuộc trung ương" / "Sở hữu đất thành phố Bắc Ninh với chi phí hợp lý" | Không cần (không kèm số) | **MỞ** |
| KM2 | "Khu dân cư quy hoạch đồng bộ 12,1 ha – 377 lô tại trung tâm Yên Thế" | Mặt bằng 1/500 + ảnh flycam | **KHOÁ** (chưa có ảnh) · chỉ nói bằng chữ, không kèm ảnh → MỞ |
| KM3 | "Tối nào quảng trường trong khu cũng có hàng trò chơi cho trẻ con, hàng quán, người ra chơi đông" (người dùng xác nhận 28/09 tối: "tối nào cũng có"); "sầm uất", "chợ đêm", "mặt bằng kinh doanh sẵn khách" (hứa hẹn kinh doanh, không kiểm chứng được) vẫn KHOÁ | Người dùng (CĐT) xác nhận 28/09 + ảnh đêm thật m01b; chuyển strict: video/ảnh buổi tối có ngày quay | **MỞ** phần quảng trường buổi tối · **KHOÁ** phần còn lại |
| KM4 | "Mua trực tiếp Chủ đầu tư – chiết khấu đến 10% (theo chính sách CĐT)" (26/09 09:5x người dùng chốt lại "chiết khấu lên đến 10%"; trước đó 25/09 ghi 6%) | Số QĐ chiết khấu, điều kiện, thời hạn | **KHOÁ** · riêng "Mua trực tiếp Chủ đầu tư" (không kèm chiết khấu) → MỞ |
| KM6 | "Ngân hàng ... hỗ trợ cho vay đến 50% giá trị lô" | Văn bản hợp tác cho vay (tên NH, số, ngày) | **KHOÁ** (người dùng xác nhận chính sách có thật 25/09, chưa có văn bản; chế độ test dùng được, giữ đúng nội dung: "đến 50% giá trị lô", không tên NH/lãi suất) |
| KM5 | CTA: "Nhắn tin/gọi 0965 539 599 để nhận bảng giá và chính sách" (từ 25/10 trong chữ bài viết dạng 0965.539.599 — người dùng) | Không cần | **MỞ** |
| KM7c | "CHỈ VỚI 500 TRIỆU ĐÃ SỞ HỮU LÔ ĐẤT" + thân bài có điều kiện (trả trước 500 triệu cho lô đến khoảng 1,3 tỷ, 4 đợt 15%, sổ T+180) | Ảnh CSBH 21/10 + người dùng chọn câu (đã được báo rủi ro) | **MỞ** (đến 20/11/2026) |
| KM11 | Tặng 30 tấn xi măng + 2 vạn gạch cho cư dân về ở sớm; ưu đãi 2% cư dân Bắc Ninh, 3% thanh toán sớm, 15 khách đầu tiên, đến 31/10/2026 | Ảnh CSBH 21/10 | **MỞ** (đến 31/10/2026) |
| KM7b | "CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU" (người dùng xác nhận 14/10/2026 còn lô dưới 1 tỷ) | Người dùng xác nhận, hạn 30 ngày (→ 13/11) | **MỞ** (đến 13/11/2026) |
| KM7 | Giá chung chung: "Chỉ khoảng 1 tỷ là mua được đất…" (biến thể "tầm/cỡ/chừng 1 tỷ" một lô) | Người dùng xác nhận mốc (25/09/2026, hạn 30 ngày); strict: bảng giá có ngày của PKD | **MỞ** (đến 25/10/2026) |
| PL | Dòng pháp lý: "Sở Xây dựng xác nhận đủ điều kiện chuyển nhượng tại văn bản số ... ngày ..." | Số hiệu + ngày văn bản | **KHOÁ** |
| KM8 | Chương trình "Cọc đất – Nhận lộc": cọc 1 lô nhận 1 chậu cảnh đá + 1 phiếu bốc thăm iPhone (quay 07/11, 21/11, 26/12) | Văn bản Sở Công Thương (số, ngày) + thể lệ đã duyệt | **KHOÁ** (dự kiến có văn bản ~20/10) |
| KM9 | Đêm hội 07/11 tại dự án: "mời cả nhà về xem đất, chọn lô tại chỗ" | Người dùng xác nhận giờ, địa điểm, nội dung chương trình | **KHOÁ** tới khi người dùng xác nhận |
| KM10 | Gói Đất + Nhà: "gửi tiền về – nhận nhà, không phải về giám sát", 3 mẫu nhà, giá xây cố định | Hợp đồng đối tác xây dựng + bảng giá xây có ngày | **KHOÁ** (dự kiến công bố 09–15/11) |

## H. Quảng cáo trả tiền (bài có `loai: quang-cao`) — thêm 15/10/2026
Nguồn: `workspace/research/2026-10-14-best-practice-quang-cao-bds.md` (§B2–B4) và `2026-10-15-thu-vien-quang-cao-cdt-lon.md`; phương án `workspace/reports/2026-10-15-phuong-an-tong-the-quang-cao.md`. §H áp dụng **thêm** vào §A–G. Quảng cáo trả tiền **luôn chấm như strict** (mục "Chế độ hiện tại": chuyển strict trước khi chạy QC trả tiền), kể cả khi `compliance_mode` còn `test` cho bài nhóm.

**Điều kiện chạy** (người dùng cập nhật; còn "CHƯA" thì mọi QC = CHẶN `H1`):
| Điều kiện | Trạng thái |
|---|---|
| Website CĐT đã công khai thông tin dự án (Luật KDBĐS 2023 Đ6; NĐ 96/2024 Đ4: sổ, văn bản Sở cho chuyển nhượng nền, hạ tầng, tình trạng thế chấp) | CHƯA xác nhận |
| Dòng pháp lý PL (số hiệu + ngày văn bản Sở Xây dựng) | CHƯA (KHOÁ ở §G) |
| Chạy từ Fanpage CĐT chính chủ + tài khoản quảng cáo doanh nghiệp | CHƯA xác nhận |

- **H1 [CHẶN]** Thiếu điều kiện chạy ở bảng trên; hoặc nội dung QC khác thông tin đã công khai (Luật QC Đ8 k9; Luật KDBĐS Đ8).
- **H2 [CHẶN]** So sánh trực tiếp với dự án/đối thủ cụ thể, kể cả ám chỉ rõ (nêu tên "Ion City", "dự án mấy tỷ bên phường…", "rẻ hơn dự án X") — Luật QC Đ8 k10.
- **H3 [CHẶN]** Ảnh, video, lời nói, tên của khách hàng/người thật khi chưa có đồng ý bằng văn bản ghi ở `workspace/quyet-dinh.md` hoặc frontmatter `dong_y:` — Luật QC Đ8 k8. (Ảnh lễ trao sổ 09/10 đã có đồng ý, xem quyet-dinh.md.)
- **H4 [CHẶN]** Hứa lợi nhuận, thu nhập, tăng giá: "tiềm năng tăng giá", "dòng tiền x/tháng", "cho thuê được x", "sinh lời", "an toàn tuyệt đối" — Luật KDBĐS Đ8 (gian lận, lừa dối) + brief §6.
- **H5 [CHẶN]** Khuyến mại có quà/bốc thăm (KM8) khi KM8 còn KHOÁ; khi MỞ: phải có thể lệ tóm tắt + số văn bản Sở Công Thương.
- **H6 [CHẶN]** Khan hiếm hoặc "đám đông" không kiểm chứng: "lô nội bộ", "quỹ căn ngoại giao", "chỉ còn x lô", "+x khách đã đăng ký", "99 khách đầu tiên" khi không có số liệu/chính sách văn bản (cùng tinh thần F13, B3).
- **H7 [CHẶN]** Gây nhầm danh tính: chạy từ page không phải Fanpage CĐT; tự xưng "đại lý độc quyền", "phòng kinh doanh CĐT" khi không đúng.
- **H8 [CHẶN khi có con số]** Mọi con số (giá, diện tích, khoảng cách, thời gian, tiến độ) phải có dòng "(*)" cuối bài, ví dụ: "(*) Thông tin theo chính sách của Chủ đầu tư tại thời điểm đăng, áp dụng có điều kiện; khoảng cách, thời gian di chuyển là ước tính."
- **H9 [CHẶN]** Thu thập dữ liệu: form phải có ô đồng ý bắt buộc (custom disclaimer) + link chính sách bảo mật; không hỏi số CCCD, thu nhập chi tiết; không nhắm tệp tải lên từ danh sách khách chưa đồng ý; không mua/dùng data ngoài (Luật 91/2025 Đ7, Đ9, Đ28).
- **H10 [CHẶN]** Nhắm đối tượng: không nhắm Mỹ, Canada, EU (Meta Special Ad Category: Housing); không chọn vị trí theo tên tỉnh "Bắc Ninh" (dùng bán kính + từng xã/huyện Bắc Giang cũ).
- **H11 [GÓP Ý]** Kỹ thuật: câu mở 3 giây là nỗi lo/mong muốn của người mua (không mở bằng tên dự án); phần chữ hiện trước "Xem thêm" ≤ 125 ký tự; tiêu đề ≤ 40 ký tự; mô tả ≤ 30 ký tự; video dọc 9:16 có phụ đề; mỗi mẫu một góc khác nhau.

**Định dạng ghi chú:** `[QC] OK | GÓP Ý: …` hoặc `[QC] CHẶN H<số> | <câu vi phạm> | <cách sửa>`. Ca kiểm tra: `evals/compliance/16-*.md` trở đi (`loai: quang-cao`).
