import requests
import os
from datetime import datetime

sources = [
    "https://cf.trackerslist.com/all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/Tunglies/TrackersList/main/all.txt"
]

def fetch_trackers(url):
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return set(r.text.strip().splitlines())
    except Exception as e:
        print(f"❌ 错误 [{url}]: {str(e)}")
        return set()

def main():
    total_count = 0
    all_trackers = set()
    
    print("🚀 开始合并Tracker列表...")
    for index, url in enumerate(sources, 1):
        print(f"🔍 正在处理源站 {index}/{len(sources)}: {url}")
        trackers = fetch_trackers(url)
        all_trackers.update(trackers)
        print(f"✅ 成功获取 {len(trackers)} 条Tracker")
        total_count += len(trackers)
    
    # 添加时间戳标记
    timestamp = datetime.utcnow().strftime("# 最后更新时间: %Y-%m-%d %H:%M:%S UTC\n")
    
    # 过滤和排序
    sorted_trackers = sorted([t for t in all_trackers if t.strip() and t.startswith(('udp://', 'http://', 'https://'))])
    
    with open("combined.txt", "w") as f:
        f.write(timestamp)
        f.write("\n".join(sorted_trackers))
    
    print(f"\n🎉 合并完成！")
    print(f"▸ 总获取条目: {total_count}")
    print(f"▸ 去重后数量: {len(sorted_trackers)}")
    print(f"▸ 文件大小: {os.path.getsize('combined.txt')} bytes")

if __name__ == "__main__":
    main()
