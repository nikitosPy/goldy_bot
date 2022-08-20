import json

import requests
from bs4 import BeautifulSoup
from discord.ext import commands

class GitHub(commands.Cog):
    """Get repository info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gh'])
    async def github(self, ctx, arg):
        """Fetch repository info"""

        req = requests.get(f'https://api.github.com/repos/{arg}')
        apijson = json.loads(req.text)
        em = discord.Embed(
          description = apijson)
        if req.status_code == 200:
            await ctx.send(embed=em)
        elif req.status_code == 404:
            """if repository not found"""
            await ctx.send(embed=teapot.messages.notfound("repository"))
        elif req.status_code == 503:
            """GithubAPI down"""
            await ctx.send("GithubAPI down")
            await ctx.send(embed=teapot.messages.notfound("Fetch repository info"))
        else:
            """some error occurred while fetching repository info"""
            await ctx.send(embed=teapot.messages.error("Fetch repository info"))


def setup(bot):
    """ Setup GitHub Module"""
    bot.add_cog(GitHub(bot))
