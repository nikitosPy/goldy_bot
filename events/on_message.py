import discord, asyncio
from discord.ext import commands
from time import time
from config import *
import random
import sqlite3
from rapidfuzz import fuzz, process
class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener('on_message')
    async def on_message1(self, message):
        admin1 = self.bot.get_user(self.bot.owner_id)
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
        for content in str(message.content).lower().split():
            difference = process.extractOne(content, bad_words)
            if difference[1] >= 90:
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
    @commands.Cog.listener('on_message')  # equivalent to discord.Event
    async def on_message2(self, message):

        if type(message.channel) == discord.DMChannel:
            user = message.author
            guild_id = 1011998830411141150 # fill it up with your support guild id
            support_server = self.bot.get_guild(guild_id)

            # try to match with a channel name
            match = False

            for channel in support_server.text_channels:
                await asyncio.sleep(0)

                if channel.name == user.name.lower():  # it's a match
                    match = True
                    user_support = get(support_server.text_channels, name = user.name.lower())  # get the user support channel as lower case, just like channels name
                    break

            # end for

            if not match:  # if the channel doesn't exist, we create it

                support_category_name = 'Support'  # defines the Support category name, case sensitive
                support_category = get(support_server.categories, name = support_category_name)  # get the support category
                user_support = get(support_server.text_channels, name = user.name.lower())  # get the user support channel as lower case, just like channels name

                if support_category == None:  # if the category is not found, we create it
                    # setting up the category permissions
                    support_category_permissions = {
                        support_server.default_role : discord.PermissionOverwrite(send_messages = False)
                    }

                    await support_server.create_category(name = support_category_name, overwrites = support_category_permissions)

                    support_category = get(support_server.categories, name = support_category_name)  # redefine the variable with the new category

                if user_support == None:  # if the channel doesn't exist

                    # setting up the permissions for the channel
                    user_channel_permissions = {
                        support_server.default_role : discord.PermissionOverwrite(read_messages = False, send_messages = False),  # othe users cannot see the channels
                        support_server.me : discord.PermissionOverwrite(read_messages = True, send_messages = True),
                        user : discord.PermissionOverwrite(read_messages = True, send_messages = True)
                    }

                    # now we create the channel
                    await support_server.create_text_channel(name = user.name, overwrites = user_channel_permissions, category = support_category)
                    user_support = get(support_server.text_channels, name = user.name.lower())  # redefine the support channel

            # now send the message to the new channel
            await user_support.send(message.content)  # sends what the user sent to the command
def setup(bot):
    bot.add_cog(Message(bot))
