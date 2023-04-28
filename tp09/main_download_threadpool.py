import httpx
import sys
from bs4 import BeautifulSoup
import time
import threading
from multiprocessing.pool import ThreadPool

def download(url):
    response = httpx.get(url)
    file_name = f'./logs/{url.split("/")[-1]}'

    with open(file_name,'w') as f:
        print(response.text,file=f)

def main():

    url ="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_a = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]    

    start = time.perf_counter()

    with ThreadPool(5) as tp:
        tp.map(download,all_a)
    
    print(time.perf_counter()-start)

    
if __name__ == '__main__':
    main()
