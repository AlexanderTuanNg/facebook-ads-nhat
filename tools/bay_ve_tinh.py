"""Đoạn mở đầu "bay 3D trên ảnh vệ tinh" (hướng A, người dùng 26/10: "dùng A & B xem ntn… test thử khi đăng lên fb").

MapLibre GL (mã nguồn mở) chạy trong Chromium không giao diện (Playwright), quay từng khung hình rồi mã hoá mp4 dọc.
Ảnh vệ tinh: Sentinel-2 (Copernicus, dùng thương mại được, `tools/sentinel_cat.py`) cắt thành ô 256 px ngay trong trình duyệt
(giao thức sen://) rồi phủ lên địa hình 3D — 26/10 người dùng chọn "giống Google Earth mà hợp pháp" (Google cấm dùng Earth cho video BĐS).
Không có "anh_ve_tinh" trong cấu hình → Esri World Imagery (cần giấy phép thương mại: chỉ xem nội bộ).
Địa hình: AWS Terrain Tiles (Terrarium, dữ liệu mở; "do_cao" = độ phóng đồi núi, "dia_hinh": false để tắt); nhãn mốc: OpenStreetMap.

  python tools/bay_ve_tinh.py <cau_hinh.json>      # dùng lat, lon, nhan_chinh, phu_de, moc, ban_kinh_m, giay_bay
Ra: <cùng thư mục cấu hình>/bay-ve-tinh.mp4 (720x1280, 30 hình/giây)
"""
import io
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FPS = 30
W, H = 720, 1280

HTML = r"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.css" rel="stylesheet">
<script src="https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js"></script>
<style>
html,body{margin:0;width:__W__px;height:__H__px;overflow:hidden;background:#000;font-family:'Segoe UI',Arial,sans-serif}
#map{position:absolute;inset:0}
.vig{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 55%,rgba(0,0,0,0) 45%,rgba(0,0,0,.55) 100%)}
.top{position:absolute;left:0;right:0;top:0;height:480px;background:linear-gradient(rgba(0,10,30,.85),rgba(0,10,30,0));pointer-events:none}
#title{position:absolute;top:286px;left:0;right:0;text-align:center;color:#f5c242;font-weight:800;font-size:52px;letter-spacing:1.5px;
 text-shadow:0 2px 12px rgba(0,0,0,.8);opacity:0}
#sub{position:absolute;top:352px;left:0;right:0;text-align:center;color:#fff;font-weight:600;font-size:27px;text-shadow:0 2px 6px #000;opacity:0}
.moc{display:flex;flex-direction:column;align-items:center}
.moc .n{background:rgba(255,255,255,.95);color:#0a1f44;font-weight:700;font-size:21px;padding:6px 14px;border-radius:10px;
 box-shadow:0 4px 14px rgba(0,0,0,.45);white-space:nowrap}  /* 26/10 bản sang: nền trắng chữ xanh đậm, bỏ viền phát sáng */
