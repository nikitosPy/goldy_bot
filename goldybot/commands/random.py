import disnake as discord
from disnake.ext import commands
import random
class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def random(self, ctx: commands.Context):
        await ctx.send(f'Случайное число от 0 до 1000: \n{random.randint(0,1001)}')
def setup(bot):
    bot.add_cog(Random(bot))