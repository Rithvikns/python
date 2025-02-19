def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_count = 0  # Stores the count of the most frequent character in the window
    char_count = {}  # Dictionary to store character frequencies
    max_length = 0  # Stores the max substring length

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])

        # Check if the number of replacements needed is greater than k
        while (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1  # Shrink the window from the left

        # Update max_length
        max_length = max(max_length, right - left + 1)

    return max_length
