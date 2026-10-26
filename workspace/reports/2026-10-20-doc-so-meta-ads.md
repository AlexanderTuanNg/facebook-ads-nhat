# Đọc số Meta Ads (B7) — 20/10/2026 ~15:30

> Đọc qua kết nối chính thức của Meta (`meta-ads`, `https://mcp.facebook.com/ads`, nick Nam Lê, quyền `ads_read` + `ads_mcp_management`). **Chỉ đọc**: không tạo, sửa, dừng, xoá, không đổi ngân sách. Mọi đề xuất dưới đây **chờ người dùng "ok"**.
> Căn cứ: [DỮ LIỆU Meta API 20/10] trừ khi ghi khác. Ngưỡng theo skill `quang-cao-bds` §5–6; luật theo `compliance-checklist.md` §F, §G, §H.

## 1. Kết nối
- `meta-ads` (cấu hình user) = **connected, 97 công cụ**. Gồm công cụ đọc (`ads_get_*`, `ads_insights_*`, `ads_library_search`…) và công cụ ghi (`ads_create_*`, `ads_update_entity`, `ads_activate_entity`, xoá…). Quyền đã cấp chỉ có `ads_read` nên lệnh ghi dự kiến bị Meta từ chối [GIẢ THUYẾT, không thử].

## 2. Tài khoản quảng cáo truy cập được (6)
| ID | Tên | Danh mục doanh nghiệp | Trạng thái | Tiền tệ |
|---|---|---|---|---|
| 882171458271697 | BM Nam 1 | BM1. Via Edwin | ACTIVE | VND |
| 1186642645969813 | (không tên) | cá nhân | ACTIVE | VND |
| 191403964356477 | (không tên) | cá nhân | ACTIVE | **USD** |
| 548267276985638 | 258 | Hiếu 259 | ACTIVE | VND |
| 1776279733543978 | 2589 | Hiếu 259 | ACTIVE | VND |
| 1681137613104981 | Hiếu 259 | Hiếu 259 | ACTIVE | VND |

Cả 6 đều cho kết nối AI đọc (`is_ads_mcp_enabled`), đều có phương thức thanh toán.

## 3. Chiến dịch act_882171458271697 ("BM Nam 1", Trang "Bán đất Phân lô tại Bắc Giang")
Cửa sổ "14 ngày gần nhất" của Meta = 06/10–19/10 (không gồm hôm nay). Mọi chiến dịch bắt đầu từ 12/10 nên số **trọn đời** = 14 ngày + hôm nay.

### 3a. Số trọn đời (tới ~15:30 ngày 20/10)
| Chiến dịch | Trạng thái | Bắt đầu | Ngân sách/ngày | Chi tiêu | Hiển thị | Người xem | Tần suất | CPM | CTR (tất cả) | Cuộc trò chuyện | Giá/cuộc |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Yên thế Video Mới. | **ĐANG CHẠY** | 17/10 10:12 | 300.000đ | 1.028.524đ | 10.537 | 5.517 | 1,91 | 97.611đ | 5,29% | **38** | **27.066đ** |
| YT4 | Tạm dừng | 17/10 10:18 | 290.000đ | 218.267đ | 2.054 | 1.400 | 1,47 | 106.264đ | 4,77% | 4 | 54.567đ |
| yên thế 2 | Tạm dừng | 14/10 07:27 | 400.000đ | 1.184.986đ | 15.317 | 7.372 | 2,08 | 77.364đ | 4,90% | 21 | 56.428đ |
| Bài viết "Mùa Thu Vàng ." (đẩy bài) | Tạm dừng | 12/10 19:06 | 50.000đ | 49.588đ | 890 | 731 | 1,22 | 55.717đ | 27,64% | — (274 tương tác, 181đ/tương tác) | — |
| Bài viết "Mùa Thu chill chill" | Tạm dừng | 12/10 13:12 | 50.000đ | 0đ | 0 | — | — | — | — | — | — |
| **Cộng 3 chiến dịch tin nhắn** | | | | **2.431.777đ** | | | | | | **63** | **38.600đ** |

Hôm nay 20/10 (tới lúc đọc): Video Mới 183.240đ, 1.157 hiển thị, 4 cuộc → 45.810đ/cuộc (cao hơn trung bình, mới nửa ngày — chưa kết luận).

