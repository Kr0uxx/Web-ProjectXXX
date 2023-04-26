import openai
from requests.exceptions import ReadTimeout
from openai.error import RateLimitError, InvalidRequestError
import telebot
from telebot import types
from datetime import datetime

from functions import gpt_func

# ОБЯЗАТЕЛЬНО НАДО БУДЕТ ЗАПУСТИТЬ spec-scrip.py


# Предоставляем ключ API 
bot = telebot.TeleBot('6135465665:AAFpRJAuVon1O2oBdvIuwFvV6yAqKHrR08k')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("👋")
    markup.add(btn1)

    bot.send_message(message.from_user.id,
                     "👋 Привет! Я бот, сделанный специально для проекта по WEB'у, у меня есть AI и не только!",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок

        btn1 = types.KeyboardButton('🖥')
        btn2 = types.KeyboardButton('👪')
        btn3 = types.KeyboardButton('❓')
        btn4 = types.KeyboardButton('🌤')
        btn5 = types.KeyboardButton('⌚️')

        markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.from_user.id, 'Жду Ваши вопросы 😉', reply_markup=markup)  # ответ бота

    elif message.text == '🖥':
        bot.send_message(message.from_user.id,
                         'Вот ссылка на наш гит - ' + '[WEB-PROJECT](https://github.com/Kr0uxx/Web-ProjectXXX)',
                         parse_mode='Markdown')

    elif message.text == '👪':
        bot.send_message(message.from_user.id,
                         'Начнем с моего первого и главного отца - ' + '[Артема](https://github.com/YL-bot)' + '. Потом стоит упоминуть второго папу, по совместительству тим-лида - ' + '[Максим](https://github.com/Kr0uxx)' + ' . Ну и, конечно же, главная и единственная женщина команды - ' + '[Екатерина](https://github.com/katiarapter)',
                         parse_mode='Markdown')

    elif message.text == '❓':
        bot.send_message(message.from_user.id,
                         'Ну вообще 06.03.2023 я писался как хотелка Артема вопреки остальным тимейтам. Chat-GPT, хайп и все дела. Но я активно развиваюсь сейчас, стану выполнять такие же функции, как и наш проектный сайт!',
                         parse_mode='Markdown')

    elif message.text == '🌤':
        bot.send_message(message.from_user.id, )
        bot.send_message(message.from_user.id, '...ищем данные у наших источников...', parse_mode='Markdown')
        bot.send_message(message.from_user.id, '...смотрим гугл...', parse_mode='Markdown')
        bot.send_message(message.from_user.id, gpt_func.ask('Погода сегодня', 0), parse_mode='Markdown')

    elif message.text == '⌚️':
        bot.send_message(message.from_user.id, '...лезем на Сикстинскую капеллу ради Вас...', parse_mode='Markdown')

        now = datetime.now()
        bot.send_message(message.from_user.id, now.strftime("%d/%m/%Y %H:%M:%S"), parse_mode='Markdown')

    else:
        bot.send_message(message.from_user.id, '...запрос обрабатывается, подождите...', parse_mode='Markdown')
        bot.send_message(message.from_user.id, gpt_func.ask(message.text, 1), parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
