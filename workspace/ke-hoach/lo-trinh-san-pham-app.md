# Lộ trình sản phẩm bản 2: bán "phòng marketing số làm thay" cho chủ đầu tư và sàn bất động sản tỉnh — thử ở Yên Thế tới 30/11, tách lõi tháng 12, khách thứ 2 tháng 01/2027

> Bản 2 ngày 21/10/2026, thay bản 1 ngày 20/10 (sao lưu `workspace/reports/backup/2026-10-21-tong-hop-sp/`). Căn cứ: 3 phiên nghiên cứu SP-1, SP-2, SP-3 và 1 lượt kiểm độc lập
> (16/22 dữ kiện khớp, chỗ lệch đã đính chính ở đầu từng file) — `workspace/research/2026-10-21-sp-*.md`; tổng chi ~1,04 triệu token. 4 tầng kế hoạch `cap-1` → `cap-4` là chi tiết Chặng 1.
> Nhãn: [DỮ LIỆU] · [SP-x Dy] (dòng trong file nghiên cứu) · [NHẬN ĐỊNH] · [ƯỚC TÍNH] · [CẦN XÁC NHẬN]. Kết luận pháp lý: cần luật sư xác nhận.

## 1. Đích đến: thắng ở chủ đầu tư và sàn đất nền tỉnh, bằng 3 thứ Meta và agency không làm
- **Bán gì:** "phòng marketing số làm thay" theo tháng — tạo bài, kiểm luật, đăng Fanpage, quản lý quảng cáo Meta, báo cáo — chấm bằng **lượt xem đất**, không bằng lượt thích.
- **Cho ai:** chủ đầu tư dự án đất nền ở tỉnh; thử song song 1 sàn bán nhiều dự án, vì sàn có thể là khách bền hơn [GIẢ THUYẾT, SP-1].
- **Thắng bằng:** (1) kiểm luật quảng cáo bất động sản Việt Nam trước khi đăng; (2) đo tới lượt xem đất và hợp đồng; (3) một đội làm thay đủ 4 khâu, giá ngang agency nhỏ 4–6,5 triệu/tháng [SP-1 D4, D5].
- **Bỏ:** bán công cụ đăng nhóm bằng nick (trái điều khoản Meta; 203 bài ra 1 SĐT), "AI viết bài" lẻ, chatbot hay bảng điều khiển quảng cáo — Meta đang tự làm, mới bắt đầu miễn phí [SP-2 M9–M14].

## 2. Vì sao: câu trả lời tạm đúng, nhưng có điều kiện ở cả 3 mặt
| Điều phải đúng | Kết luận | Điều kiện chính |
|---|---|---|
| **Có cầu** (SP-1) | Đúng có điều kiện | Cầu nhỏ và ngắn (mỗi dự án ở 3–6 tháng); chỉ trả cao khi giá gắn với lượt xem đất; chưa chủ đầu tư nào nói giá |
| **Được phép** (SP-2) | Đúng có điều kiện | 5/6 việc có đường chính thức, đăng nhóm bằng nick thì không; khách đứng tên mọi tài khoản; giữ sổ khách của nhiều chủ đầu tư có thể cần giấy chứng nhận xử lý dữ liệu [CẦN XÁC NHẬN, luật sư] |
| **Làm được** (SP-3) | Đúng có điều kiện | Phải tách lõi khỏi dữ liệu Yên Thế (8/25 file `tools/` còn chữ riêng); bán thật phải chuyển sang API key + Agent SDK; phần điều phối khoá vào Claude |

Câu hỏi: đi thế nào để đạt cả 3 điều kiện với ít tiền nhất? Trả lời: 5 chặng dưới, chặng sau chỉ mở khi cổng của chặng trước đạt.

## 3. Năm chặng (trục chia: ai làm phần việc chính — người làm tay → quy trình đóng gói → máy)
| Chặng | Làm gì | Đi tiếp khi (viết trước) |
|---|---|---|
| **1 · Thử ở Yên Thế** (nay → 30/11) | Chạy đủ 4 khâu; ghi sổ "việc tay"; đo token thật; nối Fanpage qua đường chính thức; câu chào "trợ lý tự động" + nhãn ảnh AI; anh phỏng vấn 3–5 chủ đầu tư/sàn; hỏi Anthropic và luật sư | 2 tuần liền chỉ còn việc tay bắt buộc; quy trình chạy mỗi tuần không sửa lõi; có số lượt xem đất thật |
| **2 · Tách lõi** (tháng 12) | Mô-đun "marketing bất động sản" trong bộ khung agent; thư mục cấu hình 9 nhóm file; tách ca kiểm chung/riêng; sổ tay cài + phiếu thu tư liệu | Cài lên máy sạch ≤ 1 ngày, qua đủ 4 lớp kiểm |
| **3 · Khách thứ 2** (tháng 01/2027) | Dịch vụ đóng gói cho 1 chủ đầu tư hoặc sàn; khách đứng tên mọi tài khoản; nộp hồ sơ Meta (xác minh, Tech Provider, App Review: ~4–8 tuần [ƯỚC TÍNH]) | 2 tuần không sửa lõi; giờ người ≤ 20 giờ/tháng; lãi trên khách dương |
| **4 · 3–5 khách** (quý 1–2/2027) | Chuyển "động cơ" sang API key + Agent SDK; ≥ 80% yêu cầu riêng trả bằng cấu hình; giấy tờ dữ liệu theo ý luật sư | 3 dự án cùng gói đều có lãi; < 1/3 thời gian đội làm riêng theo yêu cầu |
| **5 · App nhiều người dùng** (quyết sau) | Chỉ làm khi ≥ 5–10 dự án, đã qua App Review, khách đòi tự dùng | Khách vẫn muốn "có người làm hộ" → ở lại chặng 4 |

