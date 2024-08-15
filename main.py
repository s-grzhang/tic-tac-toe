# main.py

from game import TicTacToeApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
