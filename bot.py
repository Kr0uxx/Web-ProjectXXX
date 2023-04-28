from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
from functions import gpt_func, time_func, quote_func, weather_func, wiki_photo_func, news_func
import asyncio
import os
import aiohttp

reply_keyboard = [['/weather'], ['/time'], ['/phrase_of_the_day'], ['/news'], ['/dictionary'], ['/kitties'], ['/map'], ['/img'], ['/exchange_rate'], ['/help'], ['/GIT'], ['/GPT']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_news = [['/specific_news'], ['/general_news']]
markup_news = ReplyKeyboardMarkup(reply_keyboard_news, one_time_keyboard=True)

reply_keyboard_news_topic = [['/business'], ['/entertainment'], ['/general'], ['/health'], ['/science'], ['/sports'], ['/technology']]
markup_news_topic = ReplyKeyboardMarkup(reply_keyboard_news_topic, one_time_keyboard=True)

btn_loc = KeyboardButton('Отправить геопозицию', request_location=True)
markup_weather_loc = ReplyKeyboardMarkup([[btn_loc]], one_time_keyboard=True)


#функции затычки
async def map_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)
    
async def dictionary_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)
    
async def kitties_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)
    
async def img_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)
    
async def exchange_rate_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)

async def chat_gpt_command(update, context):
    await update.message.reply_html(rf"Временно не работает из за ошибок в OpenAI", reply_markup=markup)

##########################################

#help - доделать
async def help_command(update, context):
    await update.message.reply_text("/weather - выводит погоду по указанным данным\n/time - выводит время самых популярных мест\n"
                                    "/phrase_of_the_day - выводит фразу дня с картинкой автора\n/news - дает на выбор топики или личный запрос, потом выводит найденные новости\n"
                                    "/kitties - выводит милую фотографию котенка\n/exchange_rate - выводит курс валют\n/GIT - ссылка на наш гит\n"
                                    "/dictionary - работа с Cambridge Dictionary\n/map - работа с картой\n/img - работа с изображением\n/GPT - общение с AI от OpenAI")


#погода
async def weather_command(update, context):
    await update.message.reply_html(rf"Поделитесь с нами вашей локацией для поиска погоды в вашем районе!", reply_markup=markup_weather_loc)
    return 1

async def weather_command_response(update, context):
    long, lang = update.message.location.latitude, update.message.location.longitude
    func = weather_func.weather((lang, long))
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    return ConversationHandler.END
    
    
#новости
async def news_command(update, context):
    await update.message.reply_html(rf"Какие новости вас интересуют?", reply_markup=markup_news)

async def general_news(update, context):
    await update.message.reply_html(rf"Выберите топик", reply_markup=markup_news_topic) 
    
async def business(update, context):
    func = news_func.get_news('business', 'us')
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    
async def entertainment(update, context):
    func = news_func.get_news('entertainment', 'us')
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    
async def general(update, context):
    func = news_func.get_news('general', 'us')
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    
async def health(update, context):
    func = news_func.get_news('health', 'us')
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    
async def science(update, context):
    func = news_func.get_news('science', 'us')
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    
async def sports(update, context):
    func = news_func.get_news('sports', 'us')
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    
async def technology(update, context):
    func = news_func.get_news('technology', 'us')
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)

async def specific_news(update, context):
    await update.message.reply_text("Введите интересующий Вас топик")
    return 1

async def specific_news_response(update, context):
    func = news_func.get_spec_news(update.message.text)
    answer = await func
    await update.message.reply_html(answer, reply_markup=markup)
    return ConversationHandler.END
  

#фраза дня
async def quote_command(update, context):
    func = quote_func.quote()
    answer = await func
    await update.message.reply_text(f'{answer[0]}')
    await context.bot.send_message(update.message.chat_id, text=answer[1])
       

#гит
async def git_command(update, context):
    await update.message.reply_text('Вот ссылка на наш гит:\n\nhttps://github.com/Kr0uxx/Web-ProjectXXX')


#время
async def time_command(update, context):
    func = time_func.time()
    answer = await func
    #print(answer)
    await update.message.reply_text(answer)


#chat gpt - доделать 
async def message_answer(update, context):
    txt = update.message.text
    answer = gpt_func.ask(txt, 0)
    await update.message.reply_text(answer)


#start
async def start_command(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Здравствуй, {user.mention_html()}! Я бот с разными функциями, во мне даже есть GPT - можем пообщаться! Давай посмотрим на то, что я еще умею :D", reply_markup=markup)


#stop
async def stop(update, context):
    return ConversationHandler.END  


def main():
    application = Application.builder().token('6118068525:AAGGfYJ46p8Qe0sYLKC9v8KSsBH7cqybjf4').build()
    
    #затычки
    application.add_handler(CommandHandler("map", map_command))
    application.add_handler(CommandHandler("dictionary", dictionary_command))
    application.add_handler(CommandHandler("kitties", kitties_command))
    application.add_handler(CommandHandler("img", img_command))
    application.add_handler(CommandHandler("exchange_rate", exchange_rate_command))
    application.add_handler(CommandHandler("GPT", chat_gpt_command))
    
    
    #легкие команды
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("GIT", git_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(CommandHandler("phrase_of_the_day", quote_command))
    
    
    #новости
    application.add_handler(CommandHandler("news", news_command))
    application.add_handler(CommandHandler("general_news", general_news))
    application.add_handler(CommandHandler("business", business))
    application.add_handler(CommandHandler("entertainment", entertainment))
    application.add_handler(CommandHandler("general", general))
    application.add_handler(CommandHandler("health", health))
    application.add_handler(CommandHandler("science", science))
    application.add_handler(CommandHandler("sports", sports))
    application.add_handler(CommandHandler("technology", technology))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('specific_news', specific_news)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, specific_news_response)],   
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler)
    

    #погода
    conv_handler_weather = ConversationHandler(
        entry_points=[CommandHandler("weather", weather_command)],
        states={
            1: [MessageHandler(filters.LOCATION & ~filters.COMMAND, weather_command_response)],   
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler_weather)


    application.run_polling()



if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    main()