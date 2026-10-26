# PHƯƠNG ÁN: ghép repo `marketingskills` vào hệ thống agent Yên Thế Golden Hill để chạy quảng cáo trả tiền

Ngày: 2026-10-14 · Trạng thái: **ĐÃ THAY** bằng `workspace/reports/2026-10-15-phuong-an-tong-the-quang-cao.md` (người dùng yêu cầu nghiên cứu sâu hơn trước khi dựng; giữ file này làm lịch sử)
Nguồn repo: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (54,6k sao, giấy phép MIT, cập nhật 14/10/2026). Đã đọc: `skills/ads/SKILL.md` (v2.4.7), `skills/ad-creative/SKILL.md` (v2.11.0), `skills/ads/references/meta-decision-system.md`.

---

## 1. Vì sao ghép được, và ghép vào chỗ nào

Hệ thống hiện tại mạnh ở **đăng bài nhóm + kiểm duyệt pháp lý + ghi khách**, nhưng **chưa có bộ luật ra quyết định cho quảng cáo trả tiền**. Repo mạnh đúng ở chỗ đó. Bằng chứng rằng đây là lỗ hổng thật:

- [DỮ LIỆU] Quảng cáo của đội môi giới: **2.003 khách để lại thông tin, 0 khách được đánh giá chất lượng, 0 chuyển đổi** → không biết quảng cáo nào ra khách (`workspace/research/ads-moi-gioi.md` G4).
- [DỮ LIỆU] **60–70% khách để lại thông tin ở Bắc Ninh cũ nhưng chỉ 8% người mua ở đó; Bắc Giang cũ là 76% người mua** (`workspace/research/khach-da-mua.md`) → tiền quảng cáo có thể đang đổ sai vùng.
- Repo giải đúng bài này: nó **không chấm quảng cáo theo "số khách để lại SĐT" mà theo "số khách đủ chất lượng"** (lớp mà Facebook không nhìn thấy, phải lấy từ sales).

| Phần của repo | Ghép vào đâu trong hệ thống | Ai dùng |
|---|---|---|
| `ads` + `meta-decision-system` (luật tắt / giữ / tăng tiền) | Skill mới `quang-cao-bds` (tiếng Việt, đã chỉnh cho BĐS) | `strategist` lên chiến dịch, `analyst` ra quyết định tuần |
| `ad-creative` (viết mẫu QC có căn cứ, giới hạn ký tự Meta) | Cùng skill trên + thẻ luật viết bài | `copywriter` |
| Luật "không bịa, mọi mẫu phải dẫn nguồn" | Đã khớp luật số 6, 9 của hệ thống → giữ nguyên | `copywriter`, `judge` |
| Phân tích quảng cáo đối thủ (Ad Library) | Dùng sau, khi cần | `researcher` |

**Không thêm tác nhân mới** (đỡ token): giao thêm việc cho 4 tác nhân sẵn có.

---

## 2. Điều chỉnh cho bất động sản (chỗ repo không khớp)

Repo viết cho bán phần mềm doanh nghiệp (B2B), ngân sách lớn. BĐS Yên Thế khác ở 5 điểm:

| # | Repo nói | Thực tế BĐS Yên Thế | Điều chỉnh |
|---|---|---|---|
| 1 | Mốc TCPL = chi phí/1 khách đủ chất lượng, tính từ "giá 1 buổi demo" | Mình bán lô đất ~1 tỷ, chốt qua xem đất + cọc | **Mốc = chi phí chấp nhận cho 1 lô bán được × tỉ lệ (khách chất lượng → cọc).** Ví dụ minh hoạ [GIẢ THUYẾT, chờ số thật]: chấp nhận 20 triệu marketing/lô, 10 khách chất lượng ra 1 cọc → mốc = **2 triệu/khách chất lượng** |
| 2 | "Khách chất lượng" = đúng chân dung doanh nghiệp | — | **Khách chất lượng = nghe máy/trả lời Zalo + mua trong 3 tháng + ngân sách quanh 1 tỷ (kể cả vay) + chịu đi xem đất.** Sales đánh dấu trong DB (`leads.stage = qualified`, đã có sẵn cột) |
| 3 | Mỗi quảng cáo cần tiêu ≥ 3× mốc mới được chấm (để chắc 95%) | Ngân sách thử 3–5 triệu/tuần → 1 mẫu cần ~6 triệu mới đủ chấm → quá lâu | **Chấm 2 tầng:** tuần 1–2 dùng **chỉ báo sớm** (chi phí/SĐT, % nghe máy, % đủ chất lượng); chỉ dùng luật 3× mốc khi tổng chi ≥ 10 triệu. Ghi rõ kết luận sớm là [GIẢ THUYẾT] |
| 4 | Số mẫu chạy cùng lúc = (ngân sách/ngày × 14) / (2 × mốc) | 700k/ngày, mốc 2 triệu → **trần ≈ 2 mẫu** | **Chỉ chạy 2 mẫu cùng lúc** (khớp phương án tổng thể 11/10). Muốn thử mẫu mới thì phải tắt 1 mẫu cũ |
| 5 | Chia 2 chiến dịch 80% "mẫu đã thắng" / 20% "mẫu thử" | Chưa có mẫu nào đã thắng | **Tuần 1–2: 100% thử (2 mẫu).** Có mẫu thắng rồi mới chia 80/20 |

