from controllers.api import QuizAPI
from views import layouts, styles
from models.quiz import Quiz

class Game:
    """
    The Game class manages the overall flow of the quiz application.
    It handles the initialization, navigation between screens, and interaction with the QuizAPI.
    """
    def __init__(self, root):
        self.quiz_api = QuizAPI()
        self.root = root
        self.layout = None

        #configure the root window
        root.configure(bg= "#f7f7f7")
        root.title("Super Cool Amazing Trivia Quiz App")
        layouts.center_window(root, 400, 500)

        styles.setup_styles()
        self.go_to_home()


    def start_quiz(self):
        quiz_questions = self.quiz_api.get_questions(self.layout.selected_option.get())
        if not quiz_questions:
            # Show error popup if no questions are fetched
            layouts.ErrorPopUp(self.root)
        else:
             # Initialize the quiz with fetched questions
            self.quiz = Quiz(quiz_questions)
            self.next_question()

    def bind_question_buttons(self, buttons, next_button):
        for button in buttons:
            # Enable the 'Next' button when an answer is selected
            button.config(command= lambda: next_button.config(state="normal"))
        next_button.config(command=self.check_answer, state="disabled")

    def check_answer(self):
        if self.quiz.current_question()["correct_answer_idx"] == self.layout.selected_answer.get():
            self.quiz.correct += 1
        else:
            self.quiz.incorrect += 1
        # Highlights the correct answer
        self.layout.update_question_buttons(self.quiz.current_question()["correct_answer_idx"])
        #  Set up the 'Next' button to proceed to the next question
        self.layout.next_button.config(command=self.next_question)

    def next_question(self):
        self.quiz.current_question_idx += 1
        if self.quiz.current_question_idx < len(self.quiz.questions):
            # Load the next question            
            self.layout.frame.destroy()
            self.layout = layouts.QuestionLayout(self.root, self.quiz.current_question(), self.quiz.current_question_idx + 1)
            self.bind_question_buttons(self.layout.answer_buttons, self.layout.next_button)
            self.layout.selected_answer.set(-1)
        else:
            # Show the quiz results if there are no more questions
            self.layout.frame.destroy()
            self.layout = layouts.ResultsLayout(self.root, self.quiz.correct)
            self.layout.return_button.config(command=self.go_to_home)

    def go_to_home(self):
        # layout may be none if called from __init__
        if self.layout:
            self.layout.frame.destroy()

        categories = self.quiz_api.get_categories()
        if not categories:
            layouts.ErrorPopUp(self.root)
        else:
            self.layout= layouts.HomeLayout(self.root, categories)
            self.layout.start_button.config(command=self.start_quiz)
            self.layout.info_button.config(command=self.show_help)
    
    def show_help(self):
        self.layout.frame.destroy()
        self.layout = layouts.HelpLayout(self.root)
        self.layout.return_button.config(command=self.go_to_home)