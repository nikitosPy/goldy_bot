import disnake as discord
from disnake.ext import commands
from random import choice
class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def joke(self, ctx: commands.Context):
      with open('./jokes.txt') as j:
          joke = choice(j.readLines())
      await ctx.send(f'Случайная шутка: \n{joke}')
def setup(bot):
    bot.add_cog(Joke(bot))
