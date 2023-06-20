from discord.ext import commands
import dotenv
import os
from interactions import *
from discord import Status, Activity, Game
from bs4 import BeautifulSoup
from time import sleep
from asyncio import TimeoutError
from interactions.api.events import Component
from waifuim import WaifuAioClient


dotenv.load_dotenv()

token = os.getenv('TOKEN')

bot = Client(token=token)
wf = WaifuAioClient()

@listen()
async def on_ready():
    print(f'Bot is ready.')
    await bot.change_presence(activity=Game(name="with your mom"))

@slash_command(
    name="random",
    description="Gets a random waifu image"
)
async def random(ctx: SlashContext):
    await ctx.defer()
    image = await wf.search(is_nsfw='false')

    # await ctx.send(embed=Embed(title="Nyaaaaa~~~~", description="", color=0x73a66e))
    await ctx.send(image.url)    

bot.start()


