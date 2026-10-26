# Khung chuẩn nhân rộng: mỗi dự án mới = lõi chung + 1 thư mục cấu hình 9 nhóm file, cài ≤ 1 ngày theo 7 bước, qua 4 lớp kiểm, đo 6 số mỗi tuần

> Lập 21/10/2026 từ `workspace/research/2026-10-21-sp-3-xay-va-nhan-ban.md` mục 5c (chính), `sp-2` mục 5.c (giấy phép nền tảng, cấm cứng), `sp-1` mục 5(c) (giấy tờ bán hàng);
> đã qua kiểm độc lập (`sp-kiem-doc-lap.md`). Dùng ở Chặng 2–3 của `lo-trinh-san-pham-app.md`; sẽ thành mô-đun `marketing-bds` của bộ khung agent 0.2.4.
> Hiện dự án Yên Thế có khoảng **60%** thành phần (mục 7) [NHẬN ĐỊNH, đếm thô]. Chặng 1 chỉ ghi danh sách chỗ phải tách, không sửa gì đang chạy.

## 1. Lõi chung giữ nguyên giữa mọi dự án; chỉ thư mục cấu hình thay đổi
- **Lõi:** 8 tác nhân, skill lead, rubric chấm bài, luật trình bày top-down, `tools/` đã gỡ chữ riêng, checklist pháp lý §A–E, bộ ca kiểm chung "đất nền tỉnh", mẫu báo cáo 17:30 và thứ Hai.
- **Cấu hình riêng:** thư mục `du-an/<ma-du-an>/`, 9 nhóm file ở mục 2. Yêu cầu riêng của khách phải trả bằng cấu hình; phải viết mã mới thì ghi lại, quá 3 lần là lõi chưa tách xong.

## 2. Thư mục cấu hình một dự án (trục chia: thông tin gì của khách mà lõi cần đọc)
| # | File | Nội dung | Yên Thế đã có? |
|---|---|---|---|
| 1 | `du-an.json` | Tên thương mại, tên pháp lý, vai (chủ đầu tư/sàn), vùng, SĐT/Zalo nhận khách, người giữ quyền quyết | Rải ở `brief.md`, `CLAUDE.md`, chữ trong `tools/` → gom |
| 2 | `brief.md` | Sự thật kinh doanh: sản phẩm, pháp lý, tiện ích, khách mục tiêu | Có |
| 3 | `luat-rieng.md` + `thong-diep.md` | Quy tắc riêng dự án (§F) và sổ thông điệp KHOÁ/MỞ (§G) | Có, nằm chung checklist → tách |
| 4 | `gia-va-tu-cam.json` | Mốc giá được nói, con số cấm, từ cấm riêng | Có, trộn trong `config/banned_terms.json` → tách |
| 5 | `kho-anh/` + `kho-anh.json` | Ảnh, video đã duyệt, nhãn góc, ngày chụp, nhãn AI | Có (`assets/dong-lac/`) |
| 6 | `nhom.csv` | Nhóm Facebook, vùng, luật nhóm (chỉ dùng cho người thật đăng) | Có trong cơ sở dữ liệu → xuất file |
| 7 | `tai-khoan.json` | Mã Trang, tài khoản QC, Zalo OA, ai có quyền — **không mật khẩu, không cookie** | Rải trong STATE, settings → gom |
| 8 | `qc.json` | Ngân sách, trần, ngưỡng TẮT/GIỮ/TĂNG, vùng, giờ trực | Trộn trong skill `quang-cao-bds` và `doc_ads.py` → tách số |
| 9 | `lich.json` + `ca-kiem-rieng/` | Số bài/ngày, giờ đăng, giờ báo cáo; ≥ 10 ca kiểm riêng dự án | Trộn trong `config/settings.json`, `evals/` → tách |

## 3. Bảy bước cài cho khách mới (mục tiêu ≤ 1 ngày tại chỗ)
0. *Trước 3–5 ngày:* gửi **phiếu thu tư liệu** 1 trang (pháp lý, bảng hàng, mốc giá được nói, ảnh, SĐT nhận khách, ai quyết). Chưa đủ thì chưa hẹn ngày cài.
1. Kiểm máy: Windows, Python, Claude đứng tên khách (thử) hoặc API key của đội (bán thật); chạy lệnh chẩn đoán → "đủ điều kiện chạy".
2. Cài lõi từ kho riêng bằng 1 lệnh; tạo `du-an/<mã>/` từ mẫu.
3. Điền 9 nhóm file từ phiếu thu tư liệu (AI điền nháp, người soát).
4. **Khách tự đăng nhập** Trang, tài khoản QC, Zalo OA; giao vai trò cho đội; đội không giữ mật khẩu.
5. Chạy đủ 4 lớp kiểm (mục 5); trượt ca nào sửa cấu hình, không sửa lõi.
6. Chạy thử: 6 bài + 1 mẫu QC khách duyệt; đăng 1 bài lên Trang; chạy báo cáo 17:30 một lần.
7. Bật lịch đăng và báo cáo; ghi STATE; giao 1 tờ A4 "ai làm gì, gọi ai khi hỏng".

