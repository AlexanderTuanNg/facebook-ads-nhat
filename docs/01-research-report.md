# Báo cáo Research: Hệ thống agent marketing Facebook cho BĐS / Dự án / M&A

Ngày: 2026-09-23 · Phạm vi: repo GitHub, giới hạn kỹ thuật của Meta, phương pháp chuyên gia VN, pháp lý BĐS

---

## 1. Kết luận nhanh

| Hạng mục | Kết luận |
|---|---|
| Nền tảng agent | **Claude Code thuần**: session chính đóng vai Lead (qua skill `/lead`), các subagent đặt trong `.claude/agents/*.md`. Subagent **không gọi được subagent khác**, nên mọi điều phối đều đi qua Lead |
| Repo nên tái dùng | `ai-marketing-claude` (MIT, ~2.7k★) để tham khảo cấu trúc skill router + subagent song song. **Không dùng nguyên**: repo này thiên về audit website/US market |
| Đăng Fanpage | **Meta Graph API** (chính thức). Tự động 100%: đăng, hẹn giờ (10 phút → 30 ngày), đọc comment, trả lời |
| Đăng Group | **Không còn API** (Meta tắt 22/04/2024), chỉ còn đường giả lập trình duyệt (Playwright) |
| Repo Group tham khảo | `ariknih/autopost-facebook-group` (MIT, Playwright, lưu session, có delay) chỉ lấy ý tưởng; repo nhỏ (5★), chỉ nên đọc để học chứ không nên phụ thuộc |
| A/B Group | **Nhánh A** bán tự động (nick chính, người bấm Đăng) vs **Nhánh B** tự động hoàn toàn (nick phụ). So theo: lead/bài, tỉ lệ bài bị admin duyệt/xoá, sức khoẻ nick |
| Pháp lý | BĐS là ngành bị quản lý chặt về quảng cáo. Cần agent **Compliance** duyệt mọi bài trước khi đăng |

---

## 2. Repo GitHub đã khảo sát

### 2.1 Khung agent / marketing cho Claude Code
- **[zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude)**: 14 skill + 5 subagent song song, có router `market/SKILL.md`, MIT.
  → **Lấy**: pattern router dispatch sang skill con và chạy subagent song song. **Bỏ**: nội dung audit web/SEO/email.
