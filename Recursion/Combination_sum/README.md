# Combination Sum Problem Explanation

## Problem Statement
Given an array of **distinct integers** called `candidates` and an integer `target`, find all unique combinations of `candidates` where the sum of the chosen numbers equals `target`.

Each number in `candidates` can be used **an unlimited number of times**. The order of elements in a combination **does not matter**, but combinations must be **unique** (i.e., different frequencies of numbers create different combinations).

### Example:
#### **Input:**
```
candidates = [2,3,6,7], target = 7
```
#### **Output:**
```
[[2,2,3], [7]]
```
#### **Explanation:**
- The number `2` can be used multiple times.
- `[2,2,3]` is valid because `2+2+3 = 7`.
- `[7]` is valid because `7 = 7`.

## Approach to Solve the Problem
Since this is a **combinations** problem with **unlimited usage** of numbers, the best approach is **Backtracking with DFS (Depth-First Search)**.

### **Step-by-Step Thought Process**
1. **Sort the `candidates` array** (optional but helps with optimization).
2. **Use recursion** to explore all possible combinations:
   - Start with an empty combination list.
   - Iterate over `candidates` and try adding each number to the current combination.
   - If the sum exceeds `target`, stop that branch (backtracking).
   - If the sum equals `target`, add the combination to the output list.
   - Continue searching deeper in the recursion.
3. **Ensure no duplicate combinations**:
   - Use an index `start` to avoid revisiting previous numbers in the same recursion branch.
   - Allow the same number to be chosen again by continuing from `start` in the recursion.
4. **Backtrack** by removing the last added element before moving to the next choice.

## Complexity Analysis
- **Time Complexity:** `O(2^N)`, where `N` is the number of candidates (worst case is an exhaustive search of all subsets).
- **Space Complexity:** `O(target / min(candidates))` for the recursion stack.

## Edge Cases to Consider
1. **No valid combinations:** If no numbers can sum up to `target`, return `[]`.
2. **Single element cases:** If `candidates` has only one number, handle cases where it can/cannot sum to `target`.
3. **Large target values:** Ensure efficiency for larger `target` values by pruning unnecessary calculations.
4. **Repeated elements in input:** Although the problem states distinct elements, handling duplicate candidates is a good practice.

## Summary
- Use **DFS with Backtracking**.
- Keep track of **current sum** and **current combination**.
- Ensure **no duplicate** combinations.
- **Prune unnecessary recursion** when sum exceeds `target`.

This approach ensures an optimal and correct solution to the **Combination Sum** problem.


