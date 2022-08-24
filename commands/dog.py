import disnake as discord
from disnake.ext import commands
from config import *
import json, aiohttp
animal = 'https://some-random-api.ml/img/'
class Dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def dog(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'dog') as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send(js['link'])
        log("dog")
def setup(bot):
    bot.add_cog(Dog(bot))
