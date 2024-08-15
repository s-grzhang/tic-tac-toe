import tkinter as tk
from board import Board
from minimax import Minimax
from minimax2 import Minimax2


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI vs AI")
        self.board = Board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

        self.ai1 = Minimax(self.board, 'X')  # First AI
        self.ai2 = Minimax2(self.board, 'O')  # Second AI
        self.current_player = 'X'

        self.root.after(1000, self.play_turn)

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font='Arial 20 bold', height=2, width=5)
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def play_turn(self):
        if self.current_player == 'X':
            move = self.ai1.best_move()
        else:
            move = self.ai2.best_move()

        if move:
            self.board.make_move(move[0], move[1], self.current_player)
            self.update_buttons()

        winner = self.board.check_winner()
        if winner:
            self.display_winner(winner)
        elif self.board.is_draw():
            self.display_winner("Draw")

        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.root.after(1000, self.play_turn)

    def update_buttons(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.board.board[row][col])

    def display_winner(self, winner):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)
        if winner == "Draw":
            tk.messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        else:
            tk.messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
