# STATE · 20/10/2026: chỉ 4 khâu số (tạo · đánh giá · đăng · quảng cáo) để sau này thành app; QC 48 tr → ~40 lượt xem đất, sửa QC tạm dừng chờ Phòng KD

> Bộ nhớ làm việc, nạp vào MỌI phiên và tác nhân → **≤ 8 KB**. Trang đầu theo khuôn top-down (`.claude/rules/tu-duy-top-down.md`): thông điệp · trụ cột và tình trạng · cần quyết · 1 việc tiếp.
> Cập nhật trước khi kết thúc lượt có thay đổi file (Stop hook). "Việc vừa làm" ≤ 5 dòng, cũ hơn → `workspace/reports/log.md`. Quyết định → `workspace/quyet-dinh.md` (chỉ thêm, không xoá).
> STATE đầy đủ trước khi dựng khuôn: `workspace/reports/log.md` mục "Lưu trữ nguyên văn STATE.md lúc 20/10/2026 18:43" (bản trước 28/09: cũng trong log).

Cập nhật lần cuối: 2026-10-26 10:0x (video định vị Sentinel-2 sửa nhãn, đang dựng; giọng giữ edge-tts cho bản thử)

## 1. Thông điệp chính
Người dùng 20/10: **bỏ việc offline, chỉ làm 4 khâu số — A Tạo bài · B Đánh giá · C Đăng bài · D Quản lý quảng cáo** — để sau này đóng gói thành app nhân rộng.
Đích khâu QC (v2): **48 tr → ~400 cuộc nói chuyện → ~40 lượt xem đất → 5 HĐ**; cổng 27/10 (bật đợt 1), **09/11** (bảng chấm 14 ngày), 30/11. Kế hoạch: `workspace/ke-hoach/cap-1…cap-4`.
(Đích doanh nghiệp 60 HĐ trước 10/01/2027 giữ làm bối cảnh; việc bán offline không thuộc dự án này.)
**Lộ trình sản phẩm bản 2 (21/10):** bán "phòng marketing số làm thay" cho chủ đầu tư/sàn tỉnh; Yên Thế = Chặng 1, cổng **30/11**; tách lõi tháng 12; khách thứ 2 tháng 01/2027 — `ke-hoach/lo-trinh-san-pham-app.md`, `ke-hoach/khung-chuan-nhan-rong.md`.

## 2. Trụ cột và tình trạng (Đỏ = đang chặn mốc gần)
| Khâu · luồng | Tình trạng 20/10 | Đèn |
|---|---|---|
| A Tạo bài · A1 nhóm · A2 mẫu QC | 72 bài nhóm 22–27/10 đã viết, tự duyệt (post 224–295); mẫu QC 20/10 còn bản nháp (QC-VM2/VM3/VM4, A1, B1, F1, SK1); chưa có QC-NN1; chưa có bảng lô xanh để mẫu chỉ chào lô xanh | Vàng |
| B Đánh giá · B1 cổng · B2 đo | Cổng lint + compliance + judge chạy (lô 20/10: 6 CHẶN đã sửa, lint 72/72); evals 20/20, lint giá 31/31; chưa có bảng góc/mẫu thắng hằng tuần; lead theo mã bài chưa ai ghi | Vàng |
| C Đăng bài · C1 nhóm · C2 Fanpage | Lịch chỉ đăng bài, 8 bài/ngày tới 21/10, 12 từ 22/10 (người dùng giữ nguyên); 203 bài/79 nhóm → 1 SĐT; bài chờ duyệt 18% → 46%; Fanpage CĐT chưa nối | Đỏ |
| D Quảng cáo · D1 chiến dịch · D2 số | "Yên thế Video Mới." 300k/ngày, 27.066đ/cuộc, 38 cuộc từ 17/10; chưa biết bao nhiêu cho số/xem đất. **Sửa gộp TẠM DỪNG: người dùng "để tôi hỏi lại phòng kinh doanh đã" — KHÔNG sửa Meta tới khi người dùng báo lại.** Bộ sửa chờ "ok" (nhóm QC 120252256456550048): xoá Hoa Kỳ · bỏ tích "Tiếp cận thêm nhiều người…" · "Người sống ở đây" · thay chữ = mục D · bấm Đăng 1 lần. 2 lịch báo cáo đã tạo (lần đầu 21/10 ~17:35); sổ nguồn khách chưa có dòng thật | Vàng |

