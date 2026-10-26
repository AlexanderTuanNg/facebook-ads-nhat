# Học từ nhóm Facebook (nick David Nguyễn) → đưa vào quảng cáo — 20/10/2026

> Chỉ đọc dữ liệu đã lưu: `data/marketing.db` (mở chế độ chỉ đọc), `content/**/*.md`, `data/lich_dang_*.log`, `data/doc_group_20261011_2149.jsonl`, `data/tim_khach_20261011_2136.jsonl`, các file research/reports nêu ở từng mục. Không mở Facebook, không ghi DB. Không ghi tên, SĐT khách.
> Khoảng thời gian: 26/09 → 20/10/2026 (bỏ 3 bài thử ngày 25/09). Nhãn: [DỮ LIỆU] = đếm từ file/DB · [NGUỒN] = tài liệu đã có · [GIẢ THUYẾT] = suy luận hoặc mẫu quá nhỏ.

## Tóm tắt 8 dòng
1. 25 ngày, **203 bài** vào **79 nhóm**: 122 công khai · 64 chờ quản trị duyệt · 7 lỗi · 6 bị gỡ · 4 bỏ qua. 47 nhóm có ít nhất 1 bài công khai. [DỮ LIỆU]
2. Kết quả rất mỏng: **24 lượt tương tác ghi được** (22 người thích, 2 bình luận thật, thêm 2 bình luận rác). **1 người để lại SĐT** (07/10, vẫn ở trạng thái `new`). **0 cuộc gọi nào được ghi theo mã lead.** [DỮ LIỆU]
3. Tương tác giảm dần theo tuần: 0,41 → 0,19 → 0,08 lượt/bài công khai. Tỉ lệ bài phải chờ duyệt tăng từ 18% lên 46%. [DỮ LIỆU] Nguyên nhân (nick bị hạ uy tín, lặp ảnh) là [GIẢ THUYẾT].
4. Vùng có phản hồi theo bài: **Bố Hạ** và **Hữu Lũng** (~0,5–0,6 lượt/bài), hơn hẳn Yên Thế lõi (0,15). **Tân Yên** 23 bài công khai: 0. **KCN** 10 bài, 1 bài công khai, 0. [DỮ LIỆU, mẫu nhỏ → GIẢ THUYẾT]
5. Câu mở chạm được: **chuyện gia đình** ("Con dẫn người yêu về ra mắt?" 6 thích; "Hai vợ chồng cùng ưng mới mua" 3 thích). Hai bình luận thật đến từ bài **flycam đi một vòng** (hỏi "đã có sổ chưa") và bài **quảng trường buổi tối** (để lại SĐT). [DỮ LIỆU, mẫu nhỏ]
6. Ảnh **lễ trao sổ** dùng cho 96 bài nhưng ra ít nhất: 4 tương tác/54 bài công khai. Ảnh **buổi tối** ra nhiều nhất: 9/24. [DỮ LIỆU, bị lẫn yếu tố thời gian → GIẢ THUYẾT]
7. So kênh: nhóm 25 ngày ≈ 1 SĐT. QC Meta 6 ngày, 2,43 tr → **63 cuộc trò chuyện** (Video Mới 27.066đ/cuộc). Nhóm nên là nơi **thử câu chữ miễn phí**, không phải kênh ra khách chính. [DỮ LIỆU]
8. Việc nên làm trước tiên: (a) gọi ngay người để lại SĐT ngày 07/10; (b) quảng cáo thử góc "gia đình + buổi tối + có sổ", thêm 1 nhóm QC nhắm vành đai Bố Hạ–Hữu Lũng–Yên Thế; (c) ngừng đăng vào 20 nhóm chưa từng cho bài hiện. [GIẢ THUYẾT, chờ "ok"]

---

## 1. Đã đăng bao nhiêu, ở đâu

### 1a. Theo trạng thái [DỮ LIỆU: bảng `posts`, trạng thái lúc đăng]
| Trạng thái | Bài | Nhóm |
|---|---|---|
| Công khai (`published`) | 122 | 47 |
| Chờ quản trị duyệt (`pending_approval`) | 64 | 32 |
| Lỗi khi đăng (`failed`) | 7 | 7 |
| Bị gỡ (`removed`) | 6 | 6 |
| Bỏ qua (`skipped`) | 4 | 4 |
| **Cộng** | **203** | **79 nhóm khác nhau** |
Còn 12 bài `approved_human` chưa tới giờ (4 bài tối 20/10, 8 bài 21/10).

