import openai 
from requests.exceptions import ReadTimeout
from openai.error import RateLimitError, InvalidRequestError
import telebot
from telebot import types



# Предоставляем ключ API 
openai.api_key = "Your_Key"
bot = telebot.TeleBot('6135465665:AAFpRJAuVon1O2oBdvIuwFvV6yAqKHrR08k')


def ask(prompt): # def которая отвечает за получение ответа , чтобы задать вопрос ask('вопрос')
    completion = openai.Completion.create(engine="text-davinci-003", 
                                          prompt=prompt, 
                                          temperature=0.5, 
                                          max_tokens=1000)
    
    answ = completion.choices[0]['text']
    answer = f'Ответ на вопрос <{prompt}>:\n\n{answ}'
    
    return answer


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    
    bot.send_message(message.from_user.id, "👋 Привет! Я бот, сделанный специально для проекта по WEB'у, во мне есть chat-gpt!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        
        btn1 = types.KeyboardButton('🖥')
        btn2 = types.KeyboardButton('👪')
        btn3 = types.KeyboardButton('❓')
        
        markup.add(btn1, btn2, btn3)
        
        bot.send_message(message.from_user.id, 'Жду Ваши вопросы 😉', reply_markup=markup) #ответ бота
        
    elif message.text == '🖥':
        bot.send_message(message.from_user.id, 'Вот ссылка на наш гит - ' + '[WEB-PROJECT](https://github.com/Kr0uxx/Web-ProjectXXX)', parse_mode='Markdown')

    elif message.text == '👪':
        bot.send_message(message.from_user.id, 'Начнем с моего первого и главного отца - ' + '[Артема](https://github.com/YL-bot)' + '. Потом стоит упоминуть второго папу, по совместительству тим-лида - ' + '[Максим](https://github.com/Kr0uxx)' + ' . Ну и, конечно же, главная и единственная женщина команды - ' + '[Екатерина](https://github.com/katiarapter)', parse_mode='Markdown')

    elif message.text == '❓':
        bot.send_message(message.from_user.id, 'Ну вообще 06.03.2023 я писался как хотелка Артема вопреки остальным тимейтам. Chat-GPT, хайп и все дела. Но я активно развиваюсь сейчас, стану выполнять такие же функции, как и наш проектный сайт!', parse_mode='Markdown') 
        
    else:
        bot.send_animation(message.from_user.id, ask(message.text), parse_mode='Markdown')
        



bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть        