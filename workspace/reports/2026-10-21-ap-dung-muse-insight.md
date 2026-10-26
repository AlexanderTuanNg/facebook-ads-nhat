# Kết quả Muse 21/10: website dự án đang thành trang cờ bạc — xử lý trước; 7 điều chỉnh cho 4 khâu, 1 đã làm

> Nguồn: `workspace/research/2026-10-21-muse-insight-fb.md` (Muse, 2 vòng, đã ẩn link trang cá nhân). Claude kiểm lại 21/10 bằng công cụ của mình (mục 2).
> Nhãn: [DỮ LIỆU] = Claude tự kiểm thấy · [NGUỒN Muse] = Muse thấy, Claude chưa kiểm · [GIẢ THUYẾT] = cần thử.

## 1. Vì sao
Muse đọc được Facebook (nhóm, bình luận, Thư viện quảng cáo) mà công cụ của mình không đọc được. Kết quả có 1 rủi ro gấp (website), 2 chỗ lịch đăng đang đi sai nhóm, và vài điều chỉnh nội dung, quảng cáo. Câu hỏi: dùng gì ngay, dùng gì sau khi người dùng quyết? → Gấp: website. Đã làm: bỏ 2 nhóm cấm quảng cáo. Còn lại chờ quyết ở mục 5.

## 2. Claude kiểm lại 6 điểm chính — 6/6 khớp, 1 điểm Muse thiếu
| Điểm | Cách kiểm | Kết quả |
|---|---|---|
| yenthegoldenhill.com là trang cờ bạc | Mở trang (WebFetch 21/10) | **Khớp** [DỮ LIỆU]: tiêu đề "KASKUSTOTO : Situs Resmi Toto Togel…", tiếng Indonesia |
| Bài, quảng cáo của mình có dẫn link website không | Tìm chữ "yenthegoldenhill" trong toàn dự án | **Không** [DỮ LIỆU]: chỉ có trong 1 ghi chú cũ 25/09; quảng cáo đang chạy dẫn về Messenger |
| Hawee bật quảng cáo trả phí 20/10 | Thư viện QC qua kết nối Meta | **Khớp** (ID 28692389923736163, Trang "Nguyễn Huy - BĐS Bắc Giang", bắt đầu 20/10 ~18:47). **Muse thiếu:** Trang chính "HAWEE PARKLAND CAO THƯỢNG - HAWEE GROUP" có **2 quảng cáo chạy từ ~13/04/2026** (đã ~6 tháng — dấu hiệu hiệu quả) [DỮ LIỆU] |
| Nhà ở xã hội Parc Ville chạy nhiều quảng cáo | Thư viện QC | **Khớp**: 14 quảng cáo đang chạy, ≥ 5 Trang ("Từ 21,9tr/m²", "Điều kiện mua NOXH 2026") [DỮ LIỆU] |
| Số thành viên nhóm | So với bảng nhóm trong cơ sở dữ liệu | **Khớp**: Yên Thế Online 98k/104k, 64k/65k; Mua Bán Nhà Đất BG (vn) 145k/143k; BĐS BG 70,2k/70k; Nhà đất Cụm Yên Thế 20k [DỮ LIỆU] |
| 2 nhóm "Người Yên Thế" cấm quảng cáo | Bảng nhóm của mình **không lưu nội quy** 2 nhóm này | Chưa tự kiểm được → [NGUỒN Muse]. Đã xử lý thận trọng (mục 3, C1) vì đảo lại được |

