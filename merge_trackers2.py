import requests

sources = [
    "https://cf.trackerslist.com/all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
]

def fetch_trackers(url):
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return set(line.strip() for line in r.text.splitlines() if line.strip())
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return set()

def main():
    all_trackers = set()
    
    for url in sources:
        trackers = fetch_trackers(url)
        all_trackers.update(trackers)
    
    # 过滤有效条目
    valid_protocols = ('udp://', 'http://', 'https://')
    filtered_trackers = sorted(
        [t for t in all_trackers 
         if t.startswith(valid_protocols) 
         and '#' not in t 
         and len(t) > 10]
    )
    
    # 生成单行逗号分隔格式
    tracker_line = ",".join(filtered_trackers)
    
    with open("all_aria2", "w") as f:
        f.write(tracker_line)  # 注意这里没有换行符

if __name__ == "__main__":
    main()
