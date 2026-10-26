---
loai: quang-cao
ma_qc: QC-VM4          # biến thể A/B thứ 2 của QC đang chạy "Yên thế Video Mới." (giữ video cũ, thay chữ). Bản gốc = QC-VM2
y_tuong: QC-VM
khung_mo: cau-hoi-von
dinh_dang: video-9x16    # giữ video đang chạy (creative 2188265765441845) — CHƯA ai soát lời/chữ trong video
cau_mo: "Làm KCN mấy năm, dành dụm được ít vốn — có mua nổi mảnh đất có sổ ở quê không anh chị?"
tieu_de: "Làm KCN, về quê có đất có sổ"    # 28 ký tự
mo_ta: "Chỉ dưới 1 tỷ (*)"                 # 17 ký tự
nut: Gửi tin nhắn
dong_y: ""
can_cu: "[DỮ LIỆU] 2 vòng 16 km của QC đang chạy phủ TP Bắc Giang cũ + khu VSIP Từ Sơn (báo cáo 20/10 §3d) = tệp người làm KCN; ưu tiên nhóm KCN/đồng hương (quyet-dinh.md 14/10); khung câu hỏi vốn: Heragon City (thu-vien-qc-dat-nen-chay-lau mẫu 19); KM7b MỞ tới 13/11; câu F5; brief §1.1"
status: draft
---

# QC-VM4 — biến thể "câu hỏi vốn cho người làm KCN" cho video đang chạy

Cùng video, cùng nhóm quảng cáo với QC-VM2 (giá/vốn) và QC-VM3 (sổ đỏ). Vì vùng đang nhắm là quanh KCN, câu mở hỏi đúng nỗi lo của người làm KCN.

## Văn bản chính (dán nguyên)

```text
🏭 Làm KCN mấy năm, dành dụm được ít vốn — có mua nổi mảnh đất có sổ ở quê không anh chị?

Ở Yên Thế Golden Hill:
CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU (*)

✅ Trung tâm xã Yên Thế, thành phố Bắc Ninh (khu vực Yên Thế – Bắc Giang cũ)
✅ Lô 82–185 m², đường nhựa, đèn đường, quảng trường trong khu
✅ Đủ điều kiện chuyển nhượng, ký hợp đồng công chứng, sang tên GCN từng lô
✅ Bố mẹ ở quê qua xem đất trước, có người dẫn đi xem trực tiếp

📲 Bấm "Gửi tin nhắn", cho em biết anh chị làm KCN nào, em tính thử cho nhà mình ạ.
#YenTheGoldenHill
(*) Thông tin theo chính sách của Chủ đầu tư tại thời điểm đăng, áp dụng có điều kiện.
```

- Phần trước "Xem thêm": dòng đầu = 88 ký tự (≤ 125).
- Cố ý **không** nói khoảng cách/thời gian tới KCN hay CCN Tân Sỏi (chưa có căn cứ; thẻ luật góc 13 cấm).
- "đường nhựa, đèn đường, quảng trường" = những gì thấy trong ảnh flycam (thẻ luật "Dữ kiện được dùng").

## Dòng CHỜ — chỉ thêm khi có Quyết định chính sách (KHÔNG nằm trong văn bản chính)
"💥 Trả trước từ 500 triệu, phần còn lại trả dần theo chính sách Chủ đầu tư (*)"
→ `[CẦN XÁC NHẬN: số + ngày Quyết định chính sách thanh toán của CĐT]`. Lint dòng này: **FAIL F1** ('500 triệu') — đúng như dự kiến, chỉ mở khi có văn bản và người dùng thêm mốc vào `config/banned_terms.json`. Lưu ý kế hoạch v2 mục 5–6: lô > 1,3 tỷ trả trước 40%, và **không bán gói trả dần cho công nhân đứng tên một mình mua lô trên 1 tỷ** → câu này hợp hơn với mẫu "bố mẹ lo phần đầu" (QC-B1) hơn là nói thẳng với công nhân.

## Tin chào tự động (2 câu)
"Dạ em chào anh/chị, anh/chị đang làm KCN nào và muốn tìm đất ở gần Yên Thế/Tân Yên phải không ạ?"
"Anh/chị cho em xin SĐT hoặc Zalo, em gửi ảnh sổ, vị trí lô và tính thử cho nhà mình ạ (*)."
Nút bấm sẵn: *Gửi em ảnh sổ + vị trí* · *Em làm KCN, muốn mua ở quê* · *Bố mẹ mua cho con*.

## Kiểm
- `python -X utf8 tools/db.py lint --text "<văn bản chính>"` → **PASS** (20/10).
- §H tự đối chiếu (người viết, chưa phải người kiểm độc lập):

| Mục | Kết quả |
|---|---|
| H1 điều kiện chạy | CHẶN (đã biết, chung mọi QC) — người dùng đã "ok" giữ QC đang chạy trong lúc chờ |
| H2 so sánh đối thủ | OK — không nêu dự án KCN nào khác, không "rẻ hơn" |
| H3 người thật | OK — không dùng tên/ảnh khách |
| H4 hứa lời | OK — không nói tăng giá, không "đầu tư" |
| H5, H6, H9 | OK — không quà, không khan hiếm, không form |
| H7 danh tính | CHẶN (đã biết) — Trang không phải Fanpage CĐT; chữ không tự xưng CĐT |
| H8 dòng (*) | OK — (*) sau giá, trong mô tả và cuối bài |
| H10 nhắm | Theo danh sách sửa (bỏ Hoa Kỳ) |
| H11 kỹ thuật | OK — mở bằng nỗi lo người mua; tiêu đề 28, mô tả 17 ký tự |
| §G | KM7b MỞ (tới 13/11); F5 nguyên văn; không dùng KM3 (quảng trường chỉ nêu là có, không nói "tối nào cũng đông"), KM4, KM6, KM8–KM10 |

## [CẦN XÁC NHẬN]
- Lời/chữ trong video cũ (như QC-VM3): nếu video nói "hơn 1 tỷ"/"sổ đỏ cầm tay"/"1,5km" thì phải cắt đoạn đó trước khi chạy bản chữ này.
- Quyết định chính sách "trả trước từ 500 triệu" (dòng CHỜ ở trên).
