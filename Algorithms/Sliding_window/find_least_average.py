def least_average(inp_arr , k):
  n = len(inp_arr)
  if k > n:
    return -1
  current_sum = sum(inp_arr[0:k])
  min_sum = current_sum
  min_index = 0
  for i in range(1 , i-k +1):
    current_sum = current_sum - inp_arr[i-1] + inp_arr[i+k -1]
    if current_sum < min_sum:
      min_sum = current_sum
      min_index = i
  return min_index
