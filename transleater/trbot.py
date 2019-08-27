import telebot
bot = telebot.TeleBot("902231828:AAFwNVWjUJFTstm6ef-hH6mjr_OOvUiTKgg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)
bot.polling( none_stop=True)

# pip3 install pyTelegramBotAPI
