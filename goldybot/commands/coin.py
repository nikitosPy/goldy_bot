import disnake as discord
from disnake.ext import commands
import random
rand = random.randint(0,2)
if rand == 0:
    coin = "Орёл"
    file = "coin1.jpg"
else:
    coin = "Решка"
    file = "coin2.jpg"
class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def coin(self, ctx: commands.Context):
        await ctx.send(f"Я подбросил монетку и получил: {coin}", file = discord.File(file))
def setup(bot):
    bot.add_cog(Coin(bot))