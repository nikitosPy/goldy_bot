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
        """Fetch repository info"""
        with open("new.txt", 'w') as n:
            req = requests.get(f'https://api.github.com/repos/{arg}')
            if req.status_code == 200:
                apijson = json.loads(req.text)
                n.write(str(apijson))
        await ctx.send(file = discord.File(fp = "new.txt"))
def setup(bot):
    """ Setup GitHub Module"""
    bot.add_cog(GitHub(bot))
