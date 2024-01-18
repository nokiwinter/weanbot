import telebot
from openai import OpenAI
import time


 # await ctx.send('```!ai - !аи  |  Использовать ИИ. (Пример: !ai как дела? | Вывод: 🤔💭👍)```')

client = OpenAI(api_key='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')
bot = telebot.TeleBot('6719369577:AAG5oC6ajaPsb2C8IvJhc1Ugl6a5iAze5ps')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет *{message.from_user.first_name}*! 👋🤖\n'
    mess2 = f'*Что я умею?* ✨\n\n⋅ Отвечать на вопросы с использованием смайликов.\n⋅ Переводить тексты на разные языки.\n⋅ Помогать в написании кода.\n⋅ Создавать тексты по запросу.\n⋅ Предоставлять помощь с уроками и обучением.\n⋅ Выполнять поиск информации по заданным запросам.\n⋅ Чтобы узнать список комамд, просто введи *"/help"* 🤖🌐'
    bot.send_message(message.chat.id, mess, parse_mode= "Markdown")
    bot.send_message(message.chat.id, mess2, parse_mode= "Markdown")

@bot.message_handler(commands=['help'])
def help(message):
    mess_help = f'*/ai* | Класичный ИИ 🤖 _(Использование: /ai Привет!)_\n*/emoji* | ИИ отвечает в емодзи ✨ _(Использование: /emoji Привет!)_'
    bot.send_message(message.chat.id, mess_help, parse_mode= "Markdown")

@bot.message_handler(commands=['emoji'])
def emoji(message):
    result = str(message)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a message, and your task is to respond using emojis only."
        },
        {
        "role": "user",
        "content": result
        }
    ],
    temperature=0.8,
    max_tokens=64,
    top_p=1
    )
    print(f'{result} {response}')
    bot.send_message(message.chat.id, response.choices[0].message.content, parse_mode= "html")


@bot.message_handler(commands=['ai'])
def ai(message):
    result2 = str(message)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0301",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a message, and your task is to respond."
        },
        {
        "role": "user",
        "content": result2
        }
    ],
    temperature=0
    )
    print(f'{result2} {response}')
    bot.send_message(message.chat.id, response.choices[0].message.content, parse_mode="html")


bot.polling(none_stop=True)
