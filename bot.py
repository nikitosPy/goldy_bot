print("Запуск...") 
###
try: 
    import discord #Создание Клиента
    from discord.ext import commands #Команды
    from config import *
    from discord import app_commands
    import os #Тоже генераторы
    import logging
    from typing import List
    import asyncio
except:
    import os
    os.system("pip install -r requirements.txt")
from config import prefix, intents, token
async def load_extensions():
    await bot.load_extension(f"commands.botecho")
    for filename in os.listdir("./events"):
         if filename.endswith(".py"):
            await bot.load_extension(f"events.{filename[:-3]}")
    for filename in os.listdir("./ecogoldy"):
         if filename.endswith(".py"):
            await bot.load_extension(f"ecogoldy.{filename[:-3]}")
class MyContext(commands.Context):
    async def tick(self, value):
        # reacts to the message with an emoji
        # depending on whether value is True or False
        # if its True, it'll add a green check mark
        # otherwise, it'll add a red cross mark
        emoji = '\N{WHITE HEAVY CHECK MARK}' if value else '\N{CROSS MARK}'
        try:
            # this will react to the command author's message
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            # sometimes errors occur during this, for example
            # maybe you don't have permission to do that
            # we don't mind, so we can just ignore them
            pass


class GoldyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = prefix, 
                         intents = intents, 
                         case_insensitive = True)
    async def on_ready(self):
        await self.wait_until_ready()	
        await load_extensions()
    async def setup_hook(self):
        try:
            await self.tree.sync()
        except:
            print('sync')
    async def get_context(self, message, *, cls=MyContext):
        # when you override this method, you pass your new Context
        # subclass to the super() method, which tells the bot to
        # use the new MyContext class
        return await super().get_context(message, cls=cls)
bot = GoldyBot()
bot.remove_command("help")

#Создание бота
### ?
#Логи discord
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

"""
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f"commands.{filename[:-3]}")
    
    

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


        
with open("logs.txt", "a+") as f:
    f.write("\n")           

bot.run(token)


