# Super Cool Amazing Trivia Quiz App

## Overview
The Quiz App is a simple and interactive trivia quiz application built using Python and Tkinter. It allows users to answer multiple-choice questions and provides feedback on their performance.

## Features
- Multiple-choice quiz made up of 10 questions
- Quiz can be about different trivia categories
- Tracks correct and incorrect answers
- Displays results at the end of the quiz
- Info button on home screen for information about the app

## Installation
1. Clone the repository:
   git clone https://github.com/nguyenmason/quiz-app.git
2. Navigate to the project directory:
    cd quiz-app
3. Install the required dependencies:
    pip install -r requirements.txt


## Usage
1. Run the application.
2. Follow the on-screen instructions to start the quiz.
3. Select your answers and click "Next" to proceed to the next question.
4. At the end of the quiz, your results will be displayed.

## Project Structure
- main.py: The main entry point of the application.
- controllers/: Contains the game logic and API interaction.
   - game.py: Manages the overall flow of the quiz application.
   - api.py: Interacts with the Open Trivia Database API to fetch quiz questions.
- models/: Contains the data models.
   - quiz.py: Manages the quiz questions, tracks the score, and provides the current question.
- views/: Contains the layout and style configurations.
   - layouts.py: Defines the layout for different screens (home, question, results, help).
   - styles.py: Defines the appearance of various widgets using the ttk.Style class.
tests.py: Contains unit tests for the application.

## Acknowledgements
Tkinter - Python's standard GUI toolkit.
Open Trivia Database - The source of quiz questions.