## 3. Cần quyết (ai giữ D · hạn)
0. **GẤP — website yenthegoldenhill.com đang là trang cờ bạc** (Claude mở kiểm 21/10; tên miền đăng ký mới 10/08/2026 qua NameCheap → nhiều khả năng đã mất vào tay người khác): báo người giữ tên miền xử lý; không dẫn link website ở đâu cả — **người dùng → CĐT** — hôm nay. Kèm 3 quyết định nhỏ từ kết quả Muse (giá công khai 1 câu · vào 2 nhóm lớn · từ cấm tên miền, câu CCN Tân Sỏi): `workspace/reports/2026-10-21-danh-gia-muse-chi-tiet.md` (trang đầu) (6 việc: đợt 1 gộp 1 nhóm thử mẫu · viết lại mẫu · thử 2 tin chào · sửa skill/kế hoạch · giữ hay trả 2 nhóm · website).
1. Tiền QC: trừ 2,73 tr đã chi vào dự phòng hay vào Nền (kế hoạch QC 14 ngày §7; người dùng 20/10: chưa) — **người dùng** — 23/10.
2. Tuyên bố chiến lược của hệ thống 34 chữ (`ke-hoach/cap-1-chien-luoc.md` §1) — **người dùng** — 23/10.
3. Bật đợt 1: thử vùng 2 × 120k + Nhật/Hàn/Đài 230k/ngày (chưa VAT), khi mẫu qua cổng — **người dùng** — 27/10.
4. Lịch đăng nhóm bằng nick **trái điều khoản Meta** (SP-2): đề xuất giữ mức đang chạy, không mở rộng, không đưa vào app; dừng nếu 09/11 vẫn ~0 SĐT — **người dùng** — 09/11.
5. Cách đóng gói, giá thử M1, chi phí đội mỗi tháng (`lo-trinh-san-pham-app.md` §7) — **người dùng** — 30/11.

## 4. ▶️ Một việc tiếp
→ Tối nay kiểm kết quả 9 bài video (log `data/lich_dang_2026-10-26.log`); 27/10: đo lượt xem/bình luận bài video so với bài ảnh, lead theo mã (YT88, TY51, BH27, YT89, TY65, YT90, BH28, SC01, SC02); trần đã trả 12 (kiểm `config/settings.json`); viết lô bài tuần (thứ Ba) dùng video; SC: thêm bài cho thuê vào nhóm BĐS BG đã vào (g28, g29, g30, g31, g32, g33) + nhóm mới hết làm quen từ 29/10. Còn mở: Manulife còn ở toà không.

---
## Vận hành đang chạy (không đổi khi chưa có lệnh)
- **Lịch tự đăng** Windows task `YenThe-LichDangBai` (`tools/lich_dang.py --hom-nay`, 06:30 + khi đăng nhập Windows; máy phải bật). Đăng bài + 14:10 vào 4 nhóm + **22:20 quét khách CHỈ ĐỌC** (`quet_khach.py`, từ 25/10; tắt: VIEC_DEM = []). Không kết bạn, không nhắn tin.
- **Lịch tìm lead** Claude `yen-the-tim-lead-hang-ngay` 08:14 hằng ngày (tạo 25/10): chấm gói thử T0–T4, tự chỉnh, báo cáo `workspace/reports/lead-ngay/`; danh sách khách (có tên, link) ở `data/khach/`. Nhật ký `data/lich_dang_<ngày>.log`. **Dừng khẩn: tạo `data/stop_batch`.**
- **Lịch viết lô bài** Claude `yen-the-viet-lo-bai-tuan`: thứ Ba ~19:05 (20/10 tối đã duyệt đủ tới 27/10, post 224–295; lần tới viết từ 28/10).
- **Lịch báo cáo QC** (tạo 20/10, chế độ bỏ qua hỏi quyền, Meta chỉ đọc theo prompt): `yen-the-bao-cao-qc-1730` ~17:35 hằng ngày → `workspace/reports/qc-ngay/`; `yen-the-bao-cao-qc-thu-hai` ~08:04 thứ Hai → `workspace/reports/qc-tuan/`.
- **nick_chinh** bị hạn chế gửi tin từ 11/10 (acc clone, không xác nhận được) → CTA mọi bài = gọi/Zalo 0965 539 599; nick chỉ đăng bài.
- **Hạn mức tuần ≥ 70%** → chỉ dừng việc của Claude, lịch Python vẫn chạy (CLAUDE.md). 20/10 19:00: 13%.
- **Kết nối `meta-ads`**: 22/10 người dùng đồng ý thêm quyền `ads_management` vào `~/.claude.json` (sao lưu `.claude.json.bak-2026-10-22-truoc-ads_management`); chờ đăng nhập lại nick Nam Lê. Luật giữ: chỉ dựng/đăng/sửa QC khi người dùng "ok" kèm số tiền, không đụng Video Mới. Trước đó chỉ đọc (app "AI ads marketing" 1640936344252432, nick Nam Lê; gỡ: `claude mcp remove meta-ads -s user`). TK act_882171458271697 thuộc "BM1. Via Edwin"; "Edwin Rinaldi" là nick của Nam Lê (người dùng 20/10) → không chuyển tài khoản/danh mục.
- **Sổ nguồn khách** Google Sheet ID `13Uf2GRNO15NM9jTpCxQGAtSUyh7SO5bGsPWbY0dKMeY` (riêng tư; 3 file nháp "[XOÁ ĐƯỢC]" trong Drive chưa xoá).
- Có khách nhắn/gọi: người dùng dán tin → soạn trả lời theo `workspace/kich-ban-nhan-tin-lead.md` §B, người dùng duyệt từng tin.
- Bẫy máy: cài phần mềm/pip ghi AppData phải chạy qua `explorer.exe <file.cmd>` (hộp cát MSIX).

