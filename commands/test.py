import disnake as discord
from disnake.ext import commands
from disnake.ui import Button
class Test(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @bot.command()
  async def test(ctx):
    await ctx.send('Hello World!', view=View(
        Button(custom_id='button1', label='WOW button!', style=discord.ButtonStyle.green)
        ))
    interaction = await bot.wait_for('interaction', check=lambda i: i.custom_id == 'button1')
    await interaction.response.edit_message(content='Button clicked!', view=None)
def setup(bot):
  bot.add_cog(Test(bot))
