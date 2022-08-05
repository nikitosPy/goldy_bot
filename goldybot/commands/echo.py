from distutils import extension
import disnake as discord #Создание Клиента
from disnake.utils import get #Поиск канала
from disnake.ext import commands #Команды
class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx: commands.Context, *, args):
        await ctx.channel.purge(limit = 1)
        await ctx.send(args)

def setup(bot):
    bot.add_cog(Echo(bot))