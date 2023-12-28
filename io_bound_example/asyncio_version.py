import asyncio

import aiohttp
import time


async def download_site(url, session):
    response = await session.request(method="GET", url=url)
    content = await response.content.read()
    print(f"Read {len(content)} from {url}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(url, session))
            tasks.append(task)
        tasks = await asyncio.gather(*tasks, return_exceptions=True)
        for task in tasks:
            if isinstance(task, Exception):
                raise task


if __name__ == "__main__":
    sites = [
                "https://http.cat/",
            ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
