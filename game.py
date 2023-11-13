class TicTacToeAI:

  def __init__(self):
    self.board = [[" " for _ in range(3)] for _ in range(3)]
    self.current_turn = "X"  # Human player will be 'X' and goes first

  def print_board(self):
    for row in self.board:
      print("|".join(row))
      print("-" * 5)

  def make_move(self, row, col, player):
    if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
      self.board[row][col] = player
      return True
    return False

  def check_winner(self):
    for i in range(3):
      if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
        return self.board[i][0]
      if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
        return self.board[0][i]

    if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
      return self.board[0][0]
    if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
      return self.board[0][2]

    return None

  def check_draw(self):
    return all(" " not in row for row in self.board)

  def minimax(self, depth, is_maximizing):
    winner = self.check_winner()
    if winner == 'X':
      return -10 + depth
    elif winner == 'O':
      return 10 - depth
    elif self.check_draw():
      return 0

    if is_maximizing:
      best_score = -float('inf')
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == " ":
            self.board[i][j] = 'O'
            score = self.minimax(depth + 1, False)
            self.board[i][j] = " "
            best_score = max(score, best_score)
      return best_score
    else:
      best_score = float('inf')
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == " ":
            self.board[i][j] = 'X'
            score = self.minimax(depth + 1, True)
            self.board[i][j] = " "
            best_score = min(score, best_score)
      return best_score

  # Only make best move for O player
  def best_move(self):
    best_score = -float('inf')
    move = None
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == " ":
          self.board[i][j] = 'O'
          score = self.minimax(0, False)
          self.board[i][j] = " "
          if score > best_score:
            best_score = score
            move = (i, j)
    return move

  def human_move(self, new_board):
    # Validate board value
    for row in new_board:
      for cell in row:
        if cell not in [" ", "X", "O"]:
          raise ValueError("Invalid board value")
    if len(new_board) == 3 and all(len(row) == 3 for row in new_board):
      self.board = new_board
    else:
      raise ValueError("Invalid board state")

    winner = self.check_winner()
    if winner is not None:
      return {'board': self.board, 'status': 'end', 'winner': winner}
    if self.check_draw():
      return {'board': self.board, 'status': 'end', 'winner': 'Draw'}

    move = self.best_move()
    if move:
      self.make_move(*move, 'O')
      winner = self.check_winner()
      if winner is not None:
        return {'board': self.board, 'status': 'end', 'winner': winner}
      if self.check_draw():
        return {'board': self.board, 'status': 'end', 'winner': 'Draw'}
      return {'board': self.board, 'status': 'continue'}
    return {'board': self.board, 'status': 'unknown'}
