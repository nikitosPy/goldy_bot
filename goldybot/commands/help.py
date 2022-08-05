from distutils import extension
import disnake as discord #Создание Клиента
from disnake.utils import get #Поиск канала
from disnake.ext import commands #Команды
from Cybernator import Paginator as pag
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

        embs = [emb1, emb2, emb3, emb4, emb5, emb6]
        msg = await ctx.send(embed = emb1)
        page = pag(self.bot, msg, only = ctx.author, embeds = embs)
        await page.start()
def setup(bot):
    bot.add_cog(Help(bot))