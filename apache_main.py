import re
from collections import Counter

def analyze_log_file(log_file_path):
    with open(log_file_path, 'r') as log_file:
        log_lines = log_file.readlines()

    ip_addresses = []
    requested_pages = []
    status_codes = []

    for line in log_lines:
        try:
            ip_address = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
            requested_page = re.search(r'"(GET|POST) ([^"]+)', line).group(2)
            status_code = int(re.search(r' (\d{3}) ', line).group(1))

            ip_addresses.append(ip_address)
            requested_pages.append(requested_page)
            status_codes.append(status_code)
        except AttributeError:
            continue

    ip_count = Counter(ip_addresses)
    page_count = Counter(requested_pages)
    status_count = Counter(status_codes)

    print("Log File Analysis:")
    print("Top IP Addresses:")
    for ip, count in ip_count.most_common(5):
        print(f"{ip}: {count}")

    print("\nTop Requested Pages:")
    for page, count in page_count.most_common(5):
        print(f"{page}: {count}")

    print("\nStatus Code Summary:")
    for code, count in status_count.items():
        print(f"{code}: {count}")

    print(f"\nTotal 404 Errors: {status_count.get(404, 0)}")

# Example usage
log_file_path = "Apache_logs_1.txt"

analyze_log_file(log_file_path)