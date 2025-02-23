# Problem Statement:
Given a string `s`, find the length of the longest subsequence that is a palindrome.

# Solution Using DP:
We use **bottom-up tabulation** to efficiently solve LPS in `O(n^2)` time complexity.

```python
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the dp table
    for length in range(2, n + 1):  # Length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and length == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

# Example usage
s = "bbbab"
print(longest_palindromic_subsequence(s))  # Output: 4
```

# Explanation:
1. **Initialize DP Table**: Create a 2D table where `dp[i][j]` stores the LPS length for substring `s[i:j+1]`.
2. **Base Case**: Single characters are palindromes of length 1.
3. **Fill Table Iteratively**: If `s[i] == s[j]`, expand the LPS by 2; otherwise, take the maximum from adjacent subproblems.
4. **Final Result**: `dp[0][n-1]` gives the longest palindromic subsequence for the entire string.

## Conclusion
Dynamic Programming is a powerful technique that optimizes recursive problems by storing intermediate results, reducing time complexity, and making algorithms feasible for large inputs. It is widely used in competitive programming, artificial intelligence, and real-world optimization problems.

