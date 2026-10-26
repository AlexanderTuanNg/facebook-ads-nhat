# Video vị trí: làm 20 giây theo vùng an toàn, bỏ ảnh vệ tinh Google/Esri khỏi quảng cáo, đổi giọng sang Azure chính thức (0đ)

> Nghiên cứu 26/10/2026 cho câu người dùng "nghiên cứu kỹ hơn cách làm… add thêm voice và edit quanh khu sao cho chuyên nghiệp hơn".
> Nhãn: [NGUỒN] tài liệu đã mở đọc (link) · [DỮ LIỆU] kiểm trên máy/file dự án · [GIẢ THUYẾT] kinh nghiệm nghề, chưa kiểm · [ƯỚC TÍNH] tự tính · [CẦN XÁC NHẬN].
> Kết luận pháp lý trong file này **cần luật sư xác nhận**.

**Đã đọc trọn 23 nguồn, lướt 12** (danh sách ở Phụ lục A). **Chỗ yếu, nói trước:**
1. Không đọc được trang thông số "Facebook Reels video" của Meta (lỗi 404): vùng an toàn 14% trên / 35% dưới lấy từ trang thông số Instagram Reels (qua kết quả tìm) và nhiều nguồn thứ ba. Mức −14 LUFS là thông lệ ngành, Meta không công bố.
2. Giá và giấy phép của FPT.AI, Viettel AI, Zalo AI, Google Cloud TTS chưa đọc được văn bản gốc. Giá Azure cũng không đọc được vì trang chỉ hiện "$-"; chỉ chắc phần miễn phí 0,5 triệu ký tự/tháng.
3. Chưa tìm được bài phân tích nghề của đơn vị BĐS Việt Nam về video vị trí. Chỉ đọc được 1 bài báo (Znews) và 1 nguồn nước ngoài về nhịp video ngắn. Phần kịch bản theo giây phần lớn là [GIẢ THUYẾT] nghề, cần đo bằng số xem 3 giây và ThruPlay.
4. Mixkit, Meta Sound Collection, Mapbox, Bing: chỉ đọc được bản tóm tắt hoặc trang phụ, chưa đọc văn bản giấy phép gốc.

---

## 0. Ba phát hiện đổi được quyết định ngay

