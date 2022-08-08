import disnake as discord
from disnake.ext import commands
from time import time
from config import *
class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        admin1 = self.bot.get_user(self.bot.owner.id)
        admin2 = self.bot.get_user(goldy)
        if message.author == self.bot.user: 
            return
        if self.bot.user.mention in message.content:
            await message.channel.send(f"""""")
        
        
        if isinstance(message.channel,discord.DMChannel): 
            await message.channel.send("Отчёт отправлен!")
            await admin1.send(f'\nТебе отправили отчёт в <t:{round(time())}:F>! \nПрочти его! \nОтчёт от {message.author.name} \n{message.content}')
            await admin2.send(f'\nТебе отправили отчёт в <t:{round(time())}:F>! \nПрочти его! \nОтчёт от {message.author.name} \n{message.content}')
def setup(bot):
    bot.add_cog(Message(bot))