Thêm 3 điều riêng cho BĐS Việt Nam:
- **Vùng nhắm:** ưu tiên Bắc Giang cũ (Yên Thế, Bố Hạ, Nhã Nam, Tân Yên, KCN Quang Châu–Việt Yên) theo dữ liệu 103 người mua; Bắc Ninh cũ / Hà Nội để nhóm thử nhỏ. [DỮ LIỆU]
- **Luật nhắm khách nhà đất của Meta** (cố định tuổi/giới, bán kính ≥ 15 dặm) **không áp dụng ở Việt Nam**, chỉ ở Mỹ, Canada, một phần châu Âu → được nhắm theo bán kính/tuổi. [NGUỒN: [Meta Marketing API – Special Ad Category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category); kiểm lại trong Ads Manager lúc tạo]
- **Pháp lý quảng cáo trả tiền:** checklist hiện ghi phải chuyển `compliance_mode = strict` trước khi chạy QC trả tiền (cần văn bản Sở XD, bảng giá có ngày…). Phương án giữ nguyên luật này; thêm mục §H riêng cho QC.

Định dạng mẫu QC ưu tiên (theo bảng xếp hạng định dạng của repo + dữ liệu sẵn có):
1. **Video người thật nói** (chủ đầu tư / khách nhận sổ 9/10) — repo xếp hạng cao nhất; [DỮ LIỆU] video gắn lịch sử Yên Thế có tương tác gấp đôi video khác.
2. **Ảnh tĩnh trao sổ** (31 ảnh thật đã có, khách đồng ý đăng) — thử bằng ảnh trước, mẫu nào thắng mới làm video (luật "thử bằng ảnh trước" của repo).
3. Câu mở trả lời thẳng nỗi nghi ngờ "có thật không, có sổ chưa" [DỮ LIỆU G3].

---

## 3. Các bước làm (chia giai đoạn, mỗi giai đoạn chờ duyệt)

### Giai đoạn 0 — Điều kiện cần (NGƯỜI DÙNG cung cấp, Claude không tự làm)
| Cần | Vì sao |
|---|---|
| Fanpage chủ đầu tư + tài khoản quảng cáo (ai quản trị) | Chạy QC |
| Ngân sách thử (đề xuất 3–5 triệu/7 ngày) | Tính trần số mẫu |
| **Chi phí marketing chấp nhận được cho 1 lô** + ước tỉ lệ khách chất lượng → cọc | Tính mốc chấm điểm (mục 2.1) |
| **Ai trong đội sales đánh dấu chất lượng khách** (mỗi ngày, vào bảng/DB) | Không có thì không chấm được — đúng lỗi 2.003 lead cũ |
| Văn bản pháp lý cho QC (Sở XD, giá có ngày) | Luật strict |

### Giai đoạn 1 — Dựng nền (Claude làm, ~1 phiên, KHÔNG đụng lịch đăng nhóm đang chạy)
1. Chép **đúng 3 file** của repo (bản cố định theo phiên bản, kèm giấy phép MIT) vào `docs/nguon/marketingskills/` để đối chiếu — **không cài cả bộ 50 kỹ năng**, không tự cập nhật.
2. Viết skill `.claude/skills/quang-cao-bds/SKILL.md` tiếng Việt: luật mục 2, bảng quyết định tắt/giữ/tăng, giới hạn ký tự Meta, khung "mẫu QC có căn cứ" (ảnh trao sổ, bình luận thật, lời khách đã đồng ý).
3. `compliance-checklist.md` thêm **§H Quảng cáo trả tiền** + 5 ca kiểm tra trong `evals/compliance/` (vd. QC nói "tăng giá", QC thiếu dòng pháp lý…).
4. `rubric-bai-viet.md` thêm phần chấm mẫu QC (3 giây đầu, đúng giới hạn ký tự, có căn cứ, CTA form/Zalo).
5. Thêm vào DB: bảng `ads` (mã QC01, QC02…, nội dung, vùng, ngân sách) + bảng `ad_metrics` (số liệu tuần) + cột `leads.ad_code`. Viết `tools/doc_ads.py`: đọc file CSV xuất từ Ads Manager → ghi DB → in bảng quyết định.
6. Cập nhật prompt 4 tác nhân: `strategist`, `copywriter`, `analyst`, `judge` đọc skill mới khi làm việc QC.