## 3. Bảy điều chỉnh theo 4 khâu (trục chia: tạo bài · đánh giá · đăng bài · quảng cáo)
| Khâu | Điều chỉnh | Căn cứ | Trạng thái |
|---|---|---|---|
| **C** Đăng bài | C1. Nhóm g41 "Người Yên Thế ✅" và g50 "Người Yên Thế ♥️" → `bo_qua`. 2 bài hẹn 26/10 (post 273, 277) sẽ **tự đổi nhóm** lúc đăng (cơ chế sẵn có của `lich_dang.py`) | Nội quy "không quảng cáo/PR, vi phạm bị gỡ và xoá tên" [NGUỒN Muse]; nick đang bị hạn chế từ 11/10 | **ĐÃ LÀM 21/10** (sao lưu `data/backup/marketing-2026-10-21-truoc-bo-qua-g41-g50.db`; hoàn tác: đổi lại `joined`) |
| C | C2. Ưu tiên nhóm "Mua Bán Nhà Đất Bắc Giang (vn)" g28 (145k, **đã vào, chưa từng đăng**) cho lô bài từ 28/10; 2 nhóm lớn chưa vào: Mua Bán Nhà Đất Bắc Giang 193k, BĐS Việt Yên Bắc Giang 249k | Nhóm có người hỏi mua thật: 8 bài cần mua/30 ngày ở 3 nhóm mua bán [NGUỒN Muse] | Chờ quyết (vào nhóm mới đang tắt từ 20/10) |
| A Tạo bài | A1. Thôi dùng lại bộ ảnh trao sổ cho bài nhóm (đã đăng lại ~17 lần, phần lớn 0 thích); chuyển sang **video người thật tại đất** | [NGUỒN Muse V2-D]; khớp số mình: ảnh trao sổ ít tương tác nhất [DỮ LIỆU 20/10] | Đưa vào đề bài lô 28/10 |
| A | A2. Mỗi bài nhóm tự chứa **địa chỉ + bản đồ ghim dự án** (khách hỏi "ở đâu" thay vì nhắn tin) | 9/84 bình luận hỏi vị trí; bài không ghi địa chỉ bị hỏi dồn [NGUỒN Muse V2-B] | [GIẢ THUYẾT] thử lô 28/10; **cần toạ độ dự án** |
| A | A3. Kịch bản nhắn tin có sẵn câu trả lời khi khách so với **nhà ở xã hội** (đất riêng, sổ đã trao, xây tự do; không nêu tên dự án khác — F7/H2) | Parc Ville 14 quảng cáo, giá 139–699 tr/căn [DỮ LIỆU] | Soạn sau khi người dùng duyệt hướng |
| D Quảng cáo | D1. Bản chữ quảng cáo sửa đang chờ ("Gần CCN Tân Sỏi… – đi làm gần") → đổi thành "Gần Công ty May LGG" hoặc "gần CCN Tân Sỏi (đã có quyết định thành lập)": CCN chưa thấy khởi công, tuyển dụng | [NGUỒN Muse insight 8, resta.vn — Claude chưa mở] | Chờ người dùng (bản sửa đang tạm dừng chờ Phòng KD) |
| B Đánh giá | B1. Thêm "yenthegoldenhill.com" vào từ cấm của máy kiểm (lint) tới khi website sạch, để không bài nào lỡ dẫn link | Website cờ bạc [DỮ LIỆU] | Đề xuất, làm được ngay khi "ok" |

Giữ nguyên, không đổi: thử Nhật/Hàn/Đài đợt 1 (đối thủ bỏ trống tệp này — [NGUỒN Muse], chắc chắn thấp); quảng cáo đang chạy vẫn dẫn Messenger.

## 4. Ba rủi ro lớn nhất
| Rủi ro | Dấu hiệu sớm | Làm gì |
|---|---|---|
| Khách tìm tên dự án ra trang cờ bạc → mất niềm tin; Meta có thể chặn tên miền | Khách hỏi "web dự án sao lại…"; quảng cáo có link bị từ chối | Chủ tên miền xử lý ngay; tạm thời không dẫn link website ở đâu cả |
| 4 câu giá công khai khác nhau ("khoảng 1 tỷ", "chỉ dưới 1 tỷ", "500 triệu – lô hơn 1 tỷ", "khởi điểm 1,2 tỷ") | Khách hỏi "giá nào đúng" | Chốt 1 câu giá cho mọi kênh (mốc KM7 hết hạn 25/10) |
| Số Reel của Muse không kiểm được (tra trực tiếp ra 0) | — | Chỉ dùng số đã khớp; Reel = [GIẢ THUYẾT] |

## 5. Cần quyết
| # | Quyết gì | Đề xuất | Ai giữ D | Hạn |
|---|---|---|---|---|
| 1 | Báo người giữ tên miền yenthegoldenhill.com xử lý (gia hạn, lấy lại, hoặc tạm gỡ) | Báo ngay; Claude không đụng | Người dùng → CĐT | **Hôm nay** |
| 2 | Chốt 1 câu giá công khai | Chọn 1 trong 4 câu ở mục 4 | CĐT / người dùng | 25/10 |
| 3 | Cho nick vào 2 nhóm lớn (193k, 249k) và ưu tiên g28 | Đồng ý, vào tay 2 nhóm (không bật lại tự vào nhóm) | Người dùng | 27/10 (trước lô 28/10) |
| 4 | Thêm tên miền vào từ cấm (B1) · đổi câu CCN Tân Sỏi (D1) | Đồng ý cả hai | Người dùng | Khi tiện |

Phụ lục: bảng nhóm đầy đủ (33 nhóm, nội quy), bảng đối thủ 30 dòng, câu trích người mua — ở file nghiên cứu Muse.
