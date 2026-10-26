"""Xếp lịch lô bài group (nhánh B) và tạo dòng posts status 'planned' để copywriter viết.

  python tools/lap_lich_bai.py --tu 2026-10-06 --so-ngay 3            # chạy khô: in bảng lịch
  python tools/lap_lich_bai.py --tu 2026-10-06 --so-ngay 3 --ghi      # ghi vào DB (status planned)

Luật (settings.json + thẻ luật): N bài/ngày (limits.profile_group_posts_per_day), khung ~06:30–22:30 cách ≥ 25 phút,
group 'joined' đã hết làm quen, cùng group cách ≥ 3 ngày + 1 giờ đệm, không 2 bài liền nhau cùng vùng,
ưu tiên group CHƯA từng đăng (người dùng 28/09: nhóm cũ không ra lead), nhóm ƯU TIÊN THẤP và nhóm lạc đề xếp cuối.
Góc bài xoay vòng; bài từ 19:00 dùng góc 5 (tối ra quảng trường). Mã lead duy nhất toàn bảng posts.
"""
import argparse
import json
import random
import re
from datetime import datetime, timedelta

from common import ROOT, connect

LOAI = {286}  # 286 Hội Mua Bán Keo Hom (cây giống). 23/10 tối người dùng: "đăng các nhóm khác… hội này hội kia" → bỏ chặn 128 Diều Sáo, 139 Nhã Nam reading club (thử, đo tỉ lệ duyệt/gỡ)
GOC_NGAY = [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 4]
# 14/10: người dùng muốn tiếp cận công nhân KCN, người Yên Thế đi xuất khẩu lao động, người cao tuổi → thêm 3 vùng "đối tượng"
# (xét TRƯỚC vùng địa lý) + Nhã Nam/Cao Thượng/Chợ Mọc vào tan-yen; --vung lọc chỉ xếp các vùng chọn.
VUNG = [("kcn", r"kcn|khu công nghiệp|công nhân|quang châu|vân trung|đình trám|song khê|hòa phú|yên lư|việc làm|tuyển dụng"),
        ("xkld", r"nhật bản|tại nhật|hàn quốc|đài loan|xuất khẩu lao động|xklđ|đồng hương"),
        ("cao-tuoi", r"cao tuổi|cựu chiến binh|hưu trí|người già"),
        ("huu-lung", r"hữu lũng|lạng sơn|mẹt|bắc lệ"), ("bo-ha", r"bố hạ"), ("tan-yen", r"tân yên|nhã nam|cao thượng|chợ mọc"),
        ("que-vo", r"quế võ|từ sơn|phương liễu"), ("yen-the", r"yên thế|mỏ trạng|cầu gồ|đồng kỳ|xuân lương|tam tiến|đồng lạc"),
        ("bac-giang", r"bắc giang|bắc ninh|chợ tốt")]
TIEN_TO = {"huu-lung": "HL", "bo-ha": "BH", "tan-yen": "TY", "que-vo": "QV", "yen-the": "YT", "bac-giang": "BG",
           "kcn": "KC", "xkld": "XK", "cao-tuoi": "CT"}


BDS = re.compile(r"bất động sản|bđs|bds|nhà đất|mua bán|chợ|rao vặt|mua sắm|mua và bán|nhà trọ|phòng trọ|cho thuê", re.I)


def vung(ten: str) -> str:
    t = ten.lower()
    for v, mau in VUNG:
        if re.search(mau, t):
            return v
    return "khac"


