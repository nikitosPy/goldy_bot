import discord
from discord.ext import commands, bridge
import datetime
from discord.ui import Button, View
from discord import ButtonStyle
import view_help as help
from config import *
class MyModal(discord.ui.Modal):
    def __init__(self, bot, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.bot = bot
        self.add_item(discord.ui.InputText(label="Команда, в которой обнаружен баг"))
        self.add_item(discord.ui.InputText(label="Описание бага", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Ваш ответ")
        embed.add_field(name="Команда", value=self.children[0].value)
        embed.add_field(name="Описание", value=self.children[1].value)
        await interaction.response.send_message(embeds=[embed])
        await self.bot.get_user(969853884535283742).send(embed = embed)
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def botinfo(self, ctx: commands.Context):
        embed = discord.Embed(
            title = f"Информация о Боте {self.bot.user.name}!",
            description = f"http://goldybot.gq \nВладельцы бота:  <@{goldy}> и <@{self.bot.owner_id}> \nБот создан: \n{self.bot.user.created_at} \nВ боте обновления каждый день!")
        await ctx.send(embed = embed)
    @commands.command()
    async def botcommands(self, ctx: commands.Context):
        cmnds = '\n- '.join([c.name for c in self.bot.commands])
        await ctx.send(f"```\n{cmnds}\n```")
    @bridge.bridge_command(name = 'ping', description = "Задержка бота")
    async def ping(self, ctx: bridge.BridgeContext):
        await ctx.respond(f'Задержка бота: {round(self.bot.latency*1000)/1000} секунд')
    @bridge.bridge_command(name = 'help', description = 'Меню помощи')
    async def help(self, ctx: bridge.BridgeContext):
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


        await ctx.respond(embed = emb, view = help.SelectView())
    @commands.slash_command()
    async def bug(self, ctx: discord.ApplicationContext):
        modal = MyModal(bot = self.bot, title = 'Bug')
        await ctx.send_modal(modal)
def setup(bot):
    bot.add_cog(Info(bot))
