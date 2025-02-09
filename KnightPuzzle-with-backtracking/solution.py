# Possible moves for a knight in chess
next_move = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
             (1, 2), (1, -2), (-1, 2), (-1, -2)]

n = 8  # Board size

def is_safe(row, col, board):
    """ Check if the move is within board limits and not already visited """
    return (0 <= row < n and 0 <= col < n and board[row][col] == -1)

def backtracking(row, col, movei, board):
    """ Recursive function for solving Knight's Tour """
    if movei == n * n:  # Base case: If all squares are visited
        return True

    for dr, dc in next_move:
        next_row, next_col = row + dr, col + dc
        if is_safe(next_row, next_col, board):
            board[next_row][next_col] = movei  # Mark move
            if backtracking(next_row, next_col, movei + 1, board):  
                return True
            board[next_row][next_col] = -1  # Backtrack if no solution

    return False

def solve_knights_tour(start_row=0, start_col=0):
    """ Function to solve Knight's Tour problem """
    board = [[-1]*n for _ in range(n)]  # Initialize board
    board[start_row][start_col] = 0  # Starting position

    if backtracking(start_row, start_col, 1, board):
        for row in board:
            print(row)
    else:
        print("No solution found")

# Example: Start the knight at (0, 0)
solve_knights_tour()
