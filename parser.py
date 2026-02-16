import re

ip_pattern = r"(\d+\.\d+\.\d+\.\d+)"
status_code = r"\s(\d{3})\s"
dictionary = {}

with open("server.log") as file:
    for line in file:
        match_ip = re.search(ip_pattern, line)
        match_status = re.search(status_code, line)
        if (match_ip and match_status):
            if match_ip.group() in dictionary:
                dictionary[match_ip.group()]["count"] += 1
                dictionary[match_ip.group()]["status_codes"].append(match_status.group(1))
            else:
                dictionary[match_ip.group()] = {
                    "count": 1,
                    "status_codes": [match_status.group(1)]
                }

print(dictionary)