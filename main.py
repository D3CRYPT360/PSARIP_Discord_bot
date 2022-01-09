"""
A Discord bot which sends a message to a channel whenever a new movie/series episode is released on PSArips
"""
import ast
import glob
import logging
import os

import discord
import feedparser
from bs4 import BeautifulSoup
from discord.ext import commands, tasks
from dotenv import load_dotenv
from img_download import download_img

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

load_dotenv(".env")

CHANNEL_ID = ast.literal_eval(os.getenv("CHANNELS"))

CURRENT = None
LAST = None

activity = discord.Activity(type=discord.ActivityType.watching, name="https://psa.pm/")
bot = commands.Bot(command_prefix="=", activity=activity)


@bot.event
async def on_ready():
    """Discord bot starting event"""
    logging.info("=== BOT HAS STARTED ===")
    logging.info("User ID: %s", bot.user.id)
    logging.info("=======================")


async def channel_sender(title, link, name, channel_id):
    """Sends new content with required formatting."""
    channel_to_send = bot.get_channel(channel_id)
    embed = discord.Embed(
        colour=discord.Color.random(),
        title=title,
        # Getting the text in the P tag in the description
        description=f"[LINK]({link})\n{soup.p.text}",
    )

    # For some weird reason Discord won't put image directly on the embed from the link provided.
    # Have to download it locally and upload it.
    file = discord.File(f"./images/{name}", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await channel_to_send.send(file=file, embed=embed)


@tasks.loop(seconds=60)
async def top():
    """Main bot event"""
    feed = feedparser.parse("https://psa.pm/feed")

    desc = feed.entries[0].summary_detail.value
    title = feed.entries[0].title
    url = feed.entries[0].link

    # Parsing HTML to get the image link because the description is in HTML
    global soup
    soup = BeautifulSoup(desc, "lxml")
    img = soup.find("img").get("src")
    name = img.split("/")[7]

    global CURRENT
    global LAST
    CURRENT = title
    if CURRENT != LAST:
        LAST = CURRENT
        await download_img(img, name)

        if len(CHANNEL_ID) > 1:
            for channel in CHANNEL_ID:
                await channel_sender(title, url, name, channel)
        else:
            await channel_sender(title, url, name, CHANNEL_ID[0])

        for file in glob.glob("./images/*"):
            os.remove(file)


@top.before_loop
async def wait_for_bot():
    """Starting main bot loop AFTER bot is logged in"""
    await bot.wait_until_ready()


top.start()
bot.run(os.getenv("BOT_TOKEN"))
