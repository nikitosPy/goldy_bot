import disnake as discord
from disnake.ext import commands
import os
from config import *
from rapidfuzz import fuzz, process
class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        print()
        if isinstance(error, commands.CommandNotFound):
            cmds.sort()
            difference = process.extractOne(ctx.message.content, cmds)
            if difference[1] > 0: 
                await ctx.send(f"Вы неверно вписали команду!\nЕсть похожая команда: {difference[0]}")  
            else: 
                await ctx.send(f"Вы неверно вписали команду!")
        else:
            await ctx.send(f"Ошибка: \n{error}")
def setup(bot):
    bot.add_cog(Error(bot))