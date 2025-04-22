import requests

sources = [
    "https://cf.trackerslist.com/all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/Tunglies/TrackersList/main/all.txt"
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
    
    # 严格过滤有效协议
    valid_protocols = ('udp://', 'http://', 'https://')
    filtered_trackers = sorted(
        [t for t in all_trackers 
         if t.startswith(valid_protocols) and '#' not in t]
    )
    
    with open("Trackers.txt", "w") as f:
        f.write("\n".join(filtered_trackers))

if __name__ == "__main__":
    main()
