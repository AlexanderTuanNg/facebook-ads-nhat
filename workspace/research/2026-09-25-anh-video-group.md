# Kế hoạch ảnh/video cho 10 bài đăng group (Yên Thế Golden Hill) – task 6

Ngày làm: 2026-09-25 · Người làm: researcher · Ngày đọc mọi nguồn ngoài: **25/09/2026**
Phạm vi: chỉ đọc, không sửa file nào khác. Nhãn theo CLAUDE.md luật 9: **[DỮ LIỆU]** = số liệu/insight có trong file dự án · **[NGUỒN]** = tài liệu Meta đã đọc trực tiếp (trích nguyên văn) · **[GIẢ THUYẾT]** = suy luận/khuyến nghị chưa có nguồn xác nhận, cần test.

## Tóm tắt – dùng được ngay cho content (≤10 dòng)
1. **Bài 9 (KM3 – phố đêm) đang là bài nghẽn nhất về ảnh**: bắt buộc ảnh/video thật ghi ngày quay (checklist F10), nhưng tư liệu đang có (`flycam-dem-1x1-26s.mp4`, 3 ảnh tĩnh) cắt từ video QC cũ của môi giới, **chưa xác định được ngày quay** → chưa dùng được, KM3 vẫn KHOÁ. [DỮ LIỆU] `assets/dong-lac/media/README.md`; `workspace/STATE.md`.
2. Bài 1, 2 (giấy tờ pháp lý) **không được dùng ảnh AI** dù chỉ là đạo cụ chung, vì có hình giấy chứng nhận/hồ sơ – F12 cấm AI vẽ giấy tờ nhà đất. Phải là ảnh thật (che thông tin cá nhân).
3. Bài 7, 8 (KM4 chiết khấu, KM6 vay) là 2 bài **duy nhất được dùng ảnh AI minh hoạ** (đồ vật chung, không người/không chữ/không logo) – nhớ ghi chữ "Ảnh minh hoạ" trên ảnh và `images_meta: {ai: "<tên công cụ>"}`.
4. Meta khuyến nghị **4:5 (dọc) hoặc 1:1** cho ảnh/video trên Facebook Feed, và **9:16 (dọc)** cho Reels/Stories – trùng khớp với việc `tools/media.py card` đã mặc định xuất 1080×1350 (đúng tỉ lệ 4:5). [NGUỒN] Meta Business Help Center, đọc 25/09/2026.
5. Facebook Reels hiện **không còn ghi giới hạn số giây cố định** trên trang chính thức ("Reels can be any length or orientation") – không cần ép video xuống dưới 90 giây, nhưng nên cắt gọn vì thời gian xem trung bình chỉ 4–9 giây (G7). [NGUỒN]+[DỮ LIỆU].
6. Video tốt nhất hiện có – "Những người con Yên Thế" (`Ads Yên Thế.mov`) – có tỉ lệ tương tác cao gần gấp đôi các video khác (G1), và **có logo BlueSky** cần xác nhận quyền dùng trước khi đưa vào bài nào. [GIẢ THUYẾT] Ghi chú nội bộ có nhắc nghe thấy đoạn "Số vốn … 500tr" khoảng 1:00–1:07 (`workspace/STATE.md`, 25/09/2026) nhưng **chưa ai nghe/dịch lại để xác nhận** – phải nghe lại toàn bộ lời thoại trước khi cắt dùng; nếu đúng có số tiền thì mới vi phạm F1 và phải cắt bỏ.
7. Meta **có** tự gắn nhãn "AI info" cho ảnh/video AI dựa trên tín hiệu chuẩn ngành (C2PA/IPTC) hoặc do người đăng tự khai báo; với **nội dung tự nhiên (organic) có video/âm thanh giống ảnh thật (photorealistic)**, Meta "yêu cầu" (require) dùng công cụ tự khai báo và **có thể phạt** nếu không khai báo. [NGUỒN] about.fb.com, đọc 25/09/2026.
8. Nhiều trang thông số kỹ thuật khác của Meta Business Help Center (kích thước pixel tối thiểu, dung lượng file tối đa) **không truy cập được nội dung** trong phiên làm việc này (trang cần JavaScript/đăng nhập) – đã liệt kê rõ trong mục 2.3, không suy đoán số.
9. 4/10 bài (3, 4, 5, 10) cần ảnh **nơi có thật** ở Yên Thế nhưng chưa có tư liệu nào trong `assets/dong-lac/media/` khớp mô tả – cần đi quay/chụp mới.
10. File đầy đủ: `workspace/research/2026-09-25-anh-video-group.md` (đường dẫn dưới cùng).

