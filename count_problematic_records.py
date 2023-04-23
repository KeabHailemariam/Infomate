import pandas as pd
import sys

def main(file_path):
    column_names = ["sip", "timestamp", "request", "status", "bytes", "referrer", "user_agent"]
    problematic_count = 0
    corrupt_count = 0

    with open(file_path, "r") as f:
        lines = f.readlines()
    
    valid_lines = []

    for line in lines:
        fields = line.strip().split("|")
        if len(fields) != len(column_names):
            corrupt_count += 1
            continue
        if any(keyword in fields[-1] for keyword in ["bot", "crawl", "spider"]):
            problematic_count += 1
        valid_lines.append(line.strip())

    print(f"Corrupt records: {corrupt_count}")
    print(f"Problematic records: {problematic_count}")

    with open("cleaned_http_log.txt", "w") as f:
        f.write("\n".join(valid_lines))

if __name__ == "__main__":
    file_path = sys.argv[1]
    main(file_path)
