import disnake as discord
import os

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
