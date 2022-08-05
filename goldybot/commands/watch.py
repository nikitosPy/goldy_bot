from distutils import extension
import disnake as discord #Создание Клиента
from disnake.utils import get #Поиск канала
from disnake.ext import commands #Команды
class Watch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def watch(self, ctx: commands.Context):
        link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"Click the blue link!\n{link}")
def setup(bot):
    bot.add_cog(Watch(bot))
