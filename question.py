from datetime import datetime


class Question:
    def __init__(self, q, a):
        self.question = q
        self.answer = a
        self.creation_time = datetime.now()

