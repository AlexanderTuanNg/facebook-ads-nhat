# Hướng dẫn cài đặt (làm 1 lần)

## 1. Cài thư viện
```
pip install -r requirements.txt
python -m playwright install chromium
python tools/db.py init
```

## 2. Fanpage: lấy Page Access Token (Graph API)
Anh là admin của cả App và Page nên **không cần App Review**.

1. Vào https://developers.facebook.com → **My Apps** → **Create App** → chọn use case *"Manage everything on your Page"* (hoặc loại *Business*). Đặt tên, ví dụ "BDS Marketing Tool".
2. Trong App → **Tools → Graph API Explorer**:
   - Chọn App vừa tạo; *User or Page* → **Get User Access Token**.
   - Tick quyền: `pages_show_list`, `pages_read_engagement`, `pages_manage_posts`, `pages_manage_engagement`, `pages_read_user_content`, `pages_manage_metadata`.
   - Bấm **Generate Access Token** và cho phép với Page của anh.
3. Đổi sang **long-lived token**: vào **Tools → Access Token Debugger**, dán token, bấm **Extend Access Token** rồi copy token mới.
4. Lấy **Page token** (không hết hạn): trên Graph API Explorer, dán long-lived user token, gọi `GET me/accounts`. Trong kết quả, tìm Page của anh và copy `id` và `access_token`.
5. Tạo file `.env` (copy từ `.env.example`):
   ```
   FB_PAGE_ID=<id>
   FB_PAGE_TOKEN=<access_token của Page>
   ```
6. Kiểm tra: `python tools/fb_page.py me`

> Token Page sẽ mất hiệu lực nếu anh đổi mật khẩu Facebook hoặc thay quyền admin. Khi đó làm lại bước 2–5.

## 3. Group: lưu phiên đăng nhập cho từng nick
```
python tools/fb_group.py login --account nick_chinh
python tools/fb_group.py login --account nick_phu_1
```
Trình duyệt sẽ mở ra. Anh **tự đăng nhập** (kể cả 2FA), lướt vài giây rồi đóng cửa sổ. Phiên được lưu trong `.profiles/<nick>` (không chia sẻ thư mục này).

Kiểm tra: `python tools/fb_group.py check --account nick_phu_1`

## 4. Thêm group
Agent `researcher` đề xuất group (status `candidate`). Anh tự xin vào group bằng nick tương ứng, sau đó báo Lead (hoặc chạy lệnh):
```
python tools/db.py x "UPDATE groups SET status='joined', arm='B', account_id=3, joined_at=datetime('now','+7 hours'), warmup_until=datetime('now','+7 hours','+7 days') WHERE id=<id>"
```

## 5. Hiệu chỉnh selector lần đầu (quan trọng)
Giao diện Facebook khác nhau theo tài khoản/ngôn ngữ. Lần đầu nên chạy `prefill` (nhánh A) với 1 bài thử để xem script có tìm đúng ô soạn bài không. Nếu báo `SELECTOR_NOT_FOUND <key>`, xem ảnh chụp trong `data/` và sửa `tools/fb_selectors.json` (hoặc nhờ Claude sửa).
