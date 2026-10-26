# Bộ khung agent dùng chung — ghi chép brainstorm (28/09/2026 tối, chưa phải spec)

**Người dùng muốn:** một bộ khung để dựng hệ thống agent cho nhiều mục đích, không chỉ đăng Facebook.
**Người dùng chốt:** mục đích để sau, **mỗi lần bắt đầu hệ thống mới khung phải hỏi người dùng trước**; chọn **Hướng 1: mẫu + lệnh khởi tạo**
(không chọn: bộ công cụ toàn cục; chép dự án FB rồi gọt); không đụng hệ thống FB đang chạy; **phần 1 thiết kế DUYỆT** ("được r, tính sau").

**Phần 1 (đã duyệt):**
- Nơi đặt `C:/Users/ADMIN/ai-projects/_khung-agent/` (giữ `_mau-du-an` cho dự án 1 AI).
- Gồm: Lead (`/lead next|daily|status`, 2 vòng lặp, báo 1 bước); thư viện 7 vai (Nghiên cứu, Lập kế hoạch, Thực hiện, Kiểm luật, Giám khảo độc lập,
  Hành động ra ngoài — luôn qua cổng duyệt, Đo lường), chỉ bật vai cần; STATE ≤ 8 KB + sổ quyết định + sổ bài học + bảng việc có bằng chứng (DB nhỏ);
  rubric + 3–5 ca kiểm tra + thang tự chủ L0–L4 (bắt đầu L1); mô-đun tuỳ chọn: lịch Windows, điều khiển trình duyệt.
- Khởi tạo: `/tao-he-agent <tên>` (skill toàn cục nhỏ) → tạo `ai-projects/<tên>/`, chép khung, git → phỏng vấn ~10 câu (mục tiêu + con số "đạt";
  dữ liệu vào; sản phẩm ra; gửi/đăng/xoá/chi tiền + ai duyệt; luật riêng; chạy khi chat hay theo lịch; ưu tiên hạn mức; lịch báo cáo) → sinh CLAUDE.md,
  đề bài, agent cần, rubric, ca kiểm tra → chạy thử 1 việc có bằng chứng → người dùng mở phiên mới, `/lead next`.

**Còn lại (phiên mới, sau 03/10 12:00):** phần 2 = luật vận hành cài sẵn (bài học FB: báo 1 bước; [DỮ LIỆU]/[NGUỒN]/[GIẢ THUYẾT]; hợp đồng việc +
người kiểm ≠ người làm; việc ra ngoài cần chủ sở hữu đồng ý trong đúng phiên; hạn mức dùng chung: ≥ 70% chỉ dừng việc của Claude, việc nền Python vẫn chạy,
ưu tiên giữa các hệ thống; tối đa 2 agent; maker Sonnet/checker Opus; máy kiểm trước AI kiểm sau; việc nền bằng Windows Task Scheduler + khoá; mỗi ngày
1 phiên) + cách nghiệm thu (dựng thử 1 hệ thống mẫu không hành động ra ngoài; grep không còn chữ FB/BĐS; FB không đổi file) → spec → người dùng duyệt → writing-plans.
