import csv
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

read_file = open('example.txt', 'r', encoding='utf-8').read().splitlines()
results = []
for website in read_file:
    try:
        response = requests.get('https://'+website, timeout=5, verify=False)
        results.append((website, response.elapsed.total_seconds()))
    except requests.exceptions.Timeout:
        results.append((website, "Timeout"))

with open("timeout_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Website", "Timeout"])
    writer.writerows(results)