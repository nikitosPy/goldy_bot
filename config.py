import disnake as discord
import os
from disnake.ext import commands
from typing import List
prefix = ["gg.", "gg!", "gb.", "gb!"]
with open("token.txt") as f:
        token = f.read()
intents = discord.Intents.all()
logs_ch = 998598317774737409
owm_token = 'eb46d4ac80206870cb7641bbed4afb0c'
statuses = [
        "Привет! Я GoldyBot || gg.help", 
        "Хм... Зачем ты это читаешь?", 
        "Факт Дня: У меня ежедневные обновления!", 
        "Факт Недели: У Бота есть сайт: goldymine.tk",
        "Главное в Боте - его производительность...",
        "Факт дня: я был создан [ТАБ]LET[04]KA и MrGoldy",
        "Хотите шутку? А шутка вас нет", 
        "Бот вряд ли будет переведён на другие языки", 
        "MrGoldy Не делал бота, лишь командовал"
        ]
goldy = 902168323557589012
bad = "сука тварь гнида лох ахуел гнида хуй блять"
bad_words = bad.split()
pings = ["@everyone", "@here"]
cmds = []
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        cmds.append(f"{filename[:-3]}")
welcome = [ "приветик", "привет",  "здравствуйте", "здравствуй", "добрый день", "доброе утро", "добрый вечер"]
def log(args):
        with open("logs.txt", "a+") as l:
                l.write(f"\nИспользована команда {args}")
ends = ["пока", "до завтра", "прощай", "до свидания"]

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
