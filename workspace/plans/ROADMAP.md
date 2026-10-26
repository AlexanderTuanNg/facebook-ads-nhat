# ROADMAP tổng: KDC Đồng Lạc (bản 2, 2026-09-24)

> Kế hoạch tổng, chia theo giai đoạn. Kế hoạch tuần nằm ở `workspace/plans/2026-W*.md`; trạng thái từng ngày nằm ở `STATE.md`.
> Bản 2 bổ sung những bài học từ kênh Nguyễn Trọng Hữu (lấy insight từ tin nhắn, pipeline lead, chăm lại khách cũ, "thuê hạ tầng, tự xây quy trình") và nguồn dữ liệu mới: tài khoản quảng cáo của đội môi giới.

## Tư duy áp dụng (không đổi)
1. **Vòng ngoài chọn việc đáng làm:** mỗi giai đoạn phải gỡ đúng **nút thắt lớn nhất** (SCORECARD H1). Không làm chỉ vì làm được (H4).
2. **Vòng trong làm và kiểm chứng:** mỗi việc là một task có tiêu chí nghiệm thu và bằng chứng. **Người làm ≠ người kiểm.**
3. **Số liệu thật thay suy đoán:** mọi thay đổi playbook phải có số liệu làm bằng chứng. Đã dùng thẳng lời khách thì phải truy được về dòng gốc.
4. **Lỗi thật thành ca eval:** mỗi lỗi lọt ra ngoài thêm 1 ca eval để không lặp lại.
5. **Trao quyền dần (L0–L4):** tính năng mới bắt đầu ở mức người duyệt từng việc, đủ lịch sử mới nới.
6. **Thuê hạ tầng, tự xây quy trình** (bài học từ Hữu): phần kết nối kênh (API Meta, Zalo OA, Smax…) dùng thứ có sẵn và chính thức; chỉ tự xây phần quy trình riêng (phân loại, pipeline, kịch bản).
7. **Từng bước một:** người dùng chỉ nhận 1 việc tại một thời điểm (STATE).

## Nút thắt hiện tại (vì sao đổi thứ tự ưu tiên)
- Persona, câu mở đầu và thông điệp đều đang là **[ĐỀ XUẤT]** (Claude tự đoán). Đây là rủi ro hướng đi lớn nhất: viết giỏi đến đâu cũng có thể viết nhầm đối tượng.
- **Vừa mở khoá (24/09):** quyền vào tài khoản quảng cáo của đội môi giới, là nơi có số liệu thật về khách (tiền tiêu → tin nhắn → lead, comment dưới quảng cáo).
- H3 (đo lead đạt chuẩn) chưa đạt: bảng `leads` chưa có giai đoạn, người phụ trách, hạn chăm sóc.

---

## GĐ1: Test group (đang chạy, tuần 40)
Giữ nguyên `2026-W40-group-test.md`: 10 bài, nick cá nhân, nhánh A.
- **Nghiệm thu:** 1 bài lên group (`fb_group.py stats`), selector đã hiệu chỉnh.
- **Bổ sung từ bản 2:** comment và inbox phát sinh từ 10 bài được lưu nguyên văn vào kho lời khách (GĐ2).

## GĐ2: Kho "lời khách" (voice of customer), chạy song song GĐ1
**Vì sao:** gỡ nút thắt persona [ĐỀ XUẤT]. Đây là bài 1 của Hữu, áp dụng theo tư duy kiểm chứng.

| Bước | Việc | Người làm | Người kiểm | Bằng chứng nghiệm thu |
|---|---|---|---|---|
| 2.1 | Xuất báo cáo Ads Manager 90 ngày (CSV) vào `assets/dong-lac/ads/` | Người dùng | Lead (mở file, đếm dòng) | File tồn tại, số dòng > 0 |
| 2.2 | Phân tích quảng cáo: top/bottom theo chi phí mỗi tin nhắn/lead, góc nói, đối tượng, khung giờ | analyst | judge (tính lại 3 con số ngẫu nhiên từ CSV) | `workspace/research/ads-moi-gioi.md`, 0 số lệch |
| 2.3 | Thu lời khách: comment dưới quảng cáo, inbox (đội môi giới xuất/dán, đã **xoá tên và số điện thoại**), comment group GĐ1 | Người dùng / engager | Lead | `assets/dong-lac/voc/*.txt` |
| 2.4 | Phân loại: nỗi lo, lý do chần chừ, câu hỏi hay gặp, câu nguyên văn, giai đoạn mua | analyst | judge: **mỗi câu nguyên văn phải tìm thấy trong file gốc** | `workspace/research/voice-of-customer.md` (kèm tần suất + dòng nguồn) |
| 2.5 | Viết lại persona và câu mở đầu từ bằng chứng; playbook v3 | Lead (chỉ Lead sửa playbook) | judge | `playbook_changes` ghi rõ số liệu làm căn cứ; bỏ nhãn [ĐỀ XUẤT] ở persona có dữ liệu |

**Thay đổi hệ thống kèm theo:**
- Rubric: thêm tiêu chí "Bài có dùng nỗi lo/câu hỏi có trong kho lời khách không".
- Eval: thêm ca "câu trích dẫn khách không có trong kho" → phải REJECT (bài 8 từng dính trích dẫn giả).

