# Spec + kế hoạch (A): Giảm ngưỡng agent compliance — tách CHẶN / GHI CHÚ, ưu tiên kéo khách

Ngày: 2026-09-25 · Người làm: Lead (Claude)
Yêu cầu của chủ dự án (nguyên văn):
- 15:46: "giảm ngưỡng của agent compliance xuống, giọng điệu các caption vẫn còn AI lắm và nghe không được thật tình…"
- 16:0x: "Giảm thêm phần compliance xuống, mục tiêu để kéo được nhiều khách nhất có thể"

Cổng duyệt: spec bản 1 → Gemini **DUYỆT** 15:5x (lời khuyên: sao lưu 2 file trước khi sửa; so đáp án kiểm thử bằng script, không cần agent chấm). Bản 2 (file này) thêm yêu cầu "giảm thêm" → nộp cổng kế hoạch.

## 1. Vấn đề (có dữ liệu)
- [DỮ LIỆU] 4 lượt duyệt (task 3, 4, 5, 9) có 3 lần chặn (bài 10, 2, 3). Bài 10 và 3 chặn đúng (sai địa danh hành chính). **Bài 2 bị chặn chỉ vì một câu nhận xét đời thường** ("người mua lần đầu hay lúng túng đúng ở mấy chỗ này") bị coi là "trải nghiệm chưa có căn cứ" (F13) → phải viết lại, mất một vòng.
- [DỮ LIỆU] Ghi chú duyệt task 9 dài 1.200–2.000 ký tự/bài, trộn "phải sửa" với "nên cân nhắc" → dễ bỏ sót điều kiện thật (bài học BH-0080).
- [DỮ LIỆU] Prompt compliance ghi "khó tính, thà chặn nhầm còn hơn để lọt"; checklist §F ghi "vi phạm bất kỳ mục nào → reject" cho mọi mục.
- [GIẢ THUYẾT] Kiểu sửa "an toàn" do compliance gợi ý (thêm câu rào đón) làm bài "nghe như AI" và mất lực bán. Kiểm ở yêu cầu (B).

## 2. Mục tiêu
Compliance chỉ **chặn** khi có vi phạm thật (luật, sự thật, quy định công ty, an toàn nick); mọi thứ khác **cho qua kèm góp ý ngắn**, và **không làm yếu lực bán** của bài. Không nới hàng rào máy.

## 3. Bảng mức xử lý
**CHẶN (reject) — "sàn cứng", chỉ các nhóm sau:**
1. Lint máy FAIL: F1 con số giá, F2 từ cấm, F3 chủ đề cấm, F4 tên tỉnh sai, placeholder. (Quy định công ty trong brief §1.1/§6 + lint; đổi phải do chủ dự án/công ty quyết.)
2. Sai sự thật / bịa — **khẳng định cụ thể, kiểm được** mà không có trong brief/nguồn: dự án (vị trí, quy mô, pháp lý, tiện ích, tiến độ), địa danh hành chính, khuyến mại và vay (đổi nội dung: bỏ "đến", bỏ "theo chính sách CĐT", nêu tên ngân hàng/lãi suất), tư cách người đăng, con số; giao dịch/khách hàng/sự kiện bịa ("tuần trước 3 khách chốt").
3. Cam kết lợi nhuận / tăng giá / mua lại / kinh doanh chắc thắng (A2), huy động vốn (A3), nhận cọc sai điều kiện (A1), khan hiếm giả (B3).
4. F6 thanh toán ngoài TK công ty, F7 so sánh đích danh, F8 mã lô/dãy, F11 sai tên dự án, câu pháp lý khác câu chuẩn F5.
5. Ảnh: phối cảnh/ảnh AI không ghi "minh hoạ"; ảnh AI có giấy tờ, con dấu, logo ngân hàng, giá, tiện ích không có; ảnh AI giả làm ảnh chụp nơi có thật (F12, A4); ảnh/video không có quyền dùng (D6).
6. An toàn nick/kênh: similar > 0.6 (D1, dấu hiệu spam); vi phạm nội quy group **đã ghi trong DB** (D2: bài bị admin xoá = 0 khách); tag hàng loạt, link rút gọn (D4).
7. Thông tin cá nhân khách chưa ẩn danh/đồng ý (B4); M&A §C.
8. Chỉ khi `strict`: thông điệp §G KHOÁ, F5 dòng PL, F9, F10.

**ĐƯỢC PHÉP — khuyến khích, không chặn, không bắt rào đón** (để kéo khách):
nói mạnh các lợi ích có trong brief; cảm nhận chủ quan, không đo được về khu vực ("đường vào dễ đi", "không khí thoáng"); khuyến mại §G diễn đạt tự nhiên (giữ đúng nội dung, không cần nguyên văn); CTA mạnh, nhiều kênh (inbox, gọi, Zalo, "nhắn ngay"); tạo cấp bách từ sự thật có trong brief (chính sách có thời hạn); chuyện thật của người đăng đã được xác nhận (quê Yên Thế); câu hỏi mở; so sánh chung không đích danh ("so với mua qua nhiều lớp trung gian").

