# Tree Construction and Maximum Sum Path using DFS

## Overview
This project converts a list of edges into a tree and finds the maximum sum from the root to any leaf using Depth-First Search (DFS).

## How It Works

### 1. **Building the Tree**
- The input is a list of tuples, each representing a parent-child relationship with a weight.
- The tree is stored as an adjacency list (a dictionary where each parent node maps to a list of its children and associated edge weights).
- The root node is determined by finding a node that is never a child.

### 2. **Finding the Maximum Sum Path Using DFS**
- The algorithm starts from the root and explores all possible paths recursively.
- At each node:
  - It visits all child nodes and calculates the sum of the path weight.
  - It keeps track of the maximum sum encountered.
- The recursion stops at leaf nodes and returns the computed maximum sum.

## Example Walkthrough
### Given Edges:
```
(1, 2, 3)
(1, 3, 5)
(2, 4, 7)
(2, 5, 6)
(3, 6, 4)
(3, 7, 8)
```
### Step-by-Step Execution:
1. Construct the tree:
   ```
   1
  / \
 2   3
/ \  / \
4  5 6  7
   ```
   - Root = `1`
   - Adjacency List:
     ```
     { 1: [(2,3), (3,5)],
       2: [(4,7), (5,6)],
       3: [(6,4), (7,8)] }
     ```

2. Perform DFS to find the maximum sum path:
   - DFS traverses paths:
     - `1 → 2 → 4` (Sum = 1 + 3 + 7 = 11)
     - `1 → 2 → 5` (Sum = 1 + 3 + 6 = 10)
     - `1 → 3 → 6` (Sum = 1 + 5 + 4 = 10)
     - `1 → 3 → 7` (Sum = 1 + 5 + 8 = 15) → **Max Path**

### Output:
```
Maximum sum from root to leaf: 15
```

## Complexity Analysis
- **Tree Construction:** `O(N)`, where `N` is the number of edges.
- **DFS Traversal:** `O(N)`, as each node is visited once.
- **Overall Complexity:** `O(N)`, making it efficient for large trees.

## Conclusion
This approach efficiently finds the maximum sum path using DFS, making it ideal for hierarchical data structures where weighted path evaluation is required.


