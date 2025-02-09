def max_subarray_sum_brute_force(arr):
    """
    Function to find the maximum sum of a contiguous subarray using brute-force approach.
    
    :param arr: List of integers (positive and negative)
    :return: Maximum sum of contiguous subarray
    """
    n = len(arr)
    max_sum = float('-inf')

    # Generate all subarrays
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed

    return max_sum
