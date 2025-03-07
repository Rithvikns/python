# Best Time to Buy and Sell Stock III

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on day `i`.  
You may complete at most **two transactions** to maximize your profit.  
**Note:** You must sell the stock before buying again.

### **Example 1**
```console
Input: prices = [3,3,5,0,0,3,1,4] Output: 6 Explanation: Buy on day 4 (price = 0), sell on day 5 (price = 3), profit = 3 - 0 = 3. Buy on day 6 (price = 1), sell on day 7 (price = 4), profit = 4 - 1 = 3. Total profit = 3 + 3 = 6.
```

### **Example 2**
```
Input: prices = [1,2,3,4,5] Output: 4 Explanation: Buy on day 1, sell on day 5, profit = 4 - 1 = 4.
```
---

## **Algorithm Explanation**
### **Step 1: Compute Maximum Profit for One Transaction (Left to Right)**
- Track the **minimum price seen so far**.
- Compute the **max profit possible** if the transaction ends at each day.
- Store these in `left_profit[i]`.

| Day | Price | Min Price So Far | Max Profit So Far |
|----|------|-----------------|-----------------|
| 0 | 3 | 3 | 0 |
| 1 | 3 | 3 | 0 |
| 2 | 5 | 3 | 5 - 3 = 2 |
| 3 | 0 | 0 | 2 |
| 4 | 0 | 0 | 2 |
| 5 | 3 | 0 | 3 - 0 = 3 |
| 6 | 1 | 0 | 3 |
| 7 | 4 | 0 | 4 - 0 = 4 |

`left_profit = [0, 0, 2, 2, 2, 3, 3, 4]`

---

### **Step 2: Compute Maximum Profit for One Transaction (Right to Left)**
- Track the **maximum price seen so far**.
- Compute the **max profit possible** if the transaction starts at each day.
- Store these in `right_profit[i]`.

| Day | Price | Max Price So Far | Max Profit So Far |
|----|------|-----------------|-----------------|
| 7 | 4 | 4 | 0 |
| 6 | 1 | 4 | 4 - 1 = 3 |
| 5 | 3 | 4 | 3 |
| 4 | 0 | 4 | 4 |
| 3 | 0 | 4 | 4 |
| 2 | 5 | 5 | 4 |
| 1 | 3 | 5 | 4 |
| 0 | 3 | 5 | 4 |

`right_profit = [4, 4, 4, 4, 4, 3, 3, 0]`

---

### **Step 3: Find the Best Split Point**
Compute `max_profit = left_profit[i] + right_profit[i]` for each day.

| Day | Left Profit | Right Profit | Total Profit |
|----|------------|------------|-------------|
| 0 | 0 | 4 | 4 |
| 1 | 0 | 4 | 4 |
| 2 | 2 | 4 | 6 |
| 3 | 2 | 4 | 6 |
| 4 | 2 | 4 | 6 |
| 5 | 3 | 3 | 6 |
| 6 | 3 | 3 | 6 |
| 7 | 4 | 0 | 4 |

**Maximum profit = 6**, achieved at multiple points.

---

### **Step 4: Find the Buy/Sell Days**
1. **First transaction (before or on best split point `i=4`)**
   - Buy at **day 4 (price = 0)**.
   - Sell at **day 5 (price = 3)**.
   - **Profit = 3 - 0 = 3**.

2. **Second transaction (after best split point)**
   - Buy at **day 6 (price = 1)**.
   - Sell at **day 7 (price = 4)**.
   - **Profit = 4 - 1 = 3**.

**Total Profit = 6**.


---

Time Complexity

O(n) for both passes → O(n) overall.


Space Complexity

O(n) due to left_profit and right_profit arrays.



---

Conclusion

This approach efficiently finds the maximum profit with at most two transactions while following the given constraints.
To return exact buy/sell days, we can modify the code to store transaction indices.


---

Let me know if you want further clarifications!

---

### **How to Use It on GitHub?**
1. Create a new repository.
2. Upload this `README.md` file.
3. Add the Python file (`max_profit.py`) with the implementation.

This `README.md` file clearly explains the problem, algorithm, and solution with examples. Would you like me to add anything else?


	

