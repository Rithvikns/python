def print_chess(board):
  for row in board:
    print("".join("Q" if col else "." for col in row)
  print("\n")


def is_safe(board , row , col , n ):

    # chech if any other queen exist horizontally
          
    for i in range(row):
        if board[i][col]:
            return False

     # chech if any other queen exist upper left diagonal
    
    i,j = row , col
    while i >=0 and j>=0:
      if board[i][j]:
          return False
      i-=1
      j-=1

     # chech if any other queen exist upper right diagonal

    
    i, j = row , col
    while i>=0 , j<n:
      if board[i][j]:
          return False
      i-=1
      j+=1

  return True

def backtrackin_function(board , row , n , solution):

  if row == n:
    solution.append(["".join("Q" if col else "." for _ in r) for r in board])
    return

  for col in range(n):
    if is_safe(board , row , col , n):
      board[row][col] = 1
      backtracking_function(board , row +1 , n , solutions)
      board[row][col] = 0

def n_queen(n):
  board = [[0]*n for _ in n]
  solutions = []
  backtracking_function(board , 0 , n , solutions)
  return solutions


n = 8
solutions = n_queens(n)
for sol in solutions:
    for row in sol:
        print(row)
    print("\n" + "="*10 + "\n")
