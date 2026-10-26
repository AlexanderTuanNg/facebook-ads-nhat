"""Kiểm nhãn video định vị: in khung chữ thật của từng nhãn ở các thời điểm f (0–1 của đoạn bay), báo nhãn đè nhau / chấm bị che.

  python tools/kiem_nhan_video.py assets/<du-an>/cau-hinh.json 0.3,0.5,0.7

Dùng trước khi dựng (tools/bay_ve_tinh.py) để chỉnh `hien`, `cao`, `lech`, `duoi`, `lech_ghim` trong cấu hình. Chỉ đọc, không ghi file.
"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bay_ve_tinh as B
from pathlib import Path
cfgp = Path(sys.argv[1]); fs = [float(x) for x in sys.argv[2].split(",")]
cfg = {"zoom_tu": 11.5, "zoom_den": 16.2, "ban_kinh_m": 220, "giay_bay": 8}; cfg.update(json.loads(cfgp.read_text(encoding="utf-8")))
T = cfg["giay_bay"]
html = B.lam_html(cfg)
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    pg = b.new_page(viewport={"width": B.W, "height": B.H})
    pg.on("console", lambda m: m.text.startswith("LOI_BAN_DO") and print(m.text))
    pg.set_content(html, wait_until="load"); pg.wait_for_function("window.SAN===true", timeout=120000)
    for f in fs:
        pg.evaluate("([t,T])=>setFrame(t,T)", [f * T, T])
        r = pg.evaluate("""()=>[...document.querySelectorAll('.moc')].map(e=>{const n=e.querySelector('.n').getBoundingClientRect();const i=e.querySelector('.in');
          const d=e.querySelector('.d').getBoundingClientRect();
          return {t:e.innerText.split(String.fromCharCode(10))[0],x0:Math.round(n.left),y0:Math.round(n.top),x1:Math.round(n.right),y1:Math.round(n.bottom),d:[Math.round(d.left),Math.round(d.top),Math.round(d.right),Math.round(d.bottom)],op:+(i.style.opacity||0)*(+(e.style.opacity||1))}})""")
        hien = [m for m in r if m["op"] > 0.05]
        print(f"f={f}:", " | ".join(f"{m['t']} [{m['x0']},{m['y0']}–{m['x1']},{m['y1']}] op{m['op']:.2f}" for m in hien))
        for i in range(len(hien)):
            for j in range(i + 1, len(hien)):
                a, c = hien[i], hien[j]
                if a["x0"] < c["x1"] and c["x0"] < a["x1"] and a["y0"] < c["y1"] and c["y0"] < a["y1"]:
                    print(f"   ĐÈ: {a['t']} × {c['t']}")
        for a in hien:
            for c in hien:
                if a is c: continue
                x0,y0,x1,y1=c["d"]
                if a["x0"]-3<x1 and x0<a["x1"]+3 and a["y0"]-3<y1 and y0<a["y1"]+3:
                    print(f"   CHẤM của {c['t']} chạm chữ {a['t']}")
    b.close()
