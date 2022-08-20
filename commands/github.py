import json

import requests
from bs4 import BeautifulSoup
from discord.ext import commands

class GitHub(commands.Cog):
    """Get repository info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['github'])
    async def github(self, ctx, arg):
        """Fetch repository info"""

        req = requests.get(f'https://api.github.com/repos/{arg}')
        apijson = json.loads(req.text)
        em = discord.Embed(
          description = apijson)
        if req.status_code == 200:
            await ctx.send(embed=em)


def setup(bot):
    """ Setup GitHub Module"""
    bot.add_cog(GitHub(bot))
