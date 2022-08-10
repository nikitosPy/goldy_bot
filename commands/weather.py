import disnake as discord
from disnake.ext import commands
import pyowm
from config import owm_token
owm = pyowm.OWM(owm_token)
mgr = owm.weather_manager()
class Weather(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def weather(ctx: commands.Context, city: str):
     try:
            
            observation = mgr.weather_at_place(message.text)
            w = observation.weather
            oblaka = w.clouds
            temp = w.temperature('celsius')["temp"]
            vlazhnost = w.humidity

            answer = 'В городе ' + message.text + ' сейчас ' + w.detailed_status + '\n'
            answer += 'Температура ' + ' - ' + str(temp) + ' градусов' + '\n'
            if temp < 10:
                answer += 'Сейчас на улице очень холодно.Лучше сиди дома!'
            if temp < 20:
                answer += 'Воздух снаружи холодный.Одевайся теплее!'
            else:
                answer += 'Температура норм. Ходи в чем хочешь!'
            await ctx.send(answer)
        except:
            await ctx.send("Такого города не существует.")
