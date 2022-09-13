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
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'Задержка бота: {round(self.bot.latency*1000)/1000} секунд')
    @commands.command()
    async def help(self, ctx: commands.Context):
        title = 'Команды Бота'
        emb1 = discord.Embed(
            title = title,
            description = "help - Покажет это сообщение \nping - Задержка Бота \nclear - Очистка сообщений в Чате \necho - Сказать от Имени Бота"
        )
        emb2 = discord.Embed(
            title = title,
            description = "user - Карточка пользователя \nrole - Получить личную роль на 5 минут"
        )
        emb3 = discord.Embed(
            title = title,
            description = "join - Присоединить бот к Голосовому каналу \nwatch - Начать Активность Youtube" 
        )
        emb4 = discord.Embed(
            title = title,
            description = "cat - Рандом Кот \ndog - Рандом Собака \nfox - Рандом Лиса \nkoala - Рандом Коала\npanda - Рандом Панда\npikachu - Рандом Пикачу"
        )
        emb5 = discord.Embed(
            title = title,
            description = "cash | balance - Проверка Баланса \nshop - Магазин Ролей \nadd-shop - Добавить роль в Магазин ролей \n buy | buy-role - купить роль в Магазине Ролей \n like - Лайкнуть Пользователя\n leaderboard | lb - Список Лидеров на Сервере"
        )
        emb6 = discord.Embed(
            title = title,
            description = "Ждите обновлений..."
        )

        await ctx.send(embed = emb1)
        
        emb1.add_field(name="Fiel1", value="hi", inline=True)
        await ctx.send(embed = emb1)
        embs = [emb1, emb2, emb3, emb4, emb5, emb6]
async def setup(bot):
    await bot.add_cog(Info(bot))
