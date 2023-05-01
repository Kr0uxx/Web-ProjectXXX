from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
from functions import gpt_func, time_func, quote_func, weather_func, wiki_photo_func, news_func, kitties_func, \
    dogs_func, actual_crypto_rate, actual_rate, voice_to_txt_func
import asyncio
import os
import aiohttp
from data import db_session
from data.user import User





reply_keyboard = [['/help'], ['/GIT'], ['/weather'], ['/time'], ['/phrase_of_the_day'], ['/news'], ['/dictionary'],
                  ['/animals'],
                  ['/map'], ['/black_and_white'], ['/economics'], ['/GPT'], ['/voice_yt'], ['/voice_to_txt']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_news = [['/specific_news'], ['/general_news']]
markup_news = ReplyKeyboardMarkup(reply_keyboard_news, one_time_keyboard=True)

reply_keyboard_news_topic = [['/business'], ['/entertainment'], ['/general'], ['/health'], ['/science'], ['/sports'],
                             ['/technology']]
markup_news_topic = ReplyKeyboardMarkup(reply_keyboard_news_topic, one_time_keyboard=True)

btn_loc = KeyboardButton('Отправить геопозицию', request_location=True)
markup_weather_loc = ReplyKeyboardMarkup([[btn_loc]], one_time_keyboard=True)

reply_keyboard_economics = [['/exchange_rate'], ['/crypto_rate']]
markup_economics = ReplyKeyboardMarkup(reply_keyboard_economics, one_time_keyboard=True)

reply_keyboard_bit = [['/BTC'], ['/ETH'], ['/BNB'], ['/LTC'], ['SOL'], ['/DOGE'], ['/ADA'], ['/DOT'], ['/XRP'],
                      ['/LINA']]
markup_bit = ReplyKeyboardMarkup(reply_keyboard_bit, one_time_keyboard=True)

reply_keyboard_exch = [['/USD'], ['/EUR'], ['/CNY'], ['/GBP'], ['/JPY'], ['/CHF'], ['/UAH'], ['/TRY'], ['/AUD'],
                       ['/KZT']]
markup_exch = ReplyKeyboardMarkup(reply_keyboard_exch, one_time_keyboard=True)

reply_keyboard_animals = [['/kitties'], ['/dogs']]
markup_animals = ReplyKeyboardMarkup(reply_keyboard_animals, one_time_keyboard=True)

reply_keyboard_lang = [['/RU'], ['/UK'], ['/US'], ['/FR'], ['/DUTCH'], ['/ITA'], ['/SPAN'], ['/DK']]
markup_lang = ReplyKeyboardMarkup(reply_keyboard_lang, one_time_keyboard=True)


###########################################
# функции затычки
async def map_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)


async def dictionary_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)


async def black_and_white_command(update, context):
    await update.message.reply_html(rf"Функция временно не работает", reply_markup=markup)

###########################################


########################
# help - доделать
async def help_command(update, context):
    await update.message.reply_text(
        "/weather - выводит погоду по вашему отправленному местоположению\n\n/time - выводит время самых популярных мест\n\n/economics - дает возможность посмотреть курс и рынок крипты"
        "/phrase_of_the_day - выводит фразу дня с картинкой автора ( иногда картинка не находится по причине ее отсутсвия в википедии )\n\n/news - можете выбрать special news и ввести то, что хотите найти, или выбрать general news и выбрать из предоставленных топиков\n\n"
        "/animals - дает возможность получить милого котенка или собачку\n\n/exchange_rate - выводит курс популярных валют\n\n/GIT - ссылка на наш гит\n\n"
        "/dictionary - работа с Cambridge Dictionary\n\n/map - работа с картой\n\n/black_and_white - работа с изображением\n\n/GPT - общение с AI от OpenAI\n\n"
        "/voice_yt - по ссылке из ютуб достает звук из видео\n\n/crypto_rate - из списка можете выбрать интересующую Вас крипту и получить ее курс\n\n/voice_to_txt - из wav файла достаем звук, преобразует его потом в текст")

########################
# погода
async def weather_command(update, context):
    await update.message.reply_html(rf"Поделитесь с нами вашей локацией для поиска погоды в вашем районе!",
                                    reply_markup=markup_weather_loc)
    return 1


async def weather_command_response(update, context):
    long, lang = update.message.location.latitude, update.message.location.longitude
    func = weather_func.weather((lang, long))
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    return ConversationHandler.END


########################
# новости
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


########################
# фраза дня
async def quote_command(update, context):
    func = quote_func.quote()
    answer = await func
    await update.message.reply_text(f'{answer[0]}')
    await context.bot.send_message(update.message.chat_id, text=answer[1])


