---
name: quang-cao-bds
description: Bộ chuyên môn quảng cáo trả tiền Meta (Facebook/Instagram) cho đất nền tỉnh Yên Thế Golden Hill, khớp kế hoạch bán hàng v2 — vai trò AI quản lý quảng cáo, chuẩn dựng chiến dịch Tin nhắn/Gọi ngân sách nhỏ, checklist trước khi bật, chuẩn câu mở từ mẫu chạy lâu trong Thư viện QC, bảng ngưỡng có nguồn, cây chẩn đoán, luật TẮT/GIỮ/TĂNG, nhịp sự kiện, sổ nguồn khách, soi đối thủ. Dùng khi dựng, kiểm, viết, chấm hoặc đọc số quảng cáo trả tiền; khi lên đợt QC cho sự kiện; khi tổng kết tuần/tháng quảng cáo.
---

# Bộ chuyên môn quảng cáo BĐS (Yên Thế Golden Hill)

**Nguồn sự thật** (mâu thuẫn → thứ tự này thắng): `workspace/compliance-checklist.md` §H (sàn pháp lý) → `workspace/reports/2026-10-15-ke-hoach-ban-hang-90-ngay-v2.md` §4.1, §6 (kế hoạch bán, người dùng chốt) → file này. Nghiên cứu nền: `workspace/research/2026-10-15-chuyen-mon-qc-bds-nguon.md` (Meta chính thức, ngưỡng, cây chẩn đoán), `2026-10-15-thu-vien-qc-dat-nen-chay-lau.md` (30 mẫu đất nền chạy ≥ 60 ngày), `2026-10-15-thu-vien-quang-cao-cdt-lon.md` (Vinhomes, Ion City), `2026-10-14-best-practice-quang-cao-bds.md` (luật VN, gọi lại 5 phút), `ads-moi-gioi.md` (9 video cũ, 2.003 lead). Nhãn căn cứ bắt buộc: **[DỮ LIỆU] / [NGUỒN] / [GIẢ THUYẾT]**.

## 0. Vai trò và ranh giới
Quảng cáo là **1 kênh** của kế hoạch bán: gánh **5/60 HĐ**, 48 triệu/90 ngày. Mục tiêu bán đi trước, kỹ thuật Meta đi sau.

| Vai | Làm gì |
|---|---|
| **Chuyên gia QC** (AI, theo bộ này) | Dựng chiến dịch (để **tạm dừng** tới khi có "ok"), viết mẫu (copywriter → compliance → judge), đọc số 17:30 hằng ngày + thứ Hai, chẩn đoán, đề xuất |
| **GĐ Marketing BĐS** (vai duyệt) | Kiểm đợt QC khớp kế hoạch bán: đúng nhóm khách, đúng sự kiện, chỉ quảng cáo **lô xanh** |
| **Người kiểm độc lập** (tác nhân khác người dựng) | Phản biện thiết lập theo checklist §2b **trước khi bật**; người dựng không tự duyệt |
| **Người dùng** | Đăng nhập Meta lần đầu, thêm thẻ (Claude **không** nhập mật khẩu/thẻ), nói **"ok" cho mỗi lần tiêu tiền mới**: bật chiến dịch/mẫu mới, tăng ngân sách |

- Trước khi nối Meta Ads chính chủ: Claude chỉ soạn, đọc file xuất, đề xuất; người dùng tự bấm. Sau khi nối: **tắt/giảm theo luật §6** được làm ngay rồi báo (giảm tiêu, đảo ngược được); **bật/tăng** luôn chờ "ok".
- Sàn cứng (§H): không hứa lời/tăng giá/"dòng tiền", không so sánh đối thủ, không khan hiếm giả, không mượn mặt khách chưa đồng ý, có dòng (*) dưới mọi con số, chạy từ Fanpage CĐT. Ngoài sàn này, **ưu tiên hiệu quả bán** (người dùng 15/10).
- **Cách trình bày (từ 20/10, `.claude/rules/tu-duy-top-down.md`):** mọi báo cáo, đề xuất QC mở bằng kết luận có con số; đề xuất tiêu tiền mở bằng **[QUYẾT]** + số tiền + luật §6a + ai giữ D (người dùng) + hạn. Báo cáo 17:30 = kết luận 1 câu + 3 con số + cần quyết; thứ Hai và tổng kết tháng = khuôn 6 ô (mẫu: `workspace/plans/2026-10-20-bao-cao-qc-17h30.md` mục 2, 2b). Mã truy vết: luồng **B1** của `workspace/ke-hoach/cap-3-thang-11.md`, KR3 của `cap-2-90-ngay.md`.