---

## 1. Dữ liệu nội bộ: loại ảnh/video nào hiệu quả hay bị nghi ngờ

### 1.1 Từ phân tích quảng cáo môi giới (`workspace/research/ads-moi-gioi.md`)
- **[DỮ LIỆU] G1** (mục "1. Kết luận GIỮ", dòng G1): video gắn địa danh lịch sử Yên Thế (đền Hoàng Hoa Thám) đạt **5,61 tương tác/1.000 lượt xem – gần gấp đôi** mọi video khác (2,75–3,75). Mức tin "Cao (1 video, cần lặp lại để chắc)". → Ứng dụng: pillar `dia-phuong` nên ưu tiên video kể chuyện gắn địa danh thật hơn là ảnh tĩnh/đồ hoạ.
- **[DỮ LIỆU] G3**: có một nhóm khách **nghi ngờ dự án "ảo"** ("Rẻ vậy có thật không?", "Dự án có giấy phép chưa?"). → Ứng dụng trực tiếp cho việc chọn ảnh: ảnh/video càng "thật, có ngữ cảnh đời sống" càng phản bác được nghi ngờ này; ảnh dựng/phối cảnh đẹp quá dễ bị xem là "ảo".
- **[DỮ LIỆU] G7**: thời gian xem trung bình 4–9 giây, **3 giây đầu quyết định** người xem có dừng lại không. → Ứng dụng: cảnh mở đầu video (giây 0–3) phải có chủ thể rõ, sáng, không mờ/rung; không mở đầu bằng logo hay chữ giới thiệu dài.
- **[DỮ LIỆU] S1 (đã bị bác bỏ, không dùng làm căn cứ)**: không có bằng chứng "thêm chữ/hình cụ thể làm tăng view gấp 10 lần" – chênh lệch view chủ yếu do ngân sách quảng cáo, không phải do nội dung ảnh. → Nhắc mình: đừng suy diễn "ảnh X làm bài viral" chỉ từ 1–2 quan sát.

### 1.2 Từ rà tư liệu hiện có (`workspace/research/assets-review-2026-09-25.md`)
- **[DỮ LIỆU]** Video "Những người con Yên Thế" (`Ads Yên Thế.mov`, gốc 1440×2560) là **video tốt nhất/tương tác cao nhất hiện có** (nối với G1: đây chính là video có địa danh lịch sử). Vấn đề khi tái sử dụng: (a) có logo sàn BlueSky, **chưa xác nhận quyền dùng lại**; (b) đoạn "cảnh gia đình quây quần" chỉ là ảnh minh hoạ chung, **không phải cảnh quay tại dự án thật** – nếu dùng phải không để khách hiểu nhầm đó là hiện trạng dự án (đối chiếu A4: "không dùng ảnh làm sai lệch thực tế"). [GIẢ THUYẾT] `workspace/STATE.md` (mục việc làm 25/09/2026, dòng về `tools/media.py`) có ghi: "Video 'Những người con Yên Thế' chưa cắt: cần phụ đề/lời thoại để biết đoạn nào nói giá (có đoạn 'Số vốn … 500tr' ~1:00–1:07)" – đây là ghi chú **chưa xác nhận** (chính STATE.md cũng nói cần phụ đề/lời thoại mới biết chắc), không phải kết luận đã kiểm chứng; phải nghe lại toàn bộ video trước khi cắt dùng, nếu đúng có số tiền thì mới vi phạm F1.
- **[DỮ LIỆU]** 2 video QC khác của môi giới có **chữ giá đè lên hình** ("Chỉ với 1 TỶ 2", "vốn ban đầu hơn 500 triệu") → không dùng nguyên bản (F1); chỉ đoạn cắt buổi tối + flycam là dùng được **nếu xác định được ngày quay** – đây chính là nguồn gốc của `flycam-dem-1x1-26s.mp4` đang có.
- **[DỮ LIỆU]** Poster nhận diện thương hiệu: phần lớn ảnh là **ảnh dựng/AI** (hoa, dãy shophouse) + dùng từ cấm "đẹp nhất" → không dùng cho bài CĐT. Đây là ví dụ thực tế cho việc "ảnh dựng quá đẹp dễ bị khách soi là ảo" (khớp G3 ở trên).
- **[DỮ LIỆU]** Theo D6 (`workspace/compliance-checklist.md`): video/ảnh lấy lại của môi giới mà **không chỉnh sửa có ý nghĩa** có thể bị Meta coi là nội dung không nguyên bản và hạ phân phối → mọi footage cũ phải qua `tools/media.py clip/still` (cắt, đổi khung hình, bỏ chữ) trước khi dùng, không đăng nguyên file.