### 3b. Số 14 ngày (06–19/10) và chỉ số phụ
| Chiến dịch | Chi tiêu | Cuộc trò chuyện | Giá/cuộc | Nhấp liên kết → CTR liên kết | Xem ≥ 3 giây ÷ hiển thị | Người nhắn ≥ 3 tin | Meta ghi "khách tiềm năng" |
|---|---|---|---|---|---|---|---|
| Video Mới | 845.284đ | 34 | 24.861đ | 231 → **2,46%** | **31,4%** | 10 | 3 |
| YT4 | 218.267đ | 4 | 54.567đ | 46 → 2,24% | 28,3% | 1 | 1 |
| yên thế 2 | 1.184.986đ | 21 | 56.428đ | 248 → 1,62% | 25,8% | 5 | 3 |

"Khách tiềm năng" là số Meta tự ghi trong hộp thư (có thể do người trực đánh nhãn) — **chưa rõ cách ghi [CẦN XÁC NHẬN]**, không coi là "đã cho SĐT".

### 3c. Đối chiếu số Meta Business Suite trong STATE
| Chiến dịch | STATE (MBS) | Meta API | Kết luận |
|---|---|---|---|
| Yên thế Video Mới | 1.023.732đ / 38 | 1.028.524đ / 38 | **Khớp** (lệch +4.792đ = tiêu thêm sau lúc ghi STATE, cùng 38 cuộc) |
| YT4 | 218.267đ / 4 | 218.267đ / 4 | **Khớp** |
| yên thế 2 | 1.184.986đ / 21 | 1.184.986đ / 21 | **Khớp** |

Ngày bắt đầu: STATE ghi Video Mới "từ 16/10", "yên thế 2 (13/10)" — Meta ghi 17/10 và 14/10 (tên mẫu đặt 16/10, 13/10; chạy từ hôm sau).

### 3d. Cài đặt nhóm quảng cáo (so với skill §2a)
| Mục | Skill §2a | Đang cài | Đánh giá |
|---|---|---|---|
| Mục tiêu · điểm đến · tối ưu | Engagement → Messenger, tối ưu cuộc trò chuyện | Đúng (OUTCOME_ENGAGEMENT, MESSENGER, CONVERSATIONS) cả 3 | ✅ |
| Quốc gia | Không Mỹ/Canada/EU (§H10) | **Có "Hoa Kỳ"** trong vị trí của cả 3 chiến dịch tin nhắn. Đã tiêu ở Mỹ: **65.080đ**, 209 hiển thị, 1 cuộc (YT4) | ❌ CHẶN H10 |
| Vùng | Ghim dự án, bán kính 30 km | 2 vòng **16 km** mỗi chiến dịch. Video Mới: tâm TP Bắc Giang cũ (21,285; 106,206) + khu VSIP Từ Sơn, Bắc Ninh cũ (21,084; 105,997) — **vùng dự án Yên Thế không nằm trong** (cách tâm TP Bắc Giang ~22 km). YT4 và yên thế 2 có 1 vòng phía Yên Thế cũ (21,48; 106,18–106,19) | Lệch skill nhưng hợp nhóm khách "con làm KCN" của kế hoạch v2 — **đo, chưa sửa** [GIẢ THUYẾT]. Tên khu là ước theo toạ độ |
| Ai được nhắm | Chỉ "người sống ở đây" | "Sống ở đây" + "mới ở đây gần đây" + "hay lui tới" | ⚠️ Cây chẩn đoán §6b dòng "Khách ngoài vùng" |
| Mở rộng tự động | Bỏ tick "Reach more…" | Đối tượng Advantage+ bật, `expansion_all`, tự động tuổi/giới/vị trí = 1 | ⚠️ Cần mở Ads Manager xem có đang cho Meta nới vùng không [CẦN XÁC NHẬN] |
| Tuổi | 25–65+ | 25–65 (yên thế 2: 18–65) | ✅ |
| Lịch giờ | 7:00–21:00 | Không đặt lịch (chạy cả ngày, ngân sách ngày) | ⚠️ Tin nhắn ban đêm chờ tới sáng |
| Ngân sách | NỀN ~1,3 tr/tuần | Video Mới 300.000đ/ngày ≈ 2,1 tr/tuần | Cao hơn kế hoạch v2 (QC này không do hệ thống mình dựng) |
| Số mẫu | 1 nhóm, 3–5 mẫu khác góc | Mỗi chiến dịch 1 nhóm, 1 mẫu | Không so được mẫu trong cùng nhóm |
| Tên QC | `QC-<mã> \| <góc>` | Tên mặc định "Quảng cáo Lượt tương tác mới" | `doc_ads.py` không ghép được với sổ nguồn khách |
| Trang · tài khoản QC | Fanpage CĐT + TK QC doanh nghiệp (§H7) | Trang "Bán đất Phân lô tại Bắc Giang" (tài sản cá nhân), TK trong BM "Via Edwin" (người ngoài toàn quyền) | ❌ CHẶN H7 (đã biết, chờ chuyển danh mục) |

