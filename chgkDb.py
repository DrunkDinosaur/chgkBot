import requests
from bs4 import BeautifulSoup as b
from question import Question

URL = 'https://db.chgk.info/random'


def get_images(tag):
    images = tag.find_all('img')
    return [i.get("src") for i in images]


def parse_question(question_tag):
    # print(question_tag)
    answer_tag = question_tag.find_all('div', class_="collapsible collapsed")[0]
    answer = '; '.join(get_images(answer_tag)) + answer_tag.text

    question_tag.find('div', class_="collapsible collapsed").decompose()
    question = '; '.join(get_images(question_tag)) + question_tag.text.replace("Вопрос 1", "Внимание, вопрос")

    return Question(question, answer)


def getQuestion():
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    question = soup.find_all('div', class_='random_question')[0]

    return parse_question(question)
