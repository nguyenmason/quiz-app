import html
import random

class Quiz:
    """
    The Quiz class manages the quiz questions, tracks the score, and provides the current question.
    """
    def __init__(self, questions):
        self.questions = questions
        self.correct = 0
        self.incorrect = 0
        self.current_question_idx = -1

        # Randomize the order of the answers
        # Creates a new key for the correct answer index and the answers list
        # turns the html encoded characters back to their original form
        for question in self.questions:
            question['question'] = html.unescape(question['question'])

            correct_index = random.randint(0, 3)
            question["correct_answer_idx"] = correct_index

            question["answers"] = [html.unescape(answer) for answer in question["incorrect_answers"]]
            question["answers"].insert(correct_index, html.unescape(question["correct_answer"]))

    def current_question(self):
        return self.questions[self.current_question_idx]
    
    def get_statistics(self):
        return self.correct, self.incorrect
    