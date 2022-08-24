import disnake as discord
from disnake.ext import commands
from config import *
class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def botinfo(self, ctx: commands.Context):
        embed = discord.Embed(
            title = f"Информация о Боте {self.bot.user.name}!",
            description = f"http://goldymine.tk \nВладельцы бота:  <@{goldy}> и <@{self.bot.owner.id}> \nБот создан: \nВ начале июля 2022 \nВ боте обновления каждый день!")
        await ctx.send(embed = embed)
        log("botinfo")
def setup(bot):
    bot.add_cog(Botinfo(bot))
