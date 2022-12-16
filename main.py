import chgkDb
import telebot
from cache import Cache
from api_key import API_KEY

from bs4 import BeautifulSoup as b

bot = telebot.TeleBot(API_KEY)
cache = Cache()


@bot.message_handler(commands=['вопрос'])
def ask_question(message):
    try:
        q = chgkDb.getQuestion()
        cache.put(q, message.chat.id)
        bot.send_message(message.chat.id, q.question)
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так.")


@bot.message_handler(commands=['ответ'])
def get_answer(message):
    try:
        bot.send_message(message.chat.id, cache.get(message.chat.id).answer)
    except:
        bot.send_message(message.chat.id, "Что-то пошло не так.")


@bot.message_handler(commands=['тест'])
def test(message):
    text_file = open('test_data/test_question', "r")
    test_question = text_file.read()
    text_file.close()

    soup = b(test_question, 'html.parser')
    question = soup.find_all('div', class_='random_question')[0]
    q = chgkDb.parse_question(question)
    bot.send_message(message.chat.id, q.question)
    bot.send_message(message.chat.id, q.answer)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text.lower() == "нет":
        bot.reply_to(message, "пидора ответ")


bot.polling()

