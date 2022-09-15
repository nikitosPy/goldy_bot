import discord
from discord.ext import commands
from config import *
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def botinfo(self, ctx: commands.Context):
        embed = discord.Embed(
            title = f"Информация о Боте {self.bot.user.name}!",
            description = f"http://goldybot.gq \nВладельцы бота:  <@{goldy}> и <@{self.bot.owner.id}> \nБот создан: \nВ начале июля 2022 \nВ боте обновления каждый день!")
        await ctx.send(embed = embed)
    @commands.command()
    async def botcommands(self, ctx: commands.Context):
        cmnds = '\n- '.join([c.name for c in self.bot.commands])
        await ctx.send(f"```\n{cmnds}\n```")
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'Задержка бота: {round(self.bot.latency*1000)/1000} секунд')
    @commands.command()
    async def help(self, ctx: commands.Context):
        title = 'Команды Бота'
        emb = discord.Embed(
            title = title)
        emb.add_field(name="🆘️ help", value = "Покажет это сообщение", inline = True)
        emb.add_field(name = "🏓 ping", value = "Задержка бота", inline = True)
        emb.add_field(name = "ℹ botinfo", value = "Информация о боте", inline = True)
        
        emb.add_field(name = "🗣 botecho", value = "Сказать от имени бота", inline = True)
        emb.add_field(name = "🇬🇧 translate", value = "Перевод фразы", inline = True)
        emb.add_field(name = "🧹 clear", value = "Очистка сообщений в чате", inline = True)
        
        emb.add_field(name = "🐸 cat/dog/fox/pikachu/panda/koala", value = "Случайное фото  животного", inline = True)
        emb.add_field(name = "🤡 joke", value = "Случайная шутка", inline = True)
        emb.add_field(name = "👑 role", value = "Получение личной роли", inline = True)
        
        emb.add_field(name = "🎴 coin", value = "Подбросить монетку", inline = True)
        emb.add_field(name = "🎲 random", value = "Случайное число", inline = True)
        await ctx.send(embed = emb)
def setup(bot):
    bot.add_cog(Info(bot))