def khung_gio(ngay: datetime, so: int) -> list[datetime]:
    """so mốc trong 06:30–22:30, đều nhau + lệch ngẫu nhiên, cách nhau ≥ 25 phút."""
    dau, cuoi = ngay.replace(hour=6, minute=30), ngay.replace(hour=22, minute=30)
    buoc = (cuoi - dau) / so
    ds, truoc = [], None
    for i in range(so):
        t = dau + buoc * i + timedelta(minutes=random.randint(0, max(1, int(buoc.total_seconds() // 60) - 25)))
        if truoc and (t - truoc) < timedelta(minutes=25):
            t = truoc + timedelta(minutes=25)
        ds.append(t.replace(second=0, microsecond=0))
        truoc = t
    return ds


def so_ma_lon_nhat(con) -> dict:
    lon = {}
    for (a,) in con.execute("SELECT angle FROM posts WHERE angle LIKE '[mã %'"):
        m = re.match(r"\[mã ([A-Z]+)(\d+)\]", a or "")
        if m:
            lon[m.group(1)] = max(lon.get(m.group(1), 0), int(m.group(2)))
    return lon


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tu", required=True, help="YYYY-MM-DD")
    ap.add_argument("--so-ngay", type=int, default=3)
    ap.add_argument("--ghi", action="store_true")
    ap.add_argument("--seed", type=int, default=6)
    ap.add_argument("--vung", help="chỉ xếp các vùng này, vd yen-the,bo-ha,tan-yen,kcn,xkld,cao-tuoi")
    # 23/10 người dùng: "cứ giữ ở 50% bđs và 50% các nhóm còn lại" → mỗi ngày xen kẽ nhóm BĐS/chợ và nhóm cộng đồng/hội/KCN
    ap.add_argument("--ti-le-bds", type=float, default=0.5, help="tỉ lệ bài vào nhóm BĐS/chợ mỗi ngày (0–1)")
    a = ap.parse_args()
    random.seed(a.seed)
    st = json.loads((ROOT / "config" / "settings.json").read_text(encoding="utf-8"))
    so = st["limits"]["profile_group_posts_per_day"]
    ngay_cach = st["limits"]["same_group_min_days"]
    con = connect()
    nhom = [dict(r) for r in con.execute(
        "SELECT g.id, g.name, g.warmup_until, g.notes, g.removed_count, (SELECT max(scheduled_at) FROM posts p WHERE p.channel='group' "
        "AND p.target_id=g.id AND p.status NOT IN ('skipped','failed','removed')) AS cuoi, "
        "(SELECT count(*) FROM posts p WHERE p.target_id=g.id AND p.status IN ('published','pending_approval')) AS da_dang "
        "FROM groups g WHERE g.status='joined'")]
    for g in nhom:
        g["vung"] = vung(g["name"])
        g["bds"] = bool(BDS.search(g["name"] or ""))
        g["thap"] = g["id"] in LOAI or "ƯU TIÊN THẤP" in (g["notes"] or "")
        g["cuoi"] = datetime.strptime(g["cuoi"][:16], "%Y-%m-%d %H:%M") if g["cuoi"] else None
    if a.vung:
        chon = {v.strip() for v in a.vung.split(",") if v.strip()}
        nhom = [g for g in nhom if g["vung"] in chon]
    lon = so_ma_lon_nhat(con)
    bang, chi_so_goc = [], 0
    d0 = datetime.strptime(a.tu, "%Y-%m-%d")
    for n in range(a.so_ngay):
        ngay = d0 + timedelta(days=n)
        vung_truoc = None
        da_bds = da_tong = 0
        for t in khung_gio(ngay, so):
            def du(g, t=t):
                if g["id"] in LOAI or (g["removed_count"] or 0) > 0:  # nhóm từng gỡ bài mình → không đăng lại
                    return False
                if g["warmup_until"] and g["warmup_until"] > t.strftime("%Y-%m-%d %H:%M:%S"):
                    return False
                return not g["cuoi"] or t - g["cuoi"] >= timedelta(days=ngay_cach, hours=1)
            ung = [g for g in nhom if du(g)]
            if not ung:
                print(f"THIẾU group cho {t:%d/%m %H:%M}")
                continue
            can_bds = da_bds < round(a.ti_le_bds * (da_tong + 1))  # còn thiếu bài BĐS so với tỉ lệ → ưu tiên nhóm BĐS
            ung.sort(key=lambda g: (g["thap"], g["bds"] != can_bds, g["vung"] == vung_truoc, g["da_dang"], g["cuoi"] or datetime.min, g["id"]))
            g = ung[0]
            da_tong += 1
            da_bds += g["bds"]
            g["cuoi"], vung_truoc = t, g["vung"]
            goc = 5 if t.hour >= 19 else GOC_NGAY[chi_so_goc % len(GOC_NGAY)]
            if t.hour < 19:
                chi_so_goc += 1
            tt = TIEN_TO.get(g["vung"], "BG")
            lon[tt] = lon.get(tt, 0) + 1
            bang.append({"t": t, "g": g, "goc": goc, "ma": f"{tt}{lon[tt]}"})
    for b in bang:
        print(f"{b['t']:%d/%m %H:%M} g{b['g']['id']:<4} {b['g']['vung']:<9} góc {b['goc']:<2} {b['ma']:<5} "
              f"{'(mới)' if not b['g']['da_dang'] else ''} {b['g']['name'][:45]}")
    print(f"Tổng {len(bang)} bài, {len({b['g']['id'] for b in bang})} group khác nhau")
    if not a.ghi:
        print("(chạy khô — thêm --ghi để tạo bài planned)")
        return
    ids = []
    for b in bang:
        slug = f"{b['t']:%Y%m%d}-g{b['g']['id']}-v6-{b['ma'].lower()}"
        cur = con.execute(
            "INSERT INTO posts (slug, pillar, channel, target_id, account_id, arm, angle, cta_type, status, scheduled_at) "
            "VALUES (?, 'du-an', 'group', ?, 2, 'B', ?, 'inbox', 'planned', ?)",
            (slug, b["g"]["id"], f"[mã {b['ma']}] [góc {b['goc']}] v6: {b['g']['name'][:60]}", b["t"].strftime("%Y-%m-%d %H:%M:00")))
        ids.append(cur.lastrowid)
    con.commit()
    print("ĐÃ GHI post id:", ",".join(map(str, ids)))


if __name__ == "__main__":
    main()
