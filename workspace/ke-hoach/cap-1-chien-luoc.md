# Tầng 1 · Chiến lược tới 10/01/2027: hệ thống AI tự tạo, chấm, đăng bài và quản lý 48 triệu quảng cáo — 4 khâu, sau này là 4 mô-đun app

> Tầng trên cùng của 4 tầng (`workspace/ke-hoach/`). Không chứa việc, tên người, lịch ngày (luật `.claude/rules/tu-duy-top-down.md` §5).
> **Phạm vi từ 20/10/2026 (người dùng):** chỉ 4 khâu số — tạo bài, đánh giá, đăng bài, quản lý quảng cáo. Bỏ mọi việc offline (sự kiện tại chỗ, xe, đại lý,
> đại sứ, công cụ bán in giấy, đào tạo). Mục đích: sau này đóng gói thành app để nhân rộng. Bản trước: `workspace/reports/backup/2026-10-20-thu-hep-pham-vi/`.
> Nguồn số: kế hoạch v2 `workspace/reports/2026-10-15-ke-hoach-ban-hang-90-ngay-v2.md` (dòng Quảng cáo Meta §1, §4.1) và skill `quang-cao-bds`.
> Tầng trên: `lo-trinh-san-pham-app.md` (công cụ → app, Yên Thế là lần chạy thử đầu tiên). Không chuyển tài khoản QC sang danh mục khác (người dùng 20/10: "Edwin Rinaldi" là nick của Nam Lê).

## 1. Tuyên bố chiến lược của hệ thống (34 chữ) — **[CHỜ NGƯỜI DÙNG CHỐT]**

> **"Đến 10/01/2027, AI tự tạo, chấm, đăng bài và quản lý 48 triệu quảng cáo, ra ~400 cuộc nói chuyện, ~40 lượt xem đất, 5 hợp đồng; quy trình đủ đều để thành app."**

Mục tiêu: ~400 cuộc nói chuyện → ~40 lượt xem → 5 HĐ (đúng phần quảng cáo của v2) · Phạm vi: 4 khâu số cho Yên Thế Golden Hill · Lợi thế: chạy theo lịch,
có cổng luật tự động, đo bằng lượt xem đất chứ không bằng lượt thích. **Bối cảnh doanh nghiệp (đã chốt 20/10, giữ nguyên):** "Đến 10/01/2027 ký 60 hợp đồng
(phấn đấu 72) với 5 nhóm khách quanh Yên Thế, qua người quen, đại lý, sự kiện, quảng cáo; nhờ sổ đỏ đã trao, trả trước từ 500 triệu." Hệ thống này lo phần số.

## 2. Vì sao (SCQ)
Bối cảnh: đã có lịch tự đăng 12 bài nhóm/ngày, lịch viết lô bài tuần, cổng luật tự động, kết nối Meta chỉ đọc, 2 lịch báo cáo QC. Vướng: 203 bài nhóm ra 1 SĐT,
QC mới 1 chiến dịch chưa đo được lượt xem đất, nhiều bước vẫn cần mở chat [DỮ LIỆU research 20/10, Meta 20/10]. Câu hỏi: làm gì để vừa ra khách qua kênh số, vừa
chạy đều đến mức đóng gói thành app? Trả lời: 4 khâu dưới, mỗi khâu có đầu vào, đầu ra, cổng và số đo riêng.

## 3. Bốn trụ cột (trục chia: **4 khâu nội dung đi từ ý tưởng tới khách** — sau này mỗi khâu là 1 mô-đun app)

| Mã | Trụ cột (câu kết luận) | Đo bằng | Người lo chính |
|---|---|---|---|
| **A** | **Tạo bài:** đủ bài nhóm mỗi ngày và 3–5 mẫu QC khác góc mỗi đợt 14 ngày | Bài viết đúng hạn theo lịch tuần; số mẫu QC sẵn sàng mỗi đợt | Claude (copywriter) |
| **B** | **Đánh giá:** không gì ra ngoài khi chưa qua cổng; bài, mẫu nào thắng thì nhân lên | 100% qua lint + compliance; điểm judge; bảng góc/mẫu thắng mỗi tuần | Claude (compliance, judge, analyst) |
| **C** | **Đăng bài:** lịch tự đăng đều, an toàn nick | Bài lên đúng lịch; tỉ lệ hiện công khai; 0 lần nick bị khoá | Lịch tự đăng · người dùng giữ nick |
| **D** | **Quản lý quảng cáo:** mỗi đồng QC chấm bằng lượt xem đất, mỗi lần tiêu tiền mới có "ok" | ≤ 48 tr; chi phí/lượt xem ≤ 1,5 tr (cần ≤ 1,2 tr); TẮT/GIỮ/TĂNG theo luật | Người chạy QC bấm · Claude đọc số · người dùng "ok" |

MECE vì: A làm nội dung, B phán xét nội dung (trước khi ra: có được ra không; sau khi ra: bài, mẫu nào thắng), C đưa nội dung ra miễn phí theo lịch, D đưa ra
bằng tiền và quyết tiền đặt vào đâu — không việc nào thuộc 2 khâu. Đủ vì một nội dung phải đi qua cả 4 khâu mới tới khách và mới biết tốt hay dở.

## 4. Ba chỉ số của cả kỳ
1. **Chi phí quảng cáo cho mỗi lượt xem đất** (kết quả): ≤ 1,5 tr, cần ≤ 1,2 tr; tổng ≤ 48 tr [DỮ LIỆU v2].
2. **Người để lại SĐT/Zalo mỗi tuần, chia theo mã QC và mã bài nhóm** (dẫn đầu, đọc mỗi ngày 17:30).
3. **Mức tự chạy** (điều kiện để thành app): số bước còn phải mở chat hoặc làm tay mỗi tuần, ngoài các lần "ok" tiêu tiền [ĐỀ XUẤT, đo từ tuần 20–26/10].

## 5. Cổng đi tiếp hay đổi hướng (tiêu chí viết trước)

| Cổng | Đạt khi | Không đạt thì | Ai giữ D |
|---|---|---|---|
| **27/10** | Mẫu QC đợt 1 qua cổng; người dùng "ok" bật thử vùng | Chưa qua → giữ Video Mới như cũ, dời đợt 1 một tuần [ĐỀ XUẤT] | Người dùng |
| **09/11** | Bảng chấm 14 ngày có số thật: chi phí/lượt xem ≤ 1,5 tr | > 1,5 tr 2 tuần → giảm tiền, đổi video; ≤ 0,8 tr 2 tuần → xin "ok" tăng 20% | Người dùng |
| **30/11** | 4 tuần số thật cho cả 4 khâu; ngưỡng giả thuyết đã thay bằng số thật | Chưa đủ số → kéo dài đo 2 tuần, chưa viết đặc tả app [ĐỀ XUẤT] | Người dùng |

## 6. Ba chân trời
- **H1 (gần hết sức):** chạy đủ 4 khâu cho Yên Thế Golden Hill, đo bằng lượt xem đất.
- **H2:** đóng gói 4 khâu thành app cho chính dự án này: chạy theo lịch, không cần mở chat, người dùng chỉ "ok" tiêu tiền.
- **H3:** dùng app cho dự án hoặc chủ đầu tư khác (nhân rộng) — chỉ bàn khi H2 chạy ổn.

Phụ lục: v2 §1 (phễu theo kênh), §4.1 (48 tr), skill `quang-cao-bds` §5–§6 (ngưỡng, luật). Tầng dưới: `cap-2-90-ngay.md`.
