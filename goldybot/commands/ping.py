import disnake as discord
from disnake.ext import commands
class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'Задержка бота: {round(self.bot.latency*1000)/1000} секунд')
def setup(bot):
    bot.add_cog(Ping(bot))