### 1.3 Từ chân dung 103 khách đã mua (`workspace/research/khach-da-mua.md`)
- **[DỮ LIỆU]** 88% khách đã kết hôn, vợ cùng quyết định (`khach-da-mua.md` mục "Hệ quả" điểm 4); người vợ cùng đứng tên/quyết định **23%** (`workspace/brief.md` §4) → ảnh/video nên có yếu tố gia đình, không chỉ nhắm hình ảnh "nhà đầu tư nam giới".
- **[DỮ LIỆU]** 76% khách thuộc Bắc Giang cũ (`khach-da-mua.md` mục "Mâu thuẫn quan trọng"), **62%** ở bán kính 20–25 km (`workspace/brief.md` §4), mua theo cụm làng/truyền miệng → ảnh "nơi quen thuộc" (đường làng, biển tên đường, hàng quán quen) có sức thuyết phục hơn ảnh phối cảnh đô thị hiện đại – khớp với image_prompt của bài 3 (biển tên đường, người dân qua lại).
- File này **không nói trực tiếp** về loại hình ảnh/video hiệu quả (chủ yếu là dữ liệu persona/vùng), nên phần liên hệ ở trên là **[GIẢ THUYẾT]** suy ra từ chân dung khách, chưa phải kết luận có sẵn trong file.

### 1.4 Tài sản media đã dựng (`assets/dong-lac/media/README.md`)
| File | Dùng cho bài nào (đối chiếu) | Trạng thái |
|---|---|---|
| `post2-5-giay-to-4x5.png` | Gần khớp bài 2 (A2) – nhưng là **ảnh chữ (card)**, khác với mô tả "ảnh chụp thật bìa hồ sơ" trong `image_prompt` của bài 2. Có thể dùng thay thế hoặc dùng song song (tài liệu gửi inbox). | Chờ compliance (task 5) |
| `checklist-phap-ly-dat-nen-4x5.png` | Tài liệu gửi khách inbox sau bài 1, không phải ảnh bìa của bài 1 | Chờ compliance (task 5) |
| `flycam-dem-1x1-26s.mp4` + 3 ảnh tĩnh `dem-cong-vien-*.jpg` | Gần khớp bài 9 (KM3 phố đêm) và một phần bài 4 (mặt bằng buổi tối) | **Chưa dùng được**: chưa rõ ngày quay (F10 bắt buộc ghi ngày), chưa chốt quyền dùng video gốc của môi giới |

→ Nhận xét chung: **chưa có tư liệu nào trong kho hiện tại khớp thẳng với image_prompt của bài 3, 4, 5, 6, 9, 10** (ảnh "nơi có thật" ở Yên Thế) – đây là phần cần đi quay/chụp mới, liệt kê ở mục 4.

---

## 2. Thông số chính thức của Meta

### 2.1 Phương pháp đọc nguồn (minh bạch, để người dùng biết mức tin cậy)
Nhiều trang `facebook.com/business/help/...` là trang React/JavaScript – công cụ đọc web trực tiếp chỉ thấy được **tiêu đề trang**, không thấy nội dung. Với các trang đó, đã thử đọc lại qua dịch vụ hiển-thị-văn-bản (vẫn là đọc đúng URL gốc của Meta, chỉ khác cách trích xuất chữ trên trang). Trang nào vẫn không ra nội dung (bị chặn đăng nhập) thì ghi rõ "không truy cập được" ở mục 2.3, **không điền số vào bảng**.

