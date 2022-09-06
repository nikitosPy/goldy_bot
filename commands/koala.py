import discord
from discord.ext import commands
import json, aiohttp
from config import *
animal = 'https://some-random-api.ml/img/'
class Koala(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def koala(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(animal + 'koala') as r:
                if r.status == 200:
                    js = await r.json()
                    await ctx.send(js['link'])
    log("koala")
def setup(bot):
    bot.add_cog(Koala(bot))
