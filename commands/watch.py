from distutils import extension
import disnake as discord #Создание Клиента
from disnake.utils import get #Поиск канала
from disnake.ext import commands #Команды
from config import *
from discord_together import DiscordTogether
class Watch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def watch(self, ctx: commands.Context):
        # channel = ctx.author.voice.channel
        # await channel.connect()
        self.bot.togetherControl = await DiscordTogether(token)
        link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"Click the blue link!\n{link}")
def setup(bot):
    bot.add_cog(Watch(bot))