### 2.2 Bảng thông số đã xác minh trực tiếp từ Meta
| Vị trí đăng | Thông số | Trích nguyên văn / diễn giải | Nguồn |
|---|---|---|---|
| Facebook Feed – ảnh & video | Tỉ lệ khung hình được hỗ trợ: **1:1 và 4:5** | "Both 1:1 and 4:5 aspect ratios are supported" | [NGUỒN] Meta Business Help Center – "Best practices for aspect ratios across placements", `facebook.com/business/help/103816146375741`, đọc 25/09/2026 |
| Facebook Feed (ảnh đơn) | Khuyến nghị **4:5 (dọc)** cho Facebook Feed; **1:1 (vuông)** khuyến nghị riêng cho Instagram Feed | "4:5 (vertical) recommended for Facebook Feed; 1:1 (square) recommended for Instagram Feed" | như trên |
| Stories & Reels | Khuyến nghị **9:16 (dọc)** | "Most people hold their phones vertically so 9:16 is recommended to capture the whole screen" | như trên |
| Reels – định dạng file | Khuyến nghị **.mp4** | "Recommended format: .mp4" | [NGUỒN] "Requirements for Facebook Reels", `facebook.com/business/help/1197310377458196`, đọc 25/09/2026 |
| Reels – độ phân giải | Khuyến nghị **1080p** | "Recommended resolution: 1080p" | như trên |
| Reels – khung hình/giây | **24–60 FPS** | frame rate 24–60 FPS | như trên |
| Reels – codec video | H.264, H.265, VP9, AV1 (hỗ trợ) | liệt kê codec hỗ trợ | như trên |
| Reels – độ dài | **Không còn giới hạn số giây cố định trên trang chính thức** – "Reels can be any length or orientation" | trang không nêu số giây tối thiểu/tối đa cụ thể | như trên |
| Reels – âm thanh | Stereo, codec AAC-LC, tần số lấy mẫu 44,1kHz hoặc 48kHz, bitrate tối thiểu 128kbps | như liệt kê | như trên |
| Reels – HDR | HDR được khuyến khích; một số hiệu ứng sáng tạo (creative effects) có thể không tương thích đầy đủ với HDR | ghi chú trong trang | như trên |

**Ghi chú quan trọng:** các trang trên là trang chung của Meta Business Help Center, không tách riêng "quảng cáo" và "bài đăng thường" ở phần đã đọc được – hợp lý để áp dụng cho bài đăng group vì cùng là nội dung hiển thị trong Feed/Reels trên điện thoại. Việc `tools/media.py card` đang xuất mặc định **1080×1350** (đúng tỉ lệ 4:5) và `flycam-dem-1x1-26s.mp4` đang ở khung **1:1** – cả hai đều nằm trong 2 tỉ lệ Meta khuyến nghị cho Feed ở trên. [DỮ LIỆU] `tools/media.py` dòng 126; `assets/dong-lac/media/README.md`.

### 2.3 Số liệu CHƯA xác minh được (không suy đoán, chỉ liệt kê)
| Trang định đọc | Muốn tìm | Kết quả |
|---|---|---|
| "Recommended minimum image pixel requirements across placements" `facebook.com/business/help/469767027114079` | Số pixel tối thiểu cho ảnh Feed theo từng tỉ lệ | **Không truy cập được** (chỉ thấy tiêu đề trang / bị chuyển hướng sang trang đăng nhập) |
| "Choose the Right Size Image for Your Ad" `facebook.com/business/help/582165515184962` | Kích thước ảnh khuyến nghị cho quảng cáo | **Không truy cập được** nội dung đúng bài (trang trả về nội dung không khớp) |
| "Video length specifications across placements" `facebook.com/business/help/817989058548892` | Giới hạn giây video theo từng vị trí | **Không truy cập được** (chỉ thấy tiêu đề trang) |
| Meta Ads Guide – Feed video (outcome engagement) `facebook.com/business/ads-guide/update/video/facebook-feed/outcome-engagement` | Bảng thông số video quảng cáo Feed (dung lượng file, độ dài) | **Không truy cập được** (yêu cầu đăng nhập) |
| "About text overlays and the Safe Zone for ads in Stories and Reels" `facebook.com/business/help/980593475366490` | Vùng an toàn (safe zone) % trên/dưới/hai bên cho chữ trên Reels/Stories | **Không truy cập được** (yêu cầu đăng nhập) |

→ Vì vậy, **không đưa vào bảng 2.2** các số như "dung lượng file tối đa 4GB/30MB", "định dạng JPG/PNG", "độ phân giải tối thiểu 600px" dù các trang tổng hợp bên thứ ba (không phải Meta) có nhắc – các số này **chưa được xác minh trực tiếp từ Meta trong phiên làm việc này**, nên không dùng làm căn cứ ép buộc kỹ thuật, chỉ có thể dùng tham khảo với nhãn "chưa xác minh".

