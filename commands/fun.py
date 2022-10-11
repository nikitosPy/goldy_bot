import discord
from discord.ext import commands, bridge
import json, aiohttp
joke = 'https://geek-jokes.sameerkumar.website/api?format=json'
from translate import Translator
from easy_pil import Editor, load_image, Font
from asyncio import sleep
translator= Translator(to_lang="ru")
codes = ['test']
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @bridge.bridge_command(name = "joke", description = "Шутка")
    async def joke(self, ctx: bridge.BridgeContext):
        jokes = []
        async with aiohttp.ClientSession() as cs:
            for i in range(5):
                async with cs.get(joke) as r:
                    if r.status == 200:
                        js = await r.json()
                        joke_t = translator.translate(js['joke'])
                        jokes.append(joke_t)
                await ctx.respond('\n'.join(jokes))
    @commands.command()
    async def code(self, ctx: commands.Context):
        def is_valid_guess(m: discord.Message):
            return m.author == ctx.author and m.content.lower() in codes
        try:
            guess: discord.Message = await self.bot.wait_for("message", check=is_valid_guess, timeout=30.0)
        except TimeoutError:
            return await ctx.send_followup(f"Тут есть кто живой?")
        if guess.content.lower() in codes:
            await guess.reply("Вы угадали!", mention_author=True)
        else:
            await guess.reply(f"Вы не угадали!", mention_author=True)
    @commands.command()
    async def random(self, ctx: commands.Context):
        await ctx.send(f'Случайное число от 0 до 1000: \n{random.randint(0,1001)}')
    @commands.command()
    async def role(self, ctx: commands.Context):
        role = discord.utils.get(ctx.guild.roles,name=ctx.author.name) 
        if role not in ctx.guild.roles:
            await ctx.guild.create_role(name = ctx.author.name)
        role = discord.utils.get(ctx.guild.roles, name = ctx.author.name)
        await role.edit(colour=discord.Color.random())
        await ctx.message.author.add_roles(role) 
        await ctx.send("Вам выдана персональная роль на 5 минут")
        await sleep(300)
        await ctx.message.author.remove_roles(role)
        await role.delete()
        
    @commands.command()
    async def coin(self, ctx: commands.Context):
        rand = random.randrange(0,2)
        if rand == 0:
            coin = "Орёл"
            file = "coin1.jpg"
        else:
            coin = "Решка"
            file = "coin2.jpg"
        await ctx.send(embed = discord.Embed(title = f"Я подбросил монетку и получил: {coin}"))
        await ctx.send(file = discord.File(file))
        
    @commands.command()
    async def user(self, ctx: commands.Context):
        background = Editor("wlcbg.jpg")
        profile_image = load_image(str(ctx.author.avatar.url))
        profile = Editor(profile_image).resize((150, 150)).circle_image()

        poppins = Font.poppins(size=50, variant="bold")
        poppins_small = Font.poppins(size=25, variant="regular")
        poppins_light = Font.poppins(size=20, variant="light")

        background.paste(profile, (325, 90))
        background.ellipse((325, 90), 150, 150, outline="gold", stroke_width=4)
        background.text((400, 260), "WELCOME", color="white", font=poppins, align="center")
        background.text(
    (400, 325), ctx.author.name, color="white", font=poppins_small, align="center"
)
        background.text(
    (400, 360),
    "You are the Member",
    color="#0BE7F5",
    font=poppins_small,
    align="center",
)
        await ctx.send(file = discord.File(fp=background.image_bytes, filename = 'user.png'))
        
def setup(bot):
    bot.add_cog(Fun(bot))
