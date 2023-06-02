import aiohttp
import asyncio
import ssl
import time
import csv 

with open("async.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Percobaan", "Start Time", "End Time", "Execution Time"])

async def make_request(url):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
        async with session.get('https://'+url) as response:
            pass
            #print(f'https://{url} -> STATUS CODE : {response.status}')

async def main():
    urls = open('example.txt', 'r', encoding='utf-8').read().splitlines()
    for i in range(0, 11):
        results = []
        start_time = time.time()  # Waktu mulai
        tasks = []
        for url in urls:
            task = asyncio.create_task(make_request(url))
            tasks.append(task)

        a = await asyncio.gather(*tasks)
        end_time = time.time()  # Waktu selesai
        execution_time = end_time - start_time
        results.append((i, start_time, end_time, execution_time))
        print(f'[+] Start time : {start_time}')
        print(f'[+] End time : {end_time}')
        print("[+] Execution Time :", execution_time, "Second")
        with open("async.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(results)

asyncio.run(main())
