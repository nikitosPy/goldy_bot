import discord
from discord.ext import commands
from config import *
class Debug(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def debug(self, ctx: commands.Context):
    with open("./disnake.log") as debug:
      await ctx.send(debug.read())
      log("debug")
def setup(bot):
  bot.add_cog(Debug(bot))
