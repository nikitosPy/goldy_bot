import discord
from discord.ext import commands
from panel import Panel
class PanelCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def panel(self, ctx: commands.Context):
    await ctx.send('Панель Goldybot!', view = Panel(timeout = None))
def setup(bot):
  bot.add_cog(PanelCog(bot))