## 1. Bảy nguyên tắc vàng
1. **Chấm bằng lượt xem đất, không bằng lead.** 2.003 lead cũ, 0 chất lượng [DỮ LIỆU]. Mốc: chi phí/lượt xem đất ≤ 1,5 tr, chi phí/cọc ≤ 8 tr [DỮ LIỆU v2]. **Hai mốc chỉ khớp khi chi phí/lượt xem ≤ 1,2 tr** (8 tr × tỉ lệ xem→cọc QC 15% [GIẢ THUYẾT v2]) → coi 1,2 tr là mức cần đạt, 1,5 tr là trần.
2. **Gom để máy học được.** Meta cần ~50 kết quả/tuần/nhóm quảng cáo [NGUỒN Meta 112167992830700]; nền 1,3 tr/tuần → mỗi kết quả phải ≤ ~26k. Nên: tối ưu theo **cuộc trò chuyện** (rẻ nhất), **1 chiến dịch nền · 1 nhóm · 3–5 mẫu khác hẳn nhau**; "Learning limited" là bình thường với ngân sách này — đọc số kinh doanh, đừng sửa liên tục.
3. **Tin nhắn là chính, kéo về Zalo/SĐT ngay.** 22/30 mẫu đất nền chạy lâu dùng "Gửi tin nhắn", 0/30 dùng "Gọi ngay" [DỮ LIỆU Thư viện]. Người 45–60 nhắn hằng ngày bằng Zalo 75%, Messenger 10% [NGUỒN Decision Lab 2024] → câu chào xin SĐT/Zalo trong 1–2 câu.
4. **Chỉ chạy giờ có người trực (7:00–21:00), trả lời ≤ 5 phút.** QC gọi đặt lịch giờ trực: +25,4% cuộc gọi [NGUỒN Meta 604687010451937]; gọi lại nhanh [NGUỒN HBR/MIT, file 14/10].
5. **Bằng chứng thật làm câu mở:** sổ ĐÃ trao 09/10 (đối thủ chỉ có "lộ trình ra sổ"), khách thật có đồng ý, neo địa phương (đền Hoàng Hoa Thám: tương tác gấp đôi [DỮ LIỆU G1]).
6. **Không sửa khi đang học.** Chạy đủ 7 ngày, không đụng 48–72 giờ đầu; thêm mẫu/đổi vùng/đổi nội dung đều làm học lại [NGUỒN Meta 316478108955072] → gom thay đổi thành **đợt 14 ngày**, trừ khi luật TẮT.
7. **Số chưa có nguồn thì tự đo.** Giá/tin nhắn, giá/cuộc gọi, % nghe máy, giá/lượt xem đất của đất nền tỉnh VN **không có nguồn công khai** [NGUỒN file nghiên cứu §6] → tuần 1–2 là đo nền, sau đó mới cố định ngưỡng (§12).

## 2. Chuẩn dựng chiến dịch
**Tiền thật:** Meta thu thêm VAT 10% (từ 01/07/2025) [NGUỒN Meta 133076073434794] → nếu 48 tr là tiền trả ra thì tiền chạy ≈ 43,6 tr. Kiểm hoá đơn đầu tiên.

