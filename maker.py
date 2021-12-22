class Maker:
    def __init__(self):
        self.questions = {}

    def ask(self):
        question = input("What do you want your question to be?")
        answers = []

        inputting_answers = True
        while inputting_answers:
            answer = input("What do you want your answer for that question to be? "
                           "There can be more than one- Type '/Done' when finished")

            if answer.lower() == "/done":
                inputting_answers = False
            else:
                answers.append(answer)
