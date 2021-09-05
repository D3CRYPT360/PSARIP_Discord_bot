import discord
from discord.ext import commands, tasks
from Image_down import Img_Downloader
from dotenv import load_dotenv
import feedparser
import os
import glob
from bs4 import BeautifulSoup


CHANNEL_ID = []

load_dotenv(".env")

Last = None
Current = None

activity = discord.Activity(
    type=discord.ActivityType.watching,
    name="https://x265.club/")
bot = commands.Bot(command_prefix="=", activity=activity)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')


async def channel_sender(TITLE, LINK, NAME, CHANNEL_ID):
    channel_to_send = bot.get_channel(CHANNEL_ID)
    embed = discord.Embed(
        colour=discord.Color.random(),
        title=TITLE,
        # Getting the text in the P tag in the description
        description=f"[LINK]({LINK})\n{soup.p.text}"
    )

    # For some weird reason discord won't put image directly on the embed from the link provided.
    # Have to download it locally and upload it.
    file = discord.File(f"./images/{NAME}", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await channel_to_send.send(file=file, embed=embed)


@tasks.loop(seconds=60)
async def top():
    URL = "https://x265.club/feed"
    feed = feedparser.parse(URL)

    DESC = feed.entries[0].summary_detail.value
    TITLE = feed.entries[0].title
    LINK = feed.entries[0].link

    # Parsing HTML to get the image link because the description is in HTML
    # format
    global soup
    soup = BeautifulSoup(DESC, 'lxml')
    image = soup.find('img')
    IMAGE = image.get("src")
    NAME = IMAGE.split("/")[7]

    global Current
    global Last
    Current = TITLE
    if Current != Last:
        Last = Current
        await Img_Downloader(IMAGE, NAME)

        if len(CHANNEL_ID) > 1:
            for channel in CHANNEL_ID:
                await channel_sender(TITLE, LINK, NAME, channel)
        else:
            await channel_sender(TITLE, LINK, NAME, CHANNEL_ID[0])

        files = glob.glob("./images/*")
        for f in files:
            os.remove(f)


@top.before_loop
async def wait_for_bot():
    await bot.wait_until_ready()

top.start()
bot.run(os.getenv("BOT_TOKEN"))
