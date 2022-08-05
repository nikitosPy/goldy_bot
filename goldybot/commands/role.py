import disnake as discord
from disnake.ext import commands
from asyncio import sleep
class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def role(self, ctx: commands.Context):
        role = discord.utils.get(ctx.guild.roles,name=ctx.author.name) 
        if role not in ctx.guild.roles:
            await ctx.guild.create_role(name = ctx.author.name)
            role = discord.utils.get(ctx.guild.roles, name = ctx.author.name)
            await ctx.message.author.add_roles(role) 
            await sleep(300)
            await ctx.message.author.remove_roles(role)
            await role.delete()
        else:
             await ctx.send("Error") 
def setup(bot):
    bot.add_cog(Role(bot))