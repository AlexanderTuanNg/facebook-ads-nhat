# assets/ — tư liệu dự án (KHÔNG đưa lên Git)

Thư mục này chứa ảnh, flycam, video đã dựng (~1,2 GB), trong đó có ảnh khách hàng thật (lễ bàn giao sổ) → bị `.gitignore` chặn.
Repo chỉ giữ các file cấu hình (`cau-hinh*.json`, `kich-ban-loi-doc.txt`) và README để dựng lại.

| Thư mục | Nội dung | Cách có lại |
|---|---|---|
| `dong-lac/` | Ảnh/flycam dự án Yên Thế Golden Hill, kho ảnh xoay vòng (`kho-anh/danh_muc.json`), ảnh bài đã dựng | Chủ đầu tư cung cấp; xem `dong-lac/README.md` |
| `dong-lac/video-dinh-vi/` | Cấu hình video định vị + lời đọc; `sentinel.jpg`, `bay-ve-tinh.mp4` tự sinh | `python tools/sentinel_cat.py …` → `python tools/bay_ve_tinh.py …` → `python tools/video_dinh_vi.py …` |
| `cho-thue-sun-city/` | Ảnh văn phòng cho thuê + 2 cấu hình video | Chủ nhà cung cấp |
| `video-da-duyet/<ngày>/` | Bản video người dùng đã duyệt để đăng | Dựng lại từ cấu hình |
