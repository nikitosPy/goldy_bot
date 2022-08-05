from distutils import extension
import disnake as discord #Создание Клиента
from disnake.utils import get #Поиск канала
from disnake.ext import commands #Команды

from config import * #Ключи
from asyncio import sleep #Режим ожидания

import requests #Загрузка Аватара
from PIL import Image, ImageDraw, ImageFont, ImageOps #Создание изображений
import io #Просмотр Аватара

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def user(self, ctx: commands.Context):
        
        await ctx.channel.purge(limit = 1)
        img = Image.open(fp = "user.jpg")
        
        url = str(ctx.author.avatar.url)[:-10]
        response = requests.get(url, stream = True)
        response = Image.open(io.BytesIO(response.content))
        response = response.convert('RGBA')
        response = response.resize((100, 100), Image.ANTIALIAS)
        img.paste(response, (0, 0, 115, 115))
        idraw = ImageDraw.Draw(img)
        name = ctx.author.name 
        tag = ctx.author.discriminator 
        font = "font.ttf"
        headline = ImageFont.truetype(font, size = 20)
        undertext = ImageFont.truetype(font, size = 12)
        idraw.text((145, 15), f'{name}#{tag}', font = headline) 
        idraw.text((145, 50), f'ID: {ctx.author.id}', font = undertext)
        filename = 'usercard.png'
        img.save(filename)
        await ctx.send(file = discord.File(fp = filename))
        os.remove(filename)
        
def setup(bot):
    bot.add_cog(User(bot))