### 2a. Cấu hình
| Chiến dịch | Tiền [v2] | Mục tiêu · điểm đến | Nhắm | Đo bằng |
|---|---|---|---|---|
| **NỀN** (nhóm 1, 2, 5) | 16 tr, 21/10–10/01 | Engagement → **Message destinations** (Messenger), tối ưu cuộc trò chuyện. QC Gọi = **bản thử** cùng ngân sách nhỏ sau tuần 2 (tối ưu cuộc gọi 60 giây, chỉ trên điện thoại [NGUỒN Meta]) | Ghim dự án, **bán kính 30 km** trước, 50 km thử sau (Meta khuyên nới rộng → phải đo [NGUỒN]); **"Người sống ở vị trí này"**; **bỏ tick "Reach more people likely to respond"**; 25–65+, mọi giới; vị trí hiển thị Advantage+ | Giá/cuộc nói chuyện (sớm) → giá/lượt xem đất |
| **SỰ KIỆN** (QC-SK…) | 15 tr dồn trước sự kiện | Engagement → Messenger; **form chỉ để đăng ký phiếu ưu tiên** (§H9: ô đồng ý + chính sách bảo mật) | Như NỀN + người đã tương tác Page | Giá/gia đình đến dự ≤ 400k |
| **NHẬT/HÀN/ĐÀI** (QC-NN…) | 8 tr, 27/10–07/11 và 01–20/12 | Chiến dịch riêng, tiếng Việt, 22–40 tuổi. Nhật: Meta hạn chế tính năng nhắn tin "Châu Âu và Nhật" → tạo nháp xem còn tối ưu cuộc trò chuyện không; mất thì Traffic → link Zalo [NGUỒN Meta 212519562595207] | Quốc gia JP/KR/TW (nhóm "nhà ở" không bị bóp nhắm ở 3 nước này [NGUỒN Meta 2220749868045706]); **không** Mỹ/Canada/EU (§H10) | Chi phí/khách có số; ≥ 2,5 tr chưa ai để lại số → dừng |
| **CHẠY LẠI** | 4 tr từ 01/11 | Engagement → Messenger | Người xem ≥ 50% video, tương tác Page 30–90 ngày (gồm cả Hà Nội) | Giá/lượt xem đất |
| Dự phòng | 5 tr | Mở sau bảng chấm 09/11, dồn cho kênh thắng | | |

- **Tên QC trong Ads Manager:** `QC-<ý tưởng><bản> | <góc>` (vd `QC-A1 | so-da-trao`, `QC-SK2 | dem-hoi`, `QC-NN1 | con-o-xa`) — `doc_ads.py` dựa vào mã này.
- **Lịch:** 7:00–21:00 (ngân sách trọn đời, hoặc ngân sách ngày + "Set a schedule"). Nhật/Hàn nhanh hơn 2 giờ, Đài 1 giờ.
- **Tin chào (Automated chat), giọng sales:** "Dạ em chào anh/chị, em bên chủ đầu tư Yên Thế Golden Hill ạ." → nút bấm sẵn: *Gửi em ảnh sổ + vị trí* · *Em đang ở gần Yên Thế/Tân Yên* · *Mua cho con/bố mẹ mua cho con* → câu 2: "Anh/chị cho em xin SĐT hoặc Zalo, em gửi ảnh sổ thật và tính thử cho nhà mình ạ (*)". Ngoài giờ: hẹn gọi lại 7:00 sáng. QC Gọi: bật "nhận yêu cầu gọi lại qua Messenger".
- **Cuộc gọi phải tự ghi sổ:** ở VN Meta không báo số người gọi/nghe-nhỡ (chuyển tiếp cuộc gọi chỉ có ở Mỹ) [NGUỒN Meta 695961640151007]. Dùng 1 số riêng cho QC để tách nguồn [GIẢ THUYẾT].

### 2b. Checklist trước khi bật (người kiểm độc lập ký từng dòng, thiếu 1 dòng = chưa bật)
1. Điều kiện chạy §H đủ (website công khai, dòng PL, Fanpage + tài khoản QC doanh nghiệp); Quyết định chính sách có số nếu mẫu nhắc "trả trước 500 triệu".
2. Chỉ quảng cáo lô **xanh** trên bảng hàng ngày hôm đó.
3. Mẫu đã qua compliance `[QC] OK` + judge Phần QC + người dùng duyệt nội dung.
4. Mục tiêu/điểm đến/tối ưu đúng bảng 2a; 1 nhóm, 3–5 mẫu **khác góc** (không 5 bản 1 ảnh).
5. Vị trí: bán kính đúng, "người sống ở đây", đã **bỏ tick** "Reach more…"; không chọn theo tên tỉnh.
6. Lịch 7–21h; có tên người trực máy từng ca; Messenger/điện thoại thử nhắn/gọi được.
7. Tin chào xin SĐT/Zalo ≤ 2 câu; trả lời nhanh đã bật.
8. Tên QC đúng mã; sổ nguồn khách có sẵn mã đó (§4).
9. Ngân sách khớp bảng 2a; tổng chi đợt + VAT ≤ phần tiền người dùng đã "ok".
10. Ghi vào `workspace/quyet-dinh.md`: ai "ok", ngày, số tiền.

