import time
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def get_urls(content):
    urls = []
    root = ET.fromstring(content)
    for child in root:
        urls.extend(ch.text for ch in child if ch.tag.endswith('loc'))
    #print(len(urls)) # 2653
    MAX = 20
    if len(urls) > MAX:
        urls = urls[:MAX]

    return urls

def main():
    start = time.time()
    url = 'https://code-maven.com/slides/sitemap.xml'
    resp = requests.get(url)
    if resp.status_code != 200:
        exit(f"Incorrect status_code {resp.status_code}")

    urls = get_urls(resp.content)

    titles = []
    for url in urls:
        resp = requests.get(url)
        if resp.status_code != 200:
            print(f"Incorrect status_code {resp.status_code} for {url}")
            continue

        soup = BeautifulSoup(resp.content, 'html.parser')
        print(soup.title.string)
        titles.append(soup.title.string)
    end = time.time()
    print(f"Elapsed time: {end - start} for {len(urls)} pages.")
    print(titles)


if __name__ == '__main__':
    main()
