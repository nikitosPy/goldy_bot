print("Запуск...") 
###
try:
    import discord #Создание Клиента
    from discord.ext import commands #Команды
    from enum import Enum
    import pretty_errors
    from typing import List
    import asyncio
    import datetime
    import requests, json
    import youtube_dl
    from PIL import Image
    from PIL import ImageDraw
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
                         case_insensitive = True, 
                help_command = None)
    async def on_ready(self):
        await self.wait_until_ready()	
        load_extensions()
        abio = 'Hello'
        datajs= {"bio": abio} 
        authorizator =  'Bot OTk0MjA5MzkyNTY2MjEwNTYw.Gad6UU.lUt__A9oeMTocfPro3tCcn7wPeqIUUL-QbNC5o'
        r = requests.patch(url="https://discord.com/api/v10/users/@me", 
                       headers= {"Authorization": authorizator,
                                "Content-Type": "application/json",}, 
                       json =datajs) 
        await self.user.edit(username = "GoldyBot")
        print(r.content)
        print(self.user.avatar.url)
        print("ready!")
    async def setup_hook(self):
        try:
            await self.tree.sync()
        except:
            print('sync')
            
bot = GoldyBot()
#Создание бота
### ?
#Логи discord
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#

bot.run(token)


