# Best Time to Buy and Sell Stock II

## Problem Statement
You are given an array where the **i-th** element represents the price of a stock on day **i**. 
Design an algorithm to find the **maximum profit** you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

### Constraints:
- You **cannot** engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
- You **must** buy before you sell.

## Examples
### Example 1:
**Input:**
```python
prices = [7,1,5,3,6,4]
```
**Output:**
```python
7
```
**Explanation:**
- Buy on **day 2** (price = **1**) and sell on **day 3** (price = **5**) → Profit = `5 - 1 = 4`
- Buy on **day 4** (price = **3**) and sell on **day 5** (price = **6**) → Profit = `6 - 3 = 3`
- **Total Profit = 4 + 3 = 7**

### Example 2:
**Input:**
```python
prices = [1,2,3,4,5]
```
**Output:**
```python
4
```
**Explanation:**
- Buy on **day 1** (price = **1**) and sell on **day 5** (price = **5**) → Profit = `5 - 1 = 4`
- **Total Profit = 4**

### Example 3:
**Input:**
```python
prices = [7,6,4,3,1]
```
**Output:**
```python
0
```
**Explanation:**
- No profitable transactions can be made.

## Solution Approach
We use a **greedy algorithm**:
1. Iterate through the array.
2. Whenever there is a **price increase**, add the difference to the total profit.

### Code Implementation
```python
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# Test cases
print(maxProfit([7,1,5,3,6,4]))  # Output: 7
print(maxProfit([1,2,3,4,5]))    # Output: 4
print(maxProfit([7,6,4,3,1]))    # Output: 0
```
# Second version - Atmost One transaction
If you were only permitted to complete atmost one transaction (i.e buy one ans sell one stock), design an algorithm to find the max profit

## Solution
```python
def max_profit(prices):
    n = len(prices)
    profit = [0] * n 
    min_price = prices[0]
    for i in range(1,n):
        min_price = min(min_price , prices[i])
        profit[i] = max(profit[i-1] , prices[i] - min_price)
    return max(profit)
```
# Third Version - Atmost Two Transaction
```python
def max_profit(prices):
    n = len(prices)
    left_profit = [0] * n 
    min_price = prices[0]
    for i in range(1,n):
        min_price = min(min_price , prices[i])
        left_profit[i] = max(left_profit[i-1] , prices[i] - min_price)

    right_profit = [0] * n 
    max_price = prices[-1]
    for i in range(n-2,-1,-1):
        max_price = max(max_price , prices[i])
        right_profit[i] = max(right_profit[i-1] , max_price - prices[i])
    profit = 0
    for i in range(n):
        profit = max(profit , left_profit[i] + right_profit[i])
    return max(profit)
```     

## Complexity Analysis
- **Time Complexity**: `O(n)`, as we traverse the array once.
- **Space Complexity**: `O(1)`, since we use only a few variables.

## Summary
- The problem involves buying and selling stocks to maximize profit.
- The **greedy approach** ensures we capture all profitable opportunities.
- The solution runs in **linear time** and uses **constant space**.
