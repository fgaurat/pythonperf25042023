import httpx
import sys
from bs4 import BeautifulSoup
import time
import threading

def download(url):
    print(threading.current_thread().name)
    response = httpx.get(url)
    file_name = f'./logs/{url.split("/")[-1]}'

    with open(file_name,'w') as f:
        print(response.text,file=f)

def main():
    print(threading.current_thread().name)
    url ="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    all_a = [f"{url}{a['href']}" for a in soup.find_all('a') if ".log" in a['href']]    

    start = time.perf_counter()
    for url_to_download in all_a:
        th1 = threading.Thread(target=download,args=[url_to_download])
        th1.start()
        print("loop",th1.name)
        # threading.Thread(target=download,args=[url_to_download]).start()
    
    print(time.perf_counter()-start)

    
if __name__ == '__main__':
    main()
