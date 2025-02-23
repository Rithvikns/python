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
