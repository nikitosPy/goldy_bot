import disnake as discord
from disnake.ext import commands
from disnake.utils import find
from asyncio import sleep
class Guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await guild.owner.send("""
    Спасибо вам за приглашение на ваш сервер бота GoldyBot!
    В данный момент Бот на ОБТ (открытом бета-тестировании)
    Если возникнут вопросы / пожелания / идеи - 
    Пишите в Л / С и я это передам моим админам.
    """)
def setup(bot):
    bot.add_cog(Guild(bot))