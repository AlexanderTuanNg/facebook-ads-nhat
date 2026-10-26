---
loai: quang-cao
ma_qc: QC-VM3          # biến thể A/B của QC đang chạy "Yên thế Video Mới." (giữ video cũ, thay chữ). Bản gốc = QC-VM2 (phần B của workspace/plans/2026-10-20-tin-gui-nguoi-chay-qc.md)
y_tuong: QC-VM
khung_mo: so-do
dinh_dang: video-9x16    # giữ video đang chạy (creative 2188265765441845) — CHƯA ai soát lời/chữ trong video
cau_mo: "Ngày 9/10, chủ đầu tư đã bàn giao sổ đỏ cho các gia đình đã mua đất tại Yên Thế Golden Hill."
tieu_de: "Đã bàn giao sổ đỏ ngày 9/10"     # 27 ký tự
mo_ta: "Trung tâm xã Yên Thế"              # 20 ký tự
nut: Gửi tin nhắn
dong_y: ""               # bản chữ không dùng ảnh/lời người thật; nếu ghép ảnh trao sổ → dẫn quyet-dinh.md 09/10
can_cu: "[DỮ LIỆU] lễ bàn giao GCN 09/10/2026 (quyet-dinh.md 09/10; brief tư liệu #9); KM7b MỞ tới 13/11; câu F5; brief §1.1 (377 lô, 82–185 m², TL 292); khung so-do: 22/30 mẫu đất nền chạy lâu nhắc sổ (thu-vien-qc-dat-nen-chay-lau §2)"
status: draft
---

# QC-VM3 — biến thể "sổ đỏ làm bằng chứng" cho video đang chạy

Dùng cùng video, cùng nhóm quảng cáo với bản gốc QC-VM2 (câu mở giá/vốn) để so A/B. Không thay bản gốc.

## Văn bản chính (dán nguyên)

```text
🎉 Ngày 9/10, chủ đầu tư đã bàn giao sổ đỏ cho các gia đình đã mua đất tại Yên Thế Golden Hill.

Anh chị đang tìm mảnh đất có sổ ở quê?
CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU (*)

✅ Trung tâm xã Yên Thế, thành phố Bắc Ninh (khu vực Yên Thế – Bắc Giang cũ)
✅ Lô 82–185 m², có dãy lô mặt đường TL 292 (lô mặt đường giá riêng)
✅ Đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô
✅ Có người dẫn anh chị đi xem đất trực tiếp tại khu

📲 Bấm "Gửi tin nhắn", em gửi ảnh buổi bàn giao sổ và vị trí lô cho nhà mình ạ.
#YenTheGoldenHill
(*) Thông tin theo chính sách của Chủ đầu tư tại thời điểm đăng, áp dụng có điều kiện.
```

- Phần trước "Xem thêm": dòng đầu = 94 ký tự (≤ 125).
- Không ghi số điện thoại (giống bản gốc, để A/B công bằng; khách bấm nhắn tin).
- Không xưng "em bên chủ đầu tư": QC đang chạy từ Trang "Bán đất Phân lô tại Bắc Giang", chưa phải Fanpage CĐT (H7).

## Tin chào tự động (2 câu)
"Dạ em chào anh/chị, em gửi anh/chị ảnh buổi bàn giao sổ 9/10 và vị trí lô ở Yên Thế Golden Hill ạ."
"Anh/chị cho em xin SĐT hoặc Zalo, em gửi ảnh và tính thử cho nhà mình ạ (*)."
Nút bấm sẵn: *Gửi em ảnh sổ + vị trí* · *Em ở gần Yên Thế/Tân Yên* · *Mua cho con*.

## Kiểm
- `python -X utf8 tools/db.py lint --text "<văn bản chính>"` → **PASS** (20/10).
- §H tự đối chiếu (người viết, chưa phải người kiểm độc lập):

| Mục | Kết quả |
|---|---|
| H1 điều kiện chạy | CHẶN (đã biết, chung mọi QC): website CĐT, dòng PL, Fanpage CĐT chưa xong. Người dùng đã "ok" chạy tiếp QC đang chạy trong lúc chờ (quyet-dinh.md 20/10) |
| H2 so sánh đối thủ | OK — không nêu ai |
| H3 người thật | OK — chữ không dùng tên/ảnh khách; không nêu số khách nhận sổ |
| H4 hứa lời | OK |
| H5 quà/bốc thăm | OK — không có |
| H6 khan hiếm/đám đông | OK |
| H7 danh tính | CHẶN (đã biết) — Trang không phải Fanpage CĐT; chữ đã bỏ câu tự xưng CĐT |
| H8 dòng (*) | OK — có (*) sau giá và cuối bài; "9/10", "82–185 m²", "TL 292" nằm dưới dòng (*) |
| H9 form | Không dùng form |
| H10 nhắm | Theo danh sách sửa: bỏ Hoa Kỳ (workspace/plans/2026-10-20-sua-qc-dang-chay.md) |
| H11 kỹ thuật | OK — mở bằng sự kiện thật, không mở bằng tên dự án; tiêu đề 27, mô tả 20 ký tự |
| §G | KM7b MỞ (tới 13/11); trao sổ 09/10 có trong quyet-dinh.md; F5 nguyên văn. Không dùng KM4, KM6, KM8–KM10 |

## [CẦN XÁC NHẬN]
- Lời nói và chữ trong video cũ: nếu video có "hơn 1 tỷ", "sổ đỏ cầm tay", "pháp lý rõ ràng", "1,5km", số 0948… thì chữ mới ("dưới 1 tỷ") sẽ **ngược** với video → phải cắt đoạn đó khỏi video trước khi dùng (áp dụng cả bản gốc QC-VM2).
