import requests
from concurrent.futures import ThreadPoolExecutor
import urllib3
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time


with open("conc.csv", "a", newline="") as file:
	writer = csv.writer(file)
	writer.writerow(["Percobaan", "Start Time", "End Time", "Execution Time"])

def start(url):
	response = requests.get('https://'+url,verify=False)
	#print(f'https://{url} -> STATUS CODE : {response.status_code}')


read_file = open('example.txt', 'r', encoding='utf-8').read().splitlines()
for i in range(0, 11):
	results = []
	start_time = time.time()  # Waktu selesai
	with ThreadPoolExecutor(max_workers=5) as executor:
		a = executor.map(start, read_file)
	end_time = time.time()  # Waktu selesai
	execution_time = end_time - start_time
	results.append((i, start_time, end_time, execution_time))
	print(f'[+] Start time : {start_time}')
	print(f'[+] End time : {end_time}')
	print("[+] Execution Time :", execution_time, "Second")
	with open("conc.csv", "a", newline="") as file:
		writer = csv.writer(file)
		writer.writerows(results)
