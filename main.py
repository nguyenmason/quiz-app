import tkinter as tk
from controllers import game

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.game = game.Game(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Main()
    app.run()