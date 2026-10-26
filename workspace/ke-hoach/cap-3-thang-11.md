# Tầng 3 · Tháng 11 (20/10 → 30/11/2026): mỗi tuần 84 bài nhóm và 3–5 mẫu QC qua cổng; QC bật đợt 1 từ 27/10, chấm 09/11 bằng lượt xem đất

> Kỳ tính từ hôm nay tới 30/11 để nối liền tuần 20–26/10 (tầng 4). Mang mã tầng trên: luồng **A1–A2, B1–B2, C1–C2, D1–D2** (chữ = trụ cột `cap-1-chien-luoc.md`),
> mỗi luồng ghi KR của `cap-2-90-ngay.md`. Chỉ việc số (người dùng 20/10); việc offline đã bỏ, xem dòng cuối. Số QC theo `workspace/plans/2026-10-20-ke-hoach-qc-14-ngay.md`.

## 1. Vì sao (SCQ)
Bối cảnh: lịch tự đăng 12 bài/ngày, lịch viết lô thứ Ba, cổng luật tự động, 2 lịch báo cáo QC đã có; QC chạy 1 chiến dịch 300k/ngày, 38 cuộc trò chuyện. Vướng: sửa QC
đang **tạm dừng chờ người dùng hỏi Phòng KD**, chưa đo được lượt xem đất. Câu hỏi: 6 tuần tới 4 khâu phải giao gì? Trả lời: 8 luồng dưới.

## 2. Bốn trụ cột của tháng (trục chia: 4 khâu như tầng 1)
| Trụ cột (câu kết luận) | Kết quả đo được tới 30/11 | KR | Người lo chính |
|---|---|---|---|
| **A** Tạo bài đúng hạn, đủ góc | 6 lô bài tuần (84 bài/lô); mẫu đợt 1 (27/10), QC-SK (30/10), mẫu thay (09/11) | KR1 | Claude |
| **B** Không gì ra ngoài khi chưa qua cổng | 100% qua lint + compliance; 4 bảng góc/mẫu thắng; ngưỡng thay bằng số thật 09/11 | KR2 | Claude |
| **C** Đăng đều, giữ an toàn nick | 12 bài/ngày; tỉ lệ hiện công khai ≥ 70% [ĐỀ XUẤT]; 0 lần nick bị khoá | KR3 | Lịch tự đăng |
| **D** QC chấm bằng lượt xem đất | 21–27/10: ≥ 50 cuộc, ≥ 20 cho số, ≥ 2 lượt xem; 28/10–03/11: ≥ 90 / ≥ 35 / ≥ 4 [GIẢ THUYẾT]; chi theo kế hoạch QC §2 | KR4 | Người chạy QC · Claude |

MECE vì: mỗi luồng dưới thuộc đúng 1 khâu; thiếu khâu nào thì nội dung không ra tới khách hoặc không biết tốt hay dở.

## 3. Tám luồng việc (việc tuần ở `cap-4-viec-tuan.csv`)
| Mã | Luồng | Giao gì tới 30/11 | PIC → người kiểm | Ai giữ D |
|---|---|---|---|---|
| **A1** | Bài nhóm FB | Lịch thứ Ba 19:05: lập lịch, ảnh, viết, tự duyệt bài đạt cho 7 ngày | Lịch viết bài (Claude) → compliance | Người dùng (đã giao tự duyệt 14/10) |
| **A2** | Mẫu QC | Đợt 1 QC-VM2/VM4 + QC-A1 + QC-B1; QC-NN1; QC-SK1/SK2; mẫu thay sau 09/11; chỉ chào lô xanh | Copywriter → compliance + judge + người kiểm §2b | Người dùng |
| **B1** | Cổng trước khi ra | Lint, similar, compliance §F–§H, judge (≥ 30/40 bài, ≥ 24/30 QC); evals 20/20 mỗi lần sửa luật | Compliance, judge → máy kiểm (evals) | Người dùng |
| **B2** | Đo sau khi ra | Bài nhóm: lead theo mã, tỉ lệ công khai, câu mở có bình luận thật. Mẫu QC: giá/cuộc, % cho số, giữ chân 3s → bảng thắng/thua thứ Hai → kho ý tưởng | Analyst → judge | Người dùng |
| **C1** | Lịch tự đăng nhóm | Windows 06:30, 12 bài/ngày, chỉ đăng; dừng khẩn bằng `data/stop_batch` | Máy → Claude đọc nhật ký mỗi tuần | Người dùng |
| **C2** | Fanpage CĐT | Nối Trang CĐT: nhận tin nhắn QC, đăng bài đã qua cổng | CĐT tạo, Claude soạn → compliance | Người dùng |
| **D1** | Chiến dịch và tiền | Sửa gộp (tạm dừng) → thử vùng + Nhật/Hàn/Đài 27/10 → Sự kiện 31/10–07/11 → chạy lại 01/11 | Người chạy QC bấm (nếu anh cho quyền: Claude dựng nháp ở trạng thái tắt) → người kiểm §2b | Người dùng (mỗi lần tiêu tiền mới) |
| **D2** | Đọc số và báo cáo | Lịch 17:30 hằng ngày + 8:04 thứ Hai; bảng chấm 09/11; đọc sổ nguồn khách (đội bán ghi) | Lịch báo cáo (Claude) → người dùng | Người dùng |

