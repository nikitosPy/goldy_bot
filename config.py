import disnake as discord
import os
prefix = "gg."
token =  'OTk0MjA5MzkyNTY2MjEwNTYw.GCDu3r.0yElEovGc991fo64-dAONQa9qVVvIAJlDj9sPw'
intents = discord.Intents.all()
logs_ch = 998598317774737409
statuses = statuses = [
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
ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }
cmds = []
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        cmds.append(f"{filename[:-3]}")
for filename in os.listdir("./events"):
    if filename.endswith(".py"):
        cmds.append(f"{filename[:-3]}")