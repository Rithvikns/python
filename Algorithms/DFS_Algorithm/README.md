# Depth-First Search (DFS) Algorithm
DFS (Depth-First Search) is a fundamental graph/tree traversal algorithm that explores as deep as possible before backtracking.

## How DFS Works

DFS follows a "go deeper first" strategy:

Start at the root (or any starting node).
Visit the node and mark it as visited.
Recursively visit all its unvisited children (or adjacent nodes) one by one.
If a node has no unvisited children, backtrack to the previous node.
Repeat the process until all nodes are visited.
DFS can be implemented in two ways:

Recursive DFS (using function calls)
Iterative DFS (using a stack)
```console
     1
    / \
   2   3
  / \   \
 4   5   6
```

# Depth-First Search (DFS) Execution Steps

The table below demonstrates the step-by-step execution of **DFS traversal** on a sample graph.

## **DFS Traversal Table**

| Step | Current Node | Action | Stack |
|------|-------------|--------|-------|
| 1    | 1           | Visit 1, push neighbors 2, 3 | `[3, 2]` |
| 2    | 2           | Visit 2, push neighbors 4, 5 | `[3, 5, 4]` |
| 3    | 4           | Visit 4, no new neighbors | `[3, 5]` |
| 4    | 5           | Visit 5, no new neighbors | `[3]` |
| 5    | 3           | Visit 3, push neighbor 6 | `[6]` |
| 6    | 6           | Visit 6, no new neighbors | `[]` |

## **Key Takeaways**
- DFS follows a **"deepest node first"** approach.
- The **stack** helps backtrack when there are no more neighbors to visit.
- The traversal order for this example is:  
  **1 → 2 → 4 → 5 → 3 → 6**

---

### **📌 Steps to Upload to GitHub**
1. Go to your GitHub repository.
2. Click **"Add file" → "Create new file"**.
3. Name the file **`README.md`**.
4. Paste the content from above.
5. Click **"Commit changes"**.

Now, your table will **display properly formatted** on GitHub! 🚀  
Would you like to add any more details? 😊



Final DFS Order
Copy
Edit
1 → 2 → 4 → 5 → 3 → 6
DFS explores deep (visiting 2, 4, 5 before 3).


# DFS vs. BFS Comparison

| Feature        | DFS (Depth-First Search) | BFS (Breadth-First Search) |
|---------------|----------------------|----------------------|
| **Uses** | Stack (Iterative) or Recursion | Queue |
| **Explores** | Deepest node first | Nearest neighbors first |
| **Memory Usage** | O(D) (depth of tree/graph) | O(W) (width of tree/graph) |
| **Best for** | Deep structures (e.g., trees, backtracking) | Finding shortest paths (e.g., graphs, networks) |

## **When to Use DFS vs. BFS?**
- **Use DFS** when solving problems like:
  - Maze solving
  - Backtracking (e.g., Sudoku, N-Queens)
  - Detecting cycles in a graph

- **Use BFS** when solving problems like:
  - Finding the shortest path (e.g., Dijkstra’s Algorithm)
  - Level-order traversal in trees
  - Social network connections (e.g., mutual friends)

---

### **📌 Steps to Upload to GitHub**
1. Go to your GitHub repository.
2. Click **"Add file" → "Create new file"**.
3. Name the file **`README.md`**.
4. Paste the content from above.
5. Click **"Commit changes"**.

Now, your README file will **display the table properly formatted** on GitHub! 🚀  
Would you like to add anything else? 😊
