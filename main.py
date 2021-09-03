import discord
from discord.ext import commands, tasks
from Image_down import Img_Downloader
from dotenv import load_dotenv
import feedparser
import os
import glob
from bs4 import BeautifulSoup

load_dotenv(".env")

Last = None
Current = None

activity = discord.Activity(type=discord.ActivityType.watching, name="https://x265.club/")
bot = commands.Bot(command_prefix=">>", case_insensitive=True, activity=activity)

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command()
async def test(ctx, arg):
    await ctx.send(f"Hello {arg}")

@tasks.loop(seconds=60)
async def top():
    channels_to_send = 883082646383640626
    channel0 = bot.get_channel(channels_to_send) # Our Home
    URL = "https://x265.club/feed"
    feed = feedparser.parse(URL)

    DESC = feed.entries[0].summary_detail.value     
    TITLE = feed.entries[0].title
    LINK = feed.entries[0].link  

    # Parsing HTML to get the image link because the description is in HTML format
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


        embed = discord.Embed(
            colour = discord.Color.random(),
            title = TITLE,
            description=f"[LINK]({LINK})\n{soup.p.text}" # Getting the text in the P tag in the description
        )

        # For some weird reason discord won't put image directly on the embed from the link provided.
        # Have to download it locally and upload it. 
        file = discord.File(f"./images/{NAME}", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await channel0.send(file=file, embed=embed)

        files = glob.glob("./images/*")
        for f in files:
            os.remove(f)

@top.before_loop
async def wait_for_bot():
    await bot.wait_until_ready()

top.start()
bot.run(os.getenv("BOT_TOKEN"))