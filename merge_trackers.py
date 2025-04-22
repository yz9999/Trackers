import requests
import os

sources = [
    "https://cf.trackerslist.com/all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/Tunglies/TrackersList/main/all.txt"
]

def fetch_trackers(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return set(r.text.splitlines())
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
    return set()

def main():
    all_trackers = set()
    
    for url in sources:
        trackers = fetch_trackers(url)
        all_trackers.update(trackers)
    
    # 排序并过滤空行
    sorted_trackers = sorted([t for t in all_trackers if t.strip()])
    
    with open("combined.txt", "w") as f:
        f.write("\n".join(sorted_trackers))
    
    print(f"合并完成，共 {len(sorted_trackers)} 个唯一 Tracker")

if __name__ == "__main__":
    main()
