
# Generating Parentheses Combinations

## Problem Statement
Given an integer `n`, generate all combinations of `n` pairs of well-formed parentheses.

### Example
#### Input:
```
n = 3
```
#### Output:
```
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

## Approach
To generate all valid combinations, we can use **backtracking**:
1. Maintain two counters: `open` (number of `(` used) and `close` (number of `)` used).
2. A valid sequence must have `open <= n` and `close <= open`.
3. Start with an empty string and recursively add `(` if `open < n` and `)` if `close < open`.
4. Once `open == n` and `close == n`, a valid sequence is formed.

## Steps to Implement
1. Define a recursive function that keeps track of `open` and `close` parentheses used.
2. Add an opening parenthesis if `open < n`.
3. Add a closing parenthesis if `close < open`.
4. Append the valid sequences to the result list.

## Complexity Analysis
- Since each valid sequence consists of `2n` characters, and the total number of valid sequences is given by the **Catalan number** `C(n)`, the time complexity is **O(4^n / sqrt(n))**.
- Space complexity is **O(2n)** for storing the recursion stack.

## Applications
- Used in generating expressions for compilers.
- Helps in validating mathematical expressions.
- Useful in problems involving balanced sequences like XML parsing.

---
This file provides an explanation of the parentheses generation problem. The actual implementation can be added as a separate script.
