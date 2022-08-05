import disnake as discord
from disnake.ext import commands
import random, os

class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def restart(self, ctx: commands.Context):
        await ctx.send(f"Бот перезапущен!")
        os.system("python bot.py")
def setup(bot):
    bot.add_cog(Restart(bot))