| # | Phát hiện | So what |
|---|---|---|
| 1 | **Google Earth và Earth Studio cấm dùng trong quảng cáo, video quảng bá và trang rao bán BĐS.** Ảnh vệ tinh của Google Maps cũng chịu đúng giới hạn đó [NGUỒN](https://about.google/brand-resource-center/products-and-services/geo-guidelines/). Google "không cấp giấy phép dùng thương mại" [NGUỒN](https://www.google.com/earth/studio/faq/) | **Không** cho người dùng tự xuất Google Earth Studio để làm video bán đất hay cho thuê. Đăng thử lên Facebook cũng đã là dùng để quảng bá, nên phương án B (Earth Studio) trong STATE 26/10 **không nên đăng**, kể cả khi người dùng nhận rủi ro. Chỉ xem nội bộ thì được |
| 2 | Hai file `bay-ve-tinh.mp4` đang dùng **ảnh Esri World Imagery qua điểm truy cập miễn phí** [DỮ LIỆU `tools/bay_ve_tinh.py` dòng 50]. Lớp ảnh này theo Esri Master License Agreement [NGUỒN](https://www.arcgis.com/sharing/rest/content/items/10df2279f9684e4a9f6a7f08febac2a9?f=json). Dùng thương mại phải trả phí giấy phép, và điều khoản cấm "sao chép hoặc truyền đi vì mục đích thương mại" [NGUỒN](https://www.esri.com/en-us/legal/terms/web-site-service) | **Không đăng** bản có đoạn bay Esri, kể cả bài nhóm, cho tới khi có giấy phép |
| 3 | Bố cục hiện tại nằm sai vùng an toàn của Reels: tiêu đề ở y = 140/1280 (vùng cấm trên là 179), phụ đề sát đáy, thẻ số điện thoại ở y = 1162/1280 (vùng cấm dưới bắt đầu từ 832) [DỮ LIỆU `video_dinh_vi.py` dòng 167, 189, 302]. Meta cho biết video 9:16, có tiếng và để thông điệp trong vùng an toàn thì **khả năng được phân phối ở Reels cao gấp 2 lần** [NGUỒN](https://www.facebook.com/business/ads/facebook-instagram-reels-ads) | Sửa bố cục là việc lợi nhất, chỉ tốn khoảng 30 phút |

---

## 1. Cấu trúc video vị trí 15–30 giây

### 1.1 Thông số xuất file (áp cho cả 2 video)

| Mục | Đặt | Căn cứ |
|---|---|---|
| Khung, độ phân giải | 9:16, **1080 × 1920**, 30 hình/giây cố định, quét liên tục | 9:16 cho Reels [NGUỒN](https://www.facebook.com/business/ads/facebook-instagram-reels-ads). TikTok cần tối thiểu 720p [NGUỒN](https://ads.tiktok.com/help/article/creative-best-practices?lang=en). Meta yêu cầu H.264, pixel vuông, số hình/giây cố định, quét liên tục [NGUỒN](https://www.facebook.com/business/ads-guide/update/video) |
| Mã hoá | `-c:v libx264 -profile:v high -pix_fmt yuv420p -crf 18 -preset slow -maxrate 12M -bufsize 24M -movflags +faststart -use_editlist 0` | Meta yêu cầu file "không có danh sách chỉnh sửa" [NGUỒN](https://www.facebook.com/business/ads-guide/update/video). Meta không công bố mức bitrate; CRF 18 và trần 12 Mbps là [GIẢ THUYẾT] |
| Âm thanh | AAC stereo 48 kHz, 192 kbps; độ to tích hợp −14 LUFS, đỉnh −1,5 dBTP | Meta cần AAC stereo ≥ 128 kbps [NGUỒN](https://www.facebook.com/business/ads-guide/update/video). Mức −14 LUFS là [GIẢ THUYẾT] thông lệ |
| **Vùng an toàn** | Chừa 14% trên (269 px), 35% dưới (672 px) và 6% mỗi bên (65 px). Chữ và số điện thoại chỉ đặt trong khoảng **y 269–1248, x 65–1015** (bản 720 × 1280: y 179–832, x 43–677) | Theo trang Instagram Reels của Meta và nguồn thứ ba (lướt) [NGUỒN](https://www.facebook.com/business/ads-guide/update/image/instagram-reels) |
| Chữ trên hình | 5–10 chữ mỗi giây là tối đa; mỗi khung tối đa 2 dòng | TikTok khuyên hiển thị 5–10 chữ/giây [NGUỒN](https://ads.tiktok.com/help/article/creative-best-practices?lang=en) |
| Phụ đề | Luôn có, cỡ 44–52 px ở bề rộng 1080, đặt trong khoảng y ≈ 1050–1240 | Meta: phụ đề "không bắt buộc nhưng nên có" [NGUỒN](https://www.facebook.com/business/ads-guide/update/video). Reels mặc định bật tiếng [NGUỒN](https://www.facebook.com/business/ads/facebook-instagram-reels-ads) |
| 3 giây đầu | Nêu ngay **lợi ích hoặc nỗi lo của người xem**, không mở bằng tên dự án | TikTok: nêu "đề xuất nội dung" trong 3 giây đầu, móc câu trong 6 giây đầu [NGUỒN](https://ads.tiktok.com/help/article/creative-best-practices?lang=en). Checklist H11 [DỮ LIỆU] |
| Nhịp | Cắt hoặc đổi lớp chữ mỗi 1,5–2,5 giây; không lia chậm; độ dài 18–25 giây | Nguồn nước ngoài khuyên dưới 30–45 giây, chuyển cảnh nhanh, tránh lia chậm [NGUỒN](https://www.autoreelapp.com/blog/8-short-form-video-trends-every-real-estate-agent-should-know). Khoảng 1,5–2,5 giây là [GIẢ THUYẾT] |
| Màu, chữ | Vàng #FFCC00 cho tên khu và nhãn chính (Segoe UI Bold Italic `segoeuiz.ttf`); xanh băng #7FE6FF cho mốc; trắng cho phụ đề; nền tối độ mờ 55–65% | Máy có sẵn font [DỮ LIỆU]. Chữ có dấu tiếng Việt phải tự xem lại trên khung hình trước khi giao |
| Chuyển cảnh | Phóng nhanh (whip zoom) kèm lóe trắng 0,15 giây giữa bản đồ và flycam; chữ hiện bằng cách quét trái sang phải; không dùng chuyển cảnh lật 3D | ffmpeg trên máy có bộ lọc `xfade` [DỮ LIỆU]. Phong cách gần video người dùng thường đăng: TikTok khuyên "không quá bóng bẩy" [NGUỒN](https://ads.tiktok.com/help/article/creative-best-practices?lang=en) |
| Ghi nguồn, nhãn | Luôn thấy được: nguồn bản đồ hoặc ảnh vệ tinh (chữ nhỏ, ngay trên vùng cấm dưới), "Giọng đọc AI", "Bản đồ minh hoạ" | Mục 6 |

### 1.2 Kịch bản Sun City: cho thuê văn phòng tầng 2, 1.200 m² (khoảng 20 giây)

Bám dữ kiện có trong cấu hình [DỮ LIỆU `assets/cho-thue-sun-city/video/cau-hinh.json`]. Lời đọc khoảng 300 ký tự.

| Giây | Hình | Chữ trên hình (trong vùng an toàn) | Lời đọc |
|---|---|---|---|
| 0,0–3,0 **móc câu** | Phóng nhanh từ ảnh vệ tinh cấp tỉnh (Sentinel-2, mục 2) xuống khu Hùng Vương; lóe trắng 0,15 giây | **CẦN 1.200 m² VĂN PHÒNG?** (vàng nghiêng, cỡ to), dòng dưới: "Ngay trung tâm phường Bắc Giang" | "Công ty anh chị cần một sàn văn phòng 1.200 mét vuông ngay trung tâm?" |
| 3,0–7,5 vị trí | Bản đồ OSM tô tối, xoay nhẹ 0→5°; vòng sáng vàng gợn sóng ở toà nhà; viền neon chạy quanh khối nhà | "SUN CITY · 1B HÙNG VƯƠNG" | "Tầng 2 toà Sun City, 1B Hùng Vương." |
| 7,5–11,5 mốc | 3–4 tia sáng cong chạy từ mốc vào toà nhà, nhãn có đường gióng hiện lần lượt cách nhau 0,4 giây: Lotte Mart · Công viên Hoàng Hoa Thám · GO! Bắc Giang · BV Đa khoa Bắc Ninh số 2 (chỉ dùng mốc thật từ OSM, không ghi khoảng cách) | Tên mốc | "Quanh toà là Lotte Mart, GO!, công viên Hoàng Hoa Thám." |
| 11,5–16,0 bên trong | 3 ảnh thật tầng 2, đẩy chậm (Ken Burns), mỗi ảnh 1,5 giây, chuyển bằng trượt ngang | "1.200 m² · TẦNG 2" → "200.000 đ/m²/tháng (chưa gồm phí quản lý)" → "Miễn phí 1 tháng" [CẦN XÁC NHẬN điều kiện miễn phí] | "Hai trăm nghìn một mét vuông, chưa gồm phí quản lý, miễn phí tháng đầu." |
| 16,0–20,5 **lời mời** | Thẻ cuối: ảnh mặt tiền đã **làm mờ logo** (mục 6), nút vàng có số điện thoại đặt ở y ≈ 1050–1200/1920 | "Xem mặt bằng: gọi/Zalo **0962.478.888**"; chữ nhỏ: "(*) Thông tin tại thời điểm đăng, áp dụng có điều kiện" · "Giọng đọc AI" · "© OpenStreetMap contributors" | "Gọi không chín sáu hai, bốn bảy tám, tám tám tám để đi xem mặt bằng." |

Ghi chú:
- **Thêm "chưa gồm phí quản lý".** Phí quản lý 20 triệu/tháng tính ra khoảng 16,7 nghìn/m² [DỮ LIỆU STATE 25/10]. Chỉ nói "200 nghìn/m²" dễ bị coi là gây nhầm lẫn về giá theo Luật Quảng cáo Điều 8 khoản 9 [NGUỒN](https://luatduonggia.vn/phap-luat/hanh-vi-cam-trong-hoat-dong-quang-cao/).
- Địa chỉ: ghim cũ hiện "243 Hùng Vương", nhưng điểm VNVC trên Google Maps ghi "1B đường Hùng Vương", cách ghim khoảng 25 m [DỮ LIỆU STATE 26/10] → dùng "1B Hùng Vương".
- Muốn thu khách như video mẫu Vinhomes: video chỉ mời "Bấm Đăng ký". Biểu mẫu là phần cài trong quảng cáo, phải có ô đồng ý và đường dẫn chính sách bảo mật (checklist H9). Không vẽ biểu mẫu vào video.

### 1.3 Kịch bản Yên Thế Golden Hill: đất nền (khoảng 22 giây, theo luật §F, §G)

Không có khoảng cách, không số phút, không "nhất". Câu "500 triệu" luôn đi kèm điều kiện, chữ điều kiện nằm trên hình ít nhất 4 giây. Địa danh viết đúng F4.

| Giây | Hình | Chữ trên hình | Lời đọc |
|---|---|---|---|
| 0,0–3,0 **móc câu** | Flycam thật bay vào khu [DỮ LIỆU clip `assets/dong-lac/1784…mp4`], tăng tốc rồi lóe trắng | **VỀ YÊN THẾ LÀM NHÀ?** dòng dưới: "Xem lô đất này trước đã" | "Anh chị muốn về Yên Thế làm nhà cho bố mẹ, cho con?" |
| 3,0–7,5 vị trí | Ảnh vệ tinh Sentinel-2 cấp vùng phóng xuống (10 m, chỉ dùng cho cảnh xa); la bàn nhỏ góc phải; chữ chạy hướng "Phía Bắc khu vực Bắc Giang cũ" (hướng tính từ toạ độ thật, không ghi số km) [CẦN XÁC NHẬN cách gọi hướng] | "XÃ YÊN THẾ · THÀNH PHỐ BẮC NINH" (dòng nhỏ: "khu vực Yên Thế – Bắc Giang cũ") | "Yên Thế Golden Hill, trung tâm xã Yên Thế, mặt đường tỉnh 292." |
| 7,5–12,0 **quanh khu** | Dừng hình flycam: **viền neon chạy dọc ranh giới khu** (vẽ theo điểm ảnh trên chính khung flycam, mục 5.5), tô vàng mờ; nhãn có đường gióng: "Mặt đường ĐT.292" · "Quảng trường trong khu" | Nhãn vàng nghiêng | "Đường nhựa, quảng trường trong khu, lô đã san nền." (đúng chữ có sẵn trong cấu hình) |
| 12,0–17,0 giá | Ảnh chính sách (bản có hotline) đẩy chậm; khối chữ lớn | **CHỈ VỚI 500 TRIỆU ĐÃ SỞ HỮU LÔ ĐẤT**, ngay dưới là "Trả trước 500 triệu khi ký (lô đến khoảng 1,3 tỷ) · còn lại 4 đợt 15% trong 180 ngày, đợt cuối nhận sổ" | "Chỉ với 500 triệu đã sở hữu lô đất: trả trước 500 triệu khi ký, phần còn lại chia 4 đợt trong 180 ngày." |
| 17,0–22,0 **lời mời** | Ảnh trao sổ thật (đã có đồng ý, H3) → thẻ cuối | "Gọi/Zalo **0965.539.599**" · chữ nhỏ: "(*) Theo chính sách CĐT tại thời điểm đăng, áp dụng có điều kiện" · "Ảnh và bản đồ minh hoạ vị trí" · "Giọng đọc AI" | "Gọi không chín sáu lăm, năm ba chín, năm chín chín để hẹn xem đất." |

Ghi chú:
- **Không nhắc "377 lô, 12,1 ha" khi có hình** (KM2 còn KHOÁ khi kèm ảnh). Khu buổi tối (KM3) chỉ dùng ảnh đêm thật.
- **Mốc "Bố Hạ" kèm tia sáng nối vào khu dễ bị hiểu là "gần Bố Hạ"** và trái tinh thần F13 (hạn chế liệt kê tên xã, phường) → khuyên bỏ, chỉ giữ ĐT.292 và BV Đa khoa Yên Thế [GIẢ THUYẾT].
- **Không chạy video này làm quảng cáo trả tiền khi H1 còn "CHƯA"**: dòng pháp lý còn KHOÁ, website đang bị chiếm. Đăng bài nhóm ở chế độ test thì được [DỮ LIỆU checklist §H].

---

## 2. Ảnh vệ tinh: chỉ Sentinel-2 dùng thương mại miễn phí; ảnh nét thì phải mua

| Nguồn | Dùng cho quảng cáo trả tiền? | Ghi nguồn | Tài khoản/khoá | Chất lượng ở nông thôn Bắc Giang |
|---|---|---|---|---|
| **Google Earth / Earth Studio** | **KHÔNG.** Cấm quảng cáo số, video quảng bá, trang rao BĐS [NGUỒN](https://about.google/brand-resource-center/products-and-services/geo-guidelines/). Không có giấy phép thương mại [NGUỒN](https://www.google.com/earth/studio/faq/) | "Google Earth" + tên nhà cung cấp ảnh, luôn hiện | Cần tài khoản Google, chỉ chạy trên Chrome | Nét [GIẢ THUYẾT], nhưng không được dùng |
| **Google Maps, lớp vệ tinh** | **KHÔNG** (cùng giới hạn với Earth). Bản đồ thường dùng trong video quảng bá cũng phải xin phép [NGUỒN](https://about.google/brand-resource-center/products-and-services/geo-guidelines/) | "Map data ©Google" | Không | Không áp dụng |
| **Esri World Imagery** (công cụ đang dùng) | **Chưa được** khi chưa trả phí giấy phép thương mại [NGUỒN](https://www.esri.com/en-us/legal/terms/web-site-service). Lớp ảnh "không dành để xuất ô ảnh dùng ngoại tuyến" [NGUỒN](https://www.arcgis.com/sharing/rest/content/items/10df2279f9684e4a9f6a7f08febac2a9?f=json) | "Esri, Vantor, Earthstar Geographics, and the GIS User Community" (+ "Powered by Esri") | Cần tài khoản ArcGIS có giấy phép | Phần lớn đất liền có ảnh độ phân giải ≤ 1 m [NGUỒN item] |
| **Sentinel-2 (Copernicus)** | **ĐƯỢC.** Cho phép sao chép, phân phối, chỉnh sửa, công bố, không loại trừ dùng thương mại [NGUỒN](https://ads.atmosphere.copernicus.eu/licences/ec-sentinel) | "Contains modified Copernicus Sentinel data 2026" | Copernicus Browser cần tài khoản miễn phí (người dùng tự tạo). Kho mở trên AWS có thể không cần tài khoản [GIẢ THUYẾT, cần thử] | **10 m/điểm ảnh**: thấy rõ sông, đường lớn, khu dân cư ở mức tỉnh, huyện; không thấy lô đất. Miền Bắc hay có mây → chọn ảnh mùa khô, mây < 10% [GIẢ THUYẾT] |
| Sentinel-2 cloudless (EOX) | **KHÔNG** miễn phí: bản miễn phí là CC BY-NC-SA (phi thương mại); dùng thương mại phải mua giấy phép EOX [NGUỒN lướt](https://cloudless.eox.at/documentation/license) | Chuỗi ghi nguồn EOX | Mua giấy phép | 10 m, không mây |
| Mapbox Satellite | **Chưa rõ.** Tài liệu ảnh tĩnh không nói về video; in ấn phải hỏi bộ phận bán hàng [NGUỒN](https://docs.mapbox.com/help/dive-deeper/static-maps.md) | Mapbox + OpenStreetMap | Cần tài khoản và khoá, tính tiền theo lượt gọi | [CẦN XÁC NHẬN] |
| Bing Maps | **Không dùng.** Trang "quyền in" cũ nay chuyển về Azure Maps; Bing Maps for Enterprise đang ngừng [NGUỒN lướt] | — | — | — |
| Mua ảnh Pléiades 50 cm (qua đại lý) | **Được nếu mua giấy phép phù hợp.** Giấy phép mặc định chỉ dùng nội bộ, dùng thêm phải trả phụ phí [NGUỒN lướt](https://landinfo.com/satellite-imagery-pricing/) | Theo hợp đồng | Đặt mua | 50 cm, thấy được đường nội bộ. Ảnh lưu trữ khoảng 25 USD/km², tối thiểu 25 km² → **khoảng 625 USD ≈ 16 triệu đ** + phí giấy phép marketing [ƯỚC TÍNH, tỷ giá 26.000] |
| Bản đồ OSM (nền hiện tại) | **Dữ liệu** OSM được dùng với ghi nguồn. **Máy chủ ô bản đồ** của OSM thì cấm tải trước, tải hàng loạt, dùng ngoại tuyến, và không bảo đảm cho người dùng thương mại [NGUỒN](https://operations.osmfoundation.org/policies/tiles/) | "© OpenStreetMap contributors" | Không | Yên Thế rất thưa [DỮ LIỆU] |

**Đề xuất (rẻ trước):**
1. **Cảnh xa:** Sentinel-2. Người dùng xuất 1 ảnh màu thật cho mỗi dự án từ Copernicus Browser (khoảng 10 phút). Nếu thử được kho mở AWS thì Claude tự tải. Ghi "Contains modified Copernicus Sentinel data 2026".
2. **Cảnh gần:** flycam thật của CĐT hoặc ảnh tự chụp. Viền neon vẽ thẳng lên khung flycam. Đây là cách duy nhất vừa nét vừa không vướng giấy phép.
3. **Lớp đường, nhãn:** tự vẽ từ dữ liệu OSM (Overpass) thay cho tải ô ảnh từ tile.openstreetmap.org.
4. Chỉ mua ảnh Pléiades nếu cổng 09/11 cho thấy video vị trí kéo được khách.
5. **Không** dùng Google Earth Studio, **không** dùng Esri cho tới khi Esri xác nhận bằng văn bản.

---

## 3. Giọng đọc: dùng Azure Speech chính thức, cùng giọng HoaiMy/NamMinh, miễn phí ở mức đang dùng

| Dịch vụ | Giá | Giấy phép thương mại | Giọng miền Bắc | Khuyên |
|---|---|---|---|---|
| **Microsoft Azure Speech** (chính thức, có khoá) | Gói F0: **0,5 triệu ký tự/tháng miễn phí** [NGUỒN](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/). Trả tiền khoảng 15–16 USD cho 1 triệu ký tự [nguồn thứ ba, lướt] | Dùng theo Microsoft Product Terms. **Bắt buộc công khai là giọng tổng hợp** để người nghe không bị lừa (Code of Conduct, mục 3) [NGUỒN](https://learn.microsoft.com/en-us/legal/ai-code-of-conduct) | HoaiMyNeural (nữ), NamMinhNeural (nam): đúng 2 giọng đang dùng [DỮ LIỆU] | **DÙNG #1.** 300 ký tự/video → đủ khoảng 1.600 video/tháng miễn phí [ƯỚC TÍNH] |
| edge-tts (đang dùng) | 0đ | **Không có giấy phép.** Thư viện mượn dịch vụ đọc của trình duyệt Edge. Microsoft chặn SSML tuỳ biến, chỉ cho 1 thẻ giọng + 1 thẻ nhịp [NGUỒN](https://github.com/rany2/edge-tts). Dịch vụ có thể đổi bất kỳ lúc nào: 12/2025 đã đòi dấu nhận diện trình duyệt Edge [NGUỒN lướt](https://github.com/Migushthe2nd/MsEdgeTTS) | Như Azure | **Chỉ dùng làm nháp nội bộ**, không dùng cho bản đăng hay quảng cáo [GIẢ THUYẾT về rủi ro điều khoản] |
| FPT.AI | 100.000 ký tự miễn phí/tháng; gói 500 nghìn – 10 triệu ký tự (giá không ghi) [NGUỒN](http://docs.fpt.ai/docs/en/speech/documentation/voice-maker/) | Chưa thấy văn bản → hỏi FPT | banmai, thuminh (nữ), leminh (nam) [NGUỒN lướt] | Dự phòng #3 |
| Vbee | Gói tuỳ chỉnh 500 đ/1.000 ký tự, tối thiểu 5 triệu ký tự = **2,5 triệu đ/năm** [NGUỒN](https://help.vbee.vn/docs/thong-bao/ban-cap-nhat-thang-04-2025). Gói VIP khoảng 11,99 USD/tháng [lướt] | Chưa đọc được điều khoản quảng cáo | Nhiều giọng Bắc [GIẢ THUYẾT] | Thử nếu Azure nghe "máy" |
| Viettel AI | Chưa thấy bảng giá; 16 giọng, có giọng Bắc Quỳnh Anh [lướt] | Chưa đọc | Có | Để sau |
| Zalo AI | Tài liệu cũ, không rõ còn chạy [lướt] | — | 2 giọng Bắc | Bỏ |
| ElevenLabs | Starter **6 USD/tháng** (30 nghìn ký tự, khoảng 30 phút), có Commercial License; gói Free không ghi giấy phép thương mại [NGUỒN](https://elevenlabs.io/pricing) | Có từ gói Starter | Chất lượng tiếng Việt chưa thử [GIẢ THUYẾT] | Dự phòng #2 nếu muốn giọng có cảm xúc |
| Google Cloud TTS | Không đọc được trang giá | Theo điều khoản Google Cloud | Có vi-VN [GIẢ THUYẾT] | Để sau |
| **Giọng thật** của sale | 0đ | Cần sale đồng ý bằng văn bản (H3) | Tự nhiên nhất | Tốt nhất cho video dài hơi [GIẢ THUYẾT] |

**Mẹo cho giọng máy nghe tự nhiên:**
- **Azure (SSML đầy đủ):** chèn `<break time="250ms"/>` sau câu móc và trước số điện thoại. Đặt `<prosody rate="+6%" pitch="+2%">` cho câu móc, `rate="-5%"` cho câu điều kiện giá. Tách số điện thoại thành 3 cụm có dấu phẩy. Thẻ nhấn giọng `emphasis` và các "phong cách đọc" thường không có cho tiếng Việt [GIẢ THUYẾT, cần thử].
- **edge-tts (chỉ chỉnh được nhịp/âm lượng/cao độ cho cả lượt gọi):** sinh **từng câu một** với nhịp khác nhau, rồi nối bằng ffmpeg, chèn 150–300 ms im lặng giữa các câu. Đây là cách "SSML nghèo" [DỮ LIỆU: hàm `Communicate(rate, volume, pitch, boundary)`].
- **Chung:** viết số thành chữ (đang làm), tránh chữ IN HOA (máy dễ đánh vần từng chữ), câu ≤ 15 chữ, mỗi câu 1 ý, dùng dấu phẩy để tạo chỗ ngắt.
- Mốc thời gian từng chữ: `boundary="WordBoundary"`. Mốc tính theo đơn vị 100 nano giây (chia 10.000.000 ra giây) [DỮ LIỆU `edge_tts/communicate.py`: TICKS_PER_SECOND]. Azure SDK có sự kiện `word_boundary` tương tự [GIẢ THUYẾT].

---

## 4. Nhạc nền: chọn nhạc ngay trong Meta khi chạy quảng cáo, Pixabay cho file dựng sẵn

1. **Nhạc của Meta (Sound Collection / nhạc chọn trong Ads Manager), an toàn nhất trên Facebook.** Ads Manager cho chọn tối đa 5 bài, hoặc để Advantage+ tự chọn nhạc miễn phí bản quyền [NGUỒN](https://www.facebook.com/business/ads/facebook-instagram-reels-ads). Trợ giúp Instagram ghi nội dung Sound Collection "dùng được cho mục đích thương mại như quảng cáo" [NGUỒN lướt](https://help.instagram.com/ipad-app/402084904469945). Giấy phép gắn với nền tảng Meta (điều khoản cũ ghi "chỉ trên nền tảng Facebook") [lướt].
   - **Cách làm:** xuất video **không có nhạc** (chỉ lời đọc), rồi thêm nhạc lúc dựng quảng cáo (bước Phương tiện → Nhạc) hoặc chọn trong thư viện âm thanh khi đăng Reels.
   - Không dùng nhạc "thịnh hành" cho bài sẽ chạy quảng cáo [lướt].
2. **Pixabay Music, khi cần nhạc nằm sẵn trong file** (bài nhóm, TikTok). Giấy phép cho dùng thương mại, không bắt ghi nguồn; cấm bán lại nguyên bản; cấm dùng gây hiểu nhầm [NGUỒN](https://pixabay.com/service/terms/).
   - **Cách tải đúng:** chỉ tải từ pixabay.com/music (người dùng tự đăng nhập nếu trang yêu cầu [CẦN XÁC NHẬN]). Lưu tên bài, đường dẫn, ngày tải vào `assets/nhac/nguon-nhac.csv` làm bằng chứng.
   - Có thể bị hệ thống nhận diện bản quyền đánh dấu nhầm → giữ bằng chứng để khiếu nại [GIẢ THUYẾT].
- **Không dùng:** YouTube Audio Library (trợ giúp chỉ nói về dùng trên YouTube [NGUỒN](https://support.google.com/youtube/answer/3376882?hl=en), nguồn thứ ba thì mâu thuẫn). Mixkit (chưa đọc văn bản giấy phép gốc).
- Nhạc tự tổng hợp hiện nay: 0 rủi ro, nhưng nghe "máy". Giữ làm dự phòng.

---

## 5. Tám kỹ thuật dựng nên thêm, xếp theo lợi chia công (Python + Pillow + ffmpeg, không numpy)

Máy có sẵn các bộ lọc ffmpeg `loudnorm`, `sidechaincompress`, `xfade`, `ass`, `zoompan`, `gblur` và các font `segoeuiz.ttf`, `seguisym.ttf`, `segmdl2.ttf`, `seguiemj.ttf` [DỮ LIỆU].

| # | Kỹ thuật | Lợi | Công [ƯỚC TÍNH] |
|---|---|---|---|
| 1 | **Bố cục theo vùng an toàn** | Chữ và số điện thoại không bị nút Reels che; Meta nói phân phối có thể gấp 2 | 0,5 giờ |
| 2 | **Âm thanh chuẩn:** nhạc tự nhỏ khi có lời (ducking) + −14 LUFS | Nghe "chuyên nghiệp" ngay, lời rõ | 0,5 giờ |
| 3 | **Phụ đề karaoke từng chữ** | Người xem tắt tiếng vẫn hiểu; giữ mắt | 1,5 giờ |
| 4 | **Nhãn vàng nghiêng có đường gióng + biểu tượng** | Giống video mẫu nhất | 1,5 giờ |
| 5 | **Viền neon chạy dọc ranh giới + tô vùng** | "Khoanh khu" như Vinhomes | 2 giờ |
| 6 | **Tia sáng cong nối mốc → dự án**, đầu tia phát sáng, gợn sóng ở đích | Nâng cấp tia thẳng đang có | 1 giờ |
| 7 | **Chuyển động máy quay:** easing, xoay nhẹ, nhoè chuyển động, parallax, lóe chuyển cảnh | Hết cảm giác "slide ảnh" | 2–3 giờ |
| 8 | **Chữ chạy hướng + la bàn + hạt sáng** | Thêm chất "Phía Tây Bắc / Sông Cầu" | 2 giờ |

Cách làm ngắn gọn:

1. **Vùng an toàn.** Thêm hằng số `AN_TOAN = (0.06W, 0.14H, 0.94W, 0.65H)`. Tiêu đề đặt ở y = 0,17H; phụ đề ở 0,55–0,64H; thẻ cuối dồn khối chữ và nút số điện thoại vào 0,40–0,64H. Dòng ghi nguồn cỡ chữ 16–18 đặt ngay trên 0,65H. Thêm cờ `--luoi` để vẽ khung đỏ vùng cấm lên ảnh xem thử, kiểm bằng mắt.
2. **Ducking + độ to.**
   - Cách chắc nhất khi đã biết mốc lời: nhạc dùng `volume='if(between(t,a,b),0.25,1)':eval=frame` rồi làm mềm bằng `afade`. Cách tự động: `[nhac][doc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400`.
   - Sau đó chạy `loudnorm` **2 lượt**: lượt 1 `loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json` để đọc `measured_I/TP/LRA/thresh`; lượt 2 truyền các số đo đó kèm `linear=true`. Bỏ `alimiter=0.89` hiện tại vì nó chỉ chặn đỉnh, không chuẩn độ to.
3. **Karaoke.**
   - Gọi `Communicate(..., boundary="WordBoundary")`, gom các sự kiện thành `[{chu, tu, den}]` (offset/1e7). Gộp chữ thành dòng ≤ 26 ký tự, tối đa 2 dòng một "trang"; đổi trang khi hết câu hoặc đầy.
   - Mỗi khung: chữ đã đọc màu trắng, chữ đang đọc màu vàng, phóng 1,08 lần trong 120 ms, chữ chưa đọc trắng 60%; nền chữ nhật bo góc đen 55%.
   - Chữ trên màn hình (vd "ĐT.292") khác chữ đọc (vd "tỉnh hai chín hai"): giữ bảng ánh xạ như file `loi-doc-*.json` đang có, căn theo câu, chia đều thời gian các chữ trong câu.
4. **Nhãn có đường gióng.**
   - Chấm sáng ở mốc → đường gióng chéo 45° lên 40 px rồi nằm ngang 120 px → hộp tên.
   - Hiện dần theo thứ tự: đường gióng tự vẽ (0,25 giây) → chữ quét trái sang phải bằng mặt nạ có bề rộng tăng dần.
   - Chữ Segoe UI Bold Italic màu vàng, viền đen 2 px, thêm lớp sáng (vẽ chữ lên lớp riêng, `GaussianBlur(6)`, chồng kiểu `ImageChops.screen`).
   - Biểu tượng: ký tự từ `segmdl2.ttf`/`seguisym.ttf` (nhà, bệnh viện, mua sắm, cây) đặt trong vòng tròn [GIẢ THUYẾT: mã ký tự cần dò từng cái, xem lại bằng ảnh].
   - Tự né chồng chéo: xếp nhãn trái/phải xen kẽ, đẩy y cách nhau ≥ 56 px.
5. **Viền neon chạy.**
   - Lấy ranh giới: từ OSM nếu có; từ toạ độ góc trên mặt bằng 1/500 của CĐT; hoặc toạ độ điểm ảnh vẽ tay trên khung flycam dừng hình (Golden Hill).
   - Chia lại đa giác thành điểm cách đều 4 px theo chiều dài cung (cộng dồn khoảng cách). Giây đầu vẽ dần từ 0 tới 100% chu vi.
   - Sau đó vẽ viền nền mờ (độ đục 90), rồi một "sao chổi" dài 18% chu vi chạy vòng: đầu = (t × v) mod L, độ đục giảm dần về đuôi.
   - Lớp sáng: vẽ trên lớp RGBA riêng, chồng 3 bản làm mờ (bán kính 3, 8, 18) bằng `ImageChops.screen`. Tô vùng vàng 20–35% nhấp nháy theo sin 0,8 Hz.
   - Mỗi giai đoạn một màu như video mẫu, chỉ khi CĐT có ranh giới từng giai đoạn [CẦN XÁC NHẬN].
6. **Tia cong.**
   - Đường cong bậc 2 B(u) = (1−u)²P0 + 2(1−u)uC + u²P1. Điểm điều khiển C lệch khỏi trung điểm theo pháp tuyến một đoạn 0,2·|P1−P0|.
   - u chạy 0→1 theo easing trong 0,6 giây. Vẽ đường gấp khúc 0..u, đuôi mảnh và mờ dần; đầu tia là chấm sáng.
   - Tới đích thì bật 2 vòng gợn sóng: bán kính r = r0 + 120·τ, độ đục 1−τ.
7. **Máy quay.**
   - Zoom theo thang log (đang có) + easing bậc 3 vào/ra.
   - Xoay bản đồ 0→5° bằng `Image.rotate` trên ảnh nền lớn hơn khung 15% để không lộ góc.
   - Đoạn phóng nhanh: trộn 3 khung con (t−1/90, t, t+1/90) bằng `Image.blend` để có nhoè chuyển động.
   - Parallax: lớp nhãn trôi 1,1 lần so với nền, lớp viền tối góc đứng yên.
   - Chuyển cảnh: lóe trắng 0,15 giây (trộn với ảnh trắng theo tam giác độ đục) hoặc `xfade=transition=fadewhite:duration=0.3` khi ghép đoạn.
8. **Chữ chạy, la bàn, hạt sáng.**
   - Hướng tính từ toạ độ thật bằng công thức góc phương vị (atan2 của Δlon·cos(lat), Δlat), đổi ra 8 hướng.
   - La bàn: mũi tên chữ N xoay ngược góc xoay bản đồ.
   - Chữ chạy "PHÍA BẮC…": từng chữ cái trượt vào lệch nhau 30 ms; hoặc chạy dọc một đường thẳng nghiêng song song đường ĐT.292.
   - Hạt sáng: 40 hạt cố định hạt giống ngẫu nhiên (để dựng lại ra y hệt), mỗi hạt có vị trí, vận tốc nhẹ lên trên, tuổi thọ 1–2 giây; vẽ chấm 2–4 px lên lớp sáng.
   - **Chỉ dùng tên sông, đường có thật trong dữ liệu**, không bịa.

Cổng kiểm sau khi dựng: xuất 6 ảnh khung (giây 1, 3, 6, 9, 13, 18) kèm lưới vùng an toàn. Đọc lại từng chữ có dấu, đo độ to bằng `ebur128`, chạy máy kiểm lint cho lời đọc và chữ trên hình. Gửi người dùng duyệt trước khi gắn vào bài (luật 25/10).

---

## 6. Rủi ro pháp lý: logo, giọng AI và ảnh vệ tinh là ba chỗ phải sửa trước khi đăng (cần luật sư xác nhận)

| Rủi ro | Căn cứ | Làm gì |
|---|---|---|
| Ảnh Google Earth/Maps vệ tinh, Esri trong video bán hàng | Hướng dẫn Geo của Google [NGUỒN](https://about.google/brand-resource-center/products-and-services/geo-guidelines/); điều khoản Esri 2.2, 2.2.1 [NGUỒN](https://www.esri.com/en-us/legal/terms/web-site-service) | Bỏ đoạn `bay-ve-tinh.mp4` khỏi bản đăng; thay bằng Sentinel-2 + flycam |
| Logo **SHB, VNVC, Manulife** ở mặt tiền và poster trong ảnh tầng 2 | Luật Quảng cáo Điều 8: khoản 13 (vi phạm sở hữu trí tuệ), khoản 9 (gây nhầm lẫn) [NGUỒN](https://luatduonggia.vn/phap-luat/hanh-vi-cam-trong-hoat-dong-quang-cao/). Logo lớn dễ bị hiểu là các hãng này bảo chứng hoặc đang là đối tác [GIẢ THUYẾT] | **Làm mờ logo** trong video và ảnh (khuyên). Không nêu tên hãng trong lời đọc. Nếu muốn ghi "toà có SHB, VNVC": phải đúng là khách thuê đang hoạt động và có ý kiến luật sư |
| Giọng đọc AI không ghi nhãn | Luật Trí tuệ nhân tạo 2025 (134/2025/QH15) Điều 11 khoản 3: bên dùng AI trong hoạt động thương mại phải thông báo rõ khi đưa âm thanh, video do AI tạo ra công chúng nếu có thể gây nhầm lẫn; Nghị định 142/2026/NĐ-CP Điều 18: nhãn hiện trên nội dung, ở tiêu đề/mô tả hoặc bằng âm thanh, hiệu lực 01/5/2026 [NGUỒN](https://lsvn.vn/thong-bao-va-gan-nhan-nhan-biet-noi-dung-do-ai-tao-ra-the-nao-a172678.html). Meta yêu cầu nhãn AI cho "Reel có giọng AI giống thật" ở bài thường; quảng cáo theo quy trình riêng [NGUỒN](https://www.meta.com/help/artificial-intelligence/1783222608822690/). Microsoft bắt công khai giọng tổng hợp [NGUỒN](https://learn.microsoft.com/en-us/legal/ai-code-of-conduct) | Ghi chữ **"Giọng đọc AI"** trên video (thẻ cuối) và trong chú thích; bật nhãn AI khi đăng Reels thường. Chi phí 0đ, phủ được cả 3 bên |
| "Ảnh minh hoạ" | Checklist F12 (ảnh AI, phối cảnh). Bản đồ và đồ hoạ không phải ảnh chụp [GIẢ THUYẾT] | Ghi "Bản đồ minh hoạ vị trí" cho phần đồ hoạ; ghi "Phối cảnh minh hoạ" nếu có phối cảnh. Flycam, ảnh thật thì ghi ngày quay (F10) |
| Câu giá gây hiểu nhầm | Luật Quảng cáo Điều 8 khoản 9 [NGUỒN]; KM7c; H8 | Sun City thêm "chưa gồm phí quản lý"; Golden Hill có đủ điều kiện và dòng (*) |
| Quảng cáo trên mạng phải nhận diện được | Luật Quảng cáo sửa đổi 75/2025/QH15 (hiệu lực 01/01/2026), Điều 23 khoản 2: dấu hiệu nhận diện bằng chữ, ký hiệu, âm thanh [NGUỒN tóm tắt](https://luatvietnam.vn/linh-vuc-khac/diem-moi-cua-luat-quang-cao-sua-doi-2025-883-102813-article.html) | Quảng cáo trả tiền: nhãn "Được tài trợ" của Meta [GIẢ THUYẾT là đủ]. Bài nhóm có tính chất chào bán: hỏi luật sư có phải ghi chữ "Quảng cáo" không |
| Từ cấm "nhất" | Luật Quảng cáo Điều 8 khoản 11 [NGUỒN]; F2 | Chạy lint cả chữ trên hình, không chỉ caption |
| Máy chủ ô bản đồ OSM | Chính sách cấm tải trước, dùng ngoại tuyến [NGUỒN](https://operations.osmfoundation.org/policies/tiles/) | Chuyển sang tự vẽ từ dữ liệu Overpass, giữ dòng ghi nguồn OSM |

---

## 7. Cần người dùng quyết (kèm chi phí)

| # | Quyết gì | Đề xuất | Chi phí | Ai giữ D · hạn |
|---|---|---|---|---|
| 1 | Bỏ đoạn bay ảnh Esri khỏi mọi bản đăng; ảnh vệ tinh dùng Sentinel-2 + flycam | **Đồng ý** (khó đảo nếu đã đăng rồi bị khiếu nại) | 0đ; người dùng mất ~10 phút tạo tài khoản Copernicus và xuất ảnh (hoặc 0 phút nếu Claude tải được từ kho mở) | Người dùng · trước khi gửi bản nháp 5 |
| 2 | Giọng đọc bản đăng | **Azure Speech gói F0** (cùng giọng, có giấy phép). Người dùng tự tạo tài khoản Azure và tự dán khoá vào file cấu hình `.env` (Claude không tạo tài khoản, không nhận khoá qua chat). Phương án khác: ElevenLabs 6 USD/tháng; thu giọng sale | 0đ/tháng ở mức hiện tại [ƯỚC TÍNH] | Người dùng · 28/10 |
| 3 | Nhạc | Quảng cáo: chọn nhạc trong Ads Manager; bài nhóm/TikTok: 1–2 bài Pixabay | 0đ | Người dùng · 28/10 |
| 4 | Logo SHB/VNVC/Manulife trên ảnh Sun City | **Làm mờ** | 0đ, Claude làm khoảng 20 phút | Người dùng · trước khi đăng Sun City |
| 5 | Lời Sun City thêm "chưa gồm phí quản lý"; xác nhận "1B" hay "243 Hùng Vương"; điều kiện "miễn phí 1 tháng" | Đồng ý thêm; người dùng xác nhận 2 dữ kiện | 0đ | Người dùng · trước khi dựng lại |
| 6 | Cho Claude dựng 8 kỹ thuật ở mục 5 (làm theo thứ tự; 1–3 trước, gửi nháp 5 để duyệt) | Đồng ý 1–6 ngay; 7–8 sau khi xem nháp 5 | Khoảng 1–1,5 ngày công Claude, 1 tác nhân [ƯỚC TÍNH] | Người dùng · 27/10 |
| 7 | Mua ảnh Pléiades 50 cm | **Chưa.** Xét lại ở cổng 09/11 nếu video vị trí ra khách | ~16 triệu đ + phí giấy phép [ƯỚC TÍNH] | Người dùng · 09/11 |

---

## Phụ lục A. Nguồn

**Đọc trọn (23):**
1. Google, Hướng dẫn dùng Maps/Earth/Street View: https://about.google/brand-resource-center/products-and-services/geo-guidelines/
2. Google Earth Studio, Câu hỏi thường gặp: https://www.google.com/earth/studio/faq/
3. Esri, Web Site and Service Terms of Use: https://www.esri.com/en-us/legal/terms/web-site-service
4. Esri, thông tin lớp World Imagery (giấy phép, ghi nguồn): https://www.arcgis.com/sharing/rest/content/items/10df2279f9684e4a9f6a7f08febac2a9?f=json
5. Copernicus Sentinel data licence: https://ads.atmosphere.copernicus.eu/licences/ec-sentinel
6. OSMF, chính sách dùng máy chủ ô bản đồ: https://operations.osmfoundation.org/policies/tiles/
7. Meta, quảng cáo Reels (thông số, số liệu 2 lần, 34,5%): https://www.facebook.com/business/ads/facebook-instagram-reels-ads
8. Meta Ads Guide, thông số video: https://www.facebook.com/business/ads-guide/update/video
9. TikTok, creative best practices: https://ads.tiktok.com/help/article/creative-best-practices?lang=en
10. edge-tts README: https://github.com/rany2/edge-tts
11. Microsoft, Code of Conduct for AI Services (bản 4.0, 01/5/2026): https://learn.microsoft.com/en-us/legal/ai-code-of-conduct
12. ElevenLabs, bảng giá: https://elevenlabs.io/pricing
13. Vbee, bản cập nhật 04/2025 (gói tuỳ chỉnh): https://help.vbee.vn/docs/thong-bao/ban-cap-nhat-thang-04-2025
14. FPT.AI Voice Maker: http://docs.fpt.ai/docs/en/speech/documentation/voice-maker/
15. Pixabay, Terms of Service (mục 5 Content License): https://pixabay.com/service/terms/
16. YouTube, dùng nhạc từ Audio Library: https://support.google.com/youtube/answer/3376882?hl=en
17. Meta, nhãn AI cho nội dung: https://www.meta.com/help/artificial-intelligence/1783222608822690/
18. LuatVietnam, 7 điểm mới Luật Quảng cáo sửa đổi 2025: https://luatvietnam.vn/linh-vuc-khac/diem-moi-cua-luat-quang-cao-sua-doi-2025-883-102813-article.html
19. LSVN, thông báo và gắn nhãn nội dung AI: https://lsvn.vn/thong-bao-va-gan-nhan-nhan-biet-noi-dung-do-ai-tao-ra-the-nao-a172678.html
20. Luật Dương Gia, Điều 8 Luật Quảng cáo (16 khoản): https://luatduonggia.vn/phap-luat/hanh-vi-cam-trong-hoat-dong-quang-cao/
21. Znews, môi giới BĐS đổ bộ TikTok: https://znews.vn/moi-gioi-bat-dong-san-do-bo-tiktok-san-khach-post1650295.html
22. AutoReel, 8 xu hướng video ngắn cho môi giới: https://www.autoreelapp.com/blog/8-short-form-video-trends-every-real-estate-agent-should-know
23. Mapbox, tài liệu bản đồ tĩnh: https://docs.mapbox.com/help/dive-deeper/static-maps.md

**Lướt (chỉ đọc kết quả tìm hoặc trang phụ, 12):**
- Trang giá Azure Speech (chỉ đọc được phần miễn phí): https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/
- Giá Azure khoảng 15–16 USD/1 triệu ký tự (nguồn thứ ba).
- Trang giá Google Cloud TTS (không tải được).
- EOX cloudless (giấy phép): https://cloudless.eox.at/documentation/license
- Bing print rights (đã chuyển về Azure Maps).
- MsEdgeTTS README (thay đổi 12/2025).
- Meta Sound Collection: trợ giúp Instagram và điều khoản cũ.
- Mixkit (nguồn thứ ba).
- Viettel AI, Zalo TTS.
- LandInfo, bảng giá ảnh vệ tinh 01/2026: https://landinfo.com/satellite-imagery-pricing/
- Meta, nhãn AI cho quảng cáo: https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/
- Brands Vietnam, 15 dạng video BĐS (lỗi 403).

**Kiểm trên máy [DỮ LIỆU]:**
- ffmpeg 7.1 có `loudnorm`, `sidechaincompress`, `ebur128`, `xfade`, `ass`, `zoompan`, `gblur`.
- edge-tts 7.3.1 có `boundary` WordBoundary/SentenceBoundary, mốc tính theo đơn vị 100 ns.
- Font Segoe có đủ các bản nghiêng và bộ ký hiệu.
- `tools/bay_ve_tinh.py` dùng điểm truy cập Esri World Imagery.
- `tools/video_dinh_vi.py`: vị trí tiêu đề, phụ đề, thẻ cuối nằm ngoài vùng an toàn.
