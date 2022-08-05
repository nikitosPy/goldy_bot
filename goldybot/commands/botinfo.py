import disnake as discord
from disnake.ext import commands
from config import *
class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def botinfo(self, ctx: commands.Context):
        await ctx.send(f"Информация о Боте {self.bot.user.name}! \nhttp://goldymine.tk \nВладельцы бота:  <@{goldy}> и <@{self.bot.owner.id}> \nБот создан: \nВ начале июля 2022 \nВ боте обновления каждый день!")
def setup(bot):
    bot.add_cog(Botinfo(bot))