## 3. Form (chỉ cho sự kiện)
Form chỉ dùng **đăng ký phiếu ưu tiên / tham dự sự kiện**: 2–3 câu (khu đang ở, số người đi, giờ muốn đến), ô đồng ý bắt buộc + link chính sách bảo mật (§H9), không hỏi CCCD/thu nhập. Bỏ form Higher intent + OTP và tối ưu "khách chất lượng" (CAPI): ngân sách không bao giờ đủ ~200 lead/tháng [v2 §4.1]. Bản mẫu cũ ở `workspace/plans/qc-form-va-kich-ban.md` chỉ giữ phần kịch bản quay + gọi lại.

## 4. Sổ nguồn khách (Google Sheet) và bậc phễu
Mỗi khách 1 dòng: ngày · kênh · **ma_qc** (bắt buộc nếu từ QC; hỏi "anh/chị thấy tin ở đâu ạ", Messenger hiện QC khách bấm) · nhóm khách 1–5 + cờ N5 · **trang_thai = BẬC CAO NHẤT đã đạt** (không hạ bậc khi khách bỏ; ghi bỏ ở cột ghi chú) · nghe_may · goi_lai_phut · ai cầm 500 tr / ai trả dần / ai quyết.

| Bậc | trang_thai | Định nghĩa [v2 §6] |
|---|---|---|
| 1 | lead | Có tên + SĐT/Zalo + nguồn |
| 2 | đủ chất lượng | Nghe máy, đúng 1 trong 5 nhóm, trả lời được "phần đầu lo từ đâu", định mua trong 3 tháng |
| 3 | xem đất | Đã đến lô/đến dự sự kiện, có check-in, **người cầm tiền có mặt hoặc gọi video** |
| 4 | giữ chỗ | Phiếu ưu tiên hoặc đã giữ lô |
| 5 | cọc | 50 tr vào tài khoản BIDV + bảng "ai trả phần nào" |
| 6 | ký | HĐ công chứng + đóng đủ phần trả trước |
| 0 | loại | Sai nhu cầu, số rác, 3 lần không nghe (khi chưa tới bậc 2) |

Đọc số: `python tools/doc_ads.py --ads <xuất Ads Manager cấp Quảng cáo> --leads <CSV sổ nguồn khách>` (`--luu` khi là số thật của kỳ). Công cụ tự bỏ dòng không có mã QC, không in tên/SĐT.

## 5. Chỉ số và bảng ngưỡng
Phễu mỗi tuần: **Chi tiêu → Cuộc nói chuyện (tin nhắn + gọi + form) → Có SĐT/Zalo → Đủ chất lượng → Xem đất → Cọc → Ký.**

