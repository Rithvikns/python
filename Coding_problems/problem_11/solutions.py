def solve_problem(gas,prices):
  remaining,prev_remaining,start = 0,0,0
  for i in range(len(gas)):
    remaining = gas[i] - prices[i]
    if remaining < 0:
      prev_remaining += remaining
      start = i+1
      remaining = 0
 if start == len(gas) and (prev_remaining + remaining < 0):
   return -1
 else:
   return start


gas = [1,5,3,3,5,3,1,3,4,5]
prices = [5,2,2,8,2,4,2,5,1,2]

#output = 8
