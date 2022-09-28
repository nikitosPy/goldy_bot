import discord
from discord.ext.commands import Context, Cog
from discord.ext import commands, bridge
from gtts import gTTS
class Voice(Cog):
  def __init__(self, bot):
    self.bot = bot
  @bot.command()
  async def play (ctx, *, text1):    
      os.remove('text.mp3')
      tts = gTTS(text = text1, lang = 'ru')
      tts.save('text.mp3')
      voice_channel = ctx.author.channel
      channel = None
      if voice_channel != None:
          channel = voice_channel.name
          vc = await voice_channel.connect()    
          vc.play(discord.FFmpegPCMAudio(source='text.mp3')       
          while vc.is_playing():
              sleep(1)
          await vc.disconnect()
      else:
          await ctx.send(str(ctx.author.name) + "is not in a channel.")
      await ctx.send('Конец')
def setup(bot):
  bot.add_cog(Voice(bot))
