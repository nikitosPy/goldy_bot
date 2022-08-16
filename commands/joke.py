import disnake as discord
from disnake.ext import commands
import json, aiohttp
joke = ''
class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def cat(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(joke) as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send(js['joke'])
def setup(bot):
    bot.add_cog(Cat(bot))