## 4. Giấy phép nền tảng và luật cấm cứng (đủ hết mới bật lịch)
- **Khách là chủ** Trang, danh mục doanh nghiệp, tài khoản QC, Zalo OA, sổ khách; đã giao vai trò và bấm cho phép app; đã ký hợp đồng dịch vụ + hợp đồng xử lý dữ liệu [mẫu: cần luật sư xác nhận].
- **Bật sẵn:** câu chào "Em là trợ lý tự động của [chủ đầu tư]…" và nhãn "Ảnh minh hoạ tạo bằng AI" (Luật Trí tuệ nhân tạo Điều 11) [SP-2 L3; cần luật sư xác nhận cách áp].
- **Cấm cứng trong mã:** không lưu mật khẩu, cookie Meta/Zalo; không điều khiển trình duyệt để đăng cho khách; không nhắn chào hàng ngoài cửa sổ tin nhắn; dữ liệu mỗi khách tách riêng.
- **Hồ sơ app một lần cho mọi khách** (Chặng 3–4): xác minh doanh nghiệp, Tech Provider, App Review từng quyền, Marketing API bậc Full; hồ sơ phân loại AI.

## 5. Bốn lớp kiểm (trượt một lớp là chưa bàn giao)
1. **Máy kiểm cấu hình:** đủ 9 nhóm file, không ô trống, không còn chữ của dự án mẫu (ví dụ "Yên Thế" xuất hiện ở dự án khác = trượt).
2. **Ca kiểm chung ngành** đất nền tỉnh (giá, hứa lời, quy hoạch, so sánh đối thủ, khuyến mãi chưa có văn bản, vay vốn): đúng 100%.
3. **Ca kiểm riêng dự án** (mã lô, tên cũ, địa danh, thông điệp KHOÁ): ≥ 10 ca, đúng 100%.
4. **Chạy khô 7 ngày** lịch đăng + đọc số QC 1 lần: 0 lỗi chặn.

## 6. Sáu số đo mỗi tuần (báo cáo thứ Hai)
1. Mức tự chạy: số lần người chạm tay loại "có thể tự động" và "sự cố". 2. Giờ người cho dự án. 3. Tiền AI thật. 4. Tỉ lệ bài qua cổng lần đầu.
5. Kết quả QC: cuộc nói chuyện → người cho SĐT/Zalo → lượt xem đất (đội bán ghi sổ). 6. Yêu cầu riêng của khách: trả bằng cấu hình / bằng mã mới / từ chối.

## 7. Đối chiếu Yên Thế hôm nay
| Thành phần | Hiện trạng | Còn thiếu |
|---|---|---|
| Tác nhân, skill, rubric, khuôn trình bày | Có | Gỡ chữ riêng ở copywriter, `quang-cao-bds` |
| Máy kiểm + ca kiểm | Có: 20 ca compliance, 31 ca lint giá, 43 ca đọc số | Tách chung/riêng; máy kiểm cấu hình (lớp 1) |
| Lịch chạy, đọc số, báo cáo | Có (lịch Windows, lịch Claude, `doc_ads.py`, mẫu 17:30 + thứ Hai) | Ngưỡng số tách ra `qc.json`; phần API chưa chạy được trên máy chủ |
| Thư mục cấu hình 1 dự án | Chưa (rải ở brief, CLAUDE.md, config, cơ sở dữ liệu, 8 file `tools/`) | Toàn bộ mục 2 |
| Bộ khung chung | Khung 0.2.4 có, nhưng dự án **không dựng trên khung** | Mô-đun `marketing-bds`; chuyển dự án sang lõi khung |
| Sổ tay cài, phiếu thu tư liệu; đo mức tự chạy, giờ người, tiền AI | Chưa | Mục 3; số 1–3, 6 của mục 6 |
| Fanpage qua đường chính thức | Mã có, chưa nối | Nối ở Chặng 1 (luồng C2) |

**Giấy tờ bán hàng đi kèm khung:** bảng giá 1 trang (đơn vị "lượt xem đất"); mẫu sổ nguồn khách + định nghĩa "lượt xem đất có xác nhận" (ai xác nhận, ghi trong 24 giờ); bảng tính lãi mỗi khách; 6 câu phỏng vấn khách (SP-1 §6); lịch theo dõi luật chơi mỗi quý (Meta, Zalo, nghị định tin nhắn rác, Luật Kinh doanh bất động sản, hướng dẫn Luật Trí tuệ nhân tạo).
