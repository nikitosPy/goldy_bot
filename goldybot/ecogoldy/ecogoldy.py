import disnake as discord
from disnake.ext import commands

import sqlite3
from config import *
from Cybernator import Paginator as pag

connection = sqlite3.connect('server.db')
cursor = connection.cursor()
class EcoGoldy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            id INT,
            cash BIGINT,
            rep INT,
            lvl INT,
            server_id INT
        )""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS shop (
            role_id INT,
            id INT,
            cost BIGINT
        )""")

        for guild in self.bot.guilds:
            for member in guild.members:
                if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                    cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, 1, {guild.id})")
                else:
                    pass

        connection.commit()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
            cursor.execute(f"INSERT INTO users VALUES ('{member}', {member.id}, 0, 0, 1, {member.guild.id})")
            connection.commit()
        else:
            pass


    @commands.command(aliases = ['balance', 'cash'])
    async def __balance(self, ctx: commands.Context, member: discord.Member = None):
        if member is None:
            await ctx.send(embed = discord.Embed(
                description = f"""Баланс пользователя **{ctx.author}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]} :leaves:**"""
            ))
            
        else:
            await ctx.send(embed = discord.Embed(
                description = f"""Баланс пользователя **{member}** составляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(member.id)).fetchone()[0]} :leaves:**"""
            ))  

    @commands.command(aliases = ['add-shop'])
    async def __add_shop(self, ctx: commands.Context, role: discord.Role = None, cost: int = None):
        if role is None:
            await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете внести в магазин")
        else:
            if cost is None:
                await ctx.send(f"**{ctx.author}**, укажите стоимость для данной роли")
            elif cost < 0:
                await ctx.send(f"**{ctx.author}**, стоимость роли не может быть такой маленькой")
            else:
                cursor.execute("INSERT INTO shop VALUES ({}, {}, {})".format(role.id, ctx.guild.id, cost))
                connection.commit()

                await ctx.message.add_reaction('✅')

    @commands.command(aliases = ['shop'])
    async def __shop(self, ctx: commands.Context):
        embed = discord.Embed(title = 'Магазин ролей')

        for row in cursor.execute("SELECT role_id, cost FROM shop WHERE id = {}".format(ctx.guild.id)):
            if ctx.guild.get_role(row[0]) != None:
                embed.add_field(
                    name = f"Стоимость **{row[1]} :leaves:**",
                    value = f"Вы приобрете роль {ctx.guild.get_role(row[0]).mention}",
                    inline = False
                )
            else:
                pass

        await ctx.send(embed = embed)


    @commands.command(aliases = ['buy', 'buy-role'])
    async def __buy(seelf, ctx: commands.Context, role: discord.Role = None):
        if role is None:
            await ctx.send(f"**{ctx.author}**, укажите роль, которую вы желаете приобрести")
        else:
            if role in ctx.author.roles:
                await ctx.send(f"**{ctx.author}**, у вас уже имеется данная роль")
            elif cursor.execute("SELECT cost FROM shop WHERE role_id = {}".format(role.id)).fetchone()[0] > cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]:
                await ctx.send(f"**{ctx.author}**, у вас недостаточно средств для покупки данной роли")
            else:
                await ctx.author.add_roles(role)
                cursor.execute("UPDATE users SET cash = cash - {} WHERE id = {}".format(cursor.execute("SELECT cost FROM shop WHERE role_id = {}".format(role.id)).fetchone()[0], ctx.author.id))
                connection.commit()

                await ctx.message.add_reaction('✅')


    @commands.command(aliases = ['like'])
    async def __like(self, ctx: commands.Context, member: discord.Member = None):
        if member is None:
            await ctx.send(f"**{ctx.author}**, укажите участника сервера")
        else:
            if member.id == ctx.author.id:
                await ctx.send(f"**{ctx.author}**, вы не можете указать самого себя")
            else:
                cursor.execute("UPDATE users SET rep = rep + {} WHERE id = {}".format(1, member.id))
                connection.commit()

                await ctx.message.add_reaction('✅')


    @commands.command(aliases = ['leaderboard', 'lb'])
    async def __leaderboard(self, ctx: commands.Context):
        embed = discord.Embed(title = 'Топ 10 сервера')
        counter = 0

        for row in cursor.execute("SELECT name, cash FROM users WHERE server_id = {} ORDER BY cash DESC LIMIT 10".format(ctx.guild.id)):
            counter += 1
            embed.add_field(
                name = f'# {counter} | `{row[0]}`',
                value = f'Баланс: {row[1]}',
                inline = False
            )

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(EcoGoldy(bot))