Lưu ý: "chờ duyệt" lúc đăng không có nghĩa là không bao giờ hiện. Ít nhất 2 bài chờ duyệt sau đó có người thích (bài 82, bài 39).

### 1b. Theo vùng nhóm (phân loại theo tên nhóm)
| Vùng | Bài | Công khai | Chờ duyệt | Lỗi/gỡ/bỏ | Nhóm | Thích | BL thật | Tương tác / bài công khai |
|---|---|---|---|---|---|---|---|---|
| Yên Thế lõi (Yên Thế, Đồng Kỳ, Xuân Lương, Mỏ Trạng, Cầu Gồ) | 72 | 48 | 17 | 7 | 23 | 6 | 1 | 0,15 |
| Tân Yên – Nhã Nam – Cao Thượng | 41 | 23 | 16 | 2 | 14 | 0 | 0 | **0** |
| Nhóm BĐS cả tỉnh Bắc Giang (36k–203k) | 28 | 19 | 8 | 1 | 10 | 2 | 0 | 0,11 |
| Bố Hạ | 25 | 17 | 3 | 5 | 8 | 9 | 0 | **0,53** |
| Hữu Lũng – Lạng Sơn | 19 | 10 | 8 | 1 | 17 | 5 | 1 | **0,60** |
| KCN (Đình Trám, KCN Hữu Lũng…) | 10 | 1 | 8 | 1 | 4 | 0 | 0 | 0 |
| Quế Võ (đồng hương xa) | 5 | 4 | 1 | 0 | 2 | 0 | 0 | 0 |
| Chợ online tổng hợp / Việt Yên | 3 | 0 | 3 | 0 | 2 | 0 | 0 | — |
| **XKLĐ / người cao tuổi** | **0** | — | — | — | **0 nhóm đã vào** | — | — | chưa thử |
Thêm: đã vào **17 nhóm KCN** (9 nhóm Việt Yên–Quang Châu 37k–121k) nhưng mới đăng ở 4 nhóm. [DỮ LIỆU: bảng `groups`]

### 1c. Theo loại nhóm
| Loại | Bài | Công khai | Thích + BL thật | Tương tác / bài công khai |
|---|---|---|---|---|
| Nhóm chợ / cộng đồng | 129 | 75 | 19 | 0,25 |
| Nhóm nhà đất / BĐS | 74 | 47 | 5 | 0,11 |

### 1d. Theo tuần [DỮ LIỆU]
| Tuần | Bài | Công khai | % chờ duyệt | Tương tác | Tương tác / bài công khai |
|---|---|---|---|---|---|
| 26–28/09 | 12 | 9 | 18% | 0 | 0 (chưa có công cụ đếm) |
| 29/09–05/10 | 45 | 32 | 20% | 13 | **0,41** |
| 06–12/10 | 85 | 48 | 38% | 9 | 0,19 |
| 13–19/10 | 49 | 25 | 46% | 2 | 0,08 |
| 20/10 | 12 | 8 | 33% | — | không đo (công cụ đếm đã tắt) |

### 1e. Bài còn hiện không? (kiểm lại bài cũ) [DỮ LIỆU: bảng `metrics`]
- 138 lần kiểm 121 bài. Từ 01/10 trở đi, **gần như mọi lần kiểm đều "không thấy"** (108 lần `not_found`, chỉ 1 lần thấy bài).
- Công cụ tìm 40 chữ đầu bài trong mục "nội dung của bạn" của nhóm. "Không thấy" có thể là bài bị gỡ/ẩn, **hoặc** cách kiểm bị hỏng. Chưa phân biệt được. [GIẢ THUYẾT] Đây là lỗ hổng lớn nhất của dữ liệu nhóm.

## 2. Cái gì có tương tác — xếp hạng

Cách đếm: mỗi người thích/bình luận được ghi 1 lần vào `leads` (công cụ đọc tương tác chạy 05/10–18/10). Người đã có trong sổ không được ghi lại → số thật có thể cao hơn. Mẫu tổng chỉ 24 lượt → **mọi xếp hạng dưới đây là [GIẢ THUYẾT]**.

### 2a. Bài có tương tác (15 bài / 203)
| Hạng | Bài | Ngày, giờ | Nhóm (vùng) | Góc | Câu mở (dòng 1) | Thích | BL |
|---|---|---|---|---|---|---|---|
| 1 | 55 | 02/10 sáng | CHỢ BỐ HẠ 61k (Bố Hạ) | 3 – lo đất cho con | 🏡 CON DẪN NGƯỜI YÊU VỀ RA MẮT? CÓ LÔ CHỈ KHOẢNG 1 TỶ | 6 | 0 |
| 2 | 82 | 06/10 tối | CHỢ MẸT Hữu Lũng 37k | 2 – hai vợ chồng | 🏡 HAI VỢ CHỒNG CÙNG ƯNG MỚI MUA: CÓ LÔ CHỈ KHOẢNG 1 TỶ | 3 | 0 |
| 3 | 84 | 06/10 tối | Chợ Bắc Lệ–Tân Thành, Hữu Lũng 30k | 5 – quảng trường tối | 📍 TRẺ CON RA QUẢNG TRƯỜNG MỖI TỐI… | 1 | **1 (để lại SĐT)** |
| 4 | 59 | 02/10 chiều | BĐS YÊN THẾ 6k (Yên Thế) | 6 – flycam một vòng | 📍 BAY MỘT VÒNG XEM ĐẤT, TRONG KHU CÓ LÔ… | 1 | **1 (hỏi đã có sổ chưa)** |
| 5 | 20 | 28/09 tối | Yên Thế Online 98k | tin rao v3 | 🔥 CHỈ KHOẢNG 1 TỶ LÀ CÓ MỘT LÔ Ở TRUNG TÂM XÃ YÊN THẾ | 2 | 0 |
| 6–15 | 39, 47, 66, 81, 116, 127, 137, 150, 177 | | Bắc Giang 193k, 141k; Người Yên Thế; Chợ Bố Hạ ×3; Nhà đất Hữu Lũng; Yên Thế Online 13k; Người Yên Thế ✅ | 1, 4, 5, 6, 11, 12, 14… | "Tối có quảng trường cho cháu chơi", "Tết về quê nhà ông bà chật chỗ", "Hàng xóm rủ nhau mua cạnh nhau", "Đang ở Nhật?"… | 1 mỗi bài | 0 |
| — | 124, 128 | 10/10 | Mỏ Trạng, Chợ Yên Thế Online | 9, 4 | — | 0 | 1 rác mỗi bài (quảng cáo sửa tivi) |

### 2b. Theo góc (`goc` trong file bài)
| Góc | Bài | Công khai | Tương tác | Ghi chú |
|---|---|---|---|---|
| 3 – lo đất làm nhà cưới cho con | 7 | 2 | **6** | cả 6 từ 1 bài |
| 2 – hai vợ chồng cùng đi xem | 9 | 5 | 3 | 1 bài |
| 5 – tối cho con ra quảng trường | 20 | 12 | 3 (có 1 SĐT) | |
| 6 – flycam đi một vòng | 6 | 4 | 3 (có 1 câu hỏi sổ) | |
| 12 – người xã lân cận | 8 | 4 | 2 | |
| 1 rủ anh em · 4 Tết về quê · 14 đồng hương xa | 9 · 7 · 11 | 8 · 4 · 8 | 1 · 1 · 1 | |
| 11 – CĐT dẫn đi xem (phần lớn là bài trao sổ) | 37 | 27 | 1 | dùng nhiều nhất, ra ít nhất |
| 7, 8, 9, 10, 13 (công nhân KCN), 15 (ông bà để đất) | 48 | 26 | **0** | |
| Bài chưa gắn góc (tin rao v1–v4) | 40 | 26 | 3 | |

