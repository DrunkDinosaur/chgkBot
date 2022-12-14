class Cache:
    def __init__(self):
        self.current_question = {}

    def get(self):
        return self.current_question

    def put(self, new_question):
        self.current_question = new_question


