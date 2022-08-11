import disnake as discord
from disnake.ext import commands
import random, os

class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def restart(self, ctx: commands.Context):
        if ctx.author == self.bot.owner:
            await ctx.send(f"Бот перезапущен!")
            os.system("python bot.py")
        else:
            await ctx.send("Вы не разработчик бота...")
def setup(bot):
    bot.add_cog(Restart(bot))