### 2c. Theo ảnh, số ảnh, khung giờ, phiên bản
| Yếu tố | Nhóm | Bài (công khai) | Tương tác | / bài công khai |
|---|---|---|---|---|
| Loại ảnh | Có ảnh buổi tối | 31 (24) | 9 | **0,38** |
| | Chỉ flycam/ảnh khác | 76 (44) | 11 | 0,25 |
| | Có ảnh lễ trao sổ | 83 (48) | 4 | 0,08 |
| | Trao sổ + buổi tối | 13 (6) | 0 | 0 |
| Số ảnh | 3 ảnh | 69 (41) | 14 | 0,34 |
| | 4 ảnh | 110 (69) | 10 | 0,14 |
| | 1 ảnh / 5 ảnh | 20 (12) | 0 | 0 |
| Khung giờ | Tối 18–22h | 56 (36) | 11 | **0,31** |
| | Sáng 6–11h | 55 (41) | 9 | 0,22 |
| | Chiều 14–18h | 50 (27) | 4 | 0,15 |
| | Trưa 11–14h | 42 (18) | 0 | **0** (và 48% phải chờ duyệt) |
| Phiên bản bài | v5 (01–03/10, góc sáng tạo) | 24 (18) | 10 | **0,56** |
| | v6 (06/10 trở đi) | 105 (54) | 9 | 0,17 |
| | Bài trao sổ (TS) | 34 (24) | 2 | 0,08 |
| Persona | cha mẹ mua cho con | 26 (18) | 9 | 0,50 |
Cảnh báo: ảnh trao sổ và bản v6 đều dùng từ 09/10, đúng lúc tương tác chung đang giảm → không tách được "do ảnh" hay "do thời điểm". [GIẢ THUYẾT]

### 2d. Cuộc gọi theo mã lead
**Không có số nào.** Không file nào ghi cuộc gọi/Zalo vào 0965 539 599 kèm mã (KC, TY, YT, BH…). Báo cáo 11/10 ghi "người nhắn mã lead: 0". [DỮ LIỆU: tìm trong workspace, log]

### 2e. Mốc so sánh: bài người khác trong cùng nhóm [DỮ LIỆU: `doc_group_20261011_2149.jsonl`, 218 bài, 14 nhóm, 11/10]
- 43 bài BĐS của người khác: trung vị 0, trung bình 0,2 lượt; 37/43 bài không có lượt nào. → Bài của mình (~0,2) **ngang mặt bằng**, không tệ hơn.
- Bài nhiều tương tác nhất trong nhóm là **câu hỏi cộng đồng thật** ("cho em hỏi…", tìm nhà xe, tìm thuê nhà về quê sống), không phải tin rao.
- Quét 20 nhóm tìm người cần mua (11/10): **1 bài "cần mua" / 15 bài "bán"**. Người mua gần như không tự đăng công khai. [DỮ LIỆU: `tim_khach_lan_dau.log`]

## 3. Lead từ nhóm (chỉ số đếm)
| Nguồn | Loại | Stage `new` | `contacted` | `qualified` / `viewing` / `won` |
|---|---|---|---|---|
| Bài nhóm (26 người) | Thích bài | 20 | 2 | 0 |
| | Bình luận thật (1 hỏi sổ, 1 để lại SĐT) | 2 | 0 | 0 |
| | Bình luận rác (quảng cáo dịch vụ) | 2 | 0 | 0 |
| Danh sách người dùng gửi 26/09 (33 người, không phải từ bài) | quan tâm dự án | 27 | 6 | 0 |
| **Cộng** | | **51** | **8** | **0** |
- Theo vùng nhóm của 26 người: Bố Hạ 9 · Hữu Lũng 6 · Yên Thế lõi 7 (2 rác) · nhóm BĐS tỉnh 2 · khác 2.
- Người để lại SĐT dưới bài 84 (07/10) **vẫn `new` sau 13 ngày**. Nick không nhắn được từ 11/10 → cần Phòng KD gọi. [DỮ LIỆU]
- Không lead nào từ nhóm đi tới hẹn xem hay cọc. [DỮ LIỆU]

