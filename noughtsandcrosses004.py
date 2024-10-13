



def board_generator(size):
  return [["." for i in range(size)]for j in range (size)]


def play_game():
  size = int(input("Enter desired board size ( e.g. 3 ):"))
  board = board_generator(size)
  public_size = size
  player = "X"
  while not is_game_over(board):
    print(format_board(board))
    print("It's " + player + "'s turn.")
    board = make_move(board, player)
    if player == "X":
      player = "O"
    else:
      player = "X"
  print(format_board(board))
  print("Game over! Player "+ str(["X" if player == "O" else "O"])[2] + " wins.")

def format_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid
  

def make_move(board, player):
  row = int(input("Enter a row: "))-1
  column = int(input("Enter a column: "))-1
  if row > len(board[1]) or column > len(board[1]):
    print("Coordinates out of board range! Try again.")
    make_move(board, player)
  elif board[row][column] == ".":
    board[row][column] = player
  else:
    print("Place already taken! Try again.")
    make_move(board, player)
  return board


def won_by_rows(board):
  for row in board:
    if ["X"] * len(row) == row or ["O"] * len(row) == row:
      return True
  else:
    return False
  
def won_by_columns(board):
  boardsize = len(board[0])
  for column in range(boardsize):
    top = board[0][column]
    counter = 0
    for row in range(boardsize):
      if board[row][column] == top and (top == "X" or top == "O"):
        counter +=1
      else:
        break
    if counter == boardsize:
      return True
  return False
        
    


def won_by_diagonals(board):
  boardsize = len(board)
  all_same = False
  if board[0][0] == "X" or board[0][0] == "O":
    for i in range(boardsize):
        if board[i][i] == board[0][0]:
            all_same = True

        else:
          all_same = False
          break
    if all_same:
        return True
    
    if board[0][boardsize-1] == "X" or board[0][boardsize-1] == "O":
        for j in range(boardsize):
            if board[j][boardsize -1 -j] == board[0][boardsize-1]:
                all_same = True
            else:
                all_same = False
                return False
        if all_same:
          return True

    else:
      return False
  


def is_game_over(board):
  if won_by_columns(board) or won_by_rows(board) or won_by_diagonals(board):
    return True
  else:
    return False

print("Game time!")
play_game()
