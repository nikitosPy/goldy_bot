import discord
from discord.ext.commands import Context, Cog
from discord.ext import commands, bridge
from gtts import gTTS
import os
from asyncio import sleep
from os.path import exists
from pathlib import Path
class Voice(Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def say(self, ctx: commands.Context, *, text1):   
      tts = gTTS(text = text1, lang = 'ru')
      tts.save('text.mp3')
      voice_channel = ctx.author.voice.channel
      channel = None
      if voice_channel != None:
          channel = voice_channel.name
      if ctx.voice_client is None:
            vc = await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
            vc = ctx.voice_client 
         
      audio = discord.FFmpegPCMAudio(source='text.mp3')
      vc.play(audio)
      while vc.is_playing():
          sleep(.1)
      await vc.disconnect()
      await ctx.send('Конец')
def setup(bot):
  bot.add_cog(Voice(bot))
