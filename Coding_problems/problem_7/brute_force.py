def find_max_xor(nums):
    max_xor = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            max_xor = max(max_xor, nums[i] ^ nums[j])
    
    return max_xor

# Example usage
nums = [3, 10, 5, 25, 2, 8]
print(find_max_xor(nums))  # Output: 28
