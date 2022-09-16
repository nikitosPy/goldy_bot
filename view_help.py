
import discord
from discord.ext import commands
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Весёлости",emoji="😜",description="Ура! Весело!"),
            discord.SelectOption(label="Полезные Функции",emoji="🤔",description="Очень полезные!"),
            discord.SelectOption(label="Экономика",emoji= "💰",description="Команды для бизнеса!")
            ]
        super().__init__(placeholder="Выберите категорию...",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Весёлости":
            await interaction.response.send_message("Команды веселья!", ephemeral=True)
        elif self.values[0] == "Полезные Функции":
            await interaction.response.send_message("Полезные функции!",ephemeral=True)
        elif self.values[0] == "Экономика":
            await interaction.response.send_message("Бизнес!",ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 100):
        super().__init__(timeout=timeout)
        self.add_item(Select())
