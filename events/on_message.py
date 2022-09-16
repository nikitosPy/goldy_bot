import discord
from discord.ext import commands
from time import time
from config import *
import random
import sqlite3
from rapidfuzz import fuzz, process
class Message(commands.Cog):
    ##
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        admin1 = self.bot.get_user(self.bot.owner_id)
        admin2 = self.bot.get_user(goldy)
        if message.author == self.bot.user: 
            return
        elif self.bot.user.mention in message.content:
            await message.channel.send(f"""
Привет! Я бот {self.bot.user.name}!
В данный момент Бот на ОБТ (открытом бета-тестировании)
Если возникнут вопросы / пожелания / идеи - 
Пишите в Л / С и я это передам моим админам.
Я многофункциольный :smiley:
    """)

        for wel in welcome:
            if wel in str(message.content).lower():
                await message.channel.send(f"И тебе {wel}, дорогой <@{message.author.id}>!")
                break
        for content in str(message.content).lower().split():
            difference = process.extractOne(content, bad_words)
            if difference[1] >= 95:
                await message.channel.purge(limit = 1)
                await message.channel.send(f"<@{message.author.id}>, Не матерись! || Админы, он сказал: {message.content}, я подумал что {difference[0]}, Шанс: {difference[1]} ||")
                break
        content = str(message.content).lower()
        if "как дела" in content:
            result = ["У меня нормально, а у тебя?", "К сожаленью плохо :(", "Всё супер!"]
            await message.channel.send(random.choice(result))

        for bye in ends:
            if bye in str(message.content).lower():
                await message.channel.send(f"И тебе {bye}, дорогой <@{message.author.id}>!")
                break
        for ping in pings:
            if ping in str(message.content).lower():
                await message.channel.purge(limit = 1)
                await message.channel.send(f"Не упоминай пинги everyone и here")
                break
async def setup(bot):
    await bot.add_cog(Message(bot))
