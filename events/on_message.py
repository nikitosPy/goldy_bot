import disnake as discord
from disnake.ext import commands
from time import time
from config import *
from rapidfuzz import fuzz, process
class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        
        admin1 = self.bot.get_user(self.bot.owner.id)
        admin2 = self.bot.get_user(goldy)
        if message.author == self.bot.user: 
            return
        elif self.bot.user.mention in message.content:
            await message.channel.send(f"""
    Привет! Я бот {self.bot.user.name}!
    В данный момент Бот на ОБТ (открытом бета-тестировании)
    Если возникнут вопросы / пожелания / идеи - 
    Пишите в Л / С и я это передам моим админам.
    Я многофункциольный :smiley:
    """)
        for wel in welcome:
            if wel in str(message.content).lower():
                await message.channel.send(f"И тебе {wel}, дорогой <@{message.author.id}>!")
                break
        for b in bad_words:
            for content in str(message.content).lower().split():
                difference = process.extractOne(content, b)
                if difference[1] >= 90:
                    await message.channel.purge(limit = 1)
                    await message.channel.send(f"<@{message.author.id}>, Не матерись! || Админы, он сказал: {message.content}, я подумал что {difference[0]} ||")
                    break
        for ping in pings:
            if ping in str(message.content).lower():
                await message.channel.purge(limit = 1)
                await message.channel.send(f"Не упоминай пинги everyone и here")
                break
        elif isinstance(message.channel,discord.DMChannel): 
            for pref in prefix:
                if not message.content.startswith(pref):
                    await message.channel.send("Отчёт отправлен!")
                    await admin1.send(f'\nТебе отправили отчёт в <t:{round(time())}:F>! \nПрочти его! \nОтчёт от {message.author.name} \n{message.content}')
                    await admin2.send(f'\nТебе отправили отчёт в <t:{round(time())}:F>! \nПрочти его! \nОтчёт от {message.author.name} \n{message.content}')
                    break
        
def setup(bot):
    bot.add_cog(Message(bot))