| Chỉ số | Tốt | Cần xem lại | Kém / hành động | Căn cứ |
|---|---|---|---|---|
| Giá/lượt xem đất | ≤ 0,8 tr | 0,8–1,5 tr (cần ≤ 1,2 tr) | > 1,5 tr 2 tuần liền → giảm tiền, đổi video | [DỮ LIỆU v2]; 1,2 tr là phép tính |
| Giá/cọc | ≤ 8 tr | | > 8 tr | [DỮ LIỆU v2] |
| Giá/cuộc nói chuyện (tín hiệu sớm) | ≤ 80k | 80–150k | > 150k: xem câu mở, tin chào; tiêu ≥ 1 tr chưa ai nhắn → sai câu mở/nút | [GIẢ THUYẾT] tính ngược: 1,5 tr × 10% (nói chuyện → có số 40% → đủ CL 50% → xem 50%). Mọi ngành 10–15k/cuộc [NGUỒN THẤP]. **Chỉnh bằng số thật cuối tuần 2** |
| % cuộc nói chuyện để lại SĐT/Zalo | ≥ 40% | 20–40% | < 20%: câu chào chưa xin số, hoặc QC hút người tò mò → nêu tầm giá/vùng | [GIẢ THUYẾT], tự đo |
| % nghe máy | ≥ 60% | | < 50%: gọi lại chậm hoặc số rác | [GIẢ THUYẾT]; ví dụ CRM ~15% [NGUỒN THẤP] |
| Gọi lại (trung vị) | ≤ 5 phút | ≤ 15 phút | > 15 phút | [NGUỒN] + v2 §6 |
| CTR liên kết | > 2% | 1–1,5% | < 1% sau ≥ 500 lượt hiển thị | [NGUỒN THẤP] Chợ Đất, Zafago; chỉ để chẩn đoán |
| Giữ chân 3 giây (xem 3s ÷ hiển thị) | so giữa các mẫu | | thấp nhất nhóm → đổi 3 giây đầu | Không có nguồn số; video cũ xem TB 4–9 giây [DỮ LIỆU G7] |
| Tần suất 7 ngày (nhóm lạnh) | < 2 | 2–2,5 | > 2,5: làm sẵn mẫu thay | [NGUỒN THẤP] (Meta: không có chuẩn chung) |
| Nhãn Meta | — | **Creative limited** (giá > mẫu cũ, < 2×): chuẩn bị mẫu mới | **Creative fatigue** (≥ 2×): thay ngay | [NGUỒN Meta 1346816142327858] |
| CPM bán kính 30–50 km | tự đo | | | Không có nguồn VN; quốc tế BĐS ~$5 ≈ 130k [NGUỒN THẤP] |

**Trần số mẫu chấm được bằng lượt xem đất:** nền 1,3 tr/tuần × 2 tuần ÷ 3 tr (mốc đổi video) ≈ **1 mẫu/2 tuần** → chạy 3–5 mẫu chung 1 nhóm để Meta tự dồn tiền, **chấm mẫu bằng tín hiệu sớm** (giá/cuộc nói chuyện, % để lại số, giữ chân 3s), **chấm ý tưởng và chiến dịch bằng giá/lượt xem đất**. Tổng chi < 10 tr → mọi kết luận là [GIẢ THUYẾT].

## 6. Luật ra quyết định, cây chẩn đoán, lịch kiểm tra
### 6a. Luật TẮT/GIỮ/TĂNG (`doc_ads.py` làm sẵn; dừng ở luật đầu tiên khớp)
Chấm **ý tưởng** trước, **mẫu** sau: 3 mẫu cùng ý tưởng đều thua = ý tưởng sai; 1 mẫu thua = cách làm sai.
- Ngày 7: mẫu tiêu < 50% phần chia đều → **TẮT** (Meta không phân phối), thay mẫu khác góc.
- **NỀN:** tiêu < 3 tr → **CHỜ** (cảnh báo nếu ≥ 1 tr chưa ai nhắn/gọi) · 3–6 tr mà 0 lượt xem → **ĐỔI VIDEO** khác góc/câu mở · ≥ 6 tr vẫn 0 → **TẮT + bỏ ý tưởng**, dồn tiền sang xe đón khách · giá/lượt xem > 1,5 tr: lần đầu **THEO DÕI**, 2 tuần liền **GIẢM TIỀN + ĐỔI VIDEO** · 0,8–1,5 tr **GIỮ** · ≤ 0,8 tr 2 tuần liền + tần suất < 3 → **xin "ok" TĂNG 20%** từ dự phòng [v2]. Dưới 3 lượt xem → gắn [GIẢ THUYẾT], không tăng.
- **SỰ KIỆN:** > 400k/gia đình đến dự → **GIẢM TIỀN**. **NHẬT/HÀN/ĐÀI:** ≥ 2,5 tr chưa ai để lại số → **DỪNG**.
- **Tăng tiền:** Meta không công bố ngưỡng % an toàn (ví dụ của Meta: 100→101 USD không sao, 100→1.000 có thể học lại) → +20%/lần, cách ≥ 4 ngày là quy ước thận trọng [GIẢ THUYẾT]. Đạt cả 2 mốc v2 trong 2 tuần liền → đề nghị CĐT mở thêm quỹ.

