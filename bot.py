print("Запуск...") 
###
try: 
    import discord #Создание Клиента
    from discord.ext import commands #Команды
    from config import *
    import os #Тоже генераторы
    import logging
    from typing import List
except:
    import os
    os.system("pip install -r requirements.txt")
from config import prefix, intents, TOKEN
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

#Reload
@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == bot.owner.id:
        bot.unload_extension(f"commands.{extension}")
        bot.load_extension(f"commands.{extension}")
        await ctx.send(f"Обновлен cog {extension}!")
    else:
        await ctx.send("Не похож ты на моего разработчика...")

@bot.command()
async def tic(ctx: commands.Context):
    await ctx.send('Tic Tac Toe: X goes first', view=TicTacToe())

        
with open("logs.txt", "a+") as f:
    f.write("\n")

for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"commands.{filename[:-3]}")

for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        bot.load_extension(f"events.{filename[:-3]}")

for filename in os.listdir("./ecogoldy"):
    if filename.endswith(".py"):
        bot.load_extension(f"ecogoldy.{filename[:-3]}")

#Запуск
bot.run(token)

