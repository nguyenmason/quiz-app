import tkinter as tk
from tkinter import ttk as ttk

class HomeLayout:
    """
    The HomeLayout class defines the layout for the home screen of the quiz application.
    """
    def __init__(self, root, categories):

        self.frame = ttk.Frame(root, style= "TFrame")
        self.frame.pack(expand= True, fill= 'both')

        title_label = ttk.Label(self.frame,style= "Title.TLabel", justify= 'center',
                                text="Super Cool Amazing Trivia Quiz App", wraplength= 300)
        title_label.pack(padx= 50, pady= 20, side= 'top', anchor= 'center')

        options = [category for category in categories.keys()]
        self.selected_option = tk.StringVar()
        dropdown = ttk.OptionMenu(self.frame, self.selected_option, *options)
        dropdown.pack()

        self.start_button = ttk.Button(self.frame, style= "HomeButton.TButton", text="Start")
        self.start_button.pack(padx= 20, pady= 20, side= 'top', anchor= 'center')

        self.info_button = ttk.Button(self.frame, style= "HomeButton.TButton", text="Info")
        self.info_button.pack(padx= 20, pady= 20, side= 'top', anchor= 'center')

        self.quit_button = ttk.Button(self.frame, style= "HomeButton.TButton", text="Quit", command=root.quit)
        self.quit_button.pack(padx= 20, pady= 20, side= 'top', anchor= 'center')

class QuestionLayout:
    """
    The QuestionLayout class defines the layout for displaying quiz questions and answer options.
    """
    def __init__(self, root, question, question_number):
        self.answer_buttons = []
        self.selected_answer = tk.IntVar(value=-1)
        self.frame = ttk.Frame(root, style= "TFrame")
        self.next_button = ttk.Button(self.frame, style="NextButton.TButton" ,text="Next")

        question_label = ttk.Label(self.frame, style= "Question.TLabel", justify='center',
                                    text= f"Q{question_number} " + question["question"],
                                    wraplength= root.winfo_width() - 40)
        question_label.pack(pady=20)
        
        # Creating a frame for each answer to pair a button and label
        for idx, answer in enumerate(question["answers"]):
            answer_frame = ttk.Frame(self.frame)
            answer_frame.pack(expand=True, fill='both')

            button = ttk.Radiobutton(answer_frame, value=idx, variable=self.selected_answer)
            button.grid(row=0, column=0, padx=10, pady=10)
            self.answer_buttons.append(button)

            answer = ttk.Label(answer_frame,style="Answer.TLabel", text=answer)
            answer.grid(row=0, column=1, pady=10)

        self.frame.pack(expand=True, fill='both')
        self.next_button.pack(pady=20)
    
    def update_question_buttons(self, correct_idx):
        for idx, button in enumerate(self.answer_buttons):
            if idx == correct_idx:
                button.config(text="\u2714", state= "disabled")
            else:
                button.config(text="\u274C", state= "disabled")
        
class ResultsLayout:
    """
    The ResultsLayout class defines the layout for displaying quiz results.
    """
    def __init__(self, root, score):

        self.frame = ttk.Frame(root, style="TFrame")
        self.frame.pack(expand=True, fill='both')

        results_label = ttk.Label(self.frame, style="Title.TLabel", justify='center', text="Score")
        results_label.pack(pady=20)

        score_label = ttk.Label(self.frame, style="Question.TLabel", justify='center', text=f"Score: {score} / 10")
        score_label.pack(pady=20)

        self.return_button = ttk.Button(self.frame, style="NextButton.TButton", text="Return to Home")
        self.return_button.pack(pady=20)

class HelpLayout:
    """
    The HelpLayout class defines the layout for displaying help information.
    """
    def __init__(self, root):
        self.frame = ttk.Frame(root, style="TFrame")
        self.frame.pack(expand=True, fill='both')

        info_label = ttk.Label(self.frame, style="Title.TLabel", justify='center', text="Information")
        info_label.pack(pady=10)

        instructions = (
            "Welcome to the Super Cool Amazing Trivia Quiz!\n\n"
            "Info:\n"
            "- Pick a category of trivia you want to test yourself on \n"
            "- Choose your answer \n"
            "- Click 'Next' to check your answer. \n"
            "- Click 'Next' again to go to the next question.\n"
            "- At the end of the quiz, you will see your score.\n"
            "- The quiz consists of 10 questions.\n\n"
            "Good luck and have fun!"
        )

        # Display the instructions
        label = ttk.Label(self.frame, text=instructions, justify="left", wraplength=root.winfo_width() - 50, style="Answer.TLabel")
        label.pack(padx=20, pady=10)

        self.return_button = ttk.Button(self.frame, style="NextButton.TButton", text="Return to Home")
        self.return_button.pack(pady=20)

def ErrorPopUp(root):
    """
    Displays an error popup window.


    Args:
        root (tk.Tk): The root window of the Tkinter application.
    """
    popup_window = tk.Toplevel(root)
    center_window(popup_window, 300, 200)

    popup_window.grab_set()
    popup_window.transient(root)
    popup_window.title("Request Error")
        
    frame = ttk.Frame(master= popup_window)
    frame.pack(fill='both')

    label = ttk.Label(master= frame, text="There was an error with retrieving questions. Please try again.", style="Answer.TLabel", wraplength= 300)
    label.pack(pady= 10)
        
    return_button = ttk.Button(master= frame, text="Return to Home", command=popup_window.destroy, style="NextButton.TButton")
    return_button.pack(pady= 10, anchor= 'center')

def center_window(root, width, height):
    """
    Centers the window on the screen.

    Args:
        root (tk.Tk): The root window of the Tkinter application.
        width (int): The width of the window.
        height (int): The height of the window.
    """
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')