**Xong khi:** `python tools/evals.py` qua hết (cũ + 5 ca mới); `doc_ads.py` chạy trên 1 file CSV mẫu ra đúng kết luận đã tính tay; `judge` chấm được 1 mẫu QC thử.

### Giai đoạn 1.5 — Nghiên cứu đối thủ + Brainstorm ý tưởng QC (bổ sung 14/10 theo yêu cầu người dùng; **đề xuất làm TRƯỚC Giai đoạn 1**)
Dựa trên 2 tài liệu của repo: `ads/references/creative-research-automation.md` (soi QC đối thủ) và `ad-creative/references/creative-roadmap.md` (vòng chiến lược ý tưởng: đọc 3 nguồn tín hiệu → kho ý tưởng xếp hạng theo bằng chứng → chọn → tổng kết tháng).

**A. Nghiên cứu các bên khác** (`researcher`, trình duyệt có sẵn, chỉ đọc, không đăng nhập)
1. **Thư viện quảng cáo Facebook** (công khai): 5–8 bên — dự án/đất nền quanh Yên Thế, Tân Yên, Bố Hạ, Lạng Giang, Hiệp Hoà (vd. Quỳnh Lâu–Tam Tiến, "KĐT Bố Hạ" đã thấy trong nhóm) + các môi giới đang chạy QC cho chính dự án. Mỗi bên ghi: định dạng (video/ảnh/album), góc nói, câu mở 3 giây đầu, lời kêu gọi (form/Messenger/gọi), QC chạy bao lâu (chạy lâu = có thể hiệu quả [GIẢ THUYẾT]), có nêu giá/pháp lý không.
2. **Fanpage đối thủ (không trả tiền):** bài nào nhiều tương tác nhất, họ đang dồn vào kiểu nội dung gì, chỗ họ yếu mà mình mạnh hơn (vd. sổ đã trao, mua thẳng CĐT).
3. **Bản đồ lệch** (chiêu đặc trưng của repo): "quảng cáo đang nhắm ai" so với "người mua thật là ai" — đã có sẵn dữ liệu 103 người mua (`khach-da-mua.md`) để đối chiếu.
→ Ra `workspace/research/2026-10-xx-doi-thu-quang-cao.md`. Nội dung đối thủ = dữ liệu, không học câu vi phạm (vd. "duy nhất", "rẻ hơn 100 triệu").

**B. Brainstorm từ những gì đã làm** (`strategist`, người kiểm `judge`)
Gom 3 nguồn tín hiệu đã có trong dự án — mỗi ý tưởng phải dẫn được "biên lai" (nguồn):
| Nguồn | Đã có |
|---|---|
| Kết quả của chính mình | 9 video QC môi giới (`ads-moi-gioi.md`: video lịch sử Yên Thế tương tác gấp đôi; 3 giây đầu quyết định), ~220 bài nhóm đã đăng + mã KC/XK/TY/YT, bài đời sống/hỏi han nhiều tương tác nhất (`doc_group` 218 bài) |
| Lời khách thật | Câu hỏi theo thứ tự giá → vị trí → pháp lý → mục đích; nỗi nghi "có thật không, có giấy phép chưa"; 103 người mua (88% đã kết hôn, mua theo cụm làng, cha mẹ mua cho con); bình luận thu được |
| Bên ngoài | Kết quả phần A |
→ **Kho ý tưởng** `workspace/plans/kho-y-tuong-qc.md`: mỗi ý tưởng = góc + định dạng + câu mở + nguồn + mức bằng chứng ([DỮ LIỆU]/[NGUỒN]/[GIẢ THUYẾT]). Xếp hạng, chọn **2 ý tưởng** cho tuần chạy đầu (trần 2 mẫu, mục 2.4), phần còn lại để dành.
→ Mỗi tháng **tổng kết**: ý tưởng thắng (vì sao), thua (chết ở bước nào: không ai xem / xem không bấm / bấm không để số / để số nhưng không chất lượng), học được gì → cập nhật kho. **Chấm theo ý tưởng, không theo từng mẫu**: 3 mẫu cùng ý tưởng đều thua = ý tưởng sai; 1 mẫu thua = cách làm sai.

