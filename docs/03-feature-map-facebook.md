# Feature map: giao diện Facebook cho agent thao tác trình duyệt

> Theo Lauren Tan: khi agent chạy được ứng dụng nhưng không tìm ra màn hình/nút cần thiết, cần một **bản đồ tính năng** chỉ đường. File này là bản đồ; selector cụ thể nằm ở `tools/fb_selectors.json`.
> Khi FB đổi giao diện: chụp màn hình (`data/error_post*.png`), cập nhật cả 2 file, ghi ngày ở cột "Xác minh lần cuối".

| Tính năng | Điểm vào (URL) | Đường đi | Key selector | Dấu hiệu thành công | Xác minh lần cuối |
|---|---|---|---|---|---|
| Soạn bài trong group | `https://www.facebook.com/groups/<id>` | Nút "Bạn viết gì đi..." → hộp thoại soạn bài | `composer_open` → `composer_dialog` → `composer_textbox` | Hộp thoại mở, con trỏ trong ô soạn | chưa xác minh |
| Đính ảnh | (trong hộp thoại soạn) | input file ảnh ẩn trong dialog | `photo_input` | Thumbnail ảnh hiện trong dialog | chưa xác minh |
| Đăng bài | (trong hộp thoại soạn) | Nút "Đăng" | `post_button` | Dialog đóng; có thông báo "đang chờ phê duyệt" nếu group duyệt bài | chưa xác minh |
| Bài đã đăng của tôi | `<group>/my_posted_content` | Mở trực tiếp URL | tìm 40 ký tự đầu bài | Thấy bài → `published` | chưa xác minh |
| Bài chờ duyệt | `<group>/my_pending_content` | Mở trực tiếp URL | tìm 40 ký tự đầu bài | Thấy bài → `pending` | chưa xác minh |
| Phát hiện checkpoint | bất kỳ | URL chứa `checkpoint` hoặc text cảnh báo khoá | `checkpoint_markers` | Không có nghĩa là an toàn | chưa xác minh |
| Phát hiện hết phiên | bất kỳ | Có form đăng nhập | `login_markers` | Không có nghĩa là còn phiên | chưa xác minh |

## Nguyên tắc cho agent
- Không đoán click. Không tìm thấy selector thì dừng, chụp màn hình, báo `SELECTOR_NOT_FOUND <key>`.
- Không bao giờ bấm vào nút liên quan đến mật khẩu, bảo mật, thanh toán, cài đặt tài khoản.
- Fanpage **không** dùng bản đồ này: Page luôn đi qua Graph API (`tools/fb_page.py`).
