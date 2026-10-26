# Luật trình bày top-down cho dự án Yên Thế Golden Hill (áp cho MỌI phiên, MỌI tác nhân; dựng 20/10/2026)

> Gốc: `D:\0. AI\goi-phong-kham\nghien-cuu\startup\su-9-cach-tu-duy-va-trinh-bay-top-down.md` (SU-9: mục 1.8, 2, 3.9, 4.1–4.3).
> Phạm vi: luật này chỉ quy định **cách nghĩ và cách trình bày đầu ra**. Luật nghiệp vụ (pháp lý, giá, QC, đăng bài) vẫn nằm ở
> `CLAUDE.md`, `workspace/compliance-checklist.md`, các skill và tác nhân. Hai bên mâu thuẫn về nội dung → luật nghiệp vụ thắng.
> Việc tầm thường (sửa một dòng chữ, trả lời một con số) không cần đủ khuôn; vẫn giữ T1: câu đầu là câu trả lời.
> **Phạm vi dự án từ 20/10/2026 (người dùng):** chỉ 4 khâu số — tạo bài · đánh giá · đăng bài · quản lý quảng cáo — để sau này đóng gói thành app; việc offline ngoài phạm vi.

## 1. Tám luật T1–T8 (mỗi tài liệu, mỗi tin nhắn, mỗi bản tác nhân nộp)

| # | Luật | Ví dụ đúng ở dự án này | Kiểm nhanh |
|---|---|---|---|
| T1 | **Kết luận trước.** Câu đầu là điều người đọc phải biết hoặc phải làm | "[QUYẾT] Đề xuất giữ Video Mới 300k tới 26/10, không tăng tiền." — không mở bằng "Hôm nay em đã đọc 6 tài khoản…" | Chỉ đọc câu đầu có biết phải làm gì không? |
| T2 | **Một thông điệp chính**, nói lại được trong 1 câu ≤ 35 chữ, có ngày và con số | "Tuần 21–27/10 QC cần ≥ 50 cuộc nói chuyện, ≥ 20 người cho số với ~2,27 tr." | Đếm chữ câu chính |
| T3 | **3–5 ý đỡ, chia MECE, ghi rõ trục chia** | Trục "4 khâu": tạo bài · đánh giá · đăng bài · quản lý quảng cáo (mỗi việc thuộc đúng 1 khâu) | Có trùng không? Cộng lại có đủ không? |
| T4 | **Tiêu đề là câu kết luận**, không phải nhãn | "Nhóm FB 25 ngày ra 1 SĐT: chỉ dùng để thử câu mở" thay cho "Kết quả đăng nhóm" | Đọc riêng các tiêu đề ra đủ câu chuyện |
| T5 | **SCQ ≤ 4 câu khi người đọc thiếu bối cảnh** (TPKD, đại lý, phiên mới); chủ sở hữu đã nắm thì bỏ | Bối cảnh: QC đang chạy 300k/ngày. Vướng: quỹ nền 16 tr cạn ~08/12. Câu hỏi: giữ hay hạ? → trả lời | Bối cảnh dài hơn 4 câu là thừa |
| T6 | **Luôn kết bằng "cần quyết gì · ai giữ D · hạn nào"**; không có thì ghi "Không cần quyết" | "Cần anh: ok trừ 2,73 tr vào dự phòng · anh giữ D · trước 23/10" | Có dòng quyết ở cuối không? |
| T7 | **Trang chính ≤ 1 trang (~60 dòng); chi tiết xuống phụ lục, bảng tính hoặc file riêng, dẫn đường link** | Lịch theo ngày, bảng 23 việc, nguồn Meta → phụ lục / `workspace/ke-hoach/cap-4-viec-tuan.csv` | Bỏ phụ lục đi có còn hiểu không? |
| T8 | **Số cụ thể, ngày cụ thể; tách sự thật khỏi nhận định** bằng nhãn có sẵn của dự án: [DỮ LIỆU] · [NGUỒN] · [GIẢ THUYẾT] · [CẦN XÁC NHẬN] | "27.066đ/cuộc trò chuyện [DỮ LIỆU Meta 20/10]"; "1,2 tr/lượt xem là mức cần đạt [GIẢ THUYẾT]" | Mỗi con số có nhãn hoặc nguồn |

