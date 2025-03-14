# Understanding Recursion Problems & General Algorithm

## What are Recursion Problems?
Recursion problems are a class of computational problems that can be solved by breaking them down into smaller, similar subproblems. A recursive function calls itself with modified parameters until it reaches a **base case**, at which point it starts returning results back up the recursive chain.

Recursion is commonly used in:
- **Divide and Conquer Algorithms** (e.g., Merge Sort, Quick Sort)
- **Backtracking Problems** (e.g., Sudoku Solver, Word Search, N-Queens)
- **Tree and Graph Traversals** (e.g., DFS, Preorder/Inorder/Postorder traversals)
- **Dynamic Programming (Memoization & Tabulation)**

## General Algorithm for Solving Recursion Problems
To solve recursion-based problems efficiently, follow this structured approach:

### **1. Define the Base Case**
The base case is the stopping condition that prevents infinite recursion. It should be:
- The smallest input case for which the solution is known.
- A direct return value without further recursive calls.
  
Example:
- **Factorial Function:** Base case: `factorial(0) = 1`
- **Fibonacci Sequence:** Base cases: `fib(0) = 0`, `fib(1) = 1`

### **2. Identify the Recursive Case**
Determine how to break the problem into smaller subproblems.
- Express the solution in terms of **smaller subproblems**.
- Ensure that each recursive call moves closer to the base case.
  
Example:
- **Factorial:** `factorial(n) = n * factorial(n-1)`
- **Fibonacci:** `fib(n) = fib(n-1) + fib(n-2)`

### **3. Combine the Results**
Once the recursion reaches the base case, the results of subproblems are combined to form the final solution.
- This step is problem-specific and depends on how the recursion works.
- Can involve addition, multiplication, or merging of results.

### **4. Avoid Redundant Computation (Optimization Techniques)**
In some problems, recursion can lead to redundant computations. Use:
- **Memoization (Top-Down DP):** Store already computed results in a dictionary or array.
- **Tabulation (Bottom-Up DP):** Use iteration instead of recursion to build solutions from base cases.

### **5. Consider the Time and Space Complexity**
- **Time Complexity:** Determined by the number of recursive calls and work done at each level.
- **Space Complexity:** Depends on the depth of recursion (recursive call stack).
- Tail recursion can help optimize space complexity.

## Example Recursion Problem Breakdown
### **Problem: Compute Fibonacci Number**
#### **1. Define Base Case:**
- `fib(0) = 0, fib(1) = 1`
#### **2. Identify Recursive Case:**
- `fib(n) = fib(n-1) + fib(n-2)`
#### **3. Combine Results:**
- Compute smaller Fibonacci numbers and sum them.
#### **4. Optimize with Memoization:**
- Store previously computed results in an array.

## Summary
Recursion problems require breaking down problems into smaller subproblems, ensuring a base case exists, and combining results. Optimizations like memoization can enhance efficiency. Mastering recursion helps solve a wide range of algorithmic challenges effectively!

