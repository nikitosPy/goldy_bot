import disnake as discord
from disnake.ext import commands
import os
from config import *
class Logs(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def logs(self, ctx: commands.Context):
    file = discord.File("./logs.txt")
    await ctx.send(fp = file)
def setup(bot):
  bot.add_cog(Logs(bot))
