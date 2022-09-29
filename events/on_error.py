import discord
from discord.ext import commands
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
            cmds = [c.name for c in self.bot.commands]
            cmds.sort()
            difference = process.extractOne(ctx.message.content, cmds)
            if difference[1] > 70: 
                await ctx.send(f"Вы неверно вписали команду!\nЕсть похожая команда: {difference[0]}")  
            else: 
                await ctx.send(f"Вы неверно вписали команду!")
        elif isinstance(error, commands.UserInputError):
            await ctx.send(f"Введите правильно команду!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("У вас недостаточно прав для совершения команды")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Укажите необходимые аргументы!")
        else:
            emb = discord.Embed(title = "Произошла Ошибка: ", description = f"{error}")
            emb.set_footer(text = 'Я уже сообщил админам')
            await ctx.send(embed = emb)
            owner = self.bot.get_user(self.bot.owner_id)
            await owner.send(embed = emb) 
def setup(bot):
   bot.add_cog(Error(bot))