## 4. Mốc và đường găng (★ = trễ là trễ bảng chấm 09/11)
| Ngày | Mốc |
|---|---|
| T4 21/10 | Báo cáo QC 17:30 đầu tiên (~17:35) |
| T6 23/10 | 3 quyết định QC (sau khi hỏi Phòng KD) |
| T2 26/10 ★ | Báo cáo thứ Hai đầu tiên; mẫu QC đợt 1 qua cổng |
| T3 27/10 ★ | Bật đợt 1 thử vùng + Nhật/Hàn/Đài (cần "ok"); lô bài tuần |
| T6 30/10 ★ | QC-SK qua cổng → bật Sự kiện 31/10 (cần "ok") |
| T2 02/11 | Ngày 7 đợt 1: tắt mẫu tiêu < 50% phần chia đều |
| T2 09/11 ★ | Bảng chấm 14 ngày: chốt vùng, thay ngưỡng giả thuyết |
| T2 30/11 | Tổng kết tháng: đủ 4 tuần số thật → quyết có viết đặc tả app |

## 5. Ba rủi ro lớn nhất
| Rủi ro | Dấu hiệu sớm | Làm gì |
|---|---|---|
| QC kẹt: sửa gộp còn tạm dừng chờ Phòng KD | 23/10 chưa có trả lời | Giữ Video Mới như cũ, dời đợt 1 một tuần [ĐỀ XUẤT] |
| Nick nhóm bị hạn chế ở 12 bài/ngày | Tỉ lệ bài chờ duyệt > 50% (đã từ 18% lên 46% [DỮ LIỆU]); cảnh báo checkpoint | Tạo `data/stop_batch`, báo người dùng chọn giảm bài hay đổi nhóm |
| Không chấm được QC bằng lượt xem đất | Sau 3 ngày sổ nguồn khách chưa có dòng thật; chưa có 4 số từ người chạy QC | Báo cáo chỉ dùng tín hiệu sớm, gắn [GIẢ THUYẾT]; nhắc người dùng chia sẻ sổ |

## 6. Cần quyết gì
| # | Quyết gì | Đề xuất | Ai giữ D | Hạn |
|---|---|---|---|---|
| 1 | Quyết định tiền QC: trừ 2,73 tr đã chi vào dự phòng hay vào Nền (2 quyết định về chuyển danh mục đã bỏ 20/10) | Trừ vào dự phòng (kế hoạch QC §7, phương án a); người dùng 20/10: chưa | Người dùng | T6 23/10 |
| 2 | Tuyên bố chiến lược của hệ thống (34 chữ) | Bản ở `cap-1-chien-luoc.md` §1 | Người dùng | T6 23/10 |
| 3 | Bật đợt 1: thử vùng 2 × 120k + Nhật/Hàn/Đài 230k/ngày (chưa VAT) | Bật khi mẫu đã qua cổng | Người dùng | T3 27/10 |
| 4 | Bật Sự kiện Đêm hội 680k/ngày chưa VAT (~6 tr gồm VAT cả đợt) | Bật khi QC-SK qua cổng | Người dùng | T6 30/10 |
| 5 | Lịch đăng nhóm bằng nick: trái điều khoản Meta (SP-2) | Giữ mức đang chạy, không mở rộng, không đưa vào app; dừng nếu 09/11 vẫn ~0 SĐT | Người dùng | T2 09/11 |

Bỏ khỏi phạm vi 20/10 (việc offline, không xoá ở v2): phố đêm, xe, phiếu ưu tiên, đại sứ, đại lý, công cụ bán in, đào tạo, số cổng CĐT. Phụ lục: kế hoạch QC 14 ngày · mẫu báo cáo 17:30 · research 20/10–21/10 · skill `quang-cao-bds`.