## 4. Nhóm cho thấy gì về khách thật
| Điều thấy được | Căn cứ |
|---|---|
| Khách thật hỏi **sổ/pháp lý** trước tiên, sau đó giá, vay, ai dẫn đi xem | [DỮ LIỆU] bình luận bài 59; lead 12 (sổ), lead 17 (giá); `kich-ban-nhan-tin-lead.md` §D |
| Chạm được là **khoảnh khắc gia đình**: con cưới, hai vợ chồng cùng ưng, trẻ con chơi buổi tối | [DỮ LIỆU nhỏ] mục 2a, persona "cha mẹ mua cho con" 0,50/bài |
| Vành đai **Bố Hạ, Hữu Lũng** phản hồi tốt hơn chính Yên Thế, Tân Yên | [DỮ LIỆU nhỏ] mục 1b. Khớp với dữ liệu 103 khách đã mua: truyền miệng theo cụm làng **Bố Hạ, Vân Nham (Hữu Lũng)**, Thổ Hà [NGUỒN: `research/khach-da-mua.md`] |
| Người đã mua: **76% Bắc Giang cũ**, 8% Bắc Ninh cũ, 8% Hà Nội; 88% đã kết hôn, vợ cùng quyết | [NGUỒN: `khach-da-mua.md`] |
| Công nhân KCN, đồng hương xa: **chưa có tín hiệu** nào từ nhóm (KCN 0/10 bài, góc 13 = 0, góc 14 = 1 thích) | [DỮ LIỆU] — chưa đủ để kết luận "không chạm", vì 8/10 bài KCN phải chờ duyệt |
| Câu "báo mã XX" chưa ai dùng; người ở quê ít bình luận, ít nhắn người lạ | [DỮ LIỆU] 0 mã được báo; [GIẢ THUYẾT] lý do |
| Ảnh trao sổ làm bằng chứng thì tốt, nhưng làm câu mở/ảnh bìa thì không kéo người dừng lại | [GIẢ THUYẾT] mục 2c |

## 5. Đưa vào quảng cáo

Mọi câu chữ dưới đây là **khung để thử**. Trước khi chạy phải qua lint + compliance (câu pháp lý F5 nguyên văn, dòng (*), không "nhất", không "sổ đỏ cầm tay", không hứa tăng giá). Mọi khoản tiêu mới chờ người dùng "ok".

### 5a. 6 giả thuyết nội dung nên thử
| # | Góc | Câu mở gợi ý | Định dạng | Căn cứ |
|---|---|---|---|---|
| H1 | Lo đất cho con trước khi con cưới | "Con dẫn người yêu về ra mắt rồi. Bố mẹ đã lo được mảnh đất cho con chưa?" | Video 30–45 giây: cảnh khu đất ban ngày → quảng trường tối | [DỮ LIỆU nhỏ] bài 55: 6 thích, cao nhất. Khớp nhóm "cha mẹ mua cho con" [NGUỒN] |
| H2 | Buổi tối quảng trường, trẻ con chơi | "Tối nào trẻ con trong khu cũng ra quảng trường chơi." | Video dọc 15–30 giây quay buổi tối thật (cần quay thêm) | [DỮ LIỆU nhỏ] ảnh đêm 0,38/bài; người duy nhất để lại SĐT đến từ bài này |
| H3 | Hỏi – đáp "Đã có sổ chưa?" | "Câu anh chị hay hỏi em: đất có sổ chưa?" (không dùng chữ "nhất") | Video người thật của Phòng KD trả lời 4 câu: sổ (câu F5), giá, vay, ai dẫn đi xem | [DỮ LIỆU] câu hỏi thật đầu tiên dưới bài là về sổ |
| H4 | Hai vợ chồng cùng ưng | "Vợ ưng, chồng ưng thì mới xuống tiền." | Ảnh băng chuyền (carousel) 3–4 ảnh hoặc video hai người đi xem | [DỮ LIỆU nhỏ] bài 82: 3 thích; [NGUỒN] 88% đã kết hôn |
| H5 | Đi một vòng bằng flycam | "Bay một vòng xem khu đất trước khi anh chị về tận nơi." | Video flycam 40–60 giây, chữ chú thích trên hình | [DỮ LIỆU nhỏ] bài 59 có câu hỏi sổ; [NGUỒN] mẫu đất nền chạy lâu là video 40–90 giây |
| H6 | Rủ anh em, hàng xóm mua cạnh nhau | "Anh em, hàng xóm mua cạnh nhau, sau này sang chơi chỉ vài bước." | Flycam dãy lô liền nhau | [DỮ LIỆU nhỏ] 1 thích ở Chợ Bố Hạ; [NGUỒN] truyền miệng theo cụm làng |
Thử thế nào: giữ "Video Mới" làm mẫu đối chứng. Thêm 2–3 mẫu (H1, H2, H3 trước) vào **cùng một nhóm quảng cáo**, để so được với nhau. So bằng **số người cho SĐT/Zalo**, không chỉ giá/cuộc trò chuyện. [GIẢ THUYẾT]

