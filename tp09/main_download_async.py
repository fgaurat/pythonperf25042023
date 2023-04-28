import httpx
import sys
from bs4 import BeautifulSoup
import time
import asyncio
import threading
import functools

async def download(url):
    loop = asyncio.get_event_loop()
                    
    response = await loop.run_in_executor(None, functools.partial(httpx.get,url))
    
    file_name = f'./logs/{url.split("/")[-1]}'

    with open(file_name,'w') as f:
        print(response.text,file=f)

async def main():

    url ="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_a = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]    


    start = time.perf_counter()
    tasks = [download(u) for u in all_a]
    await asyncio.gather(*tasks)

    print(time.perf_counter()-start)

    
if __name__ == '__main__':
    asyncio.run(main())
