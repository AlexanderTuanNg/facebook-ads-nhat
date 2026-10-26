# RUBRIC CHẤM BÀI VIẾT (agent `judge` dùng)

Chấm **sau khi** bài đã PASS compliance. Compliance là cổng đạt/không đạt; rubric này chấm **chất lượng**.
Mỗi tiêu chí 1–5 điểm, tổng 40. Phải trích 1 câu trong bài làm bằng chứng cho mỗi điểm ≤ 3.

| # | Tiêu chí | 5 điểm | 3 điểm | 1 điểm |
|---|---|---|---|---|
| R1 | **Hook (2 dòng đầu)** | Cụ thể, chạm đúng nỗi đau persona, khiến muốn đọc tiếp | Rõ nhưng chung chung | Nhạt / tiêu đề quảng cáo |
| R2 | **Đúng persona** | Rõ ràng viết cho 1 persona, dùng ngữ cảnh của họ (VD: làm nhà, mặt bằng buổi tối) | Hợp nhiều người, không ai cụ thể | Lệch persona |
| R3 | **Giá trị cho người đọc** | Người đọc học được điều dùng ngay (checklist, cách kiểm tra) | Có thông tin nhưng mỏng | Chỉ quảng cáo |
| R4 | **Tính địa phương / cụ thể** | Chi tiết thật về Yên Thế / TL 292 / đời sống (có trong brief/research) | Nhắc địa danh chung | Có thể đăng ở bất kỳ tỉnh nào |
| R5 | **Giọng thương hiệu** | Đúng playbook §7: CĐT gần gũi, mộc, không hô hào | Hơi quảng cáo | Hô hào, viết hoa, nhiều emoji |
| R6 | **CTA** | Một CTA rõ, đúng cta_type, dễ làm | CTA mờ / hai CTA | Không CTA khi cần, hoặc CTA ép |
| R7 | **Dễ đọc trên điện thoại** | Câu ngắn, xuống dòng, 80–200 chữ | Hơi dài / khối chữ | Khó đọc |
| R8 | **Tin cậy** | Mọi khẳng định có căn cứ (brief/nguồn); dùng đúng câu chuẩn pháp lý | 1 khẳng định mơ hồ | Khẳng định không căn cứ |

**Ngưỡng:** ≥ 30/40 và không tiêu chí nào < 3 → `judge_pass`. Dưới ngưỡng → trả copywriter kèm 1–3 sửa cụ thể nhất.
**Ghi DB:** `python tools/db.py x "UPDATE posts SET judge_score=<n>, judge_note='<R?: ...>' WHERE id=<id>"`.

## Phần QC — mẫu quảng cáo trả tiền (`loai: quang-cao`, thêm 15/10/2026)
Chấm **sau khi** compliance ghi `[QC] OK`. Dùng **thay** R1–R8 cho file `content/qc/…`. Căn cứ: skill `quang-cao-bds` §8, `workspace/research/2026-10-14-best-practice-quang-cao-bds.md` §A7.

| # | Tiêu chí | 5 điểm | 3 điểm | 1 điểm |
|---|---|---|---|---|
| Q1 | **3 giây đầu** | Câu mở/khung đầu là nỗi lo hoặc mong muốn cụ thể của người mua (sổ, con cái, đất quê) | Có móc nhưng chung chung | Mở bằng tên dự án / lời chào |
| Q2 | **Bằng chứng thật** | Dựa trên tư liệu thật có nguồn (`can_cu`), người thật có `dong_y` | Có tư liệu nhưng chưa rõ nguồn | Không bằng chứng / ảnh minh hoạ chung |
| Q3 | **Đúng 1 nhóm người** | Rõ đang nói với ai (cha mẹ – con, đi làm xa, KCN…), khác góc các mẫu cùng đợt | Hơi chung | Nói với tất cả |
| Q4 | **Lời kêu gọi & bước tiếp** | 1 nút rõ, nói trước điều xảy ra sau khi để số (gọi lại trong ít phút, gửi mặt bằng, lịch xem đất) | Có nút nhưng không nói bước tiếp | Không CTA / CTA ép |
| Q5 | **Đúng kỹ thuật Meta** | Phần trước "Xem thêm" ≤ 125 ký tự, tiêu đề ≤ 40, mô tả ≤ 30; video 9:16 có phụ đề; có dòng (*) nếu có số | Lệch 1 giới hạn | Lệch ≥ 2 |
| Q6 | **Giọng sales BĐS** | Thẻ luật: xưng em, câu ngắn, ✅, chân thật; không mùi AI | Hơi quảng cáo | Hô hào, viết hoa cả câu, nhiều emoji |

**Ngưỡng QC:** ≥ 24/30 và không tiêu chí nào < 3. Ghi `judge_qc: <điểm> | <Q?: sửa gì>` vào frontmatter file QC.
