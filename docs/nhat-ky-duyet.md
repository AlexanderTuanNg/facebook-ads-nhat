# Nhật ký duyệt (Gemini kiến trúc sư trưởng)

| Ngày giờ | Việc | Cổng | Kết luận | Sửa đổi đã áp dụng |
|---|---|---|---|---|
| 2026-09-25 15:5x | (A) Giảm ngưỡng compliance — spec bản 1 | duyet_spec | DUYỆT | Làm theo lời khuyên: sao lưu 2 file trước khi sửa; so đáp án kiểm thử bằng script (không cần agent chấm). Câu hỏi của Gemini "báo kết quả ở đâu" → Lead tự quyết: file `workspace/reports/eval-compliance-2026-09-25.md` + tóm tắt trên màn hình. |
| 2026-09-25 16:0x | (A) bản 2 (thêm "giảm thêm, kéo nhiều khách nhất") | duyet_ke_hoach | DUYỆT | Không cần sửa. Gemini đồng ý: mồi tương tác → GHI CHÚ + thử ≤ 1/3 số bài/tuần; không tự bỏ luật không nêu giá/mã lô (hỏi chủ dự án). |
| 2026-09-26 11:5x | Phương án đăng bài v3 (`workspace/plans/2026-09-26-phuong-an-v3.md`) | duyet_ke_hoach | vòng 1 SỬA RỒI DUYỆT → vòng 2 **DUYỆT** | Giảm việc cho người dùng: chỉ xin 3–5 ảnh chụp nhanh; đo lead bằng mã riêng mỗi bài trong lời mời (Claude phản biện link rút gọn: group hay xoá bài có link, Claude không đọc được Messenger cá nhân — Gemini đồng ý); tuần đầu 2 khung giờ 11:30, 20:00. |

## Nguyên văn trả lời của Gemini

### 2026-09-25 15:5x — duyet_spec (A) bản 1
KẾT LUẬN: DUYỆT
1. Nhận định chung: Spec này giải quyết chính xác điểm đau thực tế (agent hay bắt bẻ câu cú đời thường, làm bài viết cứng nhắc và giống AI), đồng thời giữ vững các rào chắn pháp lý cốt lõi. Hướng đi tách bạch rõ ràng giữa CHẶN (vi phạm thật) và GHI CHÚ (góp ý văn phong) là hoàn toàn hợp lý.
2. Hướng đi đề xuất: Cập nhật prompt và checklist của agent compliance thành hai tầng xử lý rõ ràng, kèm bộ 14 ca kiểm thử chạy tự động bằng script. Không nới lỏng lint máy hay giới hạn an toàn. Mức tin: Cao
3. Rủi ro & đánh đổi: Rủi ro agent buông lơi các câu mơ hồ về dự án được giảm thiểu bằng luật "khi phân vân nghiêng về CHẶN". Việc tách ghi chú ngắn gọn (dưới 500 ký tự) giúp người dùng dễ đọc, tránh sót điều kiện quan trọng như bài học trước đây. Chi phí token kiểm thử tăng nhẹ nhưng nằm trong tầm kiểm soát và hoàn toàn xứng đáng với chất lượng đầu ra.
4. Nên làm trước / có thể bỏ: Nên làm trước: Sao lưu 2 file (prompt và checklist) trước khi chỉnh sửa vì dự án chưa có hệ thống quản lý mã nguồn (git). Có thể bỏ: Không cần dùng agent riêng để chấm điểm kiểm thử mà dùng script so sánh trực tiếp với đáp án (như mục 6 đã nêu) để tiết kiệm thời gian và chi phí.
5. Câu hỏi cần hỏi chủ dự án: Anh/chị muốn script kiểm thử tự động báo cáo kết quả vào đâu (file log hay hiển thị trực tiếp trên màn hình) để dễ theo dõi nhất?
[ket_luan=DUYỆT model=gemini-3.1-pro-thinking]