########################
# гит
async def git_command(update, context):
    await update.message.reply_text('Вот ссылка на наш гит:\n\nhttps://github.com/Kr0uxx/Web-ProjectXXX\n\nИ на наши профили:\n\nАртем - https://github.com/YL-bot\n\nМаксим - https://github.com/Kr0uxx\n\nКатя - https://github.com/katiarapter')


########################
# время
async def time_command(update, context):
    func = time_func.time()
    answer = await func
    # print(answer)
    await update.message.reply_text(answer)


########################
# chat gpt
async def gpt_command(update, context):
    await update.message.reply_text('Задайте мне вопрос')
    return 1


async def message_answer(update, context):
    txt = update.message.text
    answer = gpt_func.ask(txt, 0)
    await update.message.reply_html(rf"{answer}", reply_markup=markup)
    return ConversationHandler.END


########################
# start
async def start_command(update, context):
    user = update.effective_user
    id = user.id
    db_sess = db_session.create_session()

    await update.message.reply_html(
        rf"Здравствуй, {user.mention_html()}! Я бот с разными функциями, во мне даже есть GPT - можем пообщаться! Давай посмотрим на то, что я еще умею :D",
        reply_markup=markup)


########################
# stop
async def stop(update, context):
    return ConversationHandler.END


#########################
# animals
async def animals_command_response(update, context):
    await update.message.reply_html(rf"Выберите вид животного, картинку которого хотите увидеть",
                                    reply_markup=markup_animals)
# cats
async def kitties_command(update, context):
    func = kitties_func.kitties()
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)

# dogs
async def dogs_command(update, context):
    func = dogs_func.dogs()
    answer = await func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


########################
# крипта и курс
async def economics_command_response(update, context):
    await update.message.reply_html(rf"Выберите тему, интересующую вас",
                                    reply_markup=markup_economics)
# крипта

async def crypto_rate_command(update, context):
    await update.message.reply_html(rf"Выберите то, что хотите посмотреть", reply_markup=markup_bit)


async def crypto_rate_btc_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('BTC')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_eth_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('ETH')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_bnb_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('BNB')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_ltc_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('LTC')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_sol_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('SOL')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_doge_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('DOGE')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_ada_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('ADA')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_dot_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('DOT')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_xrp_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('XRP')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def crypto_rate_lina_command(update, context):
    func = actual_crypto_rate.get_actual_crypto_rate('LINA')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)

#курс
async def exchange_rate_command(update, context):
    await update.message.reply_html(rf"Выберите курс, который вам интересен", reply_markup=markup_exch)


async def exchange_rate_usd_command(update, context):
    func = actual_rate.get_actual_rate('USD')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_eur_command(update, context):
    func = actual_rate.get_actual_rate('EUR')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_cny_command(update, context):
    func = actual_rate.get_actual_rate('CNY')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_gbp_command(update, context):
    func = actual_rate.get_actual_rate('GBP')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_jpy_command(update, context):
    func = actual_rate.get_actual_rate('JPY')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_chf_command(update, context):
    func = actual_rate.get_actual_rate('CHF')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_uah_command(update, context):
    func = actual_rate.get_actual_rate('UAH')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_try_command(update, context):
    func = actual_rate.get_actual_rate('TRY')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_aud_command(update, context):
    func = actual_rate.get_actual_rate('AUD')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)


async def exchange_rate_kzt_command(update, context):
    func = actual_rate.get_actual_rate('KZT')
    answer = func
    await update.message.reply_html(rf"{answer}", reply_markup=markup)



########################
#перевод звука из ютуб
async def voice_yt_command(update, context):
    await update.message.reply_html(rf"Функция работала на момент 21 апреля, потом снова полетела из за обновления ютуб."
                                    "Не наша вина, но 'pytube' улетел уже в какой раз. Для просмотра самой функции можно в папке"
                                    "functions найти yt_convert_func.py", reply_markup=markup)


########################
# из wav в текст
async def voice_to_txt_command(update, context):
    await update.message.reply_text(rf"Отправь мне файл в формате WAV")
    return 1

async def downloader(update, context):
    file = await context.bot.get_file(update.message.document)
    await file.download_to_drive('files/main.wav')
    await update.message.reply_html(rf"Выбери язык, который в файле ( если не знаете, то выберите DK )",
                                    reply_markup=markup_lang)
    return ConversationHandler.END


async def voice_dk(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_main()}", reply_markup=markup)

async def voice_ru(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_lang('Russian')}", reply_markup=markup)

async def voice_uk(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_lang('UK English')}", reply_markup=markup)