---

## 3. Nhãn nội dung AI của Meta ("AI info")

- **[NGUỒN]** Meta **tự động gắn nhãn** dựa trên "industry standard AI image indicators" (tín hiệu chuẩn ngành nhúng trong file ảnh/video, gồm chuẩn **C2PA** và **IPTC**) **hoặc** khi người đăng **tự khai báo** lúc tải nội dung lên. Nhãn hiện gọi chung là **"AI info"** (trước đó gọi "Made with AI"/"Imagined with AI"), Meta bắt đầu mở rộng phạm vi gắn nhãn từ tháng 5/2024. Nguồn: Meta Transparency Center – "Labeling AI Content", `transparency.meta.com/governance/tracking-impact/labeling-ai-content/`, đọc 25/09/2026.
- **[NGUỒN]** Với **nội dung tự nhiên (organic, không phải quảng cáo)**: "We'll require people to use this disclosure and label tool when they post organic content with a photorealistic video or realistic-sounding audio [that was digitally created or altered], … we may apply penalties if they fail to do so." → Dịch: Meta **bắt buộc** người đăng dùng công cụ tự khai báo khi đăng video **giống thật (photorealistic)** hoặc âm thanh giống thật do AI tạo/chỉnh sửa, và **có thể phạt** nếu không khai báo. Nguồn: Meta Newsroom (about.fb.com) – "Labeling AI-Generated Images on Facebook, Instagram and Threads", công bố gốc 06/02/2024, đọc 25/09/2026.
  - Lưu ý đọc đúng phạm vi: câu "require" ở trên nói rõ nhất về **video/âm thanh giống thật**; với **ảnh tĩnh**, cách Meta mô tả nghiêng về "tự phát hiện rồi tự gắn nhãn" (qua C2PA/IPTC hoặc mô hình riêng của Meta) hơn là một nghĩa vụ "require" tường minh như video – không nên khẳng định quá tay là ảnh tĩnh AI luôn bắt buộc tự khai báo, dù thực hành an toàn nhất vẫn là tự khai báo.
- **[NGUỒN]** Với quảng cáo (ads) về chủ đề xã hội/bầu cử/chính trị, Meta yêu cầu khai báo AI bắt buộc riêng theo chính sách quảng cáo – **không áp dụng cho bài group của dự án này** (đây là bài đăng thường bằng nick cá nhân, không phải quảng cáo trả tiền, không phải chủ đề chính trị). Nguồn: Meta Help Center, `meta.com/help/artificial-intelligence/355108217670024/`, đọc 25/09/2026.
- **Đối chiếu với `compliance-checklist.md` F12**: quy tắc nội bộ F12 (ghi rõ chữ "Ảnh minh hoạ" trên mọi ảnh AI, cấm giấy tờ/con dấu/logo ngân hàng/số tiền do AI vẽ, `images_meta` ghi nguồn `ai: <tên công cụ>`) đang **chặt hơn** mức tối thiểu Meta yêu cầu – đây là điều tốt, không cần nới lỏng.
- **[GIẢ THUYẾT – cần xem giao diện thật trước khi hướng dẫn thao tác]**: nick cá nhân khi đăng ảnh AI ở Group **có thể** nhìn thấy tuỳ chọn "gắn nhãn AI info" ngay trong khung soạn bài (Meta nói chính sách áp dụng cho "organic content" nói chung, không riêng Trang doanh nghiệp) — nhưng phiên làm việc này **chưa xem màn hình đăng bài thật** nên không khẳng định giao diện cụ thể ra sao. Theo CLAUDE.md luật 9 ("hướng dẫn thao tác giao diện phải xem màn hình thật trước"), việc này cần người dùng/Lead kiểm tra trực tiếp khi đăng bài 7 hoặc 8, rồi bật tuỳ chọn đó nếu có.

---

## 4. Danh sách cảnh cần quay/chụp theo từng bài (1–10)

Chú thích loại ảnh: **THẬT** = bắt buộc ảnh/video chụp thật, không AI · **AI OK** = được dùng ảnh AI minh hoạ (F12) · **CHỮ** = ảnh dạng chữ/card do `tools/media.py card` dựng · **CHƯA CẦN** = bài đang dùng chữ, chưa bắt buộc có ảnh.