## 4. Việc lớn và người chịu trách nhiệm (Chặng 1–2; AI chỉ làm, anh chịu trách nhiệm cuối)
| Việc | AI làm | Hạn |
|---|---|---|
| Chốt hướng, giá, cách đóng gói | Soạn phương án, tính lãi 3 kịch bản | 30/11 |
| Phỏng vấn 3–5 chủ đầu tư/sàn (6 câu có sẵn ở SP-1 §6) | Soạn câu hỏi, tổng hợp câu trả lời | 30/11 |
| Đo mức tự chạy, token thật, giờ người | Ghi sổ, đếm trong báo cáo thứ Hai | từ 26/10 |
| Hỏi Anthropic + luật sư (gói Claude tự chạy, dữ liệu khách, thưởng theo lượt xem) | Soạn câu hỏi | 15/11 |
| Tách lõi, dựng mô-đun, sổ tay cài | Viết mã, cấu hình, ca kiểm | 31/12 |

## 5. Ngày quan trọng
26/10 bắt đầu sổ việc tay → 03/11 có token thật 1 tuần → 09/11 bảng chấm QC 14 ngày → 15/11 gửi câu hỏi luật sư, Anthropic → **30/11 cổng Chặng 1** → **31/12 cổng Chặng 2** → 01/2027 khách thứ 2.

## 6. Ba rủi ro lớn nhất
| Rủi ro | Dấu hiệu sớm | Làm gì |
|---|---|---|
| Meta làm thay phần quảng cáo, trả lời tin (Ads AI Connectors thử từ 29/04/2026; Business Agent) [SP-2 M13, M14] | Công cụ của Meta có tiếng Việt, mở ở Việt Nam | Dựng trên công cụ của Meta; chỉ bán phần Meta không làm |
| Lãi âm vì tiền AI và giờ người | Token thật > 2,5 tr/khách/tháng; giờ người > 20 giờ/tháng | Viết bài bằng Sonnet, phiên ngắn; chưa báo giá trước khi đo |
| Cầu quá ngắn: mỗi dự án chỉ 3–6 tháng | Chủ đầu tư được phỏng vấn không có dự án tiếp | Thử 1 sàn bán nhiều dự án; gói trả trước 90 ngày |

## 7. Cần anh quyết
| Quyết gì | Đề xuất | Hạn |
|---|---|---|
| Lịch đăng nhóm bằng nick (trái điều khoản Meta) | Giữ mức đang chạy, không mở rộng, không đưa vào app; dừng nếu 09/11 vẫn ~0 SĐT | 09/11 |
| Cách đóng gói cho khách thứ 2 | Khách tự đứng tên gói Claude để thử; bán thật thì chuyển API key + Agent SDK; không dùng gói của đội chạy hộ nhiều khách | 30/11 |
| Giá thử | M1: nền 9 tr + cài 10 tr + 200 nghìn/lượt xem đất (trần 4 tr) — chỉ chốt sau khi có token thật và ý kiến luật sư; bỏ cách thu theo hợp đồng | 30/11 |
| Chi phí đội mỗi tháng | Anh cho số thật; đang giả định 40 hoặc 60 tr → cần 7–8 hoặc 11–12 khách cùng lúc [ƯỚC TÍNH] | 30/11 |

---
## Phụ lục
**A. Lãi mỗi khách theo M1, 3 kịch bản tiền AI** (thu 11 tr ở 10 lượt xem; giờ hỗ trợ 10 giờ × 250 nghìn = 2,5 tr; chi khác 0,4 tr [GIẢ ĐỊNH SP-1]):
| Kịch bản | Tiền AI/khách/tháng | Lãi đóng góp |
|---|---|---|
| Tốt (Sonnet, bộ nhớ đệm) | 1,2 tr [SP-3 3.3e] | ≈ 6,9 tr |
| Giữa (gói Claude ~100 USD) | 2,6 tr [SP-1] | ≈ 5,5 tr |
| Xấu (toàn Opus, phiên dài) | 8,6 tr [SP-3 3.3e] | ≈ −0,5 tr |

**B.** Khung chuẩn nhân rộng: `khung-chuan-nhan-rong.md`. **C.** Việc Chặng 1 trong tuần: `cap-4-viec-tuan.csv` (W43-27 → W43-33). **D.** Nguồn: `workspace/research/2026-10-21-sp-00…sp-3`, `sp-kiem-doc-lap`; dùng lại SU-3, SU-5, SU-8 (`D:\0. AI\goi-phong-kham\nghien-cuu\startup\`), bộ khung agent 0.2.4.
