"""Lọc + chấm điểm kết quả `tools/tim_nhom.py` → thêm nhóm ứng viên (status `candidate`) cho `tools/vao_nhom.py` vào dần.

  python tools/loc_nhom.py data/tim_nhom_*.jsonl            # in bảng, không ghi
  python tools/loc_nhom.py data/tim_nhom_*.jsonl --ghi      # ghi ứng viên vào DB (bỏ nhóm đã có)

Điểm = địa danh trong tên (quanh Yên Thế/Tân Yên cao nhất) + loại nhóm (nhà đất > chợ/mua bán > cộng đồng) + cỡ nhóm.
Loại: nhóm không có địa danh vùng đích, nhóm việc làm/thuê trọ/hẹn hò/phim…, nhóm < 1.000 thành viên.
"""
import argparse
import glob
import json
import re

from common import connect, now_str

VUNG_1 = ["yên thế", "bố hạ", "cầu gồ", "phồn xương", "đồng kỳ", "tam tiến", "xuân lương", "canh nậu", "đồng vương", "đồng tâm",
          "hồng kỳ", "tân hiệp", "tam hiệp", "an thượng", "hương vĩ", "đồng hưu", "tân sỏi", "đông sơn", "tiến thắng", "đồng lạc", "mỏ trạng"]
VUNG_2 = ["tân yên", "nhã nam", "cao thượng", "ngọc thiện", "việt lập", "liên chung", "phúc hòa", "phúc hoà", "quế nham", "song vân",
          "ngọc châu", "lam cốt", "cao xá", "đại hóa", "đại hoá", "hợp đức", "lan giới", "an dương", "quang tiến", "ngọc vân", "việt ngọc",
          "liên sơn", "ngọc lý", "lạng giang", "kép", "vôi", "lục nam", "đồi ngô", "việt yên", "bích động", "nếnh", "hiệp hòa", "hiệp hoà"]
# Người dùng 28/09 chiều: "mấy group đợt rồi đăng không có lead… vào các group khác đi, ở các phường xã bên cạnh hoặc ở
# lạng sơn hữu lũng" → thêm vùng giáp Yên Thế: Hữu Lũng (Lạng Sơn, giáp phía bắc) ngang VUNG_1; Lạng Sơn chung, Chi Lăng và
# các huyện Thái Nguyên giáp phía tây (Võ Nhai, Đồng Hỷ, Phú Bình) ngang VUNG_2.
VUNG_3 = ["hữu lũng", "cai kinh", "hữu liên", "vân nham", "thiện tân", "thiện kỵ", "mẹt"]
# "lạng sơn" để cuối: nhóm chỉ có "Lạng Sơn" chung (phần lớn ở TP Lạng Sơn, ~100 km) điểm thấp hơn nhóm có huyện giáp
VUNG_4 = ["chi lăng", "đồng mỏ", "võ nhai", "la hiên", "đình cả", "đồng hỷ", "trại cau", "chùa hang", "phú bình", "lạng sơn"]
DE_TRUNG = {"tam hiệp", "tân hiệp", "an thượng", "an dương", "đồng tâm", "hồng kỳ", "đông sơn", "tiến thắng", "hương vĩ",
            "song vân", "ngọc châu", "lam cốt", "cao xá", "lan giới", "hợp đức", "quang tiến", "đại hóa", "đại hoá", "phúc hòa",
            "phúc hoà", "liên sơn", "ngọc vân", "việt ngọc", "ngọc lý", "canh nậu", "đồng lạc", "tam tiến", "kép", "vôi", "đồng vương",
            "thiện tân", "thiện kỵ", "mẹt", "chi lăng", "đồng mỏ", "đình cả", "chùa hang"}
PHAN_BIET = r"yên thế|tân yên|bắc giang|bắc ninh|nhã nam|cao thượng|bố hạ|cầu gồ|hữu lũng|lạng sơn|thái nguyên|võ nhai|đồng hỷ|phú bình"
LOAI_BO = (r"việc làm|tuyển|thuê trọ|phòng trọ|hẹn hò|kết bạn|phim|game|bóng đá|xe khách|taxi|học|thi |giáo viên|mẹ bỉm|shop|"
           r"thời trang|mỹ phẩm|vương quốc|vương giả|gunpow|"
           # trùng tên địa danh ở tỉnh khác (28/09: "Chợ Canh Nậu - Thạch Thất" là Hà Nội)
           r"thạch thất|hà nội|yên bái|lục yên|hải dương|hải phòng|thái bình|nghệ an|thanh hóa|thanh hoá|quảng ninh|"
           r"tam thanh|tam hải|tam hoà|tam hòa|đất biển|dị nậu|tây phương|hương ngải|"
           # 28/09 chiều (đợt vùng giáp): "Đồng Phú Bình Phước" khớp nhầm "phú bình"; nhóm du lịch/trường/CLB/xe không phải khách mua đất
           r"bình phước|đồng phú|review|du lịch|homestay|thpt|thcs|clb|câu lạc bộ|diều|xe máy|ô tô")