### 2026-09-25 16:0x — duyet_ke_hoach (A) bản 2
KẾT LUẬN: DUYỆT
1. Nhận định chung: Kế hoạch bản 2 rất sắc sảo, giải quyết chính xác điểm nghẽn "chặn oan do quá cẩn trọng" làm mất lực bán, đồng thời bảo vệ tuyệt đối "sàn cứng" pháp lý và an toàn nick. Việc phân định rõ giữa CHẶN và GHI CHÚ giúp tối ưu hóa chuyển đổi mà không rủi ro.
2. Hướng đi đề xuất: Tách bạch rõ nhóm vi phạm cứng (chặn) và góp ý cải thiện (ghi chú), kết hợp chạy test tự động trong bản sao tạm (tuân thủ tuyệt đối BH-0007). Mức tin: Cao.
3. Rủi ro & đánh đổi: Mồi tương tác (engagement bait) có thể khiến Meta giảm nhẹ phân phối reach của bài viết (giải quyết bằng cách giới hạn thử nghiệm dưới 1/3 số bài/tuần). Lọt một số câu chữ mơ hồ hơn (được bù đắp bằng việc giữ nguyên "sàn cứng" và người dùng thực tế vẫn duyệt từng bài cuối cùng). Chi phí token tăng nhẹ cho các ca kiểm thử agent mới (trong tầm kiểm soát).
4. Nên làm trước / có thể bỏ: Nên làm trước: Sao lưu 2 file prompt/checklist ra thư mục backup có ngày tháng trước khi sửa, và thiết lập môi trường test chạy trên thư mục tạm. Có thể bỏ: Không tự ý bỏ quy định không nêu giá/mã lô của công ty (đúng như kế hoạch đã khoanh vùng chờ hỏi chủ dự án).
5. Câu hỏi cần hỏi chủ dự án: Công ty có muốn thay đổi quy định nội bộ để cho phép nhân viên nêu giá cụ thể và mã lô trực tiếp trong bài đăng nhằm tăng tỷ lệ chốt khách nhanh hơn không?
[ket_luan=DUYỆT model=gemini-3.1-pro-thinking]

## 2026-09-26 14:3x–14:5x — duyet_ke_hoach: Kết bạn với 29 lead chưa nhận tin mở đầu
- Vòng 1: **SỬA RỒI DUYỆT** — (1) tối đa 5 lời mời/ngày trong 2 ngày đầu; (2) chỉ chạy trước 17:00; (3) khoá cứng hồ sơ trình duyệt để job đăng bài 19:55 bỏ qua khi hồ sơ bận. Bỏ: huỷ lời mời sau 7 ngày. → Áp dụng (1), (2); (3) mới gắn vào công cụ kết bạn/nhắn tin (phản biện: chưa sửa code đăng bài vài giờ trước job 19:55).
- Vòng 2: **SỬA RỒI DUYỆT** — (1) gắn khoá vào tiến trình đăng bài ngay hôm nay (chỉ thêm kiểm tra khoá); (2) ghi nhật ký PROFILE_BUSY ra file riêng. → Áp dụng: `tools/khoa_ho_so.py` + `fb_group.open_context` gọi `lay_khoa`; nhật ký `data/profile_busy.log`; 12/12 ca thử (gồm `fb_group.py check` thật: OK; bận → chặn trong 0,5 s). Đã báo phiên gốc.
- Vòng 3: **DUYỆT** (gemini-3.1-pro-thinking). Chạy: lead 4 thử riêng + đọc ảnh chụp → lead 5–8 chạy nền, xem từng ảnh.

## 2026-09-26 14:5x — duyet_ke_hoach: Tăng tốc đăng bài 4 khung/ngày, Claude tự đăng (`workspace/plans/2026-09-26-tang-toc-dang-bai.md`)
- Vòng 1: **SỬA RỒI DUYỆT** — (1) giữ "mỗi group ≥ 3 ngày"; (2) hoãn bài công khai trên trang cá nhân nick chiều nay; (3) 4 khung/ngày tăng dần theo số group đủ điều kiện, không ép tuần này. → Áp dụng cả 3.
- Vòng 2: **DUYỆT**. Chạy: hạn mức tuần 12 → 35 (ngày 9 → 6 và cách 5 → 20 phút đổi sau loạt 20:00 để không chặn 2 bài tối nay); bài 17 → CN 27/09 11:40; `tools/lich_dang.py` (12/12 ca thử xử lý kết quả, chạy khô OK) chạy nền tới 04/10; 9 khung bài v3 (post 19–27) giao copywriter.