## GĐ3: Pipeline lead ("hôm nay gọi ai?"), sau GĐ2
**Vì sao:** H3/B1 phải đo lead đạt chuẩn, không chỉ đếm like. Đây là bài 2 của Hữu (quản lý theo cơ hội, dữ liệu thuộc về công ty) và FourLand CRM.

| Bước | Việc | Người làm | Người kiểm | Bằng chứng |
|---|---|---|---|---|
| 3.1 | `db.py`: bảng `leads` thêm giai đoạn (mới → đã tư vấn → hẹn xem → đi xem → cọc → ký), người phụ trách (môi giới/CĐT), hạn chăm sóc tiếp, nguồn (bài/QC/group), nhật ký trao đổi | Claude | judge (chạy lệnh thử, đọc lại DB) | Output lệnh + test |
| 3.2 | Mỗi lead có thể có nhiều **cơ hội** (lô quan tâm, mục đích mua) | Claude | judge | Tạo 1 lead có 2 cơ hội, đọc lại |
| 3.3 | Lệnh `db.py today`: khách đến hạn chăm sóc, khách vừa tương tác, deal bị dừng quá N ngày | Claude | judge | Output trên dữ liệu mẫu |
| 3.4 | `/lead daily` in danh sách "hôm nay gọi ai" | Lead | Người dùng | 1 tuần dùng thật |
| 3.5 | (Nếu làm với đội môi giới) theo dõi hoa hồng 6% theo từng deal | Claude | judge | Khi đã chốt phương án hoa hồng |

**Nghiệm thu GĐ3:** SCORECARD B1 tính được từ DB (`lead đạt chuẩn` = có SĐT + cơ hội + đã gọi xác minh).

## GĐ4: Chăm lại khách cũ, sau khi GĐ3 có dữ liệu
**Vì sao:** khách đã hỏi nhưng dừng là nhóm rẻ nhất để kéo lại. Đây là bài 1 (phần retarget) của Hữu, làm theo thang trao quyền.

| Bước | Việc | Người làm | Người kiểm | Bằng chứng |
|---|---|---|---|---|
| 4.1 | engager đọc lịch sử lead và soạn **tin mở lời riêng cho từng người** (nối tiếp đúng chỗ khách dừng) | engager | compliance (tin nhắn cũng qua lint: không giá, không cam kết) | Nháp trong DB |
| 4.2 | **Người gửi tay** (L1): sale copy tin rồi gửi bằng Messenger/Zalo của chính mình | Người dùng / môi giới | n/a | Đánh dấu "đã gửi" trong DB |
| 4.3 | Đo tỉ lệ trả lời theo kiểu mở lời | analyst | judge | Báo cáo tuần |
| 4.4 | Chỉ khi cần gửi số lượng lớn: dùng kênh chính thức (Page Marketing Messages, Zalo OA/ZNS, hoặc Smax gắn Page/OA) | Quyết định của người dùng | n/a | Mức L3+ |

**Không lấy từ bài của Hữu:** gắn thẻ `HUMAN_AGENT` cho tin tự động; bot gửi từ Zalo cá nhân với giãn cách ngẫu nhiên. Cùng lý do với việc tắt nhánh B (uy tín CĐT, rủi ro khoá Page/nick).

## GĐ5: Fanpage và gom kênh
- Tạo Page, token Graph API, chuyển bớt bài từ group sang Page (như roadmap cũ).
- Inbox Page đọc qua API chính thức, tự đổ vào kho lời khách (GĐ2) và pipeline (GĐ3).
- **Điểm quyết định thuê Smax:** khi có từ 3 kênh inbox trở lên (Page, Zalo OA, Page của môi giới…) hoặc > 30 hội thoại/ngày. Khi đó dùng Smax làm lớp gom kênh, tool này làm phần quy trình (đúng nguyên tắc 6). Trước ngưỡng đó thì không mua.

## GĐ6: Quảng cáo trả tiền (cùng đội môi giới)
- Từ kho lời khách và kết quả test group: copywriter viết bộ mẫu quảng cáo; judge chấm; người dùng/đội môi giới duyệt rồi tự lên quảng cáo (Claude **không sửa** tài khoản quảng cáo).
- **Điều kiện bắt buộc:** chuyển `compliance_mode = strict` trước khi chạy tiền (quyết định 23/09).
- Đo: chi phí mỗi lead đạt chuẩn (lấy từ GĐ3), không dừng ở chi phí mỗi tin nhắn.

---

## Thứ tự và phụ thuộc
```
GĐ1 test group ─────────────┐
GĐ2 kho lời khách (song song)┴─► playbook v3 ─► GĐ3 pipeline ─► GĐ4 chăm lại
                                                   │
                                                   └─► GĐ5 Page/gom kênh ─► GĐ6 Ads (strict)
```

## Thay đổi SCORECARD đề xuất (Lead áp dụng ở `/lead review` gần nhất)
- **H6 (mới):** "Tuần này có quyết định nội dung nào dựa trên lời khách/số liệu QC thật không?"
- **B5:** tính thêm "% persona/hook có bằng chứng từ kho lời khách".
