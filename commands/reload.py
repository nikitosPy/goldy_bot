import discord
from discord.ext.commands import Context, Cog
from discord.ext import commands
class Reload(Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.bridge_command(name = 'reload', with_app_command = True)
  async def reload(self, ctx: Context):
    if ctx.author.id == bot.owner_id:
        async with ctx.typing():
            load_extensions()
        await ctx.send("logs updated")
    else:
        await ctx.send("Не похож ты на моего разработчика...")
def setup(bot):
  bot.add_cog(Reload(bot))
