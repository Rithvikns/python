from collections import deque

def max_sliding_window(num_arr , k):
    n = len(num_arr)
    if n*k ==0:
        return []
    if k == 1:
        return num_arr
    max_arr = []
    dq = deque()

  # iterate through all the objects in the array
    for i in range(n):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and num_arr[dq[-1]] < num_arr[i]:
            dq.pop()
        dq.append(i)
        if i>= k-1:
            max_arr.append(num_arr[dq[0]])
    return max_arr

input_arr = [1,3,5,-2,-6,9]
print(max_sliding_window(input_arr , 3))
