class Question:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

        self.answerers = {}

    def add_answerer(self, user_name, user_id, answer, is_correct):
        self.answerers[f"{user_name} ({user_id})"] = [answer, is_correct]