- **[VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)** (content-marketer.md), **[rshah515/claude-code-subagents](https://github.com/rshah515/claude-code-subagents)** (content-strategist, social-strategist): các file prompt subagent mẫu.
  → **Lấy**: cấu trúc frontmatter và cách mô tả vai trò, sau đó viết lại toàn bộ cho BĐS VN.
- **[borghei/Claude-Skills – social-media-manager](https://github.com/borghei/Claude-Skills/blob/main/marketing/social-media-manager/SKILL.md)**, **[SpillwaveSolutions/running-marketing-campaigns-agent-skill](https://github.com/SpillwaveSolutions/running-marketing-campaigns-agent-skill)**: tham khảo khung lịch nội dung, UTM, quy trình duyệt bài.

### 2.2 Tự động Facebook Group
- **[ariknih/autopost-facebook-group](https://github.com/ariknih/autopost-facebook-group)**: Playwright, nhiều tài khoản qua file session `.json`, upload nhiều ảnh, delay tự nhiên, gặp group lỗi thì bỏ qua. MIT, 5★.
- **[DevSkits916/PasteHappy-Python](https://github.com/DevSkits916/PasteHappy-Python)**: Flask + Playwright, *trợ lý* đăng group có giao diện, đi theo hướng bán tự động (khớp Nhánh A).
- **[ethanXWL/Python-Selenium-Facebook-group-auto-poster](https://github.com/ethanXWL/Python-Selenium-Facebook-group-auto-poster)**: Selenium, cũ, không dùng.
- **Đánh giá chung**: selector DOM của Facebook đổi liên tục nên mọi repo loại này sẽ hỏng định kỳ. **Tự viết module Playwright nhỏ** có lớp selector tách riêng (dễ sửa) sẽ tốt hơn fork. Ngoài ra, trong Claude Code có sẵn **Claude in Chrome** để thao tác trên trình duyệt thật của anh, dùng tốt cho Nhánh A.

---

## 3. Giới hạn kỹ thuật của Meta (2026)

- **Groups API**: đã ngừng từ 22/04/2024. Các tool thương mại (Recurpost, v.v.) giờ chỉ **gửi nhắc để người dùng tự bấm đăng**.
- **Pages API** vẫn hoạt động:
  - Quyền: `pages_manage_posts`, `pages_read_engagement`, `pages_show_list`, `pages_manage_metadata` (và `pages_manage_engagement` để trả lời comment).
  - **Mẹo**: nếu anh là admin của cả App lẫn Page thì app ở chế độ Development vẫn dùng được các quyền này **mà không cần App Review**. Chỉ cần review khi mở cho người ngoài.
  - Page Access Token lấy từ long-lived user token và **không hết hạn** (trừ khi đổi mật khẩu hoặc đổi quyền).
  - Hẹn giờ: `published=false` kèm `scheduled_publish_time` (từ 10 phút đến 30 ngày).
  - Rate limit: khoảng 200 call/giờ/user, dư sức cho 1 người dùng.
- **Page Insights**: Meta đã **khai tử một loạt metric từ 15/06/2026** (gọi sẽ báo lỗi invalid metric). Agent Analytics phải dùng metric mới (nhóm *views*) và cần kiểm tra lại danh sách metric trên docs Meta khi code.
- **Không có API tạo Fanpage**: phải tạo tay.

---

## 4. Phương pháp của chuyên gia VN, áp vào BĐS

Tổng hợp từ các bài hướng dẫn ([Rever](https://agent.rever.vn/blog/bai-dang-marketing-bat-dong-san-hap-dan-tren-facebook-0), [Huỳnh Quốc Cường](https://huynhquoccuong.com/huong-dan-chay-quang-cao-bat-dong-san-tren-facebook.html), [Zafago](https://zafago.com/cach-chay-quang-cao-facebook-bat-dong-san/), [Social Boost Asia](https://socialboost.asia/vi-vn/blog/facebook-marketing-2026-chien-luoc-xay-dung-fanpage-tu-0), [bannha.net](https://bannha.net/cach-dang-bai-ban-nha-tren-facebook/), [Brands Vietnam](https://www.brandsvietnam.com/congdong/topic/344841-chien-luoc-7-buoc-facebook-marketing-hieu-qua-voi-muc-dich-doanh-nghiep)):

1. **Group hiệu quả nhất khi đóng vai chuyên gia, không phải người rao.** Group BĐS chất lượng ưu tiên phân tích thị trường, quy hoạch, kinh nghiệm pháp lý. Đăng tin rao thuần thì dễ bị admin xoá.
2. **Content pillar đề xuất** (tỉ lệ mở đầu, Analytics sẽ tự điều chỉnh):
   - 35% **Kiến thức / phân tích**: quy hoạch, giá khu vực, pháp lý, dòng tiền
   - 25% **Dự án / sản phẩm**: thông tin đã được phép công khai
   - 20% **Case / uy tín cá nhân**: giao dịch đã chốt, kinh nghiệm, hậu trường
   - 10% **Tương tác**: hỏi đáp, bình chọn, "anh chị đang tìm ở khu nào"
   - 10% **M&A / đầu tư**: teaser ẩn danh, xu hướng thương vụ
3. **Kịch bản chăm group**: tham gia → tương tác hữu ích 1–2 tuần → mới đăng bài giá trị → sau đó mới đăng bài có CTA. Mỗi group một biến thể nội dung, **không đăng y hệt nhiều group** (Facebook nhận diện spam qua nội dung trùng).
4. **Chuyển đổi**: CTA dẫn về inbox Page / Zalo và có kịch bản inbox theo từng giai đoạn (hỏi nhu cầu, tài chính, khu vực, rồi hẹn xem nhà).
5. **Riêng M&A dự án**: đối tượng là nhà đầu tư, chủ đất, doanh nghiệp. **Không công khai chi tiết định danh dự án**, chỉ đăng *teaser* ẩn danh (vị trí cấp tỉnh/quận, quy mô, pháp lý đang ở bước nào), yêu cầu NDA trước khi gửi hồ sơ. Kênh phù hợp: group đầu tư/doanh nhân và fanpage mang tính thương hiệu tư vấn.

---

## 5. Pháp lý: rào chắn bắt buộc cho agent Compliance

> Đây là tóm tắt định hướng, **không phải tư vấn pháp lý**. Trước khi chạy thật, anh cần luật sư hoặc pháp chế xác nhận.

- **[Luật Kinh doanh BĐS 2023 (29/2023/QH15)](https://vanban.chinhphu.vn/?pageid=27160&docid=209624&classid=1&typegroupid=3)**:
  - Chủ đầu tư phải **công khai đầy đủ, trung thực** thông tin BĐS/dự án trước khi đưa vào kinh doanh.
  - **Cấm** làm sai lệch thông tin và gian dối (Điều 8).
  - Cá nhân hành nghề môi giới cần **chứng chỉ** và phải hành nghề trong doanh nghiệp môi giới hoặc sàn giao dịch.
- **Nghị định 339/2026/NĐ-CP** (ban hành 26/08/2026) quy định xử phạt trong kinh doanh BĐS, mức phạt tới **1 tỷ đồng** ([nguồn](https://congan.cantho.gov.vn/tuyen-truyen-pho-bien-giao-duc-phap-luat/nam-vung-quy-dinh-moi-ve-xu-phat-vi-pham-hanh-chinh-trong-kinh-doanh-bat-dong-san-10384.html)). Cần đọc toàn văn để lập checklist.
- **Checklist Compliance (bản nháp)**:
  - Không cam kết lợi nhuận hay "chắc chắn tăng giá"
  - Không nhận huy động vốn hay đặt cọc khi dự án chưa đủ điều kiện
  - Phối cảnh phải ghi "hình ảnh minh hoạ"
  - Có nguồn cho mọi số liệu quy hoạch
  - Không nêu tên dự án M&A khi chưa có NDA
  - Ghi đúng tư cách người đăng (môi giới thuộc sàn nào)

---

## 6. Kiến trúc đề xuất (sau research)

```
/lead  (skill, chạy trong session chính = Lead Agent)
  │  đọc brief + playbook + số liệu → ra kế hoạch tuần → giao việc
  ├─ researcher        : thị trường, đối thủ, trend, danh sách group (đánh giá chất lượng group)
  ├─ strategist        : persona, pillar, lịch 30 ngày, phân bổ group ↔ nick ↔ nhánh A/B
  ├─ copywriter        : viết bài + biến thể theo group, hook, CTA, prompt ảnh
  ├─ compliance        : duyệt pháp lý + chống trùng nội dung (bắt buộc trước khi đăng)
  ├─ publisher         : Page qua Graph API; Group nhánh A (Chrome, người bấm) / nhánh B (Playwright nick phụ)
  ├─ engager           : trả lời comment/inbox Page theo kịch bản, ghi nhận lead
  └─ analyst           : thu số liệu → chấm điểm bài/pillar/group/nhánh A-B → đề xuất sửa playbook
         ↑____________________ vòng lặp hằng tuần: Lead cập nhật playbook.md ______|

Dữ liệu: SQLite (posts, groups, accounts, metrics, leads) + thư mục content/ (markdown từng bài)
Lịch chạy: scheduled tasks (sáng lập kế hoạch ngày, tối thu số liệu, chủ nhật review tuần)
```

### Công việc anh phải tự làm (hệ thống không làm thay được)
1. Tạo Fanpage và Meta Developer App, lấy token (tôi sẽ viết hướng dẫn từng bước).
2. Đăng nhập Facebook trên trình duyệt một lần để lưu session (tôi không nhập mật khẩu hộ).
3. Chuẩn bị nick phụ cho Nhánh B, và chấp nhận rủi ro nick này bị khoá.
4. Cung cấp brief: danh mục dự án/sản phẩm, pháp lý của từng dự án, khu vực, tư cách hành nghề.

## 7. Bước tiếp theo đề xuất
1. Dựng khung: `.claude/agents/` (7 agent), skill `/lead`, schema SQLite, file `brief.md` và `playbook.md`.
2. Module Graph API cho Page (đăng, hẹn giờ, comment, insights) và hướng dẫn lấy token.
3. Module Group: nhánh A (Claude in Chrome), nhánh B (Playwright + selector tách riêng + giới hạn tần suất).
4. Chạy thử 1 tuần trên 1 Page và 3–5 group, sau đó review A/B.
