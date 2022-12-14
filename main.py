import chgkDb
import telebot
from cache import Cache

# print(q.question)
# print(q.answer)
API_KEY = ''
bot = telebot.TeleBot(API_KEY)
cache = Cache()


@bot.message_handler(commands=['вопрос'])
def ask_question(message):
    q = chgkDb.getQuestion()
    cache.put(q)
    bot.send_message(message.chat.id, q.question)


@bot.message_handler(commands=['ответ'])
def ask_question(message):
    bot.send_message(message.chat.id, cache.get().answer)


bot.polling()