## Việc vừa làm (≤ 5 dòng)
- 2026-10-26 14:31 **Bỏ nhóm bị từ chối suốt** (người dùng): 20 nhóm ≥2 bài mà 0 bài hiện → bo_qua; rời hẳn 4 nhóm 'Tin Hữu Lũng' (291/293/294/295, `tools/roi_nhom.py` mới); 8 bài đã hẹn ở nhóm bị bỏ → lịch tự đổi nhóm; SC 386 → g29. Bài video 311 (Tin Hữu Lũng) coi như mất (nhóm không duyệt). Quy tắc lưu memory `feedback-bo-nhom-tu-choi`.
- 2026-10-26 14:23 **Bài video GH đầu tiên 311 đăng được** (g291 Tin Hữu Lũng, chờ duyệt) → 351–354 cũng đổi sang video: hôm nay 7 bài GH video (311, 349 15:18, 350 16:02, 351 17:54, 352 19:10, 353 20:40, 354 21:28) + SC 385 (17:10 g27, dời từ 21:55 theo người dùng) / 386 (22:22 g29) video; nhãn AI dòng cuối; `fb_group.py` gắn .mp4 (chờ tải 20 giây, nút Đăng tới 4 phút). Vào nhóm 14:10: 750, 764, 765 đã vào; 16:12 vào thêm (tổng 8). Trần 14 riêng hôm nay, 23:59 trả 12.
- 2026-10-26 13:08–13:20 **Tìm nhóm đợt 2** (14 từ khoá cho thuê nhà/văn phòng/sang nhượng/M&A, chỉ đọc): 483 nhóm → nhập 18 ứng viên id 763–780: 8 nhóm BĐS lớn BG–BN (115–235K) q=62, 5 nhóm sang nhượng/cho thuê mặt bằng q=61, 5 nhóm M&A dự án/toà nhà (topic 'ma') q=60,5. Hàng chờ: 31 nhóm cho thuê/doanh nghiệp/M&A trước nhóm cộng đồng GH. Hôm nay vào 8 nhóm (14:10 + 16:12). Sao lưu DB `data/backup/marketing-2026-10-26-truoc-nhom-dot2.db`; kết quả thô `data/tim_nhom_20261026_1308.jsonl`.
- 2026-10-26 ~12:55 **NGƯỜI DÙNG DUYỆT 3 VIDEO** ('ok r, đưa tôi cả 3 video đây') → đã gửi bản giao `assets/video-da-duyet/2026-10-26/` (1-golden-hill-dinh-vi 23,2 giây · 2-sun-city-dinh-vi 34,1 giây · 3-sun-city-ben-trong-van-phong 28,9 giây). Nhãn giọng AI: không in trên hình; ghi ở DÒNG CUỐI chú thích '* Video sử dụng giọng đọc AI' (người dùng 26/10). Hạn mức tuần 67% lúc 12:50.
- 2026-10-26 ~12:35 **ĐÃ GỬI 2 video Sun City, chờ duyệt**: (1) định vị bản 4 — 34,1 giây, −14,0 LUFS, bỏ giá, dải đỉnh 'CHO THUÊ VĂN PHÒNG 240 – 1.200 m² · Mặt tiền Hùng Vương · Gọi/Zalo 0965.539.599', ảnh toà + 'Cùng toà nhà: VNVC · SHB · Manulife' + 'Biển hiệu mặt tiền · Hầm để xe · Thang máy', thẻ cuối 240–1.200 m² + 'Phù hợp văn phòng đại diện, công ty đa quốc gia'; (2) 'bên trong văn phòng' theo mẫu Hanoi Office (người dùng: ảnh toà trước, lời đọc mở đầu giới thiệu cho thuê toà nhà mặt đường → bản 3 gửi ~12:50) — 28,9 giây, −13,9 LUFS, `tools/video_ben_trong.py`, đoạn quay người dùng + 4 ảnh phủ kín khung (bỏ ảnh 03 có standee Manulife), ô chữ trắng theo câu đọc. Cả hai giải mã trọn OK.

## Đang chờ người dùng từ trước (chi tiết ở log)
11 việc nhỏ còn chờ (ảnh tối, PIN Messenger, nhóm 39, mốc giá KM7 trước 26/10, tiêu đề "CHỈ DƯỚI 1 TỶ", cột điện, ưu đãi 48 giờ, chế độ strict…): nguyên văn ở `workspace/reports/log.md` mục "Chuyển từ STATE 2026-10-21 (Đang chờ…)".
