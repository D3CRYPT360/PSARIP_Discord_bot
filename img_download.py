import logging
import aiofiles
import aiohttp
import asyncio


async def download_img(IMAGE, NAME):
    async with aiohttp.ClientSession() as session:
        async with session.get(IMAGE) as resp:
            logging.debug('Downloading image "%s" from PSArips', NAME)
            async with aiofiles.open(f'./images/{NAME}', mode='wb') as rss_files:
                await rss_files.write(await resp.read())
            logging.debug('Downloaded image successfully')
