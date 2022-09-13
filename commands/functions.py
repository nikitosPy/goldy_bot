import discord
from discord.ext import commands
import json, aiohttp
from config import *
from translate import Translator
translator= Translator(to_lang="ru")
class Functions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def clear(self, ctx: commands.Context, n: int):
        await ctx.channel.purge(limit = n+1)
        await ctx.send(embed = discord.Embed(title=f"Очищено {n} сообщений"))
    @commands.command()
    async def translate(self, ctx: commands.Context, *, words):
         trans = translator.translate(words)
         await ctx.send(trans)
    @commands.hybrid_command(name = "botecho", with_app_command = True)
    async def botecho(self, ctx: commands.Context, member: str, *, content: str):
        
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
async def setup(bot):
    await bot.add_cog(Translate(bot))
