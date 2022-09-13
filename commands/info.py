import discord
from discord.ext import commands
from config import *
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.hybrid_command(with_app_command = True)
    async def botinfo(self, ctx: commands.Context):
        embed = discord.Embed(
            title = f"Информация о Боте {self.bot.user.name}!",
            description = f"http://goldybot.gq \nВладельцы бота:  <@{goldy}> и <@{self.bot.owner.id}> \nБот создан: \nВ начале июля 2022 \nВ боте обновления каждый день!")
        await ctx.send(embed = embed)
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'Задержка бота: {round(self.bot.latency*1000)/1000} секунд')
async def setup(bot):
    await bot.add_cog(Info(bot))
