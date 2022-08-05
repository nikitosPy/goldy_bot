from distutils import extension
import disnake as discord #Создание Клиента
from disnake.utils import get #Поиск канала
from disnake.ext import commands #Команды
import requests, bs4
class Google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def google(self, ctx: commands.Context, *, text: str):
        url = 'https://google.com/search?q=' + text
  
# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
        request_result=requests.get( url )
  
# Creating soup from the fetched request
        soup = bs4.BeautifulSoup(request_result.text,"html.parser")
        filter=soup.find_all()
        for i in range(0,len(filter)):
            await ctx.send(filter[i].get_text())

def setup(bot):
    bot.add_cog(Google(bot))