## 4. Đánh giá theo skill §5 (bảng ngưỡng) — chiến dịch đang chạy "Yên thế Video Mới"
| Chỉ số | Số đo | Ngưỡng §5 | Kết luận |
|---|---|---|---|
| Giá/cuộc nói chuyện (tín hiệu sớm) | 27.066đ (trọn đời) | Tốt ≤ 80k | **Tốt** — rẻ bằng ½ hai mẫu đã tắt [ngưỡng là GIẢ THUYẾT] |
| % để lại SĐT/Zalo | **Chưa đo** (Meta không đếm) | ≥ 40% | Thiếu — cần sổ nguồn khách |
| Giá/lượt xem đất (chỉ số chính) | **Chưa đo** | ≤ 0,8–1,5 tr | Thiếu — cần sổ nguồn khách |
| CTR liên kết | 2,46% | Tốt > 2% | **Tốt** |
| Giữ chân 3 giây | 31,4% | So giữa các mẫu | **Cao nhất** trong 3 mẫu (28,3%, 25,8%) |
| Tần suất | 1,91 sau ~4 ngày | < 2 | Tốt nhưng **sát ngưỡng**; 2 vòng 16 km + 300k/ngày → dễ vượt 2,5 trong 1 tuần [GIẢ THUYẾT] |
| CPM | 97.611đ | Tự đo | Mốc nền đầu tiên (quốc tế BĐS ~130k [NGUỒN THẤP]) |

Tổng chi cả tài khoản ~2,48 tr < 10 tr → **mọi kết luận là [GIẢ THUYẾT]** (skill §5).

## 5. Luật §6 và cây chẩn đoán
- **§6a — Video Mới:** tiêu 1,03 tr < 3 tr → **CHỜ / GIỮ** (không có cảnh báo: đã có 38 cuộc). Không đủ điều kiện TĂNG (chưa có số lượt xem đất).
- **YT4, yên thế 2:** giá/cuộc gấp đôi Video Mới → để tắt là đúng. "yên thế 2" còn vi phạm sàn cứng (mục 6) → **không bật lại**.
- **§6b — bậc đầu tiên hỏng:** "Khách ngoài vùng" (nhắm cả Mỹ + "mới ở đây gần đây"). Bậc tiếp theo cần số: "Nhiều tin nhắn, ít người cho số?" — chưa biết vì chưa có sổ nguồn khách.
- **§6c:** chưa đọc được trạng thái "Learning" (Meta không trả `learning_stage_info` lần này). Đã qua 72 giờ đầu (từ 17/10 10:12) → sửa bây giờ không phạm "48–72 giờ đầu", nhưng **mỗi lần sửa là học lại** → gom mọi sửa vào 1 lần.

## 6. Soát nội dung mẫu (checklist §F, §G, §H)
### Mẫu ĐANG CHẠY (Video Mới, creative 2188265765441845, nút "Gửi tin nhắn")
Mở đầu: "CHỈ 500 TRIỆU – SỞ HỮU LÔ ĐẤT HƠN 1 TỶ, SỔ ĐỎ CẦM TAY, XÂY NHÀ NGAY!"

