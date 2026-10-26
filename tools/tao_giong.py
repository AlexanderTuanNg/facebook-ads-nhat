"""Tạo lời đọc bằng edge-tts (giọng máy Microsoft, bản NHÁP — bản quảng cáo nên dùng Azure Speech có giấy phép) + mốc từng câu.

  python tools/tao_giong.py "<lời đọc>" vi-VN-HoaiMyNeural "+8%" assets/<du-an>/loi-doc.mp3

Ra: <out>.mp3 và <out>.json [{"tu": giây, "den": giây, "chu": câu}] để video_dinh_vi.py canh nhãn/phụ đề theo câu.
Kiểm câu chữ trước: python tools/db.py lint --text "<lời đọc>". Video dùng giọng AI phải ghi nhãn ở bài đăng.
"""
import asyncio, json, sys
import edge_tts
text, voice, rate, out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
async def chay():
    c = edge_tts.Communicate(text, voice, rate=rate, boundary="SentenceBoundary")
    sub = []
    with open(out, "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio":
                f.write(ch["data"])
            elif ch["type"] == "SentenceBoundary":
                sub.append({"tu": round(ch["offset"] / 1e7, 2), "den": round((ch["offset"] + ch["duration"]) / 1e7, 2), "chu": ch["text"]})
    json.dump(sub, open(out.rsplit(".", 1)[0] + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for s in sub:
        print(f"{s['tu']:5.2f}-{s['den']:5.2f}  {s['chu']}")
asyncio.run(chay())