### 6b. Cây chẩn đoán (đi từ trên xuống, dừng ở bậc đầu tiên hỏng)
| Triệu chứng | Nguyên nhân hay gặp | Sửa |
|---|---|---|
| Không tiêu hết tiền / ít hiển thị | Bị từ chối; bán kính nông thôn quá hẹp; lịch giờ quá hẹp; trần giá | Xem cột Delivery; bỏ trần giá; nới 30 → 40 km [NGUỒN Meta 284656872650053] |
| "Learning limited" | Chia nhiều nhóm; tối ưu sự kiện hiếm (cuộc gọi 60s) | Gom 1 nhóm; tối ưu cuộc trò chuyện; **không** sửa nếu số kinh doanh vẫn ổn [NGUỒN Meta] |
| CPM cao, giá/cuộc nói chuyện cao | Nhóm khách hẹp; mẫu kém (Meta phạt mẫu ít liên quan); mệt mẫu | Cải thiện mẫu trước; thử 50 km ở đợt sau; mở thêm vị trí hiển thị [NGUỒN Meta 2727273724224874] |
| CTR thấp / giữ chân 3s thấp | 3 giây đầu không nói ý chính; ảnh dựng; chữ nhỏ (khách 45+) | Đổi câu mở theo §8 (giá/vốn, "đã trao sổ", câu hỏi vốn), người thật tại lô, chữ to |
| CTR ổn nhưng ít người nhắn/gọi | Không nói rõ bấm để nhắn; tin chào khó; nút sai | Nút "Gửi tin nhắn"; câu chào 1 câu dễ + nút bấm sẵn [NGUỒN Meta 269324800441478] |
| Nhiều tin nhắn, ít người cho số | Khách quen Zalo; trả lời chậm; QC không nêu tầm giá/vùng nên hút người tò mò | Xin SĐT/Zalo ngay câu 2; nêu "chỉ dưới 1 tỷ"/vùng trong QC; ≤ 5 phút |
| Cuộc gọi nhỡ / gọi ngoài giờ | Chạy ngoài giờ trực | Lịch 7–21h; bật gọi lại qua Messenger; sổ cuộc gọi nhỡ |
| Có số nhưng không ai đi xem | Không hẹn giờ cụ thể; không có xe; người cầm tiền ở xa | Hẹn **ngày giờ cụ thể** (thứ Bảy/CN 8–11h, 14–17h), xe đón Bố Hạ/Nhã Nam/Cầu Gồ, gọi video 3 bên [v2 §6] |
| Có xem nhưng không cọc | Giá, chính sách, lô, sale — **không phải lỗi QC** | Chuyển TPKD; không chỉnh QC vì việc này |
| Tần suất ↑, CTR ↓, giá ↑ | Vùng nhỏ xem lặp | Thêm mẫu **khác hẳn**, giữ mẫu cũ nếu chưa tệ |
| Chi phí tăng ngay sau khi sửa | Học lại | Chờ 7 ngày; gom thay đổi thành đợt |
| Khách ngoài vùng | "Reach more…" đang bật; người "mới tới" vùng | Bỏ tick; chọn "người sống ở đây"; hỏi khu đang ở ngay câu chào |

### 6c. Lịch kiểm tra
- **Hằng ngày 17:30** (trong báo cáo 1 trang, khuôn BLUF: kết luận 1 câu + 3 con số + cần quyết, bảng xuống phụ lục): trạng thái Delivery (Learning/Limited/bị từ chối), tiền đã chi, số tin nhắn/cuộc gọi/nhỡ, số khách được gọi lại ≤ 5 phút. Còn "Learning" → không sửa.
- **3–4 ngày/lần:** tần suất, CTR, giá/cuộc nói chuyện, % để lại số **theo từng mẫu**, so với chính nó tuần trước.
- **Thứ Hai (giao ban 8:30):** chạy `doc_ads.py` 14 ngày gần nhất → bảng phễu theo ý tưởng + mẫu → đề xuất TẮT/GIỮ/TĂNG → ghi quyết định. Báo cáo theo khuôn 6 ô (thông điệp · SCQ · 4 trụ cột theo phễu · việc tuần tới · mốc và rủi ro · cần quyết có số tiền), bảng phễu xuống phụ lục. **Thay mẫu theo đợt 14 ngày** (thứ Hai cách tuần), trừ khi luật TẮT hoặc nhãn Creative fatigue.
- **Cuối tuần 2 (09/11):** thay các ngưỡng [GIẢ THUYẾT] ở §5 bằng số thật, ghi `workspace/quyet-dinh.md`.

