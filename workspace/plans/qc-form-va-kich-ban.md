# FORM, KỊCH BẢN QUAY, KỊCH BẢN GỌI LẠI — quảng cáo đợt 1 (bản nháp 15/10/2026)

Căn cứ: skill `quang-cao-bds` §3–4, `workspace/reports/2026-10-15-phuong-an-tong-the-quang-cao.md` §6–7, `workspace/compliance-checklist.md` §H. Chữ trong ngoặc vuông `[ĐIỀN …]` là chỗ người dùng phải điền (lint tự chặn nếu lọt vào quảng cáo).

---

## 1. Form tức thì (Instant form) — loại **Higher intent**
**Tên form (nội bộ):** `FORM-1 | xem-dat | 2026-10`
**Phần giới thiệu**
- Tiêu đề: **Nhận mặt bằng & lịch xem đất**
- Mô tả: Để lại số, em gọi lại trong ít phút để gửi mặt bằng, giải đáp giấy tờ và hẹn lịch xem đất trực tiếp tại khu.

**Câu hỏi** (trắc nghiệm, theo thứ tự dễ → khó):
1. *Anh/chị đang sống ở đâu?* — TP Bắc Giang (cũ) · Yên Thế · Tân Yên · Lạng Giang · Lục Nam · Lục Ngạn · Việt Yên · Hiệp Hoà · Yên Dũng · Sơn Động · Bắc Ninh (cũ) · Hà Nội · Đang làm xa quê · Nơi khác
2. *Anh/chị tìm đất để:* Để ở · Mua cho con · Giữ tài sản · Kinh doanh nhỏ
3. *Anh/chị định mua khi nào?* Trong 1 tháng · 1–3 tháng · 3–6 tháng · Đang tham khảo
4. *Em liên hệ anh/chị qua cách nào cho tiện ạ?* Gọi điện buổi sáng · Gọi điện buổi trưa · Gọi điện buổi tối · Nhắn Zalo
- Thông tin tự điền sẵn: Họ tên, Số điện thoại. **Bật xác thực SĐT bằng mã OTP** (kiểm trên giao diện xem tài khoản VN có bật được không).
- Không hỏi: CCCD, thu nhập, địa chỉ chi tiết.

**Ô đồng ý bắt buộc (custom disclaimer)**
> ☐ Tôi đồng ý để Công ty CP Đầu tư và Phát triển Thắng Anh (Chủ đầu tư KDC Đồng Lạc) dùng họ tên, số điện thoại tôi cung cấp để liên hệ tư vấn về dự án qua điện thoại/Zalo. Tôi có thể yêu cầu ngừng liên hệ bất cứ lúc nào.

**Chính sách bảo mật:** `[ĐIỀN: link trang chính sách bảo mật trên website CĐT]`

**Màn hình cảm ơn**
- Tiêu đề: Cảm ơn anh/chị!
- Nội dung: Em sẽ gọi lại trong ít phút (7:00–21:00). Đăng ký ngoài giờ thì em gọi ngay đầu giờ sáng hôm sau ạ.
- Nút: **Gọi ngay 0965 539 599** (hoặc mở Zalo).

