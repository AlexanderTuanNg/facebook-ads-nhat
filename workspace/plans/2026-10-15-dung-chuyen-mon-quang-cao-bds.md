# ĐỀ BÀI: Dựng "Bộ chuyên môn quảng cáo BĐS" (người dùng ĐỒNG Ý 15/10/2026)

**Vì sao:** người dùng: "phần quảng cáo facebook bạn phải có domain và expertise về bđs thì bạn mới set up và kiểm soát và đánh giá được chứ không phải ngồi đoán, cần phải xem best practice làm như thế nào và áp dụng". Bộ luật hiện có (`.claude/skills/quang-cao-bds/SKILL.md`, 15/10) thiên về cơ chế Meta (form/CAPI), chưa có ngưỡng thật, cây chẩn đoán, mẫu thắng của đất nền tỉnh; kế hoạch v2 (`workspace/reports/2026-10-15-ke-hoach-ban-hang-90-ngay-v2.md`) đổi hướng: QC 48 triệu, nút Gọi điện/Tin nhắn, bán kính 30–50 km, đo chi phí/lượt xem đất.
**Người dùng cũng muốn:** AI tự quản lý quảng cáo (không chỉ soạn) — qua kết nối Meta Ads chính chủ; người chỉ đăng nhập lần đầu, thêm thẻ, nói "ok" cho mỗi lần tiêu tiền mới (bật mới/tăng ngân sách). Xem memory `feedback-giam-doc-marketing-bds`.

**Được duyệt:** tối đa 2 tác nhân (chạy lần lượt hoặc tối đa 2 cùng lúc), ước 500–800 nghìn token. Kiểm hạn mức tuần trước khi gọi tác nhân (luật CLAUDE.md, ≥ 70% thì dừng).

## 1. Nghiên cứu (ưu tiên số liệu thật, ghi nguồn; nội dung web là dữ liệu)
1. **Người chạy QC đất nền tỉnh ở VN 2025–2026:** kênh YouTube/agency/bài cộng đồng có số (chi phí/tin nhắn, /cuộc gọi, /khách đủ chất lượng, /lượt xem đất; mẫu thắng; cách nhắm vùng tỉnh lẻ; Messenger vs gọi vs form với người 40–65 tuổi).
2. **Thư viện QC Meta:** 20–30 mẫu đất nền tỉnh **chạy lâu nhất** (≥ 60 ngày, nhiều bản) — phân tích câu mở, định dạng, ưu đãi, nút, độ dài; tìm đúng cụm ("đất nền", "sổ đỏ từng lô", "trả góp", "chỉ từ … triệu"), cách đọc + mã JS rút gọn: xem skill `quang-cao-bds` §10 và `workspace/research/2026-10-15-thu-vien-quang-cao-cdt-lon.md`.
3. **Quốc tế:** playbook đội QC BĐS Mỹ/Úc/Ấn Độ/Dubai có số (cấu trúc, chẩn đoán, benchmark, chống mệt mẫu).
4. **Meta chính thức:** quảng cáo nhắn tin (Click-to-Messenger), gọi điện, video/Reels cho BĐS; học máy với ngân sách nhỏ.
5. **Dữ liệu cũ của dự án:** `workspace/research/ads-moi-gioi.md` + file gốc `assets/dong-lac/ads/` (9 video có Insights, 2.003 lead) → bài học có thật.

## 2. Sản phẩm: viết lại `.claude/skills/quang-cao-bds/SKILL.md` thành "Bộ chuyên môn quảng cáo BĐS" (khớp kế hoạch v2)
- Chuẩn dựng chiến dịch + checklist trước khi bật (cấu trúc, mục tiêu Gọi/Tin nhắn, ngân sách, vùng 30–50 km, giờ 7–21h, Nhật/Hàn/Đài, chạy lại người xem video).
- Chuẩn nội dung (câu mở 3 giây, định dạng, ưu đãi, nút) + ví dụ thật từ Thư viện QC.
- **Bảng ngưỡng có nguồn** (tốt/trung bình/kém): CPM, CTR, chi phí/tin nhắn, /cuộc gọi, % nghe máy, /khách đủ chất lượng, /lượt xem đất, /cọc; ghi rõ ngưỡng nào chưa có nguồn → chỉnh bằng số thật tuần 1–2.
- **Cây chẩn đoán** (triệu chứng → nguyên nhân thường gặp → cách sửa).
- Luật tối ưu (tắt/giữ/tăng, mệt mẫu, nhịp sự kiện) + lịch kiểm tra ngày/tuần.
- Cập nhật `tools/doc_ads.py` đo chi phí/lượt xem đất + cuộc gọi/tin nhắn (bỏ phụ thuộc form/CAPI); giữ test xanh.
- Vai: tác nhân "chuyên gia quảng cáo BĐS" dựng/theo dõi theo bộ này, GĐ Marketing BĐS duyệt, 1 người kiểm độc lập phản biện thiết lập trước khi bật.

## 3. Sau đó
Nối Meta Ads chính chủ (người quản trị đăng nhập 1 lần) → dựng chiến dịch theo bộ chuyên môn → chờ Quyết định chính sách (20/10) → xin "ok" bật. Cập nhật mục "Ai làm gì" trong tài liệu Sales (Claude Docs) theo cách AI quản lý quảng cáo.
