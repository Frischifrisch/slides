import aiohttp
import asyncio
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import time

urls = ['https://code-maven.com/', 'https://code-maven.com/slides']
sitemap_url = 'https://code-maven.com/slides/sitemap.xml'

def get_urls(content):
    urls = []
    root = ET.fromstring(content)
    for child in root:
        urls.extend(ch.text for ch in child if ch.tag.endswith('loc'))
    #print(len(urls)) # 2653
    MAX = 2
    if len(urls) > MAX:
        urls = urls[:MAX]

    return urls


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        sitemap_xml = await fetch(session, sitemap_url)

    urls = get_urls(sitemap_xml)
    #print(urls)

    titles = []
    tasks = []
    async with aiohttp.ClientSession() as session:
        tasks.extend(fetch(session, url) for url in urls)
        await ayyncio.gather(*tasks)
        print("done")
            #for html in tasks:
            #    soup = BeautifulSoup(html, 'html.parser')
            #    print(soup.title.string)
            #    titles.append(soup.title.string)
    end = time.time()
    print(f"Elapsed time: {end - start} for {len(urls)} pages.")
    print(titles)


asyncio.run(main())

