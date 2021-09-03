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



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Img_Downloader("https://x265.club/wp-content/uploads/2020/08/lower-decks.jpg", "lower-decks.jpg"))
