import discord
from discord.ext.commands import Context, Cog
from discord.ext import commands, bridge
from gtts import gTTS
import os
from os.path import exists
from pathlib import Path
class Voice(Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def play(self, ctx: commands.Context, *, text1):    
      if exists('text.mp3'):
        os.remove('text.mp3')
      tts = gTTS(text = text1, lang = 'ru')
      tts.save('text.mp3')
      voice_channel = ctx.author.voice.channel
      channel = None
      if voice_channel != None:
          channel = voice_channel.name
          vc = await voice_channel.connect()    
          ffmpeg = Path(__file__).parent
          audio = discord.FFmpegPCMAudio(executable = f'{ffmpeg}/ffmpeg.exe', source='text.mp3')
          vc.play(audio)
          while vc.is_playing():
              sleep(1)
          await vc.disconnect()
      else:
          await ctx.send(str(ctx.author.name) + "is not in a channel.")
      await ctx.send('Конец')
def setup(bot):
  bot.add_cog(Voice(bot))
