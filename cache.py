timeout_ms = 1000 * 60 * 60 * 24 * 7


class Cache:
    def __init__(self):
        self.questions_dictionary = {}

    def get(self, chat_id):
        return self.questions_dictionary[chat_id]

    def put(self, new_question, chat_id):
        self.questions_dictionary[chat_id] = new_question

    def check_timeouts(self):
        pass
