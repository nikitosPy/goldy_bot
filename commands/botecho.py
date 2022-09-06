from distutils import extension
import discord #Создание Клиента
from discord.ext import commands #Команды
from config import *
class BotEcho(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name = "botecho", with_app_command = True)
    async def botecho(self, ctx: commands.Context, member, *, content):
        
        await ctx.message.delete()
        channel = ctx.channel
        avatar_url = self.bot.user.avatar.url
        if not isinstance(channel, discord.TextChannel):
            return
        channel_webhooks = await channel.webhooks()
        for webhook in channel_webhooks:
            if webhook.user == self.bot.user and webhook.name == "Bot Webhook":
                break
        else:
            webhook = await channel.create_webhook(name="Bot Webhook")
        await webhook.send(
            content=content, username=member, avatar_url = avatar_url
        )
        log("botecho")
def setup(bot):
    bot.add_cog(BotEcho(bot))
