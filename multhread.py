import requests
import threading
import urllib3
import time
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def start(url):
	response = requests.get('https://'+url, verify=False)
	#print(f'https://{url} -> STATUS CODE : {response.status_code}')



urls = open('example.txt', 'r', encoding='utf-8').read().splitlines()
threads = []

with open("multithread.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Percobaan", "Start Time", "End Time", "Execution Time"])

for i in range(0, 11):
	results = []
	start_time = time.time()  # Waktu mulai
	for url in urls:
	    thread = threading.Thread(target=start, args=(url,))
	    thread.start()
	    threads.append(thread)

	for thread in threads:
	    thread.join()

	end_time = time.time()  # Waktu selesai
	execution_time = end_time - start_time

	results.append((i, start_time, end_time, execution_time))

	print(f'[+] Start time : {start_time}')
	print(f'[+] End time : {end_time}')
	print("[+] Execution Time :", execution_time, "Second")
	with open("multithread.csv", "a", newline="") as file:
	    writer = csv.writer(file)
	    writer.writerows(results)