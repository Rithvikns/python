def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(row):
        if board[i][col] or \
           (col - (row - i) >= 0 and board[i][col - (row - i)]) or \
           (col + (row - i) < n and board[i][col + (row - i)]):
            return False
    return True

def solve_n_queens(board, row, n, count):
    """Recursive function to count N-Queens solutions"""
    if row == n:  # If all queens are placed, count the solution
        count[0] += 1
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place queen
            solve_n_queens(board, row + 1, n, count)
            board[row][col] = 0  # Backtrack

def count_n_queens_solutions(n):
    """Returns the number of solutions for N-Queens"""
    board = [[0] * n for _ in range(n)]
    count = [0]  # Use a list to store count (mutable)
    solve_n_queens(board, 0, n, count)
    return count[0]

# Example usage:
n = 50  # Change this for different board sizes
num_solutions = count_n_queens_solutions(n)
print(f"Number of solutions for {n}-Queens: {num_solutions}")
