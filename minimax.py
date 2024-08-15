class Minimax:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.opponent = 'O' if player == 'X' else 'X'

    def minimax(self, depth, is_maximizing):
        winner = self.board.check_winner()
        if winner == self.player:
            return 10 - depth
        elif winner == self.opponent:
            return depth - 10
        elif self.board.is_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.board.board[row][col] == ' ':
                        self.board.board[row][col] = self.player
                        score = self.minimax(depth + 1, False)
                        self.board.board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board.board[row][col] == ' ':
                        self.board.board[row][col] = self.opponent
                        score = self.minimax(depth + 1, True)
                        self.board.board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = float('-inf')
        move = None
        for row in range(3):
            for col in range(3):
                if self.board.board[row][col] == ' ':
                    self.board.board[row][col] = self.player
                    score = self.minimax(0, False)
                    self.board.board[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move
