import chgkDb
import telebot
from cache import Cache
from api_key import API_KEY

from bs4 import BeautifulSoup as b
from question import Question

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


@bot.message_handler(commands=['тест'])
def test_question(message):
    text_file = open('test_data/test_question', "r")
    testQuestion = text_file.read()
    text_file.close()

    soup = b(testQuestion, 'html.parser')
    question = soup.find_all('div', class_='random_question')[0]
    q = chgkDb.parse_question(question)
    bot.send_message(message.chat.id, q.question)
    bot.send_message(message.chat.id, q.answer)


bot.polling()