## 2. Google Sheet nối CAPI — quy ước cho đội KD
- Nối theo hướng dẫn Meta: Meta Business Suite → Tất cả công cụ → Biểu mẫu tức thì → **+ Kết nối CRM** → Google Sheets → chọn bảng tính **trống** → chọn form `FORM-1`. ([Meta](https://www.facebook.com/business/help/1095577538573756))
- Cột **`lead_status`** (Meta tạo) — chỉ chọn 1 trong 5 giá trị, **giữ đúng chữ tiếng Anh**:

| Giá trị | Khi nào |
|---|---|
| `Intake` | Mới về / chưa nói chuyện được |
| `Qualified` | Nghe máy **và** đúng vùng (hoặc sẵn sàng về) **và** mua trong 6 tháng **và** đồng ý đi xem đất |
| `Converted` | Đã đến xem đất / đến Đêm hội |
| `Not qualified` | Sai nhu cầu (chỉ tìm thuê, ngân sách quá xa, môi giới dò giá, số rác) |
| `Lost` | 3 lần gọi không nghe / khách từ chối |

- Cột thêm **bên phải** (đội KD tự thêm): `nghe_may` (có/không) · `goi_lai_phut` (số phút từ lúc lead vào tới cuộc gọi đầu) · `coc` (có) · `ghi_chu`. [GIẢ THUYẾT] Meta không ghi đè cột thêm bên phải — kiểm ngay sau khi nối bằng 1 lead thử.
- **Không** xoá dòng, **không** sửa cột Meta tạo (id, created_time, ad_name…). Cập nhật `lead_status` **mỗi ngày** (Meta cần ≥ 60% lead có trạng thái).
- Thứ Hai: tải bảng tính dạng CSV + xuất báo cáo cấp "Quảng cáo" trong Ads Manager → gửi Claude chạy `python tools/doc_ads.py`.

## 3. Đặt tên quảng cáo trong Ads Manager (bắt buộc để đọc số)
`<mã>-<số bản> | <góc>` — ví dụ `QC-A1 | so-da-trao`, `QC-C1 | di-mot-vong`. Chiến dịch: `META_Lead_BacGiangCu_Dot1_2026-10`. Nhóm quảng cáo: `BanKinh+XaHuyen_BacGiangCu`.

## 4. Kịch bản quay (điện thoại, quay dọc 9:16, có phụ đề, 15–30 giây)
**Luật chung:** người thật phải ký **giấy đồng ý dùng hình ảnh** (mục 6) trước khi đưa vào quảng cáo; không quay biển số xe, giấy tờ có số; câu nói tự nhiên, không đọc thuộc lòng; không nói giá cụ thể, không "nhất", không hứa tăng giá.

| Mã | Cảnh (giây) | Lời / chữ trên hình |
|---|---|---|
| **QC-A** Sổ đã trao | 0–3: cận tay khách cầm sổ, mặt cười · 3–12: khách nói 1–2 câu thật ("Nhà em mua lô ở đây, hôm 9/10 vừa nhận sổ") · 12–22: cảnh lễ trao sổ, đường nhựa trong khu · 22–30: chữ "Để lại số – em gửi mặt bằng & lịch xem đất" | Phụ đề đúng lời khách. Chữ mở: **"Mua đất xong bao lâu thì có sổ?"** |
| **QC-B** Cha mẹ – con | 0–3: bố/mẹ đứng trên lô đất nhìn quanh · 3–15: kể ngắn vì sao mua cho con ("con đi làm xa, bố mẹ giữ mảnh đất gần nhà cho con") · 15–25: cảnh khu, trường/chợ gần (nếu có thật) · 25–30: CTA | Chữ mở: **"Lo cho con một mảnh đất gần nhà"** |
| **QC-C** Đi một vòng | 0–3: người dẫn cầm máy ở cổng: "Đi cùng em một vòng nhé" · 3–25: đi bộ: đường nhựa → đèn → quảng trường → một lô trống · 25–30: CTA | Chữ: "Đường xong · Đèn xong · Sổ đã trao" |
| **QC-D** Đi làm xa | 0–3: chữ lớn "Đi làm KCN mấy năm, về quê vẫn chưa có đất?" trên cảnh khu · 3–20: cảnh khu + ảnh trao sổ · 20–30: CTA | Không nhắc tên dự án/khu khác |

## 5. Kịch bản gọi lại trong 5 phút
1. **Chào (≤ 15 giây):** "Dạ em chào anh/chị, em là [tên] bên Chủ đầu tư khu dân cư Đồng Lạc ở Yên Thế. Anh/chị vừa để lại số trên Facebook để nhận mặt bằng và lịch xem đất phải không ạ?"
2. **Hỏi lọc** (đúng định nghĩa `Qualified`):
   - "Hiện anh/chị đang ở khu vực nào ạ?" (đã có trong form → xác nhận lại)
   - "Mình tìm đất để ở, cho con hay giữ tài sản ạ?"
   - "Anh/chị định khoảng bao giờ thì xuống tiền ạ?"
   - "Cuối tuần này hoặc tối 07/11 anh/chị có tiện về xem đất trực tiếp không ạ?" (chỉ mời 07/11 khi KM9 đã MỞ)
3. **Gửi Zalo ngay sau cuộc gọi:** mặt bằng, ảnh trao sổ, vị trí bản đồ. Giá từng lô gửi riêng theo bảng giá hiện hành của CĐT.
4. **Ghi Sheet ngay:** `lead_status`, `nghe_may`, `goi_lai_phut`.
5. Không nghe → gọi lại sau 2 giờ và tối cùng ngày → lần 3 không nghe = `Lost`.
6. **Không được:** hứa tăng giá, nói "lô cuối cùng", ép cọc, nói xấu dự án khác. Câu hỏi khó (pháp lý, vay) → theo `workspace/kich-ban-nhan-tin-lead.md` §B.

## 6. Mẫu giấy đồng ý dùng hình ảnh (bản nháp — cần pháp chế/luật sư xem)
> Tôi tên: ……………… · SĐT: ……………… đồng ý để Công ty CP Đầu tư và Phát triển Thắng Anh sử dụng hình ảnh, video, lời nói của tôi được quay ngày …/…/2026 tại KDC Đồng Lạc trong bài đăng và quảng cáo về dự án trên Facebook, Zalo, website của Công ty, thời hạn 12 tháng. Tôi có thể rút lại đồng ý bằng cách báo cho Công ty; Công ty gỡ nội dung trong 7 ngày làm việc kể từ khi nhận yêu cầu. Ký tên: ………

## 7. Việc người dùng làm trước khi bật QC (Giai đoạn chuẩn bị, mục tiêu xong ~19/10)
1. Fanpage CĐT + tài khoản quảng cáo doanh nghiệp; người quản trị là tài khoản thật.
2. Website CĐT: đăng thông tin dự án theo Luật KDBĐS Điều 6 + trang chính sách bảo mật → cập nhật bảng "Điều kiện chạy" ở checklist §H.
3. Số hiệu + ngày văn bản Sở Xây dựng (dòng PL).
4. Google Sheet trống → nối CAPI (Claude hướng dẫn từng màn hình khi anh/chị mở).
5. Người trực 7:00–21:00 + cài app Meta Business Suite bật thông báo lead.
6. Quay QC-A, QC-C, QC-D (+ QC-B nếu có gia đình đồng ý) + ký giấy đồng ý.
7. Chốt ngân sách tuần + trần chi phí QC cho 1 lô bán được.