### 5b. Vùng và đối tượng
| Gợi ý | Căn cứ |
|---|---|
| Thêm 1 nhóm quảng cáo nhắm **vành đai dự án**: Yên Thế, Bố Hạ, Hữu Lũng (Lạng Sơn), Nhã Nam. Video Mới hiện **không phủ vùng dự án** (2 vòng 16 km ở TP Bắc Giang cũ + VSIP Từ Sơn) | [DỮ LIỆU] nhóm Bố Hạ/Hữu Lũng phản hồi tốt nhất; [NGUỒN] 76% người mua ở Bắc Giang cũ; báo cáo Meta 20/10 §3d |
| Chỉ chọn "người sống ở đây", bỏ Hoa Kỳ (đã có trong tin gửi người chạy QC) | [NGUỒN] `reports/2026-10-20-doc-so-meta-ads.md` |
| Tuổi 35–60, cả nam và nữ; câu chữ nói với "anh chị", "hai vợ chồng", "bố mẹ" | [NGUỒN] 88% đã kết hôn; [DỮ LIỆU nhỏ] persona cha mẹ 0,50/bài |
| Vòng VSIP Từ Sơn / KCN: **giữ để đo, chưa mở rộng**. Trong 38 cuộc trò chuyện, cần đếm ai ở vùng nào | [DỮ LIỆU] KCN trong nhóm = 0; người mua Bắc Ninh cũ chỉ 8% [NGUỒN] |
| Tân Yên: không làm vùng riêng; để nằm trong vòng vành đai | [DỮ LIỆU] 23 bài công khai, 0 tương tác |
| Đồng hương xa (Hà Nội, Nhật/Hàn/Đài): để sau, khi đã có số SĐT từ vùng gần | [DỮ LIỆU] 1 thích ("Đang ở Nhật?"); [NGUỒN] Hà Nội chỉ 8% người mua |

### 5c. Nên DỪNG
| Dừng gì | Căn cứ |
|---|---|
| Dùng ảnh **lễ trao sổ** làm ảnh bìa hoặc câu mở. Giữ ảnh này ở cuối, làm bằng chứng | [GIẢ THUYẾT] 0,08 tương tác/bài, thấp nhất |
| Nói hai mức giá khác nhau giữa nhóm ("CHỈ DƯỚI 1 TỶ") và QC ("HƠN 1 TỶ", "500 TRIỆU") | [NGUỒN] báo cáo Meta 20/10 §6 — khách thấy cả hai sẽ thấy không khớp |
| Lấy lượt thích làm thước đo. Thước đo là SĐT/Zalo và lượt xem đất | [DỮ LIỆU] 22 lượt thích → 0 hẹn xem |
| Dựa vào "báo mã XX" để biết khách từ đâu. Thay bằng: người nghe máy hỏi "anh chị thấy tin ở đâu" | [DỮ LIỆU] 0 mã được báo |
| Mở rộng QC sang Quế Võ/Từ Sơn chỉ vì "nhiều lead" | [NGUỒN] lead Bắc Ninh 60–70% nhưng người mua chỉ 8% |

