import disnake as discord
from disnake.ext import commands
import json, aiohttp
joke = 'https://geek-jokes.sameerkumar.website/api?format=json'
from translate import Translator
translator= Translator(to_lang="ru")
class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def translate(self, ctx: commands.Context, *, words):
         trans = translator.translate(words)
         await ctx.send(trans)
def setup(bot):
    bot.add_cog(Translate(bot))
