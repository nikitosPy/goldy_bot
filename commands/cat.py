import discord
from discord.ext import commands
import json, aiohttp
from config import *
animal = 'https://some-random-api.ml/img/'
class Cat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def cat(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'cat') as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send(js['link'])
                    log("cat")
def setup(bot):
    bot.add_cog(Cat(bot))
