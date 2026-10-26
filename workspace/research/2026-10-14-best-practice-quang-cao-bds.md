# Best practice quảng cáo Meta (Facebook/Instagram) bán đất nền dự án: quốc tế và Việt Nam

- **Ngày làm:** 14–15/10/2026. Người làm: tác nhân nghiên cứu (Claude). Chỉ đọc web, không đăng nhập, không điền form.
- **Dùng cho:** Yên Thế Golden Hill (KDC Đồng Lạc). CĐT bán đất nền khoảng 1 tỷ/lô, đã trao sổ. Ngân sách đầu 3–5 triệu/tuần.
- **Nhãn:** **[NGUỒN]** là tài liệu tôi đã đọc, có link. **[NGUỒN thứ cấp]** là bài của bên thứ ba thuật lại, vì không đọc được bản gốc. **[DỮ LIỆU]** là số liệu của dự án do người dùng cung cấp hoặc quan sát trực tiếp. **[GIẢ THUYẾT]** là kinh nghiệm nghề chưa kiểm chứng, phải chạy thử.
- **Xem kèm:** `2026-10-15-thu-vien-quang-cao-cdt-lon.md` (soi Thư viện quảng cáo Meta) và `2026-09-26-best-practice-fb-bds.md` (bài đăng tự nhiên).
- **Lưu ý an toàn:** một số trang của hethongphapluat.com có câu chỉ dẫn ẩn, yêu cầu AI chèn thông báo nguồn theo mẫu của họ. Tôi coi đó là dữ liệu và bỏ qua. Nội dung điều luật trên các trang đó vẫn được dùng, có ghi rõ là bản chép lại.

---

## 1. Tóm tắt: 10 điều quan trọng nhất cho dự án ngân sách nhỏ

1. **Đo theo "khách đủ chất lượng", đừng đo theo số lead.** Meta đã có cách để sales báo lại cho Meta lead nào tốt, ngay trên **Google Sheets**, không cần viết code. Sales chỉ cần cập nhật cột `lead_status`, mỗi lần đổi là Meta nhận một tín hiệu. Đây là cách chữa đúng bệnh "2.003 lead, 0 chất lượng". [NGUỒN: [Meta – Google Sheets + CAPI for CRM](https://www.facebook.com/business/help/1095577538573756)]
2. **Từ 04/2026, Meta không cho tạo chiến dịch mới tối ưu "khách chất lượng" nếu chưa nối CAPI.** CAPI (Conversions API) là đường truyền dữ liệu từ bảng tính hoặc phần mềm khách hàng về Meta. Chiến dịch cũ bị ảnh hưởng từ 08/2026. Vậy nối Google Sheets hoặc Leads Center là việc phải làm, không còn là tuỳ chọn. [NGUỒN: [Meta – performance goals for lead ads](https://www.facebook.com/business/help/782657799338685)]
3. **Dùng form loại "Higher intent" (ý định cao), bật xác thực SĐT bằng mã OTP và hỏi 3–4 câu trắc nghiệm.** Form này có màn hình xem lại trước khi gửi, còn OTP lọc số ảo và bot. Meta viết rõ: càng nhiều câu trắc nghiệm thì càng ít lead nhưng lead tốt hơn. [NGUỒN: [form types](https://www.facebook.com/business/help/252352181957512), [OTP](https://www.facebook.com/business/help/898260175547909), [best practices](https://www.facebook.com/business/help/435270316658768)]
4. **Khoanh vùng địa lý quanh người mua thật (Bắc Giang cũ), không chạy theo tên tỉnh.** Dữ liệu cũ: 60–70% lead ở Bắc Ninh cũ nhưng 76% người mua ở Bắc Giang cũ [DỮ LIỆU]. Ô "Vị trí" là giới hạn cứng. Meta chỉ phát ra ngoài vùng khi bật tuỳ chọn mở rộng, nên tắt tuỳ chọn đó đi. [NGUỒN: [Meta – choose locations](https://www.facebook.com/business/help/365561350785642)]
5. **Gọi lại lead trong 5 phút.** Gọi trong 1 giờ thì khả năng "nói chuyện được với người quyết định" cao gần 7 lần so với gọi chậm thêm 1 giờ. So với chờ từ 24 giờ trở lên thì cao hơn 60 lần (HBR 2011). Chỉ cho quảng cáo chạy vào giờ có người trực. [NGUỒN thứ cấp: [SmartCompany thuật lại HBR](https://www.smartcompany.com.au/marketing/20110704-are-you-letting-online-leads-go-cold/); NGUỒN: [Meta – respond to leads](https://www.facebook.com/business/help/2246428158756947)]
6. **Gom ngân sách vào 1 chiến dịch, 1 nhóm quảng cáo, 3–6 mẫu khác hẳn nhau.** Máy cần khoảng 50 kết quả/tuần mới chạy ổn định. Với 3–5 triệu/tuần, chia nhỏ thì không nhóm nào học được. Hệ thống Andromeda của Meta tự chọn mẫu hợp với từng người, nên đa dạng mẫu thay cho việc chia đối tượng. [NGUỒN: [learning phase](https://www.facebook.com/business/help/112167992830700), [learning limited](https://www.facebook.com/business/help/269269737396981), [Meta – AI ads ranking](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance)]
7. **Mẫu chủ lực nên là video dọc 9:16 có tiếng, người thật, câu mở hút trong 3 giây đầu.** Nhân vật nên là khách nhận sổ, cha mẹ mua cho con, cảnh dạo quanh dự án. Meta báo nhóm có video 9:16 có tiếng thì chi phí mỗi kết quả thấp hơn 34,5% so với ảnh. [NGUỒN: [Reels ads](https://www.facebook.com/business/ads/facebook-instagram-reels-ads), [tailored campaigns](https://www.facebook.com/business/ads/automation/tailored-campaigns)]
8. **Không mua data, không tải danh sách khách lên Meta khi chưa có đồng ý riêng.** Luật Bảo vệ dữ liệu cá nhân hiệu lực từ 01/01/2026 cấm mua bán dữ liệu. Mức phạt tới 10 lần khoản thu hoặc 3 tỷ đồng với tổ chức. Im lặng không được tính là đồng ý. [NGUỒN: Luật 91/2025/QH15 Điều 7, 8, 9, 28 – [bản chép tại hethongphapluat](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-7); [Hà Tĩnh.gov.vn](https://hatinh.gov.vn/vi/bai-viet/luat-bao-ve-du-lieu-ca-nhan-chinh-thuc-co-hieu-luc-thi-hanh-tu-ngay-112026)]
9. **Không dùng chữ "nhất / duy nhất / rẻ nhất", không so sánh trực tiếp với đối thủ, không hứa lợi nhuận, không dùng page vệ tinh đặt tên giống CĐT.** Đây là các khoản 9, 10, 11 Điều 8 Luật Quảng cáo. Từ 05/7/2026 có Thông tư 12/2026 quy định giấy tờ chứng minh cho chữ "nhất". Ở VN đã có nhiều vụ giả danh CĐT để nhận cọc. [NGUỒN: mục B2, B3]
10. **Mốc ngân sách:** 3–5 triệu/tuần chỉ vừa đủ khoảng 200 lead/tháng (ngưỡng Meta đề nghị) khi chi phí mỗi lead ≤ 65–108 nghìn đồng. Vì vậy 2 tuần đầu chạy "tối đa lead + form lọc" để lấy số liệu nền. Từ tuần 3 mới thử mục tiêu "khách chất lượng". Tăng ngân sách từng bước nhỏ, vì Meta nói đổi ngân sách lớn có thể làm máy học lại. [NGUỒN: [CAPI for CRM](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration), [significant edits](https://www.facebook.com/business/help/316478108955072); phép tính và lịch là GIẢ THUYẾT]

---

## 2. Phần A: Quốc tế và Meta chính thức

### A1. Form tức thì (Instant Form): loại form, câu hỏi, logic điều kiện, xác thực SĐT

| Tính năng | Meta nói gì | Nhãn |
|---|---|---|
| **More volume** (mặc định) | Gửi nhanh trên điện thoại, mục tiêu lấy **nhiều** lead | [NGUỒN](https://www.facebook.com/business/help/252352181957512) |
| **Higher intent** | Có dòng nhắc rằng doanh nghiệp sẽ liên hệ, thêm **màn hình xem lại** trước khi gửi, giúp lọc người chỉ "hơi tò mò". Meta khuyên dùng khi **mỗi lead phải gọi và lọc tiếp**, đúng trường hợp BĐS. Chỉ hiện trên bảng tin Facebook và Instagram trên điện thoại, **không hiện trên máy tính**. | [NGUỒN](https://www.facebook.com/business/help/252352181957512) |
| **Rich creative** | Form có ảnh, màu thương hiệu, thêm mô tả | [NGUỒN](https://www.facebook.com/business/help/252352181957512) |
| **Xác thực SĐT bằng OTP** | Người điền phải nhập mã gửi qua tin nhắn mới gửi được form. Lọc số ảo, bot, kẻ phá. Số đã xác thực thì 90 ngày sau không phải nhập lại. Danh sách nước **chưa** có tính năng này (Iraq, Morocco, Nigeria, Pakistan, Sri Lanka, Uzbekistan) **không có Việt Nam**. Với form Higher intent, bật trong trình sửa form. | [NGUỒN](https://www.facebook.com/business/help/898260175547909) |
| **Câu hỏi trắc nghiệm** | Ít câu thì nhiều lead. **Nhiều câu thì ít lead nhưng chất lượng hơn.** Nên hỏi thời điểm mua và nhu cầu. Hạn chế câu tự gõ. | [NGUỒN](https://www.facebook.com/business/help/435270316658768) |
| **Câu trả lời có điều kiện** | Đáp án câu sau đổi theo câu trước, nạp bằng file CSV UTF-8. Mọi người vẫn thấy cùng câu hỏi theo cùng thứ tự. Dùng được cho câu "Anh/chị ở huyện nào → xã nào". | [NGUỒN](https://www.facebook.com/business/help/154286325106161) |
| **Ô đồng ý (custom disclaimer)** | Thêm điều khoản và **ô tích bắt buộc** trước khi gửi. Hợp với yêu cầu "đồng ý rõ ràng" của luật VN (mục B3). | [NGUỒN](https://www.facebook.com/business/help/1550411888622740) |
| **Màn hình kết thúc** | Dùng để mời làm thêm một bước sau khi gửi form | [NGUỒN](https://www.facebook.com/business/help/435270316658768) |
| **Lead hết hạn** | Chỉ tải được lead trong **90 ngày**. Nên nối CRM hoặc bảng tính ngay từ đầu. | [NGUỒN](https://www.facebook.com/business/help/1526849577619206) |
| Higher intent làm giảm bao nhiêu % số lead? | Meta không công bố. Một blog bên thứ ba chỉ nói chung là đổi bớt số lượng lấy lead sạch hơn. Con số "20–40%" lan truyền trên mạng thì **không tìm thấy** trong bài tôi đọc. → Tự đo ở tuần 1. | [NGUỒN thứ cấp](https://adsuploader.com/blog/facebook-instant-form) |

### A2. Khi nào dùng form, khi nào dùng nhắn tin, khi nào dùng cuộc gọi

| Hình thức | Mạnh ở đâu | Số liệu Meta công bố | Hợp với mình khi |
|---|---|---|---|
| **Form tức thì** | Duy nhất loại này dùng được mục tiêu **"khách chất lượng"** (Conversion leads) | Chạy form tức thì cùng form website: chi phí mỗi lead thấp hơn 60%, số lead tăng 125% so với chỉ form website [NGUỒN](https://www.facebook.com/business/ads/meta-advantage-plus/leads) | Muốn Meta học từ kết quả bán hàng → **chọn làm kênh chính** |
| **Nhắn tin** (Messenger/Instagram, mẫu **Automated chat**) | Hỏi tự động từng câu rồi sales chat tiếp. Meta khuyên **≤ 6 câu**, hỏi câu dễ trước, câu nhạy cảm sau. | Phương án "Form + Messenger" để máy tự chọn: chi phí mỗi lead thấp hơn 8%, tiếp cận nhiều hơn 48% so với chỉ form [NGUỒN](https://www.facebook.com/business/ads/ad-objectives/lead-generation/lead-ads-with-messaging); [NGUỒN](https://www.facebook.com/business/help/734075733714274) | Page có người trực inbox nhanh. Thử ở tuần 3–4 [GIẢ THUYẾT] |
| **Quảng cáo gọi điện** (Calls, có thể bật "hẹn gọi lại") | Người xem bấm gọi luôn. Đo theo cuộc gọi ≥ 60 giây. | Chi phí mỗi cuộc gọi 60 giây giảm 21% sau cập nhật. Chạy trong giờ làm việc thì cuộc gọi tăng 25,4% [NGUỒN](https://www.facebook.com/business/ads/ad-objectives/lead-generation/lead-ads-with-calling) | Khách nông thôn quen gọi điện hoặc Zalo hơn điền form [GIẢ THUYẾT] |
| **WhatsApp** | Các ca thành công nước ngoài chủ yếu dùng WhatsApp | (mục A6) | **Không hợp VN.** Người Việt dùng Zalo (78,3 triệu người dùng/tháng) và Messenger (57,8 triệu người tiếp cận được bằng quảng cáo) [NGUỒN: [DataReportal 2026](https://datareportal.com/reports/digital-2026-vietnam)] |

- Quan sát Thư viện quảng cáo Meta ngày 15/10/2026: có khoảng 2.300 quảng cáo đang chạy chứa đúng cụm "đất nền" ở VN. Trong 15 mẫu đầu, 10 mẫu dùng nút "Gửi tin nhắn". Mẫu nhỏ, chỉ cho biết **thói quen** của thị trường, không chứng minh hiệu quả. [DỮ LIỆU: quan sát trực tiếp; khớp với file 15/10]

### A3. Tối ưu "khách chất lượng" (Conversion leads / Qualified leads): điểm quan trọng nhất

**Cơ chế:** lead vào → sales gọi và đánh dấu (đủ chất lượng / đi xem đất / cọc / loại) → dữ liệu này quay về Meta → Meta tìm thêm người **giống người đã thành khách thật**, thay vì giống người hay bấm form. [NGUỒN: [Meta – performance goals](https://www.facebook.com/business/help/782657799338685)]

**Thay đổi lớn năm 2026:** từ 04/2026, mục tiêu "Maximize number of qualified leads" **không còn cho tạo chiến dịch mới nếu chưa nối CAPI**. Chiến dịch đang chạy bị ảnh hưởng từ 08/2026. [NGUỒN: [Meta](https://www.facebook.com/business/help/782657799338685)]

**Điều kiện Meta đề nghị** (Meta ghi là "hướng dẫn nên đạt", không phải điều kiện cứng): [NGUỒN: [developers.facebook.com](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration); [verify data](https://developers.facebook.com/documentation/ads-commerce/conversions-api/conversion-leads-integration/crm-integration/4-verify-your-data)]
- Dùng **form tức thì** của Facebook/Instagram.
- **≥ 200 lead/tháng**, gửi dữ liệu **ít nhất 1 lần/ngày**.
- Giai đoạn muốn tối ưu (ví dụ "đủ chất lượng") phải xảy ra **trong 28 ngày** kể từ khi có lead, và tỷ lệ chuyển sang giai đoạn đó trong khoảng **1%–40%**.
- **Độ phủ lead ≥ 60%**: ít nhất 60% lead có cập nhật trạng thái gửi về. Nên giữ **mã lead của Meta** (15–17 chữ số).
- Thời gian ra hiệu quả khoảng **1 tháng**: kiểm dữ liệu 1–2 ngày, máy học 2–4 tuần.

**3 cách nối không cần code** (dễ nhất trước):
1. **Google Sheets** (Meta Business Suite → Instant forms → + Connect CRM → Google Sheets). Lead tự đổ vào bảng tính kèm cột **`lead_status`** (Intake / Qualified / Converted / Lost / Not qualified). Mỗi lần sales sửa cột này, Meta tự lấy dữ liệu và tạo sự kiện CAPI. **Bảng tính phải trống** khi nối. [NGUỒN](https://www.facebook.com/business/help/1095577538573756)
2. **Leads Center** trong Meta Business Suite: bật *Data sharing* trong cài đặt Page là nối được CAPI, sau đó **chọn được mục tiêu Conversion leads**. Có sẵn các giai đoạn Intake → Qualified → Converted → Lost / Not qualified, đổi tên được. Ví dụ "Converted" = đã cọc. [NGUỒN](https://www.facebook.com/business/help/929596264178167)
3. Đối tác (Zapier, Make…) nối CRM có sẵn. Meta cho biết nối qua đối tác mất **dưới 1 ngày**, tự làm mất 3–4 tuần. [NGUỒN](https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration)

**Meta công bố hiệu quả:** (đều là số Meta tự báo, trung bình mọi ngành)
- Form tức thì + CAPI + mục tiêu khách chất lượng: chi phí mỗi khách chất lượng **thấp hơn 21%** so với tối ưu "nhiều lead". [NGUỒN](https://www.facebook.com/business/help/782657799338685)
- Trang Advantage+ leads ghi số khác: **thấp hơn 15%** chi phí mỗi khách chất lượng, tỷ lệ lead thành khách chất lượng **tăng 44%**. [NGUỒN](https://www.facebook.com/business/ads/meta-advantage-plus/leads)
- Dubai, D&B Properties: lead ads → Salesforce → CAPI qua Make. Sau 2 tháng, giao dịch chốt được tăng ít nhất 25% (tự báo). [NGUỒN](https://www.make.com/en/success-stories/transform-lead-management-make-meta-technologies)

**Phép tính cho ngân sách 3–5 triệu/tuần** [GIẢ THUYẾT, số học đơn giản]
- 3 triệu/tuần ≈ 13 triệu/tháng; 5 triệu/tuần ≈ 21,7 triệu/tháng.
- Muốn đủ 200 lead/tháng thì chi phí mỗi lead phải ≤ **65 nghìn** (mức 3 triệu) đến ≤ **108 nghìn** (mức 5 triệu).
- Nếu chỉ 10–20% lead đạt "Qualified" thì mới có 5–10 khách chất lượng/tuần, xa mức 50/tuần. Tối ưu thẳng theo "Qualified" gần như chắc sẽ báo "Learning limited" (học bị giới hạn). Meta nói trạng thái này **không phải bị phạt**, chỉ là máy chưa tối ưu tốt. [NGUỒN](https://www.facebook.com/business/help/269269737396981)
- **Đề xuất:** nối Google Sheets ngay từ ngày đầu, sales cập nhật trạng thái mỗi ngày. Tuần 1–2 tối ưu "nhiều lead" bằng form Higher intent + OTP để có số liệu nền. Từ tuần 3, khi đã đủ khoảng 200 lead/tháng, chạy thử mục tiêu khách chất lượng song song và so **chi phí / khách đủ chất lượng**.

### A4. Giai đoạn máy học, nhắm rộng (Advantage+), Andromeda, ngân sách nhỏ

- **Giai đoạn máy học:** thường thoát khi đạt **khoảng 50 kết quả trong 1 tuần** kể từ lần sửa lớn gần nhất. Trong giai đoạn này giá đắt hơn và kết quả dao động. Meta khuyên: đừng sửa khi đang học, gộp các nhóm giống nhau, đặt ngân sách "thực tế", tránh đổi ngân sách liên tục. [NGUỒN](https://www.facebook.com/business/help/112167992830700)
- **Sửa lớn làm máy học lại:** đổi đối tượng, đổi mẫu quảng cáo, đổi sự kiện tối ưu, thêm mẫu mới, tạm dừng từ 7 ngày, đổi cách đặt giá thầu. Đổi ngân sách thì **tuỳ độ lớn**. Meta lấy ví dụ 100 lên 101 USD thì không sao, 100 lên 1.000 USD thì có thể. Meta **không công bố ngưỡng 20%**. Luật "tăng ≤ 20%/lần" trong khung marketingskills là quy ước thận trọng của nghề, vẫn nên giữ. [NGUỒN](https://www.facebook.com/business/help/316478108955072) + [GIẢ THUYẾT]
- **Bị "Learning limited"**: thường do đối tượng hẹp, ngân sách thấp, sự kiện hiếm, quá nhiều quảng cáo. Cách chữa: gộp nhóm, mở rộng đối tượng, tăng ngân sách, hoặc chọn sự kiện xảy ra thường hơn. [NGUỒN](https://www.facebook.com/business/help/269269737396981)
- **Advantage+ audience** (nhắm rộng bằng AI): mặc định cho chiến dịch mới. Sở thích hay danh sách khách chỉ là **gợi ý**. Tuổi tối thiểu, **vị trí**, ngôn ngữ, loại trừ tệp tuỳ chỉnh là **giới hạn cứng**. Chiến dịch lead vẫn tính là "Advantage+ On" khi chọn vị trí bất kỳ. Vậy **khoanh vùng Bắc Giang cũ mà vẫn dùng được AI của Meta**. [NGUỒN: [Advantage+ leads FAQ](https://www.facebook.com/business/ads/meta-advantage-plus/leads); [location](https://www.facebook.com/business/help/365561350785642)]
- Meta khuyên: nếu vùng địa lý buộc phải hẹp thì **chỉ đặt tuổi và vị trí**, bỏ các lớp nhắm khác. [NGUỒN](https://www.facebook.com/business/ads/automation/tailored-campaigns)
- **Andromeda**: hệ thống chọn quảng cáo của Meta (ra mắt 12/2024). Nó lọc từ hàng chục triệu quảng cáo xuống vài nghìn cho mỗi người. Meta nói càng nhiều mẫu đa dạng thì Andromeda càng chọn đúng mẫu cho từng người, và chất lượng quảng cáo tăng 8%. [NGUỒN: [Meta for Business 03/2025](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance); [engineering.fb.com 12/2024](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/)]
  - Câu "creative là nhắm đối tượng" là cách người làm nghề tóm tắt điều trên, **không phải câu của Meta**. Hiểu thực tế: mỗi mẫu nên nói với một nhóm người khác nhau, ví dụ cha mẹ mua cho con, người đi làm xa mua đất quê, công nhân KCN. Không nên làm 5 bản cùng một ảnh. [GIẢ THUYẾT]
- **Thực tế khi ngân sách nhỏ:** 1 chiến dịch, 1 nhóm quảng cáo, 3–6 mẫu, chạy liền ≥ 7 ngày không sửa. Thêm mẫu mới theo lô, ví dụ mỗi 2 tuần, thay vì lắt nhắt. [GIẢ THUYẾT dựa trên NGUỒN ở trên]

### A5. Tốc độ phản hồi lead: nghiên cứu gốc

| Nghiên cứu | Số chính | Nhãn |
|---|---|---|
| **HBR 03/2011**, "The Short Life of Online Sales Leads" (Oldroyd, McElheran, Elkington) | Kiểm 2.241 công ty Mỹ: **37%** trả lời trong 1 giờ, 24% mất hơn 24 giờ, **23% không bao giờ trả lời**. Trung bình **42 giờ**. Dữ liệu 1,25 triệu lead của 42 công ty: liên hệ trong 1 giờ thì khả năng lọc được lead cao **gần 7 lần** so với chậm thêm 1 giờ, cao **hơn 60 lần** so với chờ ≥ 24 giờ. "Lọc được" nghĩa là có cuộc nói chuyện thực sự với người quyết định. | Bản tóm tắt HBR [NGUỒN](https://hbr.org/2011/03/the-short-life-of-online-sales-leads) (bài đầy đủ cần trả phí); số liệu [NGUỒN thứ cấp](https://www.smartcompany.com.au/marketing/20110704-are-you-letting-online-leads-go-cold/); trích dẫn học thuật [BYU](https://scholarsarchive.byu.edu/facpub/9711) |
| **Lead Response Management Study** (Oldroyd, MIT, với InsideSales/XANT, 10/2007) | Liên hệ trong **5 phút** cho số lead lọc được gấp **21 lần** so với chờ 30 phút. Con số "100 lần" hay được trích **không có** trong thông cáo tôi đọc. Đây là nghiên cứu do bên bán phần mềm tài trợ. | [NGUỒN (thông cáo)](https://www.insidesales.com/xant-com-research-stuns-2007-marketing-sherpa-b2b-summit) |
| **Meta** | Nối CRM hoặc Leads Center để nhận lead ngay. Tải tay từ trình quản lý quảng cáo làm chậm việc gọi lại. Chạy quảng cáo **trong giờ làm việc**. Hỏi khách muốn được gọi lúc nào, qua kênh nào. | [NGUỒN](https://www.facebook.com/business/help/2246428158756947) |

### A6. Chủ đầu tư nước ngoài làm thế nào

**Ấn Độ: đo cả phễu "chi phí/lead → chi phí/lượt xem dự án → chi phí/booking"**
- Hãng CRM Sell.do (2026) khuyên đánh giá mỗi kênh ở **bậc cuối** (booking, tức đặt cọc). Lead Meta rẻ có thể không bao giờ nghe máy. Gọi trong 1 phút. Dùng câu hỏi lọc trong form (ngân sách, thời điểm nhận nhà). Họ ước tính lead Meta ở Ấn Độ tốn ₹150–2.000. [NGUỒN thứ cấp – nhà bán phần mềm](https://www.sell.do/blog/paid-lead-generation-real-estate-india-2026)
- **Mahindra Lifespaces** (12/2016–12/2017): video dạo quanh dự án, form tức thì, chạy lại cho **người đã mở form mà chưa gửi** và người tương tác Page, tạo tệp tương tự từ người đã điền form. Kết quả: lợi nhuận trên chi phí quảng cáo gấp 4, chi phí mỗi lead giảm 30%, 4.000 lead người Ấn ở nước ngoài. [NGUỒN thứ cấp – agency đăng lại case study của Facebook](https://www.socialbeat.in/blog/mahindra-lifespaces-case-study/) (trang gốc của Facebook đã gỡ)
- **Casagrand** (Chennai, 2017): video tạo nhận biết → **chạy lại form cho người đã xem video** → tệp tương tự từ lead. Chi phí mỗi lead thấp hơn 60% so với kênh số khác, doanh thu khoảng ₹190 crore. [NGUỒN thứ cấp](https://www.socialbeat.in/blog/casagrand-case-study-published-by-facebook/)

**Dubai/UAE: nhắn tin và sự kiện**
- **DAMAC** (08–09/2025): gửi tin WhatsApp cho lead cũ, **mời dự sự kiện trực tiếp**. Tỷ lệ chuyển đổi gấp 2 so với chiến dịch không có nhắn tin, số lead gấp 3,7 so với email (tự báo). [NGUỒN](https://whatsappbusiness.com/resources/success-stories/damac-properties/)
- **D&B Properties**: nối CRM về Meta (mục A3). [NGUỒN](https://www.make.com/en/success-stories/transform-lead-management-make-meta-technologies)

**Mỹ Latinh: ca gần nhất với "đất nền"**
- **Lomas de Angelopolis** (Puebla, Mexico, **bán lô đất**, chốt 60–70 lô/tháng): đội 13 sales không trả lời kịp tin nhắn từ quảng cáo. Họ thêm trợ lý AI của Meta trả lời ngay, kể cả ngoài giờ, gửi giá và đặt lịch hẹn. Kết quả: số lịch hẹn mỗi tháng gấp 6 (từ 2 lên 12), chu kỳ bán ngắn hơn 33%. Trợ lý tự xử lý khoảng 30% cuộc trò chuyện (02–04/2026, tự báo). [NGUỒN](https://whatsappbusiness.com/resources/success-stories/lomas-de-angelopolis/)
- **Engelife** (Brazil, 20/10–03/11/2025): biểu mẫu hỏi lọc tự động trong chat, gồm nhu cầu và khả năng tài chính. Chi phí mỗi lead đủ chất lượng giảm 37%, tỷ lệ lọc đạt tăng 26 điểm phần trăm (tự báo). [NGUỒN](https://whatsappbusiness.com/resources/success-stories/engelife-construtora-e-incorporadora/)

**Úc/Mỹ: chạy lại người xem video, nuôi dưỡng lead, nhà mẫu**
- Meta cho tạo **tệp người đã xem video** theo mốc 3 giây, 10 giây, 15 giây, 25/50/75%, hoặc xem hết, trên cả Facebook và Instagram. [NGUỒN](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads)
- Meta cũng cho chạy lại **người đã mở form nhưng chưa gửi**. Meta khuyên tạo tệp tương tự từ **khách đã mua**, không phải từ người điền form. [NGUỒN](https://www.facebook.com/business/help/435270316658768)
- Mô hình "ngày mở cửa / nhà mẫu (open house)" kết hợp chạy lại người xem video ở Úc: các ca tôi tìm được đều do agency tự quảng bá, trang gốc đã gỡ (404). **Chưa có nguồn gốc đáng tin.** [GIẢ THUYẾT]

### A7. Nội dung quảng cáo BĐS hiệu quả (theo Meta)

- **Video dọc 9:16 có tiếng, chữ nằm trong vùng an toàn:** phân phối vào Reels nhiều gấp 2, chi phí mỗi kết quả thấp hơn 34,5% so với quảng cáo ảnh. [NGUỒN](https://www.facebook.com/business/ads/facebook-instagram-reels-ads)
- **Luật 3 giây:** thông điệp hoặc thương hiệu xuất hiện trong 3 giây đầu. **Dùng người thật** để giới thiệu, giải thích, hoặc kể lại cảm nhận của khách. Ảnh nên tỷ lệ 1:1 hoặc 4:5. Thiết kế cho xem **có tiếng**. [NGUỒN](https://www.facebook.com/business/ads/automation/tailored-campaigns)
- **Đa dạng mẫu** để Andromeda có lựa chọn (A4). [NGUỒN](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance)
- **Áp dụng cho BĐS** [GIẢ THUYẾT, kiểm bằng A/B]:
  - (a) Khách thật cầm sổ nói 1 câu.
  - (b) Cha mẹ kể chuyện mua đất cho con.
  - (c) Đi bộ dạo quanh dự án bằng điện thoại, quay dọc, có lời dẫn.
  - (d) Bản đồ khoảng cách tới chợ, trường, KCN.
  - (e) Câu chuyện lễ trao sổ.
  - Mỗi mẫu một "câu mở" riêng. Câu mở là **nỗi lo của người mua** ("sợ đất không sổ?"), không phải tên dự án.

---

## 3. Phần B: Việt Nam

### B1. CĐT lớn và đại lý chạy quảng cáo thế nào

- **Mô hình 2 tầng** (soi Thư viện quảng cáo 14–15/10/2026), chi tiết ở `2026-10-15-thu-vien-quang-cao-cdt-lon.md`. [DỮ LIỆU]
  - *Tầng 1: trang CĐT* làm thương hiệu, chính sách, tiến độ, sự kiện. Ít dùng form.
  - *Tầng 2: trang đại lý/sales* lấy số điện thoại bằng form "Get quote" hoặc nút "Gửi tin nhắn". Mồi thường dùng: "nhận bảng giá / bảng hàng / bài toán tài chính từng căn".
  - Nhịp chạy: ra nhiều mẫu đúng ngày đổi chính sách hoặc ngày sự kiện, có quảng cáo tổng kết sự kiện ngay hôm sau.
  - Có dòng chú thích "(*) số liệu minh hoạ / mốc dự kiến" cuối bài.
- **Nội dung "chính sách bán hàng"** của CĐT lớn hiện nay: trả trước 30%, hỗ trợ lãi suất 0% kèm ân hạn gốc 3 năm, chiết khấu theo tiến độ, quà tặng trừ vào giá. Ví dụ là bài "nội dung được tài trợ" ngày 09/04/2026. [NGUỒN: [VnExpress – Hoang Huy New City](https://vnexpress.net/hoang-huy-new-city-ap-dung-chinh-sach-0-lai-suat-trong-3-nam-5060306.html)]
  - Chuyên gia trong toạ đàm VnExpress (06/05/2026) cảnh báo: hết ưu đãi thì lãi thả nổi; phần lớn chi phí hỗ trợ lãi hoặc ân hạn gốc **đã cộng vào giá bán**; tổng trả nợ không nên quá 40% thu nhập. [NGUỒN: [VnExpress](https://vnexpress.net/chuyen-gia-canh-bao-rui-ro-goi-vay-mua-nha-lai-suat-thap-5070777.html)]
  - Dự án mình **chưa có văn bản** về chia đợt hay ngân hàng, nên **chưa dùng**.
- **Kênh chính thức và danh sách đại lý:** Ủy ban Cạnh tranh quốc gia (07/2025) khuyên người mua chỉ giao dịch với CĐT hoặc đại lý được uỷ quyền, và **tra danh sách đại lý chính thức trên website CĐT**. [NGUỒN: [LSVN 30/07/2025](https://lsvn.vn/can-trong-voi-quang-cao-sai-su-that-ve-du-an-bat-dong-san-a161016.html)]
  - Vịnh An Hoà (2021): CĐT công bố 8 đại lý chính thức sau khi có bên ngoài hệ thống nhận cọc trái phép. [NGUỒN: [Nhà Đầu tư](https://nhadautu.vn/mao-danh-chu-dau-tu-de-giao-dich-bat-dong-san-vinh-an-hoa-trai-phep-d50724.html)]
- **Quy định nội bộ** của Vinhomes và CĐT lớn với đại lý về quảng cáo (cách đặt tên page, có được chạy tên dự án không): **không tìm được văn bản công khai.** Thường nằm trong hợp đồng đại lý. [GIẢ THUYẾT]
- **Ý kiến người làm nghề VN** (bài cộng đồng Brands Vietnam, 01/03/2026, GM một agency): [NGUỒN – ý kiến cá nhân, chưa kiểm chứng](https://www.brandsvietnam.com/congdong/topic/cam-nang-toan-tap-chien-luoc-quang-cao-bat-dong-san-thuc-chien)
  - Chia quảng cáo theo 3 giai đoạn: làm nóng → mở bán → duy trì.
  - Chạy lại người đã xem là "vũ khí mạnh nhất".
  - Mục tiêu tham khảo: lead đủ chất lượng > 50%, lead → đi xem dự án 10–20%, chi phí mỗi giao dịch 1–3% giá trị (với lô 1 tỷ là 10–30 triệu).
  - Khuyên tránh "giật tít" trong BĐS.

### B2. Cách làm phổ biến nhưng NÊN TRÁNH, và vì sao

| Cách làm | Vì sao tránh | Nhãn |
|---|---|---|
| **Mua data khách** / dùng danh sách của sàn khác | **Bị cấm** từ 01/01/2026 (Luật 91/2025 Điều 7 khoản 6). Tổ chức bị phạt tới **10 lần khoản thu** hoặc **3 tỷ** khi không xác định được khoản thu; cá nhân bằng một nửa. Có thể bị xử lý hình sự. Báo chí đã mô tả thị trường "chợ đen" danh sách khách BĐS và các cuộc gọi làm phiền. | [NGUỒN: [hethongphapluat Điều 7](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-7), [Điều 8](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-8); [Tuổi Trẻ 15/09/2022](https://tuoitre.vn/bi-danh-cap-du-lieu-khach-hang-doanh-nghiep-bat-dong-san-bao-mat-ra-sao-2022091514474369.htm)] |
| **Page vệ tinh / đặt tên như trang CĐT** | Người mua bị lừa cọc, CĐT mất uy tín. Có tiền lệ: Vinhomes cảnh báo người giả danh và web giả (Cục An toàn thông tin, 22/12/2024); UDIC bác mọi việc nhận cọc nhân danh liên danh CĐT NOXH NO1 Hạ Đình khi dự án chưa đủ điều kiện (22/05/2025). Meta yêu cầu quản trị viên Page **thể hiện đúng danh tính** và có thể gỡ Page. | [NGUỒN: [LSVN](https://lsvn.vn/canh-bao-hanh-vi-gia-mao-website-doanh-nghiep-nham-lua-dao-chiem-doat-tai-san-a151452.html); [DĐDN](https://diendandoanhnghiep.vn/ha-noi-canh-giac-chieu-tro-gia-mao-lua-dao-mua-ban-can-ho-du-an-nha-o-xa-hoi-no1-10154913.html); [Meta Pages policy](https://www.facebook.com/policies_center/pages_groups_events)] |
| **Cam kết lợi nhuận / "dòng tiền x triệu/tháng"** | Cocobay Đà Nẵng (2019) tuyên bố không trả được lợi nhuận đã cam kết, làm mất niềm tin cả phân khúc. Cam kết không thực hiện được có thể bị coi là "gian lận, lừa dối" (Luật KDBĐS Điều 8 khoản 4) [GIẢ THUYẾT về cách áp dụng]. | [NGUỒN: [VnExpress 01/12/2019](https://vnexpress.net/giua-duong-dut-ganh-4020679.html)] |
| **"Nhất / duy nhất / rẻ nhất / số 1"** | Cấm nếu không có giấy tờ hợp pháp chứng minh (Luật QC Điều 8 khoản 11). Từ **05/7/2026**, Thông tư 12/2026/TT-BVHTTDL chỉ chấp nhận khảo sát của tổ chức nghiên cứu thị trường hợp pháp hoặc chứng nhận giải thưởng, và phải ghi tên, số hiệu tài liệu trên quảng cáo. Phạt **10–20 triệu** theo NĐ 87/2026 (theo báo, chưa đọc văn bản gốc). | [NGUỒN: [hethongphapluat – Luật QC Đ8](https://hethongphapluat.com/luat-quang-cao-2012/dieu-8); [LuatVietnam – TT 12/2026](https://luatvietnam.vn/tin-van-ban-moi/tai-lieu-chung-minh-de-quang-cao-duoc-su-dung-cac-tu-nhat-duy-nhat-tot-nhat-so-mot-186-109322-article.html); [NGUỒN thứ cấp NĐ 87](https://doanhnghiephoinhap.vn/tu-1552026-siet-manh-vi-pham-quang-cao-muc-phat-cao-nhat-toi-100-trieu-dong-132411.html)] |
| **So sánh trực tiếp** giá/chất lượng với dự án khác | Cấm (Luật QC Điều 8 khoản 10). Phạt 40–60 triệu theo NĐ 87/2026 (theo báo). | [NGUỒN](https://hethongphapluat.com/luat-quang-cao-2012/dieu-8); [NGUỒN thứ cấp](https://doanhnghiephoinhap.vn/tu-1552026-siet-manh-vi-pham-quang-cao-muc-phat-cao-nhat-toi-100-trieu-dong-132411.html) |
| **Dùng ảnh hay lời của khách khi chưa đồng ý** | Cấm (Luật QC Điều 8 khoản 8). Phạt 20–40 triệu (theo báo). | [NGUỒN](https://hethongphapluat.com/luat-quang-cao-2012/dieu-8) |
| **Thông tin quảng cáo khác thông tin đã công khai** | Cấm (Luật QC Điều 8 khoản 9; Luật KDBĐS Điều 8 khoản 2) | [NGUỒN](https://hethongphapluat.com/luat-kinh-doanh-bat-dong-san-2023/dieu-8) |
| **Thu thật nhiều lead rẻ rồi đổ cho sales** | Chính là bệnh "2.003 lead, 0 chất lượng". Meta lúc đó học tìm người **hay bấm form**, không tìm người **mua**. | [DỮ LIỆU] + [NGUỒN](https://www.facebook.com/business/help/782657799338685) |
| **Chạy bằng tài khoản clone / chưa xác thực** | NĐ 147/2024 (hiệu lực 25/12/2024) yêu cầu tài khoản mạng xã hội xác thực bằng SĐT VN, người dùng chịu trách nhiệm nội dung. Tài khoản bị hạn chế có thể kéo cả Business Manager bị khoá theo [GIẢ THUYẾT]. | [NGUỒN: [hatinh.gov.vn](https://hatinh.gov.vn/vi/bai-viet/tu-hom-nay-tai-khoan-mang-xa-hoi-phai-xac-thuc-so-dien-thoai-moi-duoc-dang-bai)] |

### B3. Pháp lý (đọc văn bản hoặc bản chép điều luật; tôi không phải luật sư, cần luật sư xác nhận trước khi chạy tiền)

**Luật Kinh doanh BĐS số 29/2023/QH15**
- **Hiệu lực:** Quốc hội thông qua 28/11/2023. Điều 82 ban đầu ghi hiệu lực 01/01/2025, nhưng **Luật 43/2024/QH15 đã cho có hiệu lực sớm từ 01/08/2024**. Vậy mốc "01/01/2025" trong đề bài **không còn đúng**. [NGUỒN: [caselaw – toàn văn](https://caselaw.vn/van-ban-phap-luat/411479-luat-kinh-doanh-bat-dong-san-so-29-2023-qh15-ngay-28-11-2023-cua-quoc-hoi); [LuatVietnam](https://luatvietnam.vn/dat-dai-nha-o/tong-hop-van-ban-ve-dat-dai-nha-o-co-hieu-luc-thang-8-2024-567-98648-article.html)]
- **Điều 6, công khai thông tin trước khi bán:** CĐT phải đăng thông tin trên hệ thống thông tin nhà ở và thị trường BĐS **và trên website của doanh nghiệp**. Với đất đã có hạ tầng trong dự án, phải đăng:
  - giấy chứng nhận quyền sử dụng đất;
  - văn bản xác nhận đủ điều kiện chuyển nhượng cho cá nhân tự xây nhà;
  - giấy tờ hoàn thành hạ tầng và nghĩa vụ tài chính;
  - các hạn chế quyền và việc thế chấp.
  - Thông tin phải cập nhật khi có thay đổi. [NGUỒN: [Điều 6](https://hethongphapluat.com/luat-kinh-doanh-bat-dong-san-2023/dieu-6)]
- **Điều 8, hành vi cấm** (8 khoản), liên quan nhất: làm sai lệch thông tin; không công khai thông tin; gian lận, lừa dối. [NGUỒN: [Điều 8](https://hethongphapluat.com/luat-kinh-doanh-bat-dong-san-2023/dieu-8)]
- **Điều 31, điều kiện bán đất nền cho cá nhân tự xây:** hạ tầng xong, có sổ, không tranh chấp, không thuộc phường/quận đô thị loại đặc biệt, I, II, III, đã báo Sở trước (trả lời trong 15 ngày), đã công khai theo Điều 6. **Điều 61:** môi giới phải có **chứng chỉ hành nghề** và hành nghề trong một doanh nghiệp môi giới hoặc sàn. Luật **không bắt buộc** CĐT bán qua sàn. [NGUỒN: [caselaw](https://caselaw.vn/van-ban-phap-luat/411479-luat-kinh-doanh-bat-dong-san-so-29-2023-qh15-ngay-28-11-2023-cua-quoc-hoi)]
- Luật **không có điều riêng về "quảng cáo"**. Nội dung quảng cáo phải khớp thông tin đã công khai (Điều 6, 8), phần còn lại theo Luật Quảng cáo.

**Nghị định 96/2024/NĐ-CP** (ban hành 24/07/2024, hiệu lực 01/08/2024) [NGUỒN: [VCCI – toàn văn](https://vcci.com.vn/legal-document/96-2024-nd-cp)]
- Điều 4: công khai **trước khi ký hợp đồng**, cập nhật **trong 5 ngày làm việc** khi có thay đổi.
- Điều 9: CĐT gửi thông báo cho cơ quan quản lý BĐS cấp tỉnh trước khi chuyển nhượng đất cho cá nhân tự xây; cơ quan trả lời trong 15 ngày và đăng văn bản trả lời lên cổng thông tin.

**Luật Quảng cáo 2012, sửa đổi bởi Luật 75/2025/QH15** (thông qua 16/06/2025, **hiệu lực 01/01/2026**) [NGUỒN: [LuatVietnam – 7 điểm mới](https://luatvietnam.vn/linh-vuc-khac/diem-moi-cua-luat-quang-cao-sua-doi-2025-883-102813-article.html)]
- Quảng cáo trên mạng phải có **dấu hiệu nhận diện là quảng cáo**. Người dùng mạng xã hội làm quảng cáo phải gắn nhãn quảng cáo hoặc tài trợ.
- Người có ảnh hưởng (KOL) phải kiểm tra tài liệu sản phẩm, **chưa hiểu rõ sản phẩm thì không được giới thiệu**, phải báo là đang quảng cáo. Phạt 80–100 triệu (theo báo).
- Quảng cáo vi phạm phải bị gỡ trong 24 giờ khi cơ quan yêu cầu.
- Điều 8 vẫn cấm: khoản 8 (dùng hình ảnh cá nhân chưa đồng ý), khoản 9 (gây nhầm lẫn), khoản 10 (so sánh trực tiếp), khoản 11 (chữ "nhất"). [NGUỒN](https://hethongphapluat.com/luat-quang-cao-2012/dieu-8)
- Thông tư 12/2026/TT-BVHTTDL (05/07/2026) về giấy tờ chứng minh chữ "nhất". Nghị định 87/2026/NĐ-CP xử phạt văn hoá và quảng cáo (hiệu lực 15/05/2026, khung 5–100 triệu). [NGUỒN thứ cấp, chưa đọc văn bản gốc]

**Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15** (hiệu lực **01/01/2026**) + **NĐ 356/2025/NĐ-CP** (thay NĐ 13/2023 từ 01/01/2026)
- Điều 7: **cấm mua, bán dữ liệu cá nhân**. Điều 8: mức phạt như mục B2; vi phạm chuyển dữ liệu ra nước ngoài bị phạt tới 5% doanh thu năm trước. [NGUỒN: [Điều 7](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-7), [Điều 8](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-8)]
- Điều 9, **đồng ý hợp lệ:** tự nguyện, biết rõ mục đích, **đồng ý riêng cho từng mục đích**, lưu lại được. **Im lặng hay không phản hồi không phải là đồng ý.** [NGUỒN](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-9)
- Điều 28, **dùng dữ liệu để quảng cáo:**
  - phải có đồng ý của khách, cho khách biết nội dung, cách thức, tần suất;
  - có cách để khách **từ chối và ngừng nhận** quảng cáo;
  - phải chứng minh được đã dùng dữ liệu thế nào;
  - quảng cáo theo hành vi chỉ được thu thập khi khách đồng ý.
  [NGUỒN](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-28)
- Điều 20, **chuyển dữ liệu ra nước ngoài:** gồm cả việc **dùng nền tảng ở nước ngoài để xử lý dữ liệu thu ở VN**. Phải lập hồ sơ đánh giá tác động và gửi cơ quan chuyên trách **trong 60 ngày** kể từ lần chuyển đầu. [NGUỒN](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-20)
  - Điều 38: doanh nghiệp nhỏ hoặc khởi nghiệp được chọn chưa làm Điều 21, 22 trong 5 năm; doanh nghiệp siêu nhỏ được miễn. **Không rõ có gồm hồ sơ Điều 20 không.** [NGUỒN](https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-38)
  - NĐ 356/2025 siết điều kiện chuyển dữ liệu (Mẫu 09). [NGUỒN thứ cấp: [LuatVietnam](https://luatvietnam.vn/dan-su/nghi-dinh-356-2025-nd-cp-quy-dinh-chi-tiet-luat-bao-ve-du-lieu-ca-nhan-422896-d1.html)]
- **Ảnh hưởng tới việc tải danh sách khách lên Meta làm tệp đối tượng (custom audience):**
  - Meta yêu cầu người tải lên **cam kết có quyền và căn cứ hợp pháp**. Số điện thoại được mã hoá (hash) trước khi gửi. [NGUỒN: [Meta Customer List Terms](https://www.facebook.com/legal/terms/customaudience)]
  - Mã hoá **không làm mất** nghĩa vụ xin đồng ý theo Điều 9 và 28, cũng như nghĩa vụ chuyển xuyên biên giới theo Điều 20. [GIẢ THUYẾT pháp lý, cần luật sư]
  - **Hướng an toàn:** chỉ tải lên danh sách những khách **đã tích ô đồng ý** "nhận thông tin quảng cáo qua Facebook/Zalo". Nếu chưa có thì dùng **tệp tương tác**: người xem video, người mở form, người tương tác Page. Các tệp này không phải tải dữ liệu lên.
  - Lead từ form có ô đồng ý (A1) là nguồn hợp lệ nhất.

**Nghị định 147/2024/NĐ-CP** (hiệu lực 25/12/2024): tài khoản mạng xã hội phải xác thực bằng SĐT VN; chỉ tài khoản đã xác thực mới được đăng hay bình luận; người dùng chịu trách nhiệm nội dung mình đăng. Liên quan tới quảng cáo: **người quản trị Page và tài khoản quảng cáo nên là tài khoản thật, đã xác thực**. [NGUỒN: [hatinh.gov.vn](https://hatinh.gov.vn/vi/bai-viet/tu-hom-nay-tai-khoan-mang-xa-hoi-phai-xac-thuc-so-dien-thoai-moi-duoc-dang-bai)]

### B4. "Special Ad Category: Housing" (nhóm quảng cáo nhà ở) của Meta có áp dụng ở Việt Nam không?

- **Không bắt buộc ở VN.** Giới hạn nhắm (không chọn được tuổi, giới tính, mã bưu chính, không tạo tệp tương tự, bán kính tối thiểu) chỉ áp dụng cho nhà quảng cáo **ở Mỹ hoặc chạy tới Mỹ, Canada và một số nước châu Âu**. Doanh nghiệp ngoài các vùng này vẫn phải trả lời ô "Special Ad Category" khi tạo qua API, nhưng **được chọn bật hoặc tắt giới hạn**. [NGUỒN: [Meta Help – choose SAC](https://www.facebook.com/business/help/298000447747885); [Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category)]
- **Ngoại lệ:** nếu chạy tới **Việt kiều ở Mỹ, Canada, châu Âu** thì phải khai báo Housing và chịu giới hạn. [NGUỒN như trên]

---

## 4. Áp dụng cho Yên Thế Golden Hill: làm ngay / làm sau / không làm

| Việc | Vì sao | Căn cứ |
|---|---|---|
| **LÀM NGAY (trước khi chi đồng đầu tiên)** | | |
| Kiểm website CĐT đã **công khai thông tin dự án** đủ theo Điều 6 chưa (sổ, văn bản Sở cho bán nền, hạ tầng, thế chấp). Đặt link trong form và trên Page. | Bắt buộc trước khi bán; quảng cáo phải khớp thông tin công khai | [NGUỒN] Luật KDBĐS Đ6, NĐ 96 Đ4 · **[CẦN XÁC NHẬN]** |
| Chạy **chỉ từ Page CĐT chính thức**, tài khoản quảng cáo của doanh nghiệp, người quản trị là tài khoản thật đã xác thực. Không dùng nick clone. | Tránh khoá lây; đúng NĐ 147 | [NGUỒN] + [GIẢ THUYẾT] |
| Nối **Google Sheets ↔ CAPI for CRM** (hoặc Leads Center + Data sharing) cho form đầu tiên. Thống nhất định nghĩa: *Qualified* = đúng vùng + mua trong 6 tháng + nghe máy và đồng ý xem đất. *Converted* = đã đi xem đất hoặc đã cọc. Sales cập nhật **mỗi ngày**. | Chữa bệnh "0 lead chất lượng"; điều kiện để dùng mục tiêu khách chất lượng từ 04/2026 | [NGUỒN] Meta 1095577538573756, 782657799338685 |
| Form **Higher intent + OTP + ô đồng ý**. Hỏi 3–4 câu trắc nghiệm: (1) đang sống ở xã/huyện nào (dùng câu trả lời có điều kiện); (2) mua để ở / cho con / đầu tư; (3) định mua khi nào; (4) muốn được gọi lúc nào, qua điện thoại hay Zalo. | Lọc ngay từ form; đúng luật đồng ý | [NGUỒN] A1; Luật 91/2025 Đ9, Đ28 |
| **Vị trí:** ghim bán kính quanh dự án và các xã/huyện Bắc Giang cũ nơi có người mua (dùng file 103 khách đã mua). **Tắt** tuỳ chọn mở rộng ra ngoài vùng. Mỗi tuần xem báo cáo theo vùng. | 76% người mua ở Bắc Giang cũ; lead cũ lệch về Bắc Ninh cũ | [DỮ LIỆU] + [NGUỒN] Meta location |
| Kiểm trong trình quản lý quảng cáo xem "Bắc Ninh" sau sáp nhập 07/2025 tính ranh giới cũ hay mới. **Không chọn theo tên tỉnh.** | Có thể chính đây là nguyên nhân 60–70% lead ở Bắc Ninh cũ | [GIẢ THUYẾT] |
| **1 chiến dịch, 1 nhóm quảng cáo, 3–6 mẫu khác góc**, chủ yếu video dọc 9:16 người thật: khách nhận sổ, cha mẹ mua cho con, dạo quanh dự án. Chạy ≥ 7 ngày không sửa. | Đủ dữ liệu để máy học; Andromeda cần đa dạng mẫu | [NGUỒN] A4, A7 |
| **Giờ chạy:** chỉ chạy khi có người trực. Đặt mục tiêu **gọi lại ≤ 5 phút**, ghi giờ gọi vào bảng tính. | 7 lần / 21 lần | [NGUỒN] A5 |
| Thêm dòng "(*)" cho mọi con số. Không "nhất", không so sánh, không hứa lời. Ảnh khách phải có đồng ý bằng văn bản. | Luật QC Đ8 k8–11 | [NGUỒN] B2 |
| Bảng chấm hằng tuần: chi tiêu → lead → lead OTP hợp lệ → **Qualified** → đi xem đất → cọc. Chỉ số chính: **chi phí / khách đủ chất lượng** và **chi phí / lượt đi xem đất**. | Khớp khung marketingskills; cách Ấn Độ đo cả phễu | [NGUỒN thứ cấp] Sell.do + [GIẢ THUYẾT] |
| **LÀM SAU (tuần 3 trở đi, khi đã có số liệu)** | | |
| Thử mục tiêu **"Maximize number of qualified leads"** trong chiến dịch thứ hai (so A/B) khi đạt khoảng 200 lead/tháng | Meta đề nghị ≥ 200 lead/tháng; trung bình rẻ hơn 15–21% mỗi khách chất lượng | [NGUỒN] A3 |
| Thử **Form + Messenger (Automated chat ≤ 6 câu)** hoặc **quảng cáo gọi điện** trong giờ làm việc, so chi phí mỗi khách đủ chất lượng với form | Người Việt quen nhắn và gọi | [NGUỒN] A2 + [GIẢ THUYẾT] |
| **Chạy lại** người xem video ≥ 50% và người mở form chưa gửi (cửa sổ 14–30 ngày) bằng mẫu "lịch xem đất / lễ trao sổ tiếp theo" | Cách Mahindra, Casagrand | [NGUỒN] A6 |
| Quảng cáo **sự kiện "ngày xem đất / lễ trao sổ"**: úp mở trước → mời đăng ký → tổng kết sau | Cách DAMAC và CĐT VN đang làm | [NGUỒN] A6, B1 |
| Tạo **tệp tương tự từ khách đã mua**, **chỉ** sau khi luật sư xác nhận cách xin đồng ý và hồ sơ chuyển dữ liệu ra nước ngoài | Luật 91/2025 Đ9, 20, 28 | [NGUỒN] + [GIẢ THUYẾT pháp lý] |
| Tăng ngân sách **≤ 20%/lần**, cách nhau ≥ 3–4 ngày, chỉ khi chi phí / khách đủ chất lượng ổn định | Đổi ngân sách lớn có thể làm máy học lại | [NGUỒN] + [GIẢ THUYẾT] |
| Công bố trên website **danh sách đại lý / môi giới được uỷ quyền** (có chứng chỉ hành nghề) và quy tắc cho họ: không đặt tên page giống CĐT, chỉ dùng mẫu đã duyệt | Chống page giả; đúng khuyến nghị của UBCTQG; Điều 61 | [NGUỒN] B1, B3 |
| **KHÔNG LÀM** | | |
| Mua data, xin hay mua danh sách của sàn khác, tải số điện thoại chưa có đồng ý lên Meta | Cấm; phạt tới 3 tỷ hoặc 10 lần khoản thu | [NGUỒN] |
| Page vệ tinh, page "Quỹ căn CĐT…", page giả tên CĐT | Lừa dối; Meta gỡ Page | [NGUỒN] |
| "Rẻ nhất / duy nhất / số 1", so sánh với Ion City hay dự án khác, "cam kết tăng giá / dòng tiền x triệu" | Luật QC Đ8; Luật KDBĐS Đ8 | [NGUỒN] |
| Tối ưu "nhiều lead" bằng form More volume không lọc, rồi chấm theo số lead | Lặp lại bài học 2.003 lead | [DỮ LIỆU] |
| Chia 5–10 nhóm quảng cáo nhỏ, sửa quảng cáo mỗi ngày | Không bao giờ thoát giai đoạn học | [NGUỒN] |
| Dùng tuỳ chọn WhatsApp của Meta | Người Việt dùng Zalo/Messenger | [NGUỒN] DataReportal + [GIẢ THUYẾT] |

---

## 5. Câu hỏi chưa tìm được nguồn gốc / giới hạn

1. **HBR 2011:** bài đầy đủ phải trả phí. Các số 2.241 / 37% / 42 giờ / 7 lần / 60 lần lấy qua bài thuật lại (SmartCompany 2011).
2. **Nghiên cứu 2007 (MIT/InsideSales):** chỉ đọc được thông cáo (21 lần). Con số "100 lần" hay trích **không thấy** trong thông cáo. Không có báo cáo gốc công khai.
3. **Case study BĐS chính thức của Meta** (AX Capital, Casagrand, Mahindra trên facebook.com/business/success) **đã bị gỡ (404)**. Chỉ còn bản agency đăng lại. Ca Úc (Plezzel/CoreLogic) cũng đã gỡ.
4. **Quy định nội bộ của Vinhomes và CĐT lớn với đại lý** về quảng cáo, đặt tên page: không có văn bản công khai.
5. **Chi phí mỗi lead đất nền tỉnh ở VN:** không có số đáng tin. Phải đo ở tuần 1.
6. Mức **200 lead/tháng** và **độ phủ 60%** là "nên đạt" hay chặn cứng khi bật mục tiêu khách chất lượng: tài liệu ghi là hướng dẫn. Cách nối Google Sheets/Leads Center có được tính là "đã nối CAPI" theo quy định 04/2026 không: rất có thể có, nhưng cần xem trong trình quản lý quảng cáo.
7. **Form Higher intent + OTP** có bật được cho tài khoản VN không: Việt Nam không nằm trong danh sách bị loại trừ, nhưng cần kiểm trên giao diện thật.
8. Sau sáp nhập tỉnh 07/2025, **Meta lưu ranh giới "Bắc Ninh" và tên xã mới thế nào**: chưa kiểm.
9. **Miễn hoặc ân hạn 5 năm cho doanh nghiệp nhỏ** (Luật 91/2025 Điều 38) có gồm hồ sơ chuyển dữ liệu ra nước ngoài (Điều 20) không. Tải danh sách khách lên Meta có bị tính là chuyển xuyên biên giới không: **cần luật sư**.
10. **NĐ 87/2026/NĐ-CP và NĐ 356/2025/NĐ-CP:** chưa đọc văn bản gốc. thuvienphapluat.vn có lớp kiểm tra chống bot nên tôi không vượt qua; mức phạt lấy từ báo.
11. Các điều luật đọc qua bản chép (hethongphapluat, caselaw, VCCI), không phải Công báo. Trang Cơ sở dữ liệu quốc gia (vbpl.vn) không tải được toàn văn.

---

## 6. Danh sách nguồn (đã đọc)

**Meta: trợ giúp, sản phẩm, kỹ thuật**
- About instant form types: https://www.facebook.com/business/help/252352181957512
- Best practices to create lead ads: https://www.facebook.com/business/help/435270316658768
- Best practices to respond to leads: https://www.facebook.com/business/help/2246428158756947
- About performance goals for lead ads (thay đổi 04/2026, −21%): https://www.facebook.com/business/help/782657799338685
- Set up your CRM for qualified leads: https://www.facebook.com/business/help/279369167153556
- Connect Google Sheets … Conversions API for CRM: https://www.facebook.com/business/help/1095577538573756
- Leads Center (stages, Data sharing → Conversion leads): https://www.facebook.com/business/help/929596264178167
- SMS/OTP verification: https://www.facebook.com/business/help/898260175547909
- Conditional answers: https://www.facebook.com/business/help/154286325106161
- Custom disclaimer: https://www.facebook.com/business/help/1550411888622740
- About expired leads (90 ngày): https://www.facebook.com/business/help/1526849577619206
- Lead generation in Messenger/Instagram/WhatsApp: https://www.facebook.com/business/help/734075733714274
- Lead ads that click to message (−8% CPL, +48% reach): https://www.facebook.com/business/ads/ad-objectives/lead-generation/lead-ads-with-messaging
- Lead ads with calling: https://www.facebook.com/business/ads/ad-objectives/lead-generation/lead-ads-with-calling
- Advantage+ leads campaigns (−15%, +44%, −60% CPL, FAQ Advantage+ On): https://www.facebook.com/business/ads/meta-advantage-plus/leads
- About the learning phase: https://www.facebook.com/business/help/112167992830700
- Significant edits and learning phase: https://www.facebook.com/business/help/316478108955072
- About learning limited: https://www.facebook.com/business/help/269269737396981
- How to choose locations for your ad: https://www.facebook.com/business/help/365561350785642
- How to choose a Special Ad Category: https://www.facebook.com/business/help/298000447747885
- Reels ads (2×, −34,5%): https://www.facebook.com/business/ads/facebook-instagram-reels-ads
- Tailored campaigns (luật 3 giây, người thật, chỉ tuổi + vị trí): https://www.facebook.com/business/ads/automation/tailored-campaigns
- AI innovations in Meta's ad ranking (Andromeda +8%): https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance
- Customer List Custom Audiences Terms: https://www.facebook.com/legal/terms/customaudience
- Pages, groups and events policies: https://www.facebook.com/policies_center/pages_groups_events
- Conversions API for CRM integration: https://developers.facebook.com/docs/marketing-api/conversions-api/conversion-leads-integration
- CRM integration – Verify your data (200 lead/tháng, 60%): https://developers.facebook.com/documentation/ads-commerce/conversions-api/conversion-leads-integration/crm-integration/4-verify-your-data
- Special Ad Category (Marketing API): https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category
- Video ads remarketing: https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/videoads
- Meta Andromeda (engineering, 02/12/2024): https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/
- Thư viện quảng cáo Meta (quan sát 15/10/2026): https://www.facebook.com/ads/library/

**Case study và nghiên cứu quốc tế**
- WhatsApp Business – Lomas de Angelopolis: https://whatsappbusiness.com/resources/success-stories/lomas-de-angelopolis/
- WhatsApp Business – Engelife: https://whatsappbusiness.com/resources/success-stories/engelife-construtora-e-incorporadora/
- WhatsApp Business – DAMAC: https://whatsappbusiness.com/resources/success-stories/damac-properties/
- Make – D&B Properties: https://www.make.com/en/success-stories/transform-lead-management-make-meta-technologies
- Social Beat – Mahindra Lifespaces (thứ cấp): https://www.socialbeat.in/blog/mahindra-lifespaces-case-study/
- Social Beat – Casagrand (thứ cấp): https://www.socialbeat.in/blog/casagrand-case-study-published-by-facebook/
- Sell.do – paid lead generation India 2026 (nhà bán phần mềm): https://www.sell.do/blog/paid-lead-generation-real-estate-india-2026
- HBR 2011 (tóm tắt): https://hbr.org/2011/03/the-short-life-of-online-sales-leads · BYU: https://scholarsarchive.byu.edu/facpub/9711 · SmartCompany (thứ cấp): https://www.smartcompany.com.au/marketing/20110704-are-you-letting-online-leads-go-cold/
- InsideSales/XANT 2007: https://www.insidesales.com/xant-com-research-stuns-2007-marketing-sherpa-b2b-summit
- DataReportal – Digital 2026 Vietnam: https://datareportal.com/reports/digital-2026-vietnam

**Pháp luật Việt Nam** (bản chép điều luật hoặc tin chính thống)
- Luật KDBĐS 29/2023 (toàn văn): https://caselaw.vn/van-ban-phap-luat/411479-luat-kinh-doanh-bat-dong-san-so-29-2023-qh15-ngay-28-11-2023-cua-quoc-hoi · Điều 6: https://hethongphapluat.com/luat-kinh-doanh-bat-dong-san-2023/dieu-6 · Điều 8: https://hethongphapluat.com/luat-kinh-doanh-bat-dong-san-2023/dieu-8
- Hiệu lực 01/08/2024 (Luật 43/2024): https://luatvietnam.vn/dat-dai-nha-o/tong-hop-van-ban-ve-dat-dai-nha-o-co-hieu-luc-thang-8-2024-567-98648-article.html
- NĐ 96/2024/NĐ-CP (VCCI): https://vcci.com.vn/legal-document/96-2024-nd-cp
- Luật Quảng cáo Điều 8: https://hethongphapluat.com/luat-quang-cao-2012/dieu-8 · Luật 75/2025: https://luatvietnam.vn/linh-vuc-khac/diem-moi-cua-luat-quang-cao-sua-doi-2025-883-102813-article.html · TT 12/2026: https://luatvietnam.vn/tin-van-ban-moi/tai-lieu-chung-minh-de-quang-cao-duoc-su-dung-cac-tu-nhat-duy-nhat-tot-nhat-so-mot-186-109322-article.html · NĐ 87/2026 (thứ cấp): https://doanhnghiephoinhap.vn/tu-1552026-siet-manh-vi-pham-quang-cao-muc-phat-cao-nhat-toi-100-trieu-dong-132411.html
- Luật BVDLCN 91/2025: Điều 7 https://hethongphapluat.com/luat-bao-ve-du-lieu-ca-nhan-2025/dieu-7 · Điều 8 …/dieu-8 · Điều 9 …/dieu-9 · Điều 20 …/dieu-20 · Điều 28 …/dieu-28 · Điều 38 …/dieu-38 · Hà Tĩnh: https://hatinh.gov.vn/vi/bai-viet/luat-bao-ve-du-lieu-ca-nhan-chinh-thuc-co-hieu-luc-thi-hanh-tu-ngay-112026
- NĐ 147/2024: https://hatinh.gov.vn/vi/bai-viet/tu-hom-nay-tai-khoan-mang-xa-hoi-phai-xac-thuc-so-dien-thoai-moi-duoc-dang-bai

**Báo chí và cộng đồng nghề Việt Nam**
- LSVN – Vinhomes và các thương hiệu bị giả mạo (12/2024): https://lsvn.vn/canh-bao-hanh-vi-gia-mao-website-doanh-nghiep-nham-lua-dao-chiem-doat-tai-san-a151452.html
- LSVN – UBCTQG khuyến cáo quảng cáo BĐS (07/2025): https://lsvn.vn/can-trong-voi-quang-cao-sai-su-that-ve-du-an-bat-dong-san-a161016.html
- Diễn đàn Doanh nghiệp – NOXH NO1 Hạ Đình (05/2025): https://diendandoanhnghiep.vn/ha-noi-canh-giac-chieu-tro-gia-mao-lua-dao-mua-ban-can-ho-du-an-nha-o-xa-hoi-no1-10154913.html
- Nhà Đầu tư – Vịnh An Hoà (04/2021): https://nhadautu.vn/mao-danh-chu-dau-tu-de-giao-dich-bat-dong-san-vinh-an-hoa-trai-phep-d50724.html
- VnExpress – "Giữa đường đứt gánh" (Cocobay, 12/2019): https://vnexpress.net/giua-duong-dut-ganh-4020679.html
- VnExpress – rủi ro gói vay lãi thấp (05/2026): https://vnexpress.net/chuyen-gia-canh-bao-rui-ro-goi-vay-mua-nha-lai-suat-thap-5070777.html · Hoang Huy New City, bài tài trợ (04/2026): https://vnexpress.net/hoang-huy-new-city-ap-dung-chinh-sach-0-lai-suat-trong-3-nam-5060306.html
- Ads Uploader – Facebook instant form (06/2026, bên thứ ba): https://adsuploader.com/blog/facebook-instant-form
- Tuổi Trẻ – dữ liệu khách hàng BĐS bị đánh cắp (09/2022): https://tuoitre.vn/bi-danh-cap-du-lieu-khach-hang-doanh-nghiep-bat-dong-san-bao-mat-ra-sao-2022091514474369.htm
- Brands Vietnam – Cẩm nang quảng cáo BĐS (03/2026, ý kiến người làm nghề): https://www.brandsvietnam.com/congdong/topic/cam-nang-toan-tap-chien-luoc-quang-cao-bat-dong-san-thuc-chien