Không làm: mở bằng kể lại việc đã làm; liệt kê việc theo ngày ở trang chính; bảng dài trong chat; mã việc, tên công cụ, đường dẫn dày đặc trong
phần chủ sở hữu đọc (để ở dòng cuối hoặc phụ lục); đưa danh sách lựa chọn mà không nói chọn cái nào.

## 2. Khuôn tin nhắn chat (BLUF, tối đa 10 dòng)

```
[QUYẾT|BÁO|HỎI|VIỆC] Kết luận trong 1 câu (≤ 35 chữ, có ngày/con số).
- Ý đỡ 1 ┐
- Ý đỡ 2 ├ 2–3 ý, chia MECE (vì sao / hiện trạng / rủi ro)
- Ý đỡ 3 ┘
Phương án (chỉ khi [QUYẾT]): đề xuất trước, phương án khác sau, mỗi cái 1 dòng.
Cần anh/chị: quyết gì / trả lời gì / làm gì — trước khi nào.
Em làm tiếp: 1 việc tiếp theo của Claude.
Chi tiết: <đường dẫn file> (nếu có).
```

| Nhãn | Dùng khi | Ví dụ |
|---|---|---|
| **[QUYẾT]** | Cần chủ sở hữu chọn / "ok" (nhất là mỗi lần tiêu tiền mới) | "[QUYẾT] Đề xuất bật đợt 1 thử vùng 2 × 120k/ngày từ 27/10, khi mẫu đã qua cổng." |
| **[BÁO]** | Chỉ để biết, không cần làm gì (có thể chỉ 2–3 dòng) | "[BÁO] Lịch đăng hôm nay lên <n>/12 bài, <k> lỗi; không cần làm gì." |
| **[HỎI]** | Cần một thông tin mới làm tiếp được | "[HỎI] Phòng KD đã gửi 4 số từ 38 cuộc trò chuyện chưa ạ?" |
| **[VIỆC]** | Cần chủ sở hữu tự làm một thao tác (Claude không được làm: bấm Meta, nhập PIN, gửi Zalo) | "[VIỆC] Anh dán tin mục D cho người chạy QC, trước 21/10." |

Luật thêm: một tin chỉ một nhãn chính; cần hơn 10 dòng thì viết tài liệu theo khuôn 6 ô (mục 3) rồi gửi đường dẫn; câu hỏi làm rõ cũng theo
khuôn này (1–2 dòng bối cảnh → 1 câu hỏi → các lựa chọn, lựa chọn khuyên dùng đứng đầu); vẫn giữ luật "chỉ nêu 1 bước tiếp theo" của CLAUDE.md.

## 3. Khuôn 1 trang 6 ô (kế hoạch, báo cáo, đề xuất, bản tác nhân nộp dài)

```
# [Tên kỳ]: [THÔNG ĐIỆP CHÍNH, 1 câu ≤ 35 chữ, có ngày và con số]
## 1. Vì sao (SCQ ≤ 4 câu)           Bối cảnh … Vướng … Câu hỏi … → trả lời = thông điệp ở tiêu đề.
## 2. 3–5 trụ cột (trục chia: …)     | Trụ cột (câu kết luận) | Kết quả đo được | Người lo chính |  + dòng "MECE vì: không trùng vì…, đủ vì…"
## 3. Luồng việc                     | Mã | Luồng | Giao gì | PIC → người kiểm | Ai giữ D |  (mỗi trụ cột 1–3 luồng; việc chi tiết ở bảng tính)
## 4. Mốc và đường găng              5–8 mốc có ngày; ★ = trễ là trễ mốc cuối; ghi ngày đệm còn lại.
## 5. Ba rủi ro lớn nhất             | Rủi ro | Dấu hiệu sớm | Làm gì |
## 6. Cần quyết gì                   | # | Quyết gì | Đề xuất | Ai giữ D | Hạn |   (không có → "Không cần quyết")
Phụ lục: bảng việc, căn cứ, nguồn, thuật ngữ (đường link tới file chi tiết).
```