# Tên có Thái Nguyên/Lạng Sơn chỉ nhận khi khớp địa danh VUNG_3/VUNG_4 (vd "Phúc Hòa – Thái Nguyên" vẫn là trùng tên → loại)
TINH_GIAP = r"thái nguyên|lạng sơn"


def diem(g: dict) -> tuple[int, str]:
    ten = g["ten"].lower()
    if re.search(LOAI_BO, ten):
        return 0, "loại (chủ đề không hợp)"
    v1 = next((v for v in VUNG_1 if v in ten), None)
    v2 = next((v for v in VUNG_2 if v in ten), None)
    v3 = next((v for v in VUNG_3 if v in ten), None)
    v4 = next((v for v in VUNG_4 if v in ten), None)
    if not (v1 or v2 or v3 or v4):
        return 0, "loại (không có địa danh vùng đích)"
    if not (v3 or v4) and re.search(TINH_GIAP, ten):
        return 0, "loại (tên xã trùng ở Thái Nguyên/Lạng Sơn, không phải vùng giáp Yên Thế)"
    # 28/09 đợt 2: tên xã cũ hay trùng nơi khác (Tam Hiệp, Tân Hiệp — Hà Nội, Kiên Giang…) → phải có chữ phân biệt vùng
    if (v1 or v3 or v2 or v4) in DE_TRUNG and not re.search(PHAN_BIET, ten):
        return 0, "loại (tên xã trùng nơi khác, tên nhóm không có chữ phân biệt vùng)"
    tv = g.get("thanh_vien") or 0
    if tv and tv < 1000:
        return 0, "loại (< 1.000 thành viên)"
    d = 5 if (v1 or v3) else 2 if v4 == "lạng sơn" and not (v2 or v3) else 3
    d += 3 if re.search(r"nhà đất|bất động sản|bđs|đất nền|mua bán đất", ten) else 2 if re.search(r"chợ|mua bán|rao vặt|mua và bán", ten) else 1
    d += 2 if tv >= 20000 else 1 if tv >= 5000 else 0
    d -= 0 if g.get("cong_khai") else 1
    return min(d, 10), (v1 or v3 or v2 or v4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--ghi", action="store_true")
    a = ap.parse_args()
    ds = {}
    for pat in a.files:
        for f in glob.glob(pat):
            for dong in open(f, encoding="utf-8"):
                g = json.loads(dong)
                ds.setdefault(g["url"], g)
    con = connect()
    co = {r[0].rstrip("/") for r in con.execute("SELECT url FROM groups")}
    chon = []
    for g in ds.values():
        d, ly_do = diem(g)
        if d > 0 and g["url"] not in co:
            chon.append((d, g, ly_do))
    chon.sort(key=lambda x: (-x[0], -(x[1].get("thanh_vien") or 0)))
    for d, g, v in chon:
        print(f"{d:>2} | {g['ten'][:55]:<55} | {g.get('thanh_vien') or '?':>7} tv | {'công khai' if g.get('cong_khai') else 'riêng tư '} | {v} | {g['url']}")
    print(f"→ {len(chon)} nhóm ứng viên mới (trên {len(ds)} kết quả tìm)")
    if a.ghi:
        for d, g, v in chon:
            vung = "vùng giáp Yên Thế (Hữu Lũng/Lạng Sơn/Thái Nguyên)" if v in VUNG_3 + VUNG_4 else "tìm quanh Yên Thế"
            con.execute("INSERT INTO groups(url, name, members, topic, quality_score, status, notes) VALUES (?,?,?,?,?,'candidate',?)",
                        (g["url"], g["ten"], g.get("thanh_vien"), vung, d,
                         f"tim_nhom {now_str()[:10]} (từ khoá '{g['tu_khoa']}', địa danh '{v}') | {g.get('mo_ta', '')[:150]}"))
        con.commit()
        print("đã ghi", len(chon), "ứng viên")


if __name__ == "__main__":
    main()
