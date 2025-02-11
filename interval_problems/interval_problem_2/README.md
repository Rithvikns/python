# Problem Statement

## Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [start[i], end [i]), return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]

Output: 1

Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping

# Greedy Algorithm:

A Greedy Algorithm is a problem-solving approach that makes a series of choices, each of which is the best (or "greedy") decision at that moment. The algorithm doesn't reconsider its previous choices; instead, it follows a simple, local optimization strategy to arrive at a globally optimal solution (if possible).

## Key Characteristics of Greedy Algorithms
Greedy Choice Property: A locally optimal choice at each step leads to a globally optimal solution.
Optimal Substructure: An optimal solution to a problem contains optimal solutions to its subproblems.
Not all problems can be solved optimally using a greedy approach. However, when applicable, greedy algorithms are efficient since they typically run in O(n log n) or O(n) time complexity.

### Steps in a Greedy Algorithm
Initialize: Start from an initial state.
Choose the best option at the current step based on a given criterion.
Update the state to reflect the choice made.
Repeat until a complete solution is obtained.
Examples of Greedy Algorithms
1. Activity Selection Problem (Interval Scheduling)
Given n activities with start and end times, select the maximum number of non-overlapping activities.
Greedy Strategy: Always pick the activity that ends the earliest.
2. Huffman Coding (Data Compression)
Used in file compression algorithms like ZIP and JPEG.
Greedy Strategy: Always merge the two smallest frequency nodes to build an optimal prefix code.
3. Kruskal’s Algorithm (Minimum Spanning Tree)
Finds the minimum cost to connect all nodes in a weighted graph.
Greedy Strategy: Always pick the smallest edge that does not form a cycle.
4. Dijkstra’s Algorithm (Shortest Path)
Finds the shortest path from a source node to all other nodes in a graph.
Greedy Strategy: Always pick the unvisited node with the smallest known distance.
5. Fractional Knapsack Problem (Optimization)
Given n items with values and weights, maximize the value that fits in a knapsack.
Greedy Strategy: Take the item with the highest value/weight ratio first.

# When to Use a Greedy Algorithm?
✅ When the Greedy Choice Property and Optimal Substructure hold.
✅ When there is a natural way to order choices to ensure optimality.
✅ When the problem explicitly asks for the maximum or minimum of something.

# Limitations of Greedy Algorithms
❌ Doesn't always yield the optimal solution (e.g., 0/1 Knapsack Problem).
❌ May require additional proof to verify correctness.
❌ Sometimes needs additional adjustments (e.g., backtracking or dynamic programming).

Would you like a Python implementation of one of these examples? 🚀
