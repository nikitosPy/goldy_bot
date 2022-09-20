import discord
from discord.ext import commands
import datetime
from config import *
import time
from asyncio import sleep
start = round(time.time())
class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        print('Бот запущен!')
        print('Готов под именем ---->', self.bot.user)
        print('ID:', self.bot.user.id)
        
        print(datetime.datetime.now())
        global logs, admin1, admin2
        admin1 = await self.bot.fetch_user(self.bot.owner_id)
        admin2 = await self.bot.fetch_user(goldy)
        logs = self.bot.get_channel(logs_ch)
        await admin1.send(f"Я перезапущен под именем {self.bot.user.name}: <t:{start}:R>")
        await admin2.send(f"Я перезапущен под именем {self.bot.user.name}: <t:{start}:R>")
        global owners
        owners = [admin1.id, admin2.id]
        while True:
            for status in statuses:
                await self.bot.change_presence(status=discord.Status.idle, activity = discord.Activity(type=discord.ActivityType.listening, name=status))
                await sleep(5)
def setup(bot):
    bot.add_cog(Ready(bot))
