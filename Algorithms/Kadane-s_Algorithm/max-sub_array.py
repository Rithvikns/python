def maxsubarray(arr):
  max_sum = float(-'inf')
  current_sum = 0

  for num in arr:
    current_sum = max(current_sum , current_sum + num)
    max_sum = max(max_sum , current_sum)
  return max_sum
