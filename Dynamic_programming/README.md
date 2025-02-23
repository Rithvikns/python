# Dynamic Programming (DP)

## What is Dynamic Programming?
Dynamic Programming (DP) is an optimization technique used in computer science and mathematics to solve problems by breaking them down into smaller subproblems and solving each subproblem only once. The results of subproblems are stored (memoized) and reused to avoid redundant computations, improving efficiency significantly.

### Key Principles of DP:
1. **Optimal Substructure**: The problem can be broken down into smaller subproblems, and the optimal solution to the original problem can be constructed from optimal solutions to its subproblems.
2. **Overlapping Subproblems**: The same subproblems are solved multiple times. DP avoids redundant calculations by storing previously computed results.

### DP Techniques:
- **Top-Down Approach (Memoization)**: Solve the problem recursively and store the results of subproblems to avoid recomputation.
- **Bottom-Up Approach (Tabulation)**: Solve the subproblems iteratively and use previously computed results to build up the solution.

## Why Do We Need Dynamic Programming?
DP is essential when dealing with problems that have exponential time complexity using naive recursion. By breaking problems into smaller overlapping subproblems and reusing their solutions, DP significantly reduces computation time. It is widely used in:
- **Optimization problems** (e.g., shortest path, maximum profit, minimum cost, etc.)
- **Combinatorial problems** (e.g., counting ways to do something, subset sum, etc.)
- **String processing** (e.g., longest common subsequence, edit distance, etc.)
- **Graph algorithms** (e.g., Floyd-Warshall, Bellman-Ford, etc.)
- **Game theory** (e.g., minimax algorithm with DP for decision-making problems)

### Example Problem: Fibonacci Sequence
A classic example of DP is computing Fibonacci numbers.

#### Naive Recursive Approach (Exponential Time Complexity):
```python
# Naive recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

#### Optimized DP Approach (O(n) Time Complexity):
```python
# Memoization (Top-Down)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```
```python
# Tabulation (Bottom-Up)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## Conclusion
Dynamic Programming is a powerful technique that optimizes recursive problems by storing intermediate results, reducing time complexity, and making algorithms feasible for large inputs. It is widely used in competitive programming, artificial intelligence, and real-world optimization problems.
