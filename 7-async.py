import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
urls = [
    f"https://www.cnblogs.com/sitehome/p/{page}" for page in range(1, 50+1)]

# 定义协程


async def async_craw(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url} {len(result)}")

# 获取事件循环
loop = asyncio.get_event_loop()


# 创建task列表
tasks = [loop.create_task(async_craw(url)) for url in urls]

# 执行爬虫事件列表

if __name__ == "__main__":
    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print(f"use time: {end - start} seconds")
