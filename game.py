from board import Board
from minimax import Minimax


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def play_game(self):
        while True:
            self.board.print_board()
            minimax = Minimax(self.board, self.current_player)
            move = minimax.best_move()

            if move:
                self.board.make_move(move[0], move[1], self.current_player)

            if self.board.check_winner(self.current_player):
                self.board.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.board.is_draw():
                self.board.print_board()
                print("It's a draw!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'
