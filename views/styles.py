from tkinter import ttk as ttk

def setup_styles():
    style = ttk.Style()
    # Frame Styles
    style.configure("TFrame", background="#f7f7f7")
    # Dropdown Styles
    style.configure("Dropdown.TButton",font= ("Trebucet MS", 8),
                     padding=6, relief="flat", background="#8ad8ce")
    # Button Styles
    style.configure("HomeButton.TButton", font= ("Trebucet MS", 14),
                     padding=6, relief="flat", background="#8ad8ce")
    style.configure("NextButton.TButton", font= ("Trebucet MS", 12),
                     padding=2, relief="flat", background="#8ad8ce")
    # Label Styles
    style.configure("Title.TLabel", padding=6,font= ("Trebucet MS", 18),
                     justify= "center", relief="flat", background="#f7f7f7")
    style.configure("Question.TLabel", padding=6,font= ("Trebucet MS", 16),
                     justify= "center", relief="flat", background="#f7f7f7")
    style.configure("Answer.TLabel", padding=6,font= ("Trebucet MS", 14),
                     relief="flat", background="#f7f7f7")
    

