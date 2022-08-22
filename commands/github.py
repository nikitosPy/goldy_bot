import json
import disnake as discord
import requests
from bs4 import BeautifulSoup
from disnake.ext import commands

class GitHub(commands.Cog):
    """Get repository info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['github'])
    async def __github(self, ctx, arg):
        req = requests.get(f'https://api.github.com/repos/{arg}')
        if req.status_code == 200:
            apijson = json.loads(req.text)
  
        await ctx.send(apijson)
def setup(bot):
    """ Setup GitHub Module"""
    bot.add_cog(GitHub(bot))
