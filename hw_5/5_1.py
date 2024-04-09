import aiohttp
import asyncio
import aiofiles
from pathlib import Path
import os


async def download_image(session, url, folder, index):
    async with session.get(url) as response:
        if response.status == 200:
            fpath = Path(folder) / f'image_{index}.jpg'
            async with aiofiles.open(fpath, mode='wb') as f:
                await f.write(await response.read())
            print(f"Downloaded {fpath}")


async def download_images(folder, total):
    url = "https://picsum.photos/1000"
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, url, folder, i) for i in range(total)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    current_directory = os.getcwd()
    folder = os.path.join(
        current_directory, "hw_5\\artifacts\\5.1")  # artifacts folder for 5.1
    total_images = 10  # number of pictures that we gonna download
    Path(folder).mkdir(parents=True, exist_ok=True)
    asyncio.run(download_images(folder, total_images))
