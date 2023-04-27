from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from functions import gpt_func, time_func, quote_func, weather_func, wiki_photo_func


reply_keyboard = [['/weather'], ['/time'], ['/phrase_of_the_day'], ['/news'],
                  ['/dictionary'], ['/kitties'], ['/map'], ['/img'], ['/exchange rate'], ['/help'], ['/GIT']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


#доделать
async def weather_command(update, context):
    await update.message.reply_text(weather_func.weather('координаты'))

#доделать
async def help_command(update, context):
    await update.message.reply_text("help")
 
 
async def quote_command(update, context):
    await update.message.reply_text(quote_func.quote())
       

async def git_command(update, context):
    await update.message.reply_text('Вот ссылка на наш гит:\n\nhttps://github.com/Kr0uxx/Web-ProjectXXX')


async def time_command(update, context):
    await update.message.reply_text(time_func.time())
    
    
async def message_answer(update, context):
    txt = update.message.text
    answer = gpt_func.ask(txt, 0)
    await update.message.reply_text(answer)


async def start_command(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Здравствуй, {user.mention_html()}! Я бот с разными функциями, во мне даже есть GPT - можем пообщаться! Давай посмотрим на то, что я еще умею :D", reply_markup=markup)


def main():
    application = Application.builder().token('6118068525:AAF6TU-SIYuy5lUViZgxpLOUhYIzkNDo6q8').build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message_answer)
    
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("GIT", git_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(CommandHandler("phrase_of_the_day", quote_command))
    application.add_handler(CommandHandler("whether", weather_command))



    application.run_polling()



if __name__ == '__main__':
    main()