import disnake as discord
from disnake.ext import commands
import json, aiohttp
joke = 'https://geek-jokes.sameerkumar.website/api?format=json'
from translate import Translator
class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def joke(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(joke) as r:
                if r.status == 200:
                    js = await r.json()
                    joke = js['joke']
                    translator= Translator(to_lang="ru")
                    joke = translator.translate(joke)
                    await ctx.send(joke)
                    
def setup(bot):
    bot.add_cog(Joke(bot))
