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

### Example Problem: Travelling Salesman Problem (TSP)
A complex example of DP is the **Travelling Salesman Problem (TSP)**.

#### Problem Statement:
Given a set of `n` cities and the distance between each pair of cities, find the shortest possible route that visits every city exactly once and returns to the starting city.

#### Solution Using DP (Held-Karp Algorithm):
We use **bitmasking** and **memoization** to efficiently solve TSP in `O(n^2 * 2^n)` time complexity.

```python
from functools import lru_cache

def tsp(mask, pos, dist, n, memo):
    if mask == (1 << n) - 1:
        return dist[pos][0]  # Return to starting city
    if (mask, pos) in memo:
        return memo[(mask, pos)]
    
    min_cost = float('inf')
    for city in range(n):
        if (mask & (1 << city)) == 0:  # If city not visited
            new_cost = dist[pos][city] + tsp(mask | (1 << city), city, dist, n, memo)
            min_cost = min(min_cost, new_cost)
    
    memo[(mask, pos)] = min_cost
    return min_cost

def solve_tsp(dist):
    n = len(dist)
    memo = {}
    return tsp(1, 0, dist, n, memo)

# Example distance matrix
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(solve_tsp(distance_matrix))  # Output: Minimum travel cost
```

## Conclusion
Dynamic Programming is a powerful technique that optimizes recursive problems by storing intermediate results, reducing time complexity, and making algorithms feasible for large inputs. It is widely used in competitive programming, artificial intelligence, and real-world optimization problems.
