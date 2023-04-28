from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton


reply_keyboard = [['/weather'], ['/time'], ['/phrase_of_the_day'], ['/news'], ['/dictionary'], ['/kitties'], ['/map'], ['/img'], ['/exchange rate'], ['/help'], ['/GIT']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

reply_keyboard_news = [['/specific_news'], ['/general_news']]
markup_news = ReplyKeyboardMarkup(reply_keyboard_news, one_time_keyboard=True)

reply_keyboard_news_topic = [['/business'], ['/entertainment'], ['/general'], ['/health'], ['/science'], ['/sports'], ['/technology']]
markup_news_topic = ReplyKeyboardMarkup(reply_keyboard_news_topic, one_time_keyboard=True)

btn_loc = KeyboardButton('Отправить геопозицию', request_location=True)
markup_weather_loc = ReplyKeyboardMarkup([[btn_loc]], one_time_keyboard=True)


#доделать
async def help_command(update, context):
    await update.message.reply_text("help")
    


#гит
async def git_command(update, context):
    await update.message.reply_text('Вот ссылка на наш гит:\n\nhttps://github.com/Kr0uxx/Web-ProjectXXX')


    

#chat gpt  
async def message_answer(update, context):
    txt = update.message.text
    await update.message.reply_text(txt)


#start
async def start_command(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Здравствуй, {user.mention_html()}! Я бот с разными функциями, во мне даже есть GPT - можем пообщаться! Давай посмотрим на то, что я еще умею :D", reply_markup=markup)



def main():
    BOT_TOKEN = '6118068525:AAFCNE4yXACJw7pORlDDSxbfw-gZqXUv6TM'
    application = Application.builder().token(BOT_TOKEN).build()

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message_answer)
    
    #легкие команды
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("GIT", git_command))
    #application.add_handler(CommandHandler("time", time_command))
    #application.add_handler(CommandHandler("phrase_of_the_day", quote_command))
    
    



    application.run_polling()



if __name__ == '__main__':
    main()