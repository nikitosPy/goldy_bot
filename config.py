import discord
import os
from discord.ext import commands
from typing import List

prefix = ["gg.", "gg!", "gb.", "gb!"]
token = os.getenv('TOKEN')
intents = discord.Intents.all()
logs_ch = 998598317774737409

statuses = [
        "Привет! Я GoldyBot || gg.help", 
        "Хм... Зачем ты это читаешь?", 
        "Факт Дня: У меня ежедневные обновления!", 
        "Факт Недели: У Бота есть сайт: goldybot.gq",
        "Главное в Боте - его производительность...",
        "Факт дня: я был создан Avo_cado и Boyfriend",
        "Хотите шутку? А шутка вас нет", 
        "Бот вряд ли будет переведён на другие языки", 
        "Boyfriend Не делал бота, лишь командовал"
        ]
goldy = 902168323557589012

bad = "сука тварь гнида лох ахуел гнида хуй блять"
bad_words = bad.split()
pings = ["@everyone", "@here"]

welcome = [ "приветик", "привет",  "здравствуйте", "здравствуй", "добрый день", "доброе утро", "добрый вечер"]
ends = ["пока", "до завтра", "прощай", "до свидания"]

