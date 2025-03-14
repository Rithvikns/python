from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def recursion(r, c, index):
            # Base Case: If all characters are matched, return True
            if index == len(word) - 1:
                return board[r][c] == word[index]

            # Boundary check and character match check
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[index]:
                return False

            # Temporarily mark cell as visited
            temp = board[r][c]
            board[r][c] = '#'  

            # Explore all four directions
            found = (recursion(r + 1, c, index + 1) or
                     recursion(r - 1, c, index + 1) or
                     recursion(r, c + 1, index + 1) or
                     recursion(r, c - 1, index + 1))

            # Restore the original value before returning
            board[r][c] = temp  
            return found

        # Start DFS from any cell that matches the first character of word
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and recursion(r, c, 0):
                    return True
        return False
