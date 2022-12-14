import requests
from bs4 import BeautifulSoup as b
from question import Question

URL = 'https://db.chgk.info/random'


def getQuestion():
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    questions = soup.find_all('div', class_='random_question')
    clear_questions = [q.text for q in questions]

    print(clear_questions[0])

    qa = clear_questions[0].split('Ответ')
    return Question(qa[0].replace("Вопрос 1", "Внимание, вопрос"), "Ответ" + qa[1])
