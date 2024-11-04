import telebot

tokan = "6177942697:AAG8Xg-tk8jtDMfCgViJCgxOzQk5adK3Mvk"

bot = telebot.TeleBot(tokan)

channel_id = '@hackerpdfbotlog'



@bot.message_handler(commands=['start'])
def mes(message):
    bot.send_message(message.chat.id,"bot run")



bot.infinity_polling()

