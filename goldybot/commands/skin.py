import disnake as discord
from disnake.ext import commands
import aiohttp
animal = 'https://some-random-api.ml'
class Skin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def skin(self, ctx: commands.Context, username: str):
        await ctx.send(f"Ваш скин: https://minecraft.tools/en/skin.php?skin={username}") 
def setup(bot):
    bot.add_cog(Skin(bot))