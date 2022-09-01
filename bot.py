print("Запуск...") 
try: 
    import disnake as discord #Создание Клиента
    from disnake.ext import commands #Команды
    from config import * #Ключи
    import os #Тоже генераторы
    import logging
    from typing import List
except:
    os.system("pip install -r requirements.txt")
bot = commands.Bot(command_prefix = prefix, intents = intents, case_insensitive = True)
bot.remove_command("help")
client = discord.Client()
#Создание бота
### ?
#Логи disnake
logger = logging.getLogger('disnake')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Reload
@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == bot.owner.id:
        bot.unload_extension(f"commands.{extension}")
        bot.load_extension(f"commands.{extension}")
        await ctx.send(f"Обновлен cog {extension}!")
    else:
        await ctx.send("Не похож ты на моего разработчика...")

class TicTacToeButton(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int):
        super().__init__(style=discord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = discord.ButtonStyle.danger
            self.label = 'X'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = 'O'
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = 'X won!'
            elif winner == view.O:
                content = 'O won!'
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)

class TicTacToe(discord.ui.View):
    # This tells the IDE or linter that all our children will be TicTacToeButtons
    # This is not required
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None

@bot.command()
async def tic(ctx: commands.Context):
    await ctx.send('Tic Tac Toe: X goes first', view=TicTacToe())

        
with open("logs.txt", "a+") as f:
    f.write("\n")

for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"commands.{filename[:-3]}")

for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        bot.load_extension(f"events.{filename[:-3]}")

for filename in os.listdir("./ecogoldy"):
    if filename.endswith(".py"):
        bot.load_extension(f"ecogoldy.{filename[:-3]}")

#Запуск
bot.run(token)

