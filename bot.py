print("Запуск...") 
###
try:
    import discord #Создание Клиента
    from discord.ext import commands #Команды
    from enum import Enum
    import pretty_errors
    from typing import List
    import asyncio
    import youtube_dl
except:
    import os
    os.system("pip install -r requirements.txt")
import os #Тоже генераторы
import logging
pretty_errors.activate()
from config import prefix, intents, token
def load_extensions():
    for filename in os.listdir("./commands"):
         if filename.endswith(".py") and not filename.startswith('view'):
            bot.load_extension(f"commands.{filename[:-3]}")
    for filename in os.listdir("./events"):
         if filename.endswith(".py"):
            bot.load_extension(f"events.{filename[:-3]}")
    for filename in os.listdir("./ecogoldy"):
         if filename.endswith(".py"):
            bot.load_extension(f"ecogoldy.{filename[:-3]}")



class GoldyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = prefix, 
                         intents = intents, 
                         case_insensitive = True)
    async def on_ready(self):
        await self.wait_until_ready()	
        load_extensions()
        print("ready!")
    async def setup_hook(self):
        try:
            await self.tree.sync()
        except:
            print('sync')
            
ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # Bind to ipv4 since ipv6 addresses cause issues at certain times
}

ffmpeg_options = {"options": "-vn"}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source: discord.AudioSource, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if "entries" in data:
            # Takes the first item from a playlist
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)            
            
            
            
            
            
            
            
            
            
bot = GoldyBot()
bot.remove_command('help')
#Создание бота
### ?
#Логи discord
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.command()
async def play(ctx, channel: discord.VoiceChannel, *, url: str):
    await channel.connect()
    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        ctx.voice_client.play(player, after=lambda e: print(f"Player error: {e}") if e else None)
    await ctx.send(f"Now playing: {player.title}")




#Reload
@bot.command()
async def reload(ctx):
    if ctx.author.id == bot.owner_id:
        async with ctx.typing():
            load_extensions()
        await ctx.send("logs updated")
    else:
        await ctx.send("Не похож ты на моего разработчика...")
#

bot.run(token)