| Câu trong mẫu | Mục | Mức | Cách sửa |
|---|---|---|---|
| Không có dòng **(*)** dù có 500 triệu, 1 tỷ, 5 công viên, 1,5km | **H8** (sàn cứng skill §0) | **CHẶN** | Thêm cuối bài: "(*) Thông tin theo chính sách của Chủ đầu tư tại thời điểm đăng, áp dụng có điều kiện; khoảng cách là ước tính." |
| "✅ Hạ tầng đồng bộ, **cam kết 100% dự án KHÔNG CÓ CỎ!**" | §B (tuyệt đối hoá, không kiểm chứng) + F2 "cam kết" | **Bỏ câu** | "✅ Hạ tầng đã làm xong, đường trong khu đã trải nhựa" (nếu đúng thực tế) [CẦN XÁC NHẬN] |
| "Cách CCN Tân Sỏi và Công ty May LGG chỉ khoảng **1,5km**" | H8 + B1 (khoảng cách chưa có trong brief) | CHẶN tới khi có (*) + xác nhận | Giữ câu (gắn khách làm KCN), thêm (*); CĐT xác nhận 1,5km |
| "CHỈ 500 TRIỆU – SỞ HỮU LÔ ĐẤT **HƠN 1 TỶ**", "Tài chính **chỉ từ** 500 TRIỆU" | F1 (chỉ được KM7/KM7b) + §2b dòng 1 ("trả trước 500 triệu" cần Quyết định chính sách có số) | CHẶN theo checklist; là **quyết định kinh doanh** | Nếu CĐT đã có QĐ chính sách 500 tr → giữ, thêm (*). Lưu ý: bài nhóm đang nói "CHỈ DƯỚI 1 TỶ" (KM7b), QC nói "HƠN 1 TỶ" → 2 thông điệp giá ngược nhau |
| "SỔ ĐỎ **CẦM TAY**" | F2 (biến thể cụm cấm "sổ đỏ trao tay") | CHẶN | "Đã có sổ đỏ từng lô" |
| "pháp lý rõ ràng" | F5 (chỉ dùng câu chuẩn) + thiếu dòng PL (PL còn KHOÁ) | CHẶN | "Đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô" |
| "Các hộ dân đã xây nhà, **kinh doanh buôn bán**" | KM3 (phần kinh doanh còn KHOÁ) | Góp ý | "Các hộ dân đã về xây nhà ở" |
| "📲 **Gọi ngay** 0948.903.888" (nút lại là "Gửi tin nhắn") | KM5 dùng 0965 539 599; chữ bảo gọi, nút bảo nhắn | Góp ý | Xác nhận số 0948.903.888 là của Phòng KD CĐT; đổi chữ thành "Bấm Gửi tin nhắn hoặc gọi …" |
| Chạy từ Trang "Bán đất Phân lô tại Bắc Giang" | H7 | CHẶN (đã biết) | Chuyển sang Fanpage CĐT khi đổi danh mục |

### Hai mẫu đã TẠM DỪNG (để tham khảo, không bật lại)
- **YT4** (2434415583754734): "500 TRIỆU TRONG TAY – … HƠN 1 TỶ", "SỔ ĐỎ CẦM TAY", "Pháp lý rõ ràng", "đầu tư dài hạn", "khoảng 1,5km" không có (*). Không có câu "cam kết 100%".
- **yên thế 2** (2201171844161778): "Chỉ từ **1,180 tỷ** … lô đất 90m²" rồi cuối bài "**chỉ từ 1,2 tỷ**" (2 con số giá khác nhau), "**tiềm năng tăng giá**" (H4 — sàn cứng), "**Sổ đỏ trao tay**" (F2), "kinh doanh **sầm uất**" (KM3 KHOÁ), "mặt tỉnh lộ 292", "mặt đường 15,5m" chưa có (*).

## 7. Đề xuất (CHỜ "ok", chưa đụng gì)
1. **GIỮ "Yên thế Video Mới" chạy**, không tăng tiền — rẻ nhất (27k/cuộc), luật §6a: tiêu < 3 tr → chờ.
2. **Sửa gộp 1 lần** (để Meta chỉ học lại 1 lần), người đang quản lý quảng cáo làm trong Ads Manager: (a) bỏ "Hoa Kỳ" khỏi vị trí; (b) chỉ để "người sống ở đây"; (c) thay nội dung bằng bản có dòng (*), bỏ "cam kết 100%…", "sổ đỏ cầm tay" → "đã có sổ đỏ từng lô". Thay nội dung = bài mới, mất số tương tác cũ của bài — chấp nhận được vì mới 4 ngày.
3. **Đo chất lượng (quan trọng nhất cho bán hàng):** người trực tin nhắn Trang "Bán đất Phân lô" đếm trong 38 cuộc trò chuyện: bao nhiêu người cho SĐT/Zalo, bao nhiêu hẹn/đã đi xem đất → ghi sổ nguồn khách (§4). Chỉ khi có số này mới quyết TẮT/GIỮ/TĂNG theo §6a.
4. Giữ tắt YT4 và "yên thế 2".
5. (Đã có trong STATE) Chuyển sang Fanpage CĐT + TK QC doanh nghiệp riêng trước khi cho AI sửa/tăng tiền.

## 8. Giới hạn của lần đọc này
- Không đọc được: lượt xem đất, SĐT, cuộc gọi (Meta không báo ở VN), trạng thái "Learning".
- Chưa xem video (chỉ đọc chữ của mẫu); chưa kiểm hình ảnh/lời nói trong video theo §H3, F12.
- Tên khu vực của các vòng 16 km là ước theo toạ độ, chưa đối chiếu bản đồ.
