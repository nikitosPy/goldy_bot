import disnake as discord
from disnake.ext import commands
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def clear(self, ctx: commands.Context, n: int):
        await ctx.channel.purge(limit = n+1)
        await ctx.send(f"Очищено {n} сообщений")
def setup(bot):
    bot.add_cog(Clear(bot))