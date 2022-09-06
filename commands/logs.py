import discord
from discord.ext import commands
import os
from config import *
class Logs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def logs(self, ctx: commands.Context):
    file = discord.File(fp = "./logs.txt")
    await ctx.send(file = file)
    log("logs")
def setup(bot):
  bot.add_cog(Logs(bot))
