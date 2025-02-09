import tkinter as tk
import time

class NQueensVisualizer:
    def __init__(self, n=8):
        self.n = n
        self.cell_size = 60  # Size of each square
        self.delay = 500  # Delay in milliseconds for visualization
        self.board = [-1] * n  # Stores queen positions (row -> col)
       
        # Tkinter setup
        self.window = tk.Tk()
        self.window.title(f"{n}-Queens Visualization")
        self.canvas = tk.Canvas(self.window, width=n*self.cell_size, height=n*self.cell_size)
        self.canvas.pack()
        self.draw_board()
        self.window.after(1000, self.solve_n_queens, 0, set(), set(), set())  # Start solving
        self.window.mainloop()

    def draw_board(self):
        """Draws the chessboard with alternating colors"""
        for i in range(self.n):
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(
                    j * self.cell_size, i * self.cell_size,
                    (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                    fill=color, outline="black"
                )

    def draw_queen(self, row, col):
        """Places a queen on the board"""
        x = col * self.cell_size + self.cell_size // 2
        y = row * self.cell_size + self.cell_size // 2
        self.canvas.create_oval(
            x - 20, y - 20, x + 20, y + 20,
            fill="red", outline="black"
        )

    def clear_queen(self, row, col):
        """Removes a queen from the board"""
        self.canvas.create_rectangle(
            col * self.cell_size, row * self.cell_size,
            (col + 1) * self.cell_size, (row + 1) * self.cell_size,
            fill="white" if (row + col) % 2 == 0 else "gray",
            outline="black"
        )

    def solve_n_queens(self, row, cols, diag1, diag2):
        """Backtracking function with UI updates"""
        if row == self.n:
            print("Solution Found!")
            return True  # Found a solution, exit

        for col in range(self.n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # Skip invalid placements

            # Place queen
            self.board[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            self.draw_queen(row, col)
            self.window.update()
            time.sleep(self.delay / 1000)  # Delay for visualization

            if self.solve_n_queens(row + 1, cols, diag1, diag2):
                return True  # Stop after first solution

            # Backtrack
            self.clear_queen(row, col)
            self.window.update()
            time.sleep(self.delay / 1000)

            # Remove queen
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

# Run the visualization
NQueensVisualizer(n=8)  # Change n for different board sizes