- Trang chính ≤ ~60 dòng. Báo cáo ngắn (17:30) dùng khuôn rút gọn: kết luận 1 câu + 3 con số + cần quyết (mẫu ở `workspace/plans/2026-10-20-bao-cao-qc-17h30.md`).
- Trục chia hay dùng ở dự án này (chọn 1, nói ra): **4 khâu hệ thống** (tạo · đánh giá · đăng · quảng cáo); **công thức** HĐ = lô xanh × lượt xem đất có người cầm tiền × tỉ lệ chốt;
  **kênh** (giới thiệu · đại lý · sự kiện · sale · QC); **nhóm khách** (1–5, cờ N5); **phễu 6 bậc** (lead → đủ chất lượng → xem đất → giữ chỗ → cọc → ký);
  **thời gian** (trước · trong · sau Đêm hội 07/11). Trục lẫn lộn trong một tầng là dấu hiệu chưa MECE.

## 4. Giải vấn đề: 7 bước rút gọn (Conn & McLean, SU-9 mục 2)

1. **Câu hỏi đúng:** cụ thể, đo được, có hạn, có phạm vi, người giữ D đồng ý. Ví dụ: "Làm sao QC ra ≥ 2 lượt xem đất có người cầm tiền trong tuần 21–27/10 với ~2,27 tr?"
2. **Cây vấn đề MECE, nói rõ trục chia.** Ví dụ trục phễu (kế hoạch QC 14 ngày §5): ≥ 2 lượt xem = ≥ 50 cuộc nói chuyện × ~40% cho số × ~10% đi xem:
   ```
   ≥ 2 lượt xem đất từ QC, tuần 21–27/10
   ├── A. Đủ cuộc nói chuyện     (mẫu khác góc · câu mở 3 giây · vùng "người sống ở đây" · giờ chạy 7–21h)
   ├── B. Nói chuyện ra SĐT/Zalo  (tin chào xin số ở câu 2 · trả lời ≤ 5 phút)
   └── C. Có số ra lượt xem       (gọi lại, hẹn giờ cụ thể: việc của đội bán, hệ thống chỉ đo)
   ```
3. **Giả thuyết trước** (câu trả lời ngày đầu), rồi chỉ thu số để xác nhận hoặc bác. Ví dụ: "Nghẽn ở B, không ở QC: 38 cuộc trò chuyện chưa rõ
   bao nhiêu người cho số." → kiểm bằng 4 số người chạy QC gửi về.
4. **Cắt cành 80/20:** bỏ nhánh ít tác động, ghi rõ bỏ gì. Ví dụ: nhóm FB 203 bài → 1 SĐT [DỮ LIỆU 20/10] → không dồn sức sửa câu chữ nhóm; dùng nhóm để thử câu mở miễn phí, dồn sức vào mẫu QC.
5. **Kế hoạch việc:** mỗi lá còn lại thành 1 việc có PIC, người kiểm, ai giữ D, hạn (mục 5).
6. **Phân tích bằng số thật** (lệnh + kết quả, SQL + kết quả thô); mẫu nhỏ gắn [GIẢ THUYẾT].
7. **"So what"**: mỗi phát hiện phải đổi được một quyết định, không đổi được thì đẩy xuống phụ lục. Ví dụ: "Ảnh trao sổ ra ít tương tác nhất
   (4/54 bài)" → so what: đổi ảnh bìa nhóm sang ảnh buổi tối; QC vẫn giữ góc sổ đỏ vì đó là bằng chứng, chấm bằng lượt xem đất.

## 5. Chia việc: PIC + người kiểm + ai giữ D, mỗi việc mang mã tầng trên