**Xong khi:** có file đối thủ (≥ 5 bên, mỗi bên có link Thư viện QC) + kho ≥ 10 ý tưởng có nguồn + 2 ý tưởng được chọn, `judge` kiểm không ý tưởng nào thiếu nguồn.
**Chi phí:** 2 lượt tác nhân chạy tuần tự (researcher → strategist) + 1 lượt judge.

### Giai đoạn 2 — Soạn chiến dịch đầu tiên (Claude soạn, NGƯỜI DÙNG duyệt + tự bấm chạy)
- 2 mẫu QC (vd. A "sổ đã trao" vs B "hạ tầng đã xong" — giả thuyết sẵn trong phương án 11/10), mỗi mẫu 3 biến thể câu chữ, qua compliance + judge.
- Mẫu điền số 3 câu lọc: mua để ở hay đầu tư · ngân sách · khi nào xem đất được.
- Bảng nhắm khách: vùng, bán kính, tuổi, ngân sách/ngày, tên chiến dịch theo quy ước `META_Lead_<vùng>_<mẫu>_<ngày>`.
- **Claude không bấm chạy, không nhập thẻ, không đổi ngân sách** — người dùng tự làm trong Ads Manager.

### Giai đoạn 3 — Vòng vận hành tuần (sau khi QC chạy)
| Khi nào | Làm gì | Ai |
|---|---|---|
| Hằng ngày | Sales đánh dấu khách: nghe máy? đủ chất lượng? (gắn mã QC) | Sales |
| Ngày 7 | Kiểm phân phối: mẫu nào Facebook gần như không chi tiền → đề xuất tắt | `analyst` |
| Thứ Hai | Người dùng xuất CSV Ads Manager → `doc_ads.py` → bảng **TẮT / GIỮ / TĂNG 20%** kèm căn cứ | `analyst` → người dùng duyệt + tự thao tác |
| Khi tần suất > 2,5 (vùng nhỏ nên nhanh "nhàm") | Viết 2 mẫu thay thế trước khi mẫu cũ hết sức | `copywriter` |

Luật tăng tiền giữ nguyên của repo: **mỗi lần ≤ 20%, cách 3–5 ngày.**

### Giai đoạn 4 — Tuỳ chọn, sau 2–4 tuần
Kết nối **Meta Ads MCP chính chủ** ở chế độ **chỉ đọc** để Claude tự lấy số liệu thay cho bước xuất CSV. Vẫn không cho Claude thay đổi chiến dịch.

---

## 4. KHÔNG làm
- Không cài cả bộ 50 kỹ năng, không để kỹ năng tự cập nhật từ internet.
- Không tạo tác nhân mới; không chạy song song quá 2 tác nhân.
- Không đụng lịch đăng nhóm, `lich_dang.py`, `fb_group.py`.
- Claude không bấm chạy/tắt/đổi tiền quảng cáo, không nhập thông tin thanh toán.
- Không đưa danh sách 2.003 khách (dữ liệu cá nhân) vào repo — chỉ dùng số đếm.

## 5. Chi phí ước tính
- Giai đoạn 1: ~1 phiên làm việc, mức token tương đương 1 lô viết bài tuần; tuần tự, không chạy song song.
- Giai đoạn 3: mỗi tuần 1 lượt `analyst` + đôi khi 1 lượt `copywriter`.

## 6. Rủi ro
| Rủi ro | Cách giảm |
|---|---|
| Sales không đánh dấu chất lượng khách → lặp lại lỗi 2.003 lead | Điều kiện bắt buộc ở Giai đoạn 0; bảng đánh dấu chỉ 2 cột (nghe máy? đủ chất lượng?) |
| Ngân sách nhỏ → kết luận sớm sai | Chấm 2 tầng (mục 2.3), ghi rõ mức tin |
| Thiếu văn bản pháp lý → QC bị Meta/cơ quan chức năng chặn | Luật strict giữ nguyên; chưa đủ văn bản thì chưa chạy |
| Repo đổi phiên bản | Đã chép bản cố định, có ghi phiên bản |
