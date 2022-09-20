
print("Запуск...") 
###
try:
    import discord #Создание Клиента
    from discord.ext import commands, bridge #Команды
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

def load_exts():
    for filename in os.listdir("./commands"):
         if filename.endswith(".py") and not filename.startswith('view'):
            bot.load_extension(f"commands.{filename[:-3]}")
    for filename in os.listdir("./events"):
         if filename.endswith(".py"):
            bot.load_extension(f"events.{filename[:-3]}")
    for filename in os.listdir("./ecogoldy"):
         if filename.endswith(".py"):
            bot.load_extension(f"ecogoldy.{filename[:-3]}")



class GoldyBot(bridge.Bot):
    def __init__(self):
        super().__init__(command_prefix = prefix, 
                         intents = intents, 
                         case_insensitive = True, 
                help_command = None)
    async def on_ready(self):
        await self.wait_until_ready()	
        abio = "._."
        from config import token
        token = token.replace("\n", "")
        print("ready!")
        r = requests.patch(url="https://discord.com/api/v9/users/@me",
        headers= {"Authorization": f'Bot {token}',
        "Content-type": 'application/json'}, 
        json = {"bio": abio})
        print(r.content)
bot = GoldyBot()
load_exts()
#Создание бота
### ?
#Логи discord
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='pycord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(name)s: %(message)s'))
logger.addHandler(handler)

#

bot.run(token)