- **PIC** (người lo chính, 1 người/1 vai) làm và tự chứng minh ban đầu; **người kiểm** khác PIC (luật 2 của CLAUDE.md); **ai giữ D** = một người
  quyết cuối (mượn RAPID của Bain). Ở dự án này: tiêu tiền QC mới → **người dùng** giữ D; giá, chính sách, hoa hồng, bảng hàng → **CĐT (Chủ tịch)**
  hoặc TPKD theo kế hoạch v2; nội dung đăng/QC → compliance kiểm, người dùng giữ D khi `require_human_approval=true`.
- **Bốn tầng kế hoạch, mỗi tầng ≤ 1 trang**, thư mục `workspace/ke-hoach/`:

  | Tầng | File | Trả lời | Mã |
  |---|---|---|---|
  | 1. Chiến lược tới 10/01/2027 | `cap-1-chien-luoc.md` | Thắng ở đâu, bằng gì, đo bằng gì | Trụ cột **A–D** (A Tạo bài · B Đánh giá · C Đăng bài · D Quảng cáo) |
  | 2. 90 ngày | `cap-2-90-ngay.md` | Quý này đạt gì, làm gì trước, cổng nào | **KR1–KR4** (mỗi KR gắn 1 trụ cột) |
  | 3. Tháng | `cap-3-thang-11.md` | Luồng nào, ai lo, mốc nào | Luồng **A1–A2, B1–B2, C1–C2, D1–D2** (chữ = trụ cột) |
  | 4. Tuần | `cap-4-viec-tuan.csv` | Ai làm gì, xong khi nào, ai kiểm | Việc **W43-01…** + cột `ma_tru_cot` = luồng · KR |

  Mã việc `W<tuần ISO>-<số>` theo tuần **bắt đầu** việc (hạn có thể rơi sang tuần sau). Việc chốt chính tầng 1–2 (tuyên bố chiến lược, KR) ghi `ma_tru_cot` = "Tầng 1 (A–D)" / "Tầng 2"; việc của lộ trình sản phẩm (`lo-trinh-san-pham-app.md`) ghi "Lộ trình SP · Chặng <n>".

- **Ba luật nối tầng:** (1) **truy vết**: mỗi dòng tầng dưới mang mã tầng trên; việc không gắn được mã nào thì hỏi "có cần làm không?";
  (2) **catchball**: tầng trên đề xuất, tầng dưới phản hồi trong 1 buổi rồi mới chốt; (3) **chi tiết đi xuống, kết luận đi lên**: báo cáo 17:30
  trả lời cho KR tuần, giao ban thứ Hai trả lời cho KR tháng, cổng 28/10 và 30/11 trả lời cho chiến lược.
- Kế hoạch v2 (`workspace/reports/2026-10-15-ke-hoach-ban-hang-90-ngay-v2.md`) và tài liệu cho Sales **không sửa**: đó là phụ lục, nguồn sự thật
  về số; bốn tầng chỉ xếp lại và dẫn link. Số ở bốn tầng lệch v2 → v2 thắng, ghi "LỆCH" và đưa vào ô "Cần quyết".

## 6. Bản tác nhân nộp cho Lead (mọi tác nhân trong `.claude/agents/`)

```
KẾT LUẬN: 1 câu (đạt / không đạt / chặn, kèm con số).
1–5 ý MECE (ghi trục chia), mỗi ý 1 dòng, có bằng chứng (đường dẫn, lệnh + kết quả, post id).
CẦN QUYẾT: việc Lead hoặc người dùng phải quyết (ai giữ D) — không có thì "Không cần quyết".
Phụ lục: bảng chi tiết theo đúng mẫu riêng của tác nhân (post_id | kết quả | …).
```
Bằng chứng bắt buộc theo loại việc (CLAUDE.md, skill lead) vẫn giữ nguyên; khuôn này chỉ đổi thứ tự: kết luận và quyết định lên đầu, bảng xuống cuối.
