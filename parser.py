import re

ip_pattern = r"(\d+\.\d+\.\d+\.\d+)"
status_code = r"(HTTP/1.1\")\s(\d{3})\s"
dictionary = {}

with open("server.log") as file:
    for line in file:
        match_ip = re.search(ip_pattern, line)
        match_status = re.search(status_code, line)
        if (match_ip and match_status):
            if match_ip.group() in dictionary:
                dictionary[match_ip.group()]["count"] += 1
                dictionary[match_ip.group()]["status_codes"].append(match_status.group(2))
            else:
                dictionary[match_ip.group()] = {
                    "count": 1,
                    "status_codes": [match_status.group(2)]
                }

for ip, data in dictionary.items():
    failed_logins = data["status_codes"].count("401")
    forbidden =  data["status_codes"].count("403")
    not_found = data["status_codes"].count("404")
    report_line = f"IP = {ip:15} | Requests: {data['count']}"
    if (failed_logins + forbidden + not_found > 3):
        print(report_line + f" 🚨 SECURITY ALERT: {failed_logins + forbidden + not_found} suspicious attempts detected! 🚨")
    else:
        print(report_line)