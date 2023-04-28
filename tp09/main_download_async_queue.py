import httpx
import sys
from bs4 import BeautifulSoup
import time
import asyncio
import threading
import functools

async def download(url_q,data_q,worker_id):
    while True:
        data = await url_q.get()
        url = data['url']
        print(worker_id,url)
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data_q.put_nowait({"text":response.text,"url":url})
        url_q.task_done()
    

async def save(data_q,worker_id):
    while True:
        data = await data_q.get()
        text = data["text"]
        url = data["url"]
        print(worker_id,url)
        file_name = f'./logs/{url.split("/")[-1]}'
        with open(file_name,'w') as f:
            print(text,file=f)
        data_q.task_done()

async def main():

    url_q = asyncio.Queue()
    data_q = asyncio.Queue()

    url ="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_a = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]    

    start = time.perf_counter()

    nb_workers = 5
    # tasks = [download(u) for u in all_a]
    download_tasks = [asyncio.create_task(download(url_q,data_q,f"dl_task {i}")) for i in range(nb_workers)]
    save_tasks = [asyncio.create_task(save(data_q,f"save_task {i}")) for i in range(nb_workers)]

    for the_url in all_a:
        url_q.put_nowait({"url":the_url})
    
    await url_q.join()
    await data_q.join()




    for d in download_tasks:
        d.cancel()
    
    for s in save_tasks:
        s.cancel()

    print(time.perf_counter()-start)
    
if __name__ == '__main__':
    asyncio.run(main())
