import discord
from discord.ext.commands import Context, Cog
from discord.ext import commands, bridge
from gtts import gTTS
import os
from asyncio import sleep
from os.path import exists
from pathlib import Path

async def finished_callback(sink, channel: discord.TextChannel, *args):
    recorded_users = [f"<@{user_id}>" for user_id, audio in sink.audio_data.items()]
    await sink.vc.disconnect()
    files = [
        discord.File(audio.file, f"{user_id}.{sink.encoding}")
        for user_id, audio in sink.audio_data.items()
    ]
    await channel.send(
        f"Finished! Recorded audio for {', '.join(recorded_users)}.", files=files
    )

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
  
  @commands.command()
  async def start(self, ctx: commands.Context):
      """
      Record your voice!
      """
      voice = ctx.author.voice

      if not voice:
          return await ctx.respond("You're not in a vc right now")

      vc = await voice.channel.connect()
      connections.update({ctx.guild.id: vc})

      vc.start_recording(
          discord.sinks.MP3Sink(),
          finished_callback,
          ctx.channel,
      )

      await ctx.respond("The recording has started!")

  @commands.command()
  async def stop(self, ctx: commands.Context):
      """Stop recording."""
      if ctx.guild.id in connections:
          vc = connections[ctx.guild.id]
          vc.stop_recording()
          del connections[ctx.guild.id]
          await ctx.delete()
      else:
          await ctx.respond("Not recording in this guild.")
def setup(bot):
  bot.add_cog(Voice(bot))
