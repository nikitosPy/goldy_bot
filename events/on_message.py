import disnake as discord
from disnake.ext import commands
from time import time
from config import *
import random
import sqlite3
from rapidfuzz import fuzz, process
class Message(commands.Cog):
    global admin_connected
    admin_connected = False
    connection = sqlite3.connect('ecogoldy/server.db')
    cursor = connection.cursor()
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ticket(self, ctx: commands.Context):
        channel = await ctx.guild.create_text_channel(f"ticket")
        admin_connected = True
    @commands.command()
    async def close(self, ctx: commands.Context):
        await discord.utils.get(ctx.guild.channels, name=f"ticket").delete()
        admin_connected = False
    @commands.Cog.listener()
    async def on_message(self, message):
        exp = random.randint(10, 100)
        cursor.execute("UPDATE users SET lvl = lvl + {} WHERE id = {}".format(exp, message.author.id))
        connection.commit()
        await ctx.send(cursor.execute("SELECT lvl FROM users WHERE id = {}".format(message.author.id).fetchone())
        admin1 = self.bot.get_user(self.bot.owner.id)
        admin2 = self.bot.get_user(goldy)
        if message.author == self.bot.user: 
            return
        elif isinstance(message.channel,discord.DMChannel):
            if admin_connected:
                channel = discord.utils.get(self.bot.get_all_channels(), name="ticket")
                await channel.send(f"**{message.author.name}**: {message.content}")
            else:
                await message.channel.send("Создаю сессию...")
                global amogus
                amogus = message.author.id
                await message.channel.send(f"Вы создали тикет. Ожидайте связи с оператором")  
            
        elif message.channel.name.startswith("ticket"):
            try:
              await self.bot.get_user(amogus).send(f"**{message.author.name}**: {message.content}")
            except:
              pass
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
        for content in str(message.content).lower().split():
            difference = process.extractOne(content, bad_words)
            if difference[1] >= 95:
                await message.channel.purge(limit = 1)
                await message.channel.send(f"<@{message.author.id}>, Не матерись! || Админы, он сказал: {message.content}, я подумал что {difference[0]}, Шанс: {difference[1]} ||")
                break
        content = str(message.content).lower()
        if "как дела" in content:
            result = ["У меня нормально, а у тебя?", "К сожаленью плохо :(", "Всё супер!"]
            await message.channel.send(random.choice(result))

        for bye in ends:
            if bye in str(message.content).lower():
                await message.channel.send(f"И тебе {bye}, дорогой <@{message.author.id}>!")
                break
        for ping in pings:
            if ping in str(message.content).lower():
                await message.channel.purge(limit = 1)
                await message.channel.send(f"Не упоминай пинги everyone и here")
                break
def setup(bot):
    bot.add_cog(Message(bot))
