# Word Search Problem

## Problem Statement
The Word Search problem is a common algorithmic challenge where you are given an `m x n` grid of characters (a board) and a target word. The goal is to determine if the word can be found in the grid by forming it using **sequentially adjacent** cells. A cell is considered adjacent if it is horizontally or vertically neighboring. The same cell **cannot** be used more than once in a single search path.

## Example
### **Input:**
```
board = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]
word = "ABCCED"
```

### **Output:**
```
True
```

## Solution Approach
To solve this problem efficiently, we use the **Depth-First Search (DFS) with Backtracking** approach. Below is a step-by-step breakdown of the strategy:

### **1. Iterating Through the Grid**
- We iterate through every cell in the board.
- If a cell matches the **first letter** of the word, we start a DFS search from that position.

### **2. Implementing DFS with Backtracking**
- The DFS function attempts to match the next character in the word by moving **up, down, left, and right**.
- If we reach the end of the word successfully, we return `True`.
- If the character does not match or goes out of bounds, we return `False`.

### **3. Marking Visited Cells**
- To prevent reusing the same cell in a single search path, we temporarily mark the cell as visited.
- After exploring all directions, we restore the original character to allow further searches.

### **4. Early Termination for Efficiency**
- If a valid path is found, we stop further exploration and return `True`.
- If all possible paths fail, we continue searching from other potential starting points in the grid.

## Time Complexity Analysis
- In the worst case, we may explore all possible paths in the grid.
- The time complexity is approximately **O(m × n × 4^L)** where:
  - `m` and `n` are the board dimensions.
  - `L` is the length of the word.
  - Each cell has up to 4 possible directions to move in the DFS search.

## Space Complexity
- The space complexity is **O(L)** due to the recursive call stack, where `L` is the length of the word.
- We do not use additional data structures except for modifying the board in-place.

## Summary
The Word Search problem is efficiently solved using **DFS with Backtracking**, where we explore potential paths recursively while ensuring cells are not reused. This approach guarantees we check all valid possibilities while minimizing unnecessary computations.


