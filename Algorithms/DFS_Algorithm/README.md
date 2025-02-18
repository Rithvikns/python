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

DFS traversal (starting from 1):

Step-by-Step DFS Traversal
Step	Current Node	Action	Stack
1	1	Visit 1, push neighbors 2, 3	[3, 2]
2	2	Visit 2, push neighbors 4, 5	[3, 5, 4]
3	4	Visit 4, no new neighbors	[3, 5]
4	5	Visit 5, no new neighbors	[3]
5	3	Visit 3, push neighbor 6	[6]
6	6	Visit 6, no new neighbors	[]


Final DFS Order
Copy
Edit
1 → 2 → 4 → 5 → 3 → 6
DFS explores deep (visiting 2, 4, 5 before 3).
