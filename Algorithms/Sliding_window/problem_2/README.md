# Longest Repeating Character Replacement

## Problem Statement
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Example 1:
```
Input: s = "ABAB", k = 2
Output: 4
```
#### Explanation:
Replace the two 'A's with 'B's or vice versa to get "BBBB" or "AAAA".

### Example 2:
```
Input: s = "AABABBA", k = 1
Output: 4
```
#### Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The longest substring with repeating letters is "BBBB", which has length `4`.

---

## Approach (Sliding Window)
We use a **sliding window** approach to efficiently determine the longest substring.

### Steps:
1. Use two pointers (`left` and `right`) to create a sliding window.
2. Maintain a dictionary to track character frequencies in the current window.
3. Track the most frequent character in the window (`max_count`).
4. Check if replacing the remaining characters (`window length - max_count`) exceeds `k`.
   - If yes, shrink the window from the left.
   - If no, expand the window from the right.
5. Keep track of the maximum window size encountered.

---

## Code Implementation

Initialization:

left: Marks the beginning of the sliding window.

max_count: Stores the count of the most frequent character in the current window.

char_count: Dictionary to store the frequency of characters in the window.

max_length: Stores the maximum length of the valid substring.

Expanding the Window:

The right pointer moves across the string.

char_count updates the count of characters in the window.

max_count tracks the count of the most frequent character in the window.

Checking Validity:

If the number of characters to change (window size - max_count) exceeds k, the window is shrunk by moving left forward.

Updating Maximum Length:

After adjusting the window, max_length is updated with the longest valid window size found.

---

## Dry Run Example
Let's walk through the function with an example:

```
Input: s = "AABABBA", k = 1
```

| Step | Window (`left` to `right`) | char_count | max_count | Replace Needed | Action | max_length |
|------|-----------------|------------|------------|-----------------|----------|------------|
| 1    | "A"          | `{'A': 1}` | 1          | `0` (Valid)      | Expand   | 1          |
| 2    | "AA"         | `{'A': 2}` | 2          | `0` (Valid)      | Expand   | 2          |
| 3    | "AAB"        | `{'A': 2, 'B': 1}` | 2 | `1` (Valid) | Expand | 3 |
| 4    | "AABA"       | `{'A': 3, 'B': 1}` | 3 | `1` (Valid) | Expand | 4 |
| 5    | "AABAB"      | `{'A': 3, 'B': 2}` | 3 | `2` (**Too many!**) | Shrink | 4 |
| 6    | "ABAB"       | `{'A': 2, 'B': 2}` | 2 | `2` (**Too many!**) | Shrink | 4 |
| 7    | "BABB"       | `{'A': 1, 'B': 3}` | 3 | `1` (Valid) | Expand | 4 |

Final answer: **4**.

---

## Complexity Analysis
- **Time Complexity:** \(O(N)\) since we traverse the string once.
- **Space Complexity:** \(O(1)\) because we store at most 26 characters.

---

## Summary
- We use a **sliding window** to expand and shrink dynamically.
- We track the **most frequent character** and ensure at most `k` replacements.
- The **key condition** is:
  ```
  (window size - most frequent character count) ≤ k
  ```
- The final result is the maximum valid window size encountered.

This approach ensures optimal performance, solving the problem in **O(N) time**. 🚀

---

## Contributing
If you have any improvements or alternative solutions, feel free to contribute by opening a pull request!

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

