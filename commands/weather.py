import disnake as discord
from disnake.ext import commands
import asyncio
from config import owm_token
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM(owm_token, config_dict)
mgr = owm.weather_manager()
class Weather(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
  @commands.command()
  async def weather(ctx: commands.Context, city): 
      observation = mgr.weather_at_place(city)
      w = observation.weather
      t = w.temperature("celsius")
      t1 = t['temp']
      t2 = t['feels_like']
      t3 = t['tem_max']
      t4 = t['temp_min']
      wi = w.wind()['speed']
      humi = w.humidity
      cl = w.clouds
      st = w.status
      dt = w.detailed_status
      ti = w.reference_time('iso')
      pr = w.pressure['press']
      vd = w.visibility_distance
      
      value = "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"Максимальная температура " + str(t3) + " °C" +"\n" + 
				"Минимальная температура " + str(t4) + " °C" + "\n" + 
				"Ощущается как" + str(t2) + " °C" + "\n" +
				"Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"Давление " + str(pr) + " мм.рт.ст" + "\n" + 
				"Влажность " + str(humi) + " %" + "\n" + 
				"Видимость " + str(vd) + "  метров" + "\n" +
				"Описание " + str(st) + "\n\n" + str(dt))
      await ctx.send(value)

def setup(bot):
  bot.add_cog(Weather(bot))
