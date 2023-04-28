import httpx
from bs4 import BeautifulSoup

def main():
    url ="https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # for a in soup.find_all('a'):
    #     if ".log" in a['href']:
    #         print(a['href'])

    all_a = [a['href'] for a in soup.find_all('a') if ".log" in a['href']]    

    print(all_a)

    
if __name__ == '__main__':
    main()
