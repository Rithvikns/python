# Kadane’s Algorithm (Maximum Subarray Sum)

Kadane’s Algorithm is an efficient way to find the **maximum sum of a contiguous subarray** within a given list of numbers. It runs in **O(n) time complexity**, making it much faster than brute-force approaches.

## Algorithm Steps:
1. Initialize:
   - `max_sum` → Stores the maximum sum found so far.
   - `current_sum` → Tracks the sum of the current subarray.
   
2. Iterate through the array:
   - Add the current element to `current_sum`.
   - If `current_sum` exceeds `max_sum`, update `max_sum`.

3. Return `max_sum` after scanning the entire array.

---

## Applications of Kadane’s Algorithm:

Maximum Sum Subarray (Standard Use Case)
Finds the largest sum of contiguous elements in an array.
Use Case: Stock market analysis (maximum profit in a given period).


Maximum Sum Circular Subarray
Handles cases where the maximum sum subarray wraps around the array (i.e., some elements are taken from the end and some from the beginning).
Solution:
Find the maximum sum using Kadane’s Algorithm.
Find the minimum subarray sum using Kadane’s (on negative values) and subtract it from the total sum.
Return the maximum of both cases.
Use Case: Temperature analysis, cyclic data (e.g., time-series data in scheduling).


Maximum Sum Rectangle in a 2D Matrix
Finds the submatrix with the largest sum in a 2D matrix.
Approach:
Fix two rows and apply Kadane’s Algorithm on the column-wise sum.
Use Case: Image processing, financial modeling, and path optimization.

Longest Subarray with Positive Sum
Finds the longest contiguous subarray with a sum greater than zero.
Use Case: Helps in signal processing and game score tracking.


Finding Maximum Product Subarray
Similar to Kadane’s Algorithm but considers multiplication instead of addition.
Approach:
Keep track of both maximum and minimum products (because a negative number can turn a small product into a large one).
Use Case: Helps in financial projections and risk management.


Largest Sum of Non-Adjacent Elements (Modified Kadane’s)
Variation of Kadane’s Algorithm used in dynamic programming to find the maximum sum where no two elements are adjacent.
Use Case: House Robber Problem (choosing houses to rob without alerting police).

Maximum Contiguous Bitonic Subarray
A bitonic array first increases and then decreases. This variation of Kadane’s Algorithm helps find the maximum sum of such an array.
Use Case: Used in terrain modeling and financial trend analysis.


DNA Sequence Analysis
Helps in analyzing genomic data to find highly expressed genes by identifying the most significant subsequence.
Use Case: Bioinformatics (DNA pattern matching).

##  Example:
### **Input:**
```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
### **Output:**
Maximum subarray sum: 6


