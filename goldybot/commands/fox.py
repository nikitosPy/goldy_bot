import disnake as discord
from disnake.ext import commands
import json, aiohttp
animal = 'https://some-random-api.ml/img/'
class Fox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def fox(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'fox') as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send(js['link'])
def setup(bot):
    bot.add_cog(Fox(bot))