async def voice_us(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_lang('US English')}", reply_markup=markup)

async def voice_fr(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_lang('French')}", reply_markup=markup)

async def voice_dut(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_lang('Dutch')}", reply_markup=markup)

async def voice_ital(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_lang('Italian')}", reply_markup=markup)

async def voice_sp(update, context):
    await update.message.reply_html(rf"{voice_to_txt_func.voice_lang('Spanish')}", reply_markup=markup)



########################
# основа основ основских
def main():
    application = Application.builder().token('6118068525:AAGGfYJ46p8Qe0sYLKC9v8KSsBH7cqybjf4').build()

    # затычки
    # + еще пару функций есть и нужно сделать бд
    application.add_handler(CommandHandler("map", map_command))
    application.add_handler(CommandHandler("dictionary", dictionary_command))
    application.add_handler(CommandHandler("black_and_white", black_and_white_command))
    # + функция отправки на почту сообщений, api с рецептом, + bd сделать

    # легкие команды
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("GIT", git_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(CommandHandler("phrase_of_the_day", quote_command))
    application.add_handler(CommandHandler("voice_yt", voice_yt_command))

    # Животные
    application.add_handler(CommandHandler("animals", animals_command_response))
    application.add_handler(CommandHandler("kitties", kitties_command))
    application.add_handler(CommandHandler("dogs", dogs_command))


    # Экономика
    application.add_handler(CommandHandler("economics", economics_command_response))


    # крипта
    application.add_handler(CommandHandler("crypto_rate", crypto_rate_command))

    application.add_handler(CommandHandler("BTC", crypto_rate_btc_command))
    application.add_handler(CommandHandler("ETH", crypto_rate_eth_command))
    application.add_handler(CommandHandler("BNB", crypto_rate_bnb_command))
    application.add_handler(CommandHandler("LTC", crypto_rate_ltc_command))
    application.add_handler(CommandHandler("SOL", crypto_rate_sol_command))
    application.add_handler(CommandHandler("DOGE", crypto_rate_doge_command))
    application.add_handler(CommandHandler("ADA", crypto_rate_ada_command))
    application.add_handler(CommandHandler("DOT", crypto_rate_dot_command))
    application.add_handler(CommandHandler("XRP", crypto_rate_xrp_command))
    application.add_handler(CommandHandler("LINA", crypto_rate_lina_command))


    # курс обычный
    application.add_handler(CommandHandler("exchange_rate", exchange_rate_command))

    application.add_handler(CommandHandler("USD", exchange_rate_usd_command))
    application.add_handler(CommandHandler("EUR", exchange_rate_eur_command))
    application.add_handler(CommandHandler("CNY", exchange_rate_cny_command))
    application.add_handler(CommandHandler("GBP", exchange_rate_gbp_command))
    application.add_handler(CommandHandler("JPY", exchange_rate_jpy_command))
    application.add_handler(CommandHandler("CHF", exchange_rate_chf_command))
    application.add_handler(CommandHandler("UAH", exchange_rate_uah_command))
    application.add_handler(CommandHandler("TRY", exchange_rate_try_command))
    application.add_handler(CommandHandler("AUD", exchange_rate_aud_command))
    application.add_handler(CommandHandler("KZT", exchange_rate_kzt_command))


    # новости
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


    # погода
    conv_handler_weather = ConversationHandler(
        entry_points=[CommandHandler("weather", weather_command)],
        states={
            1: [MessageHandler(filters.LOCATION & ~filters.COMMAND, weather_command_response)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler_weather)


    # файл со звуком wav в текст
    conv_handler_wav = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('voice_to_txt', voice_to_txt_command)],
        
        states={
            1: [MessageHandler(filters.Document.WAV, downloader)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler_wav)

    application.add_handler(CommandHandler("DK", voice_dk))
    application.add_handler(CommandHandler("RU", voice_ru))
    application.add_handler(CommandHandler("UK", voice_uk))
    application.add_handler(CommandHandler("US", voice_us))
    application.add_handler(CommandHandler("FR", voice_fr))
    application.add_handler(CommandHandler("DUTCH", voice_dut))
    application.add_handler(CommandHandler("ITA", voice_ital))
    application.add_handler(CommandHandler("SPAN", voice_sp))


    # GPT
    conv_handler_gpt = ConversationHandler(
        entry_points=[CommandHandler("GPT", gpt_command)],
        states={
            1: [MessageHandler(filters.TEXT, message_answer)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler_gpt)


    application.run_polling()


if __name__ == '__main__':
    db_session.global_init("db/data.db")
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    main()