## 7. Nhịp sự kiện (học Vinhomes, Ion City, Evergreen)
Mỗi sự kiện (phố đêm 23/10, **Đêm hội 07/11**, gói Đất + Nhà 09–15/11, Tri ân 21/11, Chốt năm 26/12): **úp mở 5–7 ngày trước → mời đăng ký phiếu/tham dự → tổng kết ngay trong ngày/hôm sau → "ưu đãi còn đến …"**. 2–4 bản mỗi nội dung. Tiền dồn theo bảng v2 §4.1 (phố đêm 2 tr · Đêm hội 6 tr · tổng kết 2 tr · Tri ân 2 tr · Chốt năm 3 tr). Thông điệp sự kiện phải MỞ ở §G (KM8–KM10) trước khi lên QC.

## 8. Viết mẫu QC
### 8a. Câu mở 3 giây — 5 khung (từ 30 mẫu đất nền chạy ≥ 60 ngày [DỮ LIỆU Thư viện 15/10])
| Khung | Mẫu thật đang chạy lâu | Bản cho mình (chỉ dùng thông điệp đã MỞ ở §G) |
|---|---|---|
| Giá/vốn ở dòng đầu (~15/30 mẫu) | "Chỉ 600 triệu sở hữu…", "Với số vốn 1,5 tỷ anh chị sẽ sở hữu…" | "CHỈ DƯỚI 1 TỶ LÀ CÓ CƠ HỘI SỞ HỮU đất có sổ ở trung tâm xã Yên Thế (*)" (KM7b) |
| Câu hỏi vốn (Heragon City, CĐT) | "Chỉ có 1,3 tỷ vốn tự có, mua được đất trung tâm Thanh Hoá?" | "Bố mẹ lo phần đầu, con làm KCN trả dần — mua được đất có sổ ở quê không?" (sau Quyết định chính sách) |
| Sổ đỏ làm bằng chứng (~22/30 nhắc sổ) | "ĐÃ CÓ SỔ ĐỎ TỪNG LÔ", "CHÍNH THỨC CÓ SỔ ĐỎ" | "Ngày 9/10 các gia đình đã cầm sổ đỏ tại Yên Thế Golden Hill" + ảnh trao sổ (có đồng ý) |
| Tiện ích đời sống nông thôn | "Gần chợ, trường học, trung tâm xã, bệnh viện, KCN" | Trung tâm xã, quảng trường buổi tối, đường lớn — chỉ điều đã MỞ |
| Neo địa phương / gia đình | "Bạn đang tìm mảnh đất… cùng gia đình?" | Đền Hoàng Hoa Thám dẫn về khu; "cho con mảnh đất khi lập gia đình" |

- **Định dạng:** video dọc 9:16, **40–90 giây** (phổ biến ở mẫu chạy lâu), người thật nói tại lô, **nhắc con số chính 2 lần**, phụ đề chữ to; video 9:16 có tiếng rẻ hơn ảnh 34,5%/kết quả [NGUỒN Meta]. 2–3 bản/nội dung, khác câu mở.
- **Không học** (§H4, H6): "chủ cần tiền gấp/cắt lỗ", "đón sóng", "dư địa tăng giá", "dòng tiền x tr/tháng", "rẻ nhất", "lô nội bộ", "99 khách đầu", đặt tên trang như CĐT.
- File: `content/qc/YYYY-MM-DD/<ma_qc>.md`, frontmatter:
  ```
  loai: quang-cao
  ma_qc: QC-A1          # ý tưởng A, bản 1 (QC-SK… sự kiện, QC-NN… Nhật/Hàn/Đài)
  y_tuong: QC-A         # mã trong workspace/plans/kho-y-tuong-qc.md
  khung_mo: gia-von | cau-hoi-von | so-do | tien-ich | dia-phuong
  dinh_dang: video-9x16 | anh-4x5 | anh-1x1
  cau_mo: "…"           # 3 giây đầu
  tieu_de: "…"          # ≤ 40 ký tự
  mo_ta: "…"            # ≤ 30 ký tự
  nut: Gửi tin nhắn | Gọi ngay | Đăng ký (chỉ sự kiện)
  dong_y: "…"           # đồng ý dùng ảnh/lời người thật (nguồn), rỗng nếu không có người thật
  can_cu: "[DỮ LIỆU] …"
  status: draft          # draft → review → approved (QC không tự chạy)
  ```
- Thân bài: phần trước "Xem thêm" ≤ 125 ký tự; giọng sales BĐS (`workspace/the-luat-viet-bai.md`: xưng em, câu ngắn, ✅); có con số → dòng **(*)** (§H8); nêu tên dự án → dòng PL (F5).
- Quy trình: copywriter → `python tools/db.py lint --text "…"` → compliance (§H, ghi `[QC] OK|CHẶN H…`) → judge (rubric Phần QC) → người dùng duyệt.

## 9. Kho ý tưởng và tổng kết tháng
`workspace/plans/kho-y-tuong-qc.md`: mỗi ý tưởng = góc + khung câu mở + định dạng + căn cứ (biên lai) + trạng thái §G. Không căn cứ → không vào kho. Cuối tháng: Thắng (vì sao) · Thua (chết ở bậc nào của phễu) · Thắng 1 chỉ số (giữ để thử tiếp) · Bài học → sửa kho · Loại. Trình bày theo khuôn 6 ô: tiêu đề = ý tưởng giữ/bỏ + tiền tháng sau đặt đâu (có con số); 5 nhóm trên là trục chia; ô "Cần quyết" ghi số tiền, người dùng giữ D.

## 10. Soi đối thủ (2 tuần/lần, researcher)
Thư viện QC Meta xem **không cần đăng nhập** (trình duyệt trong app). Tìm **đúng cụm** (`search_type=keyword_exact_phrase`: "đất nền", "sổ đỏ từng lô", "sổ đỏ trao tay", "ION CITY"), `country=VN`, `active_status=active`. **Mẹo tìm mẫu chạy lâu:** thêm `start_date[max]=<hôm nay − 60 ngày>` → chỉ còn mẫu đã chạy ≥ 60 ngày mà chưa tắt. Trang tải thêm bằng cuộn + nút "See more"; mỗi thẻ có "Library ID", "Started running on", "This ad has multiple versions"/"N ads use this creative", nút ở cuối thẻ. Tìm từ rời (`keyword_unordered`) ra nhiều mẫu lạc đề — tránh. Ở VN không có số chi tiêu → "chạy lâu" chỉ là [GIẢ THUYẾT] "đang hiệu quả". Đối thủ cùng tệp KCN đã thấy: Ion City (từ 2,9 tỷ/lô), "Đất nền KCN Bắc Giang" (Việt Yên, 60–80 tr/m², chạy ~10 tháng) → định vị "làm KCN, về quê có đất ~1 tỷ, có sổ", **không nêu tên đối thủ** (§H2). Ghi `workspace/research/YYYY-MM-DD-thu-vien-*.md`, không ghi tên/SĐT sale cá nhân.

## 11. Ghi chú vận hành
- Chạy thử Gọi và bán kính 50 km như **thí nghiệm có kiểm soát**: 1 thay đổi mỗi đợt 14 ngày, cùng mẫu, so giá/lượt xem đất.
- Hỏi 10–20 khách thật "anh/chị hay nhắn Zalo hay Messenger" để chỉnh tin chào (Decision Lab chỉ chia theo thế hệ).
- Người Việt ở Nhật/Hàn/Đài: luật quảng cáo BĐS nước sở tại **chưa có nguồn** → chỉ nội dung thông tin + mời xem livestream, không chào bán đầu tư.

## 12. Tự đo ở tuần 1–2 (chưa có nguồn)
CPM thật 30 vs 50 km · giá/tin nhắn và giá/cuộc gọi đất nền ~1 tỷ · % để lại SĐT/Zalo, % nghe máy · tỉ lệ nói chuyện → xem đất → cọc · giữ chân 3s của từng video · tần suất lúc bắt đầu mệt · VN có chọn được "Calls" + Call insights không (tạo nháp, không bật) · Nhật còn tối ưu cuộc trò chuyện không · bán kính tối thiểu/tối đa trên thanh trượt · hoá đơn có dòng VAT 10% không · gộp Gọi + Tin nhắn trong 1 nhóm được không.
