import aiofiles
import aiohttp
import asyncio


async def Img_Downloader(IMAGE, NAME):
    async with aiohttp.ClientSession() as session:
        async with session.get(IMAGE) as resp:
            print("Sent req to site to download Image")

            rss_files = await aiofiles.open(f'./images/{NAME}', mode='wb')
            await rss_files.write(await resp.read())
            await rss_files.close()
            print("Image has been downloaded")