## 6. Đăng nhóm nên đổi gì (chỉ trong việc viết bài và đăng bài)
1. **Ngừng đăng vào 20 nhóm chưa từng cho bài hiện** (mọi bài đều phải chờ duyệt). Trong 8 bài ngày 21/10, **5 bài đi vào các nhóm này**: g21 Chợ Xuân Lương, g110 Chợ Mọc Cao Thượng, g292 KCN Hữu Lũng, g71 Tin Tức Bố Hạ, g70 Người Bắc Ninh (Bố Hạ; 1 chờ duyệt, 1 lỗi). Đổi sang nhóm hiện bài ngay và có phản hồi: Chợ Bố Hạ (g6, g16, g17, g74), Hữu Lũng (g283, g287, g298, g305), Yên Thế Online (g5, g38), BĐS Yên Thế (g7). [DỮ LIỆU]
2. **Ít bài hơn, đúng giờ hơn:** 8 → 4 bài/ngày (khớp đề xuất v2). Chỉ đăng **tối 18–22h** và **sáng 6–11h**. Bỏ khung trưa (0 tương tác, 48% chờ duyệt). [DỮ LIỆU nhỏ]
3. **Đổi nội dung:** ưu tiên góc 3, 2, 5, 6, 1 (gia đình, vợ chồng, buổi tối, flycam, anh em). Dùng 3 ảnh, có ảnh tối. Ảnh trao sổ để cuối. Giảm góc 11/13/15 và bài trao sổ lặp. Cuối bài vẫn hỏi một câu dễ trả lời. [GIẢ THUYẾT]
4. **Nhóm dùng để thử câu mở cho QC:** mỗi tuần thử 2–3 câu mở mới (H1–H6) ở các nhóm Bố Hạ/Hữu Lũng. Câu nào ra bình luận thật thì đưa vào mẫu QC. [GIẢ THUYẾT]
5. **Nếu vẫn muốn thử KCN:** dùng 9 nhóm KCN Việt Yên–Quang Châu đã vào mà chưa đăng (g539, g542, g544, g545, g546, g547, g549, g550, g556), thay cho 2 nhóm KCN Hữu Lũng luôn bắt chờ duyệt. Đăng thử 4 bài rồi xem có bài nào hiện không. [GIẢ THUYẾT]
6. **Hai việc người dùng làm (Claude không làm được):** (a) chuyển người để lại SĐT ngày 07/10 (lead 50) cho Phòng KD gọi; (b) dặn người nghe máy 0965 539 599 ghi mã hoặc nơi khách thấy tin. Ngoài ra, nếu muốn biết bài còn hiện không: tự mở mục "nội dung của bạn" ở 5 nhóm và xem bằng mắt (máy kiểm bài cũ đã tắt theo lệnh 20/10). [DỮ LIỆU]

## 7. Giới hạn dữ liệu
- **Cỡ mẫu rất nhỏ:** 24 lượt tương tác, 2 bình luận thật, 1 SĐT. Một bài (bài 55) chiếm 6/24 lượt. Mọi xếp hạng là [GIẢ THUYẾT].
- **Đếm thiếu:** bảng `metrics` không có số thích/bình luận (cột rỗng). Số tương tác lấy từ `leads` do công cụ ghi người thích/bình luận. Công cụ này chỉ chạy 05/10–18/10 và **không ghi lại người đã có trong sổ**. Bài từ 19/10 trở đi không đo.
- **Không biết bài còn hiện không:** từ 01/10, mọi lần kiểm bài cũ đều "không thấy". Có thể bài bị gỡ, cũng có thể máy kiểm hỏng.
- **Trạng thái "chờ duyệt" là lúc đăng.** Một số bài sau đó được duyệt; DB không cập nhật lại.
- **Không có số cuộc gọi/Zalo theo mã.** Không đo được kênh quan trọng nhất của nhóm.
- **Bị lẫn yếu tố thời gian:** ảnh trao sổ, bản v6, góc KCN đều dùng từ sau 09–14/10, đúng lúc tương tác chung giảm. Không tách được.
- **Vùng nhóm phân loại theo tên nhóm,** không phải theo nơi ở của người tương tác.
- Lead 1–33 là danh sách người dùng gửi, **không phải từ bài nhóm**. Đã tách riêng ở mục 3.
- Số QC Meta chỉ có 6 ngày, 2,43 tr. Chưa có số SĐT hay lượt xem đất từ QC. So sánh nhóm và QC ở đây chỉ là so sơ bộ.
