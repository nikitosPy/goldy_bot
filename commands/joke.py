import discord
from discord.ext import commands
import json, aiohttp
joke = 'https://geek-jokes.sameerkumar.website/api?format=json'
from translate import Translator
translator= Translator(to_lang="ru")
class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def joke(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            for i in range(5):
                async with cs.get(joke) as r:
                    if r.status == 200:
                        js = await r.json()
                        joke_t = translator.translate(js['joke'])
                await ctx.send(joke_t)
        log("joke")
def setup(bot):
    bot.add_cog(Joke(bot))
