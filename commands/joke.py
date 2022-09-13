import discord
from discord.ext import commands
import json, aiohttp
joke = 'https://geek-jokes.sameerkumar.website/api?format=json'
from translate import Translator
translator= Translator(to_lang="ru")
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def joke(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as cs:
            for i in range(5):
                async with cs.get(joke) as r:
                    if r.status == 200:
                        js = await r.json()
                        joke_t = translator.translate(js['joke'])
                await ctx.send(joke_t)
    @commands.command()
    async def random(self, ctx: commands.Context):
        await ctx.send(f'Случайное число от 0 до 1000: \n{random.randint(0,1001)}')
    @commands.command()
    async def role(self, ctx: commands.Context):
        role = discord.utils.get(ctx.guild.roles,name=ctx.author.name) 
        if role not in ctx.guild.roles:
            await ctx.guild.create_role(name = ctx.author.name)
        role = discord.utils.get(ctx.guild.roles, name = ctx.author.name)
        await role.edit(colour=discord.Color.random())
        await ctx.message.author.add_roles(role) 
        await sleep(300)
        await ctx.message.author.remove_roles(role)
        await role.delete()
    @commands.command()
    async def coin(self, ctx: commands.Context):
        rand = random.randrange(0,2)
        if rand == 0:
            coin = "Орёл"
            file = "coin1.jpg"
        else:
            coin = "Решка"
            file = "coin2.jpg"
        await ctx.send(embed = discord.Embed(title = f"Я подбросил монетку и получил: {coin}"))
        await ctx.send(file = discord.File(file))
def setup(bot):
    bot.add_cog(Fun(bot))
