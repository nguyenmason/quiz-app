import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from controllers.game import Game as Game
from views import layouts
from models.quiz import Quiz

class TestQuizApp(unittest.TestCase):
    def setUp(self):
        # Set up the root window and the game instance
        self.root = tk.Tk()
        self.game = Game(self.root)

    def tearDown(self):
        # Destroy the root window after each test
        self.root.destroy()

    @patch('controllers.api.QuizAPI.get_questions')
    def test_start_quiz(self, mock_get_questions):
        # Mock the API response
        mock_get_questions.return_value = [
            {
                "question": "What is the capital of France?",
                "correct_answer": "Paris",
                "incorrect_answers": ["London", "Berlin", "Madrid"]
            }
        ]

        # Simulate starting the quiz
        self.game.start_quiz()

        # Check if the quiz was initialized correctly
        self.assertIsInstance(self.game.quiz, Quiz)
        self.assertEqual(len(self.game.quiz.questions), 1)
        self.assertEqual(self.game.quiz.questions[0]["question"], "What is the capital of France?")

    def test_go_to_home(self):
        # Simulate going to the home screen
        self.game.go_to_home()

        # Check if the home layout was initialized correctly
        self.assertIsInstance(self.game.layout, layouts.HomeLayout)
        self.assertEqual(self.game.layout.start_button.cget("text"), "Start")
        self.assertEqual(self.game.layout.info_button.cget("text"), "Info")

    def test_check_answer_correct(self):
        # Mock the quiz questions
        self.game.quiz = Quiz([
            {
                "question": "What is the capital of France?",
                "correct_answer": "Paris",
                "incorrect_answers": ["London", "Berlin", "Madrid"]
            }
        ])
        self.game.quiz.current_question_idx = 0

        # Mock the layout
        self.game.layout = layouts.QuestionLayout(self.root, self.game.quiz.current_question(), 0)
        self.game.layout.selected_answer.set(self.game.quiz.current_question()["correct_answer_idx"])  # Simulate selecting the correct answer

        # Check the answer
        self.game.check_answer()

        # Verify the score
        self.assertEqual(self.game.quiz.correct, 1)
        self.assertEqual(self.game.quiz.incorrect, 0)

    def test_info_button(self):
        # Simulate going to the home screen
        self.game.go_to_home()

        # Simulate clicking the "Info" button
        self.game.layout.info_button.invoke()

        # Check if the layout changed to HelpLayout
        self.assertIsInstance(self.game.layout, layouts.HelpLayout)
        self.assertEqual(self.game.layout.return_button.cget("text"), "Return to Home")

    def test_check_answer_incorrect(self):
        # Mock the quiz questions
        self.game.quiz = Quiz([
            {
                "question": "What is the capital of France?",
                "correct_answer": "Paris",
                "incorrect_answers": ["London", "Berlin", "Madrid"]
            }
        ])
        self.game.quiz.current_question_idx = 0

        # Mock the layout
        self.game.layout = layouts.QuestionLayout(self.root, self.game.quiz.current_question(), 1)
        correct_guess = self.game.quiz.current_question()["correct_answer_idx"]
        incorrect_guess = (correct_guess + 1) % 4
        self.game.layout.selected_answer.set(incorrect_guess)  # Simulate selecting the incorrect answer

        # Check the answer
        self.game.check_answer()

        # Verify the score
        self.assertEqual(self.game.quiz.correct, 0)
        self.assertEqual(self.game.quiz.incorrect, 1)

if __name__ == "__main__":
    unittest.main()