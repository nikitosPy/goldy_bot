import discord
from discord.ext import commands
class Panel(discord.ui.View):
    def __init__(self, bot, *args, **kwargs):
      self.bot = bot
      super().__init__(*args, **kwargs)
    @discord.ui.button(label = 'botinfo', style = discord.ButtonStyle.primary)
    async def botinfo(self, button, interaction):
        embed = discord.Embed(
            title = f"Информация о Боте {self.bot.user.name}!",
            description = f"http://goldybot.gq \nВладельцы бота:  <@{goldy}> и <@{self.bot.owner_id}> \nБот создан: \n{self.bot.user.created_at} \nВ боте обновления каждый день!")
        await interaction.response.send(embed = embed)
