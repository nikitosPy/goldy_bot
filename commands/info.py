import discord
from discord.ext import commands
import datetime
from discord. uiimport Button, View
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
        title = 'Меню помощи'
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
        emb.add_field(name = "❓ bug", value = "Репорт о баге", inline = True)
        
        emb.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
        emb.set_thumbnail(url=self.bot.user.avatar.url)
        emb.timestamp = datetime.datetime.utcnow()
        emb.set_footer(text=self.bot.user.name)
        button = Button(label = 'test')
        await ctx.send(embed = emb, view = View())
      c view.add_item(button)
    @commands.command()
    async def bug(self, ctx: commands.Context, *, bug):
        async with ctx.typing():
            await self.bot.get_user(self.bot.owner_id).send(bug)
        await ctx.send(f'Отчёт о баге отправлен \n{bug}')
def setup(bot):
    bot.add_cog(Info(bot))
