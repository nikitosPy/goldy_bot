print("Запуск...") 
###
try: 
    import discord #Создание Клиента
    from discord.ext import commands #Команды
    from config import *
    import os #Тоже генераторы
    import logging
    from typing import List
    import asyncio
except:
    import os
    os.system("pip install -r requirements.txt")
from config import prefix, intents, token
bot = commands.Bot(command_prefix = prefix, intents = intents, case_insensitive = True)
bot.remove_command("help")

#Создание бота
### ?
#Логи disnake
logger = logging.getLogger('disnake')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
async def load_extensions():
    await bot.load_extension(f"commands.botecho")
    """
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")
 """
    for filename in os.listdir("./events"):
        if filename.endswith(".py"):
            await bot.load_extension(f"events.{filename[:-3]}")
"""
    for filename in os.listdir("./ecogoldy"):
        if filename.endswith(".py"):
            await bot.load_extension(f"ecogoldy.{filename[:-3]}")
            """
#Reload
@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == bot.owner_id:
        bot.unload_extension(f"commands.{extension}")
        bot.load_extension(f"commands.{extension}")
        await ctx.send(f"Обновлен cog {extension}!")
    else:
        await ctx.send("Не похож ты на моего разработчика...")
#
@bot.event
async def on_ready():
    await load_extensions()

        
with open("logs.txt", "a+") as f:
    f.write("\n")           

bot.run(token)