| Bài | File / nhóm đăng | Loại ảnh | Cảnh cần quay/chụp (rút gọn từ `image_prompt`) | Lưu ý tuân thủ |
|---|---|---|---|---|
| 1 | `20260926-g1-a1-dau-hieu-kho-sang-ten.md` – Nhà đất Cụm Yên Thế | **THẬT** (không AI dù là đạo cụ chung) | Góc trên xuống: bàn gỗ, bản photo giấy chứng nhận đã che kín thông tin, bút, checklist viết tay 3 gạch đầu dòng; ánh sáng tự nhiên | F12 cấm AI vẽ giấy tờ nhà đất → phải dùng đạo cụ thật (giấy tờ mẫu/che tên), không tạo bằng AI dù nội dung chỉ minh hoạ chung |
| 2 | `20260926-g3-a2-5-giay-to-truoc-khi-ky.md` – MUA BÁN NHÀ ĐẤT YÊN THẾ BẮC GIANG | **THẬT** (không AI) | Bìa hồ sơ xanh mở, 5 tờ giấy so le đánh số 1–5 bằng giấy nhớ vàng, che thông tin cá nhân, nền bàn sáng | Cùng lý do bài 1. Đã có phương án thay thế bằng ảnh chữ `post2-5-giay-to-4x5.png` (mục 1.4) – cần Lead/người dùng chọn 1 trong 2 hướng, không phải quyết định của nghiên cứu này |
| 3 | `20260926-g4-a3-yen-the-thanh-pho-bac-ninh.md` – Nhà Đất Yên Thế- Bắc Ninh(BG) | **THẬT** (nơi có thật) | Con đường quen thuộc trung tâm Yên Thế buổi sáng, biển tên đường/biển cơ quan rõ chữ, người dân qua lại; không chèn chữ/logo | F12 cấm AI cho "nơi có thật ở Yên Thế… như thể ảnh chụp". Nên chọn địa điểm gần với nơi 76% khách đã mua sinh sống (Bắc Giang cũ) để hình ảnh gần gũi (mục 1.3) |
| 4 | `20260927-g2-a4-mat-bang-buoi-toi.md` – Chợ Yên Thế - Bắc Giang | **THẬT**, khuyến nghị áp chuẩn F10 | Dãy hàng quán trung tâm Yên Thế 19h–20h, đèn sáng, người mua bán; ghi ngày quay vào `images_meta` | Bài không gắn KM3 chính thức (key_messages rỗng) nhưng nội dung/ảnh thực chất là thông điệp "buổi tối sầm uất" → [GIẢ THUYẾT] nên áp cùng chuẩn F10 (ảnh thật + ghi ngày) để nhất quán, tránh bị compliance/Meta xem là gây hiểu lầm |
| 5 | `20260927-g5-a5-manh-dat-dung-lam-gi.md` – Yên Thế Online | **THẬT** (nơi có thật) | Khoảng đất trống đã san phẳng gần khu dân cư, trời xanh, vài nếp nhà phía xa; không cắm biển bán, không chèn chữ | Không bắt buộc ghi ngày theo checklist, nhưng [GIẢ THUYẾT/khuyến nghị thực hành tốt] vẫn nên ghi ngày chụp vào `images_meta` để truy vết nếu bị hỏi |
| 6 | `20260929-g1-b1-km2-quy-mo.md` – Nhà đất Cụm Yên Thế - Bắc Ninh (KM2) | **CHƯA CẦN** ảnh (sổ cái: KM2 chỉ nói bằng chữ → MỞ) | Khi có ảnh: flycam thật ban ngày toàn khu, thấy đường nội khu/cột điện/cống, ghi ngày bay | Không được dùng ảnh flycam AI cho khu đất thật (F12). [GIẢ THUYẾT/gợi ý, không phải quyết định]: có thể dùng ảnh chữ (card, kiểu bài 1/2) để trình bày "12,1 ha – 377 lô" ngay mà không cần chờ bay flycam |
| 7 | `20260929-g3-b2-km4-truc-tiep-cdt.md` – MUA BÁN NHÀ ĐẤT YÊN THẾ BẮC GIANG (KM4) | **AI OK** | Bàn tiếp khách gọn gàng, tách trà, bút, bìa hồ sơ đóng kín; KHÔNG giấy tờ/chữ/số/logo/người | Ghi chữ "Ảnh minh hoạ" trên ảnh + `images_meta: {ai: "<tên công cụ>"}` (F12). Cân nhắc bật tuỳ chọn tự khai báo AI của Facebook nếu giao diện có (mục 3, cần xem màn hình thật) |
| 8 | `20260929-g4-b3-km6-vay-50.md` – Nhà Đất Yên Thế- Bắc Ninh(BG) (KM6) | **AI OK** | Đôi bàn tay cầm bút cạnh sổ tay đóng + chùm chìa khoá, tông ấm; KHÔNG máy tính bỏ túi/màn hình số, không chữ/số tiền/logo ngân hàng | Cùng lưu ý bài 7 |
| 9 | `20260930-g2-b4-km3-pho-dem.md` – Chợ Yên Thế - Bắc Giang (KM3) | **THẬT, bắt buộc ghi ngày (F10)** | Tuyến phố quanh dự án 19h–21h: hàng quán sáng đèn, người đi lại, xe máy đỗ trước cửa hàng | **Bài nghẽn nhất** (mục tóm tắt #1): KM3 đang KHOÁ vì chưa có ảnh/video ghi rõ ngày quay. Tư liệu `flycam-dem-1x1-26s.mp4` chưa dùng được cho tới khi xác nhận ngày quay |
| 10 | `20260930-g5-b5-km1-gia-mem.md` – Yên Thế Online (KM1) | **THẬT** (nơi có thật) | Khu dân cư chiều muộn: đường nội khu đã trải nhựa, vỉa hè, vài nhà đang xây; không chèn chữ giá, không logo | KM1 đang MỞ, không bắt buộc tư liệu đặc biệt, nhưng ảnh vẫn phải là nơi thật (F12), không dùng AI vì đây là "khu đất/khu dân cư có thật" |

### Mẹo quay bằng điện thoại cho người mới
1. **Quay/chụp theo chiều dọc** khi định đăng dạng Reels/Story, hoặc theo tỉ lệ 4:5/1:1 khi định đăng ảnh Feed – khớp khuyến nghị chính thức của Meta (mục 2.2). [NGUỒN]
2. Quay thành **nhiều đoạn ngắn 5–15 giây** thay vì 1 đoạn dài liên tục, để dễ dùng `tools/media.py clip --segments` cắt bỏ đoạn lỡ nói giá/chữ nhạy cảm mà không phải quay lại từ đầu. [GIẢ THUYẾT – dựa theo cách công cụ nội bộ hoạt động, chưa có nguồn ngoài]
3. Giữ máy **ổn định và đủ sáng ngay từ giây đầu tiên** – vì thời gian xem trung bình chỉ 4–9 giây và 3 giây đầu quyết định (G7). [DỮ LIỆU nội bộ]
4. **Không tự chèn chữ/logo/khung viền** lúc quay/chụp – để chữ do `tools/media.py card`/`clip` chèn sau, tránh lọt chữ giá hoặc thông tin sai vào ảnh gốc (đối chiếu F1, F12, và nguyên tắc trong README media). [DỮ LIỆU nội bộ]
5. **Ghi lại ngày giờ quay ngay lúc quay** (chụp thêm 1 tấm có lịch/đồng hồ, hoặc ghi chú riêng gửi kèm) để điền được `images_meta` – bắt buộc với mọi cảnh "buổi tối sầm uất" (F10; áp dụng cho bài 9, khuyến nghị cho bài 4). [DỮ LIỆU nội bộ – theo checklist]
6. Tránh để lọt **biển số xe, mặt người rõ nét chưa xin phép, hoặc giấy tờ thật chưa che** vào khung hình. [GIẢ THUYẾT – thực hành chung về quyền riêng tư, không có nguồn trích dẫn cụ thể trong tài liệu dự án]
7. Chụp/quay ở **độ phân giải gốc cao nhất của máy**, tránh gửi qua nhiều lượt Zalo/Messenger (bị nén) trước khi đưa vào `tools/media.py` xử lý – Meta khuyến nghị ảnh chất lượng cao cho hiển thị tốt, dù số pixel tối thiểu cụ thể chưa xác minh được (mục 2.3). [NGUỒN một phần + GIẢ THUYẾT về mức độ nén]

---

## 5. Gợi ý góc nội dung liên quan (bonus, gắn pillar)
1. **[dia-phuong]** Video ngắn kể chuyện tại một địa danh lịch sử/quen thuộc khác ở Yên Thế (không phải đền Hoàng Hoa Thám để tránh trùng lặp) – test giả thuyết GT-A trong `ads-moi-gioi.md` (bài lịch sử/văn hoá có tương tác cao hơn bài kiến thức thuần).
2. **[kien-thuc]** Loạt ảnh "before – sau khi che thông tin" cho checklist giấy tờ (bài 1, 2) – tăng cảm giác "thật, có nghiệp vụ" thay vì ảnh minh hoạ chung chung.
3. **[tuong-tac]** Dùng chính câu trả lời comment thật của bài 4, 5 (khi có) làm chất liệu cho ảnh chữ (card) ở bài sau – vừa có dữ liệu thật, vừa không cần đi quay thêm.
4. **[du-an]** Khi có ảnh flycam thật cho KM2 (bài 6), tách thành 2 bản: 1 ảnh full cảnh, 1 ảnh chữ (card) chú thích "12,1 ha – 377 lô" để dùng lại cho các bài sau mà không cần bay flycam mỗi lần.
5. **[du-an]** Sau khi xác nhận được ngày quay cho đoạn phố đêm, cân nhắc dựng thêm 1 bản Reels dọc 9:16 (không chỉ bản 1:1 hiện có) vì Meta khuyến nghị 9:16 cho Reels/Stories (mục 2.2) – tận dụng đúng không gian màn hình di động.

---

## Nguồn đã đọc (đọc ngày 25/09/2026, trừ khi ghi khác)

**Nguồn ngoài – Meta (đọc trực tiếp hoặc qua công cụ hiển thị văn bản, cùng 1 URL gốc):**
- Meta Business Help Center – Best practices for aspect ratios across placements: https://www.facebook.com/business/help/103816146375741
- Meta Business Help Center – Requirements for Facebook Reels: https://www.facebook.com/business/help/1197310377458196
- Meta Transparency Center – Labeling AI Content: https://transparency.meta.com/governance/tracking-impact/labeling-ai-content/
- Meta Newsroom (about.fb.com) – Labeling AI-Generated Images on Facebook, Instagram and Threads (công bố gốc 06/02/2024): https://about.fb.com/news/2024/02/labeling-ai-generated-images-on-facebook-instagram-and-threads/
- Meta Help Center – How AI-generated images in ads are identified and labeled on Meta: https://www.meta.com/help/artificial-intelligence/355108217670024/

**Nguồn ngoài – đã thử nhưng không truy cập được nội dung (liệt kê ở mục 2.3, không dùng số liệu):**
- https://www.facebook.com/business/help/469767027114079
- https://www.facebook.com/business/help/582165515184962
- https://www.facebook.com/business/help/817989058548892
- https://www.facebook.com/business/ads-guide/update/video/facebook-feed/outcome-engagement
- https://www.facebook.com/business/help/980593475366490
- https://transparency.meta.com/policies/other-policies/meta-AI-disclosures

**Nguồn nội bộ (file:mục):**
- `workspace/research/ads-moi-gioi.md` (mục 1: G1, G3, G7; mục 2: S1)
- `workspace/research/assets-review-2026-09-25.md` (mục Video; mục Ảnh nhận diện; mục Mâu thuẫn M1–M4)
- `workspace/research/khach-da-mua.md` (mục "Vì sao nguồn này đáng tin nhất"; mục "Mâu thuẫn quan trọng"; mục "Hệ quả" điểm 2, 4)
- `workspace/STATE.md` (mục việc làm 25/09/2026, dòng về `tools/media.py`/video "Những người con Yên Thế" – ghi chú chưa xác nhận)
- `assets/dong-lac/media/README.md` (toàn bộ)
- `workspace/compliance-checklist.md` (F10, F12, D5, D6, A4)
- `workspace/brief.md` (§4 persona)
- `tools/media.py` (dòng 1–9 mô tả lệnh; dòng 126 mặc định `--size 1080x1350`)
- `content/2026-09-26/*.md`, `content/2026-09-27/*.md`, `content/2026-09-29/*.md`, `content/2026-09-30/*.md` (frontmatter `image_prompt`, `key_messages`, `sources` của bài 1–10)