**GHI CHÚ (approved + góp ý)** — mọi thứ còn lại, ví dụ: văn phong, giọng, độ dài, bố cục, câu "nghe AI"; nhận xét đời thường; chi tiết đời tư nhỏ chưa xác nhận, không liên quan dự án/giao dịch (Lead tự quyết); **mồi tương tác (D5)** — "comment/chấm để nhận", "tag người thân", "share giúp" — chuyển thành GHI CHÚ: **Lead thử có kiểm soát ≤ 1/3 số bài/tuần**, ghi `cta_type`, đo inbox/lead so với bài CTA inbox ([NGUỒN] Meta hạ phân phối engagement bait; lợi/hại thực tế với group BĐS là [GIẢ THUYẾT] → đo); từ ngữ dễ bị coi spam (D3); thiếu hashtag; số có trong brief nhưng thiếu `sources`; `images_meta` thiếu trường; lỗi chính tả (compliance tự sửa lỗi hiển nhiên như cũ); nội quy group chưa có trong DB; nội dung dùng lại có quyền nhưng chưa dựng lại.

**Luật khi phân vân:** chỉ CHẶN nếu là khẳng định cụ thể, kiểm được, thuộc nhóm 2 mà không có căn cứ (nêu rõ cần căn cứ gì). Còn lại → GHI CHÚ.

**Cách gợi ý sửa:** sửa tối thiểu, giữ lực bán: xoá hoặc viết lại đúng câu vi phạm; **không thêm câu rào đón/disclaimer** ("nói rõ để anh chị yên tâm", "mình không dám hứa…").

**Định dạng ghi chú:** duyệt: `[TEST] OK | GÓP Ý: … | ĐIỀU KIỆN ĐĂNG: …` (≤ 500 ký tự; "ĐIỀU KIỆN ĐĂNG" chỉ ghi điều bắt buộc lúc đăng). Chặn: `CHẶN <mã> | <câu vi phạm> | <cách sửa>`.

## 4. KHÔNG làm (trong bước này)
Không sửa lint máy (`config/banned_terms.json`, `BLOCKED_BY_LINT`), `similarity_threshold`, giới hạn tần suất, `require_human_approval` (người dùng vẫn duyệt mọi bài — L1), `compliance_mode` (vẫn `test`). Không sửa bài viết (yêu cầu B). **Luật không nêu giá (F1) và mã lô (F8) là quy định công ty** → hỏi chủ dự án, không tự bỏ.

## 5. Kế hoạch
1. Sao lưu `.claude/agents/compliance.md` + `workspace/compliance-checklist.md` → `workspace/reports/backup/2026-09-25-A/`.
2. Viết lại `compliance.md` theo §3 (vai trò, bước lint giữ nguyên, bảng mức, luật phân vân, cách gợi ý sửa, định dạng ghi chú).
3. Checklist: thêm §0 "Mức xử lý" (tóm tắt §3); gắn nhãn `[CHẶN]`/`[GHI CHÚ]`/`[CHẶN khi…]` từng mục A–F; sửa dòng đầu §F.
4. Evals: sửa ca 06 (tên cũ → "Yên Thế Golden Hill", ca chỉ còn kiểm F5); thêm 5 ca: 11 nhận xét đời thường + mời chia sẻ nhẹ (APPROVE), 12 giao dịch bịa (REJECT), 13 "Bố Hạ là xã" (REJECT), 14 tên dự án cũ (REJECT), 15 CTA "comment để nhận thông tin" (APPROVE ở `test`).
5. `python tools/evals.py` (lớp máy) → 15/15.
6. Eval lớp agent **trong bản sao tạm** (BH-0007: không ghi vào DB thật): chép `tools/ config/ workspace/ content/ data/ evals/` sang thư mục tạm (không chép `.profiles`, `.env`, `assets`); tạo 15 post tạm `review` + `content/_eval/`; chụp "dấu vân tay" DB thật (md5 của `id, status, compliance_note` bài 3–12; bài 1, 2, 5 loại ra vì phiên cũ có thể đang cập nhật trạng thái đăng); giao 1 agent `compliance` duyệt như bài thường trong thư mục tạm; script so trạng thái với `expect_agent_test` → `workspace/reports/eval-compliance-2026-09-25.md`; canh gác: dấu vân tay không đổi + DB thật không có post nào trỏ tới `content/_eval/` + thư mục thật không có `content/_eval/`; xoá bản sao tạm.
7. Đạt → ghi SCORECARD B2, STATE, `docs/nhat-ky-duyet.md` → Gemini nghiệm thu → báo chủ dự án + 1 câu hỏi (nêu giá?).

## 6. Thế nào là xong
- Lớp máy 15/15. Lớp agent: 100% ca REJECT bị chặn; ≥ 90% ca APPROVE được duyệt; ghi chú ca APPROVE ≤ 500 ký tự.
- DB thật không đổi trong lúc chạy eval (canh gác). Bản sao lưu tồn tại.

## 7. Rủi ro
- Lọt câu mơ hồ nhiều hơn → giữ "sàn cứng" §3 + người dùng duyệt mọi bài + lint chặn cứng lúc đăng.
- Mồi tương tác có thể làm Meta hạ phân phối nick → chỉ thử ≤ 1/3 số bài/tuần và đo; xấu thì tắt.
- Eval lớp agent ~150–250 nghìn token (1 agent).
