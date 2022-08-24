from distutils import extension
import disnake as discord #Создание Клиента
from disnake.ext import commands #Команды
from config import *
class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx: commands.Context, *, args):
        if args:
            await ctx.channel.purge(limit = 1)
            await ctx.send(args)
        else:
            await ctx.send("Укажите фразу, которую мне надо сказать...")
        log("echo")
def setup(bot):
    bot.add_cog(Echo(bot))
