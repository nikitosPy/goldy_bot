from distutils import extension
import disnake as discord #Создание Клиента
from disnake.ext import commands #Команды
from config import *
class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx: commands.Context, member = None, content):
        
        await ctx.message.delete()  # We don't want users to see who initiated the command, to make it more realistic :P
        # We fetch the channel's webhooks.
        channel = ctx.channel
        if not isinstance(channel, discord.TextChannel):
            return
        channel_webhooks = await channel.webhooks()
        # We check if the bot's webhook already exists in the channel.
        for webhook in channel_webhooks:
            # We will check if the creator of the webhook is the same as the bot, and if the name is the same.
            if webhook.user == self.bot.user and webhook.name == "Bot Webhook":
                break
        else:
            # If the webhook does not exist, it will be created.
            webhook = await channel.create_webhook(name="Bot Webhook")
        # Finally, sending the message via the webhook, using the user's display name and avatar.
        if not member:
            member = ctx.author.display_name
            avatar_url = ctx.display_avatar.url
        else:
            avatar_url = self.bot.avatar.url
        await webhook.send(
            content=content, username=member, avatar_url = avatar_url
        )
        log("echo")
def setup(bot):
    bot.add_cog(Echo(bot))
