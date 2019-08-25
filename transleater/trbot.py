import telebot

bot = telebot.TeleBot("902231828:AAFwNVWjUJFTstm6ef-hH6mjr_OOvUiTKgg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.cgat.id, message.txt)
bot.polling( none_stop=True)