.moc .l{width:2px;height:46px;background:linear-gradient(rgba(255,255,255,.95),rgba(255,255,255,.25))}
.moc .d{width:12px;height:12px;border-radius:50%;background:#f5c242;border:2px solid #fff;box-shadow:0 0 8px rgba(0,0,0,.55)}
.moc .p{display:block;font-size:17px;color:#a8740a;font-weight:700;margin-top:1px}
.duong .n{background:rgba(10,31,68,.9);color:#fff;font-style:italic}
#fn{position:absolute;top:388px;left:0;right:0;text-align:center;color:#fff;font-size:15px;text-shadow:0 1px 3px #000;opacity:0}
.chinh .n{background:#f5c242;color:#0a1f44;font-size:25px;box-shadow:0 4px 18px rgba(0,0,0,.55)}
.chinh .l{width:3px;background:linear-gradient(#f5c242,rgba(245,194,66,.25));height:70px}
.chinh .d{width:14px;height:14px;background:#f5c242;border:3px solid #fff;box-shadow:0 0 10px rgba(0,0,0,.6)}
.duoi .l{background:linear-gradient(rgba(255,255,255,.25),rgba(255,255,255,.95))}
.chinh.duoi .l{background:linear-gradient(rgba(245,194,66,.25),#f5c242)}
#cr{position:absolute;right:8px;bottom:6px;color:#ddd;font-size:13px;text-shadow:0 1px 2px #000}
.maplibregl-ctrl-attrib{display:none}
</style></head><body>
<div id="map"></div><div class="vig"></div><div class="top"></div>
<div id="title"></div><div id="sub"></div><div id="fn"></div><div id="cr">Ảnh vệ tinh © Esri, Maxar, Earthstar Geographics · Địa danh © OpenStreetMap</div>
<script>
/*__SEN__*/
const C=__CFG__;
const map=new maplibregl.Map({container:'map',interactive:false,attributionControl:false,fadeDuration:0,
 style:{version:8,sources:{
  sat:{type:'raster',tiles:['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],tileSize:256,maxzoom:18},
  dem:{type:'raster-dem',tiles:['https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'],encoding:'terrarium',tileSize:256,maxzoom:14}},
  layers:[{id:'sat',type:'raster',source:'sat',paint:{'raster-saturation':0.15,'raster-contrast':0.12,'raster-brightness-max':0.92}}]},
 center:[C.lon,C.lat],zoom:C.zoom_tu,pitch:0,bearing:0,maxPitch:75,preserveDrawingBuffer:true});
map.on('error',e=>console.log('LOI_BAN_DO '+((e.error&&e.error.message)||e.type)));  /* 26/10: in lỗi nạp ảnh/thư viện để biết vì sao quá giờ */
function vong(lat,lon,r){const p=[];for(let i=0;i<=72;i++){const a=i/72*2*Math.PI;
 p.push([lon+r/111320/Math.cos(lat*Math.PI/180)*Math.cos(a),lat+r/110540*Math.sin(a)]);}return p;}
const mk=[];
map.on('load',()=>{
 if(C.dia_hinh!==false)map.setTerrain({source:'dem',exaggeration:C.do_cao||1.4});  /* 26/10: ảnh Sentinel đã cắt thành ô (sen://) → phủ lên đồi núi 3D được */
 try{map.setSky({'sky-color':'#071226','horizon-color':'#1b3354','fog-color':'#0a1830','sky-horizon-blend':0.6,'horizon-fog-blend':0.7,'fog-ground-blend':0.6,'atmosphere-blend':0.4});}catch(e){}  /* trời + sương xa cho mép ảnh mềm */
 const ring=C.vung&&C.vung.length?C.vung.map(p=>[p[1],p[0]]).concat([[C.vung[0][1],C.vung[0][0]]]):vong(C.lat,C.lon,C.ban_kinh_m);
 map.addSource('vung',{type:'geojson',data:{type:'Feature',geometry:{type:'Polygon',coordinates:[ring]}}});
 map.addLayer({id:'fill',type:'fill',source:'vung',paint:{'fill-color':'#ffcc00','fill-opacity':0}});
 map.addLayer({id:'glow',type:'line',source:'vung',paint:{'line-color':'#ffd84d','line-width':18,'line-blur':14,'line-opacity':0}});
 map.addLayer({id:'edge',type:'line',source:'vung',paint:{'line-color':'#fff6c2','line-width':3.5,'line-opacity':0}});
 (C.duong||[]).forEach((dg,k)=>{
   map.addSource('dg'+k,{type:'geojson',lineMetrics:true,data:{type:'Feature',geometry:{type:'MultiLineString',coordinates:dg.diem.map(l=>l.map(p=>[p[1],p[0]]))}}});
   map.addLayer({id:'dgw'+k,type:'line',source:'dg'+k,layout:{'line-cap':'round','line-join':'round'},paint:{'line-width':dg.rong_sang||18,'line-blur':12,'line-gradient':['step',['line-progress'],'rgba(0,0,0,0)',0.5,'rgba(0,0,0,0)']}});
   map.addLayer({id:'dgc'+k,type:'line',source:'dg'+k,layout:{'line-cap':'round','line-join':'round'},paint:{'line-width':dg.rong||5,'line-gradient':['step',['line-progress'],'rgba(0,0,0,0)',0.5,'rgba(0,0,0,0)']}});
 });
 const add=(m,cls)=>{const e=document.createElement('div');e.className='moc '+cls+(m.duoi?' duoi':'');  /* duoi: nhãn nằm DƯỚI chấm (26/10, gỡ nhãn chen nhau) */
   const nn=`<div class="n">${m.ten}${m.phu?`<span class="p">${m.phu}</span>`:""}</div>`,ll='<div class="l"></div>',dd='<div class="d"></div>';
   e.innerHTML=`<div class="in" style="display:flex;flex-direction:column;align-items:center;opacity:0">${m.duoi?dd+ll+nn:nn+ll+dd}</div>`;
   if(m.cao)e.querySelector('.l').style.height=m.cao+'px';  /* cột nhãn ngắn/dài để tách nhãn gần nhau */
   if(m.lech)e.querySelector('.n').style.transform='translateX('+m.lech+'px)';  /* lệch ngang khung chữ (px), chấm vẫn đúng vị trí */
   mk.push({e,m});new maplibregl.Marker({element:e,anchor:m.duoi?'top':'bottom'}).setLngLat([m.lon,m.lat]).addTo(map);};
 add({ten:C.ten_ghim||C.nhan_chinh,lat:C.lat,lon:C.lon,cao:C.ghim_cao,duoi:C.ghim_duoi},'chinh');
 (C.moc||[]).forEach(m=>add(m,''));
 (C.duong||[]).forEach(dg=>{if(dg.nhan)add(Object.assign({hien:dg.hien_nhan},dg.nhan),'duong');});
 document.getElementById('fn').textContent=C.chu_thich||'';
 const ti=document.getElementById('title');ti.textContent=C.nhan_chinh;ti.style.whiteSpace='nowrap';
 const doRong=(el)=>{const r=document.createRange();r.selectNodeContents(el);return r.getBoundingClientRect().width;};  /* đo đúng bề rộng chữ */
 let fs=52;while(doRong(ti)>__W__-70&&fs>28){fs-=2;ti.style.fontSize=fs+'px';}
 const su=document.getElementById('sub');su.textContent=C.phu_de||'';su.style.whiteSpace='nowrap';
 let f2=27;while(doRong(su)>__W__-70&&f2>16){f2-=1;su.style.fontSize=f2+'px';}
 const cho=()=>{if(map.isSourceLoaded('sat')&&map.loaded())window.SAN=true;else setTimeout(cho,250);};cho();});  /* chờ ảnh nền nạp xong mới quay */
const ease=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const cl=x=>Math.min(1,Math.max(0,x));
function camAt(f){const K=C.canh;let i=0;while(i<K.length-2&&f>K[i+1].t)i++;const a=K[i],b=K[i+1];
 const u=ease(cl((f-a.t)/(b.t-a.t))),L=(x,y)=>x+(y-x)*u,ca=a.center||[C.lat,C.lon],cb=b.center||[C.lat,C.lon];
 return {center:[L(ca[1],cb[1]),L(ca[0],cb[0])],zoom:L(a.zoom,b.zoom),pitch:L(a.pitch,b.pitch),bearing:L(a.bearing,b.bearing)};}
window.setFrame=(t,T)=>new Promise(res=>{
 const p=ease(Math.min(1,t/(T*0.7)));
 const f=t/T;
 if(C.canh)map.jumpTo(camAt(f));else map.jumpTo({center:[C.lon,C.lat],zoom:C.zoom_tu+(C.zoom_den-C.zoom_tu)*p,pitch:62*p,bearing:-25+60*(t/T)});
 const hv=C.hien_vung!=null?C.hien_vung:0.45;
 const a=cl((f-hv)/0.15), nh=0.5+0.5*Math.sin(t*6);
 (C.duong||[]).forEach((dg,k)=>{const h=dg.hien||[0.2,0.45];const pr=Math.max(0.001,cl((f-h[0])/(h[1]-h[0])));
   const mau=dg.mau||'0,229,255',ra=pr>=0.999?'rgba('+mau+',1)':'rgba(0,0,0,0)',g=(0.55+0.25*nh).toFixed(2);
   map.setPaintProperty('dgc'+k,'line-gradient',['step',['line-progress'],'rgba(255,255,255,'+(f>=h[0]?1:0)+')',pr,ra==='rgba(0,0,0,0)'?'rgba(0,0,0,0)':'rgba(255,255,255,1)']);
   map.setPaintProperty('dgw'+k,'line-gradient',['step',['line-progress'],'rgba('+mau+','+(f>=h[0]?g:0)+')',pr,pr>=0.999?'rgba('+mau+','+g+')':'rgba(0,0,0,0)']);});
 const fn=document.getElementById('fn');const fh=C.hien_chu_thich||[2,2];fn.style.opacity=cl((f-fh[0])/0.04)*cl((fh[1]-f)/0.04);
 map.setPaintProperty('fill','fill-opacity',0.08*a+0.05*a*nh);
 map.setPaintProperty('glow','line-opacity',0.95*a);map.setPaintProperty('edge','line-opacity',a);
 const ti=document.getElementById('title'),su=document.getElementById('sub'),k=Math.min(1,t/0.6);
 ti.style.opacity=k;ti.style.transform=`translateY(${-14*(1-k)}px)`;su.style.opacity=Math.min(1,Math.max(0,(t-0.4)/0.5));
 const hEnd=Math.max(0,...mk.slice(1).map(o=>o.m.hien?o.m.hien[1]:0));  /* 26/10: lúc các mốc đang hiện, nhãn dự án lệch sang phải lech_ghim px cho khỏi đè chấm mốc; hạ máy thì trượt về giữa */
 const lg=(C.lech_ghim||0)*ease(cl((hEnd-f+0.04)/0.08));
 mk.forEach((o,i)=>{const s=i===0?T*(C.hien_ghim!=null?C.hien_ghim:0.5):T*0.30+i*0.18;
   if(i===0&&C.lech_ghim)o.e.querySelector('.n').style.transform='translateX('+lg.toFixed(1)+'px)';
   let op=o.m.hien?cl((f-o.m.hien[0])/0.04)*cl((o.m.hien[1]-f)/0.04):cl((t-s)/0.3);
   const q=map.project([o.m.lon,o.m.lat]);const r=o.e.querySelector('.n').getBoundingClientRect();
   if(r.left<36||r.right>__W__-36||r.top<(C.nhan_tren||420)||r.bottom>845)op=0;  /* 26/10: trên 420 px là dải giá + tiêu đề */  /* khung chữ thật ra ngoài vùng an toàn → ẩn */  /* ngoài vùng an toàn → ẩn, khỏi bị cắt chữ */
   o.e.querySelector('.in').style.opacity=op;});
 map.once('idle',()=>res(true));map.triggerRepaint();
 setTimeout(()=>res(false),6000);});
</script></body></html>"""


def ffmpeg() -> str:
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


SEN_JS = r"""/* 26/10: ảnh Sentinel-2 cắt thành ô 256 px ngay trong trình duyệt (sen://z/x/y) để phủ lên địa hình 3D;
   SEN_AFF = đa thức bậc 2 (kinh độ, vĩ độ) → (cột, hàng) điểm ảnh, Python khớp sẵn theo lưới UTM */
const SEN_AFF=__AFF__;
const senReady=(async()=>{const b=await(await fetch('data:image/jpeg;base64,__B64__')).blob();return await createImageBitmap(b);})();
maplibregl.addProtocol('sen',async(p)=>{const img=await senReady;const m=p.url.match(/(\d+)\/(\d+)\/(\d+)$/);const z=+m[1],x=+m[2],y=+m[3],n=2**z;
 const P=(X,Y)=>{const lo=X/n*360-180,la=Math.atan(Math.sinh(Math.PI*(1-2*Y/n)))*180/Math.PI,A=SEN_AFF,u=lo-A.lo0,v=la-A.la0,f=[1,u,v,u*u,u*v,v*v];
  let px=0,py=0;for(let i=0;i<6;i++){px+=A.cx[i]*f[i];py+=A.cy[i]*f[i];}return [px,py];};
 const a=P(x,y),b=P(x+1,y),c=P(x,y+1),S=256,ux=(b[0]-a[0])/S,uy=(b[1]-a[1])/S,vx=(c[0]-a[0])/S,vy=(c[1]-a[1])/S,dt=ux*vy-vx*uy;
 const i11=vy/dt,i12=-vx/dt,i21=-uy/dt,i22=ux/dt,cv=new OffscreenCanvas(S,S),g=cv.getContext('2d');
 g.imageSmoothingEnabled=true;g.imageSmoothingQuality='high';g.setTransform(i11,i21,i12,i22,-(i11*a[0]+i12*a[1]),-(i21*a[0]+i22*a[1]));g.drawImage(img,0,0);
 return {data:await(await cv.convertToBlob({type:'image/png'})).arrayBuffer()};});
"""


def he_so_anh(avt):
    """Đa thức bậc 2 (kinh độ, vĩ độ) → (cột, hàng) điểm ảnh của ảnh Sentinel đã cắt (lưới UTM 10 m).
    Khớp bình phương tối thiểu trên lưới 21×21 điểm tính đúng bằng công thức UTM (affine lệch tới 2,4 điểm ảnh ở mép ảnh 30×39 km
    → bậc 2); trả ({lo0, la0, cx, cy}, sai lệch lớn nhất theo điểm ảnh)."""
    import re
    sys.path.insert(0, str(ROOT / "tools"))
    from sentinel_cat import latlon_utm, utm_latlon
    zone = int(re.search(r"_(\d{2})[A-Z]{3}_", avt["canh"]).group(1))
    w, h = Image.open(ROOT / avt["file"]).size
    e0, n0 = latlon_utm(avt["goc"][0][1], avt["goc"][0][0], zone)
    mau = []
    for i in range(21):
        for j in range(21):
            px, py = w * i / 20, h * j / 20
            la, lo = utm_latlon(e0 + 10 * px, n0 - 10 * py, zone)
            mau.append((lo, la, px, py))
    lo0, la0 = sum(m[0] for m in mau) / len(mau), sum(m[1] for m in mau) / len(mau)

    N = 6
    dac = lambda lo, la: (1.0, lo - lo0, la - la0, (lo - lo0) ** 2, (lo - lo0) * (la - la0), (la - la0) ** 2)

    def khop(k):  # hệ 6×6 (đã trừ trung bình cho đỡ sai số), khử Gauss
        A = [[0.0] * N for _ in range(N)]
        bb = [0.0] * N
        for m in mau:
            v = dac(m[0], m[1])
            for r in range(N):
                bb[r] += v[r] * m[k]
                for c in range(N):
                    A[r][c] += v[r] * v[c]
        for c in range(N):
            p = max(range(c, N), key=lambda r: abs(A[r][c]))
            A[c], A[p], bb[c], bb[p] = A[p], A[c], bb[p], bb[c]
            for r in range(c + 1, N):
                f = A[r][c] / A[c][c]
                for cc in range(c, N):
                    A[r][cc] -= f * A[c][cc]
                bb[r] -= f * bb[c]
        x = [0.0] * N
        for r in range(N - 1, -1, -1):
            x[r] = (bb[r] - sum(A[r][cc] * x[cc] for cc in range(r + 1, N))) / A[r][r]
        return x
    cx, cy = khop(2), khop(3)
    tinh = lambda h, m: sum(a * b for a, b in zip(h, dac(m[0], m[1])))
    sai = max(abs(tinh(cx, m) - m[2]) + abs(tinh(cy, m) - m[3]) for m in mau)
    return {"lo0": lo0, "la0": la0, "cx": cx, "cy": cy}, sai


def lam_html(cfg) -> str:
    """HTML hoàn chỉnh của đoạn bay (dùng chung cho main và các công cụ đo nhãn)."""
    html = HTML.replace("__W__", str(W)).replace("__H__", str(H)).replace(
        "__CFG__", json.dumps({k: v for k, v in cfg.items() if not k.startswith("_")}, ensure_ascii=False))
    tt = cfg.get("tieu_de_top")  # 26/10: dải đỉnh có số điện thoại cao hơn → dời tiêu đề, phụ đề, chú thích, nền tối xuống
    if tt:
        for cu, moi in (("#title{position:absolute;top:286px", f"#title{{position:absolute;top:{tt}px"),
                        ("#sub{position:absolute;top:352px", f"#sub{{position:absolute;top:{tt + 66}px"),
                        ("#fn{position:absolute;top:388px", f"#fn{{position:absolute;top:{tt + 102}px"),
                        ("height:480px;background:linear-gradient", f"height:{tt + 194}px;background:linear-gradient")):
            assert cu in html, cu
            html = html.replace(cu, moi)
    avt = cfg.get("anh_ve_tinh")
    if not avt:
        return html.replace("/*__SEN__*/", "")
    import base64
    aff, sai = he_so_anh(avt)
    assert sai < 0.5, f"khớp toạ độ ảnh Sentinel lệch {sai:.2f} điểm ảnh"
    lo, la = [p[0] for p in avt["goc"]], [p[1] for p in avt["goc"]]
    cu = "sat:{type:'raster',tiles:['https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],tileSize:256,maxzoom:18}"
    mau_cu = "paint:{'raster-saturation':0.15,'raster-contrast':0.12,'raster-brightness-max':0.92}"
    nguon_cu = "Ảnh vệ tinh © Esri, Maxar, Earthstar Geographics · Địa danh © OpenStreetMap"
    assert cu in html and mau_cu in html and nguon_cu in html
    html = html.replace(cu, "sat:{type:'raster',tiles:['sen://{z}/{x}/{y}'],tileSize:256,maxzoom:14,bounds:"
                        + json.dumps([min(lo), min(la), max(lo), max(la)]) + "}")
    html = html.replace(mau_cu, "paint:" + json.dumps(cfg.get("raster_paint") or {"raster-saturation": 0, "raster-contrast": 0.05}))  # SC 26/10: tông tối cho sang
    html = html.replace(nguon_cu, avt["nguon"] + " · Độ cao: SRTM (NASA), AWS Terrain Tiles · Địa danh © OpenStreetMap")
    raw = (ROOT / avt["file"]).read_bytes()
    if cfg.get("anh_net"):  # 26/10 người dùng "suncity mờ quá": làm nét nhẹ ảnh 10 m trước khi cắt ô
        from PIL import ImageFilter
        nt, buf = cfg["anh_net"], io.BytesIO()
        Image.open(io.BytesIO(raw)).convert("RGB").filter(
            ImageFilter.UnsharpMask(radius=nt.get("r", 1.4), percent=nt.get("p", 90), threshold=2)).save(buf, "JPEG", quality=92)
        raw = buf.getvalue()
    b64 = base64.b64encode(raw).decode()
    return html.replace("/*__SEN__*/", SEN_JS.replace("__AFF__", json.dumps(aff)).replace("__B64__", b64))


def main():
    cfg_path = Path(sys.argv[1])
    cfg = {"zoom_tu": 11.5, "zoom_den": 16.2, "ban_kinh_m": 220, "giay_bay": 8}
    cfg.update(json.loads(cfg_path.read_text(encoding="utf-8")))
    T = cfg["giay_bay"]
    html = lam_html(cfg)
    out = cfg_path.parent / "bay-ve-tinh.mp4"
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
        pg = b.new_page(viewport={"width": W, "height": H})
        pg.on("console", lambda m: m.text.startswith("LOI_BAN_DO") and print(m.text, flush=True))
        pg.on("pageerror", lambda e: print("LỖI TRANG:", e, flush=True))
        for lan in range(3):  # 26/10: lần dựng GH đầu quá 60 giây chờ (chạy lại chỉ 6 giây) → thử lại tối đa 3 lần, in lỗi
            try:
                pg.set_content(html, wait_until="load")
                pg.wait_for_function("window.SAN===true", timeout=120000)
                break
            except Exception as e:
                print(f"chờ ảnh nền lần {lan + 1} lỗi: {str(e)[:200]}", flush=True)
                if lan == 2:
                    raise
        p = subprocess.Popen([ffmpeg(), "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                              "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", str(out)], stdin=subprocess.PIPE)
        thieu = 0
        for i in range(int(T * FPS)):
            ok = pg.evaluate("([t,T])=>setFrame(t,T)", [i / FPS, T])
            thieu += 0 if ok else 1
            im = Image.open(io.BytesIO(pg.screenshot(type="png"))).convert("RGB")
            p.stdin.write(im.tobytes())
            if i % 30 == 0:
                print(f"khung {i}/{int(T * FPS)}", flush=True)
        p.stdin.close()
        p.wait()
        b.close()
    print("XONG:", out, f"{T} giây", "khung chưa tải xong ảnh:", thieu)


if __name__ == "__main__":
    main()
