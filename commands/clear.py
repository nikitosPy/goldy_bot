import discord
from discord.ext import commands
from config import *
import os
#
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def clear(self, ctx: commands.Context, n: int):
        if n:
            await ctx.channel.purge(limit = n+1)
            await ctx.send(embed = discord.Embed(title=f"Очищено {n} сообщений"))
        else:
            await ctx.send(embed = discord.Embed(title="Укажите количество сообщений..."))
        log("clear")
def setup(bot):
    bot.add_cog(